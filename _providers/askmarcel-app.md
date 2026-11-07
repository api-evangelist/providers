---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API REST for accessing technical knowledge from AskMarcel.
  name: AskMarcel API
  slug: askmarcel-api
artifact_total: 7
asyncapis:
- description: ''
  name: Askmarcel App Webhooks
  slug: askmarcel-app-webhooks
common:
- group: design
  href: https://artifacts.apis.io/askmarcel-app/rules/askmarcel-app-rules.yml
  title: ''
  type: Spectral
  url: rules/askmarcel-app-rules.yml
- group: design
  href: https://artifacts.apis.io/askmarcel-app/json-ld/askmarcel-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/askmarcel-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/askmarcel-app/vocabulary/askmarcel-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/askmarcel-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/askmarcel-app/conventions/askmarcel-app-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/askmarcel-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/askmarcel-app/conventions/askmarcel-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/askmarcel-app-conventions.yml
- group: commercial
  href: https://artifacts.apis.io/askmarcel-app/plans/askmarcel-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askmarcel-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/askmarcel-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/askmarcel-app/asyncapi/askmarcel-app-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/askmarcel-app-webhooks.yml
- group: design
  href: https://artifacts.apis.io/askmarcel-app/data-model/askmarcel-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/askmarcel-app-data-model.yml
- group: auth
  href: https://artifacts.apis.io/askmarcel-app/authentication/askmarcel-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/askmarcel-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/askmarcel-app/errors/askmarcel-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/askmarcel-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/askmarcel-app/conformance/askmarcel-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/askmarcel-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/askmarcel-app/llms/askmarcel-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askmarcel-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/askmarcel-app/well-known/askmarcel-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askmarcel-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/askmarcel-app/hosts/askmarcel-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askmarcel-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/askmarcel-app/vendors/askmarcel-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askmarcel-app-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://askmarcel.app/fr/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askmarcel.app/fr/privacy
- group: start
  title: ''
  type: Login
  url: https://dashboard.askmarcel.app/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.askmarcel.app/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://askmarcel.app/fr/api/docs/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/askmarcel
- group: auth
  href: https://artifacts.apis.io/askmarcel-app/security/askmarcel-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askmarcel-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askmarcel.app/
- group: docs
  title: ''
  type: Documentation
  url: https://askmarcel.app/en/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://askmarcel.app/en/api
- group: company
  title: ''
  type: Blog
  url: https://askmarcel.app/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://askmarcel.app/en/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.askmarcel.app/v1/openapi.json
  - status: 401
    url: https://api.askmarcel.app/api/mcp
  - status: 401
    url: https://app.askmarcel.app/api/mcp
  - status: 401
    url: https://web.askmarcel.app/api/mcp
  - status: 200
    url: https://askmarcel.app/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Ask Marcel provides the largest HVAC troubleshooting database for UK engineers, offering over 400,000 error codes across 126 brands and 905 models. The platform includes a web and mobile app, API/MCP for developers, and detailed documentation to integrate fault code lookup into tools and services. It aims to simplify HVAC maintenance, reduce downtime, and support both technicians and integrators with comprehensive manufacturer-sourced information.
image: https://askmarcel.app/opengraph-image
jsonld:
- class_count: 55
  name: Askmarcel App Context
  property_count: 214
  slug: askmarcel-app-context
layout: provider
modified: '2026-11-01'
name: Ask Marcel
nav: Providers
network: true
overview: 'Ask Marcel publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include HVAC, Engineering, Troubleshooting, and Database.


  The Ask Marcel catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Ask Marcel''s developer surface includes authentication, support, getting-started guide, documentation, API reference, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Askmarcel App Plans Pricing
  plan_count: 3
  slug: askmarcel-app-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Ask Marcel API Rules
  rule_count: 44
  severity_counts:
    error: 33
    hint: 0
    info: 4
    warn: 7
  slug: askmarcel-app-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 60.8
    catalog_earned_first_party: 12.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 48.7
    contract_governance: 35.6
    contract_quality: 53.2
    developer_ergonomics: 41.0
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 52.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Askmarcel App Authentication
  slug: askmarcel-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Askmarcel App Domain Security
  slug: askmarcel-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: askmarcel-app
tags:
- HVAC
- Engineering
- Troubleshooting
- Database
website: https://askmarcel.app/
---
