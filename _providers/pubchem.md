---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pubchem Agentic Access
  operation_count: 12
  slug: pubchem-agentic-access
  summary_line: 12 operations
api_count: 7
apis:
- description: The PUG View API provides access to the full structured compound and substance pages as seen on the PubChem website, organized as hierarchical sections covering names, structures, physical and chemica
  name: PubChem PUG View API
  slug: pubchem-pug-view-api
- description: Legacy SOAP/XML web service interface for PubChem providing structure search, identity search, and chemical standardization capabilities. Supports submitting queries and retrieving results in ASN.1, X
  name: PubChem PUG SOAP API
  slug: pubchem-pug-soap-api
- description: Generates 2D and 3D structure images for chemical compounds by CID, SID, SMILES, or InChI. Returns PNG images at configurable sizes, suitable for embedding in applications and documents.
  name: PubChem Structure Image Service
  slug: pubchem-structure-image-service
- description: Bulk identifier conversion service for translating between PubChem CIDs, SIDs, and external identifiers such as CAS Registry Numbers, ChEMBL IDs, ChEBI IDs, and other registry identifiers at scale.
  name: PubChem Identifier Exchange Service
  slug: pubchem-identifier-exchange-service
- description: Operations on compound records
  name: PubChem Compounds API
  slug: pubchem-compounds-api
- description: Chemical structure search operations
  name: PubChem Structure Search API
  slug: pubchem-structure-search-api
- description: Utility operations
  name: PubChem Utilities API
  slug: pubchem-utilities-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pubchem-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pubchem-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nlm.nih.gov/web_policies.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nlm.nih.gov/privacy.html
- group: operate
  title: ''
  type: Status
  url: https://pubchem.ncbi.nlm.nih.gov/
- group: operate
  title: ''
  type: Support
  url: https://support.nlm.nih.gov/
- group: start
  title: ''
  type: Signup
  url: https://www.ncbi.nlm.nih.gov/account/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ncbi
- group: company
  title: ''
  type: Blog
  url: https://pubchemblog.wordpress.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pubchem.ncbi.nlm.nih.gov/docs/
- group: operate
  title: ''
  type: FAQ
  url: https://pubchem.ncbi.nlm.nih.gov/docs/faq
- group: operate
  title: ''
  type: RateLimits
  url: https://pubchem.ncbi.nlm.nih.gov/docs/programmatic-access#section=Request-Volume-Limitations
- group: commercial
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/finops.yml
created: '2026-06-13'
description: PubChem is NCBI's open chemistry database containing information on more than 100 million chemical compounds. It provides REST and view APIs for searching chemical structures, retrieving molecular properties, bioactivity data, safety information, and drug information. PubChem integrates data from hundreds of data sources and is freely accessible without authentication for standard use.
examples:
- key_count: 4
  name: Get Compound By Cid
  slug: get-compound-by-cid
- key_count: 4
  name: Get Compound By Name
  slug: get-compound-by-name
- key_count: 4
  name: Get Compound Synonyms
  slug: get-compound-synonyms
- key_count: 4
  name: Substructure Search
  slug: substructure-search
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://pubchem.ncbi.nlm.nih.gov/favicon.ico
json_schemas:
- name: PubChem Compound Properties
  property_count: 1
  slug: compound-properties
jsonld:
- class_count: 21
  name: Pubchem Context
  property_count: 0
  slug: pubchem
layout: provider
modified: '2026-06-13'
name: PubChem
nav: Providers
network: true
overview: 'PubChem publishes 3 APIs on the [APIs.io](https://apis.io/) network: Compounds API, Structure Search API, and Utilities API. Tagged areas include Chemistry, Chemical Compounds, Drug Discovery, Bioassay, and Life Sciences.


  The PubChem catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PubChem''s developer surface includes status page, support, signup flow, GitHub presence, engineering blog, documentation, FAQ, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 47
rate_limits:
- limit_count: 4
  name: Rate Limits
  slug: rate-limits
rules:
- name: PubChem API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pubchem-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.6
  delta: -5.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.0
    developer_ergonomics: 15.2
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 50.0
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
    score: 23.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/pubchem/refs/heads/main/screenshots/pubchem-2026-06-20T192236.png
security:
- kind: domain-security
  name: Pubchem Domain Security
  slug: pubchem-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pubchem
tags:
- Chemistry
- Chemical Compounds
- Drug Discovery
- Bioassay
- Life Sciences
- NCBI
- Bioinformatics
website: https://pubchem.ncbi.nlm.nih.gov/
---
