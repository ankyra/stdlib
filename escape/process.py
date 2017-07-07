import path
import os
import subprocess

class OutputRecorder(object):

    def run_script(self, cmd, env = None, log_prefix = None):
        path.make_executable(cmd[0])
        log_string = cmd[0] if log_prefix is None else log_prefix
        stdout, return_code = self.record(cmd, log_string, env)
        if return_code != 0:
            raise Exception("%s script exited with a non-zero exit code" % log_prefix)
        return stdout

    def record(self, cmd, log_string, env=None):
        env = os.environ if env is None else env
        proc = subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout = []
        line = proc.stdout.readline()
        while line:
            stdout.append(line.strip())
            print "%s:" % log_string, line.strip()
            line = proc.stdout.readline()
        return stdout, proc.wait()
