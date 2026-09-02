---
access_model:
  confidence: high
  label: Free / Open Source
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://wger.readthedocs.io/en/latest/api/api.html
  - https://wger.de/api/v2/schema
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The check-language API from Wger — 1 operation(s) for check-language.
  name: Wger Check Language API
  slug: wger-check-language-api
- description: The check-permission API from Wger — 1 operation(s) for check-permission.
  name: Wger Check Permission API
  slug: wger-check-permission-api
- description: The day API from Wger — 2 operation(s) for day.
  name: Wger Day API
  slug: wger-day-api
- description: The deletion-log API from Wger — 2 operation(s) for deletion-log.
  name: Wger Deletion Log API
  slug: wger-deletion-log-api
- description: The equipment API from Wger — 2 operation(s) for equipment.
  name: Wger Equipment API
  slug: wger-equipment-api
- description: The exercise database. Related objects are referenced by ID. This is the writable endpoint of the two exercise representations.
  name: Wger Exercise API
  slug: wger-exercise-api
- description: The exercise-submission API from Wger — 1 operation(s) for exercise-submission.
  name: Wger Exercise Submission API
  slug: wger-exercise-submission-api
- description: The exercise-translation API from Wger — 2 operation(s) for exercise-translation.
  name: Wger Exercise Translation API
  slug: wger-exercise-translation-api
- description: The exercisealias API from Wger — 2 operation(s) for exercisealias.
  name: Wger Exercisealias API
  slug: wger-exercisealias-api
- description: The exercisecategory API from Wger — 2 operation(s) for exercisecategory.
  name: Wger Exercisecategory API
  slug: wger-exercisecategory-api
- description: The exercisecomment API from Wger — 2 operation(s) for exercisecomment.
  name: Wger Exercisecomment API
  slug: wger-exercisecomment-api
- description: The exerciseimage API from Wger — 3 operation(s) for exerciseimage.
  name: Wger Exerciseimage API
  slug: wger-exerciseimage-api
- description: 'The same exercises read-only, with categories, muscles, equipment, images, videos and translations expanded inline. Meant for external tools and integrations: one request returns everything, with no I'
  name: Wger Exerciseinfo API
  slug: wger-exerciseinfo-api
- description: The gallery API from Wger — 2 operation(s) for gallery.
  name: Wger Gallery API
  slug: wger-gallery-api
- description: Nutritional information per ingredient, referencing related objects by ID. Read-only and rate limited.
  name: Wger Ingredient API
  slug: wger-ingredient-api
- description: The ingredient-image API from Wger — 2 operation(s) for ingredient-image.
  name: Wger Ingredient Image API
  slug: wger-ingredient-image-api
- description: The same data as ingredientinfo, but cursor paginated for mirroring the whole catalogue. No `count`, and only `next`/`previous` rather than arbitrary offsets. Combine with the `last_update__gt` filter
  name: Wger Ingredient Sync API
  slug: wger-ingredient-sync-api
- description: 'The same ingredients read-only, with language, license, image and weight units expanded inline. Meant for external tools and integrations: one request returns everything, with no IDs left to resolve.'
  name: Wger Ingredientinfo API
  slug: wger-ingredientinfo-api
- description: The ingredientweightunit API from Wger — 2 operation(s) for ingredientweightunit.
  name: Wger Ingredientweightunit API
  slug: wger-ingredientweightunit-api
- description: The issue-refresh-token API from Wger — 1 operation(s) for issue-refresh-token.
  name: Wger Issue Refresh Token API
  slug: wger-issue-refresh-token-api
- description: The language API from Wger — 2 operation(s) for language.
  name: Wger Language API
  slug: wger-language-api
- description: The license API from Wger — 2 operation(s) for license.
  name: Wger License API
  slug: wger-license-api
- description: Upper limit for the repetitions of a set, per iteration.
  name: Wger Max Repetitions Config API
  slug: wger-max-repetitions-config-api
- description: Upper limit for the rest between sets, per iteration.
  name: Wger Max Rest Config API
  slug: wger-max-rest-config-api
- description: Upper limit for the reps in reserve of a set, per iteration.
  name: Wger Max Rir Config API
  slug: wger-max-rir-config-api
- description: Upper limit for the number of sets, per iteration.
  name: Wger Max Sets Config API
  slug: wger-max-sets-config-api
- description: Upper limit for the weight of a set, per iteration.
  name: Wger Max Weight Config API
  slug: wger-max-weight-config-api
- description: The meal API from Wger — 3 operation(s) for meal.
  name: Wger Meal API
  slug: wger-meal-api
- description: The mealitem API from Wger — 3 operation(s) for mealitem.
  name: Wger Mealitem API
  slug: wger-mealitem-api
- description: The measurement API from Wger — 2 operation(s) for measurement.
  name: Wger Measurement API
  slug: wger-measurement-api
- description: The measurement-category API from Wger — 2 operation(s) for measurement-category.
  name: Wger Measurement Category API
  slug: wger-measurement-category-api
- description: The min-app-version API from Wger — 1 operation(s) for min-app-version.
  name: Wger Min App Version API
  slug: wger-min-app-version-api
- description: The min-server-version API from Wger — 1 operation(s) for min-server-version.
  name: Wger Min Server Version API
  slug: wger-min-server-version-api
- description: The muscle API from Wger — 2 operation(s) for muscle.
  name: Wger Muscle API
  slug: wger-muscle-api
- description: The nutritiondiary API from Wger — 3 operation(s) for nutritiondiary.
  name: Wger Nutritiondiary API
  slug: wger-nutritiondiary-api
- description: Nutrition plans, referencing meals and items by ID.
  name: Wger Nutritionplan API
  slug: wger-nutritionplan-api
- description: The same plans read-only, with meals, items and their nutritional values expanded inline. Meant for external tools and integrations that want a whole plan in one request, with no IDs left to resolve.
  name: Wger Nutritionplaninfo API
  slug: wger-nutritionplaninfo-api
- description: The powersync-keys API from Wger — 1 operation(s) for powersync-keys.
  name: Wger Powersync Keys API
  slug: wger-powersync-keys-api
- description: The powersync-token API from Wger — 1 operation(s) for powersync-token.
  name: Wger Powersync Token API
  slug: wger-powersync-token-api
- description: Read-only view of the routine templates published by other users.
  name: Wger Public Templates API
  slug: wger-public-templates-api
- description: Repetitions for a set, per iteration.
  name: Wger Repetitions Config API
  slug: wger-repetitions-config-api
- description: Rest between sets, per iteration.
  name: Wger Rest Config API
  slug: wger-rest-config-api
- description: Reps in reserve for a set, per iteration.
  name: Wger Rir Config API
  slug: wger-rir-config-api
- description: Workout routines. The nested day, slot and config structure is available in one request under `/routine/{id}/structure/`.
  name: Wger Routine API
  slug: wger-routine-api
- description: The schema API from Wger — 1 operation(s) for schema.
  name: Wger Schema API
  slug: wger-schema-api
- description: Number of sets, per iteration.
  name: Wger Sets Config API
  slug: wger-sets-config-api
- description: The setting-repetitionunit API from Wger — 2 operation(s) for setting-repetitionunit.
  name: Wger Setting Repetitionunit API
  slug: wger-setting-repetitionunit-api
- description: The setting-weightunit API from Wger — 2 operation(s) for setting-weightunit.
  name: Wger Setting Weightunit API
  slug: wger-setting-weightunit-api
- description: The slot API from Wger — 2 operation(s) for slot.
  name: Wger Slot API
  slug: wger-slot-api
- description: The slot-entry API from Wger — 2 operation(s) for slot-entry.
  name: Wger Slot Entry API
  slug: wger-slot-entry-api
- description: Read-only view of the routines the user marked as a template, plus their trainer's, if they have one.
  name: Wger Templates API
  slug: wger-templates-api
- description: The token API from Wger — 2 operation(s) for token.
  name: Wger Token API
  slug: wger-token-api
- description: The trophy API from Wger — 3 operation(s) for trophy.
  name: Wger Trophy API
  slug: wger-trophy-api
- description: The upload-powersync-data API from Wger — 1 operation(s) for upload-powersync-data.
  name: Wger Upload Powersync Data API
  slug: wger-upload-powersync-data-api
- description: The user-statistics API from Wger — 2 operation(s) for user-statistics.
  name: Wger User Statistics API
  slug: wger-user-statistics-api
- description: The user-trophy API from Wger — 2 operation(s) for user-trophy.
  name: Wger User Trophy API
  slug: wger-user-trophy-api
- description: The userprofile API from Wger — 2 operation(s) for userprofile.
  name: Wger Userprofile API
  slug: wger-userprofile-api
- description: The version API from Wger — 1 operation(s) for version.
  name: Wger Version API
  slug: wger-version-api
- description: The video API from Wger — 2 operation(s) for video.
  name: Wger Video API
  slug: wger-video-api
- description: Weight for a set, per iteration.
  name: Wger Weight Config API
  slug: wger-weight-config-api
- description: The weightentry API from Wger — 2 operation(s) for weightentry.
  name: Wger Weightentry API
  slug: wger-weightentry-api
- description: The workoutlog API from Wger — 2 operation(s) for workoutlog.
  name: Wger Workoutlog API
  slug: wger-workoutlog-api
- description: The workoutsession API from Wger — 2 operation(s) for workoutsession.
  name: Wger Workoutsession API
  slug: wger-workoutsession-api
artifact_total: 70
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/wger-project/wger/blob/master/LICENSE
- group: other
  title: ''
  type: Overlay
  url: overlays/wger-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://wger.de
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wger.de/en/software/api
- group: docs
  title: ''
  type: Documentation
  url: https://wger.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://wger.de/api/v2/schema/ui
- group: start
  title: ''
  type: GettingStarted
  url: https://wger.readthedocs.io/en/latest/api/api.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wger-project
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/wger-project/wger
- group: operate
  title: ''
  type: Support
  url: https://github.com/wger-project/wger/discussions
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/rPWFv6W
- group: start
  title: ''
  type: SignUp
  url: https://wger.de/en/user/registration
- group: start
  title: ''
  type: Login
  url: https://wger.de/en/user/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wger.de/en/software/terms-of-service
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wger-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wger-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/wger-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/wger-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wger-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/wger-cli.yml
- group: design
  title: ''
  type: Components
  url: components/wger-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wger-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/wger-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wger-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wger-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wger-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wger-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/wger-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wger-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wger-rate-limits.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: wger (wger Workout Manager) is a self-hosted, free and open source (AGPL-3.0) fitness, workout, nutrition and body-weight tracker written in Django. Its REST API is served under /api/v2/ on any wger instance — including the project's own hosted instance at wger.de — and publishes a complete OpenAPI 3.0.3 schema generated from the code at /api/v2/schema, covering 129 paths and 254 operations across routines, days, slots and per-iteration progression configs, workout logs and sessions, the community exercise database (exercises, translations, images, videos, muscles, equipment, categories), the ingredient and nutrition-plan catalog with an incremental ingredient-sync feed, body weight, body measurements, galleries and gamification trophies. System-wide reference data (exercises, ingredients, units) is readable without authentication; user-owned data takes a personal API token, a JWT issued via allauth-headless, an OAuth2/OIDC access token, or the session cookie. The project also
  ships a first-party Python API client, a first-party MCP server exposing 85 tools over the same API, React components, Flutter and Android apps, and Docker/Helm deployment stacks.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wger.png
layout: provider
mcp_servers:
- description: First-party MCP server, maintained in the wger-project GitHub organization, that exposes the wger (>= 2.6) fitness/nutrition REST API as MCP tools — routines, workout logging, sessions, the exercise a
  name: wger MCP server
  slug: wger-mcp-server
modified: '2026-08-27'
name: Wger
nav: Providers
network: true
overview: 'Wger publishes 63 APIs on the [APIs.io](https://apis.io/) network, including Check Language API, Check Permission API, Day API, and 60 more. Tagged areas include Sports And Fitness, Public APIs, Fitness, Nutrition, and Health.


  Wger''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, changelog, CLI, and 25 more developer resources.'
plans:
- name: Wger Plans Pricing
  plan_count: 0
  slug: wger-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Wger Rate Limits
  slug: wger-rate-limits
scopes:
- name: Wger Scopes
  scope_count: 5
  slug: wger-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 22
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.8
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 47.0
    developer_ergonomics: 68.5
    discoverability: 51.9
    governance: 4.5
    operational_transparency: 68.4
  previous_composite: 47.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 63
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 50.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wger/refs/heads/main/screenshots/wger-2026-06-20T201416.png
security:
- kind: authentication
  name: Wger Authentication
  slug: wger-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Wger Domain Security
  slug: wger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wger Vulnerability Disclosure
  slug: wger-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: wger
tags:
- Sports And Fitness
- Public APIs
- Fitness
- Nutrition
- Health
- Open-Source
- Self-Hosted
- Workout Tracking
- Django
- REST
website: https://wger.de
---
