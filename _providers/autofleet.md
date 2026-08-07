---
api_count: 1
artifact_total: 0
coverage:
  checked: '2026-08-06'
  detail: Autofleet's entire ReadMe developer hub at docs.autofleet.io is password-protected — every path, including /openapi.json, /llms.txt and /sitemap.xml, 302s to /password?redirect=<path> — so although the API gateway at api.autofleet.io is live and the company markets a "public API and webhooks", no endpoint, spec, auth or error reference can be read without a customer password.
  evidence:
  - status: 302
    url: https://docs.autofleet.io/
  - status: 302
    url: https://docs.autofleet.io/openapi.json
  - status: 200
    url: https://docs.autofleet.io/password?redirect=/
  - status: 200
    url: https://api.autofleet.io/
  - status: 404
    url: https://api.autofleet.io/openapi.json
  - status: 200
    url: https://autofleet.io/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: 'Autofleet is a fleet and mobility optimization platform founded in 2018 in Tel Aviv by Kobi Eisenberg and Dor Shay, and since 2024 an independently operated, wholly owned subsidiary of Element Fleet Management Corp. (TSX: EFN). Its AI-driven software plans, dispatches, routes and simulates vehicle-based operations across postal and parcel delivery, last-mile logistics, rental and car sharing, corporate motor pools, microtransit, NEMT and school transport, taxi and rideshare, field service, and autonomous mobility, in more than 20 countries. The platform is sold as an integration hub — Autofleet markets a public API and webhooks for connecting telematics, GPS, keyless access, maintenance, booking, dispatch, CRM and ERP systems — and adds Nova, a fleet-specific generative AI layer for natural-language operational questions. The API gateway is live at api.autofleet.io, but the developer reference at docs.autofleet.io is a password-protected ReadMe hub, so no machine-readable contract
  is publicly retrievable.'
image: https://cdn.prod.website-files.com/62efd8600e99ef30950239a5/630cd578c9f8724a3a154de4_Social_Share_Image%20(1).png
layout: provider
modified: '2026-08-06'
name: Autofleet
nav: Providers
network: true
random_paper: 65
slug: autofleet
tags:
- Fleet Management
- Mobility
- Transportation
- Logistics
- Route Optimization
- Dispatch
- Last Mile Delivery
- Car Sharing
- Telematics
- Artificial Intelligence
---
