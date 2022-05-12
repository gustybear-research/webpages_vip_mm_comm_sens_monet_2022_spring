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

Cooperative driving technology can be used to alleviate congestion and reduce traffic incidents on the road. For vehicles to effectively communicate with each other, an extremely large data stream bandwidth is needed for all of the necessary sensor data that are used in modern cars. The current IEEE standard operates in a range less than 6 GHz, which does not supply a large enough bandwidth for all of this required data. The aim of this project is to design a millimeter-wave (mmWave) communication system with integrated radar sensing capabilities. As a promising technology, radio communication at mmWave frequencies, particularly between 24 to 32 GHz, can meet the data rate demand of future generations of wireless networks. 

Unfortunately, the mmWave bands are often used by short-range radar sensors essential for applications such as autonomous vehicles and remote healthcare. Introducing a separate communication system in these bands would lead to extra congestion in this spectrum of frequencies, leading to suboptimal performance for both communication and sensing. To address this issue, MONET aims to unify mmWave radar and communication functions via the multiple-input and multiple-output (MIMO) technique augmented by reconfigurable reflective arrays to achieve reliable communication and accurate radar sensing. Coupling mmWave technology with MIMO and other techniques such as the line-of-sight (LoS) method can give us maximum power while maintaining multiple degrees of freedom in our signal transmission.

# Introduction

Cooperative driving is a concept based largely on the highly experimental proposition of self-driving cars. More specifically, however, cooperative driving can be defined as technology used to coordinate groups of vehicles to improve efficiency and safety. As modern cars are equipped with more and more sensors that track details within and outside the car, we can utilize this sensor data to effectively communicate with other vehicles to coordinate driving, with all vehicles simultaneously moving together as a cohesive unit. This is yet another step toward autonomous vehicles. Ideally, this technology results in less traffic congestion, lower travel times, and less traffic accidents and collisions. Vehicles are to be made aware of pedestrians, other vehicles, traffic signals, and any other obstacles in their proximity via data transmission and reception, increasing safety in both private and public transportation.

The main issue that prevents wireless communication between vehicles is the lack of usable bandwidth with standard communication technology. With around a billion cars on the road and in production on the planet, along with countless objects in these vehicles’ environments, extensive bandwidths of data are required in order for intelligent communication between cars and other objects to be remotely possible. Given the real-time nature of moving vehicles in transportation, current transmission standards are too slow to communicate sensory data in time. IEEE 802.11p, the standard to add wireless access in vehicular environments (WAVE), otherwise known as vehicular communication systems, only operates around the 5.9 GHz range, which is not nearly wide enough for all intents and purposes.

# Background

Our core proposition to solve the issue of lacking bandwidth is the notion of millimeter-wave (mmWave) technology. This powerful advancement extends the capabilities of our current data rate; and since the signal waves are in the millimeter range, they operate in between the frequencies of 24 and 32 GHz. The formerly popular 4G broadband cellular network technology runs in the 6 GHz range—closely similar to the IEEE standard—while mmWave resides in the lower end of the 5G broadband spectrum, which begins at 24 GHz. This vast bandwidth is what makes 5G significantly more powerful than 4G. Technology involving the mmWave technique has already found places in the domains of remote healthcare and radar sending, and we believe it has great potential in the realm of vehicular communication.

One of the main problems with mmWave, however, is that it often experiences strong attenuation and a lack of signal coherence over long distances. With the wavelengths of these signals being very short, maintaining their strength across great ranges—between cars along stretches of freeway, for instance—proves to be difficult. Therefore, we theorize that including the approach of multi-input multi-output (MIMO) transmission may increase functionality. This leads to the differentiation of multiple signals and permits the existence of two or more data streams within the same space. For instance, a primitive cellular phone may be able to function within reason by using a single-input, single-output (SISO) antenna to transmit data signals. Although, implementation of a MIMO antenna recognizes the transmission of multiple data streams at once. The latter is vastly standard in today’s modern devices, with many popular brands supporting 4×4 MIMO, which utilizes four transmitters and four receivers for data streaming.

In order to envision a MIMO system, one should picture an array of antennas, with a row of transmitters on one side and a row of an equal number of receivers on the other. What makes MIMO desirable is that it thrives in a rich scattering environment and has multiple degrees of freedom. This includes many paths between transmitters and receivers. For instance, Transmitter A does not have to correspond to Receiver B. Depending on the scenario, it may choose to correspond to Receiver D or F instead. The paths also vary in which they can be direct, have multiple bounce reflections, diffract, or scatter.

This form of communication is not without drawbacks, however. Depending on the distances between each antenna, the desired input may not reach the desired output. For example, if Antenna A is trying to reach Antenna B, if the spacing is not adequate, Antenna B may receive Antenna C's signal, or Antenna D may receive Antenna A's signal. Additionally, MIMO signals are not suitable for long-distance propagation. If the distance is too large, the signal is prone to attenuation and could result in either sending insufficient data, or losing the signal altogether.

The previously described cases occur because MIMO is bounded by an equation known as the Rayleigh Criterion. In this statement, the distance between rows of transmitters and receivers, D, is directly proportional to the product of the distance between consecutive transmitters, d_TX, and the distance between consecutive receivers, d_RX. This means that, for a particular combination of distances, a MIMO system may function with optimal values; but as soon as one parameter is altered too much, one signal may be confused for another or attenuation may occur. In the context of moving vehicles: if the transmitters on Car A and receivers on Car B are adequately spaced, they may be able to properly detect each other; but as soon as the distance between the vehicles changes, undesirable signal relay results may occur, perhaps with the vehicles appearing nearly invisible to the other. Fluctuations between the orientation of transmitters and receivers on even a single vehicle can make MIMO adaptation to vehicular communication arduous.

In order to assist MIMO technology, Line of Sight (LoS) is also being explored. This is a method whose definition is given in the name. In this, the transceiver and receiver are directly within each other's line of sight. This allows for the most power transmitted through the receiver. However, the drawback to using this technique is that it is not flexible. LoS technology cannot thrive in a rich scattering environment, and is limited by having only one degree of freedom.

Our solution is to combine both of these technologies with mmWave techniques and create LoS mmWave MIMO. This way, we can have the reliability of LoS with the flexibility of MIMO. This can be achieved with antenna separation, but the antenna separations need to be scaled with the wavelength. To achieve this combination, it must be tackled with a geometric approach. The key to achieving this goal is arrays. For high signal-to-noise ratio (SNR) applications, each antenna can be treated as its own degree of freedom (DOF) with equal strength. This is done by correctly spacing the antennas to create a curved wavefront. For low SNR applications, it is optimal to concentrate the power on a single DOF via beamforming and by using a planar wavefront. For immediate SNR applications, we can use a combination of the two aforementioned methods - using both planar and curved wavefronts. The antennas can also be configured as subarrays within the arrays. If the antennas need to be kept in a single array, the spacing must be adjusted as a function of the SNR.

However, this poses a challenge. What if the SNR is not fixed? Would the antennas need to be mechanically rearranged to fit the SNR? Luckily, they do not. If the SNR changes, the orientation of the transmitter and receiver arrays needs to be changed. For linear arrays, we are concerned with the projection of one in the direction of the other. The spacings for the antennas in that direction shrink with the cosine of the relative angle. In other words, by rotating the antenna array, we can adjust for different SNR. If the SNR is low, the arrays should almost be orthogonal, for high SNR, the arrays should be extensions of each other, or collinear.

# Methodology

A network analyzer will be used to generate a low frequency signal that will be used as our test signal. The test signal will then be sent to a frequency converter to convert the low frequency signal to a high frequency signal. The high frequency signal will then be sent using the sending antenna (TX) over a channel. The channel being the wireless airspace between the TX and RX antennas. The high frequency signal will then be received by the RX antenna and converted back down to a low frequency signal to be received by the RX port of the network analyzer. The network analyzer will then be used to display, process and evaluate the results of the test signal. A computer interface, Labview, will be responsible for storing the CSI to a folder location on a PC.

# Implementation and Experimentation

# Results and Analysis

# Conclusion 

Understanding how to build and implement a MIMO based system will allow for further advancement in wireless communications leading to high frequency, high bandwidth, wireless communications on the commercial and consumer level. In order to be able to test LOS MIMO communications, for the purpose of car-to-car communications, this research aims to build a physical testbed based on LoS and multipath communication models with minimal opportunity for scattering. The testbed will then be used to find D_Rx, the distance between the antennas in the receiving array that will lead to high-rank support for MIMO communications. Each D_Rx will be tested and optimal configuration for MIMO communications support will be determined. This research aims to expand understanding and implementation of LOS MIMO communications further widening its functions in car-to-car communications.

# Appendix
