---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The agent-facing commerce surface for the ModifyHealth store. A Universal Commerce Protocol (UCP) service exposed over MCP at https://modifyhealth.com/api/ucp/mcp, serving 13 unauthenticated tools for
  name: ModifyHealth UCP Commerce MCP
  slug: modifyhealth-ucp-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://modifyhealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://modifyhealth.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modifyhealth-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/modifyhealth-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/modifyhealth-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/modifyhealth-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/modifyhealth-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/modifyhealth-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/modifyhealth-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/modifyhealth-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/modifyhealth-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/modifyhealth-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/modifyhealth-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/modifyhealth-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/modifyhealth-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modifyhealth-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/modifyhealth-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://modifyhealth.com/pages/how-it-works#faq
- group: company
  title: ''
  type: Blog
  url: https://modifyhealth.com/blogs/blog
- group: operate
  title: ''
  type: Support
  url: https://modifyhealth.com/pages/how-can-we-help
- group: start
  title: ''
  type: SignUp
  url: https://modifyhealth.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://modifyhealth.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modifyhealth.com/policies/privacy-policy
created: '2026-08-26'
description: 'ModifyHealth is a US direct-to-consumer medically tailored meal delivery company that ships fully prepared, dietitian-crafted meal programs nationwide with free shipping. Its programs include Monash University Low FODMAP Certified, Mediterranean, gluten-free, heart-friendly, diabetes-friendly, carb-conscious and GLP-1 support plans, sold to consumers directly and to health plans, employers, case managers and referring clinicians as a food-as-medicine benefit. The storefront runs on Shopify and exposes a real machine surface for agents: a published /llms.txt and /agents.md, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and an unauthenticated MCP endpoint at /api/ucp/mcp serving 13 catalog, cart, checkout and order tools. ModifyHealth publishes no developer program, no OpenAPI, and no SDKs.'
image: https://modifyhealth.com/cdn/shop/files/MOD_Icon_Circle_KO_Green_400px_32x32.png?v=1623949729
layout: provider
mcp_servers:
- description: ''
  name: ModifyHealth MCP Server
  slug: modifyhealth-mcp-server
modified: '2026-08-26'
name: ModifyHealth
nav: Providers
network: true
overview: 'ModifyHealth publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Food and Beverage, Nutrition, Meal Delivery, and Food as Medicine.


  ModifyHealth''s developer surface includes documentation, authentication, pricing, engineering blog, support, signup flow, and 18 more developer resources.'
plans:
- name: Modifyhealth Plans Pricing
  plan_count: 0
  slug: modifyhealth-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Modifyhealth Rate Limits
  slug: modifyhealth-rate-limits
scopes:
- name: Modifyhealth Scopes
  scope_count: 4
  slug: modifyhealth-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 32.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modifyhealth/refs/heads/main/screenshots/modifyhealth-2026-09-02T150612.png
security:
- kind: authentication
  name: Modifyhealth Authentication
  slug: modifyhealth-authentication
  summary_line: none/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Modifyhealth Domain Security
  slug: modifyhealth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: modifyhealth
tags:
- Health
- Food and Beverage
- Nutrition
- Meal Delivery
- Food as Medicine
- E-Commerce
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Direct to Consumer
website: https://modifyhealth.com/
---
