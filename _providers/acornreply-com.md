---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for ticket intake and knowledge base management.
  name: AcornReply API
  slug: acornreply-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/acornreply-com/plans/acornreply-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/acornreply-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/acornreply-com/conformance/acornreply-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acornreply-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/acornreply-com/llms/acornreply-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acornreply-com-llms.txt
- group: other
  href: https://artifacts.apis.io/acornreply-com/hosts/acornreply-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acornreply-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/acornreply-com/vendors/acornreply-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acornreply-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acornreply.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.acornreply.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acornreply.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://acornreply.com/quickstart
- group: auth
  href: https://artifacts.apis.io/acornreply-com/authentication/acornreply-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/acornreply-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/acornreply-com/security/acornreply-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acornreply-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acornreply.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://acornreply.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://acornreply.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://acornreply.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://acornreply.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://acornreply.com/signup
- group: start
  title: ''
  type: Login
  url: https://acornreply.com/signin
- group: company
  title: ''
  type: About
  url: https://acornreply.com/about
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://acornreply.com/api/mcp
  - status: 200
    url: https://acornreply.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: AcornReply provides a support inbox solution for small teams, enabling them to receive customer messages via email, live chat, or API, and reply with AI‑assisted drafts in their own voice. The platform emphasizes simplicity, no ticket numbers, and quick setup, targeting teams of under ten who want to stay hands‑on with customer support.
image: https://acornreply.com/og-image.png?v=84b9ce52
layout: provider
modified: '2026-10-31'
name: AcornReply
nav: Providers
network: true
overview: 'AcornReply is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Support, Software-as-a-Service, Small Teams, Artificial Intelligence, and Customer Service.


  AcornReply''s developer surface includes support, getting-started guide, authentication, documentation, pricing, engineering blog, signup flow, and 12 more developer resources.'
plans:
- name: Acornreply Com Plans Pricing
  plan_count: 3
  slug: acornreply-com-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 33.6
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Acornreply Com Authentication
  slug: acornreply-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Acornreply Com Domain Security
  slug: acornreply-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acornreply-com
tags:
- Support
- Software-as-a-Service
- Small Teams
- Artificial Intelligence
- Customer Service
website: https://acornreply.com/
---
