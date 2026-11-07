---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API for controlling cloud browsers, managing sessions, leads, scraping jobs and email validation.
  name: Scrappy API
  slug: scrappy-api
- description: 'Scrappy.gg API as documented publicly: 94 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Scrappy.gg API
  slug: scrappy-gg-api
artifact_total: 14
asyncapis:
- description: ''
  name: Scrappy Gg Webhooks
  slug: scrappy-gg-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/scrappy-gg/plans/scrappy-gg-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scrappy-gg-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/scrappy-gg/rules/scrappy-gg-rules.yml
  title: ''
  type: Spectral
  url: rules/scrappy-gg-rules.yml
- group: design
  href: https://artifacts.apis.io/scrappy-gg/json-ld/scrappy-gg-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/scrappy-gg-context.jsonld
- group: design
  href: https://artifacts.apis.io/scrappy-gg/vocabulary/scrappy-gg-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/scrappy-gg-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/scrappy-gg/asyncapi/scrappy-gg-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/scrappy-gg-webhooks.yml
- group: design
  href: https://artifacts.apis.io/scrappy-gg/data-model/scrappy-gg-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scrappy-gg-data-model.yml
- group: design
  href: https://artifacts.apis.io/scrappy-gg/conventions/scrappy-gg-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/scrappy-gg-conventions.yml
- group: design
  href: https://artifacts.apis.io/scrappy-gg/conventions/scrappy-gg-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scrappy-gg-conventions.yml
- group: auth
  href: https://artifacts.apis.io/scrappy-gg/authentication/scrappy-gg-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scrappy-gg-authentication.yml
- group: design
  href: https://artifacts.apis.io/scrappy-gg/conformance/scrappy-gg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scrappy-gg-conformance.yml
- group: agent
  href: https://artifacts.apis.io/scrappy-gg/llms/scrappy-gg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scrappy-gg-llms.txt
- group: other
  href: https://artifacts.apis.io/scrappy-gg/hosts/scrappy-gg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scrappy-gg-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scrappy.gg/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://scrappy.gg/changelog
- group: start
  title: ''
  type: SignUp
  url: https://scrappy.gg/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://scrappy.gg/md/docs/guides/quickstart
- group: auth
  href: https://artifacts.apis.io/scrappy-gg/security/scrappy-gg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scrappy-gg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scrappy.gg
- group: docs
  title: ''
  type: Documentation
  url: https://scrappy.gg/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://scrappy.gg/pricing
- group: company
  title: ''
  type: Blog
  url: https://scrappy.gg/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scrappy.gg/docs/guides/terms
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://scrappy.gg/api/mcp
  - status: 200
    url: https://scrappy.gg
  reason: partner-login
  state: gated
created: '2026-11-03'
description: Scrappy.gg provides a cloud‑based real Chrome browser that developers, AI agents, and businesses can control via a REST API or MCP. It enables residential IP exits, saved logins, live takeover, and full lead‑generation pipelines, supporting web automation, scraping, email finding, and sales prospecting with a scalable browser infrastructure.
image: https://scrappy.gg/og-image.png
json_schemas:
- name: GetApiEmailVerificationStatsResponse
  property_count: 8
  slug: scrappy-gg-get-api-email-verification-stats-response
- name: PatchApiLeadsRequest
  property_count: 6
  slug: scrappy-gg-patch-api-leads-request
- name: PostApiLeadsRequest
  property_count: 7
  slug: scrappy-gg-post-api-leads-request
- name: PostApiProfilesExportRequest
  property_count: 5
  slug: scrappy-gg-post-api-profiles-export-request
- name: PostApiSourcesGenerateRequest
  property_count: 6
  slug: scrappy-gg-post-api-sources-generate-request
- name: PostApiSourcesRequest
  property_count: 6
  slug: scrappy-gg-post-api-sources-request
jsonld:
- class_count: 120
  name: Scrappy Gg Context
  property_count: 151
  slug: scrappy-gg-context
layout: provider
modified: '2026-11-03'
name: Scrappy.gg
nav: Providers
network: true
overview: 'Scrappy.gg is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Browser, Automation, Lead Generation, AI Agents, and Web Scraping.


  The Scrappy.gg catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Scrappy.gg''s developer surface includes authentication, changelog, signup flow, getting-started guide, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Scrappy Gg Plans Pricing
  plan_count: 3
  slug: scrappy-gg-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Scrappy.gg API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: scrappy-gg-rules
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 35.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Scrappy Gg Authentication
  slug: scrappy-gg-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Scrappy Gg Domain Security
  slug: scrappy-gg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scrappy-gg
tags:
- Cloud Browser
- Automation
- Lead Generation
- AI Agents
- Web Scraping
- Company
website: https://scrappy.gg
---
