---
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
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Opsmeter provides AI cost tracking and control APIs as documented in the Quickstart guide.
  name: Opsmeter API
  slug: opsmeter-api-2
- baseURL: https://api.opsmeter.io
  baseurl_source: declared
  description: 'Opsmeter.io API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Opsmeter.io API
  slug: opsmeter-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/opsmeter/plans/opsmeter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opsmeter-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/opsmeter/rules/opsmeter-rules.yml
  title: ''
  type: Spectral
  url: rules/opsmeter-rules.yml
- group: design
  href: https://artifacts.apis.io/opsmeter/json-ld/opsmeter-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/opsmeter-context.jsonld
- group: design
  href: https://artifacts.apis.io/opsmeter/vocabulary/opsmeter-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/opsmeter-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/opsmeter/data-model/opsmeter-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opsmeter-data-model.yml
- group: design
  href: https://artifacts.apis.io/opsmeter/conventions/opsmeter-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/opsmeter-conventions.yml
- group: design
  href: https://artifacts.apis.io/opsmeter/conventions/opsmeter-conventions.yml
  title: ''
  type: Conventions
  url: conventions/opsmeter-conventions.yml
- group: auth
  href: https://artifacts.apis.io/opsmeter/authentication/opsmeter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opsmeter-authentication.yml
- group: design
  href: https://artifacts.apis.io/opsmeter/conformance/opsmeter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opsmeter-conformance.yml
- group: agent
  href: https://artifacts.apis.io/opsmeter/llms/opsmeter-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opsmeter-llms.txt
- group: other
  href: https://artifacts.apis.io/opsmeter/hosts/opsmeter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opsmeter-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://opsmeter.io/security
- group: start
  title: ''
  type: GettingStarted
  url: https://opsmeter.io/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/opsmeter/security/opsmeter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opsmeter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opsmeter.io/
- group: docs
  title: ''
  type: Documentation
  url: https://opsmeter.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://opsmeter.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://opsmeter.io/blog
- group: operate
  title: ''
  type: Support
  url: https://opsmeter.io/support
- group: operate
  title: ''
  type: StatusPage
  url: https://opsmeter.io/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opsmeter.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opsmeter.io/terms
- group: start
  title: ''
  type: SignUp
  url: https://opsmeter.io/register
- group: start
  title: ''
  type: Login
  url: https://opsmeter.io/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opsmeter-io
coverage:
  checked: '2026-10-18'
  detail: The API documentation is served as HTML pages without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://opsmeter.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Opsmeter.io provides AI cost and inference control to prevent large language model bill shock. It offers root‑cause visibility into deployments, endpoints, tenants, and prompts, delivering real‑time drift detection, budget guardrails, and detailed attribution across OpenAI, Anthropic, Azure OpenAI, and Google Gemini. Users can set thresholds, receive alerts, and investigate cost spikes before month‑end, all without proxy rewrites or traffic changes.
image: https://opsmeter.io/assets/brand/og-landing.png
json_schemas:
- name: GetV1DiagnosticsWorkspaceStatusResponse
  property_count: 9
  slug: opsmeter-get-v1-diagnostics-workspace-status-response
- name: GetV1SettingsWorkspaceStatusResponse
  property_count: 9
  slug: opsmeter-get-v1-settings-workspace-status-response
- name: PostV1BillingSubscriptionChangePlanResponse
  property_count: 1
  slug: opsmeter-post-v1-billing-subscription-change-plan-response
jsonld:
- class_count: 3
  name: Opsmeter Context
  property_count: 10
  slug: opsmeter-context
layout: provider
modified: '2026-10-18'
name: Opsmeter.io
nav: Providers
network: true
overview: 'Opsmeter.io publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Cost Management, Monitoring, and Observability.


  The Opsmeter.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Opsmeter.io''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, support, signup flow, and 18 more developer resources.'
plans:
- name: Opsmeter Plans Pricing
  plan_count: 5
  slug: opsmeter-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Opsmeter.io API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: opsmeter-rules
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.0
    catalog_earned_first_party: 12.0
    catalog_gap: 49.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 19.7
    contract_quality: 23.5
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Opsmeter Authentication
  slug: opsmeter-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Opsmeter Domain Security
  slug: opsmeter-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opsmeter
tags:
- Company
- Artificial Intelligence
- Cost Management
- Monitoring
- Observability
website: https://opsmeter.io/
---
