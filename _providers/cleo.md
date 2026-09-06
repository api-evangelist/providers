---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  score: 13.3
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cleo-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cleo-ai
- group: company
  title: ''
  type: Website
  url: https://web.meetcleo.com/
- group: company
  title: ''
  type: Blog
  url: https://web.meetcleo.com/blog
- group: operate
  title: ''
  type: Help Center
  url: https://web.meetcleo.com/faqs/en/
- group: operate
  title: ''
  type: Support
  url: https://web.meetcleo.com/faqs/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://web.meetcleo.com/page/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://web.meetcleo.com/page/term-conditions
- group: commercial
  title: ''
  type: Pricing
  url: https://web.meetcleo.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meetcleo
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cleo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cleo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cleo-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cleo-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/cleo-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cleo-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cleo-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cleo-llms.txt
created: '2025-03-01'
description: Cleo is an AI-powered personal finance assistant delivered through a chat interface in iOS and Android apps. The platform helps consumers budget, track spending across linked bank accounts, set savings goals, and access features such as Cleo Wallet (savings), Cleo Cover (cash advance), and Cleo Builder (credit-building). Cleo connects to user bank accounts using Plaid for read-only transaction access and does not currently publish a public, third-party developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cleo.png
layout: provider
modified: '2026-09-05'
name: Cleo
nav: Providers
network: true
overview: 'Cleo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Banking, Budgeting, Cash Advance, and Consumer Finance.


  Cleo''s developer surface includes engineering blog, support, pricing, authentication, and 14 more developer resources.'
plans:
- name: Cleo Plans Pricing
  plan_count: 3
  slug: cleo-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Cleo Rate Limits
  slug: cleo-rate-limits
scopes:
- name: Cleo Scopes
  scope_count: 3
  slug: cleo-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 24.4
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 3.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cleo/refs/heads/main/screenshots/cleo-2026-08-07T180001.png
security:
- kind: authentication
  name: Cleo Authentication
  slug: cleo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cleo Domain Security
  slug: cleo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cleo
tags:
- Artificial Intelligence
- Banking
- Budgeting
- Cash Advance
- Consumer Finance
- Financial Assistant
- Personal Finance
website: https://web.meetcleo.com/
---
