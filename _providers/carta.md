---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
  pricing: free
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Enables incorporation partners and law firms to programmatically onboard new companies onto the Carta platform, streamlining the company formation and cap table initialisation workflow.
  name: Carta Launch API
  slug: launch-api
- description: Permits fund operators to retrieve cap table summaries and portfolio position data for their holdings, enabling downstream analytics, reporting, and portfolio management workflows.
  name: Carta Investor API
  slug: investor-api
- description: Allows law firms and technology partners to retrieve cap table data on behalf of companies, supporting legal workflows, equity issuance, and 409A valuation processes.
  name: Carta Issuer API
  slug: issuer-api
- description: Enables personal finance and wealth management platforms to aggregate equity holdings data for individuals, supporting estate planning, tax preparation, option financing, and underwriting use cases.
  name: Carta Portfolio API
  slug: portfolio-api
- description: Facilitates deal and fundraising relationship management across investment processes for fund operators, providing structured access to CRM data within the Carta platform.
  name: Carta CRM API
  slug: crm-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/carta-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carta.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.carta.com/api-platform/docs/introduction
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/carta
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carta--
- group: company
  title: ''
  type: Blog
  url: https://carta.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://carta.com/plans/pricing-for-investors/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.carta.com
- group: other
  title: ''
  type: X
  url: https://x.com/cartainc
- group: commercial
  title: ''
  type: Plans
  url: plans/carta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/carta-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/carta-finops.yml
created: '2026-06-13'
description: Carta is an equity management platform offering a REST API for cap table management, 409A valuations, fund administration, employee equity plans, and investor portfolio management. Carta's Developer Platform exposes four API suites — Launch, Investor, Issuer, and Portfolio — authenticated via OAuth 2.0 (Authorization Code and Client Credentials flows). Partner access is invite-only and requires SOC 2 Type 2 certification; Carta customers may request access to their own data on demand. A mock API environment at mock-api.carta.com is provided for sandbox development.
finops:
- name: Carta Finops
  service_category: ''
  slug: carta-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carta.png
jsonld:
- class_count: 10
  name: Carta Context
  property_count: 0
  slug: carta-context
layout: provider
modified: '2026-06-13'
name: Carta
nav: Providers
network: true
overview: 'Carta publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Equity Management, Cap Table, 409A Valuations, Fund Administration, and Employee Equity.


  The Carta catalog on APIs.io includes 1 JSON-LD context.


  Carta''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Carta Plans Pricing
  plan_count: 3
  slug: carta-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 0
  name: Carta Rate Limits
  slug: carta-rate-limits
score:
  band: emerging
  composite: 27.1
  delta: -3.2
  facets:
    commercial_clarity: 57.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carta/refs/heads/main/screenshots/carta-2026-06-20T174019.png
security:
- kind: domain-security
  name: Carta Domain Security
  slug: carta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Carta Trust Center
  slug: carta-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: carta
tags:
- Equity Management
- Cap Table
- 409A Valuations
- Fund Administration
- Employee Equity
- Investor Portfolio
- Private Markets
- FinTech
website: https://carta.com
---
