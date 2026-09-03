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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kegg Agentic Access
  operation_count: 13
  slug: kegg-agentic-access
  summary_line: 13 operations
api_count: 1
apis:
- description: 'The KEGG REST API provides unified programmatic access to all KEGG databases through seven operations: INFO (database statistics and release notes), LIST (entry identifiers and names), FIND (keyword a'
  name: KEGG REST API
  slug: kegg-rest-api
- baseURL: https://rest.kegg.jp
  baseurl_source: declared
  description: Convert identifiers between KEGG and external databases
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) conv API
  slug: kegg-conv-api
- baseURL: https://rest.kegg.jp
  baseurl_source: declared
  description: Find adverse drug-drug interactions
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) ddi API
  slug: kegg-ddi-api
- baseURL: https://rest.kegg.jp
  baseurl_source: declared
  description: Search entries by keyword or molecular property
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) find API
  slug: kegg-find-api
- baseURL: https://rest.kegg.jp
  baseurl_source: declared
  description: Retrieve specific database entries
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) get API
  slug: kegg-get-api
- baseURL: https://rest.kegg.jp
  baseurl_source: declared
  description: Display database release information and statistics
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) info API
  slug: kegg-info-api
- baseURL: https://rest.kegg.jp
  baseurl_source: declared
  description: Find related entries using database cross-references
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) link API
  slug: kegg-link-api
- baseURL: https://rest.kegg.jp
  baseurl_source: declared
  description: Obtain a list of entry identifiers and associated names
  name: Kyoto Encyclopedia of Genes and Genomes (KEGG) list API
  slug: kegg-list-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KEGG REST conv API
  slug: open-kegg-conv-api
- collection_type: open
  name: KEGG REST conv ddi API
  slug: open-kegg-ddi-api
- collection_type: open
  name: KEGG REST conv find API
  slug: open-kegg-find-api
- collection_type: open
  name: KEGG REST conv get API
  slug: open-kegg-get-api
- collection_type: open
  name: KEGG REST conv info API
  slug: open-kegg-info-api
- collection_type: open
  name: KEGG REST conv link API
  slug: open-kegg-link-api
- collection_type: open
  name: KEGG REST conv list API
  slug: open-kegg-list-api
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
random_paper: 15
rate_limits:
- limit_count: 1
  name: Kegg Rest Api
  slug: kegg-rest-api
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.7
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
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
