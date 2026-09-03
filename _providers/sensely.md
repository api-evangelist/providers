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
  - rate-limits
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The AWS API Gateway surface behind the Sensely conversational SDKs. Observed public operations cover partner authentication and token refresh, member self-service password reset, program-code verifica
  name: Sensely Platform API
  slug: sensely-platform-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sensely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sensely.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.mediktor.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sensely
- group: company
  title: ''
  type: Blog
  url: https://sensely.com/news/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sense.ly/
- group: start
  title: ''
  type: Login
  url: https://sensely.com/customer-portal/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sensely.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sensely.com/privacy-policy/
- group: build
  title: ''
  type: SDKs
  url: packages/sensely-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/sensely-packages.yml
- group: design
  title: ''
  type: Components
  url: components/sensely-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sensely-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/sensely-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sensely-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sensely-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sensely-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sensely-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sensely-rate-limits.yml
created: '2026-08-26'
description: Sensely is a San Francisco conversational-AI company whose empathy-driven avatar assistant guides health-plan members and patients through symptom assessment, care navigation, mental-health check-ins, enrollment and onboarding, and chronic-condition management. The platform is licensed to payers, providers, pharmaceutical companies and employers, and is embedded by partners through first-party iOS, Android and Web/JavaScript conversational SDKs backed by an AWS-hosted platform API at apis.sensely.com. Clinical content is licensed from Mayo Clinic and the NHS, and the assistant is deployed across the Sensely app, web, SMS, WhatsApp, Facebook Messenger, WeChat, Line and Telegram. Sensely was acquired by Spanish AI-triage company Mediktor, announced 5 June 2024.
image: https://assets.sense.ly/images/senselyLogoWhite.png
layout: provider
modified: '2026-08-26'
name: Sensely
nav: Providers
network: true
overview: 'Sensely publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Health, Conversational AI, and Virtual Assistant.


  Sensely''s developer surface includes engineering blog, changelog, and 17 more developer resources.'
plans:
- name: Sensely Plans Pricing
  plan_count: 0
  slug: sensely-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Sensely Rate Limits
  slug: sensely-rate-limits
scopes:
- name: Sensely Scopes
  scope_count: 0
  slug: sensely-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 29.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 60.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sensely/refs/heads/main/screenshots/sensely-2026-09-02T154858.png
security:
- kind: authentication
  name: Sensely Authentication
  slug: sensely-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Sensely Domain Security
  slug: sensely-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sensely
tags:
- Company
- Healthcare
- Digital Health
- Conversational AI
- Virtual Assistant
- Symptom Checker
- Patient Engagement
- Health Insurance
- Mental Health
- SDK
website: https://sensely.com/
---
