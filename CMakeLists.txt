################################################################################
#
#  MODULE NAME: $Id$
#
#  DESCRIPTION:  The GTS Build Framework
#
#  MODIFICATION HISTORY:
#
#    DATE      PROG.
#  DD-MMM-YYYY INIT.   SIR    MODIFICATION DESCRIPTION
#  ----------- ------- ------ --------------------------------------------------
#  XX-XXX-XXXX MAJCTOM XXXXXX Initial version
#  20-MAY-2015 WILKPIO 288121 add audit target
################################################################################

cmake_minimum_required( VERSION 2.6 )

project( gts.build )

find_package (PythonLibs REQUIRED)
find_package (PythonInterp REQUIRED)


#------------------------------------------------------------------------------
# Package section
#------------------------------------------------------------------------------
add_custom_target(package
          COMMAND ${CMAKE_COMMAND} -E echo "INFO: This module do not provide any documentation file"
          VERBATIM)
#------------------------------------------------------------------------------
# Doc section
#------------------------------------------------------------------------------
add_custom_target(doc
          COMMAND ${CMAKE_COMMAND} -E echo "INFO: This module do not provide any documentation file"
          VERBATIM)
#------------------------------------------------------------------------------
# test section
#------------------------------------------------------------------------------
add_custom_target(test)

#------------------------------------------------------------------------------
# audit section
#------------------------------------------------------------------------------
add_custom_target(src-audit)


add_custom_target(gen_insure_report)
#------------------------------------------------------------------------------
# Delivery description
#------------------------------------------------------------------------------
configure_file(
                "${CMAKE_SOURCE_DIR}/opt/delivery_info.xml.in"
                "${CMAKE_BINARY_DIR}/delivery_info.xml"
                COPYONLY
            )
