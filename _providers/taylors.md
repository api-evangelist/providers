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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Taylors Agentic Access
  operation_count: 11
  slug: taylors-agentic-access
  summary_line: 11 operations
api_count: 9
apis:
- description: OAI-PMH 2.0 data provider exposed by the Koha-powered Taylor's Library catalog for harvesting bibliographic metadata. The Identify response returns repository name "Taylor's Library" with earliest rec
  name: Taylor's Library OAI-PMH
  slug: library-oai
- description: The Taylor's e-Repository runs on DSpace CRIS (cris-2022.01.01) and exposes a HATEOAS HAL+JSON REST API at /server/api covering communities, collections, items, bundles, discovery, statistics, ORCID a
  name: Taylor's e-Repository DSpace REST API
  slug: irepo-rest
- description: OAI-PMH 2.0 data provider for the DSpace CRIS e-Repository, advertising repository name "Taylor's University Library" and OpenAIRE CERIF profile compliance for research-output discovery and aggregatio
  name: Taylor's e-Repository OAI-PMH
  slug: irepo-oai
- description: Item checkouts (issues)
  name: Taylor's University checkouts API
  slug: taylors-checkouts-api
- description: Holds (reservations)
  name: Taylor's University holds API
  slug: taylors-holds-api
- description: Item types
  name: Taylor's University item_types API
  slug: taylors-item-types-api
- description: Catalog items
  name: Taylor's University items API
  slug: taylors-items-api
- description: Libraries (branches)
  name: Taylor's University libraries API
  slug: taylors-libraries-api
- description: Patron (borrower) records
  name: Taylor's University patrons API
  slug: taylors-patrons-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Taylor's Library Koha REST checkouts API
  slug: open-taylors-checkouts-api
- collection_type: open
  name: Taylor's Library Koha REST checkouts holds API
  slug: open-taylors-holds-api
- collection_type: open
  name: Taylor's Library Koha REST checkouts item_types API
  slug: open-taylors-item-types-api
- collection_type: open
  name: Taylor's Library Koha REST checkouts items API
  slug: open-taylors-items-api
- collection_type: open
  name: Taylor's Library Koha REST checkouts libraries API
  slug: open-taylors-libraries-api
- collection_type: open
  name: Taylor's Library Koha REST checkouts patrons API
  slug: open-taylors-patrons-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/taylors-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taylors-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/taylors-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/taylors-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://university.taylors.edu.my/en.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Taylors-University
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/taylor's-university/
- group: auth
  title: ''
  type: Authentication
  url: https://librarycatalogue.taylors.edu.my/
- group: commercial
  title: ''
  type: Plans
  url: plans/taylors-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/taylors-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/taylors-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Taylor''s University is a private research university based in Subang Jaya, Selangor, Malaysia, and ranked #251 in the QS World University Rankings 2025. It does not operate a formal, branded developer portal, but several real, publicly reachable machine interfaces exist across its library and research infrastructure. The Taylor''s Library catalog runs on Koha (exposing a Koha REST API and an OAI-PMH data provider), and the Taylor''s e-Repository runs on DSpace CRIS (exposing a HAL+JSON REST API and an OAI-PMH endpoint). Identity is federated through Microsoft Entra ID. The institution''s GitHub organization exists but currently has no public repositories.'
examples:
- key_count: 16
  name: Taylors Getcheckout Example
  slug: taylors-getCheckout-example
- key_count: 24
  name: Taylors Getitem Example
  slug: taylors-getItem-example
- key_count: 23
  name: Taylors Getpatron Example
  slug: taylors-getPatron-example
finops:
- name: Taylors Finops
  service_category: Education
  slug: taylors-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taylors.png
json_schemas:
- name: Koha Checkout
  property_count: 16
  slug: taylors-checkout
- name: Koha Hold
  property_count: 20
  slug: taylors-hold
- name: Koha Item
  property_count: 24
  slug: taylors-item
- name: Koha Patron
  property_count: 23
  slug: taylors-patron
json_structures:
- name: Taylors Item Structure
  property_count: 20
  slug: taylors-item-structure
- name: Taylors Patron Structure
  property_count: 18
  slug: taylors-patron-structure
jsonld:
- class_count: 6
  name: Taylors Context
  property_count: 6
  slug: taylors-context
layout: provider
modified: '2026-06-03'
name: Taylor's University
nav: Providers
network: true
overview: 'Taylor''s University publishes 6 APIs on the [APIs.io](https://apis.io/) network, including checkouts API, holds API, item_types API, and 3 more. Tagged areas include Education, Higher Education, University, Library, and Institutional Repository.


  The Taylor''s University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Taylor''s University''s developer surface includes authentication, GitHub presence, and 10 more developer resources.'
plans:
- name: Taylors Plans Pricing
  plan_count: 2
  slug: taylors-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Taylors Rate Limits
  slug: taylors-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Taylor's University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: taylors-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: Taylor's University API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 4
  slug: taylors-rules
scopes:
- name: Taylors Scopes
  scope_count: 0
  slug: taylors-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.4
  delta: 4.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 25.0
    contract_quality: 64.6
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taylors/refs/heads/main/screenshots/taylors-2026-06-20T194940.png
security:
- kind: authentication
  name: Taylors Authentication
  slug: taylors-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Taylors Domain Security
  slug: taylors-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: taylors
tags:
- Education
- Higher Education
- University
- Library
- Institutional Repository
- Open Data
- Malaysia
- Asia
website: https://university.taylors.edu.my/en.html
---
