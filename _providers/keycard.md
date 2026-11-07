---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Keycard provides a platform for secure identity and access management.
  name: Keycard API
  slug: keycard-api-2
- baseURL: https://api.anthropic.com
  baseurl_source: declared
  description: 'Keycard API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Keycard API
  slug: keycard-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/keycard/plans/keycard-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/keycard-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/keycard/rules/keycard-rules.yml
  title: ''
  type: Spectral
  url: rules/keycard-rules.yml
- group: design
  href: https://artifacts.apis.io/keycard/json-ld/keycard-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/keycard-context.jsonld
- group: design
  href: https://artifacts.apis.io/keycard/vocabulary/keycard-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/keycard-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/keycard/data-model/keycard-data-model.yml
  title: ''
  type: DataModel
  url: data-model/keycard-data-model.yml
- group: build
  href: https://artifacts.apis.io/keycard/cli/keycard-cli.yml
  title: ''
  type: CLI
  url: cli/keycard-cli.yml
- group: auth
  href: https://artifacts.apis.io/keycard/authentication/keycard-authentication.yml
  title: ''
  type: Authentication
  url: authentication/keycard-authentication.yml
- group: design
  href: https://artifacts.apis.io/keycard/conformance/keycard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/keycard-conformance.yml
- group: agent
  href: https://artifacts.apis.io/keycard/llms/keycard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/keycard-llms.txt
- group: auth
  href: https://artifacts.apis.io/keycard/well-known/keycard-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/keycard-www-security.txt
- group: agent
  href: https://artifacts.apis.io/keycard/well-known/keycard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/keycard-well-known.yml
- group: other
  href: https://artifacts.apis.io/keycard/hosts/keycard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/keycard-hosts.yml
- group: other
  href: https://artifacts.apis.io/keycard/vendors/keycard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/keycard-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.keycard.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.keycard.ai/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.keycard.ai/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keycardai
- group: company
  title: ''
  type: Blog
  url: https://www.keycard.ai/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.keycard.ai/guides/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.keycard.ai/
- group: auth
  href: https://artifacts.apis.io/keycard/security/keycard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keycard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://keycard.sh
coverage:
  checked: '2026-10-24'
  detail: Documentation at https://docs.keycard.ai is HTML without a machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://docs.keycard.ai
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Keycard provides runtime authentication and authorization for software agents, giving each agent its own identity, scoped access tokens, and policy‑based control over resources. The platform integrates with existing identity providers and supports policy‑as‑code written in Cedar, enabling enterprises to manage agent permissions dynamically without long‑lived credentials.
image: https://www.keycard.ai/img/og/og-home.png
json_schemas:
- name: GetV1Response
  property_count: 2
  slug: keycard-get-v1-response
- name: PostA2AJsonrpcRequest
  property_count: 4
  slug: keycard-post-a2-ajsonrpc-request
- name: PostOauthTokenResponse
  property_count: 2
  slug: keycard-post-oauth-token-response
- name: PostV1MessagesRequest
  property_count: 3
  slug: keycard-post-v1-messages-request
- name: PostV1ResponsesRequest
  property_count: 2
  slug: keycard-post-v1-responses-request
- name: PostV1ResponsesResponse
  property_count: 2
  slug: keycard-post-v1-responses-response
jsonld:
- class_count: 7
  name: Keycard Context
  property_count: 9
  slug: keycard-context
layout: provider
modified: '2026-10-24'
name: Keycard
nav: Providers
network: true
overview: 'Keycard is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication, Authorization, Identity, Agent Security, and Policy as Code.


  The Keycard catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Keycard''s developer surface includes CLI, authentication, pricing, engineering blog, getting-started guide, and 17 more developer resources.'
plans:
- name: Keycard Plans Pricing
  plan_count: 3
  slug: keycard-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Keycard API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: keycard-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 46.1
    contract_governance: 35.6
    contract_quality: 24.2
    developer_ergonomics: 31.0
    discoverability: 64.3
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.3
  provenance:
    conformance: first-party
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
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/keycard/keycard-2026-11-03T134359.png
security:
- kind: authentication
  name: Keycard Authentication
  slug: keycard-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Keycard Domain Security
  slug: keycard-domain-security
  summary_line: TLSv1.3 · HSTS
slug: keycard
tags:
- Authentication
- Authorization
- Identity
- Agent Security
- Policy as Code
- Runtime Access
website: https://keycard.sh
---
