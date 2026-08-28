---
access_model:
  confidence: high
  label: Demo-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://brand.ai/faq/
  - https://brand.ai/book-a-demo/
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'A hosted, remote Model Context Protocol server that lets an AI agent read a company''s Brand OS — brands, machine-readable brand rules and artifacts — and write back Brand Check validations, artifacts '
  name: Brand.ai MCP Server
  slug: brandai-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://brand.ai
- group: company
  title: ''
  type: Blog
  url: https://brand.ai/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brand.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brand.ai/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brand.ai/legal/terms/
- group: auth
  title: ''
  type: Security
  url: https://brand.ai/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.brand.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://brand.ai/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/brandai-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brandai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/brandai-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brandai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brandai-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brandai-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brandai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brandai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/brandai-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brandai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brandai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brandai-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/brandai-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/brandai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brandai-rate-limits.yml
created: '2026-07-17'
description: 'Brand.ai (Access to Tools Inc.) is a San Francisco-based AI platform that turns a company''s brand into machine-readable infrastructure — "your brand, as source code" — so that every team, tool and AI agent works from one enforced brand context. The product has two halves: Brand OS, which structures brand data through Brand Foundation (guidelines compiled into machine-readable rules), Brand Ontology (150+ perception dimensions), Daily Signals and OAuth-connected applications (Figma, Notion, Google Drive, Slack, Shopify); and Brand Studio, which executes on it through Assistant (built on Claude), the Canvas visual strategy sandbox, Projects and Brand Check pre-launch risk validation. Founded in 2024 and backed by Uncork Capital, it targets brand leaders, agencies and enterprise teams. Brand.ai publishes no developer portal, no OpenAPI and no SDKs, and the product itself is demo-gated with no self-serve sign-up or published pricing — but it does operate a real hosted remote MCP
  server at https://app.brand.ai/api/mcp, gated by a full OAuth 2.0 / OpenID Connect authorization server with open Dynamic Client Registration and nine Brand OS resource scopes. Security posture is published: SOC 2 Type II, GDPR, CCPA, a Vanta trust center and a public status page.'
image: https://cdn.sanity.io/images/3zwn2ers/fullsite/1e9606e67a676cbdfd3d4d66f10f4184e9bf7c8f-1800x942.png?w=1200&auto=format
layout: provider
mcp_servers:
- description: ''
  name: Brand.ai MCP Server
  slug: brandai-mcp-server
modified: '2026-08-13'
name: Brand.ai
nav: Providers
network: true
overview: 'Brand.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Brand Management, Artificial Intelligence, Marketing, and Software-as-a-Service.


  Brand.ai''s developer surface includes engineering blog, authentication, and 21 more developer resources.'
plans:
- name: Brandai Plans Pricing
  plan_count: 0
  slug: brandai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Brandai Rate Limits
  slug: brandai-rate-limits
scopes:
- name: Brandai Scopes
  scope_count: 13
  slug: brandai-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: emerging
  composite: 23.8
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 79.6
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 23.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Brandai Authentication
  slug: brandai-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Brandai Domain Security
  slug: brandai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Brandai Trust Center
  slug: brandai-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA
slug: brandai
tags:
- Company
- Brand Management
- Artificial Intelligence
- Marketing
- Software-as-a-Service
- Brand Operating System
- AI Agents
- Design
- MCP
- Brand Governance
- Brand Intelligence
website: https://brand.ai
---
