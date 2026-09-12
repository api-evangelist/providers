---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-12'
  detail: Applied EV markets six named IoV Cloud Platform vehicle APIs on https://www.appliedev.com/cloud but serves no public reference for any of them; its developer portal at developer.appliedev.com and its identity host sso.appliedev.com exist in Certificate Transparency and resolve in DNS to 3.105.246.26, yet both origins silently drop public TCP connections on 443 and 80, so the contract is reachable only from a customer tenant or an allowlisted network.
  evidence:
  - status: 200
    url: https://www.appliedev.com/cloud
  - status: 404
    url: https://www.appliedev.com/openapi.json
  - status: 404
    url: https://www.appliedev.com/.well-known/api-catalog
  - status: 404
    url: https://www.appliedev.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-09-12'
description: 'Applied EV (formerly AEV Robotics, legal entity Applied Electric Vehicles Ltd) is an Australian software-defined vehicle company founded in Melbourne in 2015 by Julian Broadbent and Shane Ambry. It builds the Blanc Robot, a cabinless autonomous-ready electric platform for logistics, industrial, mining and agricultural transport; the Digital Backbone, a safety-rated ASIL-D programmable vehicle control system; and an Internet-of-Vehicles (IoV) Cloud Platform the company markets as API-first. The IoV platform is advertised as a set of vehicle APIs — Access Manager for identity and access management, a Vehicle Task API, a Vehicle Mission API, a Drive API for autonomous driving and motion control, a Pod and Accessory API, and Virtual Vehicles for simulation — together with a Vehicle Management System for fleet telemetry, diagnostics, mapping, mission creation and over-the-air software updates. No public developer portal, API reference or machine-readable contract is served: the
  developer host resolves but refuses public connections, and the marketing pages route every developer path to an enquiry form.'
image: https://www.appliedev.com/api/assets/5146586c-032d-4b18-90fc-2edeffc24a30
layout: provider
modified: '2026-09-12'
name: Applied EV
nav: Providers
network: true
random_paper: 9
slug: aevrobotics
tags:
- Company
- Robotics
- Autonomous Vehicles
- Electric Vehicles
- Software Defined Vehicles
- Internet of Vehicles
- Fleet Management
- Automotive
- Logistics
- Mobility
- Australia
---
