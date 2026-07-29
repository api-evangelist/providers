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
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: Account management
  name: Sigma360 Account API
  slug: sigma-ratings-account-api
- description: Informational endpoints
  name: Sigma360 Informational API
  slug: sigma-ratings-informational-api
- description: Creating new 'My Entities'
  name: 'Sigma360 Monitoring: Entity Creation API'
  slug: sigma-ratings-monitoring-entity-creation-api
- description: Browsing and retrieving monitored entities
  name: 'Sigma360 Monitoring: Entity Management API'
  slug: sigma-ratings-monitoring-entity-management-api
- description: Retrieving monitoring history
  name: 'Sigma360 Monitoring: History API'
  slug: sigma-ratings-monitoring-history-api
- description: Screening against Sigma360's risk data
  name: Sigma360 One-Off Screening API
  slug: sigma-ratings-one-off-screening-api
- description: General utilities
  name: Sigma360 Utilities API
  slug: sigma-ratings-utilities-api
artifact_total: 14
asyncapis:
- description: Event surface for Sigma360; webhook callbacks are delivered to your registered HTTPS endpoint when monitored entities change. Derived from the OpenAPI 3.1 webhooks object published at docs.sigma360.co
  name: Sigma360 Webhooks
  slug: sigma-ratings-webhooks-asyncapi
- description: ''
  name: Sigma Ratings Webhooks
  slug: sigma-ratings-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.sigma360.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sigma360.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sigma360.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sigma360.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sigma360.com/docs/user-guide/intro
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.sigma360.com/docs/release-notes
- group: operate
  title: ''
  type: StatusPage
  url: https://sigma360status.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.sigma360.com/free-trial/
- group: start
  title: ''
  type: Login
  url: https://app.sigma360.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@sigma360.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sigma360.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.sigma360.com/security-and-disclosure-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sigma360.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sigma360.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/sigma-ratings-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sigma-ratings-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sigma-ratings-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sigma-ratings-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sigma-ratings-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sigma-ratings-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sigma-ratings-openapi-overlay.yaml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/sigma-ratings-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sigma-ratings-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sigma-ratings-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sigma-ratings-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sigma-ratings-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sigma-ratings-domain-security.yml
created: '2026-07-17'
description: Sigma360 (formerly Sigma Ratings) is a financial-crime-compliance platform for sanctions and watchlist screening, AML investigations, adverse-media screening, enhanced due diligence, perpetual KYC, third-party risk management, country risk ratings, and counterparty credit-risk monitoring. Its REST API (OpenAPI 3.1, v2.0.1) lets you screen entities against risk data, enroll them for continuous monitoring, retrieve risk profiles and change history, and subscribe to webhook events — authenticated with an API key over https://api.sigma360.com/external/v2.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sigma-ratings.png
layout: provider
mcp_servers:
- description: ''
  name: sigma-ratings-mcp.yml
  slug: sigma-ratings-mcpyml
modified: '2026-07-21'
name: Sigma360
nav: Providers
network: true
overview: 'Sigma360 publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Informational API, Monitoring: Entity Creation API, and 4 more. Tagged areas include Company, Compliance, Financial Crime, KYC, and AML.


  The Sigma360 catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Sigma360''s developer surface includes documentation, API reference, getting-started guide, changelog, signup flow, support, authentication, and 21 more developer resources.'
random_paper: 54
score:
  band: developing
  composite: 52.6
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.3
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 50.0
  previous_composite: 54.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sigma Ratings Authentication
  slug: sigma-ratings-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sigma Ratings Domain Security
  slug: sigma-ratings-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sigma Ratings Vulnerability Disclosure
  slug: sigma-ratings-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Sigma Ratings Trust Center
  slug: sigma-ratings-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: sigma-ratings
tags:
- Company
- Compliance
- Financial Crime
- KYC
- AML
- Sanctions Screening
- Risk Intelligence
- RegTech
- Adverse Media
website: https://www.sigma360.com/
---
