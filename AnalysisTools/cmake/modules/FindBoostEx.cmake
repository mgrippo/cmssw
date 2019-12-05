find_file(scram_path "scram")
if(scram_path)
    execute_process(COMMAND scram tool info boost OUTPUT_VARIABLE SCRAM_BOOST_INFO)
    string(REGEX MATCH "\nINCLUDE=([^\n]*)" BOOST_STR ${SCRAM_BOOST_INFO})
    set(Boost_INCLUDE_DIRS "${CMAKE_MATCH_1}")
    string(REGEX MATCH "\nLIBDIR=([^\n]*)" BOOST_STR ${SCRAM_BOOST_INFO})
    set(Boost_LIBRARY_DIRS "${CMAKE_MATCH_1}")

    set(Boost_LIBRARIES)
    foreach(comp ${BoostEx_FIND_COMPONENTS})
        find_library(Boost_${comp}_LIBRARY "boost_${comp}" PATHS ${Boost_LIBRARY_DIRS} NO_DEFAULT_PATH)
        if(Boost_${comp}_LIBRARY)
            list(APPEND Boost_LIBRARIES ${Boost_${comp}_LIBRARY})
            list(REMOVE_ITEM BoostEx_FIND_COMPONENTS ${comp})
        elseif(Boost_FIND_REQUIRED_${comp})
            message(FATAL_ERROR "Unable to find the requested Boost library 'boost_${comp}'.")
        endif()
    endforeach()
else()
    find_package(Boost REQUIRED COMPONENTS ${BoostEx_FIND_COMPONENTS})
endif()
