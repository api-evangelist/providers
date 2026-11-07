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
api_count: 1
apis:
- description: How Weldforge works — Weldforge
  name: Weldforge API
  slug: weldforge-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/weldforge/plans/weldforge-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/weldforge-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://weldforge.ai/security
- group: design
  href: https://artifacts.apis.io/weldforge/conformance/weldforge-conformance.yml
  title: ''
  type: Conformance
  url: conformance/weldforge-conformance.yml
- group: agent
  href: https://artifacts.apis.io/weldforge/llms/weldforge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/weldforge-llms.txt
- group: other
  href: https://artifacts.apis.io/weldforge/hosts/weldforge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/weldforge-hosts.yml
- group: other
  href: https://artifacts.apis.io/weldforge/vendors/weldforge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/weldforge-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://weldforge.ai/security
- group: auth
  href: https://artifacts.apis.io/weldforge/security/weldforge-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/weldforge-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/weldforge/security/weldforge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weldforge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://weldforge.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://weldforge.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://weldforge.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://weldforge.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://weldforge.ai/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://weldforge.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://weldforge.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://weldforge.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://weldforge.ai/intake
coverage:
  checked: '2026-10-19'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://weldforge.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: Green Dolphin Software provides a no‑code integration platform that builds, runs, and bills custom integrations for SaaS applications on a flat‑fee model. Users can request connections via voice or a short form, and Weldforge automates data flows between systems like Salesforce, HubSpot, Stripe, Snowflake, and more, eliminating the need for in‑house developers or complex middleware. The service emphasizes simplicity, speed, and predictable pricing, targeting businesses seeking to streamline operations without managing integration infrastructure.
image: https://weldforge.ai/og-image.png
layout: provider
modified: '2026-10-19'
name: Green Dolphin Software
nav: Providers
network: true
overview: 'Green Dolphin Software is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, No-Code, Software-as-a-Service, Automation, and Platform.


  Green Dolphin Software''s developer surface includes documentation, pricing, engineering blog, support, signup flow, and 13 more developer resources.'
plans:
- name: Weldforge Plans Pricing
  plan_count: 4
  slug: weldforge-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 64.3
    operational_transparency: 13.2
  previous_composite: 35.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/weldforge/weldforge-2026-11-03T150119.png
security:
- kind: domain-security
  name: Weldforge Domain Security
  slug: weldforge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: trust-center
  name: Weldforge Trust Center
  slug: weldforge-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: weldforge
tags:
- Integration
- No-Code
- Software-as-a-Service
- Automation
- Platform
website: https://weldforge.ai/
---
