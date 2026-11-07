---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Aztra provides a project delivery operations platform with API access for integration.
  name: Aztra API
  slug: aztra-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/aztra-my/plans/aztra-my-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aztra-my-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aztra-my/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/aztra-my/well-known/aztra-my-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aztra-my-well-known.yml
- group: other
  href: https://artifacts.apis.io/aztra-my/hosts/aztra-my-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aztra-my-hosts.yml
- group: other
  href: https://artifacts.apis.io/aztra-my/vendors/aztra-my-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aztra-my-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://aztra.my/sign-in
- group: docs
  title: ''
  type: APIReference
  url: https://aztra.my/docs/reference/faq
- group: auth
  href: https://artifacts.apis.io/aztra-my/security/aztra-my-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aztra-my-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aztra.my/
- group: docs
  title: ''
  type: Documentation
  url: https://aztra.my/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://aztra.my/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://aztra.my/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aztra.my/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aztra.my/privacy
- group: operate
  title: ''
  type: Support
  url: https://aztra.my/contact
coverage:
  checked: '2026-11-02'
  detail: OAuth protected resource requires authentication for API access.
  evidence:
  - status: 200
    url: https://aztra.my/.well-known/oauth-protected-resource
  reason: auth-required
  state: gated
created: '2026-11-02'
description: Aztra is a Project Delivery Operations Platform that connects customer demand, engineering capacity, delivery progress, and cost, enabling delivery leaders to see risks, expenses, and impact, and to adjust plans before escalations occur. The platform supports capacity planning, risk management, and portfolio visibility for both agile and waterfall methodologies.
image: https://aztra.my/og-landing.png
layout: provider
modified: '2026-11-02'
name: Aztra
nav: Providers
network: true
overview: 'Aztra is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Project Delivery, Capacity-Planning, Risk Management, and Portfolio Management.


  Aztra''s developer surface includes API reference, documentation, getting-started guide, pricing, support, and 10 more developer resources.'
plans:
- name: Aztra My Plans Pricing
  plan_count: 5
  slug: aztra-my-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Aztra My Rate Limits
  slug: aztra-my-rate-limits
scopes:
- name: Aztra My Scopes
  scope_count: 0
  slug: aztra-my-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.1
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 31.1
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aztra My Authentication
  slug: aztra-my-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aztra My Domain Security
  slug: aztra-my-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aztra-my
tags:
- Project Delivery
- Capacity-Planning
- Risk Management
- Portfolio Management
website: https://aztra.my/
---
