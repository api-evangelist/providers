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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Life Sciences Agentic Access
  operation_count: 5
  slug: life-sciences-agentic-access
  summary_line: 5 operations
api_count: 22
apis:
- description: The European Medicines Agency's Clinical Trials Information System (CTIS) and the legacy EU Clinical Trials Register. CTIS is the single entry point for sponsors and regulators across the EU/EEA to su
  name: EU Clinical Trials Register / CTIS
  slug: eu-clinical-trials-register-ctis
- description: A U.S. Food and Drug Administration project that exposes public FDA data via a single Elasticsearch-backed REST/JSON API. Covers adverse-event reports, drug labels, recalls, NDC directory, device 510(
  name: openFDA
  slug: openfda
- description: The National Library of Medicine's authoritative source of FDA-approved Structured Product Labeling (SPL) for prescription and over-the-counter medications marketed in the United States. Exposes a RES
  name: DailyMed
  slug: dailymed
- description: The National Library of Medicine's web service for accessing RxNorm, the standardized nomenclature for clinical drugs that links names of drugs across the major U.S. drug vocabularies. Supports name-t
  name: RxNorm API
  slug: rxnorm-api
- description: A commercial drug knowledge API providing curated pharmacology, pharmacokinetics, drug-drug interaction, indication, and identifier cross-walk data covering small molecules and biologics. Used by clin
  name: DrugBank API
  slug: drugbank-api
- description: The set of nine programmatic interfaces (ESearch, EPost, ESummary, EFetch, ELink, EInfo, EGQuery, ESpell, ECitMatch) that provide unified access to all NCBI databases including PubMed, Gene, Genome, N
  name: NCBI Entrez E-utilities
  slug: ncbi-entrez-e-utilities
- description: The European Bioinformatics Institute's REST/JSON interface to the Ensembl genome browser. Provides programmatic access to genomic annotation, variation, comparative genomics, regulatory data, the Var
  name: Ensembl REST API
  slug: ensembl-rest-api
- description: 'The University of California Santa Cruz Genome Browser''s REST API for programmatic retrieval of assemblies, tracks, sequences, and annotations across the genomes hosted in the UCSC Browser, including '
  name: UCSC Genome Browser REST API
  slug: ucsc-genome-browser-rest-api
- description: The NIH/NLM database of relationships among human genomic variation and phenotype, with supporting evidence. Accessible programmatically via Entrez E-utilities and via a structured FTP feed of XML/JSO
  name: ClinVar (via E-utilities)
  slug: clinvar-via-e-utilities
- description: The NCBI Short Genetic Variations database, the canonical reference for single nucleotide polymorphisms (SNPs) and small insertions/deletions in humans and other organisms. Accessed via Entrez E-utili
  name: dbSNP (via E-utilities)
  slug: dbsnp-via-e-utilities
- description: Fast Healthcare Interoperability Resources (FHIR) is HL7's standard for health care data exchange. The current normative version is R5, released March 2023. Defines roughly 150 resource types covering
  name: HL7 FHIR
  slug: hl7-fhir
- description: An open-spec authorization profile layered on top of FHIR that enables third-party clinical applications to launch within an EHR session with OAuth 2.0 / OpenID Connect scopes scoped to FHIR resources
  name: SMART on FHIR
  slug: smart-on-fhir
- description: Benchling's REST API and webhook platform for its R&D cloud, exposing programmatic access to the Notebook (entries), Registry (registered entities, sequences, plasmids), Inventory (boxes, plates, loca
  name: Benchling Developer Platform
  slug: benchling-developer-platform
- description: A cloud-native scientific data platform that harmonizes instrument and informatics data across pharma R&D. Exposes REST APIs and SDKs for ingesting, querying, and integrating laboratory and computatio
  name: TetraScience Data Platform
  slug: tetrascience-data-platform
- description: Sapio Sciences' platform API providing programmatic access to its Electronic Laboratory Notebook, Laboratory Information Management System, and Scientific Data Cloud, covering samples, experiments, as
  name: Sapio Sciences ELN/LIMS API
  slug: sapio-sciences-elnlims-api
- description: DNAnexus is a cloud bioinformatics platform used by pharma, biotech, and research institutions to run genomic and biomedical compute workflows. Its platform API provides programmatic access to project
  name: DNAnexus Platform API
  slug: dnanexus-platform-api
- description: A multi-cloud bioinformatics platform (now part of Velsera) offering hosted instances of the NCI Cancer Genomics Cloud and other cohort analysis environments. Provides REST APIs for projects, files, t
  name: Seven Bridges (Velsera) Platform API
  slug: seven-bridges-velsera-platform-api
- description: The open-source Galaxy bioinformatics workbench exposes a REST API for managing histories, datasets, workflows, tools, jobs, and users across community Galaxy servers and self-hosted installations.
  name: Galaxy Project API
  slug: galaxy-project-api
- description: The Global Alliance for Genomics and Health publishes a suite of open REST specifications enabling federated access to genomic data and compute. Includes htsget (sequencing reads), DRS (Data Repositor
  name: GA4GH APIs (htsget, DRS, WES, TES, Beacon)
  slug: ga4gh-apis-htsget-drs-wes-tes-beacon
- description: The Stats API from Life Sciences — 1 operation(s) for stats.
  name: Life Sciences Stats API
  slug: life-sciences-stats-api
- description: The Studies API from Life Sciences — 3 operation(s) for studies.
  name: Life Sciences Studies API
  slug: life-sciences-studies-api
- description: The Version API from Life Sciences — 1 operation(s) for version.
  name: Life Sciences Version API
  slug: life-sciences-version-api
artifact_total: 33
collections:
- collection_type: open
  name: ClinicalTrials.gov API v2
  slug: open-life-sciences
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/life-sciences-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/life-sciences-domain-security.yml
created: '2025-01-01'
description: 'Industry-vertical index for the life sciences, biotechnology, and pharmaceutical landscape. Catalogs the major public and commercial APIs spanning clinical trial registries, drug and regulatory data, genomic reference data, electronic health record exchange, laboratory informatics systems, and bioinformatics pipeline platforms. The catalog is anchored by shared schemas for the three core records that recur across this domain: the clinical trial, the drug, and the gene.'
examples:
- key_count: 16
  name: Clinical Trial Example
  slug: clinical-trial-example
- key_count: 17
  name: Drug Example
  slug: drug-example
- key_count: 14
  name: Gene Example
  slug: gene-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/life-sciences.png
json_schemas:
- name: ClinicalTrial
  property_count: 17
  slug: clinical-trial
- name: Drug
  property_count: 17
  slug: drug
- name: Gene
  property_count: 14
  slug: gene
jsonld:
- class_count: 16
  name: Life Sciences Context
  property_count: 50
  slug: life-sciences-context
layout: provider
modified: '2026-05-23'
name: Life Sciences
nav: Providers
network: true
overview: 'Life Sciences publishes 3 APIs on the [APIs.io](https://apis.io/) network: Stats API, Studies API, and Version API. Tagged areas include Life Sciences, Biotech, Pharma, Healthcare, and Clinical Trials.


  The Life Sciences catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 63
rules:
- name: Life Sciences API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: life-sciences-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 69.8
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/life-sciences/refs/heads/main/screenshots/life-sciences-2026-06-20T184511.png
security:
- kind: domain-security
  name: Life Sciences Domain Security
  slug: life-sciences-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: life-sciences
tags:
- Life Sciences
- Biotech
- Pharma
- Healthcare
- Clinical Trials
- Drug Information
- Genomics
- Bioinformatics
- EHR
- FHIR
- Lab Informatics
---
