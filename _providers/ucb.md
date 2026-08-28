---
access_model:
  confidence: high
  label: Free / Affiliation-Gated
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-26'
api_count: 8
apis:
- description: 'Berkeley IT''s centralized API management developer portal, operated by the Engineering and Integration Services (EIS) team. The catalog itself is public: an anonymous client can read all roughly 28 pu'
  name: API Central (Developer Portal)
  slug: api-central
- description: The single centralized entry point for API requests across the Berkeley campus, operated by Berkeley IT on Berkeley's own CloudFront distribution. The gateway obfuscates the internal workings and phys
  name: UC Berkeley API Gateway
  slug: api-gateway
- description: 'UC Berkeley''s Shibboleth identity provider, operated by IST-CalNet, publishes a complete unauthenticated SAML 2.0 metadata document describing how any service provider federates with the institution. '
  name: CalNet Shibboleth Identity Provider (SAML 2.0 Metadata)
  slug: calnet-shibboleth
- description: The UC Berkeley Library's GIS and map discovery application, built and hosted by the Library itself (the application source is public at BerkeleyLibrary/geodata and the host resolves inside Berkeley's
  name: UC Berkeley Library GeoData (GeoBlacklight) Catalog API
  slug: geodata
- description: Berkeley Research Computing's cluster access management system, which handles allocations, project membership and access requests for the Savio high-performance computing cluster. The host resolves to
  name: MyBRC Cluster Access Management API
  slug: mybrc
- description: Berkeley's Digital Collections repository exposes a live OAI-PMH 2.0 interface, confirmed with an actual verb=Identify response reporting repositoryName "Digital Collections", repositoryIdentifier dig
  name: UC Berkeley Digital Collections OAI-PMH (TIND tenant)
  slug: digicoll-oai
- description: eScholarship is the University of California's open-access publishing platform and institutional repository, operated system-wide by the California Digital Library, not by the Berkeley campus. Its OAI
  name: eScholarship Repository and OAI-PMH (California Digital Library tenant)
  slug: escholarship
- description: Library discovery for the Berkeley campus runs on Ex Libris Primo VE as part of the shared UC Library Search environment. search.library.berkeley.edu is a Berkeley-branded hostname that CNAMEs to berk
  name: UC Library Search / Primo VE Discovery (Ex Libris tenant)
  slug: library-search
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.berkeley.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.api.berkeley.edu/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.api.berkeley.edu/apis
- group: docs
  title: ''
  type: Documentation
  url: https://integration-services.berkeley.edu/api-management/developer-portal-api-central
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.api.berkeley.edu/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.berkeley.edu/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://developers.api.berkeley.edu/contact_us
- group: operate
  title: ''
  type: Status
  url: https://systemstatus.berkeley.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://shib.berkeley.edu/idp/shibboleth
- group: other
  title: ''
  type: OpenData
  url: https://geodata.lib.berkeley.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://digicoll.lib.berkeley.edu/oai2d?verb=Identify
- group: build
  title: ''
  type: LibraryCatalog
  url: https://search.library.berkeley.edu/discovery/search?vid=01UCS_BER:UCB
- group: learn
  title: ''
  type: CourseCatalog
  url: https://classes.berkeley.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://research-it.berkeley.edu/services-projects/high-performance-computing-savio
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.berkeley.edu/guidance
- group: build
  title: ''
  type: AITooling
  url: https://ai.berkeley.edu/tools-training
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ucberkeley
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BerkeleyLibrary
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ets-berkeley-edu
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://security.berkeley.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uc-berkeley/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/UCBerkeley
- group: auth
  title: ''
  type: Authentication
  url: authentication/ucb-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ucb-education-standards-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucb-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ucb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucb-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'UC Berkeley operates a real, centrally governed API program with a publicly readable catalog of roughly 28 campus APIs, but every contract in it is behind CalNet SSO plus Data Owner approval. developers.api.berkeley.edu/apis returns 200 to an anonymous client and lists every API''s name, description, data classification and owning organization; no API''s interactive documentation or OpenAPI definition is reachable without a CalNet identity. This profile therefore holds no OpenAPI, no JSON Schema and no examples, and none were generated, because generating them would credit Berkeley with contracts it has not published. Three institution-operated machine-readable surfaces WERE found and verified by protocol response rather than by link presence: the CalNet Shibboleth/SAML IdP metadata, the library''s GeoBlacklight JSON catalog, and the MyBRC research-computing API (401 JSON). Two repository surfaces were found and are recorded as TENANT rather than as Berkeley contracts. Berkeleytime
    (berkeleytime.com), the well-known student-built Berkeley course-data API, was probed and is live behind a Cloudflare challenge, but it runs on a non-institution domain under the ASUC student association and no evidence of University endorsement or operation was found, so it is deliberately NOT credited to Berkeley here.'
  evidence:
  - status: 200
    url: https://developers.api.berkeley.edu/apis
  - status: 200
    url: https://developers.api.berkeley.edu/api/6
  - status: 200
    url: https://developers.api.berkeley.edu/terms_of_service
  - status: 200
    url: https://gateway.api.berkeley.edu/
  - status: 200
    url: https://shib.berkeley.edu/idp/shibboleth
  - status: 200
    url: https://geodata.lib.berkeley.edu/catalog.json?q=water
  - status: 401
    url: https://mybrc.brc.berkeley.edu/api/
  - status: 200
    url: https://digicoll.lib.berkeley.edu/oai2d?verb=Identify
  - status: 200
    url: https://escholarship.org/oai?verb=Identify
  - note: Responds "Institution code 01UCS_BER is invalid" -- no Berkeley Alma OAI provider.
    status: 200
    url: https://na01.alma.exlibrisgroup.com/view/oai/01UCS_BER/request?verb=Identify
  - status: 404
    url: https://www.berkeley.edu/.well-known/security.txt
  - status: 404
    url: https://www.berkeley.edu/llms.txt
  - note: Cloudflare challenge; live but student-run, not institution-operated.
    status: 403
    url: https://berkeleytime.com/
  reason: contracts_behind_authentication
  state: gated
created: '2026-06-03'
description: 'The University of California, Berkeley is a public land-grant research university and the founding campus of the University of California system. Berkeley is one of the few universities in this cohort that genuinely operates its own API program rather than merely appearing to: Berkeley IT''s Engineering and Integration Services team runs an API Central developer portal and a shared API Gateway on Berkeley''s own infrastructure, publishing a public catalog of roughly 28 campus APIs across Student Information, HR, finance and identity, each listed with its UC data classification (P1/P2/P3) and a named Data Owner. That program is real, but it is internal-first: the catalog is public and the contracts are not. No OpenAPI definition is retrievable without a CalNet identity and Data Owner approval, so this profile holds ZERO OpenAPI documents and that is the accurate measurement, not a gap in the research. What Berkeley does publish without credentials is narrower and mostly overlooked:
  a complete Shibboleth/SAML 2.0 identity provider metadata document at shib.berkeley.edu (InCommon entity urn:mace:incommon:berkeley.edu), a live GeoBlacklight JSON catalog of 5,156 geospatial datasets at geodata.lib.berkeley.edu, and a gated but well-formed research-computing API for the Savio cluster''s access management system. Its research repositories are not its engineering: the Digital Collections OAI-PMH endpoint runs on TIND, and eScholarship is a California Digital Library service for the entire UC system. Both are recorded here as tenant relationships, not as Berkeley contracts.'
finops:
- name: Ucb Finops
  service_category: Education
  slug: ucb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucb.png
jsonld:
- class_count: 6
  name: Ucb Context
  property_count: 4
  slug: ucb-context
layout: provider
modified: '2026-08-19'
name: University of California, Berkeley
nav: Providers
network: true
overview: 'University of California, Berkeley publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Public Research University, and United States.


  The University of California, Berkeley catalog on APIs.io includes 1 JSON-LD context.


  University of California, Berkeley''s developer surface includes API reference, documentation, support, status page, authentication, and 24 more developer resources.'
plans:
- name: Ucb Plans Pricing
  plan_count: 2
  slug: ucb-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Ucb Rate Limits
  slug: ucb-rate-limits
score:
  band: thin
  composite: 35.0
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 42.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 35.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucb/refs/heads/main/screenshots/ucb-2026-06-20T195937.png
security:
- kind: authentication
  name: Ucb Authentication
  slug: ucb-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ucb Domain Security
  slug: ucb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ucb
tags:
- University
- Higher Education
- Education
- Public Research University
- United States
- California
- UC System
- Research
- Identity Federation
- Research Repository
- Research Computing
- Course Catalog
- Library
- Open Data
- Geospatial Data
- OAI-PMH
website: https://www.berkeley.edu/
---
