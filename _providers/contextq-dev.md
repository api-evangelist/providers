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
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Persistent, searchable memory API for AI coding agents. Documentation at https://app.contextq.dev/docs
  name: ContextQ API
  slug: contextq-api
- description: 'ContextQ API as documented publicly: 97 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: ContextQ API
  slug: contextq-dev-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/contextq-dev/plans/contextq-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contextq-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/contextq-dev/rules/contextq-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/contextq-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/contextq-dev/json-ld/contextq-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/contextq-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/contextq-dev/vocabulary/contextq-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contextq-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/contextq-dev/data-model/contextq-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/contextq-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/contextq-dev/changelog/contextq-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/contextq-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/contextq-dev/conventions/contextq-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/contextq-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/contextq-dev/conventions/contextq-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/contextq-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/contextq-dev/authentication/contextq-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contextq-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/contextq-dev/conformance/contextq-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contextq-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contextq-dev/llms/contextq-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextq-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/contextq-dev/well-known/contextq-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contextq-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/contextq-dev/hosts/contextq-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextq-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/contextq-dev/vendors/contextq-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contextq-dev-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://contextq.dev/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://contextq.dev/changelog
- group: auth
  href: https://artifacts.apis.io/contextq-dev/security/contextq-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/contextq-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/contextq-dev/security/contextq-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextq-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contextq.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://contextq.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://contextq.dev/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://contextq.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contextq.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contextq.dev/privacy
coverage:
  checked: '2026-11-04'
  detail: API documentation is served via Swagger UI HTML pages without a machine‑readable OpenAPI spec
  evidence:
  - status: 200
    url: https://app.contextq.dev/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: ContextQ provides persistent, searchable memory for AI coding agents, enabling them to retain and retrieve contextual information across conversations, projects, and tools. The platform offers a suite of MCP tools, integrates with popular AI models, and supports self‑hosted deployments, pricing plans, and extensive documentation for developers.
image: https://contextq.dev/og.png
json_schemas:
- name: GetPluginInstallShResponse
  property_count: 1
  slug: contextq-dev-get-plugin-install-sh-response
- name: PostApiGoalSyncRequest
  property_count: 2
  slug: contextq-dev-post-api-goal-sync-request
- name: PostApiGoalSyncResponse
  property_count: 3
  slug: contextq-dev-post-api-goal-sync-response
- name: PostApiWebhookEndpointsIdTestResponse
  property_count: 5
  slug: contextq-dev-post-api-webhook-endpoints-id-test-response
jsonld:
- class_count: 4
  name: q Dev Context
  property_count: 3
  slug: contextq-dev-context
layout: provider
modified: '2026-11-04'
name: ContextQ
nav: Providers
network: true
overview: 'ContextQ is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, Persistent, Context, and Agents.


  The ContextQ catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ContextQ''s developer surface includes changelog, authentication, documentation, getting-started guide, pricing, and 19 more developer resources.'
plans:
- name: Contextq Dev Plans Pricing
  plan_count: 4
  slug: contextq-dev-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: ContextQ API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: contextq-dev-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 20.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Contextq Dev Authentication
  slug: contextq-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Contextq Dev Domain Security
  slug: contextq-dev-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Contextq Dev Vulnerability Disclosure
  slug: contextq-dev-vulnerability-disclosure
  summary_line: no policy recorded
slug: contextq-dev
tags:
- Artificial Intelligence
- Memory
- Persistent
- Context
- Agents
- Platform
website: https://contextq.dev/
---
