---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kegg Agentic Access
  operation_count: 13
  slug: kegg-agentic-access
  summary_line: 13 operations
api_count: 8
apis:
- description: 'The KEGG REST API provides unified programmatic access to all KEGG databases through seven operations: INFO (database statistics and release notes), LIST (entry identifiers and names), FIND (keyword a'
  name: KEGG REST API
  slug: kegg-rest-api
- description: Convert identifiers between KEGG and external databases
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) conv API
  slug: kegg-conv-api
- description: Find adverse drug-drug interactions
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) ddi API
  slug: kegg-ddi-api
- description: Search entries by keyword or molecular property
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) find API
  slug: kegg-find-api
- description: Retrieve specific database entries
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) get API
  slug: kegg-get-api
- description: Display database release information and statistics
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) info API
  slug: kegg-info-api
- description: Find related entries using database cross-references
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) link API
  slug: kegg-link-api
- description: Obtain a list of entry identifiers and associated names
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) list API
  slug: kegg-list-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kegg-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kegg-domain-security.yml
created: '2026-06-13'
description: The Kyoto Encyclopedia of Genes and Genomes (KEGG) is an integrated database resource for understanding high-level functions and utilities of biological systems from molecular-level information derived from genome sequencing and other high-throughput experiments. The KEGG REST API at rest.kegg.jp provides programmatic access to KEGG databases covering biological pathways, metabolic networks, molecular interactions, drug targets, disease associations, chemical compounds, genomic sequences, and functional orthologs across thousands of organisms. The API exposes seven core operations — info, list, find, get, conv, link, and ddi — enabling identifier conversion, cross-database linking, keyword and structure searches, and full entry retrieval in text, KGML, and JSON formats. Academic use is free via the REST API; FTP and commercial access require subscriptions managed through NPO Bioinformatics Japan and Pathway Solutions.
finops:
- name: Overview
  service_category: ''
  slug: overview
image: https://www.kegg.jp/favicon.ico
layout: provider
modified: '2026-06-13'
name: Kyoto Encyclopedia of Genes and Genomes (KEGG)
nav: Providers
network: true
overview: Kyoto Encyclopedia of Genes and Genomes (KEGG) publishes 7 APIs on the [APIs.io](https://apis.io/) network, including conv API, ddi API, find API, and 4 more. Tagged areas include Bioinformatics, Genomics, Life Sciences, Pathways, and Metabolomics.
plans:
- name: Kegg Rest Api
  plan_count: 4
  slug: kegg-rest-api
random_paper: 6
rate_limits:
- limit_count: 0
  name: Kegg Rest Api
  slug: kegg-rest-api
score:
  band: emerging
  composite: 29.4
  delta: -2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.5
    developer_ergonomics: 0.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 32.3
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kegg/refs/heads/main/screenshots/kegg-2026-06-20T183941.png
security:
- kind: domain-security
  name: Kegg Domain Security
  slug: kegg-domain-security
  summary_line: TLSv1.2
slug: kegg
tags:
- Bioinformatics
- Genomics
- Life Sciences
- Pathways
- Metabolomics
- Drug Targets
- Disease
- Chemical Compounds
- Enzymes
- Orthology
website: https://www.kegg.jp/kegg/rest/
---
