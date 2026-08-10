---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://kimba.ai/
- group: company
  title: ''
  type: Blog
  url: https://kimba.ai/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://kimba.ai/pages/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kimba.ai/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kimba.ai/policies/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://kimba.ai/account
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kimba-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kimba-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kimba-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kimba-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kimba-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kimba-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kimba-domain-security.yml
created: '2026-07-17'
description: Kimba is an AI-powered sleep technology company building a bedside device that uses personalized scent therapy to improve sleep quality. The device reads biometric data from wearables (Oura, WHOOP, Apple Watch, Garmin), monitors sleep architecture, breathing, movement and disturbances, and releases natural, water-based scent formulations at precise moments in the sleep cycle to enhance rest, reduce nighttime disruptions and support cognitive performance. Kimba is a Techstars-backed direct-to-consumer hardware and subscription brand whose online store runs on Shopify; it exposes an agent-facing commerce surface via the Universal Commerce Protocol (UCP), a hosted MCP endpoint, and Shopify Customer Account API (OIDC) authentication rather than a traditional developer API.
image: https://cdn.shopify.com/s/files/1/0767/5949/8890/files/black_logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Kimba UCP Shopping MCP
  slug: kimba-ucp-shopping-mcp
modified: '2026-07-19'
name: Kimba
nav: Providers
network: true
overview: 'Kimba is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sleep Technology, Consumer Hardware, Health & Wellness, and Artificial Intelligence.


  Kimba''s developer surface includes engineering blog, support, signup flow, authentication, and 9 more developer resources.'
random_paper: 52
scopes:
- name: Kimba Scopes
  scope_count: 4
  slug: kimba-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.9
  provenance:
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kimba/refs/heads/main/screenshots/kimba-2026-08-07T171224.png
security:
- kind: authentication
  name: Kimba Authentication
  slug: kimba-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Kimba Domain Security
  slug: kimba-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kimba
tags:
- Company
- Sleep Technology
- Consumer Hardware
- Health & Wellness
- Artificial Intelligence
- Wearables
- E-Commerce
- Agentic Commerce
website: https://kimba.ai/
---
