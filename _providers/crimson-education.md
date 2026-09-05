---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The backend API behind the Crimson App student and mentor platform. There is no provider-published OpenAPI or public developer portal; the surface is documented and exercised through the first-party T
  name: Crimson App API
  slug: crimson-app-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.crimsoneducation.org/us
- group: company
  title: ''
  type: Blog
  url: https://www.crimsoneducation.org/us/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crimsoneducation.org/us/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crimson-education
- group: start
  title: ''
  type: Login
  url: https://app.crimsoneducation.org/
- group: company
  title: ''
  type: Careers
  url: https://jobs.crimsoneducation.org/
- group: build
  title: ''
  type: Packages
  url: packages/crimson-education-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crimson-education-packages.yml
- group: design
  title: ''
  type: Components
  url: components/crimson-education-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crimson-education-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crimson-education-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crimson-education-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crimson-education-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crimson-education-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crimson-education-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/crimson-education-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crimson-education-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/crimson-education-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crimson-education-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crimson-education-llms.txt
created: '2026-08-04'
description: Crimson Education is a multinational university admissions consultancy founded in Auckland, New Zealand in 2013 by Jamie Beaton, Fangzhou Jiang and Sharndre Kushor. It provides college-prep and admissions consulting for US, UK, EU and Australian universities, graduate and medical school admissions support, curriculum tutoring and extracurricular mentoring, and operates the Crimson Global Academy online high school alongside brands including MedView, Crimson MBA and Unfiltered. Its student and mentor experience runs on the Crimson App, whose backend REST and GraphQL surface is reached through a first-party TypeScript SDK published on npm as @crimson-education/sdk.
image: https://app.crimsoneducation.org/static/PWAConfig/crimsonApp/icons/icon-192x192.png
layout: provider
modified: '2026-08-04'
name: Crimson Education
nav: Providers
network: true
overview: 'Crimson Education publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Admissions, and Tutoring.


  Crimson Education''s developer surface includes engineering blog, authentication, changelog, sandbox, and 16 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 11.8
    commercial_clarity: 11.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 27.4
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 18.8
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 35.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Crimson Education Authentication
  slug: crimson-education-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Crimson Education Domain Security
  slug: crimson-education-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: crimson-education
tags:
- Company
- Education
- EdTech
- Admissions
- Tutoring
- Students
- Online Learning
- Mentoring
website: https://www.crimsoneducation.org/us
---
