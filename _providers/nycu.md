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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 181
  human_in_the_loop: 5
  name: Nycu Agentic Access
  operation_count: 387
  slug: nycu-agentic-access
  summary_line: 387 operations · 181 acting · 5 human-in-the-loop
api_count: 25
apis:
- description: OAuth 2.0 (RFC 6749) authorization-code service for third-party applications to authenticate NYCU users and retrieve consented user data (email/username via the profile scope, name via the name scope,
  name: NYCU OAuth / Single Sign-On API
  slug: oauth
- description: OAI-PMH 2.0 metadata-harvesting endpoint ("NYCU Dataverse Dataverse OAI Archive") for harvesting dataset metadata from the NYCU Dataverse research-data repository.
  name: NYCU Dataverse OAI-PMH Endpoint
  slug: oai-pmh
- description: The Access API from National Yang Ming Chiao Tung University — 20 operation(s) for access.
  name: National Yang Ming Chiao Tung University Access API
  slug: nycu-access-api
- description: The Admin API from National Yang Ming Chiao Tung University — 113 operation(s) for admin.
  name: National Yang Ming Chiao Tung University Admin API
  slug: nycu-admin-api
- description: The Batch API from National Yang Ming Chiao Tung University — 3 operation(s) for batch.
  name: National Yang Ming Chiao Tung University Batch API
  slug: nycu-batch-api
- description: The Builtin Users API from National Yang Ming Chiao Tung University — 4 operation(s) for builtin users.
  name: National Yang Ming Chiao Tung University Builtin Users API
  slug: nycu-builtin-users-api
- description: The Datasets API from National Yang Ming Chiao Tung University — 56 operation(s) for datasets.
  name: National Yang Ming Chiao Tung University Datasets API
  slug: nycu-datasets-api
- description: The Datatags API from National Yang Ming Chiao Tung University — 1 operation(s) for datatags.
  name: National Yang Ming Chiao Tung University Datatags API
  slug: nycu-datatags-api
- description: The Dataverses API from National Yang Ming Chiao Tung University — 26 operation(s) for dataverses.
  name: National Yang Ming Chiao Tung University Dataverses API
  slug: nycu-dataverses-api
- description: The Edit API from National Yang Ming Chiao Tung University — 1 operation(s) for edit.
  name: National Yang Ming Chiao Tung University Edit API
  slug: nycu-edit-api
- description: The Files API from National Yang Ming Chiao Tung University — 9 operation(s) for files.
  name: National Yang Ming Chiao Tung University Files API
  slug: nycu-files-api
- description: The Harvest API from National Yang Ming Chiao Tung University — 7 operation(s) for harvest.
  name: National Yang Ming Chiao Tung University Harvest API
  slug: nycu-harvest-api
- description: The Info API from National Yang Ming Chiao Tung University — 40 operation(s) for info.
  name: National Yang Ming Chiao Tung University Info API
  slug: nycu-info-api
- description: The Ingest API from National Yang Ming Chiao Tung University — 1 operation(s) for ingest.
  name: National Yang Ming Chiao Tung University Ingest API
  slug: nycu-ingest-api
- description: The Licenses API from National Yang Ming Chiao Tung University — 5 operation(s) for licenses.
  name: National Yang Ming Chiao Tung University Licenses API
  slug: nycu-licenses-api
- description: The Mail API from National Yang Ming Chiao Tung University — 1 operation(s) for mail.
  name: National Yang Ming Chiao Tung University Mail API
  slug: nycu-mail-api
- description: The Meta API from National Yang Ming Chiao Tung University — 2 operation(s) for meta.
  name: National Yang Ming Chiao Tung University Meta API
  slug: nycu-meta-api
- description: The Metadatablocks API from National Yang Ming Chiao Tung University — 2 operation(s) for metadatablocks.
  name: National Yang Ming Chiao Tung University Metadatablocks API
  slug: nycu-metadatablocks-api
- description: The Mydata API from National Yang Ming Chiao Tung University — 1 operation(s) for mydata.
  name: National Yang Ming Chiao Tung University Mydata API
  slug: nycu-mydata-api
- description: The Notifications API from National Yang Ming Chiao Tung University — 1 operation(s) for notifications.
  name: National Yang Ming Chiao Tung University Notifications API
  slug: nycu-notifications-api
- description: The Pids API from National Yang Ming Chiao Tung University — 4 operation(s) for pids.
  name: National Yang Ming Chiao Tung University Pids API
  slug: nycu-pids-api
- description: The Roles API from National Yang Ming Chiao Tung University — 2 operation(s) for roles.
  name: National Yang Ming Chiao Tung University Roles API
  slug: nycu-roles-api
- description: The Search API from National Yang Ming Chiao Tung University — 1 operation(s) for search.
  name: National Yang Ming Chiao Tung University Search API
  slug: nycu-search-api
- description: The Users API from National Yang Ming Chiao Tung University — 8 operation(s) for users.
  name: National Yang Ming Chiao Tung University Users API
  slug: nycu-users-api
- description: The Workflows API from National Yang Ming Chiao Tung University — 1 operation(s) for workflows.
  name: National Yang Ming Chiao Tung University Workflows API
  slug: nycu-workflows-api
artifact_total: 39
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nycu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nycu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nycu.edu.tw/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://id.nycu.edu.tw/docs/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/nycu/
- group: commercial
  title: ''
  type: Plans
  url: plans/nycu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nycu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nycu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'National Yang Ming Chiao Tung University (NYCU) is a public research university in Taiwan formed in 2021 from the merger of National Yang-Ming University and National Chiao Tung University, and ranked #219 in the QS World University Rankings 2025. Its public developer footprint centers on an OAuth 2.0 / single sign-on identity service (id.nycu.edu.tw) for third-party application integration, and the NYCU Dataverse research-data repository which exposes standard Dataverse REST APIs (Native and Search) and an OAI-PMH metadata-harvesting endpoint. Most administrative, course, and portal systems are gated behind institutional SSO rather than openly documented.'
examples:
- key_count: 2
  name: Nycu Info Version Example
  slug: nycu-info-version-example
- key_count: 2
  name: Nycu Search Example
  slug: nycu-search-example
finops:
- name: Nycu Finops
  service_category: Education
  slug: nycu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nycu.png
json_schemas:
- name: NYCU Dataverse Dataset
  property_count: 11
  slug: nycu-dataset
- name: NYCU Dataverse Search Response
  property_count: 2
  slug: nycu-search-result
json_structures:
- name: Nycu Dataset Structure
  property_count: 11
  slug: nycu-dataset-structure
- name: Nycu Search Result Structure
  property_count: 2
  slug: nycu-search-result-structure
jsonld:
- class_count: 12
  name: Nycu Context
  property_count: 11
  slug: nycu-context
layout: provider
modified: '2026-06-03'
name: National Yang Ming Chiao Tung University
nav: Providers
network: true
overview: 'National Yang Ming Chiao Tung University publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Access API, Admin API, Batch API, and 20 more. Tagged areas include Education, Higher Education, University, Taiwan, and Identity.


  The National Yang Ming Chiao Tung University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Nycu Plans Pricing
  plan_count: 2
  slug: nycu-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 1
  name: Nycu Rate Limits
  slug: nycu-rate-limits
rules:
- name: National Yang Ming Chiao Tung University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nycu-jsonschema-spectral-rules
- name: National Yang Ming Chiao Tung University API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 2
  slug: nycu-rules
score:
  band: thin
  composite: 34.0
  delta: -3.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 47.1
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nycu/refs/heads/main/screenshots/nycu-2026-06-20T190547.png
security:
- kind: domain-security
  name: Nycu Domain Security
  slug: nycu-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: nycu
tags:
- Education
- Higher Education
- University
- Taiwan
- Identity
- OAuth
- Research Data
- Open Data
- Library
website: https://www.nycu.edu.tw/
---
