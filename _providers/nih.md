---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 41
  human_in_the_loop: 0
  name: Nih Agentic Access
  operation_count: 116
  slug: nih-agentic-access
  summary_line: 116 operations · 41 acting
api_count: 2
apis:
- description: The public API to the NCBI Entrez system providing programmatic access to all Entrez databases including PubMed, PMC, Gene, Nuccore, and Protein. Supports searching, fetching, linking, and summarizing
  name: NCBI E-utilities (Entrez Programming Utilities)
  slug: ncbi-e-utilities-entrez-programming-utilities
- description: 'Suite of REST APIs providing programmatic access to PubChem chemical compound data, including chemical structure searches, compound properties, biological assay data, and chemical standardization for '
  name: PubChem Power User Gateway (PUG REST)
  slug: pubchem-power-user-gateway-pug-rest
- description: REST API providing programmatic access to NIH-funded research project data including grants, contracts, publications, and patents. Enables search and retrieval of funding records with extensive filter
  name: NIH RePORTER API
  slug: nih-reporter-api
- description: API enabling developers to submit BLAST (Basic Local Alignment Search Tool) sequence searches via HTTPS for processing at NCBI or cloud service providers, check job status, and retrieve results in mul
  name: NCBI BLAST URL API
  slug: ncbi-blast-url-api
- description: APIs for programmatic access to PubMed Central's Open Access content, including file validation, Open Access service, and an ID converter for translating between PMCID, PMID, Manuscript ID, and DOI id
  name: PubMed Central (PMC) OA API
  slug: pubmed-central-pmc-oa-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  baseurl_source: declared
  description: '#### Options to download BioSample data. This BioSample service allows you to get BioSample data as a data report.'
  name: National Institutes of Health (NIH) BioSample API
  slug: nih-biosample-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  baseurl_source: declared
  description: '#### Options to download gene data, including the associated sequence and metadata. These gene services allow you to get gene metadata as a data report or download gene, transcript and protein sequenc'
  name: National Institutes of Health (NIH) Gene API
  slug: nih-gene-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  baseurl_source: declared
  description: '#### Options to download assembled genome data, including the associated sequence, annotation and metadata. These genome services allow you to get genome metadata as a data report or download genome, '
  name: National Institutes of Health (NIH) Genome API
  slug: nih-genome-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  baseurl_source: declared
  description: '#### Options to download RefSeq organelle genome data, including the associated sequence and metadata. These organelle services allow you to get RefSeq organelle genome metadata as a data report or do'
  name: National Institutes of Health (NIH) Organelle API
  slug: nih-organelle-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  baseurl_source: declared
  description: '#### Options to download prokaryote gene data, including the associated sequence and metadata. These gene services allow you to download gene and protein sequence, and metadata as a prokaryote gene da'
  name: National Institutes of Health (NIH) Prokaryote API
  slug: nih-prokaryote-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  baseurl_source: declared
  description: Data statistics
  name: National Institutes of Health (NIH) Stats API
  slug: nih-stats-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  baseurl_source: declared
  description: Related to clinical trial studies
  name: National Institutes of Health (NIH) Studies API
  slug: nih-studies-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  baseurl_source: declared
  description: '#### Options to download taxonomy data. These taxonomy services allow you to get taxonomy data as a data report or download taxonomy data as a taxonomy data package, for taxonomic nodes in NCBI Taxono'
  name: National Institutes of Health (NIH) Taxonomy API
  slug: nih-taxonomy-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  baseurl_source: declared
  description: Version info
  name: National Institutes of Health (NIH) Version API
  slug: nih-version-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
  baseurl_source: declared
  description: '#### Options to download virus genome data, including the associated sequence and metadata. These virus services allow you to get virus genome metadata as a data report or download genome and protein '
  name: National Institutes of Health (NIH) Virus API
  slug: nih-virus-api
artifact_total: 55
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ClinicalTrials.gov REST BioSample API
  slug: open-nih-biosample-api
- collection_type: open
  name: ClinicalTrials.gov REST BioSample Gene API
  slug: open-nih-gene-api
- collection_type: open
  name: ClinicalTrials.gov REST BioSample Genome API
  slug: open-nih-genome-api
- collection_type: open
  name: ClinicalTrials.gov REST BioSample Organelle API
  slug: open-nih-organelle-api
- collection_type: open
  name: ClinicalTrials.gov REST BioSample Prokaryote API
  slug: open-nih-prokaryote-api
- collection_type: open
  name: ClinicalTrials.gov REST BioSample Stats API
  slug: open-nih-stats-api
- collection_type: open
  name: ClinicalTrials.gov REST BioSample Studies API
  slug: open-nih-studies-api
- collection_type: open
  name: ClinicalTrials.gov REST BioSample Taxonomy API
  slug: open-nih-taxonomy-api
- collection_type: open
  name: ClinicalTrials.gov REST BioSample Version API
  slug: open-nih-version-api
- collection_type: open
  name: ClinicalTrials.gov REST BioSample Virus API
  slug: open-nih-virus-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nih-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nih-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nih-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nih-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.nih.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ncbi.nlm.nih.gov/home/develop/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ncbi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-institutes-of-health
- group: company
  title: ''
  type: Blog
  url: https://ncbiinsights.ncbi.nlm.nih.gov/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ncbi.nlm.nih.gov/home/develop/api/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.ncbi.nlm.nih.gov/home/develop/api/
- group: other
  title: ''
  type: X
  url: https://x.com/NIH
- group: commercial
  title: ''
  type: Plans
  url: plans/nih-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nih-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nih-finops.yml
created: '2026-06-13'
description: The US National Institutes of Health (NIH) provides a suite of public REST APIs for biomedical research, including PubMed literature search via E-utilities, ClinicalTrials.gov clinical trial data, chemical compound data through PubChem, gene and genome databases via NCBI Datasets, BLAST sequence alignment, and NIH research funding data through RePORTER.
examples:
- key_count: 4
  name: Clinicaltrials Liststudies 200
  slug: clinicaltrials-listStudies-200
- key_count: 5
  name: Clinicaltrials Study Search Request
  slug: clinicaltrials-study-search-request
- key_count: 5
  name: Ncbi Datasets Assembly Request
  slug: ncbi-datasets-assembly-request
- key_count: 5
  name: Ncbi Datasets Gene Search Request
  slug: ncbi-datasets-gene-search-request
- key_count: 5
  name: Nih Reporter Project Search Request
  slug: nih-reporter-project-search-request
- key_count: 5
  name: Pubchem Compound Request
  slug: pubchem-compound-request
finops:
- name: Nih Finops
  service_category: ''
  slug: nih-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nih.png
json_schemas:
- name: EnumInfo
  property_count: 3
  slug: clinicaltrials-enuminfo
- name: EnumStats
  property_count: 6
  slug: clinicaltrials-enumstats
- name: FieldNode
  property_count: 16
  slug: clinicaltrials-fieldnode
- name: SearchArea
  property_count: 4
  slug: clinicaltrials-searcharea
- name: SearchDocument
  property_count: 2
  slug: clinicaltrials-searchdocument
- name: StringStats
  property_count: 7
  slug: clinicaltrials-stringstats
- name: Study
  property_count: 6
  slug: clinicaltrials-study
- name: StudySize
  property_count: 2
  slug: clinicaltrials-studysize
- name: v2AssemblyDatasetAvailability
  property_count: 3
  slug: ncbi-datasets-assemblydatasetavailability
- name: v2AssemblyDatasetRequest
  property_count: 5
  slug: ncbi-datasets-assemblydatasetrequest
- name: v2DownloadSummary
  property_count: 8
  slug: ncbi-datasets-downloadsummary
- name: v2GeneDatasetReportsRequest
  property_count: 16
  slug: ncbi-datasets-genedatasetreportsrequest
- name: v2TaxonomyNode
  property_count: 17
  slug: ncbi-datasets-taxonomynode
- name: v2VirusDatasetRequest
  property_count: 17
  slug: ncbi-datasets-virusdatasetrequest
jsonld:
- class_count: 0
  name: Nih Apis Context
  property_count: 0
  slug: nih-apis
- class_count: 8
  name: Nih Context
  property_count: 10
  slug: nih-context
layout: provider
modified: '2026-06-13'
name: National Institutes of Health (NIH)
nav: Providers
network: true
overview: 'National Institutes of Health (NIH) publishes 10 APIs on the [APIs.io](https://apis.io/) network, including BioSample API, Gene API, Genome API, and 7 more. Tagged areas include Biomedical, Research, PubMed, Clinical Trials, and PubChem.


  The National Institutes of Health (NIH) catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  National Institutes of Health (NIH)''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Nih Plans Pricing
  plan_count: 5
  slug: nih-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Nih Rate Limits
  slug: nih-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: National Institutes of Health (NIH) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nih-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 59.9
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 40.9
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nih/refs/heads/main/screenshots/nih-2026-06-20T190323.png
security:
- kind: authentication
  name: Nih Authentication
  slug: nih-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Nih Domain Security
  slug: nih-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nih
tags:
- Biomedical
- Research
- PubMed
- Clinical Trials
- PubChem
- Genomics
- Health
- Science
- Government
website: https://www.nih.gov/
---
