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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'RESTful API (v3) for managing assets and retrieving attack-surface and scan data — surface-monitoring domains and IPs, IP addresses, technologies, ports, breaches, and cloud connectors. Authenticates '
  name: Detectify REST API
  slug: detectify-rest-api
artifact_total: 7
asyncapis:
- description: ''
  name: Detectify Webhooks
  slug: detectify-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://detectify.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.detectify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.detectify.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.detectify.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.detectify.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.detectify.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.detectify.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/detectify
- group: commercial
  title: ''
  type: Pricing
  url: https://detectify.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://detectify.com/createaccount
- group: commercial
  title: ''
  type: TermsOfService
  url: https://detectify.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://detectify.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.detectify.com/
- group: auth
  title: ''
  type: Security
  url: https://detectify.com/responsible-disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://docs.detectify.com/security-and-compliance
- group: auth
  title: ''
  type: Authentication
  url: authentication/detectify-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/detectify-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/detectify-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/detectify-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/detectify-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/detectify-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/detectify-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/detectify-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/detectify-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/detectify-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/detectify-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/detectify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/detectify-trust-center.yml
created: '2026-07-17'
description: Detectify is an External Attack Surface Management (EASM) and Dynamic Application Security Testing (DAST) platform that continuously discovers an organization's internet-facing assets and runs real, payload-based vulnerability tests against them. Its testing engine is fuelled by Crowdsource, a network of ~400 vetted ethical hackers who contribute 1,765+ vulnerability modules at a ~99.7% true-positive rate. Detectify ships four products — Surface Monitoring (attack surface management), Application Scanning (web app DAST), API Scanning (OpenAPI-driven API security testing), and Internal Scanning — plus a REST API (v3), a remotely-hosted MCP server for AI-driven workflows, and integrations for Jira, Slack, Splunk, and CI/CD. Founded in Stockholm and backed by Balderton Capital and Insight Partners.
image: https://d35ayjp87i0qx4.cloudfront.net/detectify_global.png
layout: provider
mcp_servers:
- description: ''
  name: detectify-mcp.yml
  slug: detectify-mcpyml
modified: '2026-07-18'
name: detectify
nav: Providers
network: true
overview: 'detectify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Attack Surface Management, and EASM.


  The detectify catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  detectify''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 70
score:
  band: developing
  composite: 52.5
  delta: 8.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 44.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/detectify/refs/heads/main/screenshots/detectify-2026-07-25T211804.png
security:
- kind: authentication
  name: Detectify Authentication
  slug: detectify-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Detectify Domain Security
  slug: detectify-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Detectify Vulnerability Disclosure
  slug: detectify-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Detectify Trust Center
  slug: detectify-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: detectify
tags:
- Company
- Security
- Cybersecurity
- Attack Surface Management
- EASM
- Vulnerability Scanning
- DAST
- Application Security
- API Security
website: https://detectify.com/
---
