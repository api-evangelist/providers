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
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The HTTP API each Norish instance serves under /api/v1, covering a public health check plus authenticated recipe read/search/create/import, grocery list management, stores, and planned recipes for tod
  name: Norish Recipe API
  slug: norish-recipe-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/norish-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://norish.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.norish.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.norish.dev/quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/norish-recipes
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/norish-recipes/norish
- group: operate
  title: ''
  type: Support
  url: https://github.com/norish-recipes/norish/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/norish-recipes/norish/blob/main/LICENSE
- group: build
  title: ''
  type: Packages
  url: packages/norish-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/norish-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/norish-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/norish-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/norish-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/norish-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/norish-mcp.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.norish.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.norish.dev/reference/api
- group: auth
  title: ''
  type: Authentication
  url: authentication/norish-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/norish-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/norish-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/norish-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/norish-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-27'
description: Norish is an open-source, self-hosted recipe and meal-planning application built for households — import a recipe from a URL, video or photo, plan the week on a shared calendar, and keep a grocery list that every member of the household sees update in real time. It is distributed as a Docker image (norishapp/norish) under AGPL-3.0 and runs entirely on the operator's own hardware, with PostgreSQL, Redis and a Python parser service behind it. Each instance exposes an HTTP API under /api/v1 — recipes, recipe imports, groceries, stores and planned recipes — secured with an instance-issued API key, plus a generated OpenAPI document and a Scalar API reference that are served from the running instance to signed-in users.
image: https://raw.githubusercontent.com/norish-recipes/norish/main/.github/assets/logo.svg
layout: provider
modified: '2026-08-27'
name: Norish
nav: Providers
network: true
overview: 'Norish publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recipes, Meal Planning, Groceries, and Food.


  Norish''s developer surface includes documentation, getting-started guide, support, changelog, API reference, authentication, and 17 more developer resources.'
plans:
- name: Norish Plans Pricing
  plan_count: 0
  slug: norish-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Norish Rate Limits
  slug: norish-rate-limits
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 24.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/norish/refs/heads/main/screenshots/norish-2026-09-02T150800.png
security:
- kind: authentication
  name: Norish Authentication
  slug: norish-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Norish Domain Security
  slug: norish-domain-security
  summary_line: TLSv1.3
slug: norish
tags:
- Company
- Recipes
- Meal Planning
- Groceries
- Food
- Self-Hosted
- Open-Source
- Household
- Calendar
- CalDAV
website: https://norish.dev
---
