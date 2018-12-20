#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostDllConan(base.BoostBaseConan):
    name = "boost_dll"
    url = "https://github.com/bincrafters/conan-boost_dll"
    lib_short_names = ["dll"]
    header_only_libs = ["dll"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_filesystem",
        "boost_function",
        "boost_move",
        "boost_mpl",
        "boost_predef",
        "boost_smart_ptr",
        "boost_spirit",
        "boost_static_assert",
        "boost_system",
        "boost_throw_exception",
        "boost_type_index",
        "boost_type_traits",
        "boost_winapi"
    ]
