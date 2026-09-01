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
  scored_at: '2026-09-01'
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
overview: 'Kimba is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sleep Technology, Consumer Hardware, Health and Wellness, and Artificial Intelligence.


  Kimba''s developer surface includes engineering blog, support, signup flow, authentication, and 9 more developer resources.'
random_paper: 12
scopes:
- name: Kimba Scopes
  scope_count: 4
  slug: kimba-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Health and Wellness
- Artificial Intelligence
- Wearables
- E-Commerce
- Agentic Commerce
website: https://kimba.ai/
---
