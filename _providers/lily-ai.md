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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The middleware API behind Lily AI's customer application at app.lily.ai. Publicly served with a Swagger UI at /api and an OpenAPI 3.0.0 contract at /api-json (63 paths, 100 operations, 41 schemas), co
  name: LilyApp Middleware API
  slug: lilyapp-middleware-api
artifact_total: 7
collections:
- collection_type: open
  name: LilyApp API - Nest Based Application
  slug: open-lily-ai-lilyapp-api
common:
- group: build
  title: ''
  type: Packages
  url: packages/lily-ai-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lily-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lily-ai-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lily-ai-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lily-ai-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lily-ai-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lily-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lily.ai/
- group: company
  title: ''
  type: Blog
  url: https://lily.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://lily.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://lily.ai/free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lily.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lily.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://lily.ai/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://lily.ai/faqs
- group: other
  title: ''
  type: CaseStudies
  url: https://lily.ai/case-studies
- group: company
  title: ''
  type: Press
  url: https://lily.ai/press
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lily-ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lily-ai-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lily-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lily.ai/
created: '2026-07-17'
description: 'Lily AI, Inc. is a retail product-intelligence company whose platform, Lily Max, enriches e-commerce product catalogs so that products are legible to advertising platforms, search engines, onsite search, and AI shopping agents. Agents identify gaps in a retailer''s product data, generate consumer-centric attributes and copy, run controlled tests against a holdout, and deploy the winning enrichments across Google Merchant Center feeds, Meta Commerce Manager catalogs, AI discovery and agentic commerce surfaces, and onsite PDP, search, and faceting. Lily AI sells to enterprise retailers, brands, and agencies and positions itself as a layer over the existing commerce stack rather than a replacement for a PIM or feed manager. The company raised a $25M Series B with participation from Canaan Partners, Conductive Ventures, Sorenson Ventures, and NEA. Lily AI operates no developer program: there is no developer portal, no published API reference, no SDK, no GitHub organization, and
  no self-service credential path, and the platform is sold and onboarded through enterprise sales. It does, however, publicly serve the OpenAPI 3.0.0 contract for the LilyApp middleware that backs its customer application at app.lily.ai — 63 paths and 100 operations behind an Azure AD B2C bearer JWT, with a public Swagger UI. That contract is captured here as the company''s only machine-readable API surface.'
image: https://lily.ai/icon.png
layout: provider
modified: '2026-08-12'
name: Lily AI
nav: Providers
network: true
overview: 'Lily AI publishes 1 API on the [APIs.io](https://apis.io/) network: LilyApp Middleware API. Tagged areas include Company, Retail, E-Commerce, Artificial Intelligence, and Product Data.


  Lily AI''s developer surface includes authentication, engineering blog, pricing, signup flow, support, and 17 more developer resources.'
plans:
- name: Lily Ai Plans Pricing
  plan_count: 0
  slug: lily-ai-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Lily Ai Rate Limits
  slug: lily-ai-rate-limits
score:
  band: developing
  composite: 40.9
  delta: -0.5
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 16.7
    contract_quality: 46.2
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 47.4
  previous_composite: 41.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lily-ai/refs/heads/main/screenshots/lily-ai-2026-07-25T225157.png
security:
- kind: authentication
  name: Lily Ai Authentication
  slug: lily-ai-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Lily Ai Domain Security
  slug: lily-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lily Ai Trust Center
  slug: lily-ai-trust-center
  summary_line: trust center published
slug: lily-ai
tags:
- Company
- Retail
- E-Commerce
- Artificial Intelligence
- Product Data
- Advertising
- Agentic Commerce
- Search
- Marketing
website: https://lily.ai/
---
