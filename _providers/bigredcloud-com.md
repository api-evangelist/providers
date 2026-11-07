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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bigredcloud-com/plans/bigredcloud-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bigredcloud-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bigredcloud-com/llms/bigredcloud-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bigredcloud-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bigredcloud-com/hosts/bigredcloud-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bigredcloud-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/bigredcloud-com/packages/bigredcloud-com-packages.yml
  title: ''
  type: SDKs
  url: packages/bigredcloud-com-packages.yml
- group: build
  href: https://artifacts.apis.io/bigredcloud-com/packages/bigredcloud-com-packages.yml
  title: ''
  type: Packages
  url: packages/bigredcloud-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bigredcloud.com/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: http://bigredcloud.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://bigredcloud.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://bigredcloud.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://bigredcloud.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://bigredcloud.com/docs-category/setup-2
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BigRedCloud
- group: auth
  href: https://artifacts.apis.io/bigredcloud-com/security/bigredcloud-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigredcloud-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bigredcloud.com/
coverage:
  checked: '2026-11-02'
  detail: Documentation is publicly available but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec was found.
  evidence:
  - status: 200
    url: https://bigredcloud.com/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Big Red Cloud provides AI-powered accounting and payroll software, with Turbo Inventory for inventory management and business operations across Ireland and the UK. Their solutions help growing businesses manage finances, people, stock, purchasing, sales and service, delivering an integrated platform for efficient financial and operational management.
image: https://bigredcloud.com/wp-content/uploads/2025/06/BRC-Social-Icon-1.jpg
layout: provider
modified: '2026-11-02'
name: Big Red Cloud
nav: Providers
network: true
overview: 'Big Red Cloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Payroll, Inventory, Artificial Intelligence, and Irish Businesses.


  Big Red Cloud''s developer surface includes support, pricing, documentation, engineering blog, getting-started guide, and 9 more developer resources.'
plans:
- name: Bigredcloud Com Plans Pricing
  plan_count: 1
  slug: bigredcloud-com-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 2.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bigredcloud Com Domain Security
  slug: bigredcloud-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bigredcloud-com
tags:
- Accounting
- Payroll
- Inventory
- Artificial Intelligence
- Irish Businesses
- UK Businesses
- Business Software
website: https://bigredcloud.com/
---
