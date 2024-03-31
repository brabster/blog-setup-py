# Exploring Python `setup.py` Risks

## Package Setup

Directory [package](./package) contains a minimal Python package, with print statements to illustrate sites for malicious code.

- [setup.py](./package/setup.py) contains a "malicious" print that runs on source dist install
- [mypackage/example.py](./package/src/mypackage/example.py) contains a "malicious" print that runs on package import

[build_package.sh](./build_package.sh) contains the command to build the package as a source distribution.

## Simple Installation in Victim Project

Safety first - make sure we don't install anything in system Python

`export PIP_REQUIRE_VIRTUALENV=true`

Basic install with update and forcing a reinstall even if cached

- `cd victim`
- `python -m venv venv`
- `. venv/bin/activate`
- `pip install -U --force-reinstall ../package/dist/demo-package-1.0.0.tar.gz`

```console
$ pip install -U --force-reinstall ../package/dist/demo-package-1.0.0.tar.gz

Processing /home/paul/projects/brabster/example_package_brabster/package/dist/demo-package-1.0.0.tar.gz
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: demo-package
  Building wheel for demo-package (pyproject.toml) ... done
  Created wheel for demo-package: filename=demo_package-1.0.0-py3-none-any.whl size=1398 sha256=11cd9416764e4b75efd0a18c96511a012f193ec1bcb2f0f9141743593cb64470
  Stored in directory: /home/paul/.cache/pip/wheels/b9/b8/6c/0a18813c919677d4ed10c57f8b8d9fc45674336576166c28f8
Successfully built demo-package
Installing collected packages: demo-package
  Attempting uninstall: demo-package
    Found existing installation: demo-package 1.0.0
    Uninstalling demo-package-1.0.0:
      Successfully uninstalled demo-package-1.0.0
Successfully installed demo-package-1.0.0
```

## Where's the print?

```console
$ pip install -U -v --force-reinstall ../package/dist/demo-package-1.0.0.tar.gz
Using pip 24.0 from /home/paul/projects/brabster/example_package_brabster/victim/venv/lib/python3.11/site-packages/pip (python 3.11)
Processing /home/paul/projects/brabster/example_package_brabster/package/dist/demo-package-1.0.0.tar.gz
  Running command pip subprocess to install build dependencies
  Collecting setuptools>=43.0.0
    Using cached setuptools-69.2.0-py3-none-any.whl.metadata (6.3 kB)
  Using cached setuptools-69.2.0-py3-none-any.whl (821 kB)
  Installing collected packages: setuptools
  Successfully installed setuptools-69.2.0
  Installing build dependencies ... done
  Running command Getting requirements to build wheel
  Hello, I'm malicious in setup.py
  running egg_info
  writing src/demo_package.egg-info/PKG-INFO
  writing dependency_links to src/demo_package.egg-info/dependency_links.txt
```



