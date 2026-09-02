---
access_model:
  confidence: high
  label: Affiliation-gated
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ucla Agentic Access
  operation_count: 91
  slug: ucla-agentic-access
  summary_line: 91 operations
api_count: 7
apis:
- description: UCLA's own Shibboleth identity provider and the most complete machine-readable artifact the university publishes. Registered by InCommon under entityID urn:mace:incommon:ucla.edu, signed with RSA-SHA2
  name: UCLA Shibboleth Identity Provider (InCommon)
  slug: identity
- description: UCLA Library self-hosts a Cantaloupe 5.0.5 image server exposing both IIIF Image API 2.x and 3.0 endpoints for its digital collections. Institution-operated on UCLA's own AWS infrastructure under a UC
  name: UCLA Library IIIF Image Service
  slug: library-iiif
- description: UCLA Library's digital collections platform, institution-hosted on a UCLA IP under a UCLA-issued certificate and developed in the open by the UCLA Library engineering organisation. Recorded as a relat
  name: UCLA Library Digital Collections
  slug: digital-collections
- description: UCLA's research data repository, running open-source Dataverse on a UCLA-owned host under a UCLA-issued certificate with no vendor CNAME - which distinguishes it from the Figshare and Elsevier Pure te
  name: UCLA Dataverse
  slug: dataverse
- description: UCLA's learning management system. The brand, the courses, the learners and the subdomain are UCLA's; the REST API, the LTI 1.3 implementation, the key rotation and the contract are Instructure's, and
  name: BruinLearn (Canvas LMS)
  slug: bruinlearn
- description: The Class Sections API from University of California, Los Angeles — 2 operation(s) for class sections.
  name: University of California, Los Angeles Class Sections API
  slug: ucla-class-sections-api
- description: The Classes API from University of California, Los Angeles — 4 operation(s) for classes.
  name: University of California, Los Angeles Classes API
  slug: ucla-classes-api
- description: The Courses API from University of California, Los Angeles — 5 operation(s) for courses.
  name: University of California, Los Angeles Courses API
  slug: ucla-courses-api
- description: The Dictionary API from University of California, Los Angeles — 61 operation(s) for dictionary.
  name: University of California, Los Angeles Dictionary API
  slug: ucla-dictionary-api
- description: The GE Foundations API from University of California, Los Angeles — 2 operation(s) for ge foundations.
  name: University of California, Los Angeles GE Foundations API
  slug: ucla-ge-foundations-api
- description: The Infrastructure API from University of California, Los Angeles — 1 operation(s) for infrastructure.
  name: University of California, Los Angeles Infrastructure API
  slug: ucla-infrastructure-api
- description: The MyUCLA API from University of California, Los Angeles — 1 operation(s) for myucla.
  name: University of California, Los Angeles My UCLA API
  slug: ucla-myucla-api
- description: The Production Calendar Jobs API from University of California, Los Angeles — 1 operation(s) for production calendar jobs.
  name: University of California, Los Angeles Production Calendar Jobs API
  slug: ucla-production-calendar-jobs-api
- description: The Weather API from University of California, Los Angeles — 14 operation(s) for weather.
  name: University of California, Los Angeles Weather API
  slug: ucla-weather-api
artifact_total: 32
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ucla-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucla.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.api.ucla.edu/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.api.ucla.edu/api-catalog
- group: docs
  title: ''
  type: Documentation
  url: https://developer.api.ucla.edu/ucla-help
- group: operate
  title: ''
  type: Support
  url: https://developer.api.ucla.edu/ucla-help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ucla.edu/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://compliance.ucla.edu/privacy
- group: other
  title: ''
  type: Accessibility
  url: https://www.ucla.edu/accessibility
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ucla
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UCLALibrary
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ucla/
- group: company
  title: ''
  type: Blog
  url: https://newsroom.ucla.edu/
- group: company
  title: ''
  type: BlogRSS
  url: https://newsroom.ucla.edu/rss.xml
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Aucla.edu
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.registrar.ucla.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.library.ucla.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://dataverse.ucla.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://oarc.ucla.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://dts.ucla.edu/initiatives/ai/ai-use-policy-guide
- group: build
  title: ''
  type: AITooling
  url: https://dts.ucla.edu/initiatives/ai/guiding-principles-responsible-use
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/ucla-sis-dictionary-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ucla-sis-dictionary-schemas.json
- group: build
  title: ''
  type: Examples
  url: examples/index.yml
- group: design
  title: ''
  type: Rules
  url: rules/ucla-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ucla-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ucla-context.jsonld
- group: auth
  title: ''
  type: Authentication
  url: authentication/ucla-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/ucla-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/ucla-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ucla-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ucla-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ucla-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucla-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ucla-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucla-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucla-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: UCLA is the strongest institution-operated API program measured in this cohort so far and it is still not consumable. Seven real OpenAPI contracts covering 91 operations are anonymously downloadable from the developer portal, and every route they describe is live on UCLA's own Apigee gateway - a documented SIS path returns 401 with oauth.v2.InvalidAccessToken and a conformant RFC 6750 Bearer challenge, which proves the contracts describe real endpoints. But a credential exists only after a developer signs in with a UCLA logon, creates an App, selects an API Product and a campus unit approves the request. There is no public registration, no sandbox, no trial key. The portal states plainly that most APIs are only visible after log on, so the eight catalogued products are a subset of an unknown whole. Two secondary limits are recorded rather than treated as findings about UCLA - dataverse.ucla.edu and digital.library.ucla.edu both answer 200 with an Anubis proof-of-work bot challenge
    on every path, so OAI-PMH, Dataverse version and DOI prefix could not be read and are not claimed; and UCLA Library's Cantaloupe IIIF server answers 403 with a stack trace for every identifier including a deliberate nonsense control, so no manifest could be retrieved. This is a correct gated profile, not a failed probe - roughly 60 URLs were fetched successfully across 15 hosts, including 7 contracts, signed federation metadata and 3 live error surfaces.
  evidence:
  - note: Eight API products listed; three of them (51, 346, 1446) were absent from the June profile.
    status: 200
    url: https://developer.api.ucla.edu/api-catalog
  - status: 200
    url: https://developer.api.ucla.edu/sites/default/files/apidoc_specs/classes_v1_4.json
  - status: 200
    url: https://developer.api.ucla.edu/sites/default/files/apidoc_specs/courses_v1%20%281%29_0.json
  - status: 200
    url: https://developer.api.ucla.edu/sites/default/files/apidoc_specs/dictionary_v1%20%281%29.json
  - status: 200
    url: https://developer.api.ucla.edu/sites/default/files/apidoc_specs/productioncalendarjobs_v1_0.json
  - status: 200
    url: https://developer.api.ucla.edu/sites/default/files/apidoc_specs/_infrastructure_verifyconnectivity_v1.json
  - status: 200
    url: https://developer.api.ucla.edu/sites/default/files/apidoc_specs/_myucla_menudata_v1.json
  - status: 200
    url: https://developer.api.ucla.edu/sites/default/files/apidoc_specs/UCLAWeather_3.yaml
  - note: oauth.v2.InvalidAccessToken with an RFC 6750 Bearer challenge; the gateway is live and enforcing.
    status: 401
    url: https://api.ucla.edu/sis/dictionary/buildings/v1
  - status: 401
    url: https://api.ucla.edu/weather/api
  - status: 200
    url: https://api.ucla.edu/oauth/client_credential/accesstoken
  - note: Plain-text "Unauthorized by UCLA API Gateway. Invalid Config Data" on every unrouted path; should be 404.
    status: 500
    url: https://api.ucla.edu/nonexistentpath
  - note: QA returns a structured ApplicationNotFound fault where production returns a 500.
    status: 404
    url: https://qa.api.ucla.edu/
  - note: Signed SAML metadata for UCLA's own Shibboleth IdP; REFEDS R&S and SIRTFI.
    status: 200
    url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Aucla.edu
  - status: 200
    url: https://met.refeds.org/met/entity/urn:mace:incommon:ucla.edu/
  - note: Tenant surface — Instructure Canvas on a UCLA vanity subdomain.
    status: 200
    url: https://bruinlearn.ucla.edu/api/lti/security/jwks
  - status: 401
    url: https://bruinlearn.ucla.edu/api/v1/accounts
  - note: Anubis bot-challenge body, not a Dataverse response; unreadable, not credited.
    status: 200
    url: https://dataverse.ucla.edu/api/info/version
  - note: Anubis bot-challenge body; OAI-PMH conformance neither confirmed nor denied.
    status: 200
    url: https://dataverse.ucla.edu/oai?verb=Identify
  - note: Anubis bot-challenge body; not credited.
    status: 200
    url: https://digital.library.ucla.edu/catalog/oai?verb=Identify
  - note: Cantaloupe 5.0.5 landing page; IIIF Image API 2.x and 3.0 endpoints advertised.
    status: 200
    url: https://iiif.library.ucla.edu/
  - note: Negative control. Identical stack-trace body to a plausible real identifier, so a 403 here is never evidence an object exists. Also leaks the private S3 bucket name.
    status: 403
    url: https://iiif.library.ucla.edu/iiif/2/bogus-identifier/info.json
  - status: 500
    url: https://api.ucla.edu/
  - note: Does not resolve; UCLA operates no open-data portal at the conventional hostname.
    status: 0
    url: https://data.ucla.edu/
  - note: Pilot portal recorded in the June 2026 profile still does not resolve from outside campus.
    status: 0
    url: https://developer-pilot.api.ucla.edu/
  - note: Referenced by info.description in UCLA's own Weather contract. Resolves in DNS but accepts no connection; dead pointer, removed rather than carried.
    status: 0
    url: https://weather.atmos.ucla.edu/
  - status: 404
    url: https://www.ucla.edu/llms.txt
  - status: 404
    url: https://developer.api.ucla.edu/.well-known/security.txt
  - note: UC systemwide repository operated by the California Digital Library. ListSets returns a single set, "everything", with no UCLA-specific set, so nothing here is attributable to UCLA and no entry is recorded for it.
    status: 200
    url: https://escholarship.org/oai?verb=ListSets
  - note: Soft-404 — redirects to the dts.ucla.edu homepage; not claimed as a pointer.
    status: 200
    url: https://it.ucla.edu/privacy
  reason: approval_required_no_self_service
  state: gated
created: '2026-06-03'
description: 'The University of California, Los Angeles is a public land-grant research university in the University of California system, ranked 29th in the QS World University Rankings, and it is one of the few institutions in this cohort that genuinely runs a central API program rather than renting one. UCLA operates its own API gateway at api.ucla.edu, fronted by Apigee under a certificate issued to the university, and a Drupal/Apigee developer portal at developer.api.ucla.edu that catalogues eight API products. Seven of those products publish a real machine-readable contract, anonymously downloadable, and all seven describe routes on UCLA''s own gateway - six Swagger 2.0 contracts covering the student information system (classes, class sections, courses, GE foundations, a 61-operation Registrar data dictionary, the mainframe production calendar, a connectivity health check and the MyUCLA portal menu) plus one OpenAPI 3.0.3 contract for a campus weather station. Ninety-one operations
  in total, every one of them a read. UCLA also runs its own Shibboleth identity provider, registered by InCommon under entityID urn:mace:incommon:ucla.edu with REFEDS Research & Scholarship and SIRTFI certification - the most complete machine-readable artifact the university publishes, and the one no API catalogue had looked at. UCLA Library self-hosts a Cantaloupe IIIF image server, a Hyrax digital collections platform and a Dataverse instance, all on ucla.edu hosts under UCLA''s own TLS certificates. What UCLA does not have is any way in: every credential requires a UCLA logon and a human approval, there is no self-service path, no status page, no changelog, no llms.txt, no machine-readable catalog index, and no rate-limit or error documentation. The learning management system, BruinLearn, is Instructure Canvas on a vanity subdomain and is recorded as a tenant relationship rather than as UCLA engineering.'
examples:
- key_count: 1
  name: Ucla Apigee Invalid Token Error
  slug: ucla-apigee-invalid-token-error
- key_count: 1
  name: Ucla Bruinlearn Lti Jwks
  slug: ucla-bruinlearn-lti-jwks
finops:
- name: Ucla Finops
  service_category: Education
  slug: ucla-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucla.png
json_schemas:
- name: UCLA myUCLA menu data — schemas in use
  property_count: 0
  slug: ucla-myucla-menu-data-schemas
- name: UCLA sis classes — schemas in use
  property_count: 0
  slug: ucla-sis-classes-schemas
- name: UCLA sis courses — schemas in use
  property_count: 0
  slug: ucla-sis-courses-schemas
- name: UCLA sis dictionary — schemas in use
  property_count: 0
  slug: ucla-sis-dictionary-schemas
- name: UCLA sis production calendar jobs — schemas in use
  property_count: 0
  slug: ucla-sis-production-calendar-jobs-schemas
- name: UCLA sis verify connectivity — schemas in use
  property_count: 0
  slug: ucla-sis-verify-connectivity-schemas
- name: UCLA weather — schemas in use
  property_count: 0
  slug: ucla-weather-schemas
jsonld:
- class_count: 31
  name: Ucla Context
  property_count: 4
  slug: ucla-context
layout: provider
modified: '2026-08-19'
name: University of California, Los Angeles
nav: Providers
network: true
overview: 'University of California, Los Angeles publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Class Sections API, Classes API, Courses API, and 6 more. Tagged areas include University, Higher Education, Education, United States, and California.


  The University of California, Los Angeles catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of California, Los Angeles'' developer surface includes API reference, documentation, support, GitHub presence, engineering blog, code examples, authentication, and 31 more developer resources.'
plans:
- name: Ucla Plans Pricing
  plan_count: 2
  slug: ucla-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Ucla Rate Limits
  slug: ucla-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: University of California, Los Angeles API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: ucla-rules
scopes:
- name: Ucla Scopes
  scope_count: 0
  slug: ucla-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 36.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 3.8
    contract_quality: 60.7
    developer_ergonomics: 45.2
    discoverability: 74.1
    governance: 3.8
    operational_transparency: 23.7
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucla/refs/heads/main/screenshots/ucla-2026-06-20T195941.png
security:
- kind: authentication
  name: Ucla Authentication
  slug: ucla-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Ucla Domain Security
  slug: ucla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ucla
tags:
- University
- Higher Education
- Education
- United States
- California
- UC System
- Public Research University
- Course Catalog
- Student Information
- Identity Federation
- Research Repository
- Library
- IIIF
- Campus Life
website: https://www.ucla.edu/
---
