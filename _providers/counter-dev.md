---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Counter Dev Agentic Access
  operation_count: 8
  slug: counter-dev-agentic-access
  summary_line: 8 operations · 5 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://t.counter.dev
  baseurl_source: declared
  description: The Account API from Counter — 4 operation(s) for account.
  name: Counter Account API
  slug: counter-dev-account-api
- baseURL: https://t.counter.dev
  baseurl_source: declared
  description: The Stats API from Counter — 2 operation(s) for stats.
  name: Counter Stats API
  slug: counter-dev-stats-api
- baseURL: https://t.counter.dev
  baseurl_source: declared
  description: The Tracking API from Counter — 2 operation(s) for tracking.
  name: Counter Tracking API
  slug: counter-dev-tracking-api
artifact_total: 17
asyncapis:
- description: 'Counter publishes NO AsyncAPI of its own. This document is DERIVED by API Evangelist from the AGPL-3.0 server source at https://github.com/ihucos/counter.dev/blob/master/backend/endpoints/dump.go and '
  name: Counter Stats Stream
  slug: counter-dev-stats-asyncapi
collections:
- collection_type: open
  name: Counter Account API
  slug: open-counter-dev-account-api
- collection_type: open
  name: Counter Account Stats API
  slug: open-counter-dev-stats-api
- collection_type: open
  name: Counter Account Tracking API
  slug: open-counter-dev-tracking-api
- collection_type: open
  name: Counter API
  slug: open-counter-dev
common:
- group: other
  href: https://artifacts.apis.io/counter-dev/capabilities/counter-dev-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/counter-dev-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/counter-dev/agentic-access/counter-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/counter-dev-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/counter-dev/security/counter-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/counter-dev-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/counter-dev/authentication/counter-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/counter-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ihucos/counter.dev
- group: company
  title: ''
  type: Website
  url: https://counter.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://counter.dev/help/integration.html
- group: commercial
  href: https://artifacts.apis.io/counter-dev/plans/counter-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/counter-dev-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/counter-dev/rate-limits/counter-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/counter-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/counter-dev/finops/counter-dev-finops.yml
  title: ''
  type: FinOps
  url: finops/counter-dev-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://counter.dev/blog
- group: build
  href: https://artifacts.apis.io/counter-dev/packages/counter-dev-packages.yml
  title: ''
  type: Packages
  url: packages/counter-dev-packages.yml
- group: docs
  href: https://artifacts.apis.io/counter-dev/asyncapi/counter-dev-stats-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/counter-dev-stats-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/counter-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/counter-dev/llms/counter-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/counter-dev-llms.txt
- group: design
  href: https://artifacts.apis.io/counter-dev/conventions/counter-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/counter-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/counter-dev/errors/counter-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/counter-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/counter-dev/lifecycle/counter-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/counter-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/counter-dev/conformance/counter-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/counter-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/counter-dev/data-model/counter-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/counter-dev-data-model.yml
- group: start
  href: https://artifacts.apis.io/counter-dev/sandbox/counter-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/counter-dev-sandbox.yml
- group: build
  href: https://artifacts.apis.io/counter-dev/cli/counter-dev-cli.yml
  title: ''
  type: CLI
  url: cli/counter-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/counter-dev/components/counter-dev-components.yml
  title: ''
  type: Components
  url: components/counter-dev-components.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://counter.dev/help/integration.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://counter.dev/help/
- group: operate
  title: ''
  type: Support
  url: https://github.com/ihucos/counter.dev/issues
- group: start
  title: ''
  type: SignUp
  url: https://counter.dev/welcome.html?sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://counter.dev/pages/privacy.html
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ihucos/counter.dev
- group: commercial
  title: ''
  type: License
  url: https://github.com/ihucos/counter.dev/blob/master/LICENSE
created: '2026-06-21'
description: Counter (counter.dev) is an open-source, privacy-friendly web analytics service. A lightweight tracking snippet POSTs a single aggregated hit per visit to a public collect endpoint (t.counter.dev), and a token-authenticated dashboard data feed returns aggregated stats. Counter uses no cookies, no logging, and no IP fingerprinting. It is AGPL-3.0 licensed and can be self-hosted; the hosted service is pay-what-you-want.
finops:
- has_sources: true
  method: derived
  name: Counter Dev Finops
  primary_unit: ''
  service_category: ''
  slug: counter-dev-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/counter-dev.png
layout: provider
modified: '2026-08-13'
name: Counter
nav: Providers
network: true
overview: 'Counter publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Account API, Stats API, and Tracking API. Tagged areas include Web Analytics, Privacy, Open Source, Tracking, and Self-Hosted.


  The Counter catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Counter''s developer surface includes authentication, documentation, engineering blog, sandbox, CLI, getting-started guide, support, and 23 more developer resources.'
plans:
- name: Counter Dev Plans Pricing
  plan_count: 2
  slug: counter-dev-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Counter Dev Rate Limits
  slug: counter-dev-rate-limits
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 51.9
    developer_ergonomics: 64.9
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/counter-dev/counter-dev-2026-07-25T210507.png
security:
- kind: authentication
  name: Counter Dev Authentication
  slug: counter-dev-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Counter Dev Domain Security
  slug: counter-dev-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: counter-dev-install-tracking
  slug: counter-dev-install-tracking
- name: counter-dev-read-site-stats
  slug: counter-dev-read-site-stats
- name: counter-dev-stream-live-stats
  slug: counter-dev-stream-live-stats
slug: counter-dev
tags:
- Web Analytics
- Privacy
- Open Source
- Tracking
- Self-Hosted
website: https://counter.dev/
---
