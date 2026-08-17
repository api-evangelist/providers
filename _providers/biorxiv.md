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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Biorxiv Agentic Access
  operation_count: 9
  slug: biorxiv-agentic-access
  summary_line: 9 operations
api_count: 7
apis:
- description: The Details API from bioRxiv — 2 operation(s) for details.
  name: bioRxiv Details API
  slug: biorxiv-details-api
- description: The Funder API from bioRxiv — 1 operation(s) for funder.
  name: bioRxiv Funder API
  slug: biorxiv-funder-api
- description: The Pub API from bioRxiv — 1 operation(s) for pub.
  name: bioRxiv Pub API
  slug: biorxiv-pub-api
- description: The Publisher API from bioRxiv — 1 operation(s) for publisher.
  name: bioRxiv Publisher API
  slug: biorxiv-publisher-api
- description: The Pubs API from bioRxiv — 2 operation(s) for pubs.
  name: bioRxiv Pubs API
  slug: biorxiv-pubs-api
- description: The Sum API from bioRxiv — 1 operation(s) for sum.
  name: bioRxiv Sum API
  slug: biorxiv-sum-api
- description: The Usage API from bioRxiv — 1 operation(s) for usage.
  name: bioRxiv Usage API
  slug: biorxiv-usage-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: bioRxiv REST Details API
  slug: open-biorxiv-details-api
- collection_type: open
  name: bioRxiv REST Details Funder API
  slug: open-biorxiv-funder-api
- collection_type: open
  name: bioRxiv REST Details Pub API
  slug: open-biorxiv-pub-api
- collection_type: open
  name: bioRxiv REST Details Publisher API
  slug: open-biorxiv-publisher-api
- collection_type: open
  name: bioRxiv REST Details Pubs API
  slug: open-biorxiv-pubs-api
- collection_type: open
  name: bioRxiv REST Details Sum API
  slug: open-biorxiv-sum-api
- collection_type: open
  name: bioRxiv REST Details Usage API
  slug: open-biorxiv-usage-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/biorxiv-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/biorxiv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biorxiv.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.biorxiv.org/content/about-biorxiv
- group: company
  title: ''
  type: About
  url: https://www.biorxiv.org/about-biorxiv
created: '2026-06-13'
description: Cold Spring Harbor Laboratory preprint server for biology providing a REST API for searching and accessing preprint metadata, full text, and category-filtered biological research. The API enables programmatic access to preprint and published article metadata from bioRxiv and medRxiv repositories.
examples:
- key_count: 2
  name: Content Details Response
  slug: content-details-response
- key_count: 2
  name: Content Summary Statistics Response
  slug: content-summary-statistics-response
- key_count: 2
  name: Published Preprint Response
  slug: published-preprint-response
- key_count: 2
  name: Usage Statistics Response
  slug: usage-statistics-response
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/biorxiv.png
json_schemas:
- name: PreprintMetadata
  property_count: 14
  slug: preprint-metadata
- name: PublishedPreprintMetadata
  property_count: 12
  slug: published-preprint
- name: StatisticsSchemas
  property_count: 0
  slug: statistics
jsonld:
- class_count: 24
  name: context Context
  property_count: 26
  slug: context
layout: provider
modified: '2026-06-13'
name: bioRxiv
nav: Providers
network: true
overview: 'bioRxiv publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Details API, Funder API, Pub API, and 4 more. Tagged areas include Biology, Preprints, Research, Open Access, and Life Sciences.


  The bioRxiv catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 26
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: bioRxiv API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: biorxiv-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 65.0
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 35.6
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
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/biorxiv/refs/heads/main/screenshots/biorxiv-2026-06-20T173251.png
security:
- kind: domain-security
  name: Biorxiv Domain Security
  slug: biorxiv-domain-security
  summary_line: TLSv1.3
slug: biorxiv
tags:
- Biology
- Preprints
- Research
- Open Access
- Life Sciences
- Scientific Publications
website: https://www.biorxiv.org/
---
