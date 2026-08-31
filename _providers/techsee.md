---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.4
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/techsee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://techsee.com/
- group: company
  title: ''
  type: About
  url: https://techsee.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://techsee.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://techsee.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://techsee.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://techsee.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://techsee.atlassian.net/servicedesk/customer/portal/5
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TechSeeDev
- group: start
  title: ''
  type: Login
  url: https://app.techsee.me/
- group: build
  title: ''
  type: Packages
  url: packages/techsee-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/techsee-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/techsee-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/techsee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/techsee-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/techsee-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/techsee-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/techsee-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/techsee-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/techsee-conformance.yml
created: '2026-08-29'
description: TechSee is an Israeli-founded customer-experience software company that builds visual assistance and visual agentic AI for customer service, contact centers and field service. Its platform — TechSee Live for agent-guided visual sessions and Sophie AI for autonomous multimodal virtual agents — combines live video, computer vision, augmented reality overlays and screen sharing so that a support agent or an AI agent can see what a customer sees and guide them to a resolution. TechSee sells into telecommunications, insurance, utilities, consumer electronics, home builders, medical devices, retail and BPO, and markets an "open integration platform" of APIs plus prebuilt connectors for Salesforce, ServiceNow, Zendesk, Amazon Connect, Oracle, Pega, Microsoft Dynamics 365, Amdocs and CSG. Public developer artifacts are limited to an iOS mobile SDK on GitHub; the API reference itself is not published publicly.
image: https://techsee.com/wp-content/uploads/2024/08/logos-03.svg
layout: provider
mcp_servers:
- description: ''
  name: TechSee MCP Server
  slug: techsee-mcp-server
modified: '2026-08-29'
name: TechSee
nav: Providers
network: true
overview: 'TechSee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Visual Assistance, Customer Experience, Customer Service, and Contact Center.


  TechSee''s developer surface includes engineering blog, pricing, support, authentication, and 16 more developer resources.'
plans:
- name: Techsee Plans Pricing
  plan_count: 0
  slug: techsee-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Techsee Rate Limits
  slug: techsee-rate-limits
scopes:
- name: Techsee Scopes
  scope_count: 0
  slug: techsee-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 24.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Techsee Authentication
  slug: techsee-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Techsee Domain Security
  slug: techsee-domain-security
  summary_line: TLSv1.3 · HSTS
slug: techsee
tags:
- Company
- Visual Assistance
- Customer Experience
- Customer Service
- Contact Center
- Computer-Vision
- Augmented Reality
- Artificial Intelligence
- Field Service
- Remote Support
- Video
- Telecommunications
website: https://techsee.com/
---
