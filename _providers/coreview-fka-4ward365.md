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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 25.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: The CoreView Public API provides programmatic access to Microsoft 365 governance operations — delegated administration, operators, platform reporting, license pools, and customer/tenant management — v
  name: CoreView Public API
  slug: coreview-public-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.coreview.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.coreview.com/en_US/how-tos-APIs
- group: docs
  title: ''
  type: Documentation
  url: https://help.coreview.com/en_US/how-tos-APIs
- group: docs
  title: ''
  type: APIReference
  url: https://help.coreview.com/api-authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://help.coreview.com/api-authentication
- group: operate
  title: ''
  type: Support
  url: https://help.coreview.com/
- group: company
  title: ''
  type: Blog
  url: https://www.coreview.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coreview.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coreview.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coreview.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coreview.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/coreview-fka-4ward365-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coreview-fka-4ward365-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://identity.coreview.com/.well-known/openid-configuration
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coreview-fka-4ward365-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coreview-fka-4ward365-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coreview-fka-4ward365-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/coreview-fka-4ward365-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/coreview-fka-4ward365-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coreview-fka-4ward365-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coreview-fka-4ward365-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coreview-fka-4ward365-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coreview-fka-4ward365-llms.txt
created: '2026-07-17'
description: CoreView (formerly 4ward365) is an enterprise Microsoft 365 governance, security, and automation platform. It secures the configuration, identity, and access layers of Microsoft 365 tenants and provides delegated administration, license management, reporting, and workflow automation. CoreView exposes a Public API secured with OAuth 2.0 / OpenID Connect (client-credentials flow) through a regional API proxy, plus a CoreFlow Workflow API for triggering and monitoring automation runs. Datacenters are available across the EU, East US, Canada, UK, Australia, and US Government (FedRAMP) regions. This profile was surfaced as a portfolio company of Insight Partners and enriched from CoreView's public developer documentation.
image: https://logo.clearbit.com/coreview.com
layout: provider
mcp_servers:
- description: ''
  name: coreview-fka-4ward365-mcp.yml
  slug: coreview-fka-4ward365-mcpyml
modified: '2026-07-18'
name: CoreView (FKA 4ward365)
nav: Providers
network: true
overview: 'CoreView (FKA 4ward365) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Microsoft 365, SaaS Management, Governance, and Security.


  CoreView (FKA 4ward365)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 16 more developer resources.'
random_paper: 0
scopes:
- name: Coreview Fka 4Ward365 Scopes
  scope_count: 14
  slug: coreview-fka-4ward365-scopes
  summary_line: 14 scopes · clientCredentials
score:
  band: thin
  composite: 33.0
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 33.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coreview-fka-4ward365/refs/heads/main/screenshots/coreview-fka-4ward365-2026-07-25T210431.png
security:
- kind: authentication
  name: Coreview Fka 4Ward365 Authentication
  slug: coreview-fka-4ward365-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Coreview Fka 4Ward365 Domain Security
  slug: coreview-fka-4ward365-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Coreview Fka 4Ward365 Trust Center
  slug: coreview-fka-4ward365-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, CIS, FedRAMP, IRAP, GDPR
slug: coreview-fka-4ward365
tags:
- Company
- Microsoft 365
- SaaS Management
- Governance
- Security
- Identity
- Automation
- Workflow
- License Management
- IT Operations
website: https://www.coreview.com/
---
