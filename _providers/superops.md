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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.6
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: GraphQL API for MSPs covering clients, tickets, assets, users, invoices, knowledge base, and service catalog. US and EU data centers.
  name: SuperOps MSP GraphQL API
  slug: superops-msp-graphql-api
- description: GraphQL API for internal IT teams covering assets, tickets, users, knowledge base, service catalog, and IT documentation. US and EU data centers.
  name: SuperOps IT GraphQL API
  slug: superops-it-graphql-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://superops.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.superops.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.superops.com/en/collections/3666305-api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://support.superops.com/en/articles/6632215-how-to-integrate-applications-using-superops-ai-graphql-apis
- group: operate
  title: ''
  type: Support
  url: https://support.superops.com
- group: company
  title: ''
  type: Blog
  url: https://superops.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://superops.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://superops.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://superops.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://superops.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.superops.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superopsai
- group: auth
  title: ''
  type: Authentication
  url: authentication/superops-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/superops-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/superops-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/superops-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/superops-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/superops-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://superops.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/superops-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/superops-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://superops.com/security/responsible-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superops-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/superops-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/superops-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/superops-llms.txt
created: '2026-07-17'
description: SuperOps is a unified PSA (Professional Services Automation) and RMM (Remote Monitoring and Management) platform for managed service providers (MSPs) and internal IT teams, spanning service desk and ticketing, endpoint monitoring, patch management, asset and IT documentation, project management, billing and invoicing, and AI-assisted operations. SuperOps exposes a public GraphQL API with separate MSP and IT surfaces across US and EU data centers, giving programmatic access to clients, tickets, assets, users, invoices, knowledge base, and service catalog data. Requests authenticate with a bearer API token plus a CustomerSubDomain header and are limited to 800 requests per minute.
image: https://us-west-2.graphassets.com/AsRMKMrtKTFW6TGbr4KgUz/cmo8lbrrc1xga07n3l58jhure
layout: provider
mcp_servers:
- description: ''
  name: superops-mcp.yml
  slug: superops-mcpyml
modified: '2026-07-21'
name: SuperOps
nav: Providers
network: true
overview: 'SuperOps publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, It Management Software, PSA, RMM, and MSP.


  SuperOps'' developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 106
rate_limits:
- limit_count: 2
  name: Superops Rate Limits
  slug: superops-rate-limits
score:
  band: thin
  composite: 41.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 49.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 68.4
  previous_composite: 41.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Superops Authentication
  slug: superops-authentication
  summary_line: http-bearer/apiKey · 2 schemes
- kind: domain-security
  name: Superops Domain Security
  slug: superops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Superops Vulnerability Disclosure
  slug: superops-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Superops Trust Center
  slug: superops-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, HIPAA, GDPR
slug: superops
tags:
- Company
- It Management Software
- PSA
- RMM
- MSP
- Service Desk
- Endpoint Management
- IT Documentation
- GraphQL
website: https://superops.com
---
