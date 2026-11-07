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
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bit-integrations/plans/bit-integrations-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bit-integrations-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bit-integrations/llms/bit-integrations-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bit-integrations-llms.txt
- group: agent
  href: https://artifacts.apis.io/bit-integrations/well-known/bit-integrations-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bit-integrations-well-known.yml
- group: other
  href: https://artifacts.apis.io/bit-integrations/hosts/bit-integrations-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bit-integrations-hosts.yml
- group: other
  href: https://artifacts.apis.io/bit-integrations/vendors/bit-integrations-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bit-integrations-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bit-integrations.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bit-integrations.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/bit-integrations/security/bit-integrations-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bit-integrations-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bit-integrations.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bit-integrations.com/wp-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://bit-integrations.com/wp-docs/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://bit-integrations.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://bit-integrations.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://forum.bitapps.pro/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://bit-integrations.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Bit Apps provides a WordPress automation plugin suite that connects WordPress sites to over 335 platforms, enabling easy automation of forms, CRM, social media, and AI workflows. Their products include Bit Form, Bit Assist, Bit Flows, and Bit Integrations, offering features like drag‑and‑drop form building, multi‑channel customer engagement, and advanced AI workflow design. The platform targets agencies and businesses seeking to streamline integrations and automate marketing, sales, and support processes.
image: https://bit-integrations.com/wp-content/uploads/2026/02/Bit-Integrations-Preview.png
layout: provider
modified: '2026-10-20'
name: Bit Apps
nav: Providers
network: true
overview: 'Bit Apps is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, WordPress, Integration, and Artificial Intelligence.


  Bit Apps'' developer surface includes documentation, getting-started guide, engineering blog, pricing, support, and 9 more developer resources.'
plans:
- name: Bit Integrations Plans Pricing
  plan_count: 4
  slug: bit-integrations-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.4
  provenance:
    conformance: unknown
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
screenshot: https://apis.io/screenshots/bit-integrations/bit-integrations-2026-11-03T121759.png
security:
- kind: domain-security
  name: Bit Integrations Domain Security
  slug: bit-integrations-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bit-integrations
tags:
- Company
- Automation
- WordPress
- Integration
- Artificial Intelligence
website: https://bit-integrations.com/
---
