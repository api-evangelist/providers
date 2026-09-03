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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: APA Corporation explores for and produces oil and natural gas in the United States, Egypt, the United Kingdom, and Suriname through its Apache Corporation and APA Suriname subsidiaries.
  name: APA Corporation
  slug: apa-corporation
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apa-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apa-corporation
- group: company
  title: ''
  type: Website
  url: https://apacorp.com
- group: docs
  title: ''
  type: Documentation
  url: https://apacorp.com
- group: operate
  title: ''
  type: Support
  url: https://apacorp.com/contact
- group: company
  title: ''
  type: Blog
  url: https://apacorp.com/feed/
created: '2026-03-21'
description: APA Corporation is an independent energy company that explores for, develops, and produces natural gas, crude oil, and natural gas liquids, with operations in the United States, Egypt, the United Kingdom, and Suriname. Organized in Delaware and headquartered in Houston, Texas, APA is listed on Nasdaq (APA) and listed on Nasdaq Texas since March 2026.
features:
- description: Exploration and production activities in the Permian Basin and other US basins through the Apache Corporation subsidiary.
  name: United States Operations
- description: Long-standing operations in Egypt's Western Desert through Apache Corporation, one of the largest private natural gas producers in Egypt.
  name: Egypt Operations
- description: North Sea oil and gas operations through Apache Corporation's UK subsidiary.
  name: United Kingdom Operations
- description: Offshore exploration in Suriname Block 58 through the APA Suriname subsidiary, with significant oil discoveries including the GranMorgu project.
  name: Suriname Exploration
- description: Exploration activities on Alaska's North Slope including the Sockeye-2 well oil discovery in partnership with Lagniappe Alaska and Santos.
  name: Alaska Exploration
finops:
- name: Apa Finops
  service_category: API
  slug: apa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apa.png
integrations:
- description: 'APA Corporation is listed on Nasdaq (ticker: APA) and Nasdaq Texas, enabling trading and investor relations integrations.'
  name: Nasdaq
layout: provider
modified: '2026-04-19'
name: APA Corporation
nav: Providers
network: true
overview: 'APA Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Oil and Gas, Energy, Exploration, and Production.


  APA Corporation''s developer surface includes documentation, support, engineering blog, and 3 more developer resources.'
plans:
- name: Apa Plans Pricing
  plan_count: 3
  slug: apa-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Apa Rate Limits
  slug: apa-rate-limits
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apa/refs/heads/main/screenshots/apa-2026-06-20T172039.png
security:
- kind: domain-security
  name: Apa Domain Security
  slug: apa-domain-security
  summary_line: TLSv1.3
slug: apa
tags:
- Oil and Gas
- Energy
- Exploration
- Production
use_cases:
- description: Access financial results, stock information, SEC filings, and corporate governance information for APA Corporation shareholders.
  name: Investor Relations
- description: Track oil, natural gas, and natural gas liquids production data across APA's operational regions.
  name: Energy Production Data
website: https://apacorp.com
---
