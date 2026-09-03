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
  score: 17.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: National Library Of Medicine Agentic Access
  operation_count: 9
  slug: national-library-of-medicine-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils
  baseurl_source: declared
  description: Discover database metadata, related records, and citations.
  name: National Library of Medicine Discovery API
  slug: national-library-of-medicine-discovery-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils
  baseurl_source: declared
  description: Manage server-side history sets via the Entrez History server.
  name: National Library of Medicine History API
  slug: national-library-of-medicine-history-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils
  baseurl_source: declared
  description: Retrieve full or summary records from Entrez databases.
  name: National Library of Medicine Retrieve API
  slug: national-library-of-medicine-retrieve-api
- baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils
  baseurl_source: declared
  description: Search Entrez databases for matching records.
  name: National Library of Medicine Search API
  slug: national-library-of-medicine-search-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NCBI E-utilities Discovery API
  slug: open-national-library-of-medicine-discovery-api
- collection_type: open
  name: NCBI E-utilities Discovery History API
  slug: open-national-library-of-medicine-history-api
- collection_type: open
  name: NCBI E-utilities Discovery Retrieve API
  slug: open-national-library-of-medicine-retrieve-api
- collection_type: open
  name: NCBI E-utilities Discovery Search API
  slug: open-national-library-of-medicine-search-api
- collection_type: open
  name: NCBI E-utilities API
  slug: open-national-library-of-medicine
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-library-of-medicine-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-library-of-medicine-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NIH-NLM
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-library-of-medicine-nlm
- group: company
  title: ''
  type: Website
  url: https://www.nlm.nih.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.ncbi.nlm.nih.gov/home/develop/api/
created: '2024-12-03'
description: The National Library of Medicine, part of the National Institutes of Health, is the world's largest biomedical library. It collects, organizes, and provides access to medical literature and information to support research and decision-making in healthcare, including PubMed and ClinicalTrials.gov.
finops:
- name: National Library Of Medicine Finops
  service_category: API
  slug: national-library-of-medicine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-library-of-medicine.png
layout: provider
modified: '2026-05-19'
name: National Library of Medicine
nav: Providers
network: true
overview: 'National Library of Medicine publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, History API, Retrieve API, and 1 more. Tagged areas include Federal-Government, Health, Library, and Medicine.


  National Library of Medicine''s developer surface includes developer portal and 5 more developer resources.'
plans:
- name: National Library Of Medicine Plans Pricing
  plan_count: 3
  slug: national-library-of-medicine-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: National Library Of Medicine Rate Limits
  slug: national-library-of-medicine-rate-limits
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-library-of-medicine/refs/heads/main/screenshots/national-library-of-medicine-2026-06-20T190032.png
security:
- kind: domain-security
  name: National Library Of Medicine Domain Security
  slug: national-library-of-medicine-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: national-library-of-medicine
tags:
- Federal-Government
- Health
- Library
- Medicine
website: https://www.nlm.nih.gov/
---
