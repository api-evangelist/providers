---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
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
  score: 15.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Adonis platform API for revenue cycle management, including real-time patient eligibility and benefits verification, patient and appointment data retrieval from partner EHR/PM systems, claims, and pay
  name: Adonis API
  slug: adonis-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://adonis.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://adonis.io/platform
- group: start
  title: ''
  type: SignUp
  url: https://app.adonis.io/
- group: start
  title: ''
  type: Login
  url: https://app.adonis.io/
- group: company
  title: ''
  type: Blog
  url: https://adonis.io/blog
- group: operate
  title: ''
  type: Support
  url: https://adonis.io/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adonis.io/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://adonis.io/privacy-and-security
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adonis-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adonis-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adonis-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adonis-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adonis-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adonis-llms.txt
created: '2026-07-17'
description: Adonis is a healthcare Revenue Cycle Management (RCM) technology company that helps physician groups, hospitals, health systems, digital health organizations, and practice management services maximize revenue and reduce the cost and time of collections. Founded in 2022 and headquartered at 3 World Trade Center in New York, Adonis pairs an AI orchestration platform (Adonis AI Agents, Adonis Intelligence, and Adonis Orchestration) with real-time patient eligibility and benefits verification, denial prevention, claims and payment automation, and revenue analytics. The platform integrates with electronic health record and practice management systems including Epic, athenahealth, eClinicalWorks, AdvancedMD, NextGen, DrChrono, Canvas, Healthie, Office Ally, Change Healthcare, and Availity, and exposes API access (for example Patient Verification) for building patient onboarding and intake experiences. Adonis is a General Catalyst portfolio company and has raised over $95M across Series
  A through Series C from General Catalyst, Quadrille Capital, Bling Capital, Max Ventures, and Homebrew.
image: https://adonis.io/favicon.ico
layout: provider
modified: '2026-07-18'
name: Adonis
nav: Providers
network: true
overview: 'Adonis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Revenue Cycle Management, RCM, and Medical Billing.


  Adonis'' developer surface includes signup flow, engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 8
scopes:
- name: Adonis Scopes
  scope_count: 14
  slug: adonis-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 53.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adonis/refs/heads/main/screenshots/adonis-2026-07-25T181659.png
security:
- kind: authentication
  name: Adonis Authentication
  slug: adonis-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Adonis Domain Security
  slug: adonis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adonis
tags:
- Company
- Healthcare
- Revenue Cycle Management
- RCM
- Medical Billing
- Health IT
- Eligibility Verification
- Claims
- Payments
- Artificial Intelligence
- Automation
website: https://adonis.io/
---
