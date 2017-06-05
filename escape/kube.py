#!/usr/bin/env python

import sys
import subprocess
import time
import json

def exec_in_pod(kubecfg, pod_name, cmd):
    cmd = ["kubectl", "--kubeconfig", kubecfg, "exec", "-i", pod_name, "--"] + cmd
    try:
        return subprocess.check_output(cmd)
    except subprocess.CalledProcessError, e:
        print "Kubectl returned with a non-zero status: ", e
        print e.output
        sys.exit(1)


def wait_for_ready_pod(kubecfg, app):
    cmd = ["kubectl", "--kubeconfig", kubecfg, "get", "pods", "-l", "app=" + app, "-o", "json"]
    tries = 1
    max_tries = 10
    sleep_time = 10
    while True:
        print "Waiting for pod matching 'app=%s' to become ready %d/%d" % (app, tries, max_tries)
        sys.stdout.flush()
        try:
            kube_resp = subprocess.check_output(cmd)
        except subprocess.CalledProcessError, e:
            print "Kubectl returned with a non-zero status: ", e
            print e.output
            sys.exit(1)

        if kube_resp == "":
            print "Empty kubectl response"
            tries += 1
            if tries == max_tries:
                print "Maximum tries exceeded."
                sys.exit(1)
            time.sleep(sleep_time)
            continue

        try:
            kube_json_resp = json.loads(kube_resp)
        except Exception, e:
            print "Failed to parse kubectl response as JSON."
            print "Response:"
            print kube_resp
            print "Error:"
            print e
            sys.exit(1)
        result = _get_ready_pod(kube_json_resp)
        if result is not None:
            return result
        tries += 1
        if tries == max_tries:
            print "Maximum tries exceeded."
            sys.exit(1)
        sys.stdout.flush()
        time.sleep(sleep_time)

def _get_ready_pod(kube_json_resp):
    if 'items' not in kube_json_resp:
        return
    items = kube_json_resp['items']
    for item in items:
        if 'status' not in item:
            continue
        status = item['status']
        if 'conditions' not in status:
            continue
        conditions = status['conditions']
        for c in conditions:
            if c['type'] != 'Ready':
                continue
            if c['status'] == 'True':
                return item

