---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://caastle.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.theorangemotel.com/ — a different registrable domain (caastle.com -> theorangemotel.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://caastle.com
coverage:
  checked: '2026-08-08'
  detail: CaaStle filed Chapter 7 in June 2025 and liquidated; caastle.com no longer belongs to the company and now 301s every path — /openapi.json, every /.well-known/ path and a nonsense control path alike — to an unrelated Indonesian-language site that answers 200 with one byte-identical HTML page, none of the archived api-*.caastle.com tenant hosts still resolve in DNS, and 6,000 Wayback records for the domain contain no developer, docs, or specification path.
  evidence:
  - status: 301
    url: https://caastle.com/
  - status: 301
    url: https://caastle.com/openapi.json
  - status: 301
    url: https://caastle.com/.well-known/agent-card.json
  - status: 301
    url: https://www.caastle.com/.well-known/security.txt
  reason: defunct
  state: none
created: '2026-08-08'
description: 'CaaStle Inc. was a New York based business-to-business "Clothing-as-a-Service" company that built white-label clothing rental, subscription and resale infrastructure for apparel retailers, operating tenant-branded storefronts and reverse-logistics for partner brands rather than selling directly to consumers. The company collapsed in 2025: its board confirmed financial distress and furloughed staff in April 2025, and it filed for Chapter 7 bankruptcy in the District of Delaware on 20 June 2025 (case 25-11187), electing liquidation over reorganization. Founder and chief executive Christine Hunsicker resigned amid allegations of fabricated financial disclosures and later pleaded guilty to a fraud scheme prosecutors valued in the hundreds of millions of dollars. CaaStle never operated a public developer program, and the caastle.com domain has since passed out of the company''s control.'
layout: provider
modified: '2026-09-15'
name: CaaStle
nav: Providers
network: true
overview: CaaStle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Fashion, E-Commerce, and Subscription.
random_paper: 7
screenshot: https://raw.githubusercontent.com/api-evangelist/caastle/refs/heads/main/screenshots/caastle-2026-09-02T144957.png
slug: caastle
tags:
- Company
- Retail
- Fashion
- E-Commerce
- Subscription
- Rentals
- Logistics
- Defunct
website: https://caastle.com
---
