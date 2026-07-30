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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Workspace-scoped REST API for embedding Improvado's data extraction, transformation, and load pipeline into agency and platform products. Manages data sources, connections, accounts, extraction templa
  name: Improvado Embedded API v3
  slug: improvado-embedded-api-v3
artifact_total: 7
asyncapis:
- description: ''
  name: Improvado Webhooks
  slug: improvado-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://improvado.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.improvado.io/api
- group: docs
  title: ''
  type: Documentation
  url: https://developers.improvado.io/api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.improvado.io/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.improvado.io/introduction
- group: company
  title: ''
  type: Blog
  url: https://improvado.io/blog
- group: operate
  title: ''
  type: Support
  url: https://improvado.io/help
- group: commercial
  title: ''
  type: Pricing
  url: https://improvado.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://improvado.io/register/talk-to-an-expert
- group: start
  title: ''
  type: Login
  url: https://report.improvado.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://improvado.io/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://improvado.io/company-legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.improvado.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.improvado.io/changelog
- group: auth
  title: ''
  type: TrustCenter
  url: security/improvado-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.improvado.io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/improvado-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/improvado-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/improvado-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/improvado-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/improvado-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://improvado.io/company-legal/responsible-disclosure-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/improvado-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/improvado-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/improvado-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/improvado-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/improvado-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/improvado-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/improvado-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/improvado-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/improvado-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Improvado is a marketing intelligence and AI-agent platform that connects, extracts, transforms, and loads data from 876+ marketing, advertising, sales, and analytics sources into governed data pipelines, warehouses, and BI tools. Its Embedded API v3 (base https://embedded.improvado.io, all paths under /api/v3/) gives agencies and platforms programmatic, workspace-scoped control over data sources, connections and accounts, extraction templates and extracts, destinations, data tables, loads, automated recipes, custom roles, and webhook endpoints for load, transformation, and extraction lifecycle events. Authentication is HTTP Basic for workspace management and short-lived Bearer tokens for workspace-scoped resources. The platform maintains a SOC 2 / HIPAA / GDPR trust center, a public status page, a dated API changelog, and a responsible-disclosure security program.
image: https://improvado.io/-/astro/logo.png
layout: provider
mcp_servers:
- description: ''
  name: improvado-mcp.yml
  slug: improvado-mcpyml
modified: '2026-07-19'
name: Improvado
nav: Providers
network: true
overview: 'Improvado publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Marketing Intelligence, Marketing Analytics, and Data Pipeline.


  The Improvado catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Improvado''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 25 more developer resources.'
random_paper: 75
score:
  band: developing
  composite: 52.9
  delta: 5.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 56.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 50.0
  previous_composite: 47.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/improvado/refs/heads/main/screenshots/improvado-2026-07-25T222205.png
security:
- kind: authentication
  name: Improvado Authentication
  slug: improvado-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Improvado Domain Security
  slug: improvado-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Improvado Vulnerability Disclosure
  slug: improvado-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Improvado Trust Center
  slug: improvado-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: improvado
tags:
- Company
- Marketing
- Marketing Intelligence
- Marketing Analytics
- Data Pipeline
- ETL
- Advertising Data
- Business Intelligence
- Data Integration
- AI Agents
website: https://improvado.io
---
