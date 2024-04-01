from cx_Freeze import setup, Executable
setup(
    name = "CLOSE",
    version = "beta",
    description = "Application for closing",
    exectables = [Executable('exe.py')]
)