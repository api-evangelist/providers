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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 60.6
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: Submit customers, designs and pricing into Palmetto's transparent, auditable clean-energy fulfillment pipeline.
  name: Palmetto Energy Platform API
  slug: palmetto-energy-platform-api
- description: Finance solar, storage and other clean-energy projects; includes contracts, documents, organizations, users and a webhook event surface.
  name: Palmetto Finance (LightReach) API
  slug: palmetto-finance-lightreach-api
- description: The Bem API from Palmetto — 1 operation(s) for bem.
  name: Palmetto Bem API
  slug: palmetto-bem-api
- description: The Health API from Palmetto — 1 operation(s) for health.
  name: Palmetto Health API
  slug: palmetto-health-api
artifact_total: 8
asyncapis:
- description: ''
  name: Palmetto Finance Webhooks
  slug: palmetto-finance-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://palmetto.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.palmetto.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.palmetto.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.palmetto.com/energy/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://help.palmetto.com
- group: company
  title: ''
  type: Blog
  url: https://palmetto.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/palmetto
- group: operate
  title: ''
  type: StatusPage
  url: https://status.palmetto.com
- group: commercial
  title: ''
  type: Pricing
  url: https://palmetto.com/business/energy-intelligence-api
- group: start
  title: ''
  type: SignUp
  url: https://ei.docs.palmetto.com/docs/getting-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://palmetto.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://palmetto.com/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/palmetto-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/palmetto-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/palmetto-packages.yml
- group: design
  title: ''
  type: Components
  url: components/palmetto-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/palmetto-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/palmetto-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/palmetto-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/palmetto-energy-intelligence-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/palmetto-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/palmetto-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/palmetto-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/palmetto-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/palmetto-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/palmetto-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/palmetto-finance-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/palmetto-model-home-energy.md
created: '2026-07-17'
description: 'Palmetto is a clean-energy technology company that helps homeowners and partners adopt solar, HVAC, battery storage, water heaters and financing. For developers and technology partners it publishes three API products under docs.palmetto.com: the Energy Intelligence API (physics-based building energy modeling and solar simulation for any US home, down to hourly granularity and disaggregated to end use), the Energy Platform API (submit customers, designs and pricing into Palmetto''s fulfillment pipeline), and the Finance (LightReach) API for financing clean-energy projects, complete with webhooks. Backed by Social Capital.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/palmetto.png
layout: provider
mcp_servers:
- description: ''
  name: palmetto-mcp.yml
  slug: palmetto-mcpyml
modified: '2026-07-20'
name: Palmetto
nav: Providers
network: true
overview: 'Palmetto publishes 2 APIs on the [APIs.io](https://apis.io/) network: Bem API and Health API. Tagged areas include Company, Clean Energy, Solar, Energy, and Building Energy Modeling.


  The Palmetto catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Palmetto''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, authentication, and 21 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 52.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 64.2
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 52.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Palmetto Authentication
  slug: palmetto-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Palmetto Domain Security
  slug: palmetto-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: palmetto
tags:
- Company
- Clean Energy
- Solar
- Energy
- Building Energy Modeling
- Home Energy
- Financing
- Sustainability
website: https://palmetto.com
---
