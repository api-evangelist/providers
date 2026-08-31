---
access_model:
  confidence: high
  label: Free · anonymous harvesting, no registration offered
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
    error_semantics: documented
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
  score: 22.1
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'Anonymous OAI-PMH 2.0 metadata harvesting over the POSTECH Library OASIS institutional repository. Verified live on 2026-08-30: repositoryName "OASIS Repository@POSTECHLIBRARY", repositoryIdentifier o'
  name: POSTECH OASIS Repository OAI-PMH
  slug: oasis-oai-pmh
- description: POSTECH's own SAML 2.0 identity provider, entityID https://idpass.postech.ac.kr/idp/simplesamlphp, registered in KAFE (the Korea Access Federation, run on KREONET) since registrationInstant 2017-06-23
  name: POSTECH SAML 2.0 Identity Provider
  slug: identity-federation
- description: POSTECH's learning management system is an institution-hosted Moodle (coursemos distribution) acting as an LTI 1.3 Advantage platform, and unusually for this cohort its platform endpoints are publicly
  name: POSTECH LMS (PLMS) LTI 1.3 Advantage Platform
  slug: plms-lti
- description: The Moodle Web Services REST interface is enabled on POSTECH's LMS and is publicly reachable, but every anonymous call returns the moodle_exception errorcode invalidtoken. Tokens are issued inside the
  name: POSTECH LMS (PLMS) Moodle Web Services
  slug: plms-webservices
- description: POSTECH's tenancy on dCollection, the Korea Education and Research Information Service national digital thesis and dissertation distribution system. The relationship is evidenced from POSTECH's own OA
  name: POSTECH dCollection Thesis Repository (KERIS tenancy)
  slug: dcollection
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.postech.ac.kr/eng/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.postech.ac.kr/eng/usage-guide/privacy_policy.do
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.postech.ac.kr/kor/usage-guide/copyright_policy.do
- group: company
  title: ''
  type: LinkedIn
  url: https://kr.linkedin.com/school/pohang-university-of-science-and-technology/
- group: company
  title: ''
  type: Blog
  url: https://www.postech.ac.kr/eng/news-center/university_news.do
- group: other
  title: ''
  type: ResearchRepository
  url: https://oasis.postech.ac.kr/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.postech.ac.kr/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://plms.postech.ac.kr/local/ubion/course/lists.php?lang=en
- group: other
  title: ''
  type: IdentityFederation
  url: https://technical.edugain.org/api.php?action=show_entity&entityid=https://idpass.postech.ac.kr/idp/simplesamlphp&format=json
- group: start
  title: ''
  type: Portal
  url: https://podium.postech.ac.kr/
- group: auth
  title: ''
  type: Authentication
  url: authentication/postech-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/postech-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/postech-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/postech-lifecycle.yml
- group: build
  title: ''
  type: Examples
  url: examples/postech-oasis-oai-pmh-examples.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postech-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/postech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/postech-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/postech-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Pohang University of Science and Technology (POSTECH) is a private research university in Pohang, North Gyeongsang, South Korea, founded in 1986 by the steelmaker POSCO and consistently ranked inside the QS world top 100. POSTECH operates no developer portal, no open-data program and no API it authored itself — but it is not empty, and three genuinely institution-operated machine-readable surfaces were verified live on 2026-08-30, all of them on POSTECH''s own network (141.223.0.0/16). The OASIS institutional repository serves a fully anonymous OAI-PMH 2.0 harvesting endpoint over a corpus of 106,805 records in twelve metadata formats across 163 sets, reaching back to 2014. POSTECH runs its own SAML 2.0 identity provider at idpass.postech.ac.kr, registered in the KAFE federation since 2017 and resolvable through eduGAIN, supporting the REFEDS Research and Scholarship entity category and asserting SIRTFI — machine-readable institutional infrastructure that almost nothing in
  this cohort catalogues. And POSTECH''s LMS publishes a live, public LTI 1.3 Advantage platform keyset and OAuth 2.0 token endpoint, which most institution-hosted Moodles keep unreachable. Everything else is a login wall or someone else''s platform: the PODIUM portal, admissions and certificate systems are gated; the DSpace REST interface sits behind a JavaScript bot challenge that returns 200 with a challenge shell; and the thesis pipeline runs through postech.dcollection.net, a tenancy on the KERIS-operated national dCollection platform, recorded here as a relationship rather than as POSTECH''s engineering.'
finops:
- name: Postech Finops
  service_category: Education
  slug: postech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postech.png
jsonld:
- class_count: 15
  name: Postech Context
  property_count: 3
  slug: postech-context
layout: provider
modified: '2026-08-30'
name: Pohang University of Science and Technology
nav: Providers
network: true
overview: 'Pohang University of Science and Technology publishes 1 API on the [APIs.io](https://apis.io/) network: POSTECH OASIS Repository OAI-PMH. Tagged areas include University, Higher Education, Education, South Korea, and Korea.


  The Pohang University of Science and Technology catalog on APIs.io includes 1 JSON-LD context.


  Pohang University of Science and Technology''s developer surface includes engineering blog, developer portal, authentication, code examples, and 16 more developer resources.'
plans:
- name: Postech Plans Pricing
  plan_count: 2
  slug: postech-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Postech Rate Limits
  slug: postech-rate-limits
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 23.9
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 55.1
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/postech/refs/heads/main/screenshots/postech-2026-06-20T192013.png
security:
- kind: authentication
  name: Postech Authentication
  slug: postech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Postech Domain Security
  slug: postech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: postech
tags:
- University
- Higher Education
- Education
- South Korea
- Korea
- Asia
- Private Research University
- Research
- Research Data
- Institutional Repository
- OAI-PMH
- DSpace
- Library
- Identity Federation
- SAML
- eduGAIN
- LTI
- Learning Management System
- Course Catalog
website: https://www.postech.ac.kr/eng/
---
