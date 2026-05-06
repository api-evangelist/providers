---
aid: williams-companies
name: Williams Companies
description: The Williams Companies is an American Fortune 500 energy company focused on natural gas infrastructure, processing, and transportation. Williams owns and operates midstream energy assets including the Transco pipeline (the largest natural gas pipeline in the United States), gathering and processing systems, and storage facilities. Williams serves natural gas producers, local distribution companies, and large-volume end users. The company provides customer portal access for operational data and FERC-regulated electronic bulletin boards for capacity transactions, but does not offer public developer REST APIs.
url: https://raw.githubusercontent.com/api-evangelist/williams-companies/refs/heads/main/apis.yml
type: Index
position: Consumer
access: 3rd-Party
tags:
  - Natural Gas
  - Energy Infrastructure
  - Midstream
  - Pipeline
  - Fortune 500
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis: []
common:
  - type: Website
    url: https://www.williams.com
  - type: Portal
    url: https://www.williams.com/customers/
  - type: Features
    data:
      - name: Transco Pipeline
        description: The Transco pipeline is the largest natural gas pipeline system in the US, running from the Gulf Coast to New York City.
      - name: Gathering and Processing
        description: Williams gathers and processes natural gas from producing basins in the Appalachian, Gulf Coast, and Rockies regions.
      - name: Storage Facilities
        description: Williams operates natural gas storage facilities providing seasonal and peak supply balancing for customers.
      - name: Customer Data Portal
        description: Customer portal providing access to operational data, nominations, and account management for gas shippers.
      - name: FERC Electronic Bulletin Board
        description: FERC-mandated electronic bulletin boards for capacity release, scheduling, and tariff information on interstate pipelines.
      - name: OATI Integration
        description: Open Access Technology International (OATI) platform integration for natural gas transportation nominations and scheduling.
  - type: UseCases
    data:
      - name: Natural Gas Transportation
        description: End-to-end transportation of natural gas from producing regions to local distribution companies and end users.
      - name: Capacity Management
        description: Shippers access Williams' FERC electronic bulletin boards to reserve, release, and manage interstate pipeline capacity.
      - name: Gas Processing
        description: Natural gas liquids extraction and conditioning services for producers in Williams' gathering and processing footprint.
      - name: Supply Reliability
        description: Utilities use Williams' pipeline and storage assets to balance seasonal demand and ensure supply reliability.
  - type: Integrations
    data:
      - name: OATI webEBB
        description: Williams participates in OATI's webEBB electronic bulletin board platform for interstate pipeline capacity transactions.
      - name: Infopost
        description: Williams uses Infopost for FERC-mandated posting of operational data, tariff information, and capacity availability.
      - name: NEXTT
        description: Industry-standard EDI/electronic nominations system for natural gas transportation scheduling with Williams pipelines.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
