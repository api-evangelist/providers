---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Project API key access to the Appie HTTP API, MCP tools, and Event Store events.
  name: Appie API
  slug: appie-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/appie-run/plans/appie-run-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appie-run-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/appie-run/vocabulary/appie-run-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/appie-run-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/appie-run/cli/appie-run-cli.yml
  title: ''
  type: CLI
  url: cli/appie-run-cli.yml
- group: design
  href: https://artifacts.apis.io/appie-run/conformance/appie-run-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appie-run-conformance.yml
- group: agent
  href: https://artifacts.apis.io/appie-run/llms/appie-run-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appie-run-llms.txt
- group: agent
  href: https://artifacts.apis.io/appie-run/well-known/appie-run-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appie-run-well-known.yml
- group: other
  href: https://artifacts.apis.io/appie-run/hosts/appie-run-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appie-run-hosts.yml
- group: other
  href: https://artifacts.apis.io/appie-run/vendors/appie-run-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appie-run-vendors.yml
- group: build
  href: https://artifacts.apis.io/appie-run/packages/appie-run-packages.yml
  title: ''
  type: SDKs
  url: packages/appie-run-packages.yml
- group: build
  href: https://artifacts.apis.io/appie-run/packages/appie-run-packages.yml
  title: ''
  type: Packages
  url: packages/appie-run-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://appie.run/help-center
- group: docs
  title: ''
  type: APIReference
  url: https://appie.run/docs/api
- group: auth
  href: https://artifacts.apis.io/appie-run/security/appie-run-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appie-run-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appie.run/
- group: docs
  title: ''
  type: Documentation
  url: https://appie.run/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://appie.run/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appie.run/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appie.run/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://appie.run/openapi.json
  - status: 401
    url: https://appie.run/mcp
  - status: 200
    url: https://appie.run/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Appie is an AI marketing stack that learns your brand and runs growth, content, chatbots, social, influencer, and marketplace tools. It offers a free tier with no credit card required, and paid plans for 2,000 and 5,000 credits per month, providing automated marketing solutions for businesses.
layout: provider
modified: '2026-11-01'
name: Appie
nav: Providers
network: true
overview: 'Appie is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, Automation, Software-as-a-Service, and Platform.


  Appie''s developer surface includes CLI, support, API reference, documentation, pricing, and 13 more developer resources.'
plans:
- name: Appie Run Plans Pricing
  plan_count: 3
  slug: appie-run-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 48.3
    catalog_earned_first_party: 12.0
    catalog_gap: 66.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 47.4
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 28.2
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appie Run Domain Security
  slug: appie-run-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appie-run
tags:
- Artificial Intelligence
- Marketing
- Automation
- Software-as-a-Service
- Platform
website: https://appie.run/
---
