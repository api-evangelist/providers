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
api_count: 1
apis:
- description: GraphQL API for personalized nutrition — users, programs/diets, meal-plan generation, recipe and restaurant search, food logging (incl. AI food log), shopping lists, health trackers, lab tests/biomark
  name: Suggestic GraphQL API
  slug: suggestic-graphql-api
artifact_total: 5
asyncapis:
- description: ''
  name: Suggestic Webhooks
  slug: suggestic-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/suggestic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://suggestic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.suggestic.com/graphql/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.suggestic.com/graphql/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.suggestic.com/graphql/graphql/graphql-playground
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.suggestic.com/graphql/start-here/getting-started
- group: company
  title: ''
  type: Blog
  url: https://blog.suggestic.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://pricing.suggestic.com/
- group: start
  title: ''
  type: SignUp
  url: https://suggestic.com/
- group: start
  title: ''
  type: Login
  url: https://console.suggestic.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Suggestic
- group: operate
  title: ''
  type: StatusPage
  url: https://status.suggestic.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.suggestic.com/graphql/changelog/2025
- group: auth
  title: ''
  type: Authentication
  url: authentication/suggestic-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/suggestic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/suggestic-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/suggestic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/suggestic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/suggestic-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.suggestic.com/graphql/helpful-resources/deprecated-features
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/suggestic-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/suggestic-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://suggestic.com/
- group: design
  title: ''
  type: Components
  url: components/suggestic-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/suggestic-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/suggestic-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/suggestic-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/suggestic-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/suggestic-llms.txt
created: '2026-07-17'
description: Suggestic is a personalized-nutrition and health platform that exposes a GraphQL API for building meal-planning, food-logging, and coaching applications. Developers use the API to create users, assign nutrition programs and diets, generate personalized meal plans, search a large recipe and restaurant database, log food (including AI photo-based logging), build shopping lists, and track sleep, steps, water, weight, heart rate, symptoms, biomarkers, and supplements. The platform also powers an AI Assistant with journeys and guardrails, a Console for configuration and webhooks, and a Telehealth/Coaching Portal. Suggestic (a Techstars-backed company) markets an enterprise AI offering for regulated health verticals and is HIPAA and SOC 2 Type II certified. Authentication is via a server-side API token plus an sg-user header, or client-side JWT bearer tokens.
image: https://suggestic.com/assets/images/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: suggestic-mcp.yml
  slug: suggestic-mcpyml
modified: '2026-07-21'
name: Suggestic
nav: Providers
network: true
overview: 'Suggestic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nutrition, Health, Meal Planning, and Recipes.


  The Suggestic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Suggestic''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 23 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 45.0
  delta: 1.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 51.6
    developer_ergonomics: 64.7
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 52.6
  previous_composite: 44.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 27.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Suggestic Authentication
  slug: suggestic-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Suggestic Domain Security
  slug: suggestic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: suggestic
tags:
- Company
- Nutrition
- Health
- Meal Planning
- Recipes
- Food
- GraphQL
- Personalization
- Wellness
- Telehealth
- Artificial Intelligence
website: https://suggestic.com/
---
