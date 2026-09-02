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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goaudience-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goaudience.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://goaudience.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://business.goaudience.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goaudience.com/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goaudience.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://goaudience.com/contact
- group: commercial
  title: ''
  type: Plans
  url: plans/goaudience-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goaudience-llms.txt
coverage:
  checked: '2026-08-13'
  detail: GoAudience sells a Shopify merchant app and runs no developer program — goaudience.com returns a hard 404 on /docs, /api, /developers and /blog, the GoAudience GitHub organization has zero public repositories, and the merchant console at business.goaudience.com is a create-react-app SPA whose catch-all answers 200 with the same HTML shell for every path including ones that do not exist.
  evidence:
  - status: 404
    url: https://goaudience.com/developers
  - status: 404
    url: https://goaudience.com/docs
  - status: 404
    url: https://goaudience.com/api
  - status: 200
    url: https://api.github.com/orgs/GoAudience/repos
  - status: 200
    url: https://business.goaudience.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: GoAudience is a customer-intelligence platform for Shopify ecommerce brands that turns first-party customer data into marketing decisions. It builds stable customer personas from real store data, surfaces findings and recommended actions ranked by impact, and syncs directly into Klaviyo, Meta, TikTok and other marketing tools. Features include a natural-language command surface for asking grounded questions about customers, a weekly "Monday Brief" digest of at-risk, lapsed and recovered customers with revenue impact, and a 90-day email audit. GoAudience is a Techstars-backed company; this profile was added to the API Evangelist network as an enrichment lead.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goaudience.png
layout: provider
modified: '2026-08-13'
name: GoAudience
nav: Providers
network: true
overview: 'GoAudience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Intelligence, E-Commerce, Shopify, and Marketing.


  GoAudience''s developer surface includes pricing, signup flow, support, and 6 more developer resources.'
plans:
- name: Goaudience Plans Pricing
  plan_count: 5
  slug: goaudience-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goaudience/refs/heads/main/screenshots/goaudience-2026-07-25T220010.png
security:
- kind: domain-security
  name: Goaudience Domain Security
  slug: goaudience-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goaudience
tags:
- Company
- Customer Intelligence
- E-Commerce
- Shopify
- Marketing
- Customer Data Platform
- Personas
- Decision Intelligence
website: https://goaudience.com/
---
