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
  scored_at: '2026-09-03'
api_count: 13
apis:
- description: The University's own API developer portal and gateway — a self-hosted Gravitee API Management deployment. The portal REST API answers anonymously and is, in practice, the University's API discovery su
  name: University of Helsinki API Portal (Gravitee)
  slug: api-gateway
- baseURL: https://gw.api.helsinki.fi/organisation
  baseurl_source: declared
  description: 'Organisation Registry Public API — the University''s organisational units and their hierarchy. The largest gateway contract: 22 paths and 19 component schemas, OpenAPI 3.0.3, X-Api-Key.'
  name: HY Organisation API
  slug: hy-organisation
- baseURL: https://gw.api.helsinki.fi/contact-search
  baseurl_source: declared
  description: Expert and contact search, used by the public helsinki.fi pages and the Flamma intranet. OpenAPI 3.1.0, 22 paths, 33 schemas — the only 3.1 document in the estate. Returns records about identifiable s
  name: Contact Search API
  slug: contact-search
- baseURL: https://gw.api.helsinki.fi/course-pages-cms
  baseurl_source: declared
  description: 'Drupal JSON:API behind the course pages — course descriptions, materials and related content. Declares an oauth2 scheme with no flows whose description links a third-party CRM vendor''s documentation, '
  name: Course pages CMS
  slug: course-pages-cms
- baseURL: https://gw.api.helsinki.fi/public_web
  baseurl_source: declared
  description: Content API for helsinki.fi — news and study search. Notable for declaring two distinct X-Api-Key schemes, NewsApiKey and StudySearchApiKey, described as issued by two different plans; it is the clear
  name: Helsinki.fi content
  slug: helsinki-fi-content
- baseURL: https://gw.api.helsinki.fi/building
  baseurl_source: declared
  description: Buildings and spaces on the University estate. Small (2 paths) and the stalest API in the gallery — created 2020-03-18, last updated 2023-05-29.
  name: HY Building API
  slug: hy-building
- baseURL: https://gw.api.helsinki.fi/serviceapi
  baseurl_source: declared
  description: Queries the University's service catalogue. Contact is the IT Centre integration services group address, not an individual.
  name: ServiceAPI
  slug: serviceapi
- baseURL: https://gw.api.helsinki.fi/employeeinformation
  baseurl_source: declared
  description: Employee information lookup. Returns records about identifiable staff — structural examples only, no live response stored. The portal card advertises 1.4.0 while the spec it serves declares info.versi
  name: EmployeeInformationAPI
  slug: employeeinformation
- baseURL: https://gw.api.helsinki.fi/persongroup
  baseurl_source: declared
  description: Selected groups and their member data. Personal data; structural examples only.
  name: PersonGroup
  slug: persongroup
- baseURL: https://gw.api.helsinki.fi/efecte
  baseurl_source: declared
  description: Creates service requests in Efecte, the University's IT service management platform. University-operated endpoint in front of a commercial ITSM product.
  name: General Efecte API
  slug: general-efecte
- baseURL: https://gw.api.helsinki.fi/netdata
  baseurl_source: declared
  description: Interface to the University's network registry data (production instance). Declares its API key header as X-API-Key where the rest of the estate uses X-Api-Key.
  name: Network registry API
  slug: network-registry
- baseURL: https://gw.api.helsinki.fi/ssapi
  baseurl_source: declared
  description: The University's application-portfolio register — a machine-readable inventory of the software the institution runs. Declares no security scheme and no error responses, so its published contract canno
  name: Sovellussalkku API
  slug: sovellussalkku
- baseURL: https://gw.api.helsinki.fi/secure/dawasync
  baseurl_source: declared
  description: Posts data into named data-warehouse tables. Newest API in the gallery (created 2026-04-20) and, like Sovellussalkku, publishes no security scheme or error responses.
  name: Dawa Sync API
  slug: dawa-sync
- description: SBOM upload to the University's Dependency Track instance from external networks. Public and running in the portal, but publishes no OpenAPI page, so no contract is stored here.
  name: Dependency Track
  slug: dependency-track
- description: Liferay headless delivery API for Flamma, the staff intranet, distributed through the University gateway. No OpenAPI page is published; the upstream contract is Liferay's.
  name: Flamma Liferay Headless API
  slug: flamma-liferay-headless
- description: Authenticated access to the Drupal JSON:API behind the internal guide, covering published and unpublished content. No OpenAPI page is published.
  name: Internal Guide CMS JSON-API
  slug: internal-guide-cms
- baseURL: https://api.laji.fi
  baseurl_source: declared
  description: 'The largest contract the University of Helsinki operates: 177 paths and 239 component schemas over Finnish species, taxonomy, occurrence records, collections, image bank and data requests. Operated by'
  name: FinBIF Laji API (Finnish Biodiversity Information Facility)
  slug: finbif-laji
- description: Public HAL REST API for Helda, the University's open institutional repository, running DSpace 7.6.2. Discovery/search, items, collections, communities and the metadata registry are all readable anonym
  name: Helda DSpace REST API
  slug: helda-rest
- description: OAI-PMH 2.0 harvesting endpoint for Helda. Identify returns repositoryName "Helda" with an earliest datestamp of 1976-05-13, and ListMetadataFormats returns fourteen prefixes — oai_dc, qdc, qdc_helda,
  name: Helda OAI-PMH Metadata Interface
  slug: helda-oai
- description: 'A SECOND, separate DSpace deployment — datakatalogi.helsinki.fi, running DSpace 9.0 with dspaceName "HyDatacatalogue" — cataloguing research DATA rather than publications. New: its OAI earliest datest'
  name: HY Data Catalogue DSpace REST API
  slug: datakatalogi-rest
- description: OAI-PMH 2.0 endpoint for the HY Data Catalogue. Identify returns repositoryName "HyDatacatalogue", adminEmail datakatalogi@helsinki.fi, granularity YYYY-MM-DDThh:mm:ssZ. Institution-operated and anony
  name: HY Data Catalogue OAI-PMH Interface
  slug: datakatalogi-oai
- description: OAI-PMH 2.0 endpoint for Editori, the University's open publishing service (PKP Open Journal Systems). Identify returns repositoryName "Editori - Avoimen julkaisemisen palvelu", adminEmail editori@hel
  name: Editori (journals.helsinki.fi) OAI-PMH Interface
  slug: editori-oai
- description: 'The University''s identity provider at login.helsinki.fi, machine-readable twice over. SAML: GET /idp/shibboleth returns an EntityDescriptor with entityID https://login.helsinki.fi/shibboleth, an IDPSS'
  name: HY Login Service — Shibboleth IdP + OpenID Connect
  slug: identity-provider
- description: TENANT RELATIONSHIP, NOT A UNIVERSITY CONTRACT. The University runs its own instance of Sisu, the student information system built by Funidata Oy and shared across Finnish universities, at sisu.helsin
  name: Sisu (Kori) Student Information System — University of Helsinki tenant
  slug: sisu-kori
- description: TENANT RELATIONSHIP. researchportal.helsinki.fi is an Elsevier Pure deployment (the page markup identifies Pure and Elsevier directly). It is the University's research information system and its conte
  name: University of Helsinki Research Portal — Elsevier Pure tenant
  slug: research-portal
- description: TENANT RELATIONSHIP. helka.helsinki.fi redirects to an Ex Libris Primo discovery interface with view identifier 358UOH_INST:VU1. Library discovery is the surface class that is almost always a vendor's
  name: Helka Library Discovery — Ex Libris Primo tenant
  slug: helka
artifact_total: 47
common:
- group: company
  title: ''
  type: Website
  url: https://www.helsinki.fi/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.helsinki.fi/portal/
- group: docs
  title: ''
  type: APIReference
  url: https://api.helsinki.fi/portal/environments/DEFAULT/apis
- group: docs
  title: ''
  type: Documentation
  url: https://api.helsinki.fi/portal/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UniversityofHelsinki
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UniversityofHelsinki
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/UH-StudentServices
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-helsinki/
- group: company
  title: ''
  type: Blog
  url: https://blogs.helsinki.fi/
- group: company
  title: ''
  type: News
  url: https://www.helsinki.fi/en/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.helsinki.fi/en/about-us/processing-data-university/data-protection
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.helsinki.fi/.well-known/security.txt
- group: other
  title: ''
  type: ResearchRepository
  url: https://helda.helsinki.fi/
- group: other
  title: ''
  type: OpenData
  url: https://datakatalogi.helsinki.fi/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://helka.helsinki.fi/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://studies.helsinki.fi/courses
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.helsinki.fi/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://haka.funet.fi/metadata/haka-metadata.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.helsinki.fi/en/research/research-units-and-infrastructures/research-infrastructures
- group: other
  title: ''
  type: AIPolicy
  url: https://studies.helsinki.fi/instructions/article/using-ai-support-learning
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-helsinki-hy-organisation-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-helsinki-hy-organisation-api-schemas.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-helsinki-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-helsinki-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-helsinki-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-helsinki-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-helsinki-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-helsinki-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/university-of-helsinki-examples.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-helsinki-openapi-spectral-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-helsinki-context.jsonld
- group: docs
  title: ''
  type: GraphQL
  url: graphql/university-of-helsinki-graphql.md
- group: agent
  title: ''
  type: WellKnown
  url: well-known/university-of-helsinki-openid-configuration.json
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-helsinki-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-helsinki-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-helsinki-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-helsinki-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-helsinki-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Helsinki is Finland''s oldest and largest multidisciplinary research university, founded in 1640, and it is one of the very few institutions in this cohort that operates a real, first-party API program rather than only renting vendor platforms. It runs its own Gravitee API gateway at gw.api.helsinki.fi behind a public developer portal at api.helsinki.fi, listing fifteen public APIs — organisations, buildings and spaces, employee and group directories, service management, the application-portfolio register, network registry, and the CMS behind helsinki.fi and the course pages — twelve of which publish a readable OpenAPI. Alongside that sit genuinely institution-operated scholarly and identity infrastructure: Helda (DSpace 7.6.2) and the newer HY Data Catalogue (DSpace 9.0), three live OAI-PMH endpoints, the Editori open-publishing service, the Shibboleth/OIDC identity provider at login.helsinki.fi with sixteen entities registered in the Haka federation, and
  the Finnish Biodiversity Information Facility (api.laji.fi, 177 paths), which is run by Luomus, a University institute. What the University does NOT author is equally important and is recorded here as tenancy rather than as its own work: Sisu/Kori is Funidata''s, the research portal is Elsevier Pure, and Helka is Ex Libris Primo. The gateway is affiliation-gated — keyless access is disabled and portal self-registration is off — so the catalogue and every specification are readable by anyone, while a credential requires a university or Haka identity.'
finops:
- name: University Of Helsinki Finops
  service_category: Education
  slug: university-of-helsinki-finops
graphqls:
- description: '<!-- x-method: searched -->'
  name: GraphQL at the University of Helsinki
  slug: university-of-helsinki-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-helsinki.png
json_schemas:
- name: University of Helsinki - Contact Search API — component schemas
  property_count: 0
  slug: university-of-helsinki-contact-search-api-schemas
- name: University of Helsinki - Courses content machine - JSON API — component schemas
  property_count: 0
  slug: university-of-helsinki-course-pages-cms-schemas
- name: EmployeeInformationAPI — component schemas
  property_count: 0
  slug: university-of-helsinki-employeeinformationapi-schemas
- name: Laji API — component schemas
  property_count: 0
  slug: university-of-helsinki-finbif-laji-schemas
- name: General Efecte API — component schemas
  property_count: 0
  slug: university-of-helsinki-general-efecte-api-schemas
- name: Helsinki.fi content — component schemas
  property_count: 0
  slug: university-of-helsinki-helsinki-fi-content-schemas
- name: HY Building API — component schemas
  property_count: 0
  slug: university-of-helsinki-hy-building-api-schemas
- name: Organisation Registry Public API — component schemas
  property_count: 0
  slug: university-of-helsinki-hy-organisation-api-schemas
- name: network registry — component schemas
  property_count: 0
  slug: university-of-helsinki-network-registry-api-schemas
- name: HY Person/Group API — component schemas
  property_count: 0
  slug: university-of-helsinki-persongroup-schemas
- name: ServiceAPI — component schemas
  property_count: 0
  slug: university-of-helsinki-serviceapi-schemas
jsonld:
- class_count: 30
  name: University Of Helsinki Context
  property_count: 5
  slug: university-of-helsinki-context
layout: provider
modified: '2026-08-30'
name: University of Helsinki
nav: Providers
network: true
overview: 'University of Helsinki publishes 13 APIs on the [APIs.io](https://apis.io/) network, including HY Organisation API, Contact Search API, Course pages CMS, and 10 more. Tagged areas include Education, Higher Education, University, Finland, and Nordic.


  The University of Helsinki catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Helsinki''s developer surface includes API reference, documentation, GitHub presence, engineering blog, product news, authentication, code examples, and 32 more developer resources.'
plans:
- name: University Of Helsinki Plans Pricing
  plan_count: 3
  slug: university-of-helsinki-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: University Of Helsinki Rate Limits
  slug: university-of-helsinki-rate-limits
rules:
- effective_rule_count: 13
  extends: []
  name: University of Helsinki API Rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 8
  slug: university-of-helsinki-openapi-spectral-rules
scopes:
- name: University Of Helsinki Scopes
  scope_count: 0
  slug: university-of-helsinki-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 44.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 29.5
    contract_quality: 63.6
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 29.5
    operational_transparency: 10.5
  previous_composite: 54.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 83.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-helsinki/refs/heads/main/screenshots/university-of-helsinki-2026-06-20T200155.png
security:
- kind: authentication
  name: University Of Helsinki Authentication
  slug: university-of-helsinki-authentication
  summary_line: apiKey/http-bearer/oauth2 · 5 schemes
- kind: domain-security
  name: University Of Helsinki Domain Security
  slug: university-of-helsinki-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Helsinki Vulnerability Disclosure
  slug: university-of-helsinki-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-helsinki
tags:
- Education
- Higher Education
- University
- Finland
- Nordic
- Research
- Open Data
- Research Data
- Institutional Repository
- OAI-PMH
- Identity Federation
- API Gateway
- Course Catalog
- Library
- Biodiversity
website: https://www.helsinki.fi/en
---
