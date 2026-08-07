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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Jebbit Agentic Access
  operation_count: 37
  slug: jebbit-agentic-access
  summary_line: 37 operations · 19 acting
api_count: 10
apis:
- description: The Auth API from Jebbit — 1 operation(s) for auth.
  name: Jebbit Auth API
  slug: jebbit-auth-api
- description: The Businesses API from Jebbit — 1 operation(s) for businesses.
  name: Jebbit Businesses API
  slug: jebbit-businesses-api
- description: The Campaigns API from Jebbit — 2 operation(s) for campaigns.
  name: Jebbit Campaigns API
  slug: jebbit-campaigns-api
- description: The Feed Columns API from Jebbit — 2 operation(s) for feed columns.
  name: Jebbit Feed Columns API
  slug: jebbit-feed-columns-api
- description: The Feed Rows API from Jebbit — 2 operation(s) for feed rows.
  name: Jebbit Feed Rows API
  slug: jebbit-feed-rows-api
- description: The Feeds API from Jebbit — 4 operation(s) for feeds.
  name: Jebbit Feeds API
  slug: jebbit-feeds-api
- description: The Integration Historic Backfills API from Jebbit — 2 operation(s) for integration historic backfills.
  name: Jebbit Integration Historic Backfills API
  slug: jebbit-integration-historic-backfills-api
- description: The Integration Mappings API from Jebbit — 2 operation(s) for integration mappings.
  name: Jebbit Integration Mappings API
  slug: jebbit-integration-mappings-api
- description: The Integrations API from Jebbit — 3 operation(s) for integrations.
  name: Jebbit Integrations API
  slug: jebbit-integrations-api
- description: The Launch Links API from Jebbit — 1 operation(s) for launch links.
  name: Jebbit Launch Links API
  slug: jebbit-launch-links-api
artifact_total: 18
asyncapis:
- description: ''
  name: Jebbit Webhooks
  slug: jebbit-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://jebbit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.jebbit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.jebbit.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.jebbit.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://support-experiences.blueconic.com/en/articles/246971-api-overview
- group: operate
  title: ''
  type: Support
  url: https://support-experiences.blueconic.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support-experiences.blueconic.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.blueconic.com/category/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jebbit
- group: start
  title: ''
  type: Login
  url: https://app.jebbit.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blueconic.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blueconic.com/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/jebbit-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jebbit-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jebbit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jebbit-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/jebbit-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jebbit-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jebbit-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jebbit-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jebbit-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/jebbit-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/jebbit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jebbit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/jebbit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jebbit-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jebbit-agentic-access.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jebbit-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/jebbit-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/jebbit-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jebbit-llms.txt
created: '2026-07-17'
description: Jebbit — now BlueConic Experiences — is an interactive experience platform that captures zero- and first-party declared data from consumers through quizzes, product finders, personality tests, and preference flows that shoppers complete because the experience gives them value in return. Responses sync into customer profiles and activate across the marketing stack in real time. Jebbit exposes a public JSON:API REST API (https://api2.jebbit.com) for managing businesses, campaigns, launch links, dynamic product feeds, and webhook integrations that stream user session data, secured with OAuth 2.0 client-credentials JWTs and HMAC-signed webhooks.
image: https://www.blueconic.com/experiences-by-jebbit
layout: provider
mcp_servers:
- description: ''
  name: jebbit-mcp.yml
  slug: jebbit-mcpyml
modified: '2026-07-19'
name: Jebbit
nav: Providers
network: true
overview: 'Jebbit publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Businesses API, Campaigns API, and 7 more. Tagged areas include Company, Interactive Experiences, Zero-Party Data, First-Party Data, and Marketing.


  The Jebbit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Jebbit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 25 more developer resources.'
random_paper: 59
scopes:
- name: Jebbit Scopes
  scope_count: 6
  slug: jebbit-scopes
  summary_line: 6 scopes
score:
  band: developing
  composite: 53.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.1
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jebbit/refs/heads/main/screenshots/jebbit-2026-07-25T223113.png
security:
- kind: authentication
  name: Jebbit Authentication
  slug: jebbit-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Jebbit Domain Security
  slug: jebbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jebbit Vulnerability Disclosure
  slug: jebbit-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Jebbit Trust Center
  slug: jebbit-trust-center
  summary_line: SOC 2 Type 2, TRUSTe Verified Privacy Seal, TRUSTe Verified International Privacy Seal
slug: jebbit
tags:
- Company
- Interactive Experiences
- Zero-Party Data
- First-Party Data
- Marketing
- Quizzes
- Product Feeds
- Webhooks
- Customer Data
- JSON:API
website: https://jebbit.com/
---
