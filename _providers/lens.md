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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Lens Agentic Access
  operation_count: 6
  slug: lens-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.lens.org
  baseurl_source: declared
  description: Search and retrieve global patent records.
  name: Lens Patents API
  slug: lens-patents-api
- baseURL: https://api.lens.org
  baseurl_source: declared
  description: Search and retrieve scholarly works.
  name: Lens Scholarly API
  slug: lens-scholarly-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lens Patents API
  slug: open-lens-patents-api
- collection_type: open
  name: Lens Patents Scholarly API
  slug: open-lens-scholarly-api
- collection_type: open
  name: Lens API
  slug: open-lens
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lens-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lens-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lens-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lensapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/k8slens
- group: company
  title: ''
  type: Website
  url: https://www.lens.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.lens.org/
- group: commercial
  title: ''
  type: Plans
  url: https://www.lens.org/lens/user/subscriptions
- group: company
  title: ''
  type: About
  url: https://www.lens.org/lens/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lens.org/lens/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lens.org/lens/privacy-policy
created: '2025-02-06'
description: Lens is an open knowledge platform from Cambia that aggregates global scholarly works and patent records and exposes them through a REST API. The versioned API supports rich Elasticsearch-style queries, cursor pagination, and field projection across the full Lens scholarly and patent corpora, enabling research, science policy, technology landscape, and patent intelligence applications.
finops:
- name: Lens Finops
  service_category: API
  slug: lens-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lens.png
layout: provider
modified: '2026-05-19'
name: Lens
nav: Providers
network: true
overview: 'Lens publishes 2 APIs on the [APIs.io](https://apis.io/) network: Patents API and Scholarly API. Tagged areas include Scholarly, Patents, Research, Science, and Open Data.


  Lens'' developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Lens Plans Pricing
  plan_count: 3
  slug: lens-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Lens Rate Limits
  slug: lens-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 55.1
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 37.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lens/refs/heads/main/screenshots/lens-2026-06-20T184429.png
security:
- kind: authentication
  name: Lens Authentication
  slug: lens-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lens Domain Security
  slug: lens-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: lens
tags:
- Scholarly
- Patents
- Research
- Science
- Open Data
website: https://www.lens.org/
---
