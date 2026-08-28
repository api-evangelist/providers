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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 24.7
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The hosted, remote Model Context Protocol server through which peopleIX exposes a customer's People Intelligence knowledge layer to agents such as Claude, ChatGPT and Copilot. A JSON-RPC POST to https
  name: peopleIX MCP
  slug: peopleix-mcp
artifact_total: 8
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/peopleix-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/peopleix-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/peopleix-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/peopleix-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/peopleix-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/peopleix-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/peopleix-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/peopleix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/peopleix-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peopleix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.peopleix.com
- group: company
  title: ''
  type: Blog
  url: https://www.peopleix.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.peopleix.com/en/auth/sign-in
- group: operate
  title: ''
  type: Support
  url: mailto:contact@peopleix.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peopleix.com/privacy
- group: other
  title: ''
  type: Imprint
  url: https://www.peopleix.com/imprint
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/peopleIX
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/peopleix-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/peopleix-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/peopleix-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.peopleix.com
created: '2026-07-17'
description: peopleIX is a People Intelligence platform for HR leaders, built and operated by peopleIX GmbH in Cologne, Germany (founded 2022). It integrates 100+ HR systems (HRIS, ATS, LMS, payroll) and pairs an AI Data Analyst (people analytics — the "what") with AI-led conversations across the workforce (conversation intelligence — the "why") to answer hard workforce questions in hours rather than months. Each engagement leaves a persistent, queryable knowledge layer the customer keeps. That knowledge layer is exposed to agents through a real, hosted, remote MCP server at https://app.peopleix.com/mcp — confirmed live, OAuth 2.1-gated (PKCE S256, dynamic client registration, Clerk-backed), and advertised through RFC 8414 and RFC 9728 discovery documents the application host serves anonymously. peopleIX publishes no OpenAPI, no REST developer portal, and no SDK; the MCP endpoint is the entire developer-facing surface, and its tool inventory sits behind customer authentication. The service
  is EU-resident end-to-end, GDPR compliant and ISO 27001 certified with a Vanta-hosted trust center at https://trust.peopleix.com, and never trains on customer data. Backed by Earlybird, neoteq ventures, ts ventures, and business angels.
image: https://www.peopleix.com/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: peopleIX MCP
  slug: peopleix-mcp
modified: '2026-08-14'
name: Peopleix
nav: Providers
network: true
overview: 'Peopleix publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HR, People Analytics, People Intelligence, and Conversation Intelligence.


  Peopleix''s developer surface includes authentication, engineering blog, support, and 18 more developer resources.'
plans:
- name: Peopleix Plans Pricing
  plan_count: 0
  slug: peopleix-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Peopleix Rate Limits
  slug: peopleix-rate-limits
scopes:
- name: Peopleix Scopes
  scope_count: 0
  slug: peopleix-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.6
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Peopleix Authentication
  slug: peopleix-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Peopleix Domain Security
  slug: peopleix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Peopleix Trust Center
  slug: peopleix-trust-center
  summary_line: ISO 27001, GDPR
slug: peopleix
tags:
- Company
- HR
- People Analytics
- People Intelligence
- Conversation Intelligence
- Human Resources
- Workforce Analytics
- Artificial Intelligence
- MCP
- Germany
website: https://www.peopleix.com
---
