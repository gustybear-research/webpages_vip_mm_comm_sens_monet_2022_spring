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

Cooperative driving technology can be used to alleviate congestion and reduce traffic incidents on the road. For vehicles to effectively communicate with each other, a large data stream bandwidth is needed for all the necessary sensor data that are used in modern cars. Our current standard is the sub-6GHz range, which does not supply a large enough bandwidth for all this data. We propose the use of mmWave technology, which can supply a data stream bandwidth within the 32GHz range. The use of MIMO and LoS techniques can give us maximum power while maintaining multiple degrees-of-freedom in our signal transmission.

# Introduction

 Cooperative driving can be defined as technology used to coordinate groups of vehicles to improve efficiency and safety. As modern cars are equipped with more and more sensors that track details within and outside the car, we can utilize this sensor data to effectively communicate with other vehicles to coordinate driving, which is another step toward autonomous vehicles. The main issue that prevents wireless communication between vehicles is the lack of usable bandwidth with standard communication technology. With mmWave technology, we have the bandwidth required to communicate all the sensor data.  However, this technology comes with some drawbacks, such as strong attenuation and lack of signal coherence over long distances. 

# Background
Picture an array of antennas, where the transceiver has multiple outputs and the receiver has multiple inputs. Multiple Input Multiple Output (MIMO) is another form of communication. What makes MIMO desirable is that it thrives in a rich scattering environment and it has multiple degrees of freedom. This includes many paths from transmitter to recevier. The paths also vary in which they can be direct, have multiple bounce reflections, diffract, or scatter. This form of communication is not without drawbacks. Depending on the distances between each antenna, the desired input may not reach the desired output. For example, if antenna A is trying to reach antenna B, if the spacing is not adequate, antenna B may receive antenna C's signal, or antenna D may receive antenna A's signal. Additionally, MIMO signals are not suitable for long distance propagation. If the distance is too large, the signal is prone to attenuation and could result in either sending insufficient data, or lose the signal all together.
Line of Sight (LoS) is a method whose definition is given in the name. LoS is a method in which the transceiver and receiver are directly within each other's line of sight. This allows for the most power transmitted through the receiver. However, the drawback to using this technique is that it is not flexible. LoS technology cannot thrive in a rich scattering environment. LoS is limited by its one degree of freedom.

Our solution is to combine both of these technologies and create LoS mmWave MIMO. This way, we can have the reliability of LoS, with the flexibility of MIMO. This can be acheived with antena separation, but the antenna separations need to be scaled with the wavelength. To achieve this combination, it must tackled with a geometric approach. The key to achieving this goal is arrays. For high signal to noise ratio (SNR) applications, each antenna can be treated as its own DOF with equal strength. This is done by correctly spacing the antennas and a curved wavefront. For low SNR applications, it is optimal to concentrate the power on a single DOF via beamforming and by using a planar wavefront. For immediate SNR applications, we can use a combination of the two aforementioned methods; using both planar and curved wavefronts. The antennas can also be configured as subarrays within the arrays. If the antennas need to be kept in a single array, the spacing must be adjusted as a function of the SNR. However, this poses a challenge. What if the SNR is not fixed? Would the antennas need to be mechanically rearranged to fit the SNR? Luckily, they do not. If the SNR changes, the orientation of the transmit and receive arrays needs to be changed. For linear arrays, we are concerned with the projection of one on the direction of the other. The spacings for the antennas on that direction shrink with the cosine of the relative angle. In other words, by rotating the antenna array, we can adjust for different SNR. If the SNR is low, the arrays should almost be orthogonal, for high SNR, the arrays should be extensions of each other, or collinear.


# Methodology
A network analyzer will be used to generate a low frequency signal that will be used as our test signal. The test signal will then be sent to a frequency converter to convert the low frequency signal to a high frequency signal. The high frequency signal will then be sent using the sending antenna (TX) over a channel. The channel being the wireless airspace between the TX and RX antennas. The high frequency signal will then be received by the RX antenna and converted back down to a low frequency signal to be received by the RX port of the network analyzer. The network analyzer will then be used to display, process and evaluate the results of the test signal. A computer interface, Labview, will be responsible for storing the CSI to a folder location on a PC.

# Implementation and Experimentation

# Results and Analysis

# Conclusion 

Understanding how to build and implement a MIMO based system will allow for further advancement in wireless communications leading to high frequency, high bandwidth, wireless communications on the commercial and consumer level. In order to be able to test LOS MIMO communications, for the purpose of car-to-car communications, this research aims to build a physical testbed based on LoS and multipath communication models with minimal opportunity for scattering. The testbed will then be used to find D_Rx, the distance between the antennas in the receiving array that will lead to high-rank support for MIMO communications. Each D_Rx will be tested and optimal configuration for MIMO communications support will be determined. This research aims to expand understanding and implementation of LOS MIMO communications further widening its functions in car-to-car communications.

# Appendix
