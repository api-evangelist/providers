---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Pie Insurance Agentic Access
  operation_count: 11
  slug: pie-insurance-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 7
apis:
- description: The Appetite API from Pie Insurance — 1 operation(s) for appetite.
  name: Pie Insurance Appetite API
  slug: pie-insurance-appetite-api
- description: The ClassCodeSearch API from Pie Insurance — 1 operation(s) for classcodesearch.
  name: Pie Insurance ClassCodeSearch API
  slug: pie-insurance-classcodesearch-api
- description: The Eligibility API from Pie Insurance — 1 operation(s) for eligibility.
  name: Pie Insurance Eligibility API
  slug: pie-insurance-eligibility-api
- description: The PriceIndication API from Pie Insurance — 2 operation(s) for priceindication.
  name: Pie Insurance PriceIndication API
  slug: pie-insurance-priceindication-api
- description: The QuoteDocument API from Pie Insurance — 1 operation(s) for quotedocument.
  name: Pie Insurance QuoteDocument API
  slug: pie-insurance-quotedocument-api
- description: The QuotePdf API from Pie Insurance — 1 operation(s) for quotepdf.
  name: Pie Insurance QuotePdf API
  slug: pie-insurance-quotepdf-api
- description: The Quotes API from Pie Insurance — 2 operation(s) for quotes.
  name: Pie Insurance Quotes API
  slug: pie-insurance-quotes-api
artifact_total: 24
collections:
- collection_type: open
  name: Pie Insurance Quote Api
  slug: open-pie-insurance-partner-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pie-insurance-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pie-insurance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pie-insurance-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.pieinsurance.com
- group: start
  title: ''
  type: Portal
  url: https://www.pieinsurance.com/agency
- group: docs
  title: ''
  type: Documentation
  url: https://www.pieinsurance.com/agency/api
- group: start
  title: ''
  type: Signup
  url: https://www.pieinsurance.com/agency/partner-with-pie
- group: start
  title: ''
  type: Login
  url: https://partner.pieinsurance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pieinsurance.com/agency/appetite-checker
- group: docs
  title: ''
  type: Documentation
  url: https://www.pieinsurance.com/agency/resources
- group: company
  title: ''
  type: About
  url: https://www.pieinsurance.com/about
- group: other
  title: ''
  type: Timeline
  url: https://www.pieinsurance.com/about/timeline
- group: other
  title: ''
  type: Leadership
  url: https://www.pieinsurance.com/about/leadership
- group: company
  title: ''
  type: Press
  url: https://www.pieinsurance.com/media
- group: company
  title: ''
  type: Blog
  url: https://www.pieinsurance.com/blog
- group: company
  title: ''
  type: Careers
  url: https://www.pieinsurance.com/culture/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.pieinsurance.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pieinsurance.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pieinsurance.com/legal/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pieinsurance
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/pieinsurance
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/pieinsurance
- group: other
  title: ''
  type: Products
  url: https://www.pieinsurance.com/coverage/workers-compensation-insurance
- group: other
  title: ''
  type: Products
  url: https://www.pieinsurance.com/coverage/business-owners-policy
- group: other
  title: ''
  type: Products
  url: https://www.pieinsurance.com/coverage/commercial-auto-insurance
- group: other
  title: ''
  type: Products
  url: https://www.pieinsurance.com/coverage/general-liability-insurance
- group: other
  title: ''
  type: Products
  url: https://www.pieinsurance.com/coverage/professional-liability-insurance
created: '2026-05-25'
description: Pie Insurance is a Washington, DC and Denver-based insurtech founded in May 2017 that makes commercial insurance for small businesses, with workers' compensation as its flagship line. Pie underwrites its own workers' comp through The Pie Insurance Company (NAIC 21857) — the carrier formerly known as Pie Casualty Insurance Company, which Pie acquired as Western Select Insurance Company in 2021 and took full-stack in February 2023 with an A- (Excellent) rating from AM Best. In addition to workers' comp, Pie offers business owners policy (BOP), commercial auto, general liability, professional liability, and errors and omissions through partner carriers. The product is sold both direct-to-business and through a partner network of 4,000+ independent insurance agencies, who quote, bind, and service policies via the Pie agency portal and the Pie Partner API. The Partner API (api.post-prod.pieinsurance.com, REST/JSON, documented with OpenAPI 3.0.4) exposes class-code search, eligibility
  questions, appetite checks, price indications, full bindable quotes, quote documents, and quote PDF retrieval so agency management systems and partner platforms can embed the Pie workers' comp experience without redirecting users off-platform. Coverage is available in 39 states plus DC; 73% of submissions are auto-decided and average quote time is roughly three minutes. The company has raised approximately $621M across Seed through Series D from investors including Allianz X, SVB Capital, Greycroft, Aspect Ventures, and Elefund. CEO and co-founder is John Swigart. The Pie Partner API is the public developer surface; there is no broader open-source SDK or GitHub organization.
features:
- Workers' compensation insurance for small business across 39 states + DC
- In-house carrier — The Pie Insurance Company (NAIC 21857), A- (Excellent) AM Best
- Direct-to-business and 4,000+ partner agencies
- Average quote time roughly three minutes; up to 30% savings vs. comparable carriers
- 73% of submissions auto-decided; 70% of NCCI class codes in appetite
- REST/JSON Partner API documented with OpenAPI 3.0.4 (Swagger UI hosted)
- Class-code search and state-by-state appetite endpoints
- Eligibility questions endpoint keyed off agency state + class code
- Price indication endpoint for fast, non-binding pricing
- Full quote lifecycle (create, retrieve, update) with bindable output
- Quote document upload and quote PDF retrieval endpoints
- Built-in support for prior-carrier history, experience modification, and officer exclusions
- Business owners policy, commercial auto, general liability, professional liability, and E&O via partner carriers
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pie-insurance.png
layout: provider
modified: '2026-05-25'
name: Pie Insurance
nav: Providers
network: true
overview: 'Pie Insurance publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Appetite API, ClassCodeSearch API, Eligibility API, and 4 more. Tagged areas include Insurance, Insurtech, Workers Compensation, Small Business, and Commercial Insurance.


  Pie Insurance''s developer surface includes authentication, developer portal, documentation, signup flow, engineering blog, and 22 more developer resources.'
random_paper: 51
score:
  band: thin
  composite: 31.5
  delta: -3.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 45.3
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pie-insurance/refs/heads/main/screenshots/pie-insurance-2026-06-20T191702.png
security:
- kind: authentication
  name: Pie Insurance Authentication
  slug: pie-insurance-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pie Insurance Domain Security
  slug: pie-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pie-insurance
tags:
- Insurance
- Insurtech
- Workers Compensation
- Small Business
- Commercial Insurance
- Business Owners Policy
- Commercial Auto
- General Liability
- Professional Liability
- Agency Portal
- Partner API
- Quoting
- Binding
website: https://www.pieinsurance.com
---
