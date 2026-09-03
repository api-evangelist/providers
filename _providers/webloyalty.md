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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/webloyalty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://webloyalty.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://webloyalty.co.uk/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://webloyalty.co.uk/privacy-cookies-policy/
- group: operate
  title: ''
  type: Support
  url: https://webloyalty.co.uk/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://webloyalty.co.uk/news-views/
- group: company
  title: ''
  type: BlogRSS
  url: https://webloyalty.co.uk/feed/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/webloyalty-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/webloyalty-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/webloyalty-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/webloyalty-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/webloyalty-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/webloyalty-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/webloyalty-packages.yml
- group: design
  title: ''
  type: Components
  url: components/webloyalty-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/webloyalty-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/webloyalty-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/webloyalty-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/webloyalty-llms.txt
created: '2026-07-17'
description: Webloyalty is a customer-engagement and loyalty-marketing company that helps ecommerce and retail businesses build stronger, more profitable customer relationships. Its market-leading rewards platform delivers savings, cashback, and shopping benefits to consumers, typically presented after an online transaction, while generating incremental secondary revenue for the retail partner. Founded in 1999 and historically part of the Affinion Group, the company operates localized programs across the United States, United Kingdom, France, Ireland, Spain, the Netherlands, Switzerland, Turkey, and Mexico. This API Evangelist profile was surfaced as a portfolio company of Canaan Partners. Webloyalty markets a consumer rewards/membership product and a partner engagement platform, and is a brand of Tenerity (formerly Affinion Group). It publishes no developer portal, API reference or OpenAPI — its commercial integration is sold as "bespoke API solutions" through sales. Its only public programmable
  surfaces are an OAuth-protected Model Context Protocol endpoint served from the UK site's WordPress REST API, and a first-party React Native SDK for embedding Webloyalty campaign banners in partner apps.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/webloyalty.png
layout: provider
mcp_servers:
- description: 'Webloyalty''s UK site (webloyalty.co.uk) serves a live, OAuth-protected Model Context Protocol endpoint from inside its WordPress REST API. It is advertised by two real discovery documents on the same '
  name: Webloyalty MCP Server
  slug: webloyalty-mcp-server
modified: '2026-08-13'
name: Webloyalty
nav: Providers
network: true
overview: 'Webloyalty is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Loyalty, Rewards, E-Commerce, and Customer Engagement.


  Webloyalty''s developer surface includes support, engineering blog, authentication, changelog, and 15 more developer resources.'
plans:
- name: Webloyalty Plans Pricing
  plan_count: 0
  slug: webloyalty-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Webloyalty Rate Limits
  slug: webloyalty-rate-limits
scopes:
- name: Webloyalty Scopes
  scope_count: 0
  slug: webloyalty-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 18.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/webloyalty/refs/heads/main/screenshots/webloyalty-2026-09-02T170530.png
security:
- kind: authentication
  name: Webloyalty Authentication
  slug: webloyalty-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Webloyalty Domain Security
  slug: webloyalty-domain-security
  summary_line: TLSv1.2 · DMARC
slug: webloyalty
tags:
- Company
- Loyalty
- Rewards
- E-Commerce
- Customer Engagement
- Marketing
- Retail
- Cashback
website: http://webloyalty.com/
---
