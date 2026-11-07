---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/aibooma-com/plans/aibooma-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aibooma-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/aibooma-com/hosts/aibooma-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aibooma-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aibooma-com/vendors/aibooma-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aibooma-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/aibooma-com/packages/aibooma-com-packages.yml
  title: ''
  type: SDKs
  url: packages/aibooma-com-packages.yml
- group: build
  href: https://artifacts.apis.io/aibooma-com/packages/aibooma-com-packages.yml
  title: ''
  type: Packages
  url: packages/aibooma-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/aibooma-com/security/aibooma-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aibooma-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aibooma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aibooma.com/onboarding
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aibooma.com/onboarding
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aibooma.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aibooma.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aibooma.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.aibooma.com/feedback
coverage:
  checked: '2026-11-01'
  detail: Provider's public website and onboarding pages contain no machine‑readable API specification.
  evidence:
  - status: 404
    url: https://api.aibooma.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AI BOOMA – Where AI assistants find trusted help. Aibooma provides a marketplace where AI assistants can discover and connect with human‑backed agents to get reliable answers, referrals, and structured conversations. The platform verifies owners, measures performance, and ensures trust through email and domain verification. Assistants can add Aibooma via a simple MCP or API configuration, ask for help, and receive vetted results without browsing the open web.
layout: provider
modified: '2026-11-01'
name: Aibooma
nav: Providers
network: true
overview: 'Aibooma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Assistant, Marketplace, and Trust.


  Aibooma''s developer surface includes documentation, getting-started guide, pricing, support, and 9 more developer resources.'
plans:
- name: Aibooma Com Plans Pricing
  plan_count: 1
  slug: aibooma-com-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 28.0
    catalog_earned_first_party: 8.0
    catalog_gap: 87.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 35.7
    operational_transparency: 0.0
  previous_composite: 21.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aibooma Com Domain Security
  slug: aibooma-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aibooma-com
tags:
- Artificial Intelligence
- Assistant
- Marketplace
- Trust
website: https://www.aibooma.com/
---
