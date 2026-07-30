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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chembl Agentic Access
  operation_count: 30
  slug: chembl-agentic-access
  summary_line: 30 operations
api_count: 16
apis:
- description: Activity values recorded in assays, linking molecules to targets with quantitative bioactivity measurements.
  name: ChEMBL Activity API
  slug: chembl-activity-api
- description: Experimental protocols and result details from source documents and datasets.
  name: ChEMBL Assay API
  slug: chembl-assay-api
- description: WHO Anatomical Therapeutic Chemical classification for drugs.
  name: ChEMBL ATC Classification API
  slug: chembl-atc-classification-api
- description: Target binding site definitions used in assays.
  name: ChEMBL Binding Site API
  slug: chembl-binding-site-api
- description: Cell line information used in assays.
  name: ChEMBL Cell Line API
  slug: chembl-cell-line-api
- description: Occurrence of a compound in a specific source document.
  name: ChEMBL Compound Record API
  slug: chembl-compound-record-api
- description: Source documents and datasets from which assay data is derived.
  name: ChEMBL Document API
  slug: chembl-document-api
- description: Approved drug information including applicants, patent numbers, and research codes.
  name: ChEMBL Drug API
  slug: chembl-drug-api
- description: Drug-disease associations with clinical trial and regulatory references.
  name: ChEMBL Drug Indication API
  slug: chembl-drug-indication-api
- description: Safety information for withdrawn or black-box warned drugs.
  name: ChEMBL Drug Warning API
  slug: chembl-drug-warning-api
- description: Mechanism of action information for approved drugs.
  name: ChEMBL Mechanism API
  slug: chembl-mechanism-api
- description: Chemical molecules including properties, structural representations, synonyms, and drug-like properties.
  name: ChEMBL Molecule API
  slug: chembl-molecule-api
- description: Molecule similarity searching using Tanimoto coefficient.
  name: ChEMBL Similarity API
  slug: chembl-similarity-api
- description: API operational status and ChEMBL database version information.
  name: ChEMBL Status API
  slug: chembl-status-api
- description: Molecular substructure searching.
  name: ChEMBL Substructure API
  slug: chembl-substructure-api
- description: Protein and non-protein targets defined in assays.
  name: ChEMBL Target API
  slug: chembl-target-api
artifact_total: 28
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chembl-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chembl-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: other
  title: ''
  type: Formats
  url: ''
- group: design
  title: ''
  type: Pagination
  url: ''
- group: other
  title: ''
  type: Filtering
  url: ''
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/licenses/by-sa/3.0/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ebi.ac.uk/about/terms-of-use/
- group: build
  title: ''
  type: PythonClient
  url: https://github.com/chembl/chembl_webresource_client
- group: operate
  title: ''
  type: Status
  url: https://www.ebi.ac.uk/chembl/api/data/status/
created: '2026-06-13'
description: ChEMBL is a manually curated database of bioactive molecules with drug-like properties, maintained by the EMBL-EBI. It provides a REST API for accessing bioactive molecules, drug targets, bioactivity data, approved drugs, clinical trial compounds, and cheminformatics utilities to support drug discovery research.
examples:
- key_count: 2
  name: Activity Example
  slug: activity-example
- key_count: 2
  name: Molecule Example
  slug: molecule-example
- key_count: 4
  name: Similarity Search Example
  slug: similarity-search-example
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.ebi.ac.uk/chembl/static/chembl/img/chembl_logo.png
json_schemas:
- name: ChEMBL Activity
  property_count: 28
  slug: activity
- name: ChEMBL Molecule
  property_count: 20
  slug: molecule
- name: ChEMBL Target
  property_count: 8
  slug: target
layout: provider
modified: '2026-06-13'
name: ChEMBL
nav: Providers
network: true
overview: 'ChEMBL publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Assay API, ATC Classification API, and 13 more. Tagged areas include Drug Discovery, Bioactivity, Molecules, Cheminformatics, and Life Sciences.


  The ChEMBL catalog on APIs.io includes 1 Spectral governance ruleset.


  ChEMBL''s developer surface includes authentication, status page, and 4 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 45
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: ChEMBL API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: chembl-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.4
  delta: -5.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.7
    developer_ergonomics: 10.9
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/chembl/refs/heads/main/screenshots/chembl-2026-06-20T174255.png
security:
- kind: domain-security
  name: Chembl Domain Security
  slug: chembl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chembl
tags:
- Drug Discovery
- Bioactivity
- Molecules
- Cheminformatics
- Life Sciences
- Bioinformatics
- Pharmacology
- EMBL-EBI
website: https://www.ebi.ac.uk/chembl/
---
