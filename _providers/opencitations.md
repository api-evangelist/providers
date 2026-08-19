---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Opencitations Agentic Access
  operation_count: 9
  slug: opencitations-agentic-access
  summary_line: 9 operations
api_count: 6
apis:
- description: SPARQL endpoints for structured queries against the OpenCitations Meta and Index datasets. Provides access to the full Linked Open Data graph for both bibliographic metadata and citation entity data u
  name: OpenCitations SPARQL Endpoint
  slug: opencitations-sparql-endpoint
- description: Operations for retrieving works by author
  name: OpenCitations Authors API
  slug: opencitations-authors-api
- description: Operations for retrieving citation metadata and counts
  name: OpenCitations Citations API
  slug: opencitations-citations-api
- description: Operations for retrieving works by editor
  name: OpenCitations Editors API
  slug: opencitations-editors-api
- description: Operations for retrieving bibliographic metadata
  name: OpenCitations Metadata API
  slug: opencitations-metadata-api
- description: Operations for retrieving outgoing reference data
  name: OpenCitations References API
  slug: opencitations-references-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenCitations Index REST Authors API
  slug: open-opencitations-authors-api
- collection_type: open
  name: OpenCitations Index REST Authors Citations API
  slug: open-opencitations-citations-api
- collection_type: open
  name: OpenCitations Index REST Authors Editors API
  slug: open-opencitations-editors-api
- collection_type: open
  name: OpenCitations Index REST Authors Metadata API
  slug: open-opencitations-metadata-api
- collection_type: open
  name: OpenCitations Index REST Authors References API
  slug: open-opencitations-references-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opencitations-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opencitations-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opencitations-authentication.yml
created: '2024-01-01'
description: OpenCitations is an open science research infrastructure providing free access to scholarly bibliographic and citation data. It offers REST APIs for querying citation networks, DOI-based citation lookups, reference data, and bibliographic metadata from millions of research articles. All data is published under CC0 Public Domain Waiver for unrestricted reuse.
examples:
- key_count: 4
  name: Author Works
  slug: author-works
- key_count: 4
  name: Citation By Oci
  slug: citation-by-oci
- key_count: 4
  name: Citation Count
  slug: citation-count
- key_count: 5
  name: Incoming Citations
  slug: incoming-citations
- key_count: 4
  name: Metadata Lookup
  slug: metadata-lookup
image: https://opencitations.net/static/favicon.ico
jsonld:
- class_count: 24
  name: Opencitations Context
  property_count: 13
  slug: opencitations
layout: provider
modified: '2026-06-13'
name: OpenCitations
nav: Providers
network: true
overview: 'OpenCitations publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authors API, Citations API, Editors API, and 2 more. Tagged areas include Citations, Scholarly, Research, Open Science, and Bibliometrics.


  The OpenCitations catalog on APIs.io includes 1 JSON-LD context.


  OpenCitations'' developer surface includes authentication and 2 more developer resources.'
random_paper: 67
score:
  band: thin
  composite: 27.4
  delta: -0.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 65.2
    developer_ergonomics: 11.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 27.7
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
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opencitations/refs/heads/main/screenshots/opencitations-2026-06-20T190921.png
security:
- kind: authentication
  name: Opencitations Authentication
  slug: opencitations-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Opencitations Domain Security
  slug: opencitations-domain-security
  summary_line: TLSv1.3
slug: opencitations
tags:
- Citations
- Scholarly
- Research
- Open Science
- Bibliometrics
- DOI
- Academic
website: https://opencitations.net
---
