---
access_model:
  confidence: medium
  label: Free — public repository reads are keyless; deposit and identity are affiliation-gated
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
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
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: Queen's runs its own Shibboleth Identity Provider and publishes SAML 2.0 IdP metadata as application/xml at a stable, unauthenticated URL on its own registrable domain. The EntityDescriptor carries en
  name: Queen's University Shibboleth Identity Provider (SAML 2.0 Metadata)
  slug: identity-federation
- description: QSpace is Queen's open-access institutional repository for theses, dissertations and scholarship. The repository identity is unambiguously Queen's — the DSpace REST root reports dspaceName "Queens Uni
  name: QSpace — Queen's University Institutional Repository (DSpace on Scholaris)
  slug: qspace-scholaris
- description: The Queen's University Dataverse Collection is Queen's multidisciplinary research-data repository — collection alias "queens", id 41133, affiliation "Queen's University", holding 815 datasets with Dat
  name: Queen's University Dataverse Collection (Borealis)
  slug: borealis-queens-dataverse
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.queensu.ca/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.queensu.ca/llms.txt
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.queensu.ca/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://queensu.scholaris.ca/
- group: other
  title: ''
  type: OpenData
  url: https://borealisdata.ca/dataverse/queens
- group: build
  title: ''
  type: LibraryCatalog
  url: https://ocul-qu.primo.exlibrisgroup.com/discovery/search?vid=01OCUL_QU:QU_DEFAULT
- group: learn
  title: ''
  type: CourseCatalog
  url: https://qmulus.io/
- group: other
  title: ''
  type: ResearchComputing
  url: https://cac.queensu.ca/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.queensu.ca/ai/strategic-framework/guiding-principles-responsible-use
- group: build
  title: ''
  type: AITooling
  url: https://www.queensu.ca/ai/applications
- group: build
  title: ''
  type: Library
  url: https://library.queensu.ca/
- group: operate
  title: ''
  type: Support
  url: https://www.queensu.ca/its/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.queensu.ca/accessandprivacy/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/queens-qmulus
- group: company
  title: ''
  type: Blog
  url: https://www.queensu.ca/gazette/rss.xml
- group: design
  title: ''
  type: Conformance
  url: conformance/queens-university-at-kingston-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/queens-university-at-kingston-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/queens-university-at-kingston-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/queens-university-at-kingston-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/queens-university-at-kingston-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/queens-university-at-kingston-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Queen''s operates no public API of its own. Every callable surface reachable under its name is a tenant deployment on a shared Ontario or Canadian platform: QSpace runs as DSpace 8.4 on Scholaris (OCUL / Scholars Portal) after qspace.library.queensu.ca was redirected to queensu.scholaris.ca, and the Queen''s University Dataverse Collection runs inside Borealis (Scholars Portal). Library discovery is Ex Libris Primo on the OCUL shared instance. Two surfaces ARE genuinely Queen''s own and are recorded as such: the Shibboleth / SAML 2.0 IdP metadata at login.queensu.ca, and a substantive authored llms.txt at www.queensu.ca. The one previously catalogued open-data API, the student-built Qmulus project, is dead — api.qmulus.io and manage.qmulus.io return NXDOMAIN and its GitHub org has not been pushed to since January 2023 — so its landing page is kept only as a CourseCatalog pointer and it is no longer listed as an API. No institution-operated OpenAPI exists, and none was generated;
    36 previously stored specs were the Dataverse product''s contract and were removed with everything derived from them.'
  evidence:
  - status: 200
    url: https://login.queensu.ca/idp/shibboleth
  - status: 200
    url: https://www.queensu.ca/llms.txt
  - status: 301
    url: https://qspace.library.queensu.ca/server/api
  - status: 200
    url: https://queensu.scholaris.ca/server/api
  - status: 200
    url: https://queensu.scholaris.ca/server/oai/request?verb=Identify
  - status: 200
    url: https://borealisdata.ca/api/dataverses/queens
  - status: 0
    url: https://api.qmulus.io/v1
  - status: 0
    url: https://manage.qmulus.io/token
  - status: 0
    url: https://api.queensu.ca/
  - status: 0
    url: https://developer.queensu.ca/
  - status: 0
    url: https://data.queensu.ca/
  reason: tenant_only
  state: none
created: '2026-06-03'
description: 'Queen''s University at Kingston is a public research university in Kingston, Ontario, Canada — a member of the U15 group of Canadian research universities, serving more than 25,000 students. Its machine-readable footprint is small, and stating it honestly matters more than inflating it: Queen''s operates no public developer portal, no institution-run open-data API, and no published course, timetable, or registrar contract. api.queensu.ca, developer.queensu.ca and data.queensu.ca do not resolve. What Queen''s genuinely operates and publishes on its own domain is federated identity — a Shibboleth Identity Provider serving SAML 2.0 metadata at login.queensu.ca — and an authored llms.txt directing AI agents to official sources. Its two research-data surfaces are real institutional facts but are tenant deployments, not Queen''s engineering: QSpace, the institutional repository, now runs as DSpace 8.4 on Scholaris, the shared service of the Ontario Council of University Libraries,
  and the Queen''s University Dataverse Collection lives inside Borealis, the national Dataverse operated by Scholars Portal. Both expose live REST and OAI-PMH interfaces, and both contracts belong to their platforms. An earlier profile of this repository carried 36 OpenAPI definitions titled after Queen''s; every one of them was the Dataverse product''s own contract, and they have been removed.'
finops:
- name: Queens University At Kingston Finops
  service_category: Education
  slug: queens-university-at-kingston-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/queens-university-at-kingston.png
layout: provider
modified: '2026-08-30'
name: Queen's University at Kingston
nav: Providers
network: true
overview: 'Queen''s University at Kingston publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Canada, and Ontario.


  Queen''s University at Kingston''s developer surface includes support, GitHub presence, engineering blog, authentication, and 18 more developer resources.'
plans:
- name: Queens University At Kingston Plans Pricing
  plan_count: 2
  slug: queens-university-at-kingston-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Queens University At Kingston Rate Limits
  slug: queens-university-at-kingston-rate-limits
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 4.4
    developer_ergonomics: 28.6
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 28.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/queens-university-at-kingston/refs/heads/main/screenshots/queens-university-at-kingston-2026-06-20T192420.png
security:
- kind: authentication
  name: Queens University At Kingston Authentication
  slug: queens-university-at-kingston-authentication
  summary_line: saml2 · 3 schemes
- kind: domain-security
  name: Queens University At Kingston Domain Security
  slug: queens-university-at-kingston-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: queens-university-at-kingston
tags:
- University
- Higher Education
- Education
- Canada
- Ontario
- U15
- Public Research University
- Research Data
- Institutional Repository
- Identity Federation
- OAI-PMH
- Library
website: https://www.queensu.ca/
---
