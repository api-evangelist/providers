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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for the Pinafly review platform.
  name: Pinafly API
  slug: pinafly-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/pinafly-com/plans/pinafly-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pinafly-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/pinafly-com/well-known/pinafly-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pinafly-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/pinafly-com/hosts/pinafly-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pinafly-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/pinafly-com/security/pinafly-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pinafly-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pinafly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pinafly.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://pinafly.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://pinafly.com/docs/agents/connect-your-agent
- group: operate
  title: ''
  type: Support
  url: https://pinafly.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://pinafly.com/pricing
- group: other
  title: ''
  type: SignIn
  url: https://pinafly.com/session/new
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pinafly.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pinafly.com/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation is delivered as a JavaScript‑rendered single‑page app, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://pinafly.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Pinafly provides a platform for website and web app reviews, enabling teams to gather consolidated feedback on real pages. Users can give precise, AI‑assisted feedback to improve products. The service is free to start and does not require an account for reviewers, focusing on collaborative evaluation and AI‑driven insights for developers and product teams.
image: https://pinafly.com/og.png
layout: provider
modified: '2026-10-30'
name: pinafly-com
nav: Providers
network: true
overview: 'pinafly-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Review, Artificial Intelligence, Collaboration, Feedback, and Web App.


  pinafly-com''s developer surface includes documentation, API reference, getting-started guide, support, pricing, and 8 more developer resources.'
plans:
- name: Pinafly Com Plans Pricing
  plan_count: 3
  slug: pinafly-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Pinafly Com Rate Limits
  slug: pinafly-com-rate-limits
scopes:
- name: Pinafly Com Scopes
  scope_count: 0
  slug: pinafly-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pinafly-com/pinafly-com-2026-11-03T141218.png
security:
- kind: authentication
  name: Pinafly Com Authentication
  slug: pinafly-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pinafly Com Domain Security
  slug: pinafly-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pinafly-com
tags:
- Review
- Artificial Intelligence
- Collaboration
- Feedback
- Web App
website: https://pinafly.com/
---
