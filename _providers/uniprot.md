---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
api_count: 7
apis:
- description: Search and retrieve protein entries from UniProtKB, which integrates Swiss-Prot (manually reviewed) and TrEMBL (computationally annotated) databases. Supports full-text and field-specific queries, ret
  name: UniProtKB REST API
  slug: uniprotkb-rest-api
- description: UniRef (UniProt Reference Clusters) groups similar sequences to reduce redundancy. UniRef100 combines identical sequences; UniRef90 clusters sequences sharing 90% identity; UniRef50 clusters at 50%. T
  name: UniRef REST API
  slug: uniref-rest-api
- description: 'UniParc (UniProt Archive) is a comprehensive non-redundant database of publicly available protein sequences. Each unique sequence appears once with a stable UniParc identifier and cross-references to '
  name: UniParc REST API
  slug: uniparc-rest-api
- description: Provides access to UniProt proteomes — the complete or near-complete sets of proteins from fully sequenced organisms. Supports retrieval of reference proteomes and gene-centric proteome data. Useful f
  name: Proteomes REST API
  slug: proteomes-rest-api
- description: 'Maps identifiers between UniProt accessions and over 150 external database identifiers (e.g., RefSeq, Ensembl, PDB, ChEMBL, KEGG, OMIM). Asynchronous job-based service: submit a mapping job, poll for '
  name: ID Mapping REST API
  slug: id-mapping-rest-api
- description: A standards-compliant SPARQL 1.1 endpoint exposing the full UniProt knowledge graph as RDF. The current release contains approximately 232 billion triples across 21 named graphs. Supports complex biol
  name: UniProt SPARQL Endpoint
  slug: uniprot-sparql-endpoint
- description: The EMBL-EBI Proteins API provides integrated access to UniProt protein annotations alongside large-scale study data including variation data from 1000 Genomes, ClinVar, ExAC, COSMIC, gnomAD, and TCGA
  name: EBI Proteins REST API
  slug: ebi-proteins-rest-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uniprot-domain-security.yml
created: '2002-01-01'
description: UniProt is the world's leading high-quality, comprehensive, and freely accessible resource for protein sequence and functional annotation data. Maintained by the UniProt Consortium (EMBL-EBI, SIB, and PIR), it integrates information from experimental literature and computational analysis to provide a single authoritative source on protein function, taxonomy, sequences, cross-references, and disease associations. UniProt exposes a REST API at rest.uniprot.org for searching and retrieving entries from UniProtKB, UniRef, UniParc, Proteomes, and supporting services such as ID mapping. All data is freely available under Creative Commons Attribution 4.0.
finops:
- name: Overview
  service_category: ''
  slug: overview
image: https://www.uniprot.org/images/logos/uniprot.svg
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: UniProt
nav: Providers
network: true
overview: 'UniProt publishes 1 API on the [APIs.io](https://apis.io/) network: UniProtKB REST API. Tagged areas include Proteins, Bioinformatics, Genomics, Life Sciences, and Open Data.


  The UniProt catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Free
  plan_count: 0
  slug: free
random_paper: 8
rate_limits:
- limit_count: 3
  name: Default
  slug: default
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 33.3
    developer_ergonomics: 9.5
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 26.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uniprot/refs/heads/main/screenshots/uniprot-2026-06-20T200029.png
security:
- kind: domain-security
  name: Uniprot Domain Security
  slug: uniprot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uniprot
tags:
- Proteins
- Bioinformatics
- Genomics
- Life Sciences
- Open Data
website: https://www.uniprot.org/
---
