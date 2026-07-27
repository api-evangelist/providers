---
api_count: 1
artifact_total: 0
created: '2026-07-27'
description: Smart DCC (the Data Communications Company) is the Ofgem-licensed monopoly that operates Britain's national smart metering communications network, connecting electricity and gas smart meters in homes and businesses to energy suppliers, network operators and other authorised users over a single secure wide-area network. It sits in the middle of the United Kingdom energy value chain as shared infrastructure rather than as a retailer or a data marketplace, and it is regulated through the Smart Meter Communication Licence and governed by the Smart Energy Code. Its API posture reflects that position exactly. Britain mandated the infrastructure, not a consumer data right — there is no UK equivalent of the Australian Consumer Data Right for energy, so Smart DCC operates no consumer data-portability API and publishes no Green Button or Consumer Data Standards surface. The real production interface is the DCC User Interface Specification (DUIS), an XML web service reached over a DCC
  User Gateway Connection, plus the Self-Service Interface; the DUIS specification and its XML schema are published openly as Smart Energy Code subsidiary documents, but the gateway itself is closed to anyone who has not acceded to the Smart Energy Code and passed SMKI and User Entry Process Testing. The only self-serve, machine-readable contract Smart DCC publishes is an OpenAPI for the open-source DCC Boxed DUIS signing and validation tool on GitHub. Network statistics are shown on a public dashboard as a rendered web page with no documented open data API or bulk download, so both the consumer-data and market-data sides are effectively closed while the interface specification itself is open.
image: https://www.smartdcc.co.uk/assets/images/favicon.ico
layout: provider
modified: '2026-07-27'
name: Smart DCC
nav: Providers
network: true
random_paper: 10
slug: dcc-smart
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Smart Metering
- Grid
- Metering Infrastructure
- Energy Data
---
