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
    dynamic_client_registration: true
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
  score: 18.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/claris/vendors/claris-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claris-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/claris/plans/claris-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/claris-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/claris/llms/claris-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claris-llms.txt
- group: agent
  href: https://artifacts.apis.io/claris/well-known/claris-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claris-well-known.yml
- group: other
  href: https://artifacts.apis.io/claris/hosts/claris-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claris-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.claris.com/company/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://www.claris.com/company/legal/security/
- group: build
  title: ''
  type: SDKs
  url: https://downloads.claris.com/DEVREL/sdk/fm_plugin_sdk_26.0.3.307.zip
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.claris.com/company/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.claris.com/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.claris.com/filemaker/whats-new/
- group: company
  title: ''
  type: Blog
  url: https://www.claris.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.claris.com/
- group: auth
  href: https://artifacts.apis.io/claris/security/claris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claris.com/
coverage:
  checked: '2026-10-20'
  detail: Claris provides no public developer portal or API documentation on its website.
  evidence:
  - status: 200
    url: https://www.claris.com
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Claris is a software company that provides a suite of low-code and no-code tools, including FileMaker, Claris Connect, and Claris Platform, enabling businesses to build custom applications, automate workflows, and integrate systems. The company focuses on empowering users to create powerful solutions without extensive coding, offering cloud and on-premises options, extensive documentation, and a developer community.
image: https://www.claris.com/site/images/og_claris.jpg
layout: provider
modified: '2026-10-20'
name: Claris
nav: Providers
network: true
overview: 'Claris is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Low-Code, No-Code, Automation, and Integration.


  Claris'' developer surface includes pricing, changelog, engineering blog, documentation, and 11 more developer resources.'
plans:
- name: Claris Plans Pricing
  plan_count: 3
  slug: claris-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 55.4
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/claris/claris-2026-11-03T124309.png
security:
- kind: domain-security
  name: Claris Domain Security
  slug: claris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: claris
tags:
- Company
- Low-Code
- No-Code
- Automation
- Integration
website: https://claris.com/
---
