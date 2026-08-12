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
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: OAuth 2.0-secured Partner API for programmatic access to Thoropass audits, evidence requests, controls, monitoring alerts, devices, change requests, training records and vulnerability data, plus a hos
  name: Thoropass Partner API
  slug: thoropass-partner-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://thoropass.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.thoropass.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thoropass.com/mcp
- group: operate
  title: ''
  type: Support
  url: https://help.thoropass.com/
- group: company
  title: ''
  type: Blog
  url: https://www.thoropass.com/learn/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thoropass.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.thoropass.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thoropass.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thoropass.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thoropass.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.thoropass.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/thoropass-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/thoropass-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/thoropass-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thoropass-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thoropass-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thoropass-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thoropass-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thoropass-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thoropass-llms.txt
created: '2026-07-17'
description: Thoropass is an auditor-led, AI-powered compliance and audit automation platform that combines software with expert auditor services. Its products span continuous compliance monitoring and alerting, automated evidence collection, a global control library, vulnerability scanning, and CREST-accredited penetration testing, helping companies achieve and maintain SOC 2, ISO 27001, HIPAA, PCI DSS and HITRUST. For developers and integration partners, Thoropass exposes a Partner API secured with OAuth 2.0 (Authorization Code + PKCE, refresh tokens, and RFC 7591 dynamic client registration) and a hosted, OAuth-protected Model Context Protocol (MCP) server for AI-agent access to audits, evidence requests, controls, alerts, devices and vulnerability data. Thoropass (formerly Laika) is backed by Bain Capital Ventures.
image: https://cdn.prod.website-files.com/6891db6efb3a962d3fcde7ae/689b377ec946ba9bb8d243f7_Thoropass_Website_OrO-Way-Hero-1.webp
layout: provider
mcp_servers:
- description: ''
  name: thoropass-mcp.yml
  slug: thoropass-mcpyml
modified: '2026-07-21'
name: Thoropass
nav: Providers
network: true
overview: 'Thoropass publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Compliance, Compliance Automation, and Audit.


  Thoropass'' developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, and 14 more developer resources.'
random_paper: 67
scopes:
- name: Thoropass Scopes
  scope_count: 24
  slug: thoropass-scopes
  summary_line: 24 scopes · authorizationCode
score:
  band: thin
  composite: 29.9
  delta: -1.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 31.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Thoropass Authentication
  slug: thoropass-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Thoropass Domain Security
  slug: thoropass-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Thoropass Trust Center
  slug: thoropass-trust-center
  summary_line: trust center published
slug: thoropass
tags:
- Company
- Fintech
- Compliance
- Compliance Automation
- Audit
- Security
- Cybersecurity
- GRC
- SOC 2
- MCP
website: https://thoropass.com/
---
