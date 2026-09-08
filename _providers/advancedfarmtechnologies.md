---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-07'
  detail: CNH Industrial absorbed Advanced Farm on 2025-04-02 and the company's own domain advanced.farm now answers every path — including /openapi.json, /llms.txt and every /.well-known probe — with a catch-all HTTP 301 to https://agriculture.newholland.com/en-us/nar, while HTTPS on that host no longer completes a TLS handshake at all.
  evidence:
  - status: 301
    url: http://advanced.farm/openapi.json
  - status: 301
    url: http://advanced.farm/.well-known/agent-card.json
  - status: 0
    url: https://advanced.farm/
  - status: 404
    url: https://api.github.com/orgs/advanced-farm
  - status: 200
    url: https://equityzen.com/company/advancedfarmtechnologies
  reason: defunct
  state: none
created: '2026-09-07'
description: 'Advanced Farm Technologies (brand: advanced.farm) was an agricultural robotics company founded in 2017 in Davis, California, building autonomous robotic harvesters for specialty crops. Its T-6 robotic strawberry harvester and six-armed robotic apple harvester used custom rugged stereo cameras and machine-learning ripeness models to identify and pick fruit alongside human crews, and the company sold harvesting as a service rather than selling the machines. It raised roughly $34M from investors including CNH Industrial, Yamaha Motor Ventures and Catapult Ventures. On 2025-04-02 CNH Industrial acquired the company''s intellectual property and assets and the majority of its technical team joined CNH; the company no longer operates independently. Its domain, advanced.farm, now returns a blanket HTTP 301 to CNH''s New Holland Agriculture site. Advanced Farm never published a public API, developer portal, SDK or machine-readable contract.'
layout: provider
modified: '2026-09-07'
name: Advanced Farm Technologies
nav: Providers
network: true
random_paper: 8
slug: advancedfarmtechnologies
tags:
- Company
- Agriculture
- Agricultural Robotics
- Robotics
- Automation
- Computer Vision
- Harvesting
---
