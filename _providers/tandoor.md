---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The api API from Tandoor Recipes — 243 operation(s) for api.
  name: Tandoor Recipes API
  slug: tandoor-api-api
- description: The api-token-auth API from Tandoor Recipes — 1 operation(s) for api-token-auth.
  name: Tandoor Recipes API Token Auth API
  slug: tandoor-api-token-auth-api
artifact_total: 7
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/tandoor-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tandoor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tandoor.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tandoor.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tandoor.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tandoor.dev/install/docker/
- group: operate
  title: ''
  type: Support
  url: https://tandoor.dev/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.tandoor.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TandoorRecipes
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TandoorRecipes/recipes
- group: commercial
  title: ''
  type: Pricing
  url: https://tandoor.dev/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.tandoor.dev/accounts/signup/
- group: start
  title: ''
  type: Login
  url: https://app.tandoor.dev/accounts/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tandoor.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tandoor.dev/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tandoor.dev/status/tandoor
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/TandoorRecipes/recipes/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tandoor-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/TandoorRecipes/recipes/security/policy
- group: commercial
  title: ''
  type: Plans
  url: plans/tandoor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tandoor-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/tandoor-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tandoor-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tandoor-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tandoor-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/tandoor-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tandoor-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tandoor-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tandoor-vulnerability-disclosure.yml
created: '2026-08-27'
description: Tandoor Recipes is an open-source, self-hostable recipe management, meal planning and shopping-list application built on Django and django-rest-framework, developed in Falkensee, Germany and offered both as freely self-hosted software (Docker, Kubernetes, Unraid, Synology, TrueNAS) and as a paid hosted service at app.tandoor.dev. Every feature of the product is driven by one REST API — recipes, steps, ingredients, foods, units, unit conversions, properties and nutrition, keywords, meal plans, meal types, shopping lists and shopping-list entries, supermarkets and supermarket category ordering, pantry inventory, recipe books, cook/view logs, spaces and households, user preferences, invite and share links, storage backends and external recipe sync, import/export of a dozen recipe formats, URL/image/PDF recipe scraping, an AI import and property-extraction pipeline routed through LiteLLM, and the Open Data food/unit/store reference database. The API is described by a live drf-spectacular
  OpenAPI 3.0.3 document served without authentication at /openapi/ on every instance, covering 244 paths and 462 operations across 244 component schemas, and it is the same contract the official Vue 3 frontend is generated against.
image: https://raw.githubusercontent.com/TandoorRecipes/recipes/develop/docs/logo_color.svg
layout: provider
modified: '2026-08-27'
name: Tandoor Recipes
nav: Providers
network: true
overview: 'Tandoor Recipes publishes 2 APIs on the [APIs.io](https://apis.io/) network, including API Token Auth API, and 1 more. Tagged areas include Recipes, Meal Planning, Food, Nutrition, and Shopping Lists.


  Tandoor Recipes'' developer surface includes documentation, getting-started guide, support, pricing, signup flow, changelog, authentication, and 23 more developer resources.'
plans:
- name: Tandoor Plans Pricing
  plan_count: 5
  slug: tandoor-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Tandoor Rate Limits
  slug: tandoor-rate-limits
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 37.8
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 58.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tandoor Authentication
  slug: tandoor-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Tandoor Domain Security
  slug: tandoor-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Tandoor Vulnerability Disclosure
  slug: tandoor-vulnerability-disclosure
  summary_line: disclosure policy published
slug: tandoor
tags:
- Recipes
- Meal Planning
- Food
- Nutrition
- Shopping Lists
- Open-Source
- Self-Hosted
- Home Automation
- Django
- Open Data
website: https://tandoor.dev
---
