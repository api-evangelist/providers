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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rio-tinto-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rio-tinto
- group: company
  title: ''
  type: Website
  url: https://www.riotinto.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/rio-tinto
- group: start
  title: ''
  type: SupplierPortal
  url: https://www.riotinto.com/suppliers
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rio-tinto-vocabulary.yml
created: '2026-05-05'
description: Rio Tinto is a British-Australian multinational mining and metals corporation and one of the world's largest producers of iron ore, aluminum, copper, and diamonds. Rio Tinto does not publish a public developer API, but operates supplier portals (Supplier Master Data Management and a transactional platform) and a START traceability program. Its GitHub presence is limited to a small number of internal forks (ai-sentry, xpano).
features:
- description: Leading global producer of iron ore from Pilbara and other regions
  name: Iron Ore Production
- description: Integrated aluminum value chain from bauxite mining to smelting
  name: Aluminum and Bauxite
- description: Copper concentrates and diamond production for global markets
  name: Copper and Diamonds
- description: Lithium and other minerals critical to electrification
  name: Energy-Transition Minerals
- description: Product traceability program for responsibly sourced metals
  name: START Traceability
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rio-tinto.png
layout: provider
modified: '2026-05-16'
name: Rio Tinto
nav: Providers
network: true
overview: Rio Tinto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mining, Metals, Resources, and Critical Minerals.
random_paper: 9
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 15.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 15.2
    operational_transparency: 5.3
  previous_composite: 6.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rio-tinto/refs/heads/main/screenshots/rio-tinto-2026-06-20T193124.png
security:
- kind: domain-security
  name: Rio Tinto Domain Security
  slug: rio-tinto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rio-tinto
tags:
- Mining
- Metals
- Resources
- Critical Minerals
use_cases:
- description: Rio Tinto maintains supplier master data and transactional portals
  name: Supplier Onboarding
- description: START provides end-to-end traceability of materials from mine to product
  name: Responsible Sourcing
website: https://www.riotinto.com/
---
