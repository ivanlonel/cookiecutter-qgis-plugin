import sys


def check_package_name() -> None:
    package_name = "{{ cookiecutter.plugin_package }}"

    if not package_name.isidentifier():
        print(
            f"ERROR: The plugin package name ({package_name}) is not a valid "
            "Python package. Please do not use a - and use _ instead"
        )

        # Exit to cancel project
        sys.exit(1)


def check_license() -> None:
    if "{{ cookiecutter.license }}".lower() not in ("gpl2", "gpl3"):
        print("QGIS plugins must comply with the GPL version 2 or greater license.")
        sys.exit(1)


def main() -> None:
    check_package_name()
    check_license()


if __name__ == "__main__":
    main()
