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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chembl Agentic Access
  operation_count: 30
  slug: chembl-agentic-access
  summary_line: 30 operations
api_count: 1
apis:
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Activity values recorded in assays, linking molecules to targets with quantitative bioactivity measurements.
  name: ChEMBL Activity API
  slug: chembl-activity-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Experimental protocols and result details from source documents and datasets.
  name: ChEMBL Assay API
  slug: chembl-assay-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: WHO Anatomical Therapeutic Chemical classification for drugs.
  name: ChEMBL ATC Classification API
  slug: chembl-atc-classification-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Target binding site definitions used in assays.
  name: ChEMBL Binding Site API
  slug: chembl-binding-site-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Cell line information used in assays.
  name: ChEMBL Cell Line API
  slug: chembl-cell-line-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Occurrence of a compound in a specific source document.
  name: ChEMBL Compound Record API
  slug: chembl-compound-record-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Source documents and datasets from which assay data is derived.
  name: ChEMBL Document API
  slug: chembl-document-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Approved drug information including applicants, patent numbers, and research codes.
  name: ChEMBL Drug API
  slug: chembl-drug-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Drug-disease associations with clinical trial and regulatory references.
  name: ChEMBL Drug Indication API
  slug: chembl-drug-indication-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Safety information for withdrawn or black-box warned drugs.
  name: ChEMBL Drug Warning API
  slug: chembl-drug-warning-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Mechanism of action information for approved drugs.
  name: ChEMBL Mechanism API
  slug: chembl-mechanism-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Chemical molecules including properties, structural representations, synonyms, and drug-like properties.
  name: ChEMBL Molecule API
  slug: chembl-molecule-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Molecule similarity searching using Tanimoto coefficient.
  name: ChEMBL Similarity API
  slug: chembl-similarity-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: API operational status and ChEMBL database version information.
  name: ChEMBL Status API
  slug: chembl-status-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Molecular substructure searching.
  name: ChEMBL Substructure API
  slug: chembl-substructure-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Protein and non-protein targets defined in assays.
  name: ChEMBL Target API
  slug: chembl-target-api
artifact_total: 45
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ChEMBL Data REST Activity API
  slug: open-chembl-activity-api
- collection_type: open
  name: ChEMBL Data REST Activity Assay API
  slug: open-chembl-assay-api
- collection_type: open
  name: ChEMBL Data REST Activity ATC Classification API
  slug: open-chembl-atc-classification-api
- collection_type: open
  name: ChEMBL Data REST Activity Binding Site API
  slug: open-chembl-binding-site-api
- collection_type: open
  name: ChEMBL Data REST Activity Cell Line API
  slug: open-chembl-cell-line-api
- collection_type: open
  name: ChEMBL Data REST Activity Compound Record API
  slug: open-chembl-compound-record-api
- collection_type: open
  name: ChEMBL Data REST Activity Document API
  slug: open-chembl-document-api
- collection_type: open
  name: ChEMBL Data REST Activity Drug API
  slug: open-chembl-drug-api
- collection_type: open
  name: ChEMBL Data REST Activity Drug Indication API
  slug: open-chembl-drug-indication-api
- collection_type: open
  name: ChEMBL Data REST Activity Drug Warning API
  slug: open-chembl-drug-warning-api
- collection_type: open
  name: ChEMBL Data REST Activity Mechanism API
  slug: open-chembl-mechanism-api
- collection_type: open
  name: ChEMBL Data REST Activity Molecule API
  slug: open-chembl-molecule-api
- collection_type: open
  name: ChEMBL Data REST Activity Similarity API
  slug: open-chembl-similarity-api
- collection_type: open
  name: ChEMBL Data REST Activity Status API
  slug: open-chembl-status-api
- collection_type: open
  name: ChEMBL Data REST Activity Substructure API
  slug: open-chembl-substructure-api
- collection_type: open
  name: ChEMBL Data REST Activity Target API
  slug: open-chembl-target-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/chembl-capability-edges.yml
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


  ChEMBL''s developer surface includes authentication, status page, and 5 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 10
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ChEMBL API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: chembl-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 13
    catalog_gap: 63.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 49.4
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 0.0
  previous_composite: 33.5
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
