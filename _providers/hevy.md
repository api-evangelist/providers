---
access_model:
  confidence: high
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-02'
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
artifact_total: 11
common:
- group: other
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
  title: ''
  type: ChangeLog
  url: changelog/hevy-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hevy-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hevy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hevy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hevy-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hevy-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hevy-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hevy-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/hevy-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hevy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hevy-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hevy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-27'
description: Hevy is a gym workout tracker and planner app for iOS, Android and the web, operated by Hevy Studios, S.L. and used by a community the company describes as 15+ million lifters. Members log strength-training sessions, build and reuse routines, organize them into folders, browse a large exercise library, and track body measurements and progress over time. Hevy also runs Hevy Coach, a separate product for personal trainers who program and monitor client training. For developers, Hevy Pro subscribers can mint an API key in the web app and call a public REST API at api.hevyapp.com covering workouts, a workout change-feed, routines, routine folders, exercise templates, exercise history, body measurements and account info. The company also publishes a first-party ChatGPT Custom GPT ("Hevy - Gym workout planner") whose OAuth-authenticated action spec it keeps in its own GitHub organization.
image: https://www.hevyapp.com/wp-content/uploads/OG-image.png
layout: provider
modified: '2026-08-27'
name: Hevy
nav: Providers
network: true
overview: 'Hevy publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Exercise History API, Exercise Templates API, Measurements API, and 4 more. Tagged areas include Company, Fitness, Health, Workout Tracking, and Strength Training.


  Hevy''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, changelog, and 22 more developer resources.'
plans:
- name: Hevy Plans Pricing
  plan_count: 2
  slug: hevy-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Hevy Rate Limits
  slug: hevy-rate-limits
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 45.9
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 50.9
  provenance:
    conformance: derived
    contracts:
      callable: 57.1
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
    score: 47.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hevy/refs/heads/main/screenshots/hevy-2026-09-02T145726.png
security:
- kind: authentication
  name: Hevy Authentication
  slug: hevy-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hevy Domain Security
  slug: hevy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hevy
tags:
- Company
- Fitness
- Health
- Workout Tracking
- Strength Training
- Consumer Apps
- Mobile
- Quantified Self
- Personal Training
- Health Data
website: https://www.hevyapp.com
---
