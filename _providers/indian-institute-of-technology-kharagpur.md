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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 23.0
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: http://www.idr.iitkgp.ac.in/xmlui/open-search/discover
  baseurl_source: declared
  description: OpenSearch 1.1 query interface over the Central Library's Institutional Digital Repository, running DSpace 6.0 self-hosted on the institute's own www.idr.iitkgp.ac.in. Verified live 2026-09-01 — /xmlu
  name: IIT Kharagpur Institutional Digital Repository OpenSearch Interface
  slug: idr-opensearch
- baseURL: https://erp.iitkgp.ac.in/InfoCellDetails/resources/external/cepdata
  baseurl_source: declared
  description: 'The only unauthenticated endpoint on the IIT Kharagpur estate that the institute wrote itself. The ERP at erp.iitkgp.ac.in is a JAX-RS application on Apache Tomcat 8.0.51 behind a bespoke session SSO '
  name: IIT Kharagpur ERP Continuing Education Programme Brochure Endpoint
  slug: erp-cep-brochures
- description: Indian Research Information Network System (IRINS) research-profile portal for IIT Kharagpur, operated by INFLIBNET — an autonomous inter-university centre of the UGC — at the institution-specific sub
  name: IIT Kharagpur IRINS Research Profile Portal (INFLIBNET tenant)
  slug: irins
- description: The alumni network at alumni.iitkgp.ac.in is an AlmaConnect deployment. The hostname is the institute's but the DNS record is a CNAME to alumni.iitkgp.ac.in.s3-website.ap-south-1.amazonaws.com, and th
  name: IIT Kharagpur Alumni Network (AlmaConnect tenant)
  slug: alumni-network
- description: IIT Kharagpur is registered in ROR as https://ror.org/03w5sq511, "Indian Institute of Technology Kharagpur" (aliases IIT KGP, IIT Kharagpur), linked to http://www.iitkgp.ac.in/. Retrieved from https:/
  name: Research Organization Registry membership
  slug: ror
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.iitkgp.ac.in/
- group: other
  title: ''
  type: ResearchRepository
  url: http://www.idr.iitkgp.ac.in/xmlui/
- group: docs
  title: ''
  type: APIReference
  url: http://www.idr.iitkgp.ac.in/xmlui/open-search/description.xml
- group: learn
  title: ''
  type: CourseCatalog
  url: https://erp.iitkgp.ac.in/InfoCellDetails/resources/external/cepdata?course_id=IIT/CEP/CFC/CFC/2025-2026/HS/144
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpc.iitkgp.ac.in/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.iitkgp.ac.in/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hpc.iitkgp.ac.in/privacy-policy
- group: build
  title: ''
  type: GitHub
  url: https://github.com/IIT-KGP
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/indian-institute-of-technology-kharagpur/
- group: other
  title: ''
  type: ProductPage
  url: https://iitkgp.irins.org/
- group: other
  title: ''
  type: ProductPage
  url: https://nptel.iitkgp.ac.in/
- group: design
  title: ''
  type: Conformance
  url: conformance/indian-institute-of-technology-kharagpur-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/indian-institute-of-technology-kharagpur-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/indian-institute-of-technology-kharagpur-errors.yml
- group: design
  title: ''
  type: Rules
  url: rules/indian-institute-of-technology-kharagpur-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/indian-institute-of-technology-kharagpur-vocabulary.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/indian-institute-of-technology-kharagpur-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/indian-institute-of-technology-kharagpur-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/indian-institute-of-technology-kharagpur-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/indian-institute-of-technology-kharagpur-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/indian-institute-of-technology-kharagpur-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Indian Institute of Technology Kharagpur (IIT KGP) is an Institute of National Importance in West Bengal, India — the first of the IITs, founded 1951, and ranked #222 in the QS World University Rankings 2025. It runs no developer portal, publishes no OpenAPI and issues no API keys, and this profile does not pretend otherwise. What it does operate, on its own iitkgp.ac.in hosts, are two unauthenticated machine surfaces found by probing rather than by documentation. The Central Library''s Institutional Digital Repository (DSpace 6.0, 8,162 items, the first IR among the IITs) exposes an OpenSearch 1.1 description document and an Atom query endpoint at www.idr.iitkgp.ac.in/xmlui — served over plain HTTP only, with every identifier in the feed emitted as http://127.0.0.1/xmlui because dspace.baseUrl is misconfigured, and with no OAI-PMH provider, no DSpace REST API and no registered Handle prefix. The institute''s own ERP exposes a single public JAX-RS resource, /InfoCellDetails/resources/external/cepdata,
  which returns the brochure PDF for any Continuing Education Programme course by structured course_id; the institute homepage links it two hundred times, and it is the only endpoint on the estate that IIT Kharagpur itself wrote and left open. Everything else is gated or leased: the ERP behind a bespoke session SSO whose JAX-RS WADL 302s to a login page, the PARAM Shakti HPC allocation system behind its own login, the IRINS research-profile portal a tenant deployment on INFLIBNET''s Cloudflare-fronted platform, and the alumni network a tenant on AlmaConnect. No Shibboleth or SAML identity provider for iitkgp.ac.in exists anywhere in eduGAIN, including in India''s own INFED federation where peer IITs are registered; the institute is not a DataCite or Crossref member and mints no DOIs. Its one verifiable registry membership is ROR 03w5sq511. The institute website itself returns HTTP 200 with an Angular shell for /llms.txt, /.well-known/security.txt and /sitemap.xml alike, so none of those
  exist either.'
finops:
- name: Indian Institute Of Technology Kharagpur Finops
  service_category: Education
  slug: indian-institute-of-technology-kharagpur-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/indian-institute-of-technology-kharagpur.png
json_schemas:
- name: IIT Kharagpur ERP CEP Brochure Request
  property_count: 1
  slug: indian-institute-of-technology-kharagpur-erp-cep-request
- name: IIT Kharagpur IDR OpenSearch Result Feed
  property_count: 9
  slug: indian-institute-of-technology-kharagpur-idr-opensearch-feed
jsonld:
- class_count: 10
  name: Indian Institute Of Technology Kharagpur Context
  property_count: 18
  slug: indian-institute-of-technology-kharagpur-context
layout: provider
modified: '2026-09-01'
name: Indian Institute of Technology Kharagpur
nav: Providers
network: true
overview: 'Indian Institute of Technology Kharagpur publishes 2 APIs on the [APIs.io](https://apis.io/) network: IIT Kharagpur Institutional Digital Repository OpenSearch Interface and IIT Kharagpur ERP Continuing Education Programme Brochure Endpoint. Tagged areas include Education, Higher Education, University, Institute of Technology, and India.


  The Indian Institute of Technology Kharagpur catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Indian Institute of Technology Kharagpur''s developer surface includes API reference, GitHub presence, authentication, and 19 more developer resources.'
plans:
- name: Indian Institute Of Technology Kharagpur Plans Pricing
  plan_count: 2
  slug: indian-institute-of-technology-kharagpur-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Indian Institute Of Technology Kharagpur Rate Limits
  slug: indian-institute-of-technology-kharagpur-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Indian Institute of Technology Kharagpur API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: indian-institute-of-technology-kharagpur-rules
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 45.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 3.8
    contract_quality: 67.1
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 3.8
    operational_transparency: 26.3
  previous_composite: 41.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/indian-institute-of-technology-kharagpur/refs/heads/main/screenshots/indian-institute-of-technology-kharagpur-2026-06-20T183332.png
security:
- kind: authentication
  name: Indian Institute Of Technology Kharagpur Authentication
  slug: indian-institute-of-technology-kharagpur-authentication
  summary_line: none/session · 4 schemes
- kind: domain-security
  name: Indian Institute Of Technology Kharagpur Domain Security
  slug: indian-institute-of-technology-kharagpur-domain-security
  summary_line: TLSv1.3 · DMARC
slug: indian-institute-of-technology-kharagpur
tags:
- Education
- Higher Education
- University
- Institute of Technology
- India
- Research
- Research Repository
- Institutional Repository
- DSpace
- OpenSearch
- Course Catalog
- Research Computing
- Library
website: https://www.iitkgp.ac.in/
---
