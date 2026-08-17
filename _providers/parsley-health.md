---
access_model:
  confidence: high
  label: Consumer Membership
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.parsleyhealth.com/care
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The agent-callable surface of Parsley Health's direct-to-consumer supplement store. A live, anonymous Universal Commerce Protocol MCP endpoint exposes thirteen tools for catalog search, product lookup
  name: Parsley Health Store — UCP / MCP Agent Commerce
  slug: parsley-health-store-ucp-mcp-agent-commerce
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.parsleyhealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.parsleyhealth.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.parsleyhealth.com/care
- group: start
  title: ''
  type: SignUp
  url: https://www.parsleyhealth.com/join/get-care
- group: start
  title: ''
  type: Login
  url: https://my.parsleyhealth.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.parsleyhealth.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parsleyhealth.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.parsleyhealth.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.parsleyhealth.com
- group: operate
  title: ''
  type: FAQ
  url: https://www.parsleyhealth.com/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parsleyhealth
- group: auth
  title: ''
  type: Compliance
  url: https://www.parsleyhealth.com/notice-of-privacy-practices
- group: company
  title: ''
  type: Careers
  url: https://www.parsleyhealth.com/careers
- group: company
  title: ''
  type: Press
  url: https://www.parsleyhealth.com/press
- group: other
  title: ''
  type: Locations
  url: https://www.parsleyhealth.com/locations
- group: other
  title: ''
  type: Products
  url: https://www.parsleyhealth.com/store/collections/all
- group: other
  title: ''
  type: Reviews
  url: https://www.parsleyhealth.com/reviews
- group: other
  title: ''
  type: EditorialPolicy
  url: https://www.parsleyhealth.com/editorial-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/parsley-health_stock/
- group: build
  title: ''
  type: Packages
  url: packages/parsley-health-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/parsley-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parsley-health-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/parsley-health-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parsley-health-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/parsley-health-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/parsley-health-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parsley-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/parsley-health-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parsley-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/parsley-health-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/parsley-health-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parsley-health-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/parsley-health-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/parsley-health-plans-pricing.yml
- group: other
  title: ''
  type: Store
  url: https://store.parsleyhealth.com
created: '2026-08-02'
description: 'Parsley Health is a physician-led virtual and in-person medical practice founded in 2016 by Dr. Robin Berzin, MD, headquartered at 126 5th Ave, New York, NY, that delivers functional medicine as a membership-based primary and specialty care service. Members are matched with board-certified MD, DO, NP or PA clinicians who hold additional functional medicine fellowship training through Parsley and the Institute for Functional Medicine, and are supported by functional nutrition coaches, an RN care manager and a care coordinator. Care programs cover gut and digestive health, hormone balance, autoimmune and inflammatory conditions, unexplained symptoms, mental and emotional health, heart and metabolic health, longevity, perimenopause and menopause, fertility, pregnancy and postpartum, and environmental exposure. The membership bundles five medical visits, two nutrition coaching sessions, advanced diagnostic lab testing, a personalized care plan, a symptom tracking dashboard and
  unlimited messaging, priced at $150/month or $1,500/year with insurance and $275/month or $2,750/year self-pay. Parsley is available nationwide via telehealth with in-person care in New York City and Los Angeles, is in network with major commercial insurers including Aetna, Cigna, UnitedHealthcare, BlueCross BlueShield, Humana and Centene, and also operates a direct-to-consumer supplement store. Parsley Health is a consumer healthcare service rather than a developer platform: it publishes no developer portal, no API reference, no API keys and no OpenAPI, and its public GitHub organization contains internal engineering tooling (Docker images, GitHub Actions, lint configs, an Apollo Router fork) rather than any client SDK. It does, however, serve real agent-callable surfaces on its supplement store at store.parsleyhealth.com: a live anonymous Universal Commerce Protocol MCP endpoint exposing thirteen catalog, cart, checkout and order tools, an anonymous Shopify Storefront GraphQL endpoint,
  an llms.txt and agents.md written for agents, and OAuth 2.0 / OpenID Connect discovery documents. Those surfaces are provided by the Shopify commerce platform under Parsley Health''s own hostname, cover retail supplement purchase only, and are governed by a published rule that agents must not complete payment without contemporaneous human approval. No clinical data is reachable by machine: there is no FHIR endpoint, no patient-access API and no appointment, lab or medical-record surface, and the member application at my.parsleyhealth.com remains an authenticated single-page app with no documented public API.'
image: https://cdn-builder.parsleyhealth.com/api/v1/image/assets%2F996895949aaa465aa438b22f75b680b6%2F3ca4c568b1cc4dc7b064ff122217abe6
layout: provider
mcp_servers:
- description: ''
  name: parsley-health-mcp.yml
  slug: parsley-health-mcpyml
modified: '2026-08-15'
name: Parsley Health
nav: Providers
network: true
overview: 'Parsley Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Telehealth, and Telemedicine.


  Parsley Health''s developer surface includes engineering blog, pricing, signup flow, support, FAQ, authentication, and 30 more developer resources.'
plans:
- name: Parsley Health Plans Pricing
  plan_count: 0
  slug: parsley-health-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 0
  name: Parsley Health Rate Limits
  slug: parsley-health-rate-limits
scopes:
- name: Parsley Health Scopes
  scope_count: 0
  slug: parsley-health-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.6
  delta: 10.4
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 22.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/parsley-health/refs/heads/main/screenshots/parsley-health-2026-08-07T191503.png
security:
- kind: authentication
  name: Parsley Health Authentication
  slug: parsley-health-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Parsley Health Domain Security
  slug: parsley-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parsley-health
tags:
- Company
- Health
- Healthcare
- Telehealth
- Telemedicine
- Functional Medicine
- Primary Care
- Wellness
- Nutrition
- Diagnostics
- Lab Testing
- Membership
- Digital Health
- Consumer Health
- Ecommerce
- Agentic Commerce
- MCP
- Supplements
website: https://www.parsleyhealth.com/
---
