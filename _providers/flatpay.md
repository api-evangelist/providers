---
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.flatpay.com/
- group: operate
  title: ''
  type: Support
  url: https://www.flatpay.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.flatpay.com/en/support/solutions
- group: company
  title: ''
  type: Blog
  url: https://www.flatpay.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flatpay.com/pricing
- group: start
  title: ''
  type: Login
  url: https://portal.flatpay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flatpay.com/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flatpay.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FLATPAY-DK
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flatpay.com/
- group: auth
  title: ''
  type: Security
  url: https://flatpay.com/responsible-disclosure
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/flatpay-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flatpay-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flatpay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flatpay-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flatpay-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flatpay-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flatpay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flatpay-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/flatpay-packages.yml
coverage:
  checked: '2026-08-16'
  detail: Flatpay ships no developer program of its own — api.flatpay.com and developer.flatpay.com do not resolve, the 1,554-URL sitemap contains no /developers, /docs or /api path, and the help center's webshop-integration articles hand merchants an emailed API key and link out to Frisbii's billwerk.plus plugin pages, because Flatpay Online runs on the Frisbii (Billwerk+) platform operated by a different company.
  evidence:
  - status: 0
    url: https://api.flatpay.com/
  - status: 404
    url: https://www.flatpay.com/openapi.json
  - status: 200
    url: https://www.flatpay.com/sitemap.xml
  - status: 200
    url: https://help.flatpay.com/en/support/solutions
  - status: 200
    url: https://www.flatpay.com/.well-known/security.txt
  - status: 200
    url: https://www.flatpay.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-16'
description: 'Flatpay is a Copenhagen-headquartered payments company founded in 2022 that sells card acceptance to small and medium-sized European merchants on a single flat per-transaction rate with no monthly subscription. Its product line is a PAX card terminal, an all-in-one point-of-sale system, an online payment solution for webshops built on the Frisbii (Billwerk+) platform, and Flatpay Capital merchant financing. The company operates in Denmark, Finland, Germany, Italy, France, the Netherlands and the United Kingdom, serves roughly 70,000 merchants, and reached unicorn valuation in 2025. Flatpay publishes no public developer portal, API reference or machine-readable specification: webshop integration is delivered through Frisbii+ Pay plugins and a merchant-issued API key for the Frisbii gateway, which is operated by a different company.'
image: https://cdn.prod.website-files.com/675c2b1d9cefa24db1fdcafc/681a7a4079e0bf9e26fad636_en-open-graph-main-all-products.jpg
layout: provider
modified: '2026-08-16'
name: Flatpay
nav: Providers
network: true
overview: 'Flatpay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Point-of-Sale, Card Terminals, and Merchant Acquiring.


  Flatpay''s developer surface includes support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Flatpay Plans Pricing
  plan_count: 4
  slug: flatpay-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Flatpay Rate Limits
  slug: flatpay-rate-limits
score:
  band: emerging
  composite: 25.8
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 25.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Flatpay Domain Security
  slug: flatpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flatpay Vulnerability Disclosure
  slug: flatpay-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: flatpay
tags:
- Company
- Payments
- Point-of-Sale
- Card Terminals
- Merchant Acquiring
- Fintech
- Online Payments
- Denmark
- Europe
- Small Business
website: https://www.flatpay.com/
---
