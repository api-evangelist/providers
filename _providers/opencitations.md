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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Opencitations Agentic Access
  operation_count: 9
  slug: opencitations-agentic-access
  summary_line: 9 operations
api_count: 2
apis:
- description: SPARQL endpoints for structured queries against the OpenCitations Meta and Index datasets. Provides access to the full Linked Open Data graph for both bibliographic metadata and citation entity data u
  name: OpenCitations SPARQL Endpoint
  slug: opencitations-sparql-endpoint
- baseURL: https://api.opencitations.net/index/v2
  baseurl_source: declared
  description: Operations for retrieving works by author
  name: OpenCitations Authors API
  slug: opencitations-authors-api
- baseURL: https://api.opencitations.net/index/v2
  baseurl_source: declared
  description: Operations for retrieving citation metadata and counts
  name: OpenCitations Citations API
  slug: opencitations-citations-api
- baseURL: https://api.opencitations.net/index/v2
  baseurl_source: declared
  description: Operations for retrieving works by editor
  name: OpenCitations Editors API
  slug: opencitations-editors-api
- baseURL: https://api.opencitations.net/index/v2
  baseurl_source: declared
  description: Operations for retrieving bibliographic metadata
  name: OpenCitations Metadata API
  slug: opencitations-metadata-api
- baseURL: https://api.opencitations.net/index/v2
  baseurl_source: declared
  description: Operations for retrieving outgoing reference data
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
random_paper: 1
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 63.4
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.3
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
