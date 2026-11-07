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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agently provides an AI Work OS API documented at https://agently.dev/docs/mcp-authentication
  name: Agently API
  slug: agently-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/agently-dev/plans/agently-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agently-dev-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/agently-dev/authentication/agently-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agently-dev-authentication.yml
- group: agent
  href: https://artifacts.apis.io/agently-dev/llms/agently-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agently-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/agently-dev/well-known/agently-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agently-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/agently-dev/hosts/agently-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agently-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agently-dev/vendors/agently-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agently-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agently.dev/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://agently.dev/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agently.dev/privacy-policy
- group: auth
  href: https://artifacts.apis.io/agently-dev/security/agently-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agently-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agently.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://agently.dev/docs/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://agently.dev/docs/brain
- group: commercial
  title: ''
  type: Pricing
  url: https://agently.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://agently.dev/blog
- group: operate
  title: ''
  type: Changelog
  url: https://agently.dev/changelog
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are HTML without a machine‑readable OpenAPI or other contract, and no spec could be discovered despite probing known locations.
  evidence:
  - status: 404
    url: https://agently.dev/openapi.json
  - status: 404
    url: https://api.agently.dev/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Agently is an AI Work OS that acts as a chief of staff for companies, learning from connected tools to automate tasks like drafting replies, chasing invoices, and managing deals. It offers a free tier and a Pro plan at $99/month with credits, storage, and team members, ensuring data is encrypted in transit and at rest, never used to train models.
image: https://agently.dev/assets/og.png
layout: provider
modified: '2026-11-01'
name: Agently
nav: Providers
network: true
overview: 'Agently is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Productivity, Software-as-a-Service, and Chief of Staff.


  Agently''s developer surface includes authentication, support, documentation, getting-started guide, pricing, engineering blog, changelog, and 9 more developer resources.'
plans:
- name: Agently Dev Plans Pricing
  plan_count: 2
  slug: agently-dev-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 0.0
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
security:
- kind: authentication
  name: Agently Dev Authentication
  slug: agently-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agently Dev Domain Security
  slug: agently-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agently-dev
tags:
- Artificial Intelligence
- Automation
- Productivity
- Software-as-a-Service
- Chief of Staff
website: https://agently.dev/
---
