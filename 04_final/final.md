---
title: "Final Design Report"
date: 2022-01-13
type: book
commentable: true

# Provide the name of the presenter
# summary: "Provide one or two sentences to describe the final design."
summary: "This final design report discusses our testbench procedure and hardware/software requirements, and documents our current findings on LoS MIMO"

# Provide other tags that describe the paper
tags:
- autonomous vehicle
- v2x
- multipath
- phased array
- reconfigurable MIMO
- rayleigh's criterion
- intelligent reflecting surface
- fresnel zone analysis

weight: 04
---

# Executive Summary

Cooperative driving can be defined as technology used to coordinate groups of vehicles to improve efficiency and safety. For vehicles to effectively communicate with each other, a large data stream bandwidth is needed for all the necessary sensor data that are used in modern cars. Our current standard is the sub-6GHz range, which does not supply a large enough bandwidth for all this data. We propose the use of mmWave technology, which can supply a data stream bandwidth within the 32GHz range. However, this technology comes with some drawbacks, such as strong attenuation and lack of signal coherence over long distances. The use of MIMO and LoS techniques can give us maximum power while maintaining multiple degrees-of-freedom in our signal transmission.

# Introduction

# Background

# Methodology

# Implementation and Experimentation

A network analyzer will be used to generate a low freq signal that will be used as our test signal. The test signal will then be sent to a frequency converter to convert the low frequency signal to a high frequency signal. The high frequency signal will then be sent using the sending antenna (TX) over a channel. (The channel being the wireless airspace between antennas. The high freq signal will then be received by the RX antenna, converted back down to a low frequency signal to be received by the network analyzer. A network analyzer will then be used to display, process and evaluate the results of the test signal. Labview will be responsible for storing the csi to a folder location on a pc

# Results and Analysis

# Conclusion (Nikki is still editing)

Understanding how to build and implement a MIMO based system will allow for further advancement in wireless communications leading to high frequency, high bandwidth, wireless communications on the commercial and consumer level. In order to be able to test LOS MIMO communications, for the purpose of car-to-car communications, this research aimed to build a physical testbed based on LoS and multipath communication models with minimal opportunity for scattering. The testbed will then be used to find D_Rx, the distance between the antennas in the receiving array that will lead to high-rank support for MIMO communications. Each D_Rx will be tested and optimal configuration for MIMO communications support will be determined. This research aims to expand understanding and implementation of MIMO communications further widening its functions in car-to-car communications and to more industries and uses.

# Appendix
