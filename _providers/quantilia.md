---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quantilia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quantilia.com/
- group: company
  title: ''
  type: Blog
  url: https://www.quantilia.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.quantilia.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.quantilia.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.quantilia.com/book-a-demo/
- group: start
  title: ''
  type: Login
  url: https://app.quantilia.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quantilia.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quantilia.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quantilia/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.quantilia.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quantilia-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/quantilia-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/quantilia-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/quantilia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quantilia-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/quantilia-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quantilia-llms.txt
coverage:
  checked: '2026-08-17'
  detail: Quantilia markets API delivery ("Output as files, dashboards, or API feeds for downstream systems") and runs a live API host at api.quantilia.com, but that host answers HTTP 403 Forbidden from nginx to every unauthenticated request including "/", and the 48-page public sitemap contains no developer portal, API reference or specification of any kind — the contract is only reachable with a signed client agreement.
  evidence:
  - status: 403
    url: https://api.quantilia.com/
  - status: 404
    url: https://www.quantilia.com/openapi.json
  - status: 403
    url: https://www.quantilia.com/.well-known/security.txt
  - status: 200
    url: https://www.quantilia.com/sitemap_index.xml
  reason: customer-only-docs
  state: gated
created: '2026-08-17'
description: Quantilia is a Nice, France based financial data and portfolio reporting platform for institutional investors, family offices, asset managers, private banks, insurance companies and corporates and endowments. It aggregates fragmented investment data from custodian banks, fund administrators, fund managers, private equity and real estate GPs, ESG score providers and benchmark vendors such as MSCI and Bloomberg, then extracts, tests, categorizes, standardizes, labels, enriches and controls it into a single auditable reporting layer with full financial data lineage. Products cover tailored portfolio monitoring, multi-source data aggregation, security-level and private equity lookthrough, structured products monitoring, ESG and risk reports, quantitative analysis, document generation and AI services, with regulatory output for Solvency II, QRT, COREP, CRR3, SFDR, PAI and LEC29. Delivery is via dashboards, report packs, Excel, PDF and API feeds. The company states ISO-27001 certification,
  GDPR and DORA compliance, and EU/Swiss based hosting. No public developer portal, API reference or machine-readable specification is published; the API surface is delivered to contracted clients.
image: https://www.quantilia.com/wp-content/uploads/2026/05/og_quantilia_en.png
layout: provider
modified: '2026-08-17'
name: Quantilia
nav: Providers
network: true
overview: 'Quantilia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Data, Financial Data, Portfolio Reporting, and Investment Management.


  Quantilia''s developer surface includes engineering blog, support, signup flow, and 15 more developer resources.'
plans:
- name: Quantilia Plans Pricing
  plan_count: 0
  slug: quantilia-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Quantilia Rate Limits
  slug: quantilia-rate-limits
score:
  band: emerging
  composite: 17.8
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: domain-security
  name: Quantilia Domain Security
  slug: quantilia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quantilia
tags:
- Company
- Ai Data
- Financial Data
- Portfolio Reporting
- Investment Management
- Asset Management
- Risk Analytics
- ESG
- Private Markets
- Regulatory Reporting
- Data Aggregation
- France
website: https://www.quantilia.com/
---
