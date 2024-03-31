#!/bin/bash

set -euo pipefail

(cd package && python -m build --sdist)