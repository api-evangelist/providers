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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 6.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/caribooks-com/plans/caribooks-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/caribooks-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/caribooks-com/llms/caribooks-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caribooks-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/caribooks-com/well-known/caribooks-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caribooks-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/caribooks-com/hosts/caribooks-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caribooks-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/caribooks-com/vendors/caribooks-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caribooks-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://caribooks.com/en/terms
- group: operate
  title: ''
  type: Support
  url: https://caribooks.com/en/help
- group: auth
  title: ''
  type: Security
  url: https://caribooks.com/en/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caribooks.com/en/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://caribooks.com/en/pricing
- group: start
  title: ''
  type: Login
  url: https://caribooks.com/en/login
- group: docs
  title: ''
  type: Documentation
  url: https://caribooks.com/en/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://caribooks.com/en/setup
- group: auth
  href: https://artifacts.apis.io/caribooks-com/security/caribooks-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caribooks-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caribooks.com/
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are rendered via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://caribooks.com/en/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Caribooks provides AI-powered conversational access to QuickBooks data, enabling users to ask accounting questions in natural language, generate invoices, and retrieve financial reports. The service integrates with Claude, ChatGPT, and Microsoft Copilot, and offers tiered pricing for companies of various sizes.
image: https://caribooks.com/og-en.jpg
layout: provider
modified: '2026-11-03'
name: Peich Technologies Inc.
nav: Providers
network: true
overview: 'Peich Technologies Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Artificial Intelligence, Integration, QuickBooks, and Software-as-a-Service.


  Peich Technologies Inc.''s developer surface includes support, pricing, documentation, getting-started guide, and 11 more developer resources.'
plans:
- name: Caribooks Com Plans Pricing
  plan_count: 4
  slug: caribooks-com-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caribooks Com Domain Security
  slug: caribooks-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: caribooks-com
tags:
- Accounting
- Artificial Intelligence
- Integration
- QuickBooks
- Software-as-a-Service
website: https://caribooks.com/
---
