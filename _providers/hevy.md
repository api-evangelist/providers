---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.hevyapp.com
  baseurl_source: declared
  description: The ExerciseHistory API from Hevy — 1 operation(s) for exercisehistory.
  name: Hevy Exercise History API
  slug: hevy-exercisehistory-api
- baseURL: https://api.hevyapp.com
  baseurl_source: declared
  description: The ExerciseTemplates API from Hevy — 2 operation(s) for exercisetemplates.
  name: Hevy Exercise Templates API
  slug: hevy-exercisetemplates-api
- baseURL: https://api.hevyapp.com
  baseurl_source: declared
  description: The Measurements API from Hevy — 2 operation(s) for measurements.
  name: Hevy Measurements API
  slug: hevy-measurements-api
- baseURL: https://api.hevyapp.com
  baseurl_source: declared
  description: The RoutineFolders API from Hevy — 3 operation(s) for routinefolders.
  name: Hevy Routine Folders API
  slug: hevy-routinefolders-api
- baseURL: https://api.hevyapp.com
  baseurl_source: declared
  description: The Routines API from Hevy — 3 operation(s) for routines.
  name: Hevy Routines API
  slug: hevy-routines-api
- baseURL: https://api.hevyapp.com
  baseurl_source: declared
  description: The Users API from Hevy — 1 operation(s) for users.
  name: Hevy Users API
  slug: hevy-users-api
- baseURL: https://api.hevyapp.com
  baseurl_source: declared
  description: The Workouts API from Hevy — 5 operation(s) for workouts.
  name: Hevy Workouts API
  slug: hevy-workouts-api
artifact_total: 17
common:
- group: other
  href: https://artifacts.apis.io/hevy/overlays/hevy-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hevy-public-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.hevyapp.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.hevyapp.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.hevyapp.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.hevyapp.com/docs
- group: operate
  title: ''
  type: Support
  url: https://www.hevyapp.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.hevyapp.com/help/
- group: company
  title: ''
  type: Blog
  url: https://www.hevyapp.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hevyapp
- group: commercial
  title: ''
  type: Pricing
  url: https://hevy.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://hevy.com/signup
- group: start
  title: ''
  type: Login
  url: https://hevy.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hevyapp.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hevyapp.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.hevyapp.com/status/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.hevyapp.com/community-updates/
- group: operate
  href: https://artifacts.apis.io/hevy/changelog/hevy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hevy-changelog.yml
- group: design
  href: https://artifacts.apis.io/hevy/lifecycle/hevy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hevy-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/hevy/authentication/hevy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hevy-authentication.yml
- group: design
  href: https://artifacts.apis.io/hevy/conventions/hevy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hevy-conventions.yml
- group: design
  href: https://artifacts.apis.io/hevy/errors/hevy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hevy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hevy/data-model/hevy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hevy-data-model.yml
- group: design
  href: https://artifacts.apis.io/hevy/conformance/hevy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hevy-conformance.yml
- group: auth
  href: https://artifacts.apis.io/hevy/security/hevy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hevy-domain-security.yml
- group: build
  href: https://artifacts.apis.io/hevy/packages/hevy-packages.yml
  title: ''
  type: Packages
  url: packages/hevy-packages.yml
- group: operate
  href: https://artifacts.apis.io/hevy/rate-limits/hevy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hevy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/hevy/plans/hevy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hevy-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/hevy/llms/hevy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hevy-llms.txt
- group: agent
  href: https://artifacts.apis.io/hevy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-27'
description: Hevy is a gym workout tracker and planner app for iOS, Android and the web, operated by Hevy Studios, S.L. and used by a community the company describes as 15+ million lifters. Members log strength-training sessions, build and reuse routines, organize them into folders, browse a large exercise library, and track body measurements and progress over time. Hevy also runs Hevy Coach, a separate product for personal trainers who program and monitor client training. For developers, Hevy Pro subscribers can mint an API key in the web app and call a public REST API at api.hevyapp.com covering workouts, a workout change-feed, routines, routine folders, exercise templates, exercise history, body measurements and account info. The company also publishes a first-party ChatGPT Custom GPT ("Hevy - Gym workout planner") whose OAuth-authenticated action spec it keeps in its own GitHub organization.
finops:
- has_sources: true
  method: derived
  name: Hevy Finops
  primary_unit: ''
  service_category: ''
  slug: hevy-finops
  template: true
image: https://www.hevyapp.com/wp-content/uploads/OG-image.png
layout: provider
modified: '2026-08-27'
name: Hevy
nav: Providers
network: true
overview: 'Hevy publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Exercise History API, Exercise Templates API, Measurements API, and 4 more. Tagged areas include Company, Fitness, Health, Workout Tracking, and Strength Training.


  The Hevy catalog on APIs.io includes 1 Spectral governance ruleset.


  Hevy''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, changelog, and 22 more developer resources.'
plans:
- name: Hevy Plans Pricing
  plan_count: 2
  slug: hevy-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Hevy Rate Limits
  slug: hevy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Hevy API Rules
  rule_count: 43
  severity_counts:
    error: 37
    hint: 0
    info: 2
    warn: 4
  slug: hevy-rules
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 47.0
    discoverability: 73.2
    operational_transparency: 34.2
  previous_composite: 47.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hevy/hevy-2026-09-02T145726.png
security:
- kind: authentication
  name: Hevy Authentication
  slug: hevy-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hevy Domain Security
  slug: hevy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: Build a Hevy training program
  slug: hevy-build-training-program
- name: Log a workout to Hevy
  slug: hevy-log-a-workout
- name: Sync a Hevy training history
  slug: hevy-sync-workout-history
- name: Track body measurements in Hevy
  slug: hevy-track-body-measurements
slug: hevy
tags:
- Company
- Fitness
- Health
- Workout Tracking
- Strength Training
- Consumer App
- Mobile
- Quantified Self
- Personal Training
- Health Data
website: https://www.hevyapp.com
---
