---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://sensee.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sensee-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sensee-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sensee-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sensee-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://visiongroup.io/responsible-disclosure/
created: '2026-07-17'
description: Sensee is a French direct-to-consumer online optician and contact-lens retailer, operating since 2005 and run by licensed opticians. It sells contact lenses, lens-care solutions, eye-health products and eyewear across six European markets (France, Germany, Italy, Spain, Switzerland and Austria) under localized storefronts, and supports third-party insurance payment (tiers payant) via networks such as Kalixia, Santeclair, Almerys and Optilys. Sensee is a subsidiary of Vision Group Holding AG. It was surfaced as a portfolio company of Partech and added to the API Evangelist network for enrichment; the enrichment pass found no public API, SDK or developer program, only a corporate security.txt / responsible-disclosure surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sensee.png
layout: provider
modified: '2026-07-21'
name: Sensee
nav: Providers
network: true
overview: Sensee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Eyewear, Contact Lenses, and Optical.
random_paper: 13
score:
  band: minimal
  composite: 5.8
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Sensee Domain Security
  slug: sensee-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Sensee Vulnerability Disclosure
  slug: sensee-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sensee
tags:
- Company
- Consumer
- Eyewear
- Contact Lenses
- Optical
- E-Commerce
- Healthcare
- Retail
- Europe
website: https://sensee.com/
---
