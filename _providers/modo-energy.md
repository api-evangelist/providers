---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Modo Energy Agentic Access
  operation_count: 5
  slug: modo-energy-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Modo Energy's API is designed for battery operators, owners, and utilities looking to build state-of-the-art energy data systems. RESTful, JSON-encoded, authenticated via x-token header.
  name: Modo Energy
  slug: modo-energy
- baseURL: https://api.modoenergy.com/pub/v1
  baseurl_source: declared
  description: ERCOT (Texas) battery operations
  name: Modo Energy ERCOT API
  slug: modo-energy-ercot-api
- baseURL: https://api.modoenergy.com/pub/v1
  baseurl_source: declared
  description: Great Britain market datasets
  name: Modo Energy GB API
  slug: modo-energy-gb-api
- baseURL: https://api.modoenergy.com/pub/v1
  baseurl_source: declared
  description: Australian National Electricity Market
  name: Modo Energy NEM API
  slug: modo-energy-nem-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Modo Energy ERCOT API
  slug: open-modo-energy-ercot-api
- collection_type: open
  name: Modo Energy ERCOT GB API
  slug: open-modo-energy-gb-api
- collection_type: open
  name: Modo Energy ERCOT NEM API
  slug: open-modo-energy-nem-api
- collection_type: open
  name: Modo Energy API
  slug: open-modo-energy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/modo-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modo-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/modo-energy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/modo-energy
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.modoenergy.com/llms.txt
created: '2025-05-02'
description: Modo Energy's API is designed for battery operators, owners, and utilities looking to build state-of-the-art energy data systems.
finops:
- name: Modo Energy Finops
  service_category: API
  slug: modo-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/modo-energy.png
layout: provider
modified: '2026-04-28'
name: Modo Energy
nav: Providers
network: true
overview: 'Modo Energy publishes 3 APIs on the [APIs.io](https://apis.io/) network: ERCOT API, GB API, and NEM API. Tagged areas include Energy, Battery Storage, Utilities, and Data.


  Modo Energy''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Modo Energy Plans Pricing
  plan_count: 3
  slug: modo-energy-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Modo Energy Rate Limits
  slug: modo-energy-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/modo-energy/refs/heads/main/screenshots/modo-energy-2026-06-20T185702.png
security:
- kind: authentication
  name: Modo Energy Authentication
  slug: modo-energy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Modo Energy Domain Security
  slug: modo-energy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: modo-energy
tags:
- Energy
- Battery Storage
- Utilities
- Data
---
