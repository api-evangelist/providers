---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
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
  description: Chembl Activities Resource
  name: ChEMBL Activities API
  slug: chembl-activities-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Chembl Assays Resource
  name: ChEMBL Assays API
  slug: chembl-assays-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Drug Resource
  name: ChEMBL Drugs API
  slug: chembl-drugs-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: EFO Resource
  name: ChEMBL EFO disease terms API
  slug: chembl-efo-disease-terms-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: HPO Resource
  name: ChEMBL HPO API
  slug: chembl-hpo-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Intact Resource
  name: ChEMBL Intact API
  slug: chembl-intact-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Chembl Molecules Resource
  name: ChEMBL Molecules API
  slug: chembl-molecules-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Protein Resource
  name: ChEMBL Proteins API
  slug: chembl-proteins-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Pubchem Bioassay Sids Resource
  name: ChEMBL PubChem Bioassay Sids API
  slug: chembl-pubchem-bioassay-sids-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Pubchem Bioassay Resource
  name: ChEMBL PubChem Biossays API
  slug: chembl-pubchem-biossays-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Pubchem Compound Resource
  name: ChEMBL PubChem Compounds API
  slug: chembl-pubchem-compounds-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Pubchem Substance Resource
  name: ChEMBL PubChem Substances API
  slug: chembl-pubchem-substances-api
- baseURL: https://www.ebi.ac.uk/chembl/api/data/
  baseurl_source: declared
  description: Chembl Targets Resource
  name: ChEMBL Targets API
  slug: chembl-targets-api
artifact_total: 41
collections:
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
- group: commercial
  href: https://artifacts.apis.io/chembl/plans/plans.yml
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  href: https://artifacts.apis.io/chembl/rate-limits/rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chembl/finops/finops.yml
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: other
  href: https://artifacts.apis.io/chembl/capabilities/chembl-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/chembl-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/chembl/agentic-access/chembl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chembl-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/chembl/security/chembl-domain-security.yml
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
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
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
overview: 'ChEMBL publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Assays API, Drugs API, and 10 more. Tagged areas include Drug Discovery, Bioactivity, Molecules, Cheminformatics, and Life Sciences.


  The ChEMBL catalog on APIs.io includes 1 Spectral governance ruleset.


  ChEMBL''s developer surface includes authentication, status page, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 19
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: ChEMBL — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: chembl-jsonschema-spectral-rules
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.3
    catalog_earned_first_party: 0.0
    catalog_gap: 72.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 42.9
    developer_ergonomics: 21.4
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 26.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 43.3
      total: 30
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/chembl/chembl-2026-06-20T174255.png
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
