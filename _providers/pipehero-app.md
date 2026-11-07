---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://myapp.t.pipehero.app
  baseurl_source: declared
  description: The Mcp API from pipehero-app — 1 operation(s) for mcp.
  name: pipehero-app MCP API
  slug: pipehero-app-mcp-api
- baseURL: https://myapp.t.pipehero.app
  baseurl_source: declared
  description: The Slack API from pipehero-app — 1 operation(s) for slack.
  name: pipehero-app Slack API
  slug: pipehero-app-slack-api
- baseURL: https://myapp.t.pipehero.app
  baseurl_source: declared
  description: The Webhooks API from pipehero-app — 10 operation(s) for webhooks.
  name: pipehero-app Webhooks API
  slug: pipehero-app-webhooks-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/pipehero-app/rules/pipehero-app-rules.yml
  title: ''
  type: Spectral
  url: rules/pipehero-app-rules.yml
- group: design
  href: https://artifacts.apis.io/pipehero-app/vocabulary/pipehero-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pipehero-app-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/pipehero-app/cli/pipehero-app-cli.yml
  title: ''
  type: CLI
  url: cli/pipehero-app-cli.yml
- group: auth
  href: https://artifacts.apis.io/pipehero-app/authentication/pipehero-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pipehero-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/pipehero-app/conformance/pipehero-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pipehero-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pipehero-app/llms/pipehero-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pipehero-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/pipehero-app/mcp/pipehero-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pipehero-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pipehero-app/well-known/pipehero-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pipehero-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/pipehero-app/hosts/pipehero-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pipehero-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/pipehero-app/vendors/pipehero-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pipehero-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/pipehero-app/packages/pipehero-app-packages.yml
  title: ''
  type: SDKs
  url: packages/pipehero-app-packages.yml
- group: build
  href: https://artifacts.apis.io/pipehero-app/packages/pipehero-app-packages.yml
  title: ''
  type: Packages
  url: packages/pipehero-app-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pipehero.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pipehero.app/privacy
- group: auth
  href: https://artifacts.apis.io/pipehero-app/security/pipehero-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pipehero-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pipehero.app/
- group: docs
  title: ''
  type: Documentation
  url: https://pipehero.app/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://pipehero.app/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://pipehero.app/#pricing
- group: docs
  title: ''
  type: APIReference
  url: https://pipehero.app/docs/apis
created: '2026-10-30'
description: Pipehero provides webhook tunneling, real-time inspection, replay, signature verification, and an AI-powered MCP server that can read and replay webhooks, expose local services to cloud AI clients, and offer a full API workspace for developers to document, test, and monitor APIs using real traffic, all via a secure HTTPS tunnel and a developer-friendly interface.
image: https://pipehero.app/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.pipehero.app.
  name: pipehero-app MCP Server
  slug: pipehero-app-mcp-yml
modified: '2026-10-30'
name: pipehero-app
nav: Providers
network: true
overview: 'pipehero-app is listed with 3 APIs on the [APIs.io](https://apis.io/) network: MCP API, Slack API, and Webhooks API. Tagged areas include Webhook, API Workspace, Developer Tools, MCP, and Integration.


  The pipehero-app catalog on APIs.io includes 1 Spectral governance ruleset.


  pipehero-app''s developer surface includes CLI, authentication, documentation, getting-started guide, pricing, API reference, and 14 more developer resources.'
plans:
- name: Pipehero App Plans Pricing
  plan_count: 0
  slug: pipehero-app-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Pipehero App Rate Limits
  slug: pipehero-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: pipehero-app API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: pipehero-app-rules
scopes:
- name: Pipehero App Scopes
  scope_count: 0
  slug: pipehero-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 45.0
    catalog_earned_first_party: 0.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 15.8
    contract_governance: 19.7
    contract_quality: 10.7
    developer_ergonomics: 40.5
    discoverability: 70.0
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pipehero-app/pipehero-app-2026-11-03T141240.png
security:
- kind: authentication
  name: Pipehero App Authentication
  slug: pipehero-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pipehero App Domain Security
  slug: pipehero-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: pipehero-app
tags:
- Webhook
- API Workspace
- Developer Tools
- MCP
- Integration
website: https://pipehero.app/
---
