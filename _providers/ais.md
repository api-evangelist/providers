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
api_count: 1
apis:
- description: 'The AIS Client Portal is the secure area where financial advisors and individual investors reach AIS statements, performance reporting and account documents. Probed 2026-08-30: clients.aisgroup.com is'
  name: AIS Client Portal
  slug: ais-client-portal
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ais-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ais-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.aisgroup.com
- group: operate
  title: ''
  type: Contact
  url: https://www.aisgroup.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aisgroup.com/privacy-policy
coverage:
  checked: '2026-08-30'
  detail: AIS Capital Management, L.P. is a registered investment manager whose product is a managed global-macro program, not software — the Drupal marketing site has no developer, docs or API path, and the one "portal" in the profile is a white-labeled Onehub workspace that redirects to ws.onehub.com/signin, so the only API in reach belongs to a vendor rather than to AIS.
  evidence:
  - status: 404
    url: https://www.aisgroup.com/developers
  - status: 404
    url: https://www.aisgroup.com/openapi.json
  - status: 404
    url: https://www.aisgroup.com/.well-known/api-catalog
  - status: 404
    url: https://clients.aisgroup.com/.well-known/agent-card.json
  - status: 200
    url: https://www.aisgroup.com/api
  - status: 200
    url: https://www.aisgroup.com/
  reason: not-a-software-company
  state: none
created: '2025-01-01'
description: 'AIS Group — trading as AIS Capital Management, L.P., where AIS stands for "Applied Intelligence Strategies" — is an investment management firm running absolute-return, global macro programs for financial advisors and individual investors. It combines discretionary macroeconomic and intermarket research (the Multi-Asset Allocation Portfolio family) with systematic, shorter-horizon models (the Frontera programs), trading only liquid instruments listed on major exchanges and describing its methodology as transparent rather than black-box. The firm is an investment manager rather than a software vendor: it publishes no public API, no developer program and no machine-readable contract, and its client portal is a licensed third-party workspace rather than software it operates.'
features:
- description: Quantitative analysis across commodity, currency, equity, and fixed-income markets to identify investment opportunities.
  name: Global Investment Analytics
- description: Investment strategies designed to provide diversifying return streams with low correlations to traditional and alternative investments.
  name: Non-Correlated Strategies
- description: Independent macroeconomic and intermarket analysis supporting tactical asset allocation and risk management decisions.
  name: Macroeconomic Research
- description: Comprehensive portfolio reporting and performance analytics accessible via the secure client portal.
  name: Client Portfolio Reporting
- description: Risk-adjusted return analysis and portfolio risk metrics to support investment decision-making.
  name: Risk Management Analytics
finops:
- name: Ais Finops
  service_category: API
  slug: ais-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ais.png
layout: provider
modified: '2026-08-30'
name: AIS Group
nav: Providers
network: true
overview: AIS Group publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Finance, Global Macro, Investment Analytics, and Investment Management.
plans:
- name: Ais Plans Pricing
  plan_count: 0
  slug: ais-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Ais Rate Limits
  slug: ais-rate-limits
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -2.7
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ais/refs/heads/main/screenshots/ais-2026-06-20T171439.png
security:
- kind: domain-security
  name: Ais Domain Security
  slug: ais-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ais
tags:
- Analytics
- Finance
- Global Macro
- Investment Analytics
- Investment Management
- Risk Management
use_cases:
- description: Financial advisors use AIS analytics to identify non-correlated investment strategies that reduce portfolio concentration risk.
  name: Portfolio Diversification
- description: Institutional investors leverage AIS macroeconomic research to inform tactical shifts across asset classes.
  name: Tactical Asset Allocation
- description: Investment professionals access AIS quantitative models to evaluate alternative and global investment opportunities.
  name: Alternative Investment Research
- description: Clients use the portal's reporting tools to benchmark portfolio performance against relevant indices and peer groups.
  name: Performance Benchmarking
website: https://www.aisgroup.com
---
