---
access_model:
  confidence: high
  label: Free · No signup, no developer portal
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  - authentication
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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: KFUPM runs an Elsevier Pure research information system at pure.kfupm.edu.sa and its Pure Web Services REST API is reachable at /ws/api, authenticated with a Pure api-key header. The deployment, the t
  name: KFUPM Elsevier Pure Web Services (tenant deployment)
  slug: pure-tenant
- baseURL: https://sts.kfupm.edu.sa
  baseurl_source: declared
  description: Unauthenticated metadata endpoints. All three fetched live 2026-08-30.
  name: King Fahd University of Petroleum & Minerals Discovery API
  slug: kfupm-discovery-api
- baseURL: https://sts.kfupm.edu.sa
  baseurl_source: declared
  description: Record-level export in a named format.
  name: King Fahd University of Petroleum & Minerals Export API
  slug: kfupm-export-api
- baseURL: https://eprints.kfupm.edu.sa/cgi/oai2
  baseurl_source: declared
  description: OAI-PMH 2.0 protocol requests. All six verbs verified live 2026-08-30.
  name: King Fahd University of Petroleum & Minerals Oai Pmh API
  slug: kfupm-oai-pmh-api
- baseURL: https://sts.kfupm.edu.sa
  baseurl_source: declared
  description: Free-text search with a machine-readable output format.
  name: King Fahd University of Petroleum & Minerals Search API
  slug: kfupm-search-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: OAuth 2.0 / OpenID Connect endpoints as declared by KFUPM's own discovery document.
  name: King Fahd University of Petroleum & Minerals Oauth2 API
  slug: kfupm-oauth2-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The activity API from King Fahd University of Petroleum & Minerals — 39 operation(s) for activity.
  name: King Fahd University of Petroleum & Minerals Activity API
  slug: kfupm-activity-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The application API from King Fahd University of Petroleum & Minerals — 36 operation(s) for application.
  name: King Fahd University of Petroleum & Minerals Application API
  slug: kfupm-application-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The authorCollaboration API from King Fahd University of Petroleum & Minerals — 9 operation(s) for authorcollaboration.
  name: King Fahd University of Petroleum & Minerals Author Collaboration API
  slug: kfupm-authorcollaboration-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The award API from King Fahd University of Petroleum & Minerals — 37 operation(s) for award.
  name: King Fahd University of Petroleum & Minerals Award API
  slug: kfupm-award-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The classificationScheme API from King Fahd University of Petroleum & Minerals — 7 operation(s) for classificationscheme.
  name: King Fahd University of Petroleum & Minerals Classification Scheme API
  slug: kfupm-classificationscheme-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The concept API from King Fahd University of Petroleum & Minerals — 4 operation(s) for concept.
  name: King Fahd University of Petroleum & Minerals Concept API
  slug: kfupm-concept-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The conferenceSeries API from King Fahd University of Petroleum & Minerals — 14 operation(s) for conferenceseries.
  name: King Fahd University of Petroleum & Minerals Conference Series API
  slug: kfupm-conferenceseries-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The contract API from King Fahd University of Petroleum & Minerals — 27 operation(s) for contract.
  name: King Fahd University of Petroleum & Minerals Contract API
  slug: kfupm-contract-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The course API from King Fahd University of Petroleum & Minerals — 27 operation(s) for course.
  name: King Fahd University of Petroleum & Minerals Course API
  slug: kfupm-course-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The dataSet API from King Fahd University of Petroleum & Minerals — 30 operation(s) for dataset.
  name: King Fahd University of Petroleum & Minerals Data Set API
  slug: kfupm-dataset-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The education API from King Fahd University of Petroleum & Minerals — 14 operation(s) for education.
  name: King Fahd University of Petroleum & Minerals Education API
  slug: kfupm-education-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The equipment API from King Fahd University of Petroleum & Minerals — 28 operation(s) for equipment.
  name: King Fahd University of Petroleum & Minerals Equipment API
  slug: kfupm-equipment-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The ethicalReview API from King Fahd University of Petroleum & Minerals — 22 operation(s) for ethicalreview.
  name: King Fahd University of Petroleum & Minerals Ethical Review API
  slug: kfupm-ethicalreview-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The event API from King Fahd University of Petroleum & Minerals — 22 operation(s) for event.
  name: King Fahd University of Petroleum & Minerals Event API
  slug: kfupm-event-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The externalOrganization API from King Fahd University of Petroleum & Minerals — 29 operation(s) for externalorganization.
  name: King Fahd University of Petroleum & Minerals External Organization API
  slug: kfupm-externalorganization-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The externalPerson API from King Fahd University of Petroleum & Minerals — 22 operation(s) for externalperson.
  name: King Fahd University of Petroleum & Minerals External Person API
  slug: kfupm-externalperson-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The fingerprint API from King Fahd University of Petroleum & Minerals — 3 operation(s) for fingerprint.
  name: King Fahd University of Petroleum & Minerals Fingerprint API
  slug: kfupm-fingerprint-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The fundingOpportunity API from King Fahd University of Petroleum & Minerals — 21 operation(s) for fundingopportunity.
  name: King Fahd University of Petroleum & Minerals Funding Opportunity API
  slug: kfupm-fundingopportunity-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The impact API from King Fahd University of Petroleum & Minerals — 31 operation(s) for impact.
  name: King Fahd University of Petroleum & Minerals Impact API
  slug: kfupm-impact-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The journal API from King Fahd University of Petroleum & Minerals — 22 operation(s) for journal.
  name: King Fahd University of Petroleum & Minerals Journal API
  slug: kfupm-journal-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The keywordGroupConfiguration API from King Fahd University of Petroleum & Minerals — 7 operation(s) for keywordgroupconfiguration.
  name: King Fahd University of Petroleum & Minerals Keyword Group Configuration API
  slug: kfupm-keywordgroupconfiguration-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The milestone API from King Fahd University of Petroleum & Minerals — 24 operation(s) for milestone.
  name: King Fahd University of Petroleum & Minerals Milestone API
  slug: kfupm-milestone-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The organization API from King Fahd University of Petroleum & Minerals — 34 operation(s) for organization.
  name: King Fahd University of Petroleum & Minerals Organization API
  slug: kfupm-organization-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The person API from King Fahd University of Petroleum & Minerals — 58 operation(s) for person.
  name: King Fahd University of Petroleum & Minerals Person API
  slug: kfupm-person-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The personExpertise API from King Fahd University of Petroleum & Minerals — 7 operation(s) for personexpertise.
  name: King Fahd University of Petroleum & Minerals Person Expertise API
  slug: kfupm-personexpertise-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The pressMedia API from King Fahd University of Petroleum & Minerals — 24 operation(s) for pressmedia.
  name: King Fahd University of Petroleum & Minerals Press Media API
  slug: kfupm-pressmedia-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The prize API from King Fahd University of Petroleum & Minerals — 29 operation(s) for prize.
  name: King Fahd University of Petroleum & Minerals Prize API
  slug: kfupm-prize-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The project API from King Fahd University of Petroleum & Minerals — 33 operation(s) for project.
  name: King Fahd University of Petroleum & Minerals Project API
  slug: kfupm-project-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The publisher API from King Fahd University of Petroleum & Minerals — 18 operation(s) for publisher.
  name: King Fahd University of Petroleum & Minerals Publisher API
  slug: kfupm-publisher-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The researchOutput API from King Fahd University of Petroleum & Minerals — 67 operation(s) for researchoutput.
  name: King Fahd University of Petroleum & Minerals Research Output API
  slug: kfupm-researchoutput-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The role API from King Fahd University of Petroleum & Minerals — 2 operation(s) for role.
  name: King Fahd University of Petroleum & Minerals Role API
  slug: kfupm-role-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The semester API from King Fahd University of Petroleum & Minerals — 8 operation(s) for semester.
  name: King Fahd University of Petroleum & Minerals Semester API
  slug: kfupm-semester-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The specialization API from King Fahd University of Petroleum & Minerals — 8 operation(s) for specialization.
  name: King Fahd University of Petroleum & Minerals Specialization API
  slug: kfupm-specialization-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The studentProject API from King Fahd University of Petroleum & Minerals — 26 operation(s) for studentproject.
  name: King Fahd University of Petroleum & Minerals Student Project API
  slug: kfupm-studentproject-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The studentThesis API from King Fahd University of Petroleum & Minerals — 26 operation(s) for studentthesis.
  name: King Fahd University of Petroleum & Minerals Student Thesis API
  slug: kfupm-studentthesis-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The thesaurus API from King Fahd University of Petroleum & Minerals — 5 operation(s) for thesaurus.
  name: King Fahd University of Petroleum & Minerals Thesaurus API
  slug: kfupm-thesaurus-api
- baseURL: https://pure.kfupm.edu.sa/ws/api
  baseurl_source: declared
  description: The user API from King Fahd University of Petroleum & Minerals — 7 operation(s) for user.
  name: King Fahd University of Petroleum & Minerals User API
  slug: kfupm-user-api
artifact_total: 52
common:
- group: other
  href: https://artifacts.apis.io/kfupm/capabilities/kfupm-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kfupm-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.kfupm.edu.sa/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kfupm.edu.sa/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kfupm.edu.sa/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://news.kfupm.edu.sa/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/kfupm/
- group: other
  title: ''
  type: IdentityFederation
  url: https://sts.kfupm.edu.sa/FederationMetadata/2007-06/FederationMetadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://eprints.kfupm.edu.sa/
- group: start
  title: ''
  type: ResearchPortal
  url: https://pure.kfupm.edu.sa/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://registrar.kfupm.edu.sa/courses-classes/course-offering1/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library-web.kfupm.edu.sa/
- group: build
  title: ''
  type: AITooling
  url: https://www.kfupm.edu.sa/about-us/discover/ai-x
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KFUPM-OSC
- group: auth
  href: https://artifacts.apis.io/kfupm/authentication/kfupm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kfupm-authentication.yml
- group: auth
  href: https://artifacts.apis.io/kfupm/scopes/kfupm-scopes.yml
  title: ''
  type: Scopes
  url: scopes/kfupm-scopes.yml
- group: design
  href: https://artifacts.apis.io/kfupm/conformance/kfupm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kfupm-conformance.yml
- group: design
  href: https://artifacts.apis.io/kfupm/errors/kfupm-errors.yml
  title: ''
  type: Errors
  url: errors/kfupm-errors.yml
- group: design
  href: https://artifacts.apis.io/kfupm/lifecycle/kfupm-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kfupm-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/kfupm/vocabulary/kfupm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kfupm-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/kfupm/security/kfupm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kfupm-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/kfupm/plans/kfupm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kfupm-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kfupm/rate-limits/kfupm-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kfupm-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kfupm/finops/kfupm-finops.yml
  title: ''
  type: FinOps
  url: finops/kfupm-finops.yml
- group: other
  href: https://artifacts.apis.io/kfupm/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'King Fahd University of Petroleum & Minerals (KFUPM) is a public research university in Dhahran, Saudi Arabia. Its programmable footprint is small, and most of what previously appeared in this profile was not its own: 37 OpenAPI definitions attributed to KFUPM here were the Elsevier Pure Web Services contract (info.title "Pure API", contact pure-support@elsevier.com, version 5.35.3-4) served from the university''s Pure tenant at pure.kfupm.edu.sa. That contract is Elsevier''s and has been removed; the tenant relationship is recorded instead. What KFUPM genuinely operates is three surfaces on its own infrastructure. Its identity provider at sts.kfupm.edu.sa publishes signed SAML 2.0 federation metadata and an OpenID Connect discovery document, and is registered in eduGAIN through MAEEN, the Saudi identity federation, with scope kfupm.edu.sa — an institution-operated machine-readable surface by definition. The KFUPM ePrints repository (EPrints 3.4.1) serves a live, unauthenticated
  OAI-PMH 2.0 harvesting interface with six working verbs and six metadata formats, plus record-level and search-level JSON export whose record model carries a KFUPM-local `arabic_abstract` field. The registrar publishes a live course offering system, but it answers only an HTML form POST and returns no machine-readable format. There is no central developer portal, no API documentation, no changelog, no status page, no robots.txt, no sitemap and no llms.txt on the university''s own domain. The library discovery surface sits behind a Cloudflare bot challenge. KFUPM does not publish an OpenAPI for anything it operates; the three descriptions in this repo were derived by probing the live endpoints.'
examples:
- key_count: 2
  name: Kfupm Sts Openid Configuration
  slug: kfupm-sts-openid-configuration
finops:
- has_sources: true
  method: derived
  name: Kfupm Finops
  primary_unit: ''
  service_category: Education
  slug: kfupm-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kfupm.png
json_schemas:
- name: KFUPM ePrints Record
  property_count: 0
  slug: kfupm-eprints-record
layout: provider
modified: '2026-08-30'
name: King Fahd University of Petroleum & Minerals
nav: Providers
network: true
overview: 'King Fahd University of Petroleum & Minerals publishes 43 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discovery API, Export API, Oai Pmh API, and 40 more. Tagged areas include University, Higher Education, Education, Research, and Saudi Arabia.


  The King Fahd University of Petroleum & Minerals catalog on APIs.io includes 1 Spectral governance ruleset.


  King Fahd University of Petroleum & Minerals'' developer surface includes engineering blog, authentication, and 22 more developer resources.'
plans:
- name: Kfupm Plans Pricing
  plan_count: 2
  slug: kfupm-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Kfupm Rate Limits
  slug: kfupm-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: King Fahd University of Petroleum & Minerals API Rules
  rule_count: 64
  severity_counts:
    error: 39
    hint: 0
    info: 3
    warn: 22
  slug: kfupm-rules
scopes:
- name: Kfupm Scopes
  scope_count: 9
  slug: kfupm-scopes
  summary_line: 9 scopes
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 51.3
    catalog_earned_first_party: 0.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 26.3
    contract_governance: 17.4
    contract_quality: 56.3
    developer_ergonomics: 23.8
    discoverability: 71.4
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 34.9
  provenance:
    conformance: first-party
    contracts:
      callable: 11.9
      derived: 0
      marker_coverage: 88.1
      total: 42
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kfupm/kfupm-2026-06-20T184024.png
security:
- kind: authentication
  name: Kfupm Authentication
  slug: kfupm-authentication
  summary_line: openIdConnect/oauth2/saml2/apiKey/none · 4 schemes
- kind: domain-security
  name: Kfupm Domain Security
  slug: kfupm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kfupm
tags:
- University
- Higher Education
- Education
- Research
- Saudi Arabia
- Middle East
- Identity Federation
- Research Repository
- Open Access
- OAI-PMH
- Theses
- Course Catalog
website: https://www.kfupm.edu.sa/
---
