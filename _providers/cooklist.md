---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Cooklist Webhooks
  slug: cooklist-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://cooklist.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cooklist.com/platform/agentic-commerce
- group: company
  title: ''
  type: About
  url: https://cooklist.com/company/about
- group: operate
  title: ''
  type: Support
  url: https://cooklist.com/support
- group: start
  title: ''
  type: SignUp
  url: https://cooklist.com/request-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cooklist.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cooklist.com/terms-of-use
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cooklist-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cooklist-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cooklist-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cooklist-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cooklist-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/cooklist-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cooklist-domain-security.yml
created: '2026-07-17'
description: Cooklist is an agentic commerce platform purpose-built for grocery and retail. It provides retailer-native AI shopping assistants that plan meals, run solution-first agentic search over live catalog and inventory, assemble cart-ready bundles, and execute verified cart operations against the retailer's system of record. Founded in 2018, Cooklist powers the first agentic AI shopping experience launched by Kroger (the Kroger AI Meal Assistant, live since December 2025) and integrates with 15+ retailer catalogs. Retailers embed a drop-in JavaScript SDK that talks to Cooklist over HTTPS (GraphQL) and WSS (real-time streaming); a B2B Partner API (API key or JWT auth, per-organization field allowlists), authenticated webhooks, and a Model Context Protocol (MCP) interface expose real-time retail inventory and pricing to third-party LLMs such as ChatGPT and Gemini for off-site agentic commerce.
image: https://cooklist.com/images/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Cooklist MCP Server
  slug: cooklist-mcp-server
modified: '2026-07-18'
name: Cooklist
nav: Providers
network: true
overview: 'Cooklist is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agentic Commerce, Grocery, Retail, and AI Assistant.


  The Cooklist catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cooklist''s developer surface includes documentation, support, signup flow, authentication, and 10 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.2
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cooklist/refs/heads/main/screenshots/cooklist-2026-07-25T210357.png
security:
- kind: authentication
  name: Cooklist Authentication
  slug: cooklist-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cooklist Domain Security
  slug: cooklist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cooklist
tags:
- Company
- Agentic Commerce
- Grocery
- Retail
- AI Assistant
- MCP
- Recipes
- Meal Planning
- E-Commerce
- Personalization
website: https://cooklist.com/
---
