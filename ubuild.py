import os
import sys
import uranium


uranium.current_build.config.set_defaults({
    "package_name": "setuptools-cmmi",
    "module": "setuptools_cmmi",
    "test_packages": {
        "mock": None,
    },
})

def main(build):
    build.packages.install(".", develop=True)

    for package, version in build.config.get("additional_packages", {}).items():
        build.packages.install(package, version=version)


def test_packages(build):
    build.packages.versions.update({
        "coverage": "==4.0.1"
    })
    build.packages.install("mock")
    build.packages.install("pytest")
    build.packages.install("pytest-cov")
    build.packages.install("pytest-runfailed")
    for pkg, version in build.config.get(
            "test_packages", {}
    ).items():
        build.packages.install(pkg, version=version)


@uranium.task_requires(test_packages)
def test(build):
    """ run unit tests with pytest. """
    test_root = build.config.get(
        "test_root", os.path.join(build.config.get("module"), "tests")
    )
    # we add our build/bin to the path.
    build.executables.run([
        sys.executable,
        os.path.join(build.root, "bin", "py.test"),
        test_root,
        "--cov", build.config.get("module"),
        "--cov-report", "term-missing"
    ] + build.options.args)
