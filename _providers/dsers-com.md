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
    agent_skills: unknown
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
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for DSers dropshipping automation platform, documented at the integration page.
  name: DSers API
  slug: dsers-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/dsers-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/dsers-com/plans/dsers-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dsers-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/dsers-com/hosts/dsers-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dsers-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dsers-com/vendors/dsers-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dsers-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/dsers-com/packages/dsers-com-packages.yml
  title: ''
  type: SDKs
  url: packages/dsers-com-packages.yml
- group: build
  href: https://artifacts.apis.io/dsers-com/packages/dsers-com-packages.yml
  title: ''
  type: Packages
  url: packages/dsers-com-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dsers
- group: auth
  href: https://artifacts.apis.io/dsers-com/security/dsers-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dsers-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dsers.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dsers.com/en/features
- group: docs
  title: ''
  type: APIReference
  url: https://dsers.com/en/integration
- group: start
  title: ''
  type: GettingStarted
  url: https://dsers.com/en/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.dsers.com/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.dsers.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://dsers.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dsers.com/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dsers.com/en/privacy
coverage:
  detail: Help center pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://help.dsers.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: DSers is an AI‑powered dropshipping automation platform founded in 2018. It connects ecommerce sellers with suppliers across AliExpress, Alibaba, 1688 and its own Agent Network, automating product sourcing, pricing, order fulfillment and tracking. The service offers multi‑store management, bulk price updates, AI‑driven product information optimization, and integrates with Shopify, WooCommerce, Magento and major marketplaces. DSers aims to reduce repetitive operational work, letting merchants focus on growth and creativity.
layout: provider
modified: '2026-11-06'
name: DSers
nav: Providers
network: true
overview: 'DSers is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Dropshipping, Automation, Artificial Intelligence, and Integration.


  DSers'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Dsers Com Plans Pricing
  plan_count: 4
  slug: dsers-com-plans-pricing
random_paper: 21
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 49.3
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dsers Com Domain Security
  slug: dsers-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dsers-com
tags:
- E-Commerce
- Dropshipping
- Automation
- Artificial Intelligence
- Integration
website: https://dsers.com/
---
