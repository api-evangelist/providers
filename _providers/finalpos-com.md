---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
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
    auth_clarity: bearer
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/finalpos-com/plans/finalpos-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/finalpos-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/finalpos-com/authentication/finalpos-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/finalpos-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/finalpos-com/conformance/finalpos-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/finalpos-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/finalpos-com/llms/finalpos-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/finalpos-com-llms.txt
- group: other
  href: https://artifacts.apis.io/finalpos-com/hosts/finalpos-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finalpos-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/finalpos-com/vendors/finalpos-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/finalpos-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://finalpos.com/release-notes
- group: auth
  href: https://artifacts.apis.io/finalpos-com/security/finalpos-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finalpos-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finalpos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://finalpos.com/docs
- group: company
  title: ''
  type: Blog
  url: https://finalpos.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://finalpos.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://finalpos.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://finalpos.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finalpos.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finalpos.com/legal/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://finalpos.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Final POS provides customizable point-of-sale systems, kiosks, and mobile checkout solutions for merchants and resellers. Their platform offers a checkout OS, hardware integration, FinAI tools, and APIs for building apps and extensions, aiming to streamline in‑person commerce across various business sizes.
image: https://finalpos.com/opengraph-image
layout: provider
modified: '2026-10-30'
name: finalpos-com
nav: Providers
network: true
overview: 'finalpos-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Point-of-Sale, Retail, Payments, and Fintech.


  finalpos-com''s developer surface includes authentication, changelog, documentation, engineering blog, pricing, getting-started guide, support, and 9 more developer resources.'
plans:
- name: Finalpos Com Plans Pricing
  plan_count: 4
  slug: finalpos-com-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 55.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/finalpos-com/finalpos-com-2026-11-03T132010.png
security:
- kind: authentication
  name: Finalpos Com Authentication
  slug: finalpos-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Finalpos Com Domain Security
  slug: finalpos-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finalpos-com
tags:
- Company
- Point-of-Sale
- Retail
- Payments
- Fintech
website: https://finalpos.com/
---
