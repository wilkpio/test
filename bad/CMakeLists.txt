################################################################################
#
#  MODULE NAME: $Id$
#
#  DESCRIPTION:  The description
#
#  MODIFICATION HISTORY:
#
################################################################################

cmake_minimum_required( VERSION 2.6 )
project( example )
find_package (PythonLibs REQUIRED)
find_package (PythonInterp REQUIRED)

#------------------------------------------------------------------------------
# test target
#------------------------------------------------------------------------------
add_custom_target(test)


