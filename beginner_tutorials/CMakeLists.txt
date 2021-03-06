cmake_minimum_required(VERSION 2.8.3)
project(beginner_tutorials)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  laser_geometry
  occupancy_grid_utils
  PCL
)




include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

## To declare and build messages, services or actions from within this
## package, follow these steps:
## * Let MSG_DEP_SET be the set of packages whose message types you use in
##   your messages/services/actions (e.g. std_msgs, actionlib_msgs, ...).
## * In the file package.xml:
##   * add a build_depend tag for "message_generation"
##   * add a build_depend and a run_depend tag for each package in MSG_DEP_SET
##   * If MSG_DEP_SET isn't empty the following dependency has been pulled in
##     but can be declared for certainty nonetheless:
##     * add a run_depend tag for "message_runtime"
## * In this file (CMakeLists.txt):
##   * add "message_generation" and every package in MSG_DEP_SET to
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * add "message_runtime" and every package in MSG_DEP_SET to
##     catkin_package(CATKIN_DEPENDS ...)
##   * uncomment the add_*_files sections below as needed
##     and list every .msg/.srv/.action file to be processed
##   * uncomment the generate_messages entry below
##   * add every package in MSG_DEP_SET to generate_messages(DEPENDENCIES ...)

## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   Num.msg
   
 )

## Generate services in the 'srv' folder
 add_service_files(
   FILES
  AddTwoInts.srv
 )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )


## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
 )

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

## To declare and build dynamic reconfigure parameters within this
## package, follow these steps:
## * In the file package.xml:
##   * add a build_depend and a run_depend tag for "dynamic_reconfigure"
## * In this file (CMakeLists.txt):
##   * add "dynamic_reconfigure" to
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * uncomment the "generate_dynamic_reconfigure_options" section below
##     and list every .cfg file to be processed

## Generate dynamic reconfigure parameters in the 'cfg' folder
# generate_dynamic_reconfigure_options(
#   cfg/DynReconf1.cfg
#   cfg/DynReconf2.cfg
# )

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES beginner_tutorials
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime geometry_msgs sensor_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a C++ library
# add_library(beginner_tutorials
#   src/${PROJECT_NAME}/beginner_tutorials.cpp
# )

## Add cmake target dependencies of the library
## as an example, code may need to be generated before libraries
## either from message generation or dynamic reconfigure
# add_dependencies(beginner_tutorials ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Declare a C++ executable
# add_executable(beginner_tutorials_node src/beginner_tutorials_node.cpp)

## Add cmake target dependencies of the executable
## same as for the library above
# add_dependencies(beginner_tutorials_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
# target_link_libraries(beginner_tutorials_node
#   ${catkin_LIBRARIES}
# )

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
# install(PROGRAMS
#   scripts/my_python_script
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark executables and/or libraries for installation
# install(TARGETS beginner_tutorials beginner_tutorials_node
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark cpp header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############
find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIRS})
add_definitions(${EIGEN3_DEFINITIONS})

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_beginner_tutorials.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(talker src/talker.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})
add_dependencies(talker beginner_tutorials_generate_messages_cpp)


add_executable(ControlRob src/ControlRob.cpp)
target_link_libraries(ControlRob ${catkin_LIBRARIES})
add_dependencies(ControlRob beginner_tutorials_generate_messages_cpp)

add_executable(scan2pcl src/scan2pcl.cpp)
target_link_libraries(scan2pcl ${catkin_LIBRARIES})
add_dependencies(scan2pcl beginner_tutorials_generate_messages_cpp )

add_executable(scan2pcl2 src/scan2pcl2.cpp)
target_link_libraries(scan2pcl2 ${catkin_LIBRARIES})
add_dependencies(scan2pcl2 beginner_tutorials_generate_messages_cpp )

add_executable(scan2pcl1 src/scan2pcl1.cpp)
target_link_libraries(scan2pcl1 ${catkin_LIBRARIES})
add_dependencies(scan2pcl1 beginner_tutorials_generate_messages_cpp )

add_executable(scan2pcl3 src/scan2pcl3.cpp)
target_link_libraries(scan2pcl3 ${catkin_LIBRARIES})
add_dependencies(scan2pcl3 beginner_tutorials_generate_messages_cpp )

add_executable(scan2pcl4 src/scan2pcl4.cpp)
target_link_libraries(scan2pcl4 ${catkin_LIBRARIES})
add_dependencies(scan2pcl4 beginner_tutorials_generate_messages_cpp )

add_executable(scan2pcl5 src/scan2pcl5.cpp)
target_link_libraries(scan2pcl5 ${catkin_LIBRARIES})
add_dependencies(scan2pcl5 beginner_tutorials_generate_messages_cpp )

add_executable(scan2pcl6 src/scan2pcl6.cpp)
target_link_libraries(scan2pcl6 ${catkin_LIBRARIES})
add_dependencies(scan2pcl6 beginner_tutorials_generate_messages_cpp )

add_executable(scan2pcl7 src/scan2pcl7.cpp)
target_link_libraries(scan2pcl7 ${catkin_LIBRARIES})
add_dependencies(scan2pcl7 beginner_tutorials_generate_messages_cpp )

add_executable(scan2pcl8 src/scan2pcl8.cpp)
target_link_libraries(scan2pcl8 ${catkin_LIBRARIES})
add_dependencies(scan2pcl8 beginner_tutorials_generate_messages_cpp )

add_executable(map_merging src/map_merging.cpp)
target_link_libraries(map_merging ${catkin_LIBRARIES})
add_dependencies(map_merging beginner_tutorials_generate_messages_cpp )

add_executable(merge_occ_grids src/merge_occ_grids.cpp)
target_link_libraries(merge_occ_grids ${catkin_LIBRARIES})
add_dependencies(merge_occ_grids beginner_tutorials_generate_messages_cpp )

add_executable (passthrough src/passthrough.cpp)
target_link_libraries (passthrough ${PCL_LIBRARIES})

add_executable(add_two_ints_server src/add_two_ints_server.cpp)
target_link_libraries(add_two_ints_server ${catkin_LIBRARIES})
add_dependencies(add_two_ints_server beginner_tutorials_gencpp)


