---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
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
  score: 19.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for briq platform
  name: briq API
  slug: briq-api
- baseURL: https://api.briq.cloud
  baseurl_source: declared
  description: Services and sandboxes for AI agents.
  name: briq API V1 API
  slug: briq-api-v1-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/briq-cloud/rules/briq-cloud-rules.yml
  title: ''
  type: Spectral
  url: rules/briq-cloud-rules.yml
- group: design
  href: https://artifacts.apis.io/briq-cloud/json-ld/briq-cloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/briq-cloud-context.jsonld
- group: design
  href: https://artifacts.apis.io/briq-cloud/vocabulary/briq-cloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/briq-cloud-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/briq-cloud/conformance/briq-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/briq-cloud-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/briq-cloud/plans/briq-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/briq-cloud-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/briq-cloud/data-model/briq-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/briq-cloud-data-model.yml
- group: build
  href: https://artifacts.apis.io/briq-cloud/cli/briq-cloud-cli.yml
  title: ''
  type: CLI
  url: cli/briq-cloud-cli.yml
- group: operate
  href: https://artifacts.apis.io/briq-cloud/changelog/briq-cloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/briq-cloud-changelog.yml
- group: start
  href: https://artifacts.apis.io/briq-cloud/sandbox/briq-cloud-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/briq-cloud-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/briq-cloud/authentication/briq-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/briq-cloud-authentication.yml
- group: design
  href: https://artifacts.apis.io/briq-cloud/errors/briq-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/briq-cloud-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/briq-cloud/llms/briq-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/briq-cloud-llms.txt
- group: agent
  href: https://artifacts.apis.io/briq-cloud/well-known/briq-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/briq-cloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/briq-cloud/hosts/briq-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/briq-cloud-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://briq.cloud/legal/terms
- group: start
  title: ''
  type: SignUp
  url: https://briq.cloud/sign-up
- group: start
  title: ''
  type: Sandbox
  url: https://briq.cloud/cookbook/sandbox
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://briq.cloud/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/briq-cloud
- group: operate
  title: ''
  type: ChangeLog
  url: https://briq.cloud/blog/category/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.n8n.io/connect/n8n-api
- group: auth
  href: https://artifacts.apis.io/briq-cloud/security/briq-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/briq-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://briq.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://briq.cloud/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://briq.cloud/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://briq.cloud/#pricing
- group: company
  title: ''
  type: Blog
  url: https://briq.cloud/blog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://briq.cloud/v1/openapi.json
  - status: null
    url: https://api.briq.cloud/v1/openapi.json
  - status: null
    url: https://app.briq.cloud/v1/openapi.json
  - status: 401
    url: https://api.briq.cloud/mcp
  - status: 401
    url: https://briq.cloud/v1/graphql
  - status: 401
    url: https://api.briq.cloud/v1/graphql
  reason: partner-login
  state: gated
created: '2026-11-03'
description: briq provides coding agents with real databases, sandboxed environments, and full‑stack applications accessible via a single MCP call. Hosted in the EU, the platform bills by the second, offers a capped budget, and emphasizes security and isolation for AI‑driven workloads. It enables developers to prototype, test, and run code in production‑like settings without managing infrastructure, targeting AI, automation, and low‑latency use cases.
image: https://briq.cloud/opengraph-image?564364a0b058c19b
json_schemas:
- name: Briq
  property_count: 26
  slug: briq-cloud-briq
- name: KeyPolicy
  property_count: 6
  slug: briq-cloud-key-policy
- name: RunBody
  property_count: 0
  slug: briq-cloud-run-body
- name: StackForkBody
  property_count: 5
  slug: briq-cloud-stack-fork-body
- name: StackUpBody
  property_count: 6
  slug: briq-cloud-stack-up-body
- name: StackUpResult
  property_count: 7
  slug: briq-cloud-stack-up-result
jsonld:
- class_count: 18
  name: Briq Cloud Context
  property_count: 73
  slug: briq-cloud-context
layout: provider
modified: '2026-11-03'
name: briq
nav: Providers
network: true
overview: 'briq publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API V1 API, and 1 more. Tagged areas include Artificial Intelligence, Cloud, Sandbox, Database, and Platform.


  The briq catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  briq''s developer surface includes CLI, changelog, sandbox, authentication, signup flow, API reference, documentation, and 20 more developer resources.'
plans:
- name: Briq Cloud Plans Pricing
  plan_count: 3
  slug: briq-cloud-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: briq API Rules
  rule_count: 43
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 6
  slug: briq-cloud-rules
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 41.7
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Briq Cloud Authentication
  slug: briq-cloud-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Briq Cloud Domain Security
  slug: briq-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: briq-cloud
tags:
- Artificial Intelligence
- Cloud
- Sandbox
- Database
- Platform
- Company
website: https://briq.cloud/
---
