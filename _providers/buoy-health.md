---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Auth0-backed OAuth 2.0 / OpenID Connect authorization server that issues the bearer tokens the Buoy Symptom Checker API requires. Publishes anonymous RFC 8414 authorization-server metadata and OIDC di
  name: Buoy Authorization Server
  slug: buoy-authorization-server
- baseURL: https://api.buoyhealth.com/symptom-checker/v2
  baseurl_source: declared
  description: The Complaints API from Buoy Health — 2 operation(s) for complaints.
  name: Buoy Health Complaints API
  slug: buoy-health-complaints-api
- baseURL: https://api.buoyhealth.com/symptom-checker/v2
  baseurl_source: declared
  description: The Intents API from Buoy Health — 2 operation(s) for intents.
  name: Buoy Health Intents API
  slug: buoy-health-intents-api
- baseURL: https://api.buoyhealth.com/symptom-checker/v2
  baseurl_source: declared
  description: The Interviews API from Buoy Health — 2 operation(s) for interviews.
  name: Buoy Health Interviews API
  slug: buoy-health-interviews-api
- baseURL: https://api.buoyhealth.com/symptom-checker/v2
  baseurl_source: declared
  description: The Queries API from Buoy Health — 1 operation(s) for queries.
  name: Buoy Health Queries API
  slug: buoy-health-queries-api
- baseURL: https://api.buoyhealth.com/symptom-checker/v2
  baseurl_source: declared
  description: The Questions API from Buoy Health — 3 operation(s) for questions.
  name: Buoy Health Questions API
  slug: buoy-health-questions-api
- baseURL: https://api.buoyhealth.com/symptom-checker/v2
  baseurl_source: declared
  description: The Results API from Buoy Health — 1 operation(s) for results.
  name: Buoy Health Results API
  slug: buoy-health-results-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Buoy Symptom Checker Complaints API
  slug: open-buoy-health-complaints-api
- collection_type: open
  name: Buoy Symptom Checker Intents API
  slug: open-buoy-health-intents-api
- collection_type: open
  name: Buoy Symptom Checker Interviews API
  slug: open-buoy-health-interviews-api
- collection_type: open
  name: Buoy Symptom Checker Queries API
  slug: open-buoy-health-queries-api
- collection_type: open
  name: Buoy Symptom Checker Questions API
  slug: open-buoy-health-questions-api
- collection_type: open
  name: Buoy Symptom Checker Results API
  slug: open-buoy-health-results-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.buoyhealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.buoyhealth.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://buoyhealth.readme.io/reference/interviews_anonymous
- group: docs
  title: ''
  type: APIReference
  url: https://buoyhealth.readme.io/reference
- group: operate
  title: ''
  type: Support
  url: https://www.buoyhealth.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.buoyhealth.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buoyhealth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buoyhealth.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/buoy-health-api/buoy-symptom-checker-api/overview
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/buoy-health-symptom-checker-openapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/buoy-health-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/buoy-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/buoy-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/buoy-health-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/buoy-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/buoy-health-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/buoy-health-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/buoy-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/buoy-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.buoyhealth.com/security-and-privacy
- group: start
  title: ''
  type: Sandbox
  url: sandbox/buoy-health-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/buoy-health-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/buoy-health-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.buoyhealth.com/security-and-privacy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/buoy-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buoy-health-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/buoy-health-symptom-checker-overlay.yaml
created: '2026-08-08'
description: Buoy Health is a Boston-based digital health company whose clinically-trained AI symptom checker and triage engine is offered to health systems, payers and employers as an embeddable API. The Buoy Symptom Checker API v2.0 exposes a conversational triage interview as REST resources — interviews, complaints, queries, intents, questions and results — so an integrator can create a de-identified anonymous interview from basic demographics, accept a chief complaint, walk an adaptively generated question sequence, and read back a differential diagnosis with a recommended level of care and customizable care-handoff destinations. The API is OAuth 2.0 protected against an Auth0-backed authorization server with separate sandbox and production environments, is documented on ReadMe with a published OpenAPI 3.0.1 definition and an llms.txt, and Buoy is HITRUST CSF certified.
image: https://www.buoyhealth.com/cms/images/buoy_logo.svg
layout: provider
modified: '2026-08-08'
name: Buoy Health
nav: Providers
network: true
overview: 'Buoy Health publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Complaints API, Intents API, Interviews API, and 3 more. Tagged areas include Symptom Checker, medical-triage, Digital Health, Healthcare, and Clinical AI.


  Buoy Health''s developer surface includes documentation, API reference, support, engineering blog, authentication, sandbox, and 22 more developer resources.'
random_paper: 9
scopes:
- name: Buoy Health Scopes
  scope_count: 14
  slug: buoy-health-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 57.6
    developer_ergonomics: 53.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 51.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 82.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buoy-health/refs/heads/main/screenshots/buoy-health-2026-08-17T080742.png
security:
- kind: authentication
  name: Buoy Health Authentication
  slug: buoy-health-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Buoy Health Domain Security
  slug: buoy-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Buoy Health Vulnerability Disclosure
  slug: buoy-health-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: buoy-health
tags:
- Symptom Checker
- medical-triage
- Digital Health
- Healthcare
- Clinical AI
- Care Navigation
- Patient Engagement
- Diagnosis
- Telehealth
- Authentication
website: https://www.buoyhealth.com/
---
