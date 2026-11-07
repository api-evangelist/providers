---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Juma, by Juma Labs, runs AI marketing flows end‑to‑end: ads reports, SEO articles, carousels and campaign briefs. Free to start.'
  name: Juma
  slug: juma
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/juma/plans/juma-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/juma-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/juma/llms/juma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/juma-llms.txt
- group: agent
  href: https://artifacts.apis.io/juma/well-known/juma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/juma-well-known.yml
- group: other
  href: https://artifacts.apis.io/juma/hosts/juma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/juma-hosts.yml
- group: other
  href: https://artifacts.apis.io/juma/vendors/juma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/juma-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://juma.ai/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.juma.ai/
- group: auth
  href: https://artifacts.apis.io/juma/security/juma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/juma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://juma.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://juma.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://juma.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://juma.ai/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://juma.ai/privacy-security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://juma.ai/mcp
coverage:
  checked: '2026-10-29'
  detail: Juma's website provides marketing product information but no public machine‑readable API specification.
  evidence:
  - status: 200
    url: https://juma.ai
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Juma provides AI-powered marketing automation for agencies and marketing teams, delivering end‑to‑end AI marketing flows that generate ads, reports, SEO articles, carousel creatives, and campaign briefs. The platform integrates with popular advertising and analytics tools, enabling users to create, optimize, and track campaigns with minimal manual effort. Juma offers a free‑to‑start tier and a paid SaaS model, targeting marketers who want to leverage generative AI to accelerate content creation and improve performance.
image: https://cdn.prod.website-files.com/690c991817868d8bdc640108/6a0173c46c1d82da4bc9fbd3_OG%20image.png
layout: provider
modified: '2026-10-29'
name: Juma
nav: Providers
network: true
overview: 'Juma is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Marketing, Automation, and Software-as-a-Service.


  Juma''s developer surface includes pricing, engineering blog, support, and 11 more developer resources.'
plans:
- name: Juma Plans Pricing
  plan_count: 9
  slug: juma-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Juma Rate Limits
  slug: juma-rate-limits
scopes:
- name: Juma Scopes
  scope_count: 0
  slug: juma-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 64.3
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.3
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
screenshot: https://apis.io/screenshots/juma/juma-2026-11-03T134242.png
security:
- kind: authentication
  name: Juma Authentication
  slug: juma-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Juma Domain Security
  slug: juma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: juma
tags:
- Company
- Artificial Intelligence
- Marketing
- Automation
- Software-as-a-Service
- Advertising
website: https://juma.ai
---
