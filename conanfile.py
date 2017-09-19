from conans import ConanFile, tools, os

class BoostDllConan(ConanFile):
    name = "Boost.Dll"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-dll"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["dll"]
    requires =  "Boost.Config/1.65.1@bincrafters/stable", \
                      "Boost.Core/1.65.1@bincrafters/stable", \
                      "Boost.Filesystem/1.65.1@bincrafters/stable", \
                      "Boost.Function/1.65.1@bincrafters/stable", \
                      "Boost.Move/1.65.1@bincrafters/stable", \
                      "Boost.Mpl/1.65.1@bincrafters/stable", \
                      "Boost.Predef/1.65.1@bincrafters/stable", \
                      "Boost.Smart_Ptr/1.65.1@bincrafters/stable", \
                      "Boost.Spirit/1.65.1@bincrafters/stable", \
                      "Boost.Static_Assert/1.65.1@bincrafters/stable", \
                      "Boost.System/1.65.1@bincrafters/stable", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/stable", \
                      "Boost.Type_Index/1.65.1@bincrafters/stable", \
                      "Boost.Type_Traits/1.65.1@bincrafters/stable", \
                      "Boost.Winapi/1.65.1@bincrafters/stable"

                      #config0 core2 filesystem8 function5 move3 mpl5 predef0 smart_ptr4 spirit11 static_assert1 system3 throw_exception2 type_index5 type_traits3 winapi1
                      
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()