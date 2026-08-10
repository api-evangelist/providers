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
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Versioned REST API (v1 / v3) for programmatic access to Cyera's data discovery, classification, access-exposure, and risk findings. Secured with OAuth 2.0 client_credentials (Client ID + Client Secret
  name: Cyera API
  slug: cyera-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.cyera.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.cyera.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://support.cyera.io/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://api.cyera.io/docs
- group: operate
  title: ''
  type: Support
  url: https://support.cyera.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.cyera.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cyera.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.cyera.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cyera.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cyera.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cyera.io
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cyera-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cyera-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cyera-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cyera-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cyera-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cyera-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.cyera.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/cyera-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cyera-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cyera.com/legal/vulnerability-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyera-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cyera-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cyera-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cyera-llms.txt
created: '2026-07-17'
description: Cyera is an AI-native data security company whose Data Security Posture Management (DSPM) platform discovers, classifies, and secures sensitive data across cloud service providers (AWS, GCP, Azure), SaaS applications, data warehouses, and on-premises stores using an agentless architecture that scans hundreds of petabytes without impacting performance. Cyera exposes a versioned REST API (api.cyera.io, with an EU region at api-eu.cyera.io) secured with OAuth 2.0 / OpenID Connect and short-lived JWT bearer tokens, a published Model Context Protocol server (Cyera MCP over DataPort, a per-customer managed Snowflake warehouse) for natural-language querying of data-security findings, and a SafeBase-powered trust center covering SOC 2, ISO 27001, PCI DSS, HIPAA, and GDPR. It was surfaced as a portfolio company of Lightspeed Venture Partners and enriched by the API Evangelist pipeline.
image: https://cdn.prod.website-files.com/69443372754a5005a10559a5/6992ed2b1e335ac321854654_Cyera-Protect-your-data-Secure%20AI.png
layout: provider
mcp_servers:
- description: ''
  name: cyera-mcp.yml
  slug: cyera-mcpyml
modified: '2026-07-18'
name: Cyera
nav: Providers
network: true
overview: 'Cyera publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Data Security, DSPM, and Data Security Posture Management.


  Cyera''s developer surface includes documentation, API reference, support, engineering blog, pricing, changelog, authentication, and 18 more developer resources.'
random_paper: 68
scopes:
- name: Cyera Scopes
  scope_count: 3
  slug: cyera-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 42.1
  previous_composite: 37.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cyera/refs/heads/main/screenshots/cyera-2026-07-25T211042.png
security:
- kind: authentication
  name: Cyera Authentication
  slug: cyera-authentication
  summary_line: oauth2/openIdConnect/http · 3 schemes
- kind: domain-security
  name: Cyera Domain Security
  slug: cyera-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cyera Vulnerability Disclosure
  slug: cyera-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Cyera Trust Center
  slug: cyera-trust-center
  summary_line: SOC 2, ISO/IEC 27001, PCI DSS, HIPAA, GDPR, CCPA, C5, EU-US Data Privacy Framework, VPAT
slug: cyera
tags:
- Company
- Cybersecurity
- Data Security
- DSPM
- Data Security Posture Management
- Data Classification
- Cloud Security
- Compliance
- MCP
- AI Security
website: https://www.cyera.com
---
