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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Logo Link delivers brand logos directly via CDN URL embedding. Supports lookup by domain, stock ticker, crypto symbol, or ISIN. Parameters include logo type (icon, symbol, logo), theme (light/dark), h
  name: Brandfetch Logo Link API
  slug: brandfetch-logo-link-api
- description: 'Brand Search API matches brand names to their corresponding domain URLs and unique identifiers, enabling rich autocomplete experiences. Endpoint: GET https://api.brandfetch.io/v2/search/:name. Authent'
  name: Brandfetch Brand Search API
  slug: brandfetch-brand-search-api
- description: The Brands API from Brand API (Brandfetch) — 1 operation(s) for brands.
  name: Brand API (Brandfetch) Brands API
  slug: brand-api-brands-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brand-api-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brandfetch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brandfetch
- group: other
  title: ''
  type: Customers
  url: https://brandfetch.com/developers/customers
- group: commercial
  title: ''
  type: Pricing
  url: https://brandfetch.com/developers/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.brandfetch.com/docs/getting-started
- group: design
  title: ''
  type: Webhooks
  url: https://docs.brandfetch.com/docs/webhooks/overview
- group: other
  title: ''
  type: EventTypes
  url: https://docs.brandfetch.com/docs/webhooks/event-types
- group: operate
  title: ''
  type: Support
  url: https://docs.brandfetch.com/support/getting-help
- group: operate
  title: ''
  type: Issues
  url: https://docs.brandfetch.com/support/report-inaccuracies
- group: learn
  title: ''
  type: Recipes
  url: https://docs.brandfetch.com/recipes/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brandfetch.com/reference/overview
- group: start
  title: ''
  type: Sandbox
  url: https://docs.brandfetch.com/docs/brand-api#testing-sandbox
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.brandfetch.com/changelog/2024
- group: start
  title: ''
  type: Login
  url: https://developers.brandfetch.com/
- group: start
  title: ''
  type: Signup
  url: https://developers.brandfetch.com/register
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.brandfetch.com/llms.txt
created: '2024-03-30'
description: Brandfetch provides programmatic access to brand assets and company data through a suite of APIs. The Brand API retrieves logos, color schemes, fonts, images, and firmographic information for any company via domain, stock ticker, ISIN code, or crypto symbol. The Logo Link API serves logos via CDN with support for multiple formats, themes, and sizes. The Brand Search API enables autocomplete experiences by matching brand names to their domains and identifiers. All APIs support Bearer token authentication with free access for development.
finops:
- name: Brand Api Finops
  service_category: Brand Data API
  slug: brand-api-finops
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/brand-api-create-branded-experiences.png
layout: provider
modified: '2026-04-21'
name: Brand API (Brandfetch)
nav: Providers
network: true
overview: 'Brand API (Brandfetch) publishes 1 API on the [APIs.io](https://apis.io/) network: Brands API. Tagged areas include Brands, Logos, Brand Assets, Company Data, and Firmographics.


  Brand API (Brandfetch)''s developer surface includes pricing, getting-started guide, support, documentation, sandbox, changelog, signup flow, and 10 more developer resources.'
plans:
- name: Brand Api Plans Pricing
  plan_count: 3
  slug: brand-api-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 4
  name: Brand Api Rate Limits
  slug: brand-api-rate-limits
score:
  band: developing
  composite: 45.4
  delta: -1.7
  facets:
    commercial_clarity: 63.2
    contract_quality: 49.2
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 60.5
  previous_composite: 47.1
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brand-api/refs/heads/main/screenshots/brand-api-2026-06-20T173632.png
security:
- kind: domain-security
  name: Brand Api Domain Security
  slug: brand-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: brand-api
tags:
- Brands
- Logos
- Brand Assets
- Company Data
- Firmographics
---
