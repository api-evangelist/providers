---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Busymate provides a platform to capture, inspect, and debug HTTPS traffic across iOS, Android, browsers, and backend services. Documentation is at https://docs.busymate.dev and a quickstart guide at h
  name: Busymate API
  slug: busymate-api
- baseURL: https://api.busymate.net
  baseurl_source: declared
  description: 'Busymate DevTools core API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Busymate DevTools core API
  slug: core-api
- baseURL: https://api.busymate.net
  baseurl_source: declared
  description: 'Busymate DevTools federation API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Busymate DevTools federation API
  slug: federation-api
- baseURL: https://api.busymate.net
  baseurl_source: declared
  description: 'Busymate DevTools mcp API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Busymate DevTools mcp API
  slug: mcp-api
artifact_total: 22
common:
- group: commercial
  href: https://artifacts.apis.io/busymate-dev/plans/busymate-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/busymate-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/busymate-dev/rules/busymate-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/busymate-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/busymate-dev/json-ld/busymate-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/busymate-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/busymate-dev/vocabulary/busymate-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/busymate-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/busymate-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/busymate-dev/data-model/busymate-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/busymate-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/busymate-dev/cli/busymate-dev-cli.yml
  title: ''
  type: CLI
  url: cli/busymate-dev-cli.yml
- group: operate
  href: https://artifacts.apis.io/busymate-dev/changelog/busymate-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/busymate-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/busymate-dev/conformance/busymate-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/busymate-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/busymate-dev/llms/busymate-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/busymate-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/busymate-dev/well-known/busymate-dev-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/busymate-dev-support-security.txt
- group: agent
  href: https://artifacts.apis.io/busymate-dev/well-known/busymate-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/busymate-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/busymate-dev/hosts/busymate-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/busymate-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/busymate-dev/vendors/busymate-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/busymate-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://busymate.dev/terms
- group: operate
  title: ''
  type: Support
  url: https://support.busymate.dev/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.busymate.dev/
- group: auth
  title: ''
  type: Security
  url: https://busymate.dev/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://busymate.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://busymate.dev/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/serebano
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.busymate.dev/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://busymate.dev/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.busymate.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.busymate.dev\\\
- group: auth
  href: https://artifacts.apis.io/busymate-dev/security/busymate-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/busymate-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/busymate-dev/security/busymate-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/busymate-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://busymate.dev/
coverage:
  checked: '2026-11-03'
  detail: Docs are public HTML but no OpenAPI/GraphQL/AsyncAPI spec is accessible; GraphQL endpoint returns 401 unauthorized.
  evidence:
  - status: 401
    url: https://api.busymate.dev/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Busymate DevTools provides a platform to capture, inspect, and debug HTTPS traffic across iOS devices, Android, browsers, and backend services in real time. It offers a live feed of network requests, tools to pause, modify, replay traffic, and AI assistance to analyze data, supporting over 459 tools for developers and security teams.
image: https://busymate.dev/opengraph-image?7e279cdbec081e1e
json_schemas:
- name: GetCaBundleResponse
  property_count: 2
  slug: busymate-dev-get-ca-bundle-response
- name: GetLoginResponse
  property_count: 3
  slug: busymate-dev-get-login-response
- name: GetRestV1ServiceStatsResponse
  property_count: 1
  slug: busymate-dev-get-rest-v1-service-stats-response
- name: GetRestV1ServiceStatusResponse
  property_count: 1
  slug: busymate-dev-get-rest-v1-service-status-response
- name: PostAllocateRequest
  property_count: 3
  slug: busymate-dev-post-allocate-request
- name: PostAllocateResponse
  property_count: 4
  slug: busymate-dev-post-allocate-response
- name: PostExchangeRequest
  property_count: 2
  slug: busymate-dev-post-exchange-request
- name: PostExchangeResponse
  property_count: 6
  slug: busymate-dev-post-exchange-response
- name: PostFunctionsV1FederationBrokerExchangeResponse
  property_count: 6
  slug: busymate-dev-post-functions-v1-federation-broker-exchange-response
- name: PostFunctionsV1FederationBrokerStartResponse
  property_count: 3
  slug: busymate-dev-post-functions-v1-federation-broker-start-response
- name: PostStartRequest
  property_count: 7
  slug: busymate-dev-post-start-request
- name: PostStartResponse
  property_count: 3
  slug: busymate-dev-post-start-response
- name: PostV1CheckoutConfirmRequest
  property_count: 3
  slug: busymate-dev-post-v1-checkout-confirm-request
jsonld:
- class_count: 17
  name: Busymate Dev Context
  property_count: 32
  slug: busymate-dev-context
layout: provider
modified: '2026-11-03'
name: Busymate DevTools
nav: Providers
network: true
overview: 'Busymate DevTools is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including core API, federation API, mcp API, and 1 more. Tagged areas include Developer Tools, Network Monitoring, HTTPS Debugging, AI Assistance, and Mobile Development.


  The Busymate DevTools catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Busymate DevTools'' developer surface includes CLI, changelog, support, pricing, getting-started guide, documentation, and 22 more developer resources.'
plans:
- name: Busymate Dev Plans Pricing
  plan_count: 4
  slug: busymate-dev-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Busymate DevTools API Rules
  rule_count: 45
  severity_counts:
    error: 39
    hint: 0
    info: 2
    warn: 4
  slug: busymate-dev-rules
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 31.4
    discoverability: 62.5
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Busymate Dev Domain Security
  slug: busymate-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Busymate Dev Vulnerability Disclosure
  slug: busymate-dev-vulnerability-disclosure
  summary_line: no policy recorded
slug: busymate-dev
tags:
- Developer Tools
- Network Monitoring
- HTTPS Debugging
- AI Assistance
- Mobile Development
website: https://busymate.dev/
---
