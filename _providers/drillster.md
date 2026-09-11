---
access_model:
  confidence: high
  label: Enterprise licence, sales-led
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://drillster.com/en/pricing
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: The Drillster REST API (v2.1.1) lets developers integrate Drillster's adaptive learning and training platform into external applications. Roughly 180 documented endpoints and 200 response objects cove
  name: Drillster API
  slug: drillster-api
artifact_total: 9
asyncapis:
- description: ''
  name: Drillster Push Webhooks
  slug: drillster-push-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.drillster.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.drillster.com/info/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.drillster.com/info/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://www.drillster.com/info/developers/api/2.1.1/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.drillster.com/info/developers/rest-apis/registering-your-application/
- group: auth
  title: ''
  type: Authentication
  url: authentication/drillster-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/drillster-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/drillster-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/drillster-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/drillster-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.drillster.com/info/developers/api/2.1.1/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/drillster-push-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/drillster-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/drillster-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/drillster-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/drillster-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/drillster-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/drillster-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/drillster-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/drillster-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.drillster.com/info/reporting-security-breach/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/drillster-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drillster-domain-security.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://drillster.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://drillster.com/en/request-demo
- group: start
  title: ''
  type: Login
  url: https://www.drillster.com/console
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drillster.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drillster.com/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.drillster.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://drillster.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/drillster
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drillster-bv
created: '2025-02-17'
description: Drillster is a Utrecht-based adaptive learning platform for corporate and vocational training, built on repetition-based drills that schedule practice at the moment a learner is about to forget. Customers in aviation, healthcare, financial services, energy, railway and construction use it to keep safety- and compliance-critical knowledge reliable year-round. For developers, Drillster publishes a documented REST API (version 2.1.1, JSON over HTTPS, OAuth 2.0 with a JWT-bearer service-account grant) covering user provisioning, group and membership management, catalogs, drills, tests, objectives and results reporting; an outbound event notification service with seven webhook event types and a seven-day retry contract; an embeddable widget family with a JavaScript loader; and standards-based LMS integration through LTI 1.0/1.3, SCORM 1.2 and OpenID Connect single sign-on.
finops:
- name: Drillster Finops
  service_category: API
  slug: drillster-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drillster.png
layout: provider
modified: '2026-09-06'
name: Drillster
nav: Providers
network: true
overview: 'Drillster publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Assessments, Education, Learning, Quizzes, and Training.


  The Drillster catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Drillster''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, signup flow, support, and 25 more developer resources.'
plans:
- name: Drillster Plans Pricing
  plan_count: 1
  slug: drillster-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Drillster Rate Limits
  slug: drillster-rate-limits
scopes:
- name: Drillster Scopes
  scope_count: 1
  slug: drillster-scopes
  summary_line: 1 scope · authorizationCode/urn:ietf:params:oauth:grant-type:jwt-bearer
score:
  band: strong
  composite: 57.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 57.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 75.9
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/drillster/refs/heads/main/screenshots/drillster-2026-06-20T180231.png
security:
- kind: authentication
  name: Drillster Authentication
  slug: drillster-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Drillster Domain Security
  slug: drillster-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Drillster Vulnerability Disclosure
  slug: drillster-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: drillster
tags:
- Assessments
- Education
- Learning
- Quizzes
- Training
- LMS
- Adaptive Learning
- Compliance Training
- Webhooks
website: https://www.drillster.com
---
