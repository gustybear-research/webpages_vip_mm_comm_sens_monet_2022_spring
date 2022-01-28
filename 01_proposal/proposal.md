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

---

# Abstract

Vehicular communication in the millimeter wave (mmWave) band has been recently proposed to realize multi-Gbps data rates and support future intelligent transportation systems (ITS) [1]. Today, radar sensors are used in ITS in some advanced vehicles to scan surrounding and detect the object due to its sensitivity regardless of the environment. Recently, scholars’ attention focuses on the concept of LOS (Line-of-Sight) MIMO ( Multiple-input Multiple-output) for antennas in radar sensors due to the striking feature of maximum received power over the direct LOS path and a multiplicity of DOFs[2]. However, the challenge on the application of this concept is that propagating waves is difficult to distinguish between transmitters. Most recent studies established that if the antenna spacing is suitably set, the LOS MIMO concept can be successfully applied in the sensing system in vehicles. This paper discusses the concept of LOS MIMI in Vehicular communication and proposes the research on finding the best receivers’ distance with known distance between each pair of transmitter and receiver, distance between each transmitter, quantity of antennas, and wavelength.

# Introduction

As the communications industry accelerates in technological advancement, new and refined approaches to information system management are required to continue the field’s progression. A crucial area of this development involves millimeter-wave (mmWave) sensing technology, which allows highly accurate communication in a range of applications including autonomous driving and drone guiding. In this territory, the Multiple-Input Multiple-Output paradigm has emerged as an effective format to organize systems of transmitters and receivers. This research project intends to design a MIMO-modeled system which integrates mmWave signal transmission with embedded radar sensing. An important challenge to this goal involves the Signal to Noise Ratio (SNR) exacerbated by additional information streams in the mmWave spectrum, diminishing the overall coherence of signal transmission. This project seeks to leverage non-Line of Sight (nonLOS) multipath propagation to this end, and ultimately to design a MIMO communication network with enhanced radar integration that minimizes the SNR of such a system. 

# Motion of mmWave MIMO For Vehicular Communication

In mmWave MIMO communication, a phased array is used to concentrate the wave in a particular direction. A reflective surface is also used to propagate the signal in a way that assists the receiver antenna to differentiate between the different transmitters. This differentiation between signals is important in the context of vehicular communication, as these different signals would end up being different information from various sensors within the car. 

# Theoretical Understanding of LoS mmWave MIMO 

For our specific implementation, we are aiming to achieve high bandwidth sensor communication between cars. Line-of-sight, or LOS propagation was the traditional method of signal transmission between a transmitter and receiver, and allowed for coherence and maximum power. However, just LOS transmission by itself comes with a drawback: The closeness of individual transmitters will affect the overall degree of freedom of the system [1]. If the transmitters are not a sufficient distance apart from each other, the individual signals will sum into one general signal that the receivers will see. 
	MIMO counters the loss of DOF by employing multiple transmitters and receivers that are spaced in such a way that allows the receivers to differentiate between the transmitters, effectively increasing the overall resolution of the data. However this strategy is also flawed in that it produces a much lower power wave across transmission. 
The signal-to-noise ratio (SNR)  affects the effectiveness of the antenna geometry. Thus, the spacing of the antennas must change when the SNR is variable in the environment. With MIMO however, spacing of the antenna layout can also be emulated by changing the relative orientation of the transmitters and receivers. 

# Proposed Evaluation

To evaluate the effectiveness of MIMO in an optimal arrangement of transmitters and receivers, we will perform several experiments involving the use of a 2x2 channel array with transmitter and receiver antennas. The transmitter and receiver will be powered by 2 computers, with the transmitter using a phase array to continuously beam-form a signal across the distance from transmitter to receiver. A Windows PC will be used to move the transmitter and receiver antenna, as well as collect the CSI, or Channel State Information that allows us to calculate the signal conditions from transmitter to receiver, which will tell us the optimal positions for the antennas and the reflector surface.  
	Rayleigh's Criterion tells us about the distinguishability of a signal. If the distance between transmitters is such that the following equation is true:

<img src=" ">

then the resultant vectors in the channel matrix come out to be orthogonal.
When transmitters send signals simultaneously, there is a challenge for the receivers to distinguish each signal. Since there is a linear relationship between the signal's parameters, finding the “matrix” (pre-setup scalar) for the computer will help receivers to identify which transmitter the signal is from. 

# Conclusion

Currently and in the future, there will be more connected devices and more wireless needs. Understanding how to build and implement a MIMO based system will allow for further advancement in wireless communications leading to high frequency, high bandwidth, wireless communications on the commercial and consumer level. In order to be able to achieve MIMO communications, for the purpose of car to car communications, this research aims to build a physical testbed based on LOS and multipath communication models with minimal opportunity for scattering. The test bed will then be used to find D_Rx, the distance between the antennas in the receiving array that will lead to high rank support for MIMO communications. Each D_Rx will be tested and optimal configuration for MIMO communications support will be determined. This research aims to expand understanding and implementation of MIMO communications further widening its functions in car to car communications and to more industries and uses. 

# References

[1] Haejoon Jung, In-Ho Lee, "Secrecy Performance Analysis of Analog Cooperative Beamforming in Three-Dimensional Gaussian Distributed Wireless Sensor Networks", Wireless Communications IEEE Transactions on, vol. 18, no. 3, pp. 1860-1873, 2019.
[2] Angel Lozano, “Old Theory Up to New Tricks Issue 25 Aug 2021” in IEEE Community Society,  Jan. 2022. [Online]. Available: https://www.comsoc.org/publications/ctn/old-theory-new-tricks

