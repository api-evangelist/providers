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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Pdb Agentic Access
  operation_count: 28
  slug: pdb-agentic-access
  summary_line: 28 operations · 10 acting
api_count: 7
apis:
- description: Provides structured access to the complete RCSB PDB holdings via REST and GraphQL interfaces. Given a known PDB identifier, callers can retrieve rich JSON metadata about entries, polymer entities, non
  name: RCSB PDB Data API
  slug: rcsb-pdb-data-api
- description: GraphQL service providing sequence-level alignments between structural databases and external sequence resources. Exposes two core queries — alignment and annotations — enabling callers to map PDB cha
  name: RCSB PDB Sequence Coordinates API
  slug: rcsb-pdb-sequence-coordinates-api
- description: Asynchronous REST API that performs programmatic structure alignment calculations between PDB entries or user-supplied coordinate files. Callers submit an alignment job via POST /submit (accepting PDB
  name: RCSB PDB Structure Alignment API
  slug: rcsb-pdb-alignment-api
- description: The General API from RCSB PDB — 12 operation(s) for general.
  name: RCSB PDB General API
  slug: pdb-general-api
- description: The Metadata Service API from RCSB PDB — 3 operation(s) for metadata service.
  name: RCSB PDB Metadata Service API
  slug: pdb-metadata-service-api
- description: The Search Service API from RCSB PDB — 2 operation(s) for search service.
  name: RCSB PDB Search Service API
  slug: pdb-search-service-api
- description: The Suggest Service API from RCSB PDB — 1 operation(s) for suggest service.
  name: RCSB PDB Suggest Service API
  slug: pdb-suggest-service-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pdb-domain-security.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/pdb.json
- group: company
  title: ''
  type: Website
  url: https://www.rcsb.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.rcsb.org/docs/programmatic-access/web-apis-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.rcsb.org/docs/programmatic-access
- group: other
  title: ''
  type: FileDownloads
  url: https://files.wwpdb.org
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rcsb
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/rcsb/py-rcsb-api
- group: build
  title: ''
  type: JavaScriptSDK
  url: https://github.com/rcsb/rcsb-api-tools
- group: operate
  title: ''
  type: StatusPage
  url: https://www.rcsb.org/pages/policies
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pdb-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pdb-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pdb-finops.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:info@rcsb.org
- group: other
  title: ''
  type: MailingList
  url: https://groups.google.com/g/rcsb-pdb-api-announcements
created: '2026-06-13'
description: RCSB Protein Data Bank (RCSB PDB) is a scientific data resource providing free, open access to the 3D structural data of biological macromolecules including proteins, nucleic acids, and complex assemblies. It serves researchers worldwide through a suite of programmatic APIs covering data retrieval, full-text and attribute search, sequence and structure similarity search, molecular model data access, volumetric electron density maps, sequence coordinate alignments, and structure alignment calculations.
finops:
- name: Pdb Finops
  service_category: Open Scientific Data API
  slug: pdb-finops
graphqls:
- description: The RCSB PDB GraphQL API provides flexible, field-selective access to the complete structural biology holdings of the Protein Data Bank. Callers can retrieve richly nested metadata about entries, poly
  name: RCSB Protein Data Bank GraphQL API
  slug: pdb-graphql
image: https://www.rcsb.org/img/rcsb_logo.png
layout: provider
modified: '2026-06-13'
name: RCSB PDB
nav: Providers
network: true
overview: 'RCSB PDB publishes 4 APIs on the [APIs.io](https://apis.io/) network, including General API, Metadata Service API, Search Service API, and 1 more. Tagged areas include Structural Biology, Proteomics, Bioinformatics, Genomics, and Life Sciences.


  RCSB PDB''s developer surface includes documentation, getting-started guide, GitHub presence, and 13 more developer resources.'
plans:
- name: Pdb Plans Pricing
  plan_count: 1
  slug: pdb-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 7
  name: Pdb Rate Limits
  slug: pdb-rate-limits
score:
  band: thin
  composite: 31.3
  delta: -0.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 46.1
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pdb/refs/heads/main/screenshots/pdb-2026-06-20T191514.png
security:
- kind: domain-security
  name: Pdb Domain Security
  slug: pdb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pdb
tags:
- Structural Biology
- Proteomics
- Bioinformatics
- Genomics
- Life Sciences
- Open Data
- Research
- Macromolecules
- Crystallography
- NMR
website: https://www.rcsb.org
---
