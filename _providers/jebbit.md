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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Jebbit Agentic Access
  operation_count: 37
  slug: jebbit-agentic-access
  summary_line: 37 operations · 19 acting
api_count: 1
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
artifact_total: 31
asyncapis:
- description: ''
  name: Jebbit Webhooks
  slug: jebbit-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jebbit Auth API
  slug: open-jebbit-auth-api
- collection_type: open
  name: Jebbit Auth Businesses API
  slug: open-jebbit-businesses-api
- collection_type: open
  name: Jebbit Auth Campaigns API
  slug: open-jebbit-campaigns-api
- collection_type: open
  name: Jebbit Auth Feed Columns API
  slug: open-jebbit-feed-columns-api
- collection_type: open
  name: Jebbit Auth Feed Rows API
  slug: open-jebbit-feed-rows-api
- collection_type: open
  name: Jebbit Auth Feeds API
  slug: open-jebbit-feeds-api
- collection_type: open
  name: Jebbit Auth Integration Historic Backfills API
  slug: open-jebbit-integration-historic-backfills-api
- collection_type: open
  name: Jebbit Auth Integration Mappings API
  slug: open-jebbit-integration-mappings-api
- collection_type: open
  name: Jebbit Auth Integrations API
  slug: open-jebbit-integrations-api
- collection_type: open
  name: Jebbit Auth Launch Links API
  slug: open-jebbit-launch-links-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/jebbit-openapi-overlay.yaml
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
- group: build
  title: ''
  type: Packages
  url: packages/jebbit-packages.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/jebbit-tool-crosswalk.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jebbit-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jebbit-plans-pricing.yml
created: '2026-07-17'
description: Jebbit — now BlueConic Experiences — is an interactive experience platform that captures zero- and first-party declared data from consumers through quizzes, product finders, personality tests, and preference flows that shoppers complete because the experience gives them value in return. Responses sync into customer profiles and activate across the marketing stack in real time. Jebbit exposes a public JSON:API REST API (https://api2.jebbit.com) for managing businesses, campaigns, launch links, dynamic product feeds, and webhook integrations that stream user session data, secured with OAuth 2.0 client-credentials JWTs and HMAC-signed webhooks.
image: https://jebbit-public-api-docs.s3.amazonaws.com/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Jebbit MCP Server
  slug: jebbit-mcp-server
modified: '2026-08-13'
name: Jebbit
nav: Providers
network: true
overview: 'Jebbit publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Businesses API, Campaigns API, and 7 more. Tagged areas include Company, Interactive Experiences, Zero-Party Data, First-Party Data, and Marketing.


  The Jebbit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Jebbit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 30 more developer resources.'
plans:
- name: Jebbit Plans Pricing
  plan_count: 0
  slug: jebbit-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Jebbit Rate Limits
  slug: jebbit-rate-limits
scopes:
- name: Jebbit Scopes
  scope_count: 6
  slug: jebbit-scopes
  summary_line: 6 scopes
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 24
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 62.5
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 51.0
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Webhook
- Customer Data
- JSON:API
website: https://jebbit.com/
---
