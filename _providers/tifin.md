---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tifin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tifin.com/
- group: company
  title: ''
  type: About
  url: https://tifin.com/company/
- group: other
  title: ''
  type: Products
  url: https://tifin.com/products/
- group: company
  title: ''
  type: Blog
  url: https://tifin.com/resources/
- group: company
  title: ''
  type: News
  url: https://tifin.com/news/
- group: start
  title: ''
  type: SignUp
  url: https://tifin.com/product/tifinai/request-access/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tifin.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tifin.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://tifin.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tifin/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/tifin-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tifin-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tifin-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tifin-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tifin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tifin-rate-limits.yml
coverage:
  checked: '2026-08-30'
  detail: TIFIN markets its AI capabilities as "a suite of APIs that can plug into existing wealthtech stacks", but every product page ends at a "Get access" request form and no developer host exists at all — developer.tifin.com, docs.tifin.com, api.tifin.com, developers.tifin.com, docs.tifin.ai and api.tifin.ai do not resolve in DNS, and the full eight-page tifin.com sitemap contains no developer, pricing, or documentation page.
  evidence:
  - status: 200
    url: https://tifin.com/product/tifinai/request-access/
  - status: 200
    url: https://tifin.com/page-sitemap.xml
  - status: 0
    url: https://developer.tifin.com/
  - status: 0
    url: https://api.tifin.com/
  - status: 404
    url: https://api.magnifi.com/openapi.json
  reason: sales-gate
  state: gated
created: '2026-08-30'
description: TIFIN is a Boulder, Colorado based fintech company founded in 2018 by Dr. Vinay Nair that builds AI-driven wealth technology for financial advisors, RIAs, broker-dealers, asset managers and insurance firms. Its platforms span TIFIN.AI (an agentic operating system consolidating the group's AI businesses for wealth and asset management workflows), TIFIN Wealth (investment proposal, risk-capacity and client-personalization tooling that integrates with Fidelity, BNY Pershing, Black Diamond, Salesforce, Wealthbox, Redtail, Orion and iRebal), TIFIN AMP/AG for asset-manager distribution intelligence, TIFIN Give for charitable giving accounts, TIFIN @Work for workplace financial wellness, and Magnifi, an AI investing assistant. TIFIN incubated 55ip (sold to J.P. Morgan) and Paralel, and announced a joint venture, TIFIN.AI, with J.P. Morgan Asset Management. The company states its AI capabilities are available as APIs that plug into existing wealthtech stacks, but publishes no public
  developer portal, API reference, or machine-readable contract; access is gated behind a "Get access" request form.
image: https://tifin.com/wp-content/uploads/TIFIN_SmallSizes_K.svg
layout: provider
modified: '2026-08-30'
name: TIFIN
nav: Providers
network: true
overview: 'TIFIN is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Wealth Management, Asset Management, and Artificial Intelligence.


  TIFIN''s developer surface includes engineering blog, product news, signup flow, and 14 more developer resources.'
plans:
- name: Tifin Plans Pricing
  plan_count: 0
  slug: tifin-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Tifin Rate Limits
  slug: tifin-rate-limits
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
security:
- kind: domain-security
  name: Tifin Domain Security
  slug: tifin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tifin
tags:
- Company
- Financial-Services
- Wealth Management
- Asset Management
- Artificial Intelligence
- Fintech
- WealthTech
- Financial Advisors
- Investment Management
- Insurance
website: https://tifin.com/
---
