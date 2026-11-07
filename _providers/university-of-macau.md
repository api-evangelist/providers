---
access_model:
  confidence: high
  label: Free, but closed to the public — a UMPASS account is required for a key
  onboarding: unknown
  pricing: free
  public: false
  source:
  - https://data.um.edu.mo/quickstart
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: UMPASS, the university's single sign-on, is served by UM's own AD FS farm. It publishes federation metadata as application/samlmetadata+xml — 71 KB, signed, carrying both an IDPSSODescriptor and an SP
  name: UM Web SSO — institutional SAML 2.0 / OpenID Connect identity provider
  slug: websso-idp
- description: 'The identity broker in front of UM''s own IdP. Sign-in to data.um.edu.mo, UMMoodle and the GenAI chat starts at a Microsoft sign-in page and is redirected to websso.um.edu.mo, so the Entra tenant is a '
  name: Microsoft Entra ID tenant federation for um.edu.mo
  slug: entra-federation
- description: The University of Macau's Moodle learning management system publishes a live LTI 1.3 Advantage platform key set at /mod/lti/certs.php (200, application/json, RSA RS256 signing key), an OAuth 2.0 clien
  name: UMMoodle — LTI 1.3 Advantage platform
  slug: ummoodle-lti
- description: The University of Macau Library's catalog and discovery layer is an Ex Libris Primo VE tenancy. UM's institution code is 853UOM_INST and its view is umlibrary. No UM-operated library API exists; any P
  name: UM Library discovery — Ex Libris Primo VE tenancy
  slug: primo-discovery
- description: '澳門大學學者庫, the University of Macau''s institutional repository and scholar profile system, indexing faculties and institutes, scholars, publications and subjects. It is not harvestable: /oai and /oai/req'
  name: UM Scholars Hub — institutional repository
  slug: scholars-hub
- description: The university's own generative-AI chat service for staff and students, an Open WebUI deployment authenticated by OIDC against UMPASS, with self-signup and the local login form disabled. Its unauthent
  name: UM GENAI Chat — Open WebUI deployment
  slug: genai-chat
- description: The University of Macau is Crossref member 53643, with DOI prefix 10.64219 and 21 DOIs registered as of 2026-09-01. This is a fact about the institution and one of the education regime's named standar
  name: Crossref membership — University of Macau
  slug: crossref-member
- description: Research Organization Registry identifier for the University of Macau, carrying its English, Portuguese and historical names (Universidade de Macau, University of East Asia) and its cross-references t
  name: ROR identifier — University of Macau
  slug: ror
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes online door access records.
  name: University of Macau Access Control Records API
  slug: university-of-macau-access-control-records-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes the total number of available parking spaces for the car park according to the vehicle type or parking type.
  name: University of Macau Car Park Availability API
  slug: university-of-macau-car-park-availability-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes the locations and availability status of computer room PCs at the University of Macau. It details the PC name, locations and availability.
  name: University of Macau Computer Room PC Status API
  slug: university-of-macau-computer-room-pc-status-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes latest information of computer room locations and reservations records.
  name: University of Macau Computer Room Reservations API
  slug: university-of-macau-computer-room-reservations-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes all course information of current academic year.
  name: University of Macau Course Catalog API
  slug: university-of-macau-course-catalog-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes courses and their corresponding sections. For each section, two JSON Array of objects detail the schedule and instructor arrangements.
  name: University of Macau Courses API
  slug: university-of-macau-courses-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes events data of the University of Macau.
  name: University of Macau Events API
  slug: university-of-macau-events-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes news data published by the University of Macau.
  name: University of Macau News API
  slug: university-of-macau-news-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: 'This data set includes current units and sub-units information of the University of Macau in three languages: Chinese, English and Portuguese.'
  name: University of Macau Organizational Units API
  slug: university-of-macau-organizational-units-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes the date of the public holidays of the University of Macau.
  name: University of Macau Public Holidays API
  slug: university-of-macau-public-holidays-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes current information of bed spaces in residential college excluded PGH. No historical records, and bed name is pre-generated for the whole year ahead.
  name: University of Macau RC Hostel Bed Spaces API
  slug: university-of-macau-rc-hostel-bed-spaces-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes the bus arrival time records and station information.
  name: University of Macau Shuttle Bus Arrival Time API
  slug: university-of-macau-shuttle-bus-arrival-time-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes current sports facilities on the University of Macau campus.
  name: University of Macau Sports Facilities API
  slug: university-of-macau-sports-facilities-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes booking information about current sports facilities on the University of Macau campus.
  name: University of Macau Sports Facilities Booking API
  slug: university-of-macau-sports-facilities-booking-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes information of job vacancy advertisement posted in Job Vacancy E-system for student.
  name: University of Macau Student Job Vacancies API
  slug: university-of-macau-student-job-vacancies-api
- baseURL: https://api.data.um.edu.mo
  baseurl_source: declared
  description: This data set includes WiFi access logs from outdoor wireless access points.
  name: University of Macau Wifi Access Log API
  slug: university-of-macau-wifi-access-log-api
artifact_total: 32
common:
- group: company
  title: ''
  type: Blog
  url: https://www.um.edu.mo/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.um.edu.mo/feed/
- group: company
  title: ''
  type: Website
  url: https://www.um.edu.mo/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.um.edu.mo/
- group: other
  title: ''
  type: OpenData
  url: https://data.um.edu.mo/dataset
- group: docs
  title: ''
  type: Documentation
  url: https://data.um.edu.mo/api-documents/api-operations
- group: docs
  title: ''
  type: APIReference
  url: https://data.um.edu.mo/data-dictionary
- group: docs
  href: https://artifacts.apis.io/university-of-macau/openapi/university-of-macau-open-data-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/university-of-macau-open-data-api-openapi.yml
- group: learn
  title: ''
  type: CourseCatalog
  url: https://data.um.edu.mo/data-dictionary
- group: other
  title: ''
  type: IdentityFederation
  url: https://websso.um.edu.mo/FederationMetadata/2007-06/FederationMetadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.um.edu.mo/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://umlibrary.primo.exlibrisgroup.com/discovery/search?vid=853UOM_INST:umlibrary
- group: other
  title: ''
  type: AIPolicy
  url: https://genai.um.edu.mo/
- group: build
  title: ''
  type: AITooling
  url: https://chat.genai.um.edu.mo/
- group: auth
  href: https://artifacts.apis.io/university-of-macau/authentication/university-of-macau-authentication.yml
  title: ''
  type: Authentication
  url: authentication/university-of-macau-authentication.yml
- group: design
  href: https://artifacts.apis.io/university-of-macau/conformance/university-of-macau-conformance.yml
  title: ''
  type: Conformance
  url: conformance/university-of-macau-conformance.yml
- group: design
  href: https://artifacts.apis.io/university-of-macau/errors/university-of-macau-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/university-of-macau-problem-types.yml
- group: design
  href: https://artifacts.apis.io/university-of-macau/lifecycle/university-of-macau-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-macau-lifecycle.yml
- group: start
  title: ''
  type: SignUp
  url: https://data.um.edu.mo/quickstart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.um.edu.mo/terms-and-conditions-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.um.edu.mo/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://data.um.edu.mo/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universityofmacau/
- group: auth
  href: https://artifacts.apis.io/university-of-macau/security/university-of-macau-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-macau-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/university-of-macau/plans/university-of-macau-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/university-of-macau-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/university-of-macau/rate-limits/university-of-macau-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/university-of-macau-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/university-of-macau/finops/university-of-macau-finops.yml
  title: ''
  type: FinOps
  url: finops/university-of-macau-finops.yml
- group: other
  href: https://artifacts.apis.io/university-of-macau/review.yml
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'The University of Macau operates a genuine institution-owned API platform and documents it unusually well, but no part of it can be called without a UMPASS account, which is issued only to UM staff and students. Every one of the sixteen APIs on api.data.um.edu.mo answers an unauthenticated request with 401 and an Azure API Management key challenge; the single published product, "UM Members", cannot be subscribed to from outside the institution. The surface itself is fully readable — the developer portal''s own backend at /developer/apis?api-version=2022-04-01-preview is anonymously readable and yielded the complete API list, every operation, and every documented query parameter, which is how the OpenAPI in this repository was reconstructed — so this is coverage limited by credentials, not by obscurity. UM publishes no OpenAPI of its own (the portal''s export returns paths: {}), no llms.txt, no apis.json, no /.well-known/api-catalog and no security.txt. Two further institution-operated
    machine-readable surfaces are fully open and are recorded here: the SAML 2.0 federation metadata and OIDC discovery for UM''s own AD FS identity provider, and the LTI 1.3 key set on UMMoodle. What UM does not have is a research-output surface — no OAI-PMH provider exists on any um.edu.mo host, the institutional repository blocks harvesting by IP, and there is no DataCite account. No official University of Macau GitHub organization exists; github.com/university-of-macau and github.com/umacau are both empty registrations with zero public repositories and no profile, and neither is claimed here.'
  evidence:
  - status: 401
    url: https://api.data.um.edu.mo/service/media/events/all
  - status: 200
    url: https://data.um.edu.mo/developer/apis?api-version=2022-04-01-preview
  - status: 200
    url: https://data.um.edu.mo/
  - status: 200
    url: https://data.um.edu.mo/api-documents/api-operations
  - status: 200
    url: https://data.um.edu.mo/quickstart
  - status: 200
    url: https://data.um.edu.mo/dataset
  - status: 200
    url: https://data.um.edu.mo/data-dictionary
  - status: 200
    url: https://websso.um.edu.mo/FederationMetadata/2007-06/FederationMetadata.xml
  - status: 200
    url: https://websso.um.edu.mo/adfs/.well-known/openid-configuration
  - status: 200
    url: https://login.microsoftonline.com/um.edu.mo/v2.0/.well-known/openid-configuration
  - status: 200
    url: https://ummoodle.um.edu.mo/mod/lti/certs.php
  - status: 404
    url: https://repository.um.edu.mo/oai?verb=Identify
  - note: 200 body reads "Your IP is not allowed to access or harvest this resources!"
    status: 200
    url: https://repository.um.edu.mo/api/core/sites
  - status: 200
    url: https://umlibrary.primo.exlibrisgroup.com/discovery/search?vid=853UOM_INST:umlibrary
  - status: 200
    url: https://chat.genai.um.edu.mo/api/config
  - status: 200
    url: https://genai.um.edu.mo/
  - status: 200
    url: https://api.crossref.org/members/53643
  - status: 200
    url: https://ror.org/01r4q9n85
  - note: empty data array — no DataCite account
    status: 200
    url: https://api.datacite.org/clients?query=Macau
  - status: 404
    url: https://data.um.edu.mo/llms.txt
  - status: 404
    url: https://data.um.edu.mo/.well-known/api-catalog
  - status: 404
    url: https://www.um.edu.mo/.well-known/security.txt
  reason: auth-required
  state: gated
created: '2026-06-03'
description: 'The University of Macau (UM), founded in 1981, is the public comprehensive research university of the Macao Special Administrative Region, teaching mainly in English with a largely international faculty and a residential-college undergraduate model. Its programmable footprint is real but narrow, and it is almost entirely campus operations rather than research output. The Information and Communication Technology Office (ICTO) operates a Data and Open Data API Platform at data.um.edu.mo whose gateway, api.data.um.edu.mo, serves sixteen JSON APIs across nineteen operations: organizational units and public holidays, the course catalog and per-semester course offerings, car park availability, computer room PC status and reservations, shuttle bus arrival times, sports facilities and their bookings, door access control records, outdoor WiFi access logs, university news and events, residential college hostel bed spaces and student job vacancies. The platform documents pagination, filtering,
  sorting and a full response-code table with remediation guidance — better documentation discipline than most universities manage. It publishes no OpenAPI, however, and it is not callable by the public: every API requires a subscription key issued only to holders of a UMPASS account, which means UM staff and students. Two further institution-run surfaces are machine-readable and were missed by earlier profiling: UM''s own AD FS identity provider at websso.um.edu.mo publishes signed SAML 2.0 metadata and an OpenID Connect discovery document, and its Moodle deployment publishes a live LTI 1.3 Advantage platform key set. Everything else that looks like a UM API belongs to somebody else — library discovery is an Ex Libris Primo VE tenancy, the UM Scholars Hub repository runs third-party institutional-repository software behind an IP allowlist with no OAI-PMH, and the university''s GenAI chat is an Open WebUI deployment with API keys switched off. UM registers DOIs as a Crossref member and is
  identified in ROR; it holds no DataCite account.'
finops:
- has_sources: true
  method: derived
  name: University Of Macau Finops
  primary_unit: ''
  service_category: ''
  slug: university-of-macau-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-macau.png
json_schemas:
- name: University of Macau Data and Open Data API — schemas
  property_count: 0
  slug: university-of-macau-open-data-schemas
jsonld:
- class_count: 21
  name: University Of Macau Context
  property_count: 5
  slug: university-of-macau-context
layout: provider
modified: '2026-10-06'
name: University of Macau
nav: Providers
network: true
overview: 'University of Macau publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Control Records API, Car Park Availability API, Computer Room PC Status API, and 21 more. Tagged areas include University, Higher Education, Education, Public Research University, and Macau.


  The University of Macau catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Macau''s developer surface includes engineering blog, documentation, API reference, authentication, signup flow, support, and 22 more developer resources.'
plans:
- name: University Of Macau Plans Pricing
  plan_count: 1
  slug: university-of-macau-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: University Of Macau Rate Limits
  slug: university-of-macau-rate-limits
rules:
- authorship: generated
  effective_rule_count: 15
  extends: []
  name: University of Macau — openapi rules
  rule_count: 15
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 9
  slug: university-of-macau-openapi-spectral-rules
score:
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.2
    catalog_earned_first_party: 16.0
    catalog_gap: 49.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 29.5
    contract_quality: 62.3
    developer_ergonomics: 57.1
    discoverability: 57.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 50.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/university-of-macau/university-of-macau-2026-06-20T200211.png
security:
- kind: authentication
  name: University Of Macau Authentication
  slug: university-of-macau-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: University Of Macau Domain Security
  slug: university-of-macau-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-macau
tags:
- University
- Higher Education
- Education
- Public Research University
- Macau
- China
- Open Data
- Course Catalog
- Campus Life
- Identity Federation
- Research Repository
- Library
website: https://www.um.edu.mo/
---
