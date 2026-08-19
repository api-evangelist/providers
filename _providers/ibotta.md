---
access_model:
  confidence: medium
  label: Partner / sales gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.9
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Single-operation product search API behind the Ibotta browser extension. POST /openai/search accepts an array of keyword queries plus limit / minPrice / maxPrice / storeId filters and returns products
  name: Ibotta Product API
  slug: ibotta-product-api
artifact_total: 9
collections:
- collection_type: open
  name: Ibotta Product API
  slug: open-ibotta-product-api
common:
- group: company
  title: ''
  type: Website
  url: https://home.ibotta.com/
- group: company
  title: ''
  type: Blog
  url: https://home.ibotta.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.ibotta.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ibotta
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.ibotta.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.ibotta.com/
- group: company
  title: ''
  type: Partners
  url: https://ipn.ibotta.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ipn.ibotta.com/integrating-with-the-ipn
- group: start
  title: ''
  type: GettingStarted
  url: https://ipn.ibotta.com/resource-hub/ipn-integration
- group: start
  title: ''
  type: Login
  url: https://portal.ipn.ibotta.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibotta-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ibotta-well-known.yml
- group: auth
  title: ''
  type: Security
  url: security/ibotta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibotta-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ibotta-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ibotta-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ibotta-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ibotta-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/ibotta-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ibotta-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ibotta-llms.txt
created: '2026-07-17'
description: 'Ibotta is a Denver-based consumer technology company (NYSE: IBTA) that operates a cash-back rewards platform and the Ibotta Performance Network (IPN), a digital promotions and retail-media network. Consumers earn real cash back on everyday purchases in-store and online through the Ibotta mobile app, browser extension, and connected retailer loyalty accounts. For brands, agencies, and retailers, the Ibotta Performance Network distributes digital rebates and promotions to more than 200 million shoppers across Ibotta''s owned properties and a network of partner retailers and publishers (including Walmart, Dollar General, Family Dollar, and others). Ibotta was surfaced in the API Evangelist network as a portfolio company of GGV Capital. Ibotta publishes exactly one machine-readable API contract: the Ibotta Product API (an OpenAPI 3.0.1 document at ibotta.com/bex-api/api-docs.json), declared by the ChatGPT plugin manifest Ibotta still serves at ibotta.com/.well-known/ai-plugin.json
  — a single product-search operation backing the Ibotta browser extension, gated by a service bearer token that is not self-serve. The Ibotta Performance Network APIs that partners actually integrate against are documented only inside the IPN partner portal (portal.ipn.ibotta.com), which is behind Auth0 and reached through a sales conversation; no public IPN API reference, pricing, or rate-limit documentation exists.'
image: https://images.ctfassets.net/zgieqvh3kubv/59XQvan2WhYzTi2PwaCGQV/454455352f937dde633bac1485ab3fdd/featured-ibotta.webp
layout: provider
mcp_servers:
- description: ''
  name: ibotta-mcp.yml
  slug: ibotta-mcpyml
modified: '2026-08-12'
name: Ibotta
nav: Providers
network: true
overview: 'Ibotta publishes 1 API on the [APIs.io](https://apis.io/) network: Product API. Tagged areas include Company, Consumer, Cash Back, Rewards, and Retail Media.


  Ibotta''s developer surface includes engineering blog, support, documentation, getting-started guide, and 17 more developer resources.'
plans:
- name: Ibotta Plans Pricing
  plan_count: 0
  slug: ibotta-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 0
  name: Ibotta Rate Limits
  slug: ibotta-rate-limits
scopes:
- name: Ibotta Scopes
  scope_count: 0
  slug: ibotta-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.1
  delta: -5.8
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 16.7
    contract_quality: 54.5
    developer_ergonomics: 28.6
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 13.2
  previous_composite: 38.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ibotta/refs/heads/main/screenshots/ibotta-2026-07-25T221955.png
security:
- kind: authentication
  name: Ibotta Authentication
  slug: ibotta-authentication
  summary_line: http/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Ibotta Domain Security
  slug: ibotta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ibotta Vulnerability Disclosure
  slug: ibotta-vulnerability-disclosure
  summary_line: Hackerone
slug: ibotta
tags:
- Company
- Consumer
- Cash Back
- Rewards
- Retail Media
- Coupons
- Loyalty
- Shopping
- Advertising
- Promotions
- Product Search
- Retail
- Affiliate
- CPG
website: https://home.ibotta.com/
---
