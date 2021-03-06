
from conans import ConanFile, CMake, tools
import os

class AtomsConan(ConanFile):
    name = "Atoms"
    user = "aev25"
    version = "0.1.0"
    channel = "stable"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    

