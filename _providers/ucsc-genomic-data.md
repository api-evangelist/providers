---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ucsc Genomic Data Agentic Access
  operation_count: 12
  slug: ucsc-genomic-data-agentic-access
  summary_line: 12 operations
api_count: 5
apis:
- description: Genome assembly discovery and search
  name: UCSC Genomic Data Genomes API
  slug: ucsc-genomic-data-genomes-api
- description: Track hub management
  name: UCSC Genomic Data Hubs API
  slug: ucsc-genomic-data-hubs-api
- description: Genome browser search
  name: UCSC Genomic Data Search API
  slug: ucsc-genomic-data-search-api
- description: DNA sequence retrieval
  name: UCSC Genomic Data Sequences API
  slug: ucsc-genomic-data-sequences-api
- description: Annotation track listings and data retrieval
  name: UCSC Genomic Data Tracks API
  slug: ucsc-genomic-data-tracks-api
artifact_total: 20
collections:
- collection_type: open
  name: UCSC Genome Browser REST API
  slug: open-ucsc-genomic-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ucsc-genomic-data-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ucsc-genomic-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucsc-genomic-data-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ucscgenomebrowser
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ucsc-genomics-institute
- group: company
  title: ''
  type: Blog
  url: https://genome-blog.soe.ucsc.edu/blog/feed
created: '2025-03-01'
description: The UCSC Genome Browser is a widely-used bioinformatics tool providing access to genomic data, sequence information, and annotation tracks for hundreds of organisms. The REST API provides programmatic access to genome assemblies, DNA sequences, annotation tracks, and track hubs. No authentication is required; rate limiting of one request per second is recommended. Data is returned in JSON format.
examples:
- key_count: 2
  name: Ucsc Get Dna Sequence Example
  slug: ucsc-get-dna-sequence-example
- key_count: 2
  name: Ucsc List Tracks Example
  slug: ucsc-list-tracks-example
finops:
- name: Ucsc Genomic Data Finops
  service_category: API
  slug: ucsc-genomic-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucsc-genomic-data.png
json_schemas:
- name: UCSC DNA Sequence Result
  property_count: 5
  slug: ucsc-genomic-data-sequence
- name: UCSC Genome Browser Track
  property_count: 7
  slug: ucsc-genomic-data-track
json_structures:
- name: Ucsc Genomic Data Structure
  property_count: 0
  slug: ucsc-genomic-data-structure
jsonld:
- class_count: 5
  name: Ucsc Genomic Data Context
  property_count: 16
  slug: ucsc-genomic-data-context
layout: provider
modified: '2026-05-19'
name: UCSC Genomic Data
nav: Providers
network: true
overview: 'UCSC Genomic Data publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Genomes API, Hubs API, Search API, and 2 more. Tagged areas include Genomics, Bioinformatics, DNA, Biology, and Research.


  The UCSC Genomic Data catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  UCSC Genomic Data''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Ucsc Genomic Data Plans Pricing
  plan_count: 3
  slug: ucsc-genomic-data-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Ucsc Genomic Data Rate Limits
  slug: ucsc-genomic-data-rate-limits
rules:
- name: UCSC Genomic Data API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ucsc-genomic-data-jsonschema-spectral-rules
- name: UCSC Genomic Data API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: ucsc-genomic-data-rules
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 71.9
    developer_ergonomics: 2.2
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucsc-genomic-data/refs/heads/main/screenshots/ucsc-genomic-data-2026-06-20T195951.png
security:
- kind: domain-security
  name: Ucsc Genomic Data Domain Security
  slug: ucsc-genomic-data-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ucsc Genomic Data Vulnerability Disclosure
  slug: ucsc-genomic-data-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ucsc-genomic-data
tags:
- Genomics
- Bioinformatics
- DNA
- Biology
- Research
- Open Science
---
