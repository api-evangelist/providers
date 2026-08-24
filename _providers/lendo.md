---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Production API host backing the Lendo web and mobile applications. Discovered by probe at https://api.lendo.sa - it is live and returns a structured bilingual (Arabic/English) JSON envelope, but every
  name: Lendo Platform API
  slug: platform-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://lendo.sa
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.lendo.sa/en/help-center
- group: docs
  title: ''
  type: Documentation
  url: https://www.lendo.sa/en/help-center
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.lendo.sa/en/help-center
- group: operate
  title: ''
  type: Support
  url: https://lendo.freshdesk.com/en/support/tickets/new
- group: company
  title: ''
  type: Blog
  url: https://www.lendo.sa/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lendo.sa/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.lendo.sa/register
- group: start
  title: ''
  type: Login
  url: https://app.lendo.sa/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lendo.sa/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lendo.sa/en/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.lendo.sa/
- group: auth
  title: ''
  type: TrustCenter
  url: security/lendo-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lendo-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/lendo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lendo-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lendo-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lendo-domain-security.yml
created: '2026-07-17'
description: Lendo (شركة ليندو السعودية للتمويل) is a Riyadh-based Saudi fintech licensed by the Saudi Central Bank (SAMA, License No. 61/A SH/202203, capital SAR 50M) that operates the Kingdom's first SAMA-licensed Sharia-compliant debt-based crowdfunding platform. Lendo connects small and medium enterprises needing liquidity with retail and institutional investors, offering invoice financing, working capital financing, purchase-order financing and term loans funded within 48 hours of document completion, alongside government-backed programs with Monshaat, SME Bank, the Tourism Development Fund, the Cultural Development Fund, Modon and the Kafala guarantee scheme. On the investor side it runs tiered retail products (Basic, Premium, High Net Worth), an auto-invest engine and an A-D credit scoring engine, reporting SAR 4.5B+ in cumulative financing across 10,000+ funded deals at a 2.93% overall default rate. Lendo publishes no public developer program, API documentation or SDKs; its production
  API host is authentication-gated and its machine-readable public surface is limited to an llms.txt and a SafeBase-hosted trust center.
image: https://cdn.prod.website-files.com/694bacb635847d327e4bb887/6976655d086075b08122ba96_OG%20Image.png
layout: provider
modified: '2026-07-19'
name: Lendo
nav: Providers
network: true
overview: 'Lendo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Lending, and Crowdfunding.


  Lendo''s developer surface includes documentation, support, engineering blog, pricing, signup flow, and 13 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 27.1
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 27.1
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lendo/refs/heads/main/screenshots/lendo-2026-07-25T224908.png
security:
- kind: domain-security
  name: Lendo Domain Security
  slug: lendo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lendo Trust Center
  slug: lendo-trust-center
  summary_line: SAMA CSF
slug: lendo
tags:
- Company
- Financial-Services
- Fintech
- Lending
- Crowdfunding
- Invoice Financing
- SME Finance
- Islamic Finance
- Saudi Arabia
- Middle East
website: https://lendo.sa
---
