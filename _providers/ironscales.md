---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: The public IRONSCALES Management API — a Swagger 2.0 (drf-yasg) contract covering incident retrieval and classification, account-takeover remediation, mitigation and email statistics, escalated emails
  name: IRONSCALES Management API
  slug: ironscales-management-api
- description: Remote Model Context Protocol server operated by IRONSCALES at mcp.ironscales.com, served over streamable HTTP at /mcp/. Access is OAuth 2.0 protected — an unauthenticated tools/list returns an RFC 67
  name: IRONSCALES MCP Server
  slug: ironscales-mcp-server
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ironscales-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ironscales-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ironscales-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ironscales.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://appapi.ironscales.com/appapi/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://ironscales.com/platform/api
- group: docs
  title: ''
  type: APIReference
  url: https://appapi.ironscales.com/appapi/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://ironscales.com/platform/api
- group: operate
  title: ''
  type: Support
  url: https://ironscales.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.ironscales.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://ironscales.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ironscales.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://secure.ironscales.com/free-trial
- group: start
  title: ''
  type: Login
  url: https://members.ironscales.com/signin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ironscales.com/hubfs/PDFs/Ironscales%20EULA%20Template%20(January%202025).pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ironscales.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ironscales.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://ironscales.com/blog/tag/release-notes
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ironscales.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ironscales.com/
- group: auth
  title: ''
  type: Security
  url: https://trust.ironscales.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ironscales-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ironscales-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ironscales-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ironscales-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ironscales-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ironscales-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ironscales-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ironscales-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ironscales-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ironscales-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ironscales-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/ironscales-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: IRONSCALES is an AI-powered, API-based email security platform protecting organizations against phishing, business email compromise (BEC), account takeover (ATO), VIP impersonation, QR-code phishing, malicious URLs and attachments, and deepfake-assisted social engineering. Rather than sitting inline as a secure email gateway, IRONSCALES connects to Microsoft 365 and Google Workspace through their APIs and operates at the mailbox level — no MX record changes — combining adaptive AI detection, computer-vision analysis, automated multi-mailbox remediation, a crowdsourced threat-intelligence network, phishing simulation testing, and security awareness training in one platform. The public IRONSCALES Management API (appapi.ironscales.com) exposes incidents, mitigation statistics, escalated emails, mailbox management, deepfake SIEM events, phishing-simulation campaigns, SAT training campaigns, and tenant security settings, and is the surface behind the company's SIEM/SOAR/XDR integrations.
  IRONSCALES also operates an OAuth-protected remote MCP server for agent-based access.
image: https://ironscales.com/hubfs/Icons%20and%20Logos/ironscales_icon_only_dark_blue-01.svg
layout: provider
mcp_servers:
- description: ''
  name: ironscales-mcp.yml
  slug: ironscales-mcpyml
modified: '2026-08-04'
name: IRONSCALES
nav: Providers
network: true
overview: 'IRONSCALES publishes 1 API on the [APIs.io](https://apis.io/) network: Management API. Tagged areas include email-security, cybersecurity, phishing, anti-phishing, and business-email-compromise.


  IRONSCALES''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 58
rate_limits:
- limit_count: 1
  name: Ironscales Rate Limits
  slug: ironscales-rate-limits
score:
  band: strong
  composite: 56.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 52.7
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 63.2
  previous_composite: 56.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Ironscales Authentication
  slug: ironscales-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Ironscales Domain Security
  slug: ironscales-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ironscales Vulnerability Disclosure
  slug: ironscales-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Ironscales Trust Center
  slug: ironscales-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 42001:2023, SOC 2 Type 2
slug: ironscales
tags:
- email-security
- cybersecurity
- phishing
- anti-phishing
- business-email-compromise
- account-takeover
- threat-intelligence
- incident-response
- security-awareness-training
- phishing-simulation
- microsoft-365
- google-workspace
- soc-automation
- deepfake-detection
- mcp
website: https://ironscales.com/
---
