---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://foreveroceans.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/foreveroceans
- group: other
  title: ''
  type: Listing
  url: https://forgeglobal.com/forever-oceans_stock/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/forever-oceans/refs/heads/main/security/forever-oceans-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/forever-oceans-domain-security.yml
coverage:
  checked: '2026-08-16'
  detail: Forever Oceans was an offshore fish-farming company whose investors handed it to liquidation specialists in November 2024; its own domain foreveroceans.com now refuses HTTPS entirely (connection refused on 443) and serves only a Gandi registrar parking page reading "foreveroceans.com is unavailable" over plain HTTP, with no api/docs/developer subdomains resolving and an empty corporate GitHub org.
  evidence:
  - status: 0
    url: https://foreveroceans.com/
  - status: 200
    url: http://foreveroceans.com/
  - status: 200
    url: http://foreveroceans.com/openapi.json
  - status: 0
    url: http://foreveroceans.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/foreveroceans
  reason: defunct
  state: none
created: '2026-08-16'
description: 'Forever Oceans Corporation was a US offshore aquaculture company, founded in 2014 and headquartered in Virginia, that raised sushi-grade kanpachi (Seriola rivoliana) in deep water off the Pacific coast of Panama using a patented single-point mooring system that let its submerged pens orient with ocean currents. It raised roughly $170M and held a large Brazilian marine-aquaculture concession, with planned farms in Brazil and Indonesia. Its investors brought in restructuring and liquidation specialists in November 2024, and its corporate domain foreveroceans.com is now a registrar parking page that refuses HTTPS. Seafood production, not software, was the product: the company never published an API, developer portal, SDK or any machine-readable contract, and no such surface survives.'
layout: provider
modified: '2026-09-15'
name: Forever Oceans
nav: Providers
network: true
overview: Forever Oceans is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aquaculture, Seafood, Food Production, and Sustainability.
random_paper: 9
security:
- kind: domain-security
  name: Forever Oceans Domain Security
  slug: forever-oceans-domain-security
  summary_line: no transport/DNS hardening detected
slug: forever-oceans
tags:
- Company
- Aquaculture
- Seafood
- Food Production
- Sustainability
- Offshore Farming
- Ocean Technology
- Defunct
website: https://foreveroceans.com/
---
