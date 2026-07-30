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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: GraphQL API for programmatic access to core Strise functionality — search companies and persons, screen for PEP/sanctions/ownership, run reviews, manage a monitoring portfolio, and subscribe to webhoo
  name: Strise Connect API
  slug: strise-connect-api
artifact_total: 7
asyncapis:
- description: ''
  name: Strise Webhooks
  slug: strise-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.strise.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.strise.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.strise.ai
- group: docs
  title: ''
  type: APIReference
  url: https://graphql.strise.ai/connect/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.strise.ai/api/onboarding-a-business-customer/
- group: operate
  title: ''
  type: Support
  url: https://docs.strise.ai/help-center/
- group: company
  title: ''
  type: Blog
  url: https://www.strise.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/strise
- group: start
  title: ''
  type: SignUp
  url: https://app.strise.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.strise.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.strise.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.strise.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.strise.ai/technology/compliance-in-strise/
- group: auth
  title: ''
  type: Security
  url: https://docs.strise.ai/technology/bug-bounty-program/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/strise-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/strise-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/strise-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/strise-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/strise-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/strise-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/strise-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/strise-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/strise-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/strise-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/strise-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/strise-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/strise-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Strise is an Oslo-based (founded 2019) AI platform for financial-crime compliance — "The Autonomous FinCrime Department" that European fincrime teams run on. It automates AML and KYC/KYB work across a Knowledge Graph of companies, persons, ownership, PEP/sanctions and adverse-media screening, continuous monitoring, identity verification and risk scoring. Beyond the SaaS modules (SuperData, RiskLense, Compliance Memory, KYB, KYC, Monitoring, IDV, Forms, Grow), Strise exposes its platform programmatically through the Strise Connect API — a GraphQL API for search, screening, portfolio monitoring, reviews and webhooks — and a hosted, OAuth-protected MCP server for AI agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/strise.png
layout: provider
mcp_servers:
- description: ''
  name: strise-mcp.yml
  slug: strise-mcpyml
modified: '2026-07-21'
name: Strise
nav: Providers
network: true
overview: 'Strise publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, RegTech, AML, and KYC.


  The Strise catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Strise''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 52.0
  delta: 7.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.6
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 55.3
  previous_composite: 44.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Strise Authentication
  slug: strise-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Strise Domain Security
  slug: strise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Strise Vulnerability Disclosure
  slug: strise-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Strise Trust Center
  slug: strise-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR
slug: strise
tags:
- Company
- Fintech
- RegTech
- AML
- KYC
- KYB
- Compliance
- Financial Crime
- Screening
- Sanctions
- PEP
- GraphQL
- MCP
website: https://www.strise.ai
---
