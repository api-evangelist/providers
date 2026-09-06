---
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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Willow's storefront agent surface — a JSON-RPC 2.0 Model Context Protocol endpoint implementing the Universal Commerce Protocol 2026-08-25 shopping service. tools/list answers unauthenticated and retu
  name: Willow Pump UCP Commerce MCP
  slug: willow-pump-ucp-commerce-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/willow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onewillow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://onewillow.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/willow-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/willow-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/willow-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/willow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/willow-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/willow-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/willow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/willow-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/willow-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/willow-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/willow-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/willow-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/willow-plans-pricing.yml
- group: operate
  title: ''
  type: Support
  url: https://help.onewillow.com/s
- group: operate
  title: ''
  type: HelpCenter
  url: https://onewillow.com/pages/willow-support
- group: company
  title: ''
  type: Blog
  url: https://onewillow.com/blogs/all
- group: start
  title: ''
  type: SignUp
  url: https://onewillow.com/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onewillow.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onewillow.com/policies/privacy-policy
created: '2026-09-04'
description: 'Willow Innovations, Inc. is a Mountain View, California consumer health-technology company founded in 2014 that makes wearable, in-bra breast pumps — the Willow 360, Willow Go and the Wave manual pump — sold direct to consumers at onewillow.com and paired with a mobile app that tracks output and controls suction. Willow publishes no developer programme, API keys or OpenAPI, but its storefront is an agent-callable surface: it serves a Universal Commerce Protocol merchant profile at /.well-known/ucp.json and a live, anonymous MCP endpoint at /api/ucp/mcp exposing 13 tools for catalog search, cart, checkout and order retrieval, alongside published agent instructions (agents.md, llms.txt) and OAuth 2.0/OIDC customer-account discovery documents.'
image: https://onewillow.com/cdn/shop/files/OG-Image_db607121-7a26-49c9-b231-3a1e572a0fca_1200x630.jpg?v=1716782735
layout: provider
mcp_servers:
- description: Willow's online store at onewillow.com exposes a live, anonymous Model Context Protocol endpoint implementing the Universal Commerce Protocol (UCP) shopping service. An MCP client POSTs JSON-RPC to ht
  name: Willow Pump UCP Commerce MCP Server
  slug: willow-pump-ucp-commerce-mcp-server
modified: '2026-09-04'
name: Willow
nav: Providers
network: true
overview: 'Willow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Health, Breast Pumps, Maternal Health, and Medical Devices.


  Willow''s developer surface includes documentation, authentication, support, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Willow Plans Pricing
  plan_count: 0
  slug: willow-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Willow Rate Limits
  slug: willow-rate-limits
scopes:
- name: Willow Scopes
  scope_count: 0
  slug: willow-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 27.0
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
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Willow Authentication
  slug: willow-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Willow Domain Security
  slug: willow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: willow
tags:
- Company
- Consumer Health
- Breast Pumps
- Maternal Health
- Medical Devices
- Ecommerce
- Agentic Commerce
- MCP
- UCP
- agent-native
- Shopify
website: https://onewillow.com/
---
