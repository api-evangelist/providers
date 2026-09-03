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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ecoplanet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ecoplanet.tech
- group: company
  title: ''
  type: Blog
  url: https://www.ecoplanet.tech/ressourcen/blog
- group: operate
  title: ''
  type: Support
  url: https://www.ecoplanet.tech/support
- group: start
  title: ''
  type: Login
  url: https://app.ecoplanet.tech/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ecoplanet.tech/datenschutz
created: '2026-07-17'
description: 'ecoplanet provides cloud-based, integrated energy management software for German mid-market companies. The platform combines three core functions: real-time consumption monitoring through meter integration with AI-powered anomaly detection and automated load-shifting on price signals; strategic energy procurement using algorithmic purchasing across spot markets, tranches, and power purchase agreements (PPAs); and automated ISO 50001 compliance documentation. The company reports customers achieve up to 15% consumption savings and ~13.9% average price advantages on energy purchases. Backed by EQT Ventures and HV Capital. No public developer/API surface was found at the time of profiling.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ecoplanet.png
layout: provider
modified: '2026-07-19'
name: ecoplanet
nav: Providers
network: true
overview: 'ecoplanet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate, Energy, Energy Management, and Sustainability.


  ecoplanet''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 9.0
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ecoplanet/refs/heads/main/screenshots/ecoplanet-2026-07-25T212805.png
security:
- kind: domain-security
  name: Ecoplanet Domain Security
  slug: ecoplanet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ecoplanet
tags:
- Company
- Climate
- Energy
- Energy Management
- Sustainability
- ISO 50001
- Energy Procurement
- Software
- Germany
website: https://www.ecoplanet.tech
---
