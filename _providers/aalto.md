---
access_model:
  confidence: high
  label: Free, but API-key issuance requires an Aalto account
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  - documentation
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-04'
api_count: 5
apis:
- description: Aalto's own Red Hat 3scale API gateway, the front door to every institution-operated API at Aalto. Five API products are documented on the portal; the underlying ActiveDocs index is public and lists f
  name: Aalto API Gateway
  slug: api-gateway
- baseURL: https://facilities.api.aalto.fi/api/aalto
  baseurl_source: declared
  description: Buildings, building details, opening hours, rooms and room reservations across Aalto's Espoo campus. OpenAPI 3.0.1, version 1.0.2, contact it-integ@aalto.fi, served from facilities.api.aalto.fi. Docum
  name: Aalto Facilities API
  slug: facilities
- baseURL: https://course.api.aalto.fi/api/sisu/v1
  baseurl_source: declared
  description: Course units and course-unit realisations drawn from SISU, the Finnish higher-education student information system Aalto runs. OpenAPI 3.0.1, version 0.0.18, titled "Sisu API (replaces /oodiapi)" — th
  name: Aalto Course API (SISU)
  slug: course-sisu
- baseURL: https://research.api.aalto.fi/api/acris/v1
  baseurl_source: declared
  description: Aalto's own four-path gateway contract over Acris, its research information system, exposing research outputs, a single output by id, an enhanced output view and output fingerprints. OpenAPI 3.0.0 ser
  name: Aalto Research Publications API (Acris gateway)
  slug: acris-research
- baseURL: https://api.aalto.fi/api/dw_projects
  baseurl_source: declared
  description: Administrative reference data — cost centres, projects, departments and schools — from Aalto's data warehouse. OpenAPI 3.0.0, version 1.0.10, X-ApiKey header, served from api.aalto.fi. The contract st
  name: Aalto Projects and Cost Centers API
  slug: projects-costcenters
- baseURL: https://aaltopeople.api.aalto.fi/api/aaltopeople/v1
  baseurl_source: declared
  description: A two-path proxy over Aaltopeople returning groups and public staff profiles. OpenAPI 3.0.1, version 1.0.3, contact it-integ@aalto.fi, served from aaltopeople.api.aalto.fi. Present in the public Activ
  name: Aalto People Profile API
  slug: people-profile
- description: 'The Oodi-sourced course API, still published on the portal and explicitly marked deprecated: "This API source is OODI and should not be used." Swagger 2.0, two paths, superseded by the SISU Course API'
  name: Aalto Open API — Course API (Oodi, deprecated)
  slug: course-oodi-deprecated
- description: 'Aalto''s institutional repository of theses, articles and conference publications, running Aalto-hosted DSpace 9.2 on aaltodoc.aalto.fi. Both read surfaces are fully anonymous and were verified live: a'
  name: Aaltodoc Repository — OAI-PMH and DSpace REST
  slug: aaltodoc
- description: Aalto's own Shibboleth SAML 2.0 identity provider, entityID https://idp.aalto.fi/idp/shibboleth, scope aalto.fi, registration authority http://www.aalto.fi registered 2019-04-15. The metadata is publi
  name: Aalto Shibboleth Identity Provider (Haka / eduGAIN)
  slug: identity-federation
- description: Aalto's open data published as Linked Data — courses, people, publications, places, projects, organisation and events — under data.aalto.fi URIs. The landing page and dataset descriptions are on Aalto
  name: Linked Open Aalto Data (SPARQL)
  slug: linked-open-data
- description: 'Aalto''s research information system is Elsevier Pure, deployed as Acris at acris.aalto.fi with the Pure Portal at research.aalto.fi. The data and the DOIs are Aalto''s; the contract is Elsevier''s. The '
  name: Acris — Aalto Current Research Information System (Elsevier Pure)
  slug: acris-pure
- description: Library discovery and the library management system are Ex Libris products under Aalto tenancies — primo.aalto.fi resolves to the Primo NDE interface with view 358AALTO_INST:MAIN, and aalto.alma.exlib
  name: Aalto Learning Centre discovery (Ex Libris Primo / Alma, Finna)
  slug: library-discovery
- description: sisu.aalto.fi is Aalto's deployment of SISU, the student information system built by Funidata, a company jointly owned by Finnish universities. It is the system of record behind the SISU Course API on
  name: SISU student information system (Funidata)
  slug: sisu-sis
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://www.aalto.fi/en
- group: docs
  title: ''
  type: Documentation
  url: https://www.aalto.fi/en/services/api-gateway-application-programming-interface
- group: docs
  title: ''
  type: APIReference
  url: https://3scale.apps.ocp4.aalto.fi/docs
- group: start
  title: ''
  type: Portal
  url: https://3scale.apps.ocp4.aalto.fi/
- group: start
  title: ''
  type: Signup
  url: https://apiportal.aalto.fi/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aalto.fi/en/aalto-handbook/privacy-notice-for-aaltofi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AaltoSciComp
- group: build
  title: ''
  type: SourceCode
  url: https://version.aalto.fi/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/aalto-university/
- group: other
  title: ''
  type: OpenData
  url: https://data.aalto.fi/
- group: other
  title: ''
  type: ResearchRepository
  url: https://aaltodoc.aalto.fi/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://primo.aalto.fi/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://sisu.aalto.fi/student/search/main
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.aalto.fi/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://scicomp.aalto.fi/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.aalto.fi/en/services/ai-in-aalto
- group: build
  title: ''
  type: AITooling
  url: https://ai.aalto.fi/
- group: auth
  title: ''
  type: Authentication
  url: authentication/aalto-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aalto-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aalto-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aalto-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aalto-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aalto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aalto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aalto-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Aalto University is a multidisciplinary public research university in Espoo, Finland, formed in 2010 from the merger of the Helsinki University of Technology, the Helsinki School of Economics and the University of Art and Design Helsinki. Unusually for this cohort, Aalto operates a real institution-owned API program rather than only a set of vendor tenancies: the Aalto API Gateway (Red Hat 3scale, at 3scale.apps.ocp4.aalto.fi) publishes five documented API products — facilities and room reservations, SISU course data, Acris research publications, projects and cost centres, and a deprecated Oodi-sourced course API — and its ActiveDocs index is publicly readable, exposing forty-four Aalto-authored Swagger/OpenAPI documents whose servers all sit under *.api.aalto.fi. Every one of those endpoints is API-key gated and returns 403 to an anonymous caller, so the contracts are public while the data is not. The genuinely anonymous surfaces are elsewhere: the Aaltodoc institutional repository
  (Aalto-hosted DSpace 9.2) serves a live OAI-PMH 2.0 endpoint with sixteen metadata formats and an open REST API, and the Linked Open Aalto Data SPARQL endpoint answers real queries — but only over POST, since GET times out. Aalto also runs its own Shibboleth SAML 2.0 identity provider and is registered in the Haka federation with forty-one entities, which is machine-readable institutional infrastructure that almost no university in this cohort catalogues. Its library discovery, research information system and research portal are vendor tenancies (Ex Libris, Elsevier Pure) and are recorded as relationships, not as Aalto''s engineering.'
finops:
- name: Aalto Finops
  service_category: Education
  slug: aalto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aalto.png
json_schemas:
- name: Sisu API (replaces /oodiapi) — component schemas
  property_count: 0
  slug: aalto-course-sisu-api
- name: Aalto facilities api — component schemas
  property_count: 0
  slug: aalto-facilities-api
jsonld:
- class_count: 20
  name: Aalto Context
  property_count: 7
  slug: aalto-context
layout: provider
modified: '2026-08-30'
name: Aalto University
nav: Providers
network: true
overview: 'Aalto University publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Aalto Facilities API, Aalto Course API (SISU), Aalto Research Publications API (Acris gateway), and 2 more. Tagged areas include University, Higher Education, Education, Finland, and Europe.


  The Aalto University catalog on APIs.io includes 1 JSON-LD context.


  Aalto University''s developer surface includes documentation, API reference, developer portal, signup flow, authentication, and 21 more developer resources.'
plans:
- name: Aalto Plans Pricing
  plan_count: 2
  slug: aalto-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Aalto Rate Limits
  slug: aalto-rate-limits
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 63.0
    catalog_earned_first_party: 0.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 54.7
    developer_ergonomics: 38.1
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 42.2
  provenance:
    conformance: first-party
    contracts:
      callable: 60.0
      derived: 0
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aalto/refs/heads/main/screenshots/aalto-2026-06-20T162945.png
security:
- kind: authentication
  name: Aalto Authentication
  slug: aalto-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aalto Domain Security
  slug: aalto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aalto
tags:
- University
- Higher Education
- Education
- Finland
- Europe
- Public Research University
- Research
- Research Data
- Open Data
- Linked Data
- Course Catalog
- Identity Federation
- Research Computing
- Library
- API Gateway
website: https://www.aalto.fi/en
---
