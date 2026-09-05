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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Agentic-commerce API for the Winc storefront, implemented via the Shopify-native Universal Commerce Protocol (UCP). Agents discover capabilities at /.well-known/ucp and call commerce tools over the MC
  name: Winc UCP Commerce MCP
  slug: winc-ucp-commerce-mcp
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://winc.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/winc-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/winc-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/winc-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/winc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/winc-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/winc-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/winc-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.winc.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.winc.com/policies/terms-of-service
created: '2026-07-17'
description: 'Winc is a direct-to-consumer online wine club and retailer (winc.com) offering curated, personalized wine subscriptions and single-bottle purchases matched to a member''s palate profile. The winc.com storefront runs on Shopify and exposes a modern agentic-commerce surface: a hosted UCP (Universal Commerce Protocol) MCP endpoint, Shopify Customer Account API authentication (OpenID Connect), and published /llms.txt and /agents.md agent instructions that let AI shopping assistants discover the catalog, build carts, and drive buyer-approved checkout. Originally surfaced as a VC portfolio company and enriched from its public agent-facing surface by the API Evangelist enrichment pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/winc.png
layout: provider
mcp_servers:
- description: Winc (winc.com) exposes a hosted, remote Model Context Protocol (MCP) server for agent-driven commerce, implemented via the Shopify-native Universal Commerce Protocol (UCP). Agents discover capabiliti
  name: Winc UCP Commerce MCP Server
  slug: winc-ucp-commerce-mcp-server
modified: '2026-07-21'
name: Winc
nav: Providers
network: true
overview: 'Winc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wine, E-Commerce, Retail, and Subscription.


  Winc''s developer surface includes authentication and 10 more developer resources.'
random_paper: 13
scopes:
- name: Winc Scopes
  scope_count: 0
  slug: winc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 13.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 16.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/winc/refs/heads/main/screenshots/winc-2026-09-02T170754.png
security:
- kind: authentication
  name: Winc Authentication
  slug: winc-authentication
  summary_line: 1 scheme
slug: winc
tags:
- Company
- Wine
- E-Commerce
- Retail
- Subscription
- Agentic Commerce
- MCP
- Shopify
- UCP
website: https://winc.com
---
