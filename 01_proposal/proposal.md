---
title: "Project Proposal"
date: 2022-01-13
type: book
commentable: true

# Provide the name of the presenter
summary: The project proposal describes the objective and purpose of LoS MIMO communication in vehicles, and how we use an experimental setup to verify optimal spacing arrangements of antennas to effectively employ MIMO in such situations.

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

weight: 01

authors:
- Nikki A. Arakawa
- Jennifer J. Guo
- Desmond Lum
- Adrianna F. Saymo
- Branden L. Tsuji-Jones
- Nicholas A. Ali
- Liam K. Tapper
- Edward B. Maloney
---

# Abstract

Vehicular communication in the millimeter wave (mmWave) band has been recently proposed to realize multi-Gbps data rates and support future intelligent transportation systems (ITS) [1]. Radar sensors are commonly used in ITS for some advanced vehicles to scan surrounding and detect the object due to its sensitivity regardless of the environment. Recently, scholars’ attention focuses on the concept of LOS (Line-of-Sight) MIMO (Multiple-input Multiple-output) for antennas in radar sensors due to the striking features of maximum received power over the direct LOS path and a multiplicity of DOFs[2]. Although this concept improves the sensor’s performance, it is often practically difficult to transmit messages accurately in high frequency. The implementation of LOS MIMO requires exceedingly precise and suitable antenna spacing. Therefore, this focus group aims to investigate suitable spacing between antennas and test LOS MIMO’s performance on communication and sensing for autonomous vehicles. We propose to do simulations in Matlab and HFSS for a set of 2X2 spatial multiplexing antennas at millimeter wave and then evaluate practical performance on a testbed.


# Introduction

The widening application of ITS promises significant advancement of the transportation sector, both in terms of safety and efficiency. ITS have been harnessed in a variety of areas through several generations of transportation infrastructure, but the advent of cooperative driving technologies offers much unexplored territory. While the traditional standard of vehicular communication still relies heavily on user-operation, cooperative driving instead allows vehicles in proximity to each other to share data concurrently across a collective network, thus broadening the information available to each individual vehicle. Although much research and development has been devoted to this field, conditional challenges still frustrate efforts to achieve robust cooperative driving networks in practicality. Specifically, the bandwidth required to accommodate multiple data streams within a vehicular network far exceeds present technological capabilities. Therefore, practical application of cooperative driving must be preceded by further refinement of relevant wireless communication systems. 
	To this end, mmWave transmission is a promising venue for cooperative vehicular communication, owing to its powerful propagation over short distances. The mmWave spectrum ranges from 24 GHz to 300 GHz, though this project will focus primarily on frequencies between 24 to 32 GHz. At such frequencies, the multiple data streams required for cooperative driving theoretically can be supported, though new challenges arise in practice. A network where individual vehicles use radar sensing to ascertain their own surroundings, while simultaneously communicating that information to other vehicles who in turn share their own data would result in great congestion of the overall system spectrum. This reality makes paramount the reduction of the Signal to Noise Ratio (SNR) experienced by a system in order to facilitate optimum signal transmission. Enter the MIMO paradigm, which is oriented to support multiple information streams across an array of transmitters and receivers. The increased DOF offered by such a system is ideal for cooperative driving technology, but accuracy of transmission must also be considered. In mmWave MIMO communication, a phased array is used to concentrate the wave in a particular direction. A reflective surface is also used to propagate the signal in a way that assists the receiver antenna to differentiate between the different transmitters. This differentiation between signals is important in the context of vehicular communication, as these different signals would end up being different information from various sensors within the car. LoS multipath propagation has been standard in MIMO systems, as it ensures maximum received power to maintain signal coherence. LoS propagation also carries limiting factors that must be addressed, particularly that there must be no physical obstruction between the transmitter and receiver. These complications can be mitigated through the strategic placement and spacing of antennas within a MIMO system, ensuring optimal conditions for signal transmission. 
	This research project will explore the design and implementation of a LoS-MIMO communication system as applied to a cooperative driving network. Of particular interest is the placement of antennas within such a system to maximize transmission power while minimizing signal interference. 
 

# Motion of mmWave MIMO For Vehicular Communication

In mmWave MIMO communication, a phased array is used to concentrate the wave in a particular direction. A reflective surface is also used to propagate the signal in a way that assists the receiver antenna to differentiate between the different transmitters. This differentiation between signals is important in the context of vehicular communication, as these different signals would end up being different information from various sensors within the car. 

# Theoretical Understanding of LoS mmWave MIMO (Desmond, Adrianna)

For our specific implementation, we are aiming to achieve high bandwidth sensor communication between cars. Line-of-sight, or LOS propagation was the traditional method of signal transmission between a transmitter and receiver, and allowed for coherence and maximum power. However, just LOS transmission by itself comes with a drawback: The closeness of individual transmitters will affect the overall degree of freedom of the system [1]. If the transmitters are not a sufficient distance apart from each other, the individual signals will sum into one general signal that the receivers will see. 

MIMO counters the loss of DOF by employing multiple transmitters and receivers that are spaced in such a way that allows the receivers to differentiate between the transmitters, effectively increasing the overall resolution of the data. However this strategy is also flawed in that it produces a much lower power wave across transmission. 

The signal-to-noise ratio (SNR)  affects the effectiveness of the antenna geometry. Thus, the spacing of the antennas must change when the SNR is variable in the environment. With MIMO however, spacing of the antenna layout can also be emulated by changing the relative orientation of the transmitters and receivers. 

Rayleigh's Criterion imposes specific distances that we can place our antennas such that multiple DOFs can be achieved. To determine these distances, the waves generated by the signals can be represented as vectors with a direction and magnitude. These channel vectors must be completely orthogonal from each other to achieve multiple DOFs because any projection from one channel vector to another can cause interference in the communicated signals. They are made orthogonal by the phase difference of each wave. Each channel vector in the configuration can be placed in a n x m matrix, which allows us to use mathematical procedures to find the DOF of the configuration itself. The following equation is based off on Rayleigh's criterion and gives the antenna spacing required to fulfill this condition. 

<img src="https://github.com/gustybear-research/webpages_vip_mm_comm_sens_monet_2022_spring/raw/main/01_proposal/images/distance_equation.png">

Note that the number of antenna itself affects the optimal distance, so it is possible to have multiple optimal distances at which multiple DOFs are achieved. 

# Proposed Evaluation

To evaluate the effectiveness of MIMO in an optimal arrangement of transmitters and receivers, we will perform several experiments involving the use of a 2x2 channel array with transmitter and receiver antennas. The transmitter and receiver will be powered by 2 computers, with the transmitter using a phase array to continuously beam-form a signal across the distance from transmitter to receiver. A Windows PC will be used to move the transmitter and receiver antenna, as well as collect the CSI, or Channel State Information that allows us to calculate the signal conditions from transmitter to receiver, which will tell us the optimal positions for the antennas and the reflector surface.  
	
Rayleigh's Criterion tells us about the distinguishability of a signal. If the distance between transmitters is such that the following equation is true:

then the resultant vectors in the channel matrix come out to be orthogonal. 

When transmitters send signals simultaneously, there is a challenge for the receivers to distinguish each signal. Since there is a linear relationship between the signal's parameters, finding the “matrix” (pre-setup scalar) for the computer will help receivers to identify which transmitter the signal is from. 

# Conclusion

Currently and in the future, there will be more connected devices and more wireless needs. Understanding how to build and implement a MIMO based system will allow for further advancement in wireless communications leading to high frequency, high bandwidth, wireless communications on the commercial and consumer level. In order to be able to achieve MIMO communications, for the purpose of car to car communications, this research aims to build a physical testbed based on LOS and multipath communication models with minimal opportunity for scattering. The test bed will then be used to find D_Rx, the distance between the antennas in the receiving array that will lead to high rank support for MIMO communications. Each D_Rx will be tested and optimal configuration for MIMO communications support will be determined. This research aims to expand understanding and implementation of MIMO communications further widening its functions in car to car communications and to more industries and uses. 

# References

[1] Haejoon Jung, In-Ho Lee, "Secrecy Performance Analysis of Analog Cooperative Beamforming in Three-Dimensional Gaussian Distributed Wireless Sensor Networks", Wireless Communications IEEE Transactions on, vol. 18, no. 3, pp. 1860-1873, 2019.

[2] Angel Lozano, “Old Theory Up to New Tricks Issue 25 Aug 2021” in IEEE Community Society,  Jan. 2022. [Online]. Available: https://www.comsoc.org/publications/ctn/old-theory-new-tricks

