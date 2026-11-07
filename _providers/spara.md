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
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Spara platform providing sales automation and AI‑powered workflow capabilities.
  name: Spara API
  slug: spara-api
artifact_total: 4
asyncapis:
- description: ''
  name: Spara Webhooks
  slug: spara-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/spara/plans/spara-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/spara-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/spara/asyncapi/spara-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/spara-webhooks.yml
- group: design
  href: https://artifacts.apis.io/spara/conformance/spara-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spara-conformance.yml
- group: agent
  href: https://artifacts.apis.io/spara/llms/spara-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spara-llms.txt
- group: agent
  href: https://artifacts.apis.io/spara/well-known/spara-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spara-well-known.yml
- group: other
  href: https://artifacts.apis.io/spara/hosts/spara-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spara-hosts.yml
- group: other
  href: https://artifacts.apis.io/spara/vendors/spara-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spara-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.spara.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spara.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spara.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.spara.com/press
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spara.com/guides/installation-guides/readme
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.spara.com
- group: auth
  href: https://artifacts.apis.io/spara/security/spara-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spara-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spara.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spara.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spara.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.spara.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.spara.com/contact-sales
coverage:
  checked: '2026-10-29'
  detail: Provider's API documentation is served as a JavaScript‑rendered site, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://api.spara.co/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Spara is a platform for agent‑led growth, providing AI‑powered sales automation tools that help teams capture inbound leads, run demos, and automate multi‑step workflows across chat, email, voice, and text. The solution includes AI chat, product demos, voice AI, and analytics, targeting businesses from lean startups to enterprises. Spara emphasizes security with SOC‑2 compliance and offers integrations with CRM, calendar, and analytics platforms.
image: https://a-us.storyblok.com/f/1022990/1200x630/4f570343c0/og-image.png
layout: provider
modified: '2026-10-29'
name: Spara
nav: Providers
network: true
overview: 'Spara is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Artificial Intelligence, Sales Automation, and AgentLedGrowth.


  The Spara catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spara''s developer surface includes getting-started guide, documentation, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Spara Plans Pricing
  plan_count: 2
  slug: spara-plans-pricing
random_paper: 7
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 40.8
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 19.0
    discoverability: 65.2
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 41.1
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/spara/spara-2026-11-03T143612.png
security:
- kind: domain-security
  name: Spara Domain Security
  slug: spara-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spara
tags:
- Company
- Software-as-a-Service
- Artificial Intelligence
- Sales Automation
- AgentLedGrowth
- CRM Integration
website: https://www.spara.co
---
