---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: United States National Library Of Medicine Agentic Access
  operation_count: 17
  slug: united-states-national-library-of-medicine-agentic-access
  summary_line: 17 operations · 1 acting
api_count: 10
apis:
- description: BLAST sequence search submission and retrieval
  name: United States National Library of Medicine BLAST API
  slug: united-states-national-library-of-medicine-blast-api
- description: Retrieve records from Entrez databases
  name: United States National Library of Medicine Fetch API
  slug: united-states-national-library-of-medicine-fetch-api
- description: Gene records and sequence data
  name: United States National Library of Medicine Gene API
  slug: united-states-national-library-of-medicine-gene-api
- description: Genome assembly data and metadata
  name: United States National Library of Medicine Genome API
  slug: united-states-national-library-of-medicine-genome-api
- description: Database information and statistics
  name: United States National Library of Medicine Info API
  slug: united-states-national-library-of-medicine-info-api
- description: Find linked records across databases
  name: United States National Library of Medicine Link API
  slug: united-states-national-library-of-medicine-link-api
- description: API metadata and field definitions
  name: United States National Library of Medicine Metadata API
  slug: united-states-national-library-of-medicine-metadata-api
- description: Search Entrez databases
  name: United States National Library of Medicine Search API
  slug: united-states-national-library-of-medicine-search-api
- description: Clinical trial study search and retrieval
  name: United States National Library of Medicine Studies API
  slug: united-states-national-library-of-medicine-studies-api
- description: NCBI taxonomy information
  name: United States National Library of Medicine Taxonomy API
  slug: united-states-national-library-of-medicine-taxonomy-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NCBI BLAST URL API
  slug: open-ncbi-blast
- collection_type: open
  name: NCBI Datasets REST API
  slug: open-ncbi-datasets
- collection_type: open
  name: NCBI E-Utilities API
  slug: open-ncbi-e-utilities
- collection_type: open
  name: ClinicalTrials.gov API
  slug: open-nlm-clinicaltrials
- collection_type: open
  name: NCBI URL BLAST API
  slug: open-united-states-national-library-of-medicine-blast-api
- collection_type: open
  name: NCBI URL BLAST Fetch API
  slug: open-united-states-national-library-of-medicine-fetch-api
- collection_type: open
  name: NCBI URL BLAST Gene API
  slug: open-united-states-national-library-of-medicine-gene-api
- collection_type: open
  name: NCBI URL BLAST Genome API
  slug: open-united-states-national-library-of-medicine-genome-api
- collection_type: open
  name: NCBI URL BLAST Info API
  slug: open-united-states-national-library-of-medicine-info-api
- collection_type: open
  name: NCBI URL BLAST Link API
  slug: open-united-states-national-library-of-medicine-link-api
- collection_type: open
  name: NCBI URL BLAST Metadata API
  slug: open-united-states-national-library-of-medicine-metadata-api
- collection_type: open
  name: NCBI URL BLAST Search API
  slug: open-united-states-national-library-of-medicine-search-api
- collection_type: open
  name: NCBI URL BLAST Studies API
  slug: open-united-states-national-library-of-medicine-studies-api
- collection_type: open
  name: NCBI URL BLAST Taxonomy API
  slug: open-united-states-national-library-of-medicine-taxonomy-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/united-states-national-library-of-medicine-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-states-national-library-of-medicine-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/united-states-national-library-of-medicine-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-library-of-medicine-nlm
- group: start
  title: ''
  type: Portal
  url: https://www.ncbi.nlm.nih.gov/home/develop/api/
created: 2024/01/01
description: The United States National Library of Medicine (NLM) is the world's largest biomedical library. It serves as a vital resource for researchers, healthcare professionals, and the general public by providing access to a vast collection of biomedical literature and resources. The NLM offers a wide range of services and resources including online databases, digital archives, and research tools that support medical research, education, and patient care. Key APIs include the NCBI E-Utilities (PubMed, Entrez), NCBI Datasets (genomes, genes), BLAST sequence alignment, and the ClinicalTrials.gov API.
examples:
- key_count: 3
  name: Ncbi Datasets Get Genome Example
  slug: ncbi-datasets-get-genome-example
- key_count: 3
  name: Ncbi Esearch Pubmed Example
  slug: ncbi-esearch-pubmed-example
- key_count: 3
  name: Nlm Clinicaltrials Search Example
  slug: nlm-clinicaltrials-search-example
finops:
- name: United States National Library Of Medicine Finops
  service_category: API
  slug: united-states-national-library-of-medicine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-states-national-library-of-medicine.png
json_schemas:
- name: NCBI PubMed Article
  property_count: 12
  slug: ncbi-pubmed-article
- name: ClinicalTrials.gov Study
  property_count: 17
  slug: nlm-clinical-trial
json_structures:
- name: Ncbi Pubmed Article Structure
  property_count: 0
  slug: ncbi-pubmed-article-structure
jsonld:
- class_count: 4
  name: United States National Library Of Medicine Context
  property_count: 19
  slug: united-states-national-library-of-medicine-context
layout: provider
modified: '2026-05-19'
name: United States National Library of Medicine
nav: Providers
network: true
overview: 'United States National Library of Medicine publishes 10 APIs on the [APIs.io](https://apis.io/) network, including BLAST API, Fetch API, Gene API, and 7 more. Tagged areas include Federal Government, Biomedical Research, Healthcare, Genomics, and Literature.


  The United States National Library of Medicine catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  United States National Library of Medicine''s developer surface includes authentication, developer portal, and 3 more developer resources.'
plans:
- name: United States National Library Of Medicine Plans Pricing
  plan_count: 3
  slug: united-states-national-library-of-medicine-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: United States National Library Of Medicine Rate Limits
  slug: united-states-national-library-of-medicine-rate-limits
rules:
- effective_rule_count: 7
  extends: []
  name: United States National Library of Medicine API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: ncbi-e-utilities-rules
- effective_rule_count: 5
  extends: []
  name: United States National Library of Medicine API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: united-states-national-library-of-medicine-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.4
  delta: 2.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 30.3
    contract_quality: 58.0
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 30.3
    operational_transparency: 7.9
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/united-states-national-library-of-medicine/refs/heads/main/screenshots/united-states-national-library-of-medicine-2026-06-20T200054.png
security:
- kind: authentication
  name: United States National Library Of Medicine Authentication
  slug: united-states-national-library-of-medicine-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: United States National Library Of Medicine Domain Security
  slug: united-states-national-library-of-medicine-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: united-states-national-library-of-medicine
tags:
- Federal Government
- Biomedical Research
- Healthcare
- Genomics
- Literature
website: https://www.ncbi.nlm.nih.gov/home/develop/api/
---
