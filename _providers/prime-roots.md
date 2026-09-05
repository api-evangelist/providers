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
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'The Prime Roots Shopify storefront''s agent-facing commerce surface: a UCP merchant profile, a hosted MCP endpoint for catalog/cart/checkout, and read-only storefront JSON endpoints.'
  name: Prime Roots Storefront (Agentic Commerce)
  slug: prime-roots-storefront-agentic-commerce
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://primeroots.com
- group: company
  title: ''
  type: Blog
  url: https://www.primeroots.com/blogs/all
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.primeroots.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.primeroots.com/policies/terms-of-service
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prime-roots-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prime-roots-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prime-roots-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prime-roots-domain-security.yml
created: '2026-07-17'
description: 'Prime Roots is a Berkeley, California foodtech company making koji- and plant-based deli meats and bacon marketed as "the clean deli meat" — no preservatives, nitrates, or celery salt. It sells direct-to-consumer and through foodservice, running its online store on Shopify. That storefront exposes a native agent-commerce surface: an llms.txt / agents.md agent guide, a Universal Commerce Protocol (UCP, https://ucp.dev) discovery document at /.well-known/ucp, and a hosted MCP endpoint at /api/ucp/mcp for agent-driven catalog search, cart, and buyer-approved checkout. Added to the API Evangelist network as a Prosus Ventures portfolio company and enriched from its live public discovery surfaces.'
image: https://www.primeroots.com/cdn/shop/files/logo.png
layout: provider
mcp_servers:
- description: 'Prime Roots operates a hosted, remote MCP endpoint as part of its Shopify storefront implementation of the Universal Commerce Protocol (UCP, https://ucp.dev). Agents POST JSON-RPC to the endpoint and '
  name: Prime Roots MCP Server
  slug: prime-roots-mcp-server
modified: '2026-07-20'
name: Prime Roots
nav: Providers
network: true
overview: 'Prime Roots publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Tech, Plant-Based, Deli Meat, and Food Service.


  Prime Roots'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.3
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prime-roots/refs/heads/main/screenshots/prime-roots-2026-09-02T152018.png
security:
- kind: domain-security
  name: Prime Roots Domain Security
  slug: prime-roots-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: prime-roots
tags:
- Company
- Food Tech
- Plant-Based
- Deli Meat
- Food Service
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- E-Commerce
website: https://primeroots.com
---
