---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 2.5
  scored_at: '2026-09-04'
api_count: 5
apis:
- description: 'Queen''s University Belfast operates a production Shibboleth SAML 2.0 Identity Provider registered in the UK Access Management Federation and, through it, eduGAIN. The signed SAML entity descriptor is '
  name: Queen's University Belfast Shibboleth Identity Provider (UK Access Management Federation)
  slug: identity-federation-idp
- description: Live OAI-PMH 2.0 metadata harvesting endpoint for the QUB Research Portal. Identify returns repositoryName "QUB Research Portal" with adminEmail puresupport@qub.ac.uk and an earliest datestamp of 2016
  name: Queen's University Belfast Research Portal — OAI-PMH harvesting endpoint
  slug: research-portal-oai
- description: The QUB tenancy of the Elsevier Pure Web Service API. The deployment is real and callable at https://pureadmin.qub.ac.uk/ws/api — an unauthenticated request returns HTTP 401 "Full authentication is re
  name: Queen's University Belfast Pure API deployment (Elsevier Pure tenancy)
  slug: pure-web-service-api
- description: The Queen's Canvas virtual learning environment, reachable at canvas.qub.ac.uk. The Canvas REST API responds on the QUB hostname (an unauthenticated GET /api/v1/courses returns 401 "user authorisation
  name: Queen's University Belfast Canvas LMS deployment (Instructure tenancy)
  slug: canvas-lms
- description: Queen's University Belfast is a DataCite consortium organization (provider jxtg) and has operated a registered DataCite repository client, BL.QUB, since 2015, through which the Research Portal mints D
  name: Queen's University Belfast Research Portal — DataCite repository client
  slug: datacite-repository-client
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.qub.ac.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.qub.ac.uk/directorates/InformationServices/TheLibrary/ResearchSupport/OpenResearch/
- group: other
  title: ''
  type: ResearchRepository
  url: https://pure.qub.ac.uk/
- group: other
  title: ''
  type: IdentityFederation
  url: http://mdq.ukfederation.org.uk/entities/https%3A%2F%2Fqub.ac.uk%2Fshibboleth
- group: build
  title: ''
  type: LibraryCatalog
  url: https://qub.primo.exlibrisgroup.com/discovery/search?vid=44QSUB_INST:QUB
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.qub.ac.uk/courses/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.ni-hpc.ac.uk/
- group: other
  title: ''
  type: AIPolicy
  url: https://blogs.qub.ac.uk/digitallearning/ai/ai-in-research/qub-guidance-on-responsible-use-of-ai-in-research/
- group: build
  title: ''
  type: AITooling
  url: https://libguides.qub.ac.uk/AILibrary
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qub.ac.uk/about/website/privacy-and-cookies/
- group: other
  title: ''
  type: Accessibility
  url: https://www.qub.ac.uk/about/website/accessibility-statement/
- group: operate
  title: ''
  type: Support
  url: https://www.qub.ac.uk/contact/ask-a-question/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/queens-university-belfast/
- group: design
  title: ''
  type: Conformance
  url: conformance/queens-university-belfast-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/queens-university-belfast-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/queens-university-belfast-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/queens-university-belfast-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/queens-university-belfast-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Queen''s University Belfast is a public research-intensive university in Belfast, Northern Ireland, founded in 1845 and a member of the Russell Group. Its programmable footprint is almost entirely a buyer''s footprint rather than a builder''s: there is no central developer portal, no api.qub.ac.uk, no institutional open-data portal, and no institution-authored OpenAPI. The research surface people mistake for QUB engineering is an Elsevier Pure tenancy — pure.qub.ac.uk and pureadmin.qub.ac.uk both CNAME into eu.prod.elsevierpure.com, and the OpenAPI served there is titled "Pure API" with contact pure-support@elsevier.com, so the data is QUB''s and the contract is Elsevier''s. The same pattern holds for the VLE (Canvas at canvas.qub.ac.uk, CNAME qub-vanity.instructure.com) and library discovery (Ex Libris Primo at qub.primo.exlibrisgroup.com). What QUB genuinely operates and publishes in machine-readable form is its identity federation: a production Shibboleth SAML 2.0 Identity
  Provider (entityID https://qub.ac.uk/shibboleth) registered in the UK Access Management Federation, which also hosts federated identity for the Healthcare Library of Northern Ireland and AFBI. Alongside that sit a live OAI-PMH 2.0 harvesting endpoint for the Research Portal, a registered DataCite repository client (BL.QUB, 2015), a school-level Crossref membership, and the NI-HPC / Kelvin2 national high-performance computing service, whose site runs on QUB''s own web platform. This profile deliberately records those tenancies as relationships rather than as QUB''s own contracts.'
finops:
- name: Queens University Belfast Finops
  service_category: Education
  slug: queens-university-belfast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/queens-university-belfast.png
layout: provider
modified: '2026-08-30'
name: Queen's University Belfast
nav: Providers
network: true
overview: 'Queen''s University Belfast publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Research, and United Kingdom.


  Queen''s University Belfast''s developer surface includes documentation, support, and 17 more developer resources.'
plans:
- name: Queens University Belfast Plans Pricing
  plan_count: 2
  slug: queens-university-belfast-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Queens University Belfast Rate Limits
  slug: queens-university-belfast-rate-limits
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 7
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
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 27.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Queens University Belfast Domain Security
  slug: queens-university-belfast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: queens-university-belfast
tags:
- University
- Higher Education
- Education
- Research
- United Kingdom
- Northern Ireland
- Russell Group
- Identity Federation
- Research Repository
- Open Access
- OAI-PMH
- Shibboleth
- SAML
- Research Computing
website: https://www.qub.ac.uk/
---
