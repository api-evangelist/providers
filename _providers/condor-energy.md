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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/condor-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.condor.energy/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/condor-energy-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/condor-energy-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/condor-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.condor.energy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.condor.energy/privacy
- group: start
  title: ''
  type: Login
  url: https://app.condor.energy/dashboard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/condorenergy
- group: commercial
  title: ''
  type: Legal
  url: https://www.condor.energy/legal
created: '2026-07-17'
description: Condor Energy is an AI-powered energy management operating system for enterprise energy procurement, built for industrial companies, retailers, and data center operators who buy electricity at scale. The platform aggregates consumption data, PPAs, solar, batteries, and live market data into real-time dashboards; models load against market dynamics to execute hedging strategies and produce board-ready price-risk reporting; and analyzes granular load data to find flexibility opportunities and evaluate ROI on solar, battery, EV-charging, and hybrid investments. Founded in 2026 by former electricity traders and energy physicists, the Paris-based company is a Y Combinator Winter 2026 company. No public API, developer portal, or SDK is published as of this profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/condor-energy.png
layout: provider
modified: '2026-07-18'
name: Condor Energy
nav: Providers
network: true
overview: 'Condor Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Energy Procurement, Energy Management, and Sustainability.


  Condor Energy''s developer surface includes legal docs and 9 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 21.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/condor-energy/refs/heads/main/screenshots/condor-energy-2026-07-25T210233.png
security:
- kind: domain-security
  name: Condor Energy Domain Security
  slug: condor-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Condor Energy Vulnerability Disclosure
  slug: condor-energy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: condor-energy
tags:
- Company
- Energy
- Energy Procurement
- Energy Management
- Sustainability
- Data Centers
- Price Risk Management
- Artificial Intelligence
- Analytics
website: https://www.condor.energy
---
