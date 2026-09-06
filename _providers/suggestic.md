---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: GraphQL API for personalized nutrition — users, programs/diets, meal-plan generation, recipe and restaurant search, food logging (incl. AI food log), shopping lists, health trackers, lab tests/biomark
  name: Suggestic GraphQL API
  slug: suggestic-graphql-api
artifact_total: 4
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: Suggestic
nav: Providers
network: true
overview: 'Suggestic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nutrition, Health, Meal Planning, and Recipes.


  The Suggestic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Suggestic''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 23 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 46.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 27.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/suggestic/refs/heads/main/screenshots/suggestic-2026-08-17T082152.png
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
