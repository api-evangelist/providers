---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://nexa3d.com'', ''status'': 301, ''note'': ''declared website redirects to https://i-am-marketplace.com/welcome-isquared-customers/ — a different registrable domain (nexa3d.com -> i-am-marketplace.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://nexa3d.com
coverage:
  checked: '2026-08-04'
  detail: Nexa3D sold its IP, inventory and equipment to Stratasys in July 2025 and stopped operating; nexa3d.com now 301-redirects off-brand to the am-material-marketplace / iAM Marketplace storefront, its docs/api/developer subdomains no longer resolve in DNS, and its GitHub organization has zero public repositories, so there is no API surface left to profile.
  evidence:
  - status: 301
    url: https://nexa3d.com/
  - status: 404
    url: https://nexa3d.com/openapi.json
  - status: 404
    url: https://nexa3d.com/llms.txt
  - status: 404
    url: https://nexa3d.com/.well-known/agent-card.json
  - status: 404
    url: https://nexa3d.com/.well-known/agent.json
  - status: 404
    url: https://nexa3d.com/.well-known/security.txt
  - status: 301
    url: https://www.am-material-marketplace.com/
  - status: 200
    url: https://github.com/nexa3d
  reason: defunct
  state: none
created: '2026-08-04'
description: 'Nexa3D was a Ventura, California additive-manufacturing company that built ultrafast photopolymer 3D printers (NXE 400, XiP, XiP Pro) around its Lubricant Sublayer Photo-curing (LSPc) process, QLS selective-laser-sintering systems, and the NexaX print-preparation and print-management software. The company disclosed severe funding challenges in late 2024, withdrew from Formnext, scaled back operations, and in July 2025 sold select assets — intellectual property, inventory and equipment, but not personnel — to Stratasys, with customer support and materials continuity moving to Stratasys subsidiary iSQUARED. Nexa3D no longer operates as an independent company: nexa3d.com now 301-redirects to a third-party additive-manufacturing materials marketplace, and no public developer portal, API reference, or machine-readable specification (OpenAPI, AsyncAPI, GraphQL SDL, MCP manifest, agent card) was found on any Nexa3D host, live or archived.'
layout: provider
modified: '2026-09-15'
name: Nexa3D
nav: Providers
network: true
overview: Nexa3D is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D Printing, Additive Manufacturing, Manufacturing, and Hardware.
random_paper: 7
slug: nexa3d
tags:
- Company
- 3D Printing
- Additive Manufacturing
- Manufacturing
- Hardware
- Industrial
- Defunct
website: https://nexa3d.com
---
