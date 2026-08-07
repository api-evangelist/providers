---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-06'
  detail: 'Battery Smart runs a real production API — api.upgrid.in answers {"message":"Battery Smart API"} and a /health check for SQL, Redis, Kafka and Mongo, discovered only through Certificate Transparency on the Upgrid engineering domain — but it exists purely to serve the Driver and Partner Android apps: every spec path on that host returns a JSON 404, batterysmart.in has no /developers, no api./docs./developer. subdomain in DNS at all, and the company publishes no reference, SDK, webhook catalog or specification anywhere.'
  evidence:
  - status: 200
    url: https://api.upgrid.in/
  - status: 404
    url: https://api.upgrid.in/openapi.json
  - status: 404
    url: https://www.batterysmart.in/openapi.json
  - status: 404
    url: https://www.batterysmart.in/llms.txt
  - status: 404
    url: https://www.batterysmart.in/.well-known/agent-card.json
  - status: 0
    url: https://developer.batterysmart.in/
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Battery Smart is India''s largest battery-swapping network for electric two- and three-wheelers, founded in 2019 by Pulkit Khurana and Siddharth Sikka and operated from New Delhi by Upgrid Solutions Private Limited and Upgrid Electrilease Private Limited. It runs an asset-light, partner-led model: local businesses — kirana stores, petrol pumps and neighbourhood shops — host swap points where a driver exchanges a depleted lithium-ion pack for a charged one in roughly two minutes and pays per swap instead of buying the battery with the vehicle, which removes the single largest cost from an electric two- or three-wheeler. The network is concentrated in Delhi NCR, Mumbai, Bengaluru, Hyderabad, Jaipur and Lucknow, and the company has raised across eleven rounds including a USD 65 million Series B led by LeapFrog Investments with MUFG Bank, Panasonic, Ecosystem Integrity Fund, Blume Ventures and British International Investment participating, plus a USD 15 million debt round with
  Mirova in April 2026. Battery Smart''s software ships only as end-user Android applications — Battery Smart Driver and Battery Smart Partner — backed by a production API host at api.upgrid.in that self-identifies as the "Battery Smart API". As of this profile the company publishes no developer portal, API reference, SDK, webhook catalog or machine-readable specification of any kind.'
image: https://www.batterysmart.in/_next/static/media/logo.9f0b8870.webp
layout: provider
modified: '2026-08-06'
name: Battery Smart
nav: Providers
network: true
random_paper: 3
slug: battery-smart
tags:
- Company
- Battery Swapping
- Electric Vehicles
- EV Infrastructure
- Battery as a Service
- Energy
- Clean Energy
- Mobility
- Two Wheelers
- Three Wheelers
- Last Mile Delivery
- India
---
