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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
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
- group: auth
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
- name: Hundsun Finops
  service_category: API
  slug: hundsun-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hundsun.png
layout: provider
modified: '2026-04-28'
name: Hundsun Technologies
nav: Providers
network: true
overview: 'Hundsun Technologies publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Asset Management, Banking Software, China, Financial Technology, and Securities Trading.


  Hundsun Technologies'' developer surface includes support and 6 more developer resources.'
plans:
- name: Hundsun Plans Pricing
  plan_count: 3
  slug: hundsun-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Hundsun Rate Limits
  slug: hundsun-rate-limits
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
