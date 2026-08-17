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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Arphie's remote Model Context Protocol server. It exposes Arphie projects, workload and project-volume metrics, and the company's agentic chat engine to MCP clients such as Claude, ChatGPT, Cursor, an
  name: Arphie MCP
  slug: arphie-mcp
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arphie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arphie.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.arphie.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.arphie.ai/
- group: start
  title: ''
  type: Login
  url: https://app.arphie.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.arphie.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.arphie.ai/contact
- group: auth
  title: ''
  type: Compliance
  url: https://www.arphie.ai/security
- group: auth
  title: ''
  type: Security
  url: https://www.arphie.ai/responsible-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arphie-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arphie.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arphie.ai/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arphie.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arphie.ai/docs/intro
- group: agent
  title: ''
  type: MCPServer
  url: mcp/arphie-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arphie-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arphie-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arphie-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/arphie-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arphie-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/arphie-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arphie-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/arphie-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/arphie-plans-pricing.yml
created: '2026-07-17'
description: Arphie is an AI-powered knowledge activation platform that helps go-to-market teams automate RFP (Request for Proposal) responses, security questionnaires, and due-diligence questionnaires. Its AI agents draft answers from a company's knowledge base, cite sources with confidence scores, and integrate with knowledge sources such as Google Drive, SharePoint, Confluence, Notion, Seismic, and Highspot. Arphie is used by high-growth and publicly traded companies to win more deals faster while keeping proposal content accurate, current, and auditable. The company is SOC 2 Type 2 compliant, operates zero data retention with model providers, supports SAML 2.0 SSO and role-based access controls, and is backed by General Catalyst. Arphie publishes no REST API and no OpenAPI, but it does operate a live, remote Model Context Protocol server at https://app.arphie.ai/api/mcp — OAuth-protected, with RFC 9728 protected-resource discovery — that brings Arphie projects, workload metrics, and
  agentic chat into Claude, ChatGPT, Cursor, an IDE, or the terminal. Arphie also serves an llms.txt for AI agents. This profile was surfaced as a portfolio lead and enriched by the API Evangelist pipeline.
image: https://cdn.prod.website-files.com/672fc2345132970736914ada/67313797c7d6407f3b2c8a39_Arphie%20Social.jpg
layout: provider
mcp_servers:
- description: ''
  name: arphie-mcp.yml
  slug: arphie-mcpyml
modified: '2026-08-13'
name: Arphie
nav: Providers
network: true
overview: 'Arphie publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Artificial Intelligence, Sales Enablement, and RFP Automation.


  Arphie''s developer surface includes signup flow, engineering blog, support, documentation, getting-started guide, authentication, and 18 more developer resources.'
plans:
- name: Arphie Plans Pricing
  plan_count: 0
  slug: arphie-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 0
  name: Arphie Rate Limits
  slug: arphie-rate-limits
scopes:
- name: Arphie Scopes
  scope_count: 1
  slug: arphie-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 30.8
  delta: 13.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 17.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/arphie/refs/heads/main/screenshots/arphie-2026-07-25T201242.png
security:
- kind: authentication
  name: Arphie Authentication
  slug: arphie-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Arphie Domain Security
  slug: arphie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arphie Vulnerability Disclosure
  slug: arphie-vulnerability-disclosure
  summary_line: disclosure policy published
slug: arphie
tags:
- Company
- Enterprise
- Artificial Intelligence
- Sales Enablement
- RFP Automation
- Security Questionnaires
- Knowledge Management
- Go-To-Market
- MCP
- Agents
website: https://www.arphie.ai/
---
