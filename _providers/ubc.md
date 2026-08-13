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
    dry_run_mode: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 177
  human_in_the_loop: 5
  name: Ubc Agentic Access
  operation_count: 378
  slug: ubc-agentic-access
  summary_line: 378 operations · 177 acting · 5 human-in-the-loop
api_count: 25
apis:
- description: Public REST/JSON API over UBC Library's Open Collections, the university's digitized historical and research collections. Backed by an ElasticSearch index, it exposes search and collection-listing end
  name: UBC Library Open Collections API
  slug: open-collections
- description: 'OAI-PMH metadata-harvesting endpoint exposed by UBC Library Open Collections, supporting the standard Open Archives Initiative Protocol for Metadata Harvesting verbs (Identify, ListRecords, etc.) for '
  name: UBC Library OAI-PMH Endpoint
  slug: oai-pmh
- description: Enterprise/institutional APIs delivered by the Office of the CIO's Integration Enablement Centre using MuleSoft, aligned with the University Data Model and secured through a Data Access Framework. The
  name: UBC Integration Enablement Centre APIs (MuleSoft / DAF)
  slug: iec-mulesoft
- description: The Access API from University of British Columbia — 20 operation(s) for access.
  name: University of British Columbia Access API
  slug: ubc-access-api
- description: The Admin API from University of British Columbia — 113 operation(s) for admin.
  name: University of British Columbia Admin API
  slug: ubc-admin-api
- description: The Batch API from University of British Columbia — 3 operation(s) for batch.
  name: University of British Columbia Batch API
  slug: ubc-batch-api
- description: The Builtin Users API from University of British Columbia — 4 operation(s) for builtin users.
  name: University of British Columbia Builtin Users API
  slug: ubc-builtin-users-api
- description: The Datasets API from University of British Columbia — 54 operation(s) for datasets.
  name: University of British Columbia Datasets API
  slug: ubc-datasets-api
- description: The Datatags API from University of British Columbia — 1 operation(s) for datatags.
  name: University of British Columbia Datatags API
  slug: ubc-datatags-api
- description: The Dataverses API from University of British Columbia — 26 operation(s) for dataverses.
  name: University of British Columbia Dataverses API
  slug: ubc-dataverses-api
- description: The Edit API from University of British Columbia — 1 operation(s) for edit.
  name: University of British Columbia Edit API
  slug: ubc-edit-api
- description: The Files API from University of British Columbia — 9 operation(s) for files.
  name: University of British Columbia Files API
  slug: ubc-files-api
- description: The Harvest API from University of British Columbia — 7 operation(s) for harvest.
  name: University of British Columbia Harvest API
  slug: ubc-harvest-api
- description: The Info API from University of British Columbia — 40 operation(s) for info.
  name: University of British Columbia Info API
  slug: ubc-info-api
- description: The Ingest API from University of British Columbia — 1 operation(s) for ingest.
  name: University of British Columbia Ingest API
  slug: ubc-ingest-api
- description: The Mail API from University of British Columbia — 1 operation(s) for mail.
  name: University of British Columbia Mail API
  slug: ubc-mail-api
- description: The Meta API from University of British Columbia — 2 operation(s) for meta.
  name: University of British Columbia Meta API
  slug: ubc-meta-api
- description: The Metadatablocks API from University of British Columbia — 2 operation(s) for metadatablocks.
  name: University of British Columbia Metadatablocks API
  slug: ubc-metadatablocks-api
- description: The Mydata API from University of British Columbia — 1 operation(s) for mydata.
  name: University of British Columbia Mydata API
  slug: ubc-mydata-api
- description: The Notifications API from University of British Columbia — 1 operation(s) for notifications.
  name: University of British Columbia Notifications API
  slug: ubc-notifications-api
- description: The Pids API from University of British Columbia — 4 operation(s) for pids.
  name: University of British Columbia Pids API
  slug: ubc-pids-api
- description: The Roles API from University of British Columbia — 2 operation(s) for roles.
  name: University of British Columbia Roles API
  slug: ubc-roles-api
- description: The Search API from University of British Columbia — 1 operation(s) for search.
  name: University of British Columbia Search API
  slug: ubc-search-api
- description: The Users API from University of British Columbia — 8 operation(s) for users.
  name: University of British Columbia Users API
  slug: ubc-users-api
- description: The Workflows API from University of British Columbia — 1 operation(s) for workflows.
  name: University of British Columbia Workflows API
  slug: ubc-workflows-api
artifact_total: 41
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ubc-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ubc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ubc.ca/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ubc-library
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ubc/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.library.ubc.ca/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/ubc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ubc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ubc-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://news.ubc.ca/feed/
created: '2026-06-03'
description: 'The University of British Columbia (UBC) is a public research university in Vancouver and Kelowna, British Columbia, Canada, ranked #33 in the QS World University Rankings 2025. UBC''s public developer footprint is led by UBC Library, which operates the Open Collections API (an ElasticSearch-backed REST API over digitized collections) and the Abacus Dataverse research-data repository (a standard Dataverse REST API), along with an OAI-PMH harvesting endpoint. Institutional/enterprise data APIs are delivered through the Office of the CIO''s Integration Enablement Centre via MuleSoft and a Data Access Framework, which are gated behind a formal data access request rather than a self-service public developer portal.'
examples:
- key_count: 3
  name: Ubc Get Dataverse Example
  slug: ubc-get-dataverse-example
- key_count: 3
  name: Ubc Search Datasets Example
  slug: ubc-search-datasets-example
finops:
- name: Ubc Finops
  service_category: Education
  slug: ubc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ubc.png
json_schemas:
- name: UBC Abacus Dataverse DataFile
  property_count: 14
  slug: ubc-datafile
- name: UBC Abacus Dataverse Dataset
  property_count: 16
  slug: ubc-dataset
- name: UBC Abacus Dataverse Collection
  property_count: 11
  slug: ubc-dataverse
json_structures:
- name: Ubc Dataset Structure
  property_count: 13
  slug: ubc-dataset-structure
- name: Ubc Dataverse Structure
  property_count: 8
  slug: ubc-dataverse-structure
jsonld:
- class_count: 15
  name: Ubc Context
  property_count: 9
  slug: ubc-context
layout: provider
modified: '2026-06-03'
name: University of British Columbia
nav: Providers
network: true
overview: 'University of British Columbia publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Access API, Admin API, Batch API, and 19 more. Tagged areas include Education, Higher Education, University, Canada, and Library.


  The University of British Columbia catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of British Columbia''s developer surface includes GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Ubc Plans Pricing
  plan_count: 2
  slug: ubc-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 1
  name: Ubc Rate Limits
  slug: ubc-rate-limits
rules:
- name: University of British Columbia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ubc-jsonschema-spectral-rules
- name: University of British Columbia API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: ubc-rules
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.2
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ubc/refs/heads/main/screenshots/ubc-2026-06-20T195923.png
security:
- kind: domain-security
  name: Ubc Domain Security
  slug: ubc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ubc Vulnerability Disclosure
  slug: ubc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ubc
tags:
- Education
- Higher Education
- University
- Canada
- Library
- Open Data
- Research Data
- Digital Collections
website: https://www.ubc.ca/
---
