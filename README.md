# Escape stdlib

This is a Python library that you can import in your build, deployment and
errand scripts to make it slightly easier to get variables in and out of Escape
and perform common tasks such as executing a script in a Kubernetes pod.  This
library is mainly used by Ankyra itself to produce releases.

* [Escape Documentation](https://escape.ankyra.io/docs/)
* [Escape client](https://github.com/ankyra/escape)

## Usage

Here's an example from the [extension-docker](https://github.com/ankyra/extension-docker):

```
name: extension-docker
version: 0.5.@
logo: logo.png
description: ...

depends:
- stdlib-latest

build: build_and_push_image.py

```

The release depends on stdlib like a regular Escape package, which means that
it gets downloaded and unpacked (under `./deps/_/stdlib`) at build and deploy
time - if it's not already there. Because Python won't regularly search this
path, we need to make sure to tell Python about it before we can finally import
the `escape` library:

```
#!/usr/bin/env python

import json
import os
import subprocess

import sys
sys.path = ["deps/_/stdlib"] + sys.path
import escape

docker_image = escape.get_string_input('docker_image')
docker_image_version = escape.get_string_input('docker_image_version')
```
We agree this is not the most elegant solution, but we didn't want to mess 
with the user's python path. If this is not a concern you can install the library 
into a proper place using a `pre_build` and `pre_deploy` step.

## License

```
Copyright 2017, 2018 Ankyra

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
