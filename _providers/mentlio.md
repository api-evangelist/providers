---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Mentlio API provides endpoints for engineering intelligence and token optimization.
  name: Mentlio API
  slug: mentlio-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://www.mentlio.com/security
- group: agent
  href: https://artifacts.apis.io/mentlio/llms/mentlio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mentlio-llms.txt
- group: auth
  href: https://artifacts.apis.io/mentlio/well-known/mentlio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mentlio-security.txt
- group: auth
  href: https://artifacts.apis.io/mentlio/well-known/mentlio-mentlio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mentlio-mentlio-security.txt
- group: auth
  href: https://artifacts.apis.io/mentlio/well-known/mentlio-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mentlio-app-security.txt
- group: agent
  href: https://artifacts.apis.io/mentlio/well-known/mentlio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mentlio-well-known.yml
- group: other
  href: https://artifacts.apis.io/mentlio/hosts/mentlio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mentlio-hosts.yml
- group: other
  href: https://artifacts.apis.io/mentlio/vendors/mentlio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mentlio-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mentlio/security/mentlio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mentlio-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mentlio/security/mentlio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mentlio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mentlio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mentlio.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.mentlio.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mentlio.com/
- group: operate
  title: ''
  type: Support
  url: https://www.mentlio.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.mentlio.com/research
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mentlio.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mentlio.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mentlio.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mentlio
- group: operate
  title: ''
  type: Roadmap
  url: https://www.mentlio.com/roadmap
- group: start
  title: ''
  type: SignUp
  url: https://www.mentlio.com/login
- group: operate
  title: ''
  type: Status
  url: https://www.mentlio.com/status
coverage:
  checked: '2026-10-18'
  detail: Documentation pages are JavaScript-rendered single-page apps with no machine‑readable OpenAPI or other contract discovered.
  evidence:
  - status: 200
    url: https://www.mentlio.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Mentlio provides engineering intelligence and token optimization for AI workloads. Their platform measures AI usage locally, reduces token waste, and keeps prompts and source code on-device. By offering detailed insights into AI costs, performance, and ROI, Mentlio helps teams understand and control AI spend, improve efficiency, and ensure data privacy. The service includes research, documentation, and integrations, targeting enterprises seeking to optimize AI adoption and reduce operational expenses.
image: https://www.mentlio.com/mentlio-icon.png
layout: provider
modified: '2026-10-18'
name: Mentlio
nav: Providers
network: true
overview: 'Mentlio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Engineering Intelligence, Token Optimization, and Enterprise.


  Mentlio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 64.3
    operational_transparency: 10.5
  previous_composite: 25.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mentlio/mentlio-2026-11-03T135502.png
security:
- kind: domain-security
  name: Mentlio Domain Security
  slug: mentlio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mentlio Vulnerability Disclosure
  slug: mentlio-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mentlio
tags:
- Company
- Artificial Intelligence
- Engineering Intelligence
- Token Optimization
- Enterprise
website: https://mentlio.com/
---
