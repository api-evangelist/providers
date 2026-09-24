---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: The agent-facing commerce surface of the drinkhint.com storefront. Discovery is published at https://www.drinkhint.com/.well-known/ucp (Universal Commerce Protocol merchant profile, versions 2026-04-0
  name: Hint Agentic Commerce (UCP / MCP)
  slug: hint-agentic-commerce-ucp-mcp
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/security/hint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.drinkhint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.drinkhint.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://www.drinkhint.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.drinkhint.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://www.drinkhint.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.drinkhint.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.drinkhint.com/policies/privacy-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/mcp/hint-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hint-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/llms/hint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hint-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/well-known/hint-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hint-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/authentication/hint-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hint-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/scopes/hint-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hint-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/conventions/hint-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hint-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/conventions/hint-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hint-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/errors/hint-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hint-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/conformance/hint-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hint-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/lifecycle/hint-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hint-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/rate-limits/hint-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hint-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/plans/hint-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hint-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/data-model/hint-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hint-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-22'
description: 'Hint Inc. is a San Francisco based beverage company founded in 2005 by Kara Goldin, known for fruit-infused unsweetened water sold in still, sparkling, caffeinated and kids formats across 25+ flavors. A large share of its business is direct-to-consumer through its own storefront at drinkhint.com, which runs on Shopify. Hint publishes no traditional developer program, SDKs or OpenAPI, but the storefront does expose a live, anonymous agent surface: an agents.md / llms.txt agent instruction document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and a Model Context Protocol endpoint at /api/ucp/mcp that answers tools/list with 13 real catalog, cart, checkout and order tools. Checkout explicitly requires contemporaneous human approval before payment.'
image: https://www.drinkhint.com/cdn/shop/files/Logo_Hint-Wordmark-Droplet-Secondary-2_Color.png?v=1762813167
layout: provider
mcp_servers:
- description: ''
  name: Hint Storefront Agentic Commerce MCP
  slug: hint-storefront-agentic-commerce-mcp
modified: '2026-08-22'
name: Hint
nav: Providers
network: true
overview: 'Hint publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beverages, Consumer Packaged Goods, E-Commerce, and Direct to Consumer.


  Hint''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
plans:
- name: Hint Plans Pricing
  plan_count: 0
  slug: hint-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Hint Rate Limits
  slug: hint-rate-limits
scopes:
- name: Hint Scopes
  scope_count: 0
  slug: hint-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 0.0
  previous_composite: 22.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/hint/refs/heads/main/screenshots/hint-2026-09-02T145732.png
security:
- kind: authentication
  name: Hint Authentication
  slug: hint-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hint Domain Security
  slug: hint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hint
tags:
- Company
- Beverages
- Consumer Packaged Goods
- E-Commerce
- Direct to Consumer
- Retail
- Agentic Commerce
- MCP
- Universal Commerce Protocol
- Shopify
website: https://www.drinkhint.com/
---
