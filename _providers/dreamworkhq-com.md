---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Dreamwork agents platform providing job search automation.
  name: Dreamwork Agents API
  slug: dreamwork-agents-api
- baseURL: https://api.dreamworkhq.com
  baseurl_source: declared
  description: 'Dreamwork API as documented publicly: 35 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: Dreamwork API
  slug: dreamworkhq-com-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/dreamworkhq-com/plans/dreamworkhq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dreamworkhq-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dreamworkhq-com/rules/dreamworkhq-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dreamworkhq-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dreamworkhq-com/json-ld/dreamworkhq-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dreamworkhq-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dreamworkhq-com/vocabulary/dreamworkhq-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dreamworkhq-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dreamworkhq-com/data-model/dreamworkhq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dreamworkhq-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dreamworkhq-com/changelog/dreamworkhq-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dreamworkhq-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/dreamworkhq-com/authentication/dreamworkhq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dreamworkhq-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dreamworkhq-com/conformance/dreamworkhq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dreamworkhq-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dreamworkhq-com/llms/dreamworkhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dreamworkhq-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dreamworkhq-com/well-known/dreamworkhq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dreamworkhq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dreamworkhq-com/hosts/dreamworkhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dreamworkhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dreamworkhq-com/vendors/dreamworkhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dreamworkhq-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Omodaka9375
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.dreamworkhq.com/agents/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dreamworkhq.com/agents/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/dreamworkhq-com/security/dreamworkhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dreamworkhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dreamworkhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dreamworkhq.com/about
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dreamworkhq.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dreamworkhq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dreamworkhq.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.dreamworkhq.com/blog
coverage:
  checked: '2026-11-06'
  detail: Documentation pages are public but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://www.dreamworkhq.com/agents/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dreamwork is an AI-powered job search platform that helps tech professionals find, tailor, and auto‑apply to relevant roles. It crawls company career sites daily, ranks openings against a user’s resume, generates customized resumes and cover letters, and can submit applications automatically or with user review. The service offers paid plans with autopilot features, integrates with MCP clients, and provides tools for tracking applications and recruiter replies.
image: https://www.dreamworkhq.com/opengraph-image?c40b7b11d866857f
json_schemas:
- name: PostJobsIdPackRequest
  property_count: 1
  slug: dreamworkhq-com-post-jobs-id-pack-request
jsonld:
- class_count: 1
  name: Dreamworkhq Com Context
  property_count: 1
  slug: dreamworkhq-com-context
layout: provider
modified: '2026-11-05'
name: Dreamwork
nav: Providers
network: true
overview: 'Dreamwork is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Job Search, Automation, TechCareer, and Platform.


  The Dreamwork catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dreamwork''s developer surface includes changelog, authentication, getting-started guide, documentation, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Dreamworkhq Com Plans Pricing
  plan_count: 3
  slug: dreamworkhq-com-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Dreamwork API Rules
  rule_count: 41
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 3
  slug: dreamworkhq-com-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dreamworkhq Com Authentication
  slug: dreamworkhq-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dreamworkhq Com Domain Security
  slug: dreamworkhq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dreamworkhq-com
tags:
- Artificial Intelligence
- Job Search
- Automation
- TechCareer
- Platform
website: https://dreamworkhq.com/
---
