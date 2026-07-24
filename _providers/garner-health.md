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
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 77.9
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Garner Health Agentic Access
  operation_count: 4
  slug: garner-health-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 4
apis:
- description: The Facilities API from Garner Health — 1 operation(s) for facilities.
  name: Garner Health Facilities API
  slug: garner-health-facilities-api
- description: The Professionals API from Garner Health — 1 operation(s) for professionals.
  name: Garner Health Professionals API
  slug: garner-health-professionals-api
- description: The Provider Annotations API from Garner Health — 1 operation(s) for provider annotations.
  name: Garner Health Provider Annotations API
  slug: garner-health-provider-annotations-api
- description: The Providers API from Garner Health — 1 operation(s) for providers.
  name: Garner Health Providers API
  slug: garner-health-providers-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://garnerhealth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://garnerhealth.redoc.ly
- group: docs
  title: ''
  type: Documentation
  url: https://garnerhealth.redoc.ly
- group: docs
  title: ''
  type: APIReference
  url: https://garnerhealth.redoc.ly
- group: start
  title: ''
  type: GettingStarted
  url: 'https://garnerhealth.redoc.ly/#section/Authentication:'
- group: auth
  title: ''
  type: Authentication
  url: authentication/garner-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/garner-health-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/garner-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/garner-health-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/garner-health-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/garner-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/garner-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://garnerhealth.com/news/garner-completes-soc-2-type-ii-certification
- group: agent
  title: ''
  type: MCPServer
  url: mcp/garner-health-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/garner-health-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/garner-health-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/garner-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/garner-health-llms.txt
- group: docs
  title: ''
  type: OpenAPIOverlay
  url: overlays/garner-health-openapi-overlay.yaml
- group: company
  title: ''
  type: Blog
  url: https://garnerhealth.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://garnerhealth.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://garnerhealth.com/request-demo
- group: start
  title: ''
  type: Login
  url: https://app.getgarner.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://garnerhealth.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://garnerhealth.com/privacy-policy
created: '2026-07-17'
description: Garner Health is a healthcare technology company that helps members find high-quality, in-network doctors and helps employers, benefits advisors, health plans, and providers improve care quality while lowering healthcare costs. Garner analyzes more than 60 billion de-identified medical records from 320M+ patients and scores providers on 550+ specialty-specific quality and efficiency metrics across 80+ specialties to identify Top Providers. Its provider-recommendation API returns rank-ordered providers, professional and facility detail, and a provider-annotation endpoint over the base host api.getgarner.com, authenticated with OAuth 2.0 client credentials. Garner is SOC 2 Type II certified.
image: https://cdn.prod.website-files.com/6994c8f92ae6b0d756f5e541/69b15a86b59f244f1a4d372e_Open%20graph%20img.png
layout: provider
mcp_servers:
- description: ''
  name: garner-health-mcp.yml
  slug: garner-health-mcpyml
modified: '2026-07-19'
name: Garner Health
nav: Providers
network: true
overview: 'Garner Health publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Facilities API, Professionals API, Provider Annotations API, and 1 more. Tagged areas include Company, Healthcare, Health Data, Provider Directory, and Care Navigation.


  Garner Health''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 39
score:
  band: developing
  composite: 50.1
  delta: 2.7
  facets:
    commercial_clarity: 52.6
    contract_quality: 57.1
    developer_ergonomics: 63.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 47.4
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Garner Health Authentication
  slug: garner-health-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Garner Health Domain Security
  slug: garner-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: garner-health
tags:
- Company
- Healthcare
- Health Data
- Provider Directory
- Care Navigation
- Claims Analytics
- Health Plans
- Employee Benefits
website: https://garnerhealth.com
---
