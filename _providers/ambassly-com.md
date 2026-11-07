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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Ambassly Com Webhooks
  slug: ambassly-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/ambassly-com/plans/ambassly-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ambassly-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ambassly-com/asyncapi/ambassly-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ambassly-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/ambassly-com/conventions/ambassly-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ambassly-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/ambassly-com/conventions/ambassly-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ambassly-com-conventions.yml
- group: agent
  href: https://artifacts.apis.io/ambassly-com/llms/ambassly-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ambassly-com-llms.txt
- group: other
  href: https://artifacts.apis.io/ambassly-com/hosts/ambassly-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ambassly-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ambassly-com/vendors/ambassly-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ambassly-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://ambassly.com/docs/webhook-setup
- group: auth
  href: https://artifacts.apis.io/ambassly-com/security/ambassly-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ambassly-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ambassly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ambassly.com/docs
- group: company
  title: ''
  type: Blog
  url: https://ambassly.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ambassly.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://ambassly.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ambassly.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ambassly.com/privacy
coverage:
  checked: '2026-11-01'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://ambassly.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Ambassly provides affiliate management software for SaaS and developer tools, enabling creators to track referrals, commissions, and payouts with a full audit trail. The platform offers per‑content links, customizable commission structures, and no revenue caps, helping businesses grow through trusted affiliate programs.
image: https://ambassly.com/og.png
layout: provider
modified: '2026-11-01'
name: Ambassly
nav: Providers
network: true
overview: 'Ambassly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Affiliates, Software-as-a-Service, Marketing, Software, and Platform.


  The Ambassly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ambassly''s developer surface includes getting-started guide, documentation, engineering blog, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Ambassly Com Plans Pricing
  plan_count: 3
  slug: ambassly-com-plans-pricing
random_paper: 0
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 35.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ambassly Com Domain Security
  slug: ambassly-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ambassly-com
tags:
- Affiliates
- Software-as-a-Service
- Marketing
- Software
- Platform
website: https://ambassly.com/
---
