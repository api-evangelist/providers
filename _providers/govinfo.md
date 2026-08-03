---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Govinfo Agentic Access
  operation_count: 11
  slug: govinfo-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 5
apis:
- description: Discover new and updated documents based on GovInfo lastModified date/time
  name: GovInfo Collections API
  slug: govinfo-collections-api
- description: Return content and metadata for individual packages
  name: GovInfo Packages API
  slug: govinfo-packages-api
- description: Discover documents on GovInfo based on official publication date
  name: GovInfo Published API
  slug: govinfo-published-api
- description: Discover relationships between documents available on GovInfo
  name: GovInfo Related API
  slug: govinfo-related-api
- description: Discover documents on GovInfo using search queries and field operators available in the GovInfo UI
  name: GovInfo Search API
  slug: govinfo-search-api
artifact_total: 12
collections:
- collection_type: open
  name: GovInfo API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/govinfo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/govinfo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/govinfo-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.govinfo.gov
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.govinfo.gov/developers
- group: docs
  title: ''
  type: Documentation
  url: https://api.govinfo.gov/docs/
- group: start
  title: ''
  type: Signup
  url: https://www.govinfo.gov/api-signup
- group: build
  title: ''
  type: GitHub
  url: https://github.com/usgpo/api
- group: auth
  title: ''
  type: Authentication
  url: https://api.data.gov
- group: commercial
  title: ''
  type: License
  url: https://github.com/usgpo/api/blob/master/LICENSE.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.govinfo.gov/about/policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.govinfo.gov/privacy
created: '2024-11-14'
description: The GovInfo API, provided by the U.S. Government Publishing Office (GPO), provides services for developers and webmasters to access GovInfo content and metadata, including search, packages, granules, collections, related items, and published documents.
finops:
- name: Govinfo Finops
  service_category: API
  slug: govinfo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/govinfo.png
layout: provider
modified: '2026-05-19'
name: GovInfo
nav: Providers
network: true
overview: 'GovInfo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Packages API, Published API, and 2 more. Tagged areas include Federal Government, Government Publishing, Documents, and Open Data.


  GovInfo''s developer surface includes authentication, developer portal, documentation, signup flow, GitHub presence, and 7 more developer resources.'
plans:
- name: Govinfo Plans Pricing
  plan_count: 3
  slug: govinfo-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Govinfo Rate Limits
  slug: govinfo-rate-limits
score:
  band: thin
  composite: 41.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 54.7
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/govinfo/refs/heads/main/screenshots/govinfo-2026-06-20T182303.png
security:
- kind: authentication
  name: Govinfo Authentication
  slug: govinfo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Govinfo Domain Security
  slug: govinfo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: govinfo
tags:
- Federal Government
- Government Publishing
- Documents
- Open Data
website: https://www.govinfo.gov/developers
---
