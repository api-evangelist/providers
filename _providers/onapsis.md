---
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
- description: GraphQL-based public API for The Onapsis Platform. Introduced with support for Assess (vulnerability and scan results) and preliminary support for Comply, it powers third-party integrations with ticke
  name: Onapsis Platform API
  slug: platform-graphql
artifact_total: 6
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/onapsis-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://onapsis.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/onapsis_stock/
- group: docs
  title: ''
  type: Documentation
  url: https://onapsis.com/platform/
- group: operate
  title: ''
  type: Support
  url: https://onapsis.com/support/
- group: company
  title: ''
  type: Blog
  url: https://onapsis.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://onapsis.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Onapsis
- group: start
  title: ''
  type: Login
  url: https://onapsis.com/customer-portal/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onapsis.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onapsis.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://onapsis.com/security-vulnerability-reporting-guidelines/
- group: auth
  title: ''
  type: Compliance
  url: https://onapsis.com/compliance-resources/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onapsis-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/onapsis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/onapsis-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onapsis-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/onapsis-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onapsis-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onapsis-authentication.yml
created: '2026-08-04'
description: Onapsis is a cybersecurity and compliance company for business-critical applications — SAP, Oracle and Salesforce — headquartered in Boston with offices in Buenos Aires and Heidelberg. The Onapsis Platform delivers vulnerability management (Assess), threat detection and response (Defend), secure SAP development and transport control (Control), continuous compliance (Comply) and an AI-driven Security Advisor, backed by the threat intelligence produced by Onapsis Research Labs. The platform exposes a GraphQL-based public API for third-party integrations, custom reporting and workflow automation, authenticated with a UI-generated API key exchanged for a bearer token; the API is served from each customer's own Onapsis console rather than from a shared multi-tenant host, and the API reference is published inside the customer portal. Onapsis previewed an MCP Gateway for SAP Security in March 2026 to let corporate-sanctioned AI agents invoke platform capabilities and Research Labs
  threat intelligence.
image: https://onapsis.com/wp-content/uploads/Onapsis-Featured-Image.png
layout: provider
mcp_servers:
- description: ''
  name: onapsis-mcp.yml
  slug: onapsis-mcpyml
modified: '2026-08-04'
name: Onapsis
nav: Providers
network: true
overview: 'Onapsis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Application Security, Vulnerability Management, and Compliance.


  Onapsis'' developer surface includes documentation, support, engineering blog, changelog, authentication, and 15 more developer resources.'
random_paper: 69
score:
  band: thin
  composite: 30.2
  delta: 0.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 29.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onapsis/refs/heads/main/screenshots/onapsis-2026-08-07T190215.png
security:
- kind: authentication
  name: Onapsis Authentication
  slug: onapsis-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Onapsis Domain Security
  slug: onapsis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Onapsis Vulnerability Disclosure
  slug: onapsis-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Onapsis Trust Center
  slug: onapsis-trust-center
  summary_line: ISO/IEC 27001:2022, O-TTPS (ISO/IEC 20243:2023), SOC 1 Type II, SOC 2 Type II, TISAX AL3, EU-US Data Privacy Framework, Veracode Verified
slug: onapsis
tags:
- Company
- Cybersecurity
- Application Security
- Vulnerability Management
- Compliance
- SAP
- ERP
- Threat Detection
- GraphQL
- Enterprise Software
website: https://onapsis.com/
---
