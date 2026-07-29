---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dartmouth Agentic Access
  operation_count: 11
  slug: dartmouth-agentic-access
  summary_line: 11 operations
api_count: 9
apis:
- description: DartAPI is Dartmouth's institutional API platform, documenting resource APIs such as the People API (directory information like name and email for Dartmouth identities) and a Nextgen API for student e
  name: DartAPI Developer Portal
  slug: dartapi
- description: An OpenAI-compatible REST API exposing large language models, embedding models, and reranking models deployed on Dartmouth's compute infrastructure as well as third-party cloud models made available b
  name: Dartmouth Chat AI API
  slug: chat-ai
- description: The Catalog API from Dartmouth College — 1 operation(s) for catalog.
  name: Dartmouth College Catalog API
  slug: dartmouth-catalog-api
- description: The Collection API from Dartmouth College — 2 operation(s) for collection.
  name: Dartmouth College Collection API
  slug: dartmouth-collection-api
- description: The OgcItem API from Dartmouth College — 4 operation(s) for ogcitem.
  name: Dartmouth College OgcItem API
  slug: dartmouth-ogcitem-api
- description: The OgcItemAggregation API from Dartmouth College — 1 operation(s) for ogcitemaggregation.
  name: Dartmouth College OgcItemAggregation API
  slug: dartmouth-ogcitemaggregation-api
- description: The OgcRoot API from Dartmouth College — 1 operation(s) for ogcroot.
  name: Dartmouth College OgcRoot API
  slug: dartmouth-ogcroot-api
- description: The OgcRootConformance API from Dartmouth College — 1 operation(s) for ogcrootconformance.
  name: Dartmouth College OgcRootConformance API
  slug: dartmouth-ogcrootconformance-api
- description: The Queryable API from Dartmouth College — 1 operation(s) for queryable.
  name: Dartmouth College Queryable API
  slug: dartmouth-queryable-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dartmouth-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dartmouth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://home.dartmouth.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dartmouth
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dartmouth-dltg
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dartmouth.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/dartmouth-college/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/dartmouth
- group: auth
  title: ''
  type: Authentication
  url: https://login.dartmouth.edu/cas/login
- group: commercial
  title: ''
  type: Plans
  url: plans/dartmouth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dartmouth-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dartmouth-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://home.dartmouth.edu/rss.xml
created: '2026-06-03'
description: 'Dartmouth College is a private Ivy League research university in Hanover, New Hampshire, United States, ranked #243 in the QS World University Rankings 2025. Its public developer footprint centers on the DartAPI developer portal (developer.dartmouth.edu), which documents institutional resource APIs (such as a People/directory API) gated behind Dartmouth CAS authentication and manually issued API keys. Dartmouth also operates a public ArcGIS Hub open-data portal, an OpenAI-compatible Dartmouth Chat AI API for hosted/on-premise models, and active GitHub organizations including the Digital Library Technologies Group.'
examples:
- key_count: 5
  name: Dartmouth Search Items Example
  slug: dartmouth-search-items-example
finops:
- name: Dartmouth Finops
  service_category: Education
  slug: dartmouth-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dartmouth.png
json_schemas:
- name: Dartmouth Open Data OGC Item
  property_count: 4
  slug: dartmouth-item
- name: Dartmouth Open Data OGC Item Collection
  property_count: 5
  slug: dartmouth-itemcollection
json_structures:
- name: Dartmouth Item Structure
  property_count: 4
  slug: dartmouth-item-structure
- name: Dartmouth Itemcollection Structure
  property_count: 5
  slug: dartmouth-itemcollection-structure
jsonld:
- class_count: 20
  name: Dartmouth Context
  property_count: 2
  slug: dartmouth-context
layout: provider
modified: '2026-06-03'
name: Dartmouth College
nav: Providers
network: true
overview: 'Dartmouth College publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Collection API, OgcItem API, and 4 more. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Dartmouth College catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Dartmouth College''s developer surface includes GitHub presence, authentication, engineering blog, and 11 more developer resources.'
plans:
- name: Dartmouth Plans Pricing
  plan_count: 2
  slug: dartmouth-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 1
  name: Dartmouth Rate Limits
  slug: dartmouth-rate-limits
rules:
- name: Dartmouth College API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dartmouth-jsonschema-spectral-rules
- name: Dartmouth College API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: dartmouth-rules
score:
  band: thin
  composite: 39.2
  delta: -4.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.4
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dartmouth/refs/heads/main/screenshots/dartmouth-2026-07-25T211220.png
security:
- kind: domain-security
  name: Dartmouth Domain Security
  slug: dartmouth-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: dartmouth
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Artificial Intelligence
- United States
- Ivy League
website: https://home.dartmouth.edu/
---
