---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://starry.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://starry.com/internet
- group: operate
  title: ''
  type: Support
  url: https://support.starry.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://account.starry.com/login
- group: company
  title: ''
  type: Blog
  url: https://starry.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StarryInternet
- group: commercial
  title: ''
  type: TermsOfService
  url: https://starry.com/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://starry.com/legal/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/starry-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/starry-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/starry-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starry-domain-security.yml
coverage:
  checked: '2026-08-29'
  detail: Starry is a consumer/property-facing fixed-wireless ISP with no developer program at all — developer.starry.com, docs.starry.com and api.starry.com do not resolve in DNS, starry.com/developers and starry.com/api both 404, and the 30-URL sitemap.xml contains only marketing, city-coverage, careers and legal pages; the sole machine surface found is the authenticated customer account portal at account.starry.com, which answers every path (including /.well-known/*) with a hapi-style JSON 401 "Missing authentication".
  evidence:
  - status: 404
    url: https://starry.com/openapi.json
  - status: 404
    url: https://starry.com/developers
  - status: 0
    url: https://developer.starry.com/
  - status: 401
    url: https://account.starry.com/openapi.json
  - status: 200
    url: https://starry.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: 'Starry, Inc. is a Boston-founded (2014) internet service provider that delivers fixed wireless broadband to multi-dwelling buildings and homes in five US metropolitan markets — Boston, New York City, Los Angeles, Denver and Washington, D.C. — over its own licensed millimeter-wave spectrum and proprietary radio hardware rather than leased last-mile cable or fiber. Consumer plans run from Starry 200 (200 Mbps, $30/mo) to Starry Gigabit (1 Gbps, $45/mo), month-to-month with no data caps, a bundled Wi-Fi router and a three-year price lock, alongside a Starry Connect program for affordable-housing properties and a wholesale/bulk offering for property owners. Starry restructured through Chapter 11 in 2023 and was acquired by Verizon in a deal announced October 2025. It is a consumer/property-facing broadband operator: it runs an authenticated customer account portal and publishes an llms.txt and a substantial open-source GitHub organization, but it operates no public developer program
  and publishes no machine-readable API contract.'
image: https://dyajmw2sca9cs.cloudfront.net/img/logo/starry-logo.jpg
layout: provider
modified: '2026-08-29'
name: Starry
nav: Providers
network: true
overview: 'Starry is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Internet Service Provider, Broadband, Fixed Wireless, and Telecommunications.


  Starry''s developer surface includes pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Starry Plans Pricing
  plan_count: 3
  slug: starry-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Starry Rate Limits
  slug: starry-rate-limits
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Starry Domain Security
  slug: starry-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: starry
tags:
- Company
- Internet Service Provider
- Broadband
- Fixed Wireless
- Telecommunications
- Networking
- Consumer Internet
- Millimeter Wave
website: https://starry.com/
---
