---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The Spectrum Enterprise Open API provides B2B REST API access for enterprise clients to integrate directly with the Spectrum Enterprise portal. It supports automated ticket creation and management, ci
  name: Spectrum Enterprise Client API
  slug: spectrum-enterprise-api
- description: The Spectrum Carrier Serviceability API enables carrier partners to submit address serviceability requests to determine Charter network coverage. Supports both single-address and batch address service
  name: Spectrum Carrier Serviceability API
  slug: carrier-serviceability-api
- description: Bryte IQ is Charter Communications' NaaS developer platform built on the Linux Foundation's CAMARA open API framework. Launched in September 2024, it provides secure, privacy-friendly APIs for third-p
  name: Bryte IQ Network-as-a-Service API
  slug: bryte-iq-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/charter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spectrum.com
- group: company
  title: ''
  type: Website
  url: https://corporate.charter.com
- group: company
  title: ''
  type: EnterpriseWebsite
  url: https://enterprise.spectrum.com
- group: docs
  title: ''
  type: Documentation
  url: https://enterprise.spectrum.com/support/faqs/api-faqs.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/charter
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/charter-communications
- group: company
  title: ''
  type: Blog
  url: https://corporate.charter.com/newsroom
- group: commercial
  title: ''
  type: Pricing
  url: plans/charter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/charter-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/charter-finops.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://statusgator.com/services/charter-communications
- group: other
  title: ''
  type: X
  url: https://x.com/CharterNewsroom
- group: commercial
  title: ''
  type: Plans
  url: plans/charter-plans-pricing.yml
created: '2026-06-13'
description: Charter Communications, operating under the Spectrum brand, is the second-largest cable operator in the United States serving more than 32 million customers across 41 states. Charter offers REST APIs for enterprise network provisioning, service account management, broadband diagnostics, customer support ticket automation, and circuit serviceability. The Spectrum Enterprise Open API enables B2B integrations for ticketing, circuit management, and network operations. Charter's Bryte IQ platform, built on the Linux Foundation's CAMARA framework, provides NaaS (Network-as-a-Service) APIs enabling third-party developers to build services that interact with Charter's wired and wireless networks, including connected device visibility, CPE management, and home network support.
finops:
- name: Charter Finops
  service_category: ''
  slug: charter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/charter.png
layout: provider
modified: '2026-07-25'
name: Charter Communications
nav: Providers
network: true
overview: 'Charter Communications publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Internet Service Provider, Cable, Network Provisioning, and Broadband.


  Charter Communications'' developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Charter Plans Pricing
  plan_count: 3
  slug: charter-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Charter Rate Limits
  slug: charter-rate-limits
score:
  band: emerging
  composite: 19.4
  delta: -0.8
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/charter/refs/heads/main/screenshots/charter-2026-06-20T174232.png
security:
- kind: domain-security
  name: Charter Domain Security
  slug: charter-domain-security
  summary_line: TLSv1.3 · DMARC
slug: charter
tags:
- Telecommunications
- Internet Service Provider
- Cable
- Network Provisioning
- Broadband
- Spectrum
- NaaS
- Enterprise
website: https://www.spectrum.com
---
