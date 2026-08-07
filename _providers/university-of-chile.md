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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 201
  human_in_the_loop: 5
  name: University Of Chile Agentic Access
  operation_count: 419
  slug: university-of-chile-agentic-access
  summary_line: 419 operations · 201 acting · 5 human-in-the-loop
api_count: 25
apis:
- description: The University of Chile institutional repository (Repositorio Academico), managed by SISIB and built on DSpace, exposes an OAI-PMH 2.0 interface for harvesting Dublin Core / metadata records of theses
  name: Repositorio Academico OAI-PMH
  slug: repositorio-oai-pmh
- description: The Access API from University of Chile — 20 operation(s) for access.
  name: University of Chile Access API
  slug: university-of-chile-access-api
- description: The Admin API from University of Chile — 120 operation(s) for admin.
  name: University of Chile Admin API
  slug: university-of-chile-admin-api
- description: The Batch API from University of Chile — 3 operation(s) for batch.
  name: University of Chile Batch API
  slug: university-of-chile-batch-api
- description: The Builtin Users API from University of Chile — 4 operation(s) for builtin users.
  name: University of Chile Builtin Users API
  slug: university-of-chile-builtin-users-api
- description: The Datasets API from University of Chile — 62 operation(s) for datasets.
  name: University of Chile Datasets API
  slug: university-of-chile-datasets-api
- description: The Datatags API from University of Chile — 1 operation(s) for datatags.
  name: University of Chile Datatags API
  slug: university-of-chile-datatags-api
- description: The Dataverses API from University of Chile — 28 operation(s) for dataverses.
  name: University of Chile Dataverses API
  slug: university-of-chile-dataverses-api
- description: The Edit API from University of Chile — 1 operation(s) for edit.
  name: University of Chile Edit API
  slug: university-of-chile-edit-api
- description: The Files API from University of Chile — 13 operation(s) for files.
  name: University of Chile Files API
  slug: university-of-chile-files-api
- description: The Harvest API from University of Chile — 7 operation(s) for harvest.
  name: University of Chile Harvest API
  slug: university-of-chile-harvest-api
- description: The Inbox API from University of Chile — 1 operation(s) for inbox.
  name: University of Chile Inbox API
  slug: university-of-chile-inbox-api
- description: The Info API from University of Chile — 40 operation(s) for info.
  name: University of Chile Info API
  slug: university-of-chile-info-api
- description: The Ingest API from University of Chile — 1 operation(s) for ingest.
  name: University of Chile Ingest API
  slug: university-of-chile-ingest-api
- description: The Licenses API from University of Chile — 6 operation(s) for licenses.
  name: University of Chile Licenses API
  slug: university-of-chile-licenses-api
- description: The Mail API from University of Chile — 1 operation(s) for mail.
  name: University of Chile Mail API
  slug: university-of-chile-mail-api
- description: The Meta API from University of Chile — 2 operation(s) for meta.
  name: University of Chile Meta API
  slug: university-of-chile-meta-api
- description: The Metadatablocks API from University of Chile — 2 operation(s) for metadatablocks.
  name: University of Chile Metadatablocks API
  slug: university-of-chile-metadatablocks-api
- description: The Mydata API from University of Chile — 1 operation(s) for mydata.
  name: University of Chile Mydata API
  slug: university-of-chile-mydata-api
- description: The Notifications API from University of Chile — 6 operation(s) for notifications.
  name: University of Chile Notifications API
  slug: university-of-chile-notifications-api
- description: The Pids API from University of Chile — 4 operation(s) for pids.
  name: University of Chile Pids API
  slug: university-of-chile-pids-api
- description: The Roles API from University of Chile — 2 operation(s) for roles.
  name: University of Chile Roles API
  slug: university-of-chile-roles-api
- description: The Search API from University of Chile — 1 operation(s) for search.
  name: University of Chile Search API
  slug: university-of-chile-search-api
- description: The Users API from University of Chile — 8 operation(s) for users.
  name: University of Chile Users API
  slug: university-of-chile-users-api
- description: The Workflows API from University of Chile — 1 operation(s) for workflows.
  name: University of Chile Workflows API
  slug: university-of-chile-workflows-api
artifact_total: 41
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-chile-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-chile-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uchile.cl/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/eol-uchile
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/open-uchile
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universidad-de-chile/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-chile-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-chile-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-chile-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-chile-context.jsonld
created: '2026-06-03'
description: 'The University of Chile (Universidad de Chile, UChile) is the country''s oldest public university, founded in 1842 in Santiago, and is ranked #139 in the QS World University Rankings 2025. Its public, machine-readable footprint is centered on research and scholarly infrastructure rather than a single branded developer portal: a Dataverse-based research data repository (datos.uchile.cl) that exposes the standard Dataverse REST API, and a DSpace institutional repository (repositorio.uchile.cl) that exposes an OAI-PMH interface for metadata harvesting. The university also maintains official open-source GitHub organizations for its Open edX online-education platform. No general-purpose, self-service developer program with API keys was confirmed; access is via open standards and open data.'
examples:
- key_count: 2
  name: University Of Chile Info Version Example
  slug: university-of-chile-info-version-example
- key_count: 2
  name: University Of Chile Search Example
  slug: university-of-chile-search-example
finops:
- name: University Of Chile Finops
  service_category: Education
  slug: university-of-chile-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-chile.png
json_schemas:
- name: Dataverse DataFile
  property_count: 21
  slug: university-of-chile-datafile
- name: Dataverse Dataset
  property_count: 20
  slug: university-of-chile-dataset
- name: Dataverse Collection
  property_count: 18
  slug: university-of-chile-dataverse
- name: Dataverse Search Result Item (dataset)
  property_count: 23
  slug: university-of-chile-search-item
json_structures:
- name: University Of Chile Dataset Structure
  property_count: 13
  slug: university-of-chile-dataset-structure
- name: University Of Chile Dataverse Structure
  property_count: 11
  slug: university-of-chile-dataverse-structure
jsonld:
- class_count: 21
  name: University Of Chile Context
  property_count: 7
  slug: university-of-chile-context
layout: provider
modified: '2026-06-03'
name: University of Chile
nav: Providers
network: true
overview: 'University of Chile publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Access API, Admin API, Batch API, and 21 more. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The University of Chile catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Chile''s developer surface includes GitHub presence and 10 more developer resources.'
plans:
- name: University Of Chile Plans Pricing
  plan_count: 2
  slug: university-of-chile-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: University Of Chile Rate Limits
  slug: university-of-chile-rate-limits
rules:
- name: University of Chile API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-chile-jsonschema-spectral-rules
- name: University of Chile API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: university-of-chile-rules
score:
  band: thin
  composite: 32.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 44.4
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-chile/refs/heads/main/screenshots/university-of-chile-2026-06-20T200146.png
security:
- kind: domain-security
  name: University Of Chile Domain Security
  slug: university-of-chile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-chile
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- Repository
- OAI-PMH
- Dataverse
- Chile
website: https://uchile.cl/
---
