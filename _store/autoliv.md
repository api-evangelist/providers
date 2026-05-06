---
aid: autoliv
name: Autoliv
description: Autoliv is the world's largest automotive safety supplier, designing, manufacturing, and selling airbags, seatbelts, steering wheels, inflators, pyrotechnic actuators, and related safety electronics for vehicle manufacturers worldwide. The company operates in 25 countries with 13 technology centers and serves all major OEMs.
url: https://raw.githubusercontent.com/api-evangelist/autoliv/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Automotive
  - Automotive Safety
  - Airbags
  - Seatbelts
  - Safety Systems
  - Manufacturing
apis:
  - aid: autoliv:supplier-portal
    name: Autoliv Supplier Portal
    description: The Autoliv Supplier Portal (autoliv.biz) provides suppliers and partners with access to procurement, logistics, and collaboration tools for doing business with Autoliv. It enables supplier onboarding, document exchange, and supply chain coordination with Autoliv manufacturing sites globally.
    humanURL: https://autoliv.biz
    tags:
      - Supply Chain
      - Procurement
      - Supplier Management
      - B2B
    properties:
      - type: Portal
        url: https://autoliv.biz
common:
  - type: Website
    url: https://www.autoliv.com
  - type: GitHubOrganization
    url: https://github.com/autoliv
  - type: Features
    data:
      - name: Airbag Systems
        description: Front, side curtain, knee, pedestrian, and center airbag systems for passenger vehicles, commercial vehicles, and motorcycles.
      - name: Seatbelt Systems
        description: Seatbelt assemblies, webbing, and retractors engineered for crash performance across all vehicle segments.
      - name: Steering Wheels
        description: Steering wheel systems including foldable designs for autonomous vehicles and advanced driver assistance configurations.
      - name: Pyrotechnic Components
        description: Inflators, initiators, pyro safety switches, and pyrotechnic actuators for airbag deployment and battery disconnect applications.
      - name: HBM Safety Suite
        description: Software platform supporting occupant safety simulation, virtual testing, and digital validation of safety systems.
      - name: Commercial Vehicle Safety
        description: Seat belt and airbag solutions tailored for trucks, buses, and off-road vehicles.
  - type: UseCases
    data:
      - name: OEM Supply Chain Integration
        description: Tier-1 supplier integration with automotive OEM procurement and logistics systems for just-in-time delivery of safety components.
      - name: Supplier Onboarding
        description: Onboarding new suppliers into Autoliv's global supply base through the supplier portal with document management and compliance workflows.
      - name: Connected Safety
        description: Integration of Autoliv safety systems with vehicle telematics and connected car platforms for post-crash notification and safety analytics.
      - name: Safety Simulation
        description: Virtual occupant safety testing and crash simulation using the HBM Safety Suite to accelerate product development and validation.
  - type: Integrations
    data:
      - name: Automotive OEM ERP Systems
        description: EDI and system integrations with OEM enterprise resource planning systems for procurement, logistics, and order management.
      - name: SAP Supply Chain
        description: Supply chain management integration with SAP systems used across Autoliv's global manufacturing network.
      - name: IATF 16949 Quality Systems
        description: Quality management integrations aligned with the IATF 16949 automotive quality management standard.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
