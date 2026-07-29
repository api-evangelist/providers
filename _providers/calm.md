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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Calm Agentic Access
  operation_count: 3
  slug: calm-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 2
apis:
- description: Obtain a JWT access token via OAuth 2.0 client credentials.
  name: Calm Authentication API
  slug: calm-authentication-api
- description: Link and cancel partner-user Calm subscriptions.
  name: Calm Subscriptions API
  slug: calm-subscriptions-api
artifact_total: 7
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partner.calm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://partner.calm.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://partner.calm.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://partner.calm.com/docs/api
- group: operate
  title: ''
  type: Support
  url: https://support.calm.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.calm.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.calm.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://business.calm.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/calm-partner-api-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/calm-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/calm-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/calm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calm-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/calm-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/calm-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/calm-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/calm-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/calm-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/calm-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/calm-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/calm-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/calm-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Calm is a leading consumer mental-wellness company whose app offers guided meditations, Sleep Stories, breathing programs, mindfulness masterclasses, and soundscapes. Beyond the direct-to-consumer app, Calm sells two B2B products: Calm Business, which delivers the Calm experience to employers as an employee wellness benefit, and Calm Health, a clinical mental-health offering for health plans and large self-insured employers. Both are powered by the Calm Partner API, an OAuth 2.0 client-credentials REST surface that partner HR and benefits systems use to provision, link, and cancel Calm subscriptions for their members, alongside SAML 2.0 IdP-initiated SSO and SFTP eligibility-file uploads. Calm is a portfolio company of Lightspeed Venture Partners.'
image: https://www.calm.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: calm-mcp.yml
  slug: calm-mcpyml
modified: '2026-07-18'
name: Calm
nav: Providers
network: true
overview: 'Calm publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Subscriptions API. Tagged areas include Company, Mental Health, Wellness, Meditation, and Mindfulness.


  Calm''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, sandbox, and 16 more developer resources.'
random_paper: 13
scopes:
- name: Calm Scopes
  scope_count: 2
  slug: calm-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 41.5
  delta: -6.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 47.9
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/calm/refs/heads/main/screenshots/calm-2026-07-25T204251.png
security:
- kind: authentication
  name: Calm Authentication
  slug: calm-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Calm Domain Security
  slug: calm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: calm
tags:
- Company
- Mental Health
- Wellness
- Meditation
- Mindfulness
- Sleep
- Employee Benefits
- Health
- B2B
- Subscriptions
website: https://partner.calm.com/
---
