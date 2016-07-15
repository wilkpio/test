################################################################################
#
#  MODULE NAME: $Id$
#
#  DESCRIPTION:  The description
#
#  MODIFICATION HISTORY:
#
#    DATE      PROG.
#  DD-MMM-YYYY INIT.   SIR    MODIFICATION DESCRIPTION
#  ----------- ------- ------ --------------------------------------------------
################################################################################

cmake_minimum_required( VERSION 2.6 )
project( example )
find_package (PythonLibs REQUIRED)
find_package (PythonInterp REQUIRED)

#------------------------------------------------------------------------------
# Package section
#------------------------------------------------------------------------------
add_custom_target(package COMMAND ${CMAKE_COMMAND} -E echo "INFO: This module do not provide any documentation file" VERBATIM)
#------------------------------------------------------------------------------
# Doc section
#------------------------------------------------------------------------------
add_custom_target(doc COMMAND ${CMAKE_COMMAND} -E echo "INFO: This module do not provide any documentation file" VERBATIM)
#------------------------------------------------------------------------------
# test section
#------------------------------------------------------------------------------
add_custom_target(test)


