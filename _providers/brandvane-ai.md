---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
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
  score: 17.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/brandvane-ai/plans/brandvane-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brandvane-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/brandvane-ai/conventions/brandvane-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/brandvane-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/brandvane-ai/conventions/brandvane-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/brandvane-ai-conventions.yml
- group: agent
  href: https://artifacts.apis.io/brandvane-ai/well-known/brandvane-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brandvane-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/brandvane-ai/hosts/brandvane-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brandvane-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/brandvane-ai/vendors/brandvane-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brandvane-ai-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://brandvane.ai/connect/codex/
- group: auth
  href: https://artifacts.apis.io/brandvane-ai/security/brandvane-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brandvane-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandvane.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://brandvane.ai/pricing/
- group: company
  title: ''
  type: Blog
  url: https://brandvane.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brandvane.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brandvane.ai/privacy/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.brandvane.ai/mcp
  - status: 200
    url: https://brandvane.ai/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: BrandVane provides AI‑driven SEO research tools that let small businesses and agencies discover keywords, compare competitors, and plan content directly within AI assistants like ChatGPT, Claude, or Codex. Their platform offers transparent pricing starting at $29/month, with cost estimates shown before each run, and integrates free tools and paid plans to enhance visibility and content strategy.
image: https://brandvane.ai/og-default.png
layout: provider
modified: '2026-11-02'
name: BrandVane
nav: Providers
network: true
overview: 'BrandVane is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SEO, Artificial Intelligence, Marketing, and Tools.


  BrandVane''s developer surface includes getting-started guide, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Brandvane Ai Plans Pricing
  plan_count: 5
  slug: brandvane-ai-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brandvane Ai Domain Security
  slug: brandvane-ai-domain-security
  summary_line: TLSv1.3
slug: brandvane-ai
tags:
- Company
- SEO
- Artificial Intelligence
- Marketing
- Tools
- Small Business
website: https://brandvane.ai/
---
