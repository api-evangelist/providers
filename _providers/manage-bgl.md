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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Manage Bgl Agentic Access
  operation_count: 20
  slug: manage-bgl-agentic-access
  summary_line: 20 operations · 13 acting
api_count: 5
apis:
- description: Account creation, login, token, and session operations
  name: Manage BGL Authentication API
  slug: manage-bgl-authentication-api
- description: Creating, updating, deleting, and extracting diabetes log data
  name: Manage BGL Logs API
  slug: manage-bgl-logs-api
- description: Subscriber-only BGL prediction and dose features
  name: Manage BGL Predictions API
  slug: manage-bgl-predictions-api
- description: User ratios and configuration
  name: Manage BGL Settings API
  slug: manage-bgl-settings-api
- description: Health checks and operational status
  name: Manage BGL System API
  slug: manage-bgl-system-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/manage-bgl-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://jadediabetes.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://jadediabetes.com/api/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://jadediabetes.com/api/api-rest/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://jadediabetes.com/api/api-rest/index.html
- group: start
  title: ''
  type: Sandbox
  url: https://app.jadediabetes.com/api/sample.html
- group: commercial
  title: ''
  type: Pricing
  url: https://jadediabetes.com/subscribe/index.html
- group: start
  title: ''
  type: SignUp
  url: https://jadediabetes.com/subscribe/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jadediabetes.com/policy-privacy/index.html
- group: operate
  title: ''
  type: Support
  url: https://jadediabetes.com/contact/index.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://jadediabetes.com/faq/index.html
- group: auth
  title: ''
  type: Compliance
  url: https://jadediabetes.com/policy-hipaa-phi/index.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/manage-bgl-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/manage-bgl-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/manage-bgl-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/manage-bgl-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/manage-bgl-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/manage-bgl-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/manage-bgl-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/manage-bgl-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manage-bgl-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/manage-bgl-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/manage-bgl-overlay.yaml
created: '2026-07-17'
description: Manage BGL is the diabetes-management platform from Jade Diabetes, a Melbourne, Australia company whose iOS and Android app helps people with Type 1, Type 1.5, Type 2, gestational, and LADA diabetes track blood glucose levels and calculate insulin doses. Jade tracks 64 types of diabetes data, calculates doses from carbohydrates, protein, fat, fiber, insulin-on-board and personalized factors, and offers a prediction engine that forecasts blood sugar hours ahead. It integrates with Dexcom, FreeStyle Libre, NightScout, fitness and food apps, and more than 60 diabetic devices, and supports live data sharing with care teams for remote patient monitoring. Jade exposes a public REST API (v1.0) so developers and partners can read and write diabetes data securely.
image: https://jadediabetes.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: manage-bgl-mcp.yml
  slug: manage-bgl-mcpyml
modified: '2026-07-20'
name: Manage BGL
nav: Providers
network: true
overview: 'Manage BGL publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Logs API, Predictions API, and 2 more. Tagged areas include Company, Diabetes, Health, Healthcare, and Digital Health.


  Manage BGL''s developer surface includes API reference, documentation, sandbox, pricing, signup flow, support, authentication, and 17 more developer resources.'
random_paper: 43
score:
  band: thin
  composite: 41.1
  delta: -1.4
  facets:
    commercial_clarity: 42.1
    contract_quality: 54.8
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/manage-bgl/refs/heads/main/screenshots/manage-bgl-2026-07-25T230015.png
security:
- kind: authentication
  name: Manage Bgl Authentication
  slug: manage-bgl-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Manage Bgl Domain Security
  slug: manage-bgl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: manage-bgl
tags:
- Company
- Diabetes
- Health
- Healthcare
- Digital Health
- Insulin
- Blood Glucose
- Remote Patient Monitoring
- Telemedicine
- REST API
website: https://jadediabetes.com
---
