# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

include(GrPython)

if(ENABLE_TESTING)
    GR_PYTHON_CHECK_MODULE_RAW(
        "pytest"
        "import pytest"
        PYTEST_FOUND
    )

    if(PYTEST_FOUND)
        set(GRC_BLOCKS_PATH
            ${CMAKE_CURRENT_SOURCE_DIR}/../blocks
            ${CMAKE_CURRENT_SOURCE_DIR}/../tests/resources
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-analog/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-audio/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-blocks/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-channels/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-digital/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-dtv/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-fec/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-fft/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-filter/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-qtgui/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-trellis/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-uhd/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-video-sdl/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-vocoder/grc
            ${CMAKE_CURRENT_SOURCE_DIR}/../../gr-zeromq/grc)
        string(REPLACE ";" ":" GRC_BLOCKS_PATH "${GRC_BLOCKS_PATH}")

        set(GR_TEST_ENVIRONS "GRC_BLOCKS_PATH=\"${GRC_BLOCKS_PATH}\"")
        GR_ADD_TEST(grc_tests ${QA_PYTHON_EXECUTABLE} -B -m pytest ${CMAKE_CURRENT_SOURCE_DIR})
    endif()
endif(ENABLE_TESTING)
