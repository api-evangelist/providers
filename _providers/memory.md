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
  band: human-only
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Timely's REST API (version 1.1) at api.timelyapp.com, secured with OAuth 2.0, for programmatic access to accounts, projects, clients, users, events (time entries), labels and reports.
  name: Timely API
  slug: timely-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.timely.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.timely.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.timely.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.timely.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.timely.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.timely.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.timely.com/help/
- group: start
  title: ''
  type: SignUp
  url: https://app.timelyapp.com/join
- group: start
  title: ''
  type: Login
  url: https://app.timelyapp.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.timely.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.timely.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.timely.com/security/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.timely.com/status/
- group: auth
  title: ''
  type: Authentication
  url: authentication/memory-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/memory-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/memory-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.timely.com/security/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/memory-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memory-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/memory-llms.txt
created: '2026-07-17'
description: Memory AS (operating as Timely, timely.com) is an Oslo, Norway based software company behind Timely, an AI-powered automatic time tracking and timesheet platform for consultancies, agencies, professional-services firms and SaaS teams. Its Memory tracking engine passively captures work across the apps a person uses and its AutoSheet feature auto-completes timesheets, letting teams auto-capture, auto-allocate and one-click approve time. Timely exposes a REST API at api.timelyapp.com (version 1.1) secured with OAuth 2.0 for building on accounts, projects, clients, users, events (time entries) and reports, and offers 90+ direct integrations with tools such as QuickBooks, Xero, Asana, Jira, GitHub, Slack, Google Calendar and Salesforce. The company is ISO 27001:2022 certified and GDPR-aligned, backed by 500 Global.
image: https://www.timely.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Memory
nav: Providers
network: true
overview: 'Memory publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Time Tracking, Timesheets, Productivity, and Project Management.


  Memory''s developer surface includes documentation, API reference, pricing, engineering blog, support, signup flow, authentication, and 13 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 32.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/memory/refs/heads/main/screenshots/memory-2026-08-07T172504.png
security:
- kind: authentication
  name: Memory Authentication
  slug: memory-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Memory Domain Security
  slug: memory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: memory
tags:
- Company
- Time Tracking
- Timesheets
- Productivity
- Project Management
- Professional Services
- Reporting
- Automation
- Artificial Intelligence
- Software-as-a-Service
website: https://www.timely.com
---
