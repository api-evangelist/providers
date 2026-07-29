---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mcgill Agentic Access
  operation_count: 6
  slug: mcgill-agentic-access
  summary_line: 6 operations
api_count: 4
apis:
- description: McGill University Authentication Service, a Shibboleth Identity Provider offering SAML 2.0 federated single sign-on for McGill web applications and federation partners. This is an identity/SSO endpoin
  name: McGill Shibboleth SAML Single Sign-On
  slug: shibboleth-sso
- description: The Dataverses API from McGill University — 2 operation(s) for dataverses.
  name: McGill University Dataverses API
  slug: mcgill-dataverses-api
- description: The Info API from McGill University — 2 operation(s) for info.
  name: McGill University Info API
  slug: mcgill-info-api
- description: The Search API from McGill University — 2 operation(s) for search.
  name: McGill University Search API
  slug: mcgill-search-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mcgill-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mcgill-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mcgill-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.mcgill.ca/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/mcgillu
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/mcgill-university/
- group: auth
  title: ''
  type: Authentication
  url: https://shibboleth.mcgill.ca/
- group: commercial
  title: ''
  type: Plans
  url: plans/mcgill-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mcgill-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mcgill-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'McGill University is a public research university in Montreal, Quebec, Canada, ranked #64 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is centered on research-data infrastructure rather than a unified developer portal: the McGill University Dataverse is published through the Borealis (Scholars Portal) Dataverse platform, which exposes the full Dataverse Native and Search REST APIs over the McGill collection. Identity is federated through a Shibboleth SAML single sign-on service. Most other institutional systems (course catalogue, Minerva/Banner registration, library discovery) are gated behind authentication or web UIs and do not publish open, documented public APIs.'
examples:
- key_count: 2
  name: Mcgill Get Dataverse Example
  slug: mcgill-get-dataverse-example
- key_count: 2
  name: Mcgill Info Version Example
  slug: mcgill-info-version-example
- key_count: 2
  name: Mcgill Search Example
  slug: mcgill-search-example
finops:
- name: Mcgill Finops
  service_category: Education
  slug: mcgill-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mcgill.png
json_schemas:
- name: Dataverse Collection
  property_count: 14
  slug: mcgill-dataverse
- name: Dataverse Search Item
  property_count: 11
  slug: mcgill-search-item
json_structures:
- name: Mcgill Dataverse Structure
  property_count: 11
  slug: mcgill-dataverse-structure
- name: Mcgill Search Item Structure
  property_count: 11
  slug: mcgill-search-item-structure
jsonld:
- class_count: 20
  name: Mcgill Context
  property_count: 5
  slug: mcgill-context
layout: provider
modified: '2026-06-03'
name: McGill University
nav: Providers
network: true
overview: 'McGill University publishes 3 APIs on the [APIs.io](https://apis.io/) network: Dataverses API, Info API, and Search API. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The McGill University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  McGill University''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Mcgill Plans Pricing
  plan_count: 2
  slug: mcgill-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 1
  name: Mcgill Rate Limits
  slug: mcgill-rate-limits
rules:
- name: McGill University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: mcgill-jsonschema-spectral-rules
- name: McGill University API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: mcgill-rules
score:
  band: thin
  composite: 37.8
  delta: -3.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.8
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mcgill/refs/heads/main/screenshots/mcgill-2026-06-20T185057.png
security:
- kind: authentication
  name: Mcgill Authentication
  slug: mcgill-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mcgill Domain Security
  slug: mcgill-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mcgill
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- Canada
- Quebec
website: https://www.mcgill.ca/
---
