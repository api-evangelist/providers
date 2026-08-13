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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://facet.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://facet.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://facet.com/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://facet.com/legal-documents/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://facet.com/privacy-notice/
- group: operate
  title: ''
  type: Support
  url: https://facet.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://facet.com/learn/library/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Facet-Wealth
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/facet-wealth-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/facet-wealth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/facet-wealth-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/facet-wealth-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/facet-wealth_stock/
coverage:
  checked: '2026-08-12'
  detail: 'Facet sells human financial advice, not software: its one live JSON host (api.facet.com) is the private backend for its own member application and returns plain-text 404s on every spec path, the marketing site is WordPress with no developer section in its sitemap, and the only machine-readable document Facet publishes — facet.com/llms.txt — describes the advisory service and never mentions an API.'
  evidence:
  - status: 200
    url: https://api.facet.com/
  - status: 404
    url: https://api.facet.com/openapi.json
  - status: 404
    url: https://api.facet.com/.well-known/agent-card.json
  - status: 200
    url: https://facet.com/llms.txt
  - status: 200
    url: https://facet.com/pricing/
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Facet (also known as Facet Wealth) is a national SEC-registered investment advisor and financial planning firm founded in 2016 and headquartered in Baltimore, Maryland. Facet delivers fiduciary, product-agnostic financial advice through a flat annual membership rather than an assets-under-management fee, pairing a proprietary technology platform with CERTIFIED FINANCIAL PLANNER professionals. Membership covers comprehensive financial planning, investment management, retirement planning, tax strategy and filing, equity compensation planning, insurance guidance, education planning, and estate planning delivered in partnership with Wealth.com. Facet is a direct-to-consumer advisory service: it publishes no public developer program, API documentation, or machine-readable contract.'
image: https://facet.com/wp-content/uploads/2023/02/Facet_logo_rgb_pos-min.png
layout: provider
modified: '2026-08-12'
name: Facet Wealth
nav: Providers
network: true
overview: 'Facet Wealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Financial Planning, Wealth Management, and Investment Management.


  Facet Wealth''s developer surface includes pricing, signup flow, support, engineering blog, and 9 more developer resources.'
plans:
- name: Facet Wealth Plans Pricing
  plan_count: 3
  slug: facet-wealth-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Facet Wealth Rate Limits
  slug: facet-wealth-rate-limits
score:
  band: emerging
  composite: 23.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: domain-security
  name: Facet Wealth Domain Security
  slug: facet-wealth-domain-security
  summary_line: TLSv1.3 · DMARC
slug: facet-wealth
tags:
- Company
- Financial Services
- Financial Planning
- Wealth Management
- Investment Management
- Retirement Planning
- Tax Planning
- Registered Investment Advisor
- Personal Finance
website: https://facet.com/
---
