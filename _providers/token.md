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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/token-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.token.security/
- group: company
  title: ''
  type: Blog
  url: https://www.token.security/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tokensec
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.token.security/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.token.security/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/token-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.token.security/
- group: auth
  title: ''
  type: Security
  url: https://trust.token.security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/token-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/token-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/token-mcp.yml
created: '2026-07-17'
description: Token Security is a cybersecurity company that secures non-human identities (NHIs) and AI agents across on-premises, hybrid, and cloud environments. Its platform continuously discovers every AI agent, service account, and machine identity, maps ownership and security posture, detects identity threats, and automates remediation. Capabilities span NHI inventory, security posture management, lifecycle management, secrets, and identity threat detection and response. The company also ships the Token MCP Server and a native Token AI Agent so security teams can query and act on NHI data conversationally from Claude, ChatGPT, Gemini, or Cursor. Backed by Bloomberg Beta, GGV Capital, and Qiming, Token Security serves enterprise security teams, CISOs, and IAM professionals governing machine and agent identity at scale.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/token.png
layout: provider
mcp_servers:
- description: ''
  name: token-mcp.yml
  slug: token-mcpyml
modified: '2026-07-21'
name: Token
nav: Providers
network: true
overview: 'Token is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Non-Human Identity, and Identity and Access Management.


  Token''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 18.1
  delta: -0.2
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 18.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Token Domain Security
  slug: token-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Token Vulnerability Disclosure
  slug: token-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Token Trust Center
  slug: token-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022
slug: token
tags:
- Company
- Security
- Cybersecurity
- Non-Human Identity
- Identity and Access Management
- AI Agents
- Model Context Protocol
website: https://www.token.security/
---
