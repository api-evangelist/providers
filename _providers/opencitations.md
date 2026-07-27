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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-27'
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
artifact_total: 15
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
random_paper: 48
score:
  band: emerging
  composite: 29.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 70.3
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.8
  schema_version: 0.5
  scored_at: '2026-07-27'
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
