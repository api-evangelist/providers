---
access_model:
  confidence: high
  label: Free · no registration
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
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
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://www.curtin.edu.au/wp-json
  baseurl_source: declared
  description: Curtin's own REST namespace on its public web platform, keyless and live. Serves the global navigation, site menu and footer shared across Curtin's federated WordPress estate, and exposes search/elast
  name: Curtin Web Platform API (mimas/v1)
  slug: web-platform
- baseURL: https://api.coki.ac
  baseurl_source: declared
  description: Curtin's most substantial self-engineered API. Keyless, CORS-open JSON serving open-access performance statistics for 60,562 institutions and every country, keyed on ROR identifiers, with a 26-year pe
  name: COKI Open Access Dashboard API
  slug: coki
- description: A Shibboleth SAML 2.0 service provider that Curtin Library runs on its own Kubernetes cluster, serving its entity metadata unauthenticated as application/samlmetadata+xml at the standard Shibboleth.ss
  name: Curtin Library Shibboleth Service Provider
  slug: identity-sp
- description: Curtin's SAML 2.0 Identity Provider, entityID https://idpp1.curtin.edu.au/idp/shibboleth, registered in the Australian Access Federation and reachable through eduGAIN. It serves its own entity metadat
  name: Curtin University SAML Identity Provider (AAF Managed IdP)
  slug: identity-idp
- description: Curtin's internal data catalog, dashboard and file-search platform — a Remix single-page application at data.curtin.edu.au calling a Curtin-operated AWS API Gateway at /prod/AMP/Catalogs and /prod/AMP
  name: Curtin Data Platform (AMP)
  slug: data-platform
- description: 'Curtin''s institutional research repository, formerly espace on Ex Libris, now running on Figshare at curate.curtin.edu.au. The data, the theses, the DOIs and the tenant are Curtin''s; the platform and '
  name: Curtin Curate Research Repository (Figshare tenant)
  slug: curate
- description: Curtin University is a DataCite member organisation and had minted 3,243 DOIs under its provider at time of probing, across two registered repositories — `ardcx.curtin`, the Curtin University Research
  name: Curtin University DOI Registration (DataCite)
  slug: datacite
- description: Curtin Library's discovery layer, running on Ex Libris Primo over Alma. The collection and the holdings are Curtin's; the platform, its APIs and its contracts are Ex Libris's and are not saved here. R
  name: Curtin Library Discovery (Ex Libris Primo/Alma tenant)
  slug: catalogue
- description: Curtin's learning management system, a Blackboard Learn tenant fronted by Curtin's own PingAM SAML identity provider at id.curtin.edu.au. Any LTI, Caliper or QTI conformance here is Blackboard's produ
  name: Curtin Blackboard Learn (tenant)
  slug: lms
- description: Curtin contributes research data collection records to Research Data Australia, the national registry run by the Australian Research Data Commons. The records are Curtin's; the registry, its harvestin
  name: Curtin Research Data in Research Data Australia (ARDC)
  slug: researchdata
artifact_total: 23
common:
- group: company
  title: ''
  type: Website
  url: https://www.curtin.edu.au/
- group: company
  title: ''
  type: Website
  url: https://open.coki.ac/
- group: docs
  title: ''
  type: APIReference
  url: https://www.curtin.edu.au/wp-json/
- group: other
  title: ''
  type: OpenData
  url: https://data.curtin.edu.au/
- group: other
  title: ''
  type: ResearchRepository
  url: https://curate.curtin.edu.au/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalogue.curtin.edu.au/discovery/search?vid=61CUR_INST:CUR_ALMA
- group: learn
  title: ''
  type: CourseCatalog
  url: https://handbook.curtin.edu.au/
- group: other
  title: ''
  type: IdentityFederation
  url: https://auth.lis.curtin.edu.au/Shibboleth.sso/Metadata
- group: other
  title: ''
  type: IdentityFederation
  url: https://idpp1.curtin.edu.au/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://datascience.curtin.edu.au/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.curtin.edu.au/about/values-vision-strategy/artificial-intelligence/
- group: build
  title: ''
  type: AITooling
  url: https://www.curtin.edu.au/students/essentials/rights/academic-integrity/gen-ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CurtinIDS
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Curtin-Open-Knowledge-Initiative
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/The-Academic-Observatory
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curtin.edu.au/disclaimer-of-liability/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.curtin.edu.au/about/governance/privacy/
- group: commercial
  title: ''
  type: License
  url: https://www.curtin.edu.au/copyright-statement/
- group: operate
  title: ''
  type: Support
  url: https://www.curtin.edu.au/about/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.curtin.edu.au/news/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/curtin-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/curtin-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/curtin-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/curtin-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/curtin-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curtin-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/curtin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/curtin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/curtin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Curtin University is a public research university in Perth, Western Australia, and the largest university in the state. Its programmable footprint is small, real, and almost entirely unadvertised: Curtin operates no developer portal, publishes no OpenAPI, and issues no API keys, yet three institution-operated surfaces answer unauthenticated requests today. The first is `mimas/v1`, the bespoke REST namespace registered by Curtin''s own WordPress theme on www.curtin.edu.au, whose `search/elastic` endpoint is a keyless proxy onto Curtin''s Elasticsearch cluster indexing `curtin-learning-offerings-prod-*` — the university''s course and unit catalog. The second is the Curtin Open Knowledge Initiative''s open-access analytics API at api.coki.ac, which serves CORS-open JSON for 60,562 institutions and every country with a 26-year time series, and is the most substantial API Curtin engineers itself. The third is identity: Curtin Library runs a Shibboleth SAML 2.0 service provider on
  its own Kubernetes cluster, registered in the Australian Access Federation and therefore eduGAIN, serving its entity metadata publicly. Curtin''s matching Identity Provider carries a curtin.edu.au hostname but CNAMEs into AAF''s managed IdP service, so it is recorded as a tenant, a distinction only DNS resolution reveals. Beyond those, Curtin is a buyer rather than a producer. The research repository at curate.curtin.edu.au is a Figshare tenant — espace.curtin.edu.au, which this profile previously described as an Ex Libris Primo/Esploro repository, now hard-redirects there. Library discovery is an Ex Libris Primo/Alma tenant, the LMS is a Blackboard tenant, and the service desk is ServiceNow. Those relationships are recorded here as tenant surfaces because they are genuine institutional facts; the contracts behind them belong to the vendors and are deliberately not saved under Curtin''s name.'
examples:
- key_count: 2
  name: Curtin Coki Institution 02N415Q13
  slug: curtin-coki-institution-02n415q13
- key_count: 2
  name: Curtin Coki Search Curtin
  slug: curtin-coki-search-curtin
- key_count: 2
  name: Curtin Web Global Menu
  slug: curtin-web-global-menu
- key_count: 3
  name: Curtin Web Header 403
  slug: curtin-web-header-403
- key_count: 2
  name: Curtin Web Search Elastic Engineering
  slug: curtin-web-search-elastic-engineering
finops:
- name: Curtin Finops
  service_category: Education
  slug: curtin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/curtin.png
json_schemas:
- name: COKI Entity
  property_count: 20
  slug: curtin-coki-entity
- name: Curtin Web Search Response (mimas/v1)
  property_count: 0
  slug: curtin-web-search
jsonld:
- class_count: 10
  name: Curtin Context
  property_count: 2
  slug: curtin-context
layout: provider
modified: '2026-08-30'
name: Curtin University
nav: Providers
network: true
overview: 'Curtin University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Curtin Web Platform API (mimas/v1) and COKI Open Access Dashboard API. Tagged areas include University, Higher Education, Education, Research, and Open Access.


  The Curtin University catalog on APIs.io includes 1 JSON-LD context.


  Curtin University''s developer surface includes API reference, support, engineering blog, authentication, and 26 more developer resources.'
plans:
- name: Curtin Plans Pricing
  plan_count: 2
  slug: curtin-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Curtin Rate Limits
  slug: curtin-rate-limits
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 50.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 26.1
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.5
  provenance:
    conformance: unknown
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/curtin/refs/heads/main/screenshots/curtin-2026-06-20T175346.png
security:
- kind: authentication
  name: Curtin Authentication
  slug: curtin-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Curtin Domain Security
  slug: curtin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: curtin
tags:
- University
- Higher Education
- Education
- Research
- Open Access
- Open Data
- Course Catalog
- Library
- Identity Federation
- Research Data
- Australia
- Western Australia
- Australian Technology Network
website: https://www.curtin.edu.au/
---
