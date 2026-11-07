---
access_model:
  confidence: high
  label: Free · course data open, SSO keys issued by email on request
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  - documentation
  - authentication
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The university's digital preservation platform for theses, dissertations, rare books, multimedia and digitised manuscripts, operated by the Office of Academic Resources. cuir.car.chula.ac.th, the lega
  name: Chula DigiVerse — Institutional Digital Repository
  slug: digiverse
- description: The university's open-access journals, theses and ETD platform, and the only working OAI-PMH endpoint in the estate. The Identify response names "Chula Digital Collections", ListSets returns 30 sets i
  name: Chula Digital Collections (bepress Digital Commons tenant)
  slug: digital-collections
- description: The university's cloud identity, and the most complete machine-readable contract anywhere in this profile. Entra tenant 271d5e7b-1350-4b96-ab84-52dbda4cf40c carries the federation brand name "Chulalon
  name: Chulalongkorn University Identity Federation (Microsoft Entra ID tenant)
  slug: entra-federation
- description: Chulalongkorn University is a DataCite consortium organization, provider id lygd, country TH, with one registered repository — lygd.aguxul, "Chula Digiverse", pointing at digiverse.chula.ac.th. This i
  name: DataCite Membership (consortium organization lygd)
  slug: datacite
- description: Chulalongkorn registers Crossref DOIs through eleven separate member records, one per faculty, institute or office, each with its own prefix — Engineering 10.4186, Medicine 10.5372, Architecture 10.54
  name: Crossref Membership (eleven faculty and institute member records)
  slug: crossref
- description: 'Chulalongkorn University''s Research Organization Registry record, carrying the Thai and English names, the acronym CU, ten Crossref Funder IDs, GRID grid.7922.e, ISNI 0000 0001 0244 7875 and Wikidata '
  name: ROR Registration (https://ror.org/028wp3y58)
  slug: ror
- description: The Office of Academic Resources fronts its licensed-content discovery through EBSCO, under the named customer account chulalun. The links published on car.chula.ac.th carry that account explicitly (p
  name: Chula Library Discovery (EBSCO tenant)
  slug: library-discovery
- description: The university's central data exchange, consolidating and sharing data across departments in two connection modes — batch over SFTP and online over an API. Access is limited to officially assigned uni
  name: CU Data Gateway
  slug: data-gateway
- baseURL: https://account.it.chula.ac.th/
  baseurl_source: declared
  description: Degree programs and fields of study
  name: Chulalongkorn University Curriculum API
  slug: chulalongkorn-curriculum-api
- baseURL: https://account.it.chula.ac.th/
  baseurl_source: declared
  description: Service metadata
  name: Chulalongkorn University Meta API
  slug: chulalongkorn-meta-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The About API from Chulalongkorn University — 1 operation(s) for about.
  name: Chulalongkorn University About API
  slug: chulalongkorn-about-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The admin API from Chulalongkorn University — 11 operation(s) for admin.
  name: Chulalongkorn University Admin API
  slug: chulalongkorn-admin-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The ChulaSSO Service API from Chulalongkorn University — 1 operation(s) for chulasso service.
  name: Chulalongkorn University ChulaSSO Service API
  slug: chulalongkorn-chulasso-service-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The Html API from Chulalongkorn University — 1 operation(s) for html.
  name: Chulalongkorn University Html API
  slug: chulalongkorn-html-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The Login API from Chulalongkorn University — 1 operation(s) for login.
  name: Chulalongkorn University Login API
  slug: chulalongkorn-login-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The Logout API from Chulalongkorn University — 1 operation(s) for logout.
  name: Chulalongkorn University Logout API
  slug: chulalongkorn-logout-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The myapps API from Chulalongkorn University — 3 operation(s) for myapps.
  name: Chulalongkorn University Myapps API
  slug: chulalongkorn-myapps-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The qr API from Chulalongkorn University — 1 operation(s) for qr.
  name: Chulalongkorn University Qr API
  slug: chulalongkorn-qr-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The QrValidation API from Chulalongkorn University — 1 operation(s) for qrvalidation.
  name: Chulalongkorn University Qr Validation API
  slug: chulalongkorn-qrvalidation-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The ServiceValidation API from Chulalongkorn University — 1 operation(s) for servicevalidation.
  name: Chulalongkorn University Service Validation API
  slug: chulalongkorn-servicevalidation-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The tickets API from Chulalongkorn University — 2 operation(s) for tickets.
  name: Chulalongkorn University Tickets API
  slug: chulalongkorn-tickets-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The users API from Chulalongkorn University — 4 operation(s) for users.
  name: Chulalongkorn University Users API
  slug: chulalongkorn-users-api
- baseURL: https://digital.car.chula.ac.th/do/oai/
  baseurl_source: declared
  description: The 2 FA API from Chulalongkorn University — 5 operation(s) for 2 fa.
  name: Chulalongkorn University 2 FA API
  slug: chulalongkorn-2-fa-api
artifact_total: 34
common:
- group: company
  title: ''
  type: Website
  url: https://www.chula.ac.th/en/
- group: docs
  title: ''
  type: APIReference
  url: https://account.it.chula.ac.th/wiki/doku.php?id=how_does_it_work
- group: docs
  title: ''
  type: Documentation
  url: https://account.it.chula.ac.th/wiki/doku.php
- group: learn
  title: ''
  type: CourseCatalog
  url: https://cas.reg.chula.ac.th/class/course-schedule
- group: other
  title: ''
  type: ResearchRepository
  url: https://digiverse.chula.ac.th/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.car.chula.ac.th/
- group: other
  href: https://artifacts.apis.io/chulalongkorn/identity-federation/chulalongkorn-identity-federation.yml
  title: ''
  type: IdentityFederation
  url: identity-federation/chulalongkorn-identity-federation.yml
- group: design
  href: https://artifacts.apis.io/chulalongkorn/conformance/chulalongkorn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chulalongkorn-conformance.yml
- group: auth
  href: https://artifacts.apis.io/chulalongkorn/authentication/chulalongkorn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chulalongkorn-authentication.yml
- group: other
  title: ''
  type: AIPolicy
  url: https://www.chula.ac.th/en/news/125190/
- group: build
  title: ''
  type: AITooling
  url: https://genie.chula.ac.th/
- group: operate
  title: ''
  type: Support
  url: https://portal.it.chula.ac.th/home
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ChulalongkornUniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/chulalongkorn-university/
- group: auth
  href: https://artifacts.apis.io/chulalongkorn/security/chulalongkorn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chulalongkorn-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/chulalongkorn/plans/chulalongkorn-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chulalongkorn-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/chulalongkorn/rate-limits/chulalongkorn-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chulalongkorn-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chulalongkorn/finops/chulalongkorn-finops.yml
  title: ''
  type: FinOps
  url: finops/chulalongkorn-finops.yml
- group: other
  href: https://artifacts.apis.io/chulalongkorn/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Chulalongkorn University is Thailand''s oldest public research university, founded in 1917 in Bangkok. Its programmable footprint is small, real, and almost entirely undeclared: there is no developer portal, no open data portal, no published specification of any kind, and no self-service registration anywhere in the estate. What it does operate are two genuine institution-run surfaces. Chula SSO at account.it.chula.ac.th has been in production since January 2017 and is documented endpoint-by-endpoint on a public wiki — a modified CAS 1.0 protocol with an added application-authentication step, backed by the university LDAP directory, with keys issued by email rather than by a console. The Office of the Registrar''s CU-REG Course Schedule application answers unauthenticated JSON at cas.reg.chula.ac.th/class/api for its curriculum register and build version, though the thirteen further endpoints its own client declares return 404 from outside the campus network. Everything else
  that looks like a Chulalongkorn API belongs to somebody else: Chula Digital Collections, which serves the university''s only working OAI-PMH endpoint, is a bepress Digital Commons tenancy (digital.car.chula.ac.th is a CNAME to dcchula.bepress.com, adminEmail dc-support@elsevier.com); federated login is a Microsoft Entra ID tenant; DOIs are registered through DataCite and, faculty by faculty, through eleven separate Crossref member records. The institution''s own DigiVerse repository publishes no machine-readable interface at all, and the previously recorded claim that it is a DSpace deployment exposing DSpace REST and OAI-PMH does not survive probing. The central data exchange, CU Data Gateway, is restricted to assigned university personnel and unreachable from outside the campus network.'
examples:
- key_count: 2
  name: Chulalongkorn Course Studies Example
  slug: chulalongkorn-course-studies-example
- key_count: 3
  name: Chulalongkorn Sso Servicevalidation Example
  slug: chulalongkorn-sso-servicevalidation-example
finops:
- has_sources: true
  method: generated
  name: Chulalongkorn Finops
  primary_unit: ''
  service_category: Education
  slug: chulalongkorn-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chulalongkorn.png
json_schemas:
- name: CU-REG Course Study (Degree Program)
  property_count: 34
  slug: chulalongkorn-course-study
- name: Chula SSO Authenticated User
  property_count: 6
  slug: chulalongkorn-sso-user
jsonld:
- class_count: 12
  name: Chulalongkorn Context
  property_count: 6
  slug: chulalongkorn-context
layout: provider
modified: '2026-09-01'
name: Chulalongkorn University
nav: Providers
network: true
overview: 'Chulalongkorn University publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Curriculum API, Meta API, About API, and 20 more. Tagged areas include Education, Higher Education, University, Research, and Thailand.


  The Chulalongkorn University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chulalongkorn University''s developer surface includes API reference, documentation, authentication, support, GitHub presence, and 14 more developer resources.'
plans:
- name: Chulalongkorn Plans Pricing
  plan_count: 2
  slug: chulalongkorn-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Chulalongkorn Rate Limits
  slug: chulalongkorn-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Chulalongkorn University API Rules
  rule_count: 46
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 6
  slug: chulalongkorn-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 58.5
    catalog_earned_first_party: 10.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 54.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - thailand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 28.1
  provenance:
    conformance: first-party
    contracts:
      callable: 31.6
      derived: 4
      marker_coverage: 100.0
      total: 19
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/chulalongkorn/chulalongkorn-2026-06-20T174339.png
security:
- kind: authentication
  name: Chulalongkorn Authentication
  slug: chulalongkorn-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Chulalongkorn Domain Security
  slug: chulalongkorn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chulalongkorn
tags:
- Education
- Higher Education
- University
- Research
- Thailand
- Bangkok
- Identity Federation
- SSO
- Course Catalog
- Research Repository
- Library
- Open Access
- OAI-PMH
website: https://www.chula.ac.th/en/
---
