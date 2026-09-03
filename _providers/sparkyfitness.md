---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: A first-party Model Context Protocol server running in-process inside the SparkyFitness API server, mounted at POST /mcp over a stateless streamable HTTP transport. 56 tools across food, exercise, che
  name: SparkyFitness MCP Server
  slug: sparkyfitness-mcp-server
- baseURL: https://{host}/api
  baseurl_source: declared
  description: The Admin API from SparkyFitness — 3 operation(s) for admin.
  name: SparkyFitness Admin API
  slug: sparkyfitness-admin-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: The AI API from SparkyFitness — 1 operation(s) for ai.
  name: SparkyFitness AI API
  slug: sparkyfitness-ai-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: AI-powered chat assistance, reports, trends, and analytical insights.
  name: SparkyFitness AI & Insights API
  slug: sparkyfitness-ai-insights-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: The Allergen Preferences API from SparkyFitness — 2 operation(s) for allergen preferences.
  name: SparkyFitness Allergen Preferences API
  slug: sparkyfitness-allergen-preferences-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: The Authentication API from SparkyFitness — 4 operation(s) for authentication.
  name: SparkyFitness Authentication API
  slug: sparkyfitness-authentication-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: The Dashboard API from SparkyFitness — 3 operation(s) for dashboard.
  name: SparkyFitness Dashboard API
  slug: sparkyfitness-dashboard-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: The Dashboard Layouts API from SparkyFitness — 1 operation(s) for dashboard layouts.
  name: SparkyFitness Dashboard Layouts API
  slug: sparkyfitness-dashboard-layouts-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: The Exercise Entries API from SparkyFitness — 1 operation(s) for exercise entries.
  name: SparkyFitness Exercise Entries API
  slug: sparkyfitness-exercise-entries-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: The Exercise Stats API from SparkyFitness — 4 operation(s) for exercise stats.
  name: SparkyFitness Exercise Stats API
  slug: sparkyfitness-exercise-stats-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: The Exercise & Workouts API from SparkyFitness — 23 operation(s) for exercise & workouts.
  name: SparkyFitness Exercise & Workouts API
  slug: sparkyfitness-exercise-workouts-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: Third-party service connections (Garmin, Withings, OIDC, etc.).
  name: SparkyFitness External Integrations API
  slug: sparkyfitness-external-integrations-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: Exercise database, workout presets, plan templates, and activity logging.
  name: SparkyFitness Fitness & Workouts API
  slug: sparkyfitness-fitness-workouts-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: Personal goal setting, goal presets, and application preferences.
  name: SparkyFitness Goals & Personalization API
  slug: sparkyfitness-goals-personalization-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: User authentication, registration, profile management, MFA, and access control.
  name: SparkyFitness Identity & Security API
  slug: sparkyfitness-identity-security-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: Medication cabinet, schedules, GLP-1 injections, pen/vial inventory, titration, and modeled PK/site-rotation.
  name: SparkyFitness Medications & GLP-1 API
  slug: sparkyfitness-medications-glp-1-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: Food database, diary logging, meal planning, and nutritional preferences.
  name: SparkyFitness Nutrition & Meals API
  slug: sparkyfitness-nutrition-meals-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: The SleepScience API from SparkyFitness — 7 operation(s) for sleepscience.
  name: SparkyFitness Sleep Science API
  slug: sparkyfitness-sleepscience-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: The Synced Data API from SparkyFitness — 2 operation(s) for synced data.
  name: SparkyFitness Synced Data API
  slug: sparkyfitness-synced-data-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: System configuration, administrative tasks, backups, reviews, and versioning.
  name: SparkyFitness System & Admin API
  slug: sparkyfitness-system-admin-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: The Utility API from SparkyFitness — 1 operation(s) for utility.
  name: SparkyFitness Utility API
  slug: sparkyfitness-utility-api
- baseURL: https://{host}/api
  baseurl_source: declared
  description: Health metrics tracking (weight, measurements, sleep, mood) and fasting.
  name: SparkyFitness Wellness & Metrics API
  slug: sparkyfitness-wellness-metrics-api
artifact_total: 28
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sparkyfitness-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sparkyfitness-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://codewithcj.github.io/SparkyFitness/
- group: docs
  title: ''
  type: Documentation
  url: https://codewithcj.github.io/SparkyFitness/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://codewithcj.github.io/SparkyFitness/developer/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://codewithcj.github.io/SparkyFitness/developer/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://codewithcj.github.io/SparkyFitness/install/docker-compose
- group: operate
  title: ''
  type: Support
  url: https://codewithcj.github.io/SparkyFitness/help-me
- group: operate
  title: ''
  type: HelpCenter
  url: https://discord.gg/vcnMT5cPEA
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CodeWithCJ
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/CodeWithCJ/SparkyFitness
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codewithcj.github.io/SparkyFitness/privacy_policy
- group: commercial
  title: ''
  type: License
  url: https://github.com/CodeWithCJ/SparkyFitness/blob/main/LICENSE
- group: operate
  title: ''
  type: FAQ
  url: https://codewithcj.github.io/SparkyFitness/faq
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/CodeWithCJ/SparkyFitness/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sparkyfitness-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/sparkyfitness-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sparkyfitness-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sparkyfitness-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sparkyfitness-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sparkyfitness-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sparkyfitness-domain-security.yml
created: '2026-08-27'
description: 'SparkyFitness is a self-hosted, open-source health and fitness tracker for food, exercise, water, sleep, mood, body measurements and medications, built for families and designed around an AI assistant. It ships a full Express 5 + PostgreSQL REST API (423 operations across 328 paths, described by an OpenAPI 3.0 document the server generates and serves at /api/api-docs/json) and — unusually for a project this size — a first-party Model Context Protocol server running in-process at POST /mcp, exposing 56 tools for logging and reading a user''s own health data under PostgreSQL row-level security. It synchronises with Garmin, Fitbit, Withings, Strava, Polar, Oura, Hevy, Apple HealthKit and Google Health Connect, and looks food up against OpenFoodFacts, USDA, FatSecret and Nutritionix. Because it is self-hosted, there is no vendor API host, no pricing and no signup: you run the containers and the API is yours. Distributed under a source-available non-commercial licence.'
image: https://codewithcj.github.io/SparkyFitness/logo.png
layout: provider
mcp_servers:
- description: ''
  name: SparkyFitness MCP Server
  slug: sparkyfitness-mcp-server
modified: '2026-08-27'
name: SparkyFitness
nav: Providers
network: true
overview: 'SparkyFitness publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Admin API, AI API, AI & Insights API, and 18 more. Tagged areas include Company, Health, Fitness, Nutrition, and Self-Hosted.


  SparkyFitness'' developer surface includes documentation, API reference, getting-started guide, support, FAQ, changelog, and 17 more developer resources.'
plans:
- name: Sparkyfitness Plans Pricing
  plan_count: 0
  slug: sparkyfitness-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Sparkyfitness Rate Limits
  slug: sparkyfitness-rate-limits
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 14.4
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 31.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 21
      marker_coverage: 100.0
      total: 21
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sparkyfitness/refs/heads/main/screenshots/sparkyfitness-2026-09-02T160339.png
security:
- kind: authentication
  name: Sparkyfitness Authentication
  slug: sparkyfitness-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sparkyfitness Domain Security
  slug: sparkyfitness-domain-security
  summary_line: HSTS
- kind: vulnerability-disclosure
  name: Sparkyfitness Vulnerability Disclosure
  slug: sparkyfitness-vulnerability-disclosure
  summary_line: Hackerone
slug: sparkyfitness
tags:
- Company
- Health
- Fitness
- Nutrition
- Self-Hosted
- Open-Source
- Wearables
- MCP
- AI Assistant
- Quantified Self
website: https://codewithcj.github.io/SparkyFitness/
---
