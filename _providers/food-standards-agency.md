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
api_count: 1
apis:
- description: UK food hygiene rating data API
  name: Food Standards Agency
  slug: food-standards-agency
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/food-standards-agency-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/food-standards-agency-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://ratings.food.gov.uk/open-data/en-GB
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: UK food hygiene rating data API
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/food-standards-agency.png
layout: provider
modified: '2026-05-28'
name: Food Standards Agency
nav: Providers
network: true
overview: Food Standards Agency publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 9
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/food-standards-agency/refs/heads/main/screenshots/food-standards-agency-2026-06-20T181401.png
security:
- kind: domain-security
  name: Food Standards Agency Domain Security
  slug: food-standards-agency-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Food Standards Agency Vulnerability Disclosure
  slug: food-standards-agency-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: food-standards-agency
tags:
- Government
- Public APIs
website: http://ratings.food.gov.uk/open-data/en-GB
---
