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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.hookdeploy.dev
  baseurl_source: declared
  description: 'HookDeploy API as documented publicly: 25 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: HookDeploy API
  slug: hookdeploy-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/hookdeploy/plans/hookdeploy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hookdeploy-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hookdeploy/rules/hookdeploy-rules.yml
  title: ''
  type: Spectral
  url: rules/hookdeploy-rules.yml
- group: design
  href: https://artifacts.apis.io/hookdeploy/json-ld/hookdeploy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hookdeploy-context.jsonld
- group: design
  href: https://artifacts.apis.io/hookdeploy/vocabulary/hookdeploy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hookdeploy-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/hookdeploy/data-model/hookdeploy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hookdeploy-data-model.yml
- group: build
  href: https://artifacts.apis.io/hookdeploy/cli/hookdeploy-cli.yml
  title: ''
  type: CLI
  url: cli/hookdeploy-cli.yml
- group: design
  href: https://artifacts.apis.io/hookdeploy/conventions/hookdeploy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hookdeploy-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://hookdeploy.dev/security/
- group: auth
  href: https://artifacts.apis.io/hookdeploy/authentication/hookdeploy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hookdeploy-authentication.yml
- group: design
  href: https://artifacts.apis.io/hookdeploy/conformance/hookdeploy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hookdeploy-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hookdeploy/llms/hookdeploy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hookdeploy-llms.txt
- group: other
  href: https://artifacts.apis.io/hookdeploy/hosts/hookdeploy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hookdeploy-hosts.yml
- group: other
  href: https://artifacts.apis.io/hookdeploy/vendors/hookdeploy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hookdeploy-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://hookdeploy.dev/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hookdeploy.dev/terms
- group: auth
  title: ''
  type: Security
  url: https://hookdeploy.dev/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hookdeploy.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hookdeploy
- group: operate
  title: ''
  type: ChangeLog
  url: https://hookdeploy.dev/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://hookdeploy.dev/docs/getting-started/introduction
- group: auth
  href: https://artifacts.apis.io/hookdeploy/security/hookdeploy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hookdeploy-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hookdeploy/security/hookdeploy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hookdeploy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hookdeploy.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://hookdeploy.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://hookdeploy.dev/docs/api/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://hookdeploy.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://hookdeploy.dev/blog
- group: operate
  title: ''
  type: Support
  url: https://hookdeploy.dev/support
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI/AsyncAPI/GraphQL spec found at the API host; attempts returned 404.
  evidence:
  - status: 404
    url: https://api.hookdeploy.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: HookDeploy provides a private webhook delivery platform that captures incoming webhooks at the edge and forwards them securely to user-defined endpoints, even behind firewalls. It offers a source‑available agent for outbound mTLS connections, a developer‑friendly dashboard, and integrations with services like Stripe, GitHub, Shopify, Twilio, and Linear. Users can start for free with generous limits, access detailed documentation, and benefit from built‑in security features such as encrypted traffic and no open ports.
image: https://static.hookdeploy.dev/metav2.png
json_schemas:
- name: GetV1EndpointsIdResponse
  property_count: 1
  slug: hookdeploy-get-v1-endpoints-id-response
- name: GetV1EndpointsResponse
  property_count: 1
  slug: hookdeploy-get-v1-endpoints-response
- name: GetV1UsageResponse
  property_count: 1
  slug: hookdeploy-get-v1-usage-response
- name: PatchV1EndpointsIdRequest
  property_count: 4
  slug: hookdeploy-patch-v1-endpoints-id-request
- name: PatchV1EndpointsIdResponse
  property_count: 1
  slug: hookdeploy-patch-v1-endpoints-id-response
- name: PostV1MembersInviteResponse
  property_count: 1
  slug: hookdeploy-post-v1-members-invite-response
jsonld:
- class_count: 10
  name: Hookdeploy Context
  property_count: 7
  slug: hookdeploy-context
layout: provider
modified: '2026-10-17'
name: HookDeploy
nav: Providers
network: true
overview: 'HookDeploy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Webhook, PrivateInfrastructure, Security, Integration, and Developer Tools.


  The HookDeploy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HookDeploy''s developer surface includes CLI, authentication, changelog, getting-started guide, documentation, API reference, pricing, and 21 more developer resources.'
plans:
- name: Hookdeploy Plans Pricing
  plan_count: 5
  slug: hookdeploy-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: HookDeploy API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: hookdeploy-rules
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 23.7
    developer_ergonomics: 54.8
    discoverability: 66.1
    operational_transparency: 39.5
  previous_composite: 49.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hookdeploy Authentication
  slug: hookdeploy-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hookdeploy Domain Security
  slug: hookdeploy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Hookdeploy Trust Center
  slug: hookdeploy-trust-center
  summary_line: SOC 2
slug: hookdeploy
tags:
- Webhook
- PrivateInfrastructure
- Security
- Integration
- Developer Tools
website: https://hookdeploy.dev/
---
