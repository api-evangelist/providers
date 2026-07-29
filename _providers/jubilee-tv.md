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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://getjubileetv.com/
- group: company
  title: ''
  type: Blog
  url: https://getjubileetv.com/blogs/jubileetv
- group: operate
  title: ''
  type: Support
  url: https://getjubileetv.com/pages/support
- group: commercial
  title: ''
  type: Pricing
  url: https://getjubileetv.com/products/jubilee-tv-direct
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getjubileetv.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getjubileetv.com/policies/terms-of-service
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jubilee-tv-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jubilee-tv-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jubilee-tv-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jubilee-tv-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jubilee-tv-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jubilee-tv-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jubilee-tv-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jubilee-tv-domain-security.yml
created: '2026-07-17'
description: 'JubileeTV (by Caavo) is a US consumer remote-caregiving system that turns an aging loved one''s existing television into a family connection and monitoring hub. A caregiver uses their phone to control the senior''s TV remotely, host multi-way video calls on the big screen, run one-way wellness check-ins, send photos and reminders, and get alerts when TV routines or room activity look off. Hardware plus a subscription membership; no learning curve for the senior. The company publishes no bespoke developer API, but its getjubileetv.com storefront exposes a real agentic-commerce surface on Shopify: an OIDC/OAuth Customer Accounts authorization server, a Universal Commerce Protocol (UCP) merchant profile, a shopping MCP endpoint, and published /llms.txt and /agents.md agent instructions.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jubilee-tv.png
layout: provider
mcp_servers:
- description: ''
  name: jubilee-tv-mcp.yml
  slug: jubilee-tv-mcpyml
modified: '2026-07-19'
name: Jubilee TV
nav: Providers
network: true
overview: 'Jubilee TV is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Caregiving, Seniors, and Smart TV.


  Jubilee TV''s developer surface includes engineering blog, support, pricing, authentication, and 11 more developer resources.'
random_paper: 67
scopes:
- name: Jubilee Tv Scopes
  scope_count: 4
  slug: jubilee-tv-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 21.2
  delta: 1.6
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 19.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Jubilee Tv Authentication
  slug: jubilee-tv-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Jubilee Tv Domain Security
  slug: jubilee-tv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jubilee-tv
tags:
- Company
- Consumer
- Caregiving
- Seniors
- Smart TV
- Video Calling
- Agentic Commerce
- Shopify
website: https://getjubileetv.com/
---
