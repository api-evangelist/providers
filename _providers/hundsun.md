---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: Enterprise trading platform offered to brokerages and securities firms, covering order management, execution, clearing, and back-office settlement. Integration is typically delivered through enterpris
  name: Hundsun Trading Platform
  slug: hundsun-trading-platform
- description: Wealth management platform for banks and wealth managers covering portfolio management, product distribution, customer analytics, and advisor workflows. Integration is delivered as an enterprise produ
  name: Hundsun Wealth Management Platform
  slug: hundsun-wealth-management-platform
- description: Fund management platform supporting fund subscription, redemption, transaction processing, and NAV calculation for asset managers. Delivered as enterprise software for fund companies and custodians.
  name: Hundsun Fund Management Platform
  slug: hundsun-fund-management-platform
artifact_total: 7
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hundsun/refs/heads/main/plans/hundsun-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hundsun-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hundsun/refs/heads/main/rate-limits/hundsun-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hundsun-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hundsun/refs/heads/main/finops/hundsun-finops.yml
  title: ''
  type: FinOps
  url: finops/hundsun-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hundsun.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hundsun/refs/heads/main/security/hundsun-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hundsun-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hundsun
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hundsun
- group: company
  title: ''
  type: Website
  url: https://www.hundsun.com
- group: operate
  title: ''
  type: Support
  url: https://support.hundsun.com
- group: design
  title: ''
  type: Rules
  url: https://raw.githubusercontent.com/api-evangelist/hundsun/refs/heads/main/hundsun-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://www.hundsun.com/llms.txt
created: '2024'
description: Hundsun Technologies Inc. is a leading Chinese fintech company providing software solutions and services for financial institutions including securities, funds, futures, banking, asset management, and wealth management. Hundsun's products are typically delivered as enterprise software with bespoke customer integrations rather than as a public developer API platform.
finops:
- has_sources: false
  method: generated
  name: Hundsun Finops
  primary_unit: ''
  service_category: API
  slug: hundsun-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hundsun.png
layout: provider
modified: '2026-10-06'
name: Hundsun Technologies
nav: Providers
network: true
overview: 'Hundsun Technologies is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Asset Management, Banking Software, China, Financial Technology, and Securities Trading.


  Hundsun Technologies'' developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Hundsun Plans Pricing
  plan_count: 3
  slug: hundsun-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Hundsun Rate Limits
  slug: hundsun-rate-limits
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 69.6
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hundsun Domain Security
  slug: hundsun-domain-security
  summary_line: TLSv1.3 · HSTS
slug: hundsun
tags:
- Asset Management
- Banking Software
- China
- Financial Technology
- Securities Trading
website: https://www.hundsun.com
---
