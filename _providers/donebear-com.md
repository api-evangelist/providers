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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
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
  score: 43.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Done Bear task‑management platform
  name: Done Bear API
  slug: done-bear-api
- baseURL: https://api.donebear.com
  baseurl_source: declared
  description: Done Bear is a local-first GTD task manager.
  name: Done Bear API API
  slug: done-bear-api-api
artifact_total: 16
asyncapis:
- description: ''
  name: Donebear Com Webhooks
  slug: donebear-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/donebear-com/rules/donebear-com-rules.yml
  title: ''
  type: Spectral
  url: rules/donebear-com-rules.yml
- group: design
  href: https://artifacts.apis.io/donebear-com/json-ld/donebear-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/donebear-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/donebear-com/vocabulary/donebear-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/donebear-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/donebear-com/conformance/donebear-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/donebear-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/donebear-com/plans/donebear-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/donebear-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/donebear-com/asyncapi/donebear-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/donebear-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/donebear-com/data-model/donebear-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/donebear-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/donebear-com/cli/donebear-com-cli.yml
  title: ''
  type: CLI
  url: cli/donebear-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/donebear-com/changelog/donebear-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/donebear-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/donebear-com/authentication/donebear-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/donebear-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/donebear-com/lifecycle/donebear-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/donebear-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/donebear-com/lifecycle/donebear-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/donebear-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/donebear-com/errors/donebear-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/donebear-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/donebear-com/llms/donebear-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/donebear-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/donebear-com/mcp/donebear-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/donebear-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/donebear-com/well-known/donebear-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/donebear-com-security.txt
- group: agent
  href: https://artifacts.apis.io/donebear-com/well-known/donebear-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/donebear-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/donebear-com/hosts/donebear-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/donebear-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/donebear-com/vendors/donebear-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/donebear-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/donebear-com/packages/donebear-com-packages.yml
  title: ''
  type: SDKs
  url: packages/donebear-com-packages.yml
- group: build
  href: https://artifacts.apis.io/donebear-com/packages/donebear-com-packages.yml
  title: ''
  type: Packages
  url: packages/donebear-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://donebear.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://donebear.com/status
- group: auth
  title: ''
  type: Security
  url: https://donebear.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://donebear.com/privacy
- group: start
  title: ''
  type: Login
  url: https://donebear.com/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://donebear.com/whats-new
- group: company
  title: ''
  type: Blog
  url: https://donebear.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://donebear.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://donebear.com/docs/help/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.donebear.com/
- group: docs
  title: ''
  type: APIReference
  url: https://donebear.com/developers
- group: auth
  href: https://artifacts.apis.io/donebear-com/security/donebear-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/donebear-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/donebear-com/security/donebear-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/donebear-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://donebear.com/
created: '2026-11-05'
description: Done Bear is a cross‑platform task‑management app that lets users keep a single to‑do list across Windows, macOS, Linux, iPhone and the web. It combines inbox processing, GTD principles and a simple, local‑first design to help organise daily work and long‑term goals.
image: https://donebear.com/opengraph-image?a37187da5e618253
json_schemas:
- name: AgentSignupComplete
  property_count: 7
  slug: donebear-com-agent-signup-complete
- name: AgentSignupPending
  property_count: 7
  slug: donebear-com-agent-signup-pending
- name: AgentSignupStartRequest
  property_count: 2
  slug: donebear-com-agent-signup-start-request
- name: WebhookDelivery
  property_count: 14
  slug: donebear-com-webhook-delivery
- name: WebhookEndpointCreate
  property_count: 4
  slug: donebear-com-webhook-endpoint-create
- name: WebhookEndpoint
  property_count: 11
  slug: donebear-com-webhook-endpoint
jsonld:
- class_count: 19
  name: Donebear Com Context
  property_count: 51
  slug: donebear-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.donebear.com requiring OAuth.
  name: Done Bear MCP Server
  slug: donebear-com-mcp-yml
modified: '2026-11-05'
name: Done Bear
nav: Providers
network: true
overview: 'Done Bear publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Task Management, Productivity, Cross-Platform, To-Do, and Local-First.


  The Done Bear catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Done Bear''s developer surface includes CLI, changelog, authentication, engineering blog, pricing, getting-started guide, documentation, and 28 more developer resources.'
plans:
- name: Donebear Com Plans Pricing
  plan_count: 4
  slug: donebear-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: Done Bear API Rules
  rule_count: 69
  severity_counts:
    error: 62
    hint: 0
    info: 2
    warn: 5
  slug: donebear-com-rules
score:
  band: strong
  composite: 61.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 57.1
    discoverability: 65.0
    operational_transparency: 57.9
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Donebear Com Authentication
  slug: donebear-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Donebear Com Domain Security
  slug: donebear-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Donebear Com Vulnerability Disclosure
  slug: donebear-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: donebear-com
tags:
- Task Management
- Productivity
- Cross-Platform
- To-Do
- Local-First
website: https://donebear.com/
---
