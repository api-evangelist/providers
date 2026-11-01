---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.5
  scored_at: '2026-10-31'
api_count: 4
apis:
- description: REST API for Seekrit secret management.
  name: Seekrit API
  slug: seekrit-api
- baseURL: https://api.seekrit.dev
  baseurl_source: declared
  description: 'seekrit-dev docs API as documented publicly: 29 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: seekrit-dev docs API
  slug: docs-api
- baseURL: https://api.seekrit.dev
  baseurl_source: declared
  description: 'seekrit-dev guides API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: seekrit-dev guides API
  slug: guides-api
- baseURL: https://api.seekrit.dev
  baseurl_source: declared
  description: 'seekrit-dev reference API as documented publicly: 100 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: seekrit-dev reference API
  slug: reference-api
artifact_total: 28
common:
- group: design
  href: https://artifacts.apis.io/seekrit-dev/rules/seekrit-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/seekrit-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/seekrit-dev/json-ld/seekrit-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/seekrit-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/seekrit-dev/vocabulary/seekrit-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/seekrit-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/seekrit-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/seekrit-dev/data-model/seekrit-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/seekrit-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/seekrit-dev/cli/seekrit-dev-cli.yml
  title: ''
  type: CLI
  url: cli/seekrit-dev-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://seekrit.dev/trust
- group: auth
  title: ''
  type: Security
  url: https://seekrit.dev/trust#responsible-disclosure
- group: design
  href: https://artifacts.apis.io/seekrit-dev/conformance/seekrit-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/seekrit-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/seekrit-dev/llms/seekrit-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seekrit-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/seekrit-dev/mcp/seekrit-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/seekrit-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/seekrit-dev/well-known/seekrit-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/seekrit-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/seekrit-dev/well-known/seekrit-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/seekrit-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/seekrit-dev/hosts/seekrit-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seekrit-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/seekrit-dev/vendors/seekrit-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seekrit-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/seekrit-dev/packages/seekrit-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/seekrit-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/seekrit-dev/packages/seekrit-dev-packages.yml
  title: ''
  type: Packages
  url: packages/seekrit-dev-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.seekrit.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://seekrit.dev/docs/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://seekrit.dev/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/seekrit-dev/security/seekrit-dev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/seekrit-dev-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/seekrit-dev/security/seekrit-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/seekrit-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/seekrit-dev/security/seekrit-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seekrit-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seekrit.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://seekrit.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://seekrit.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://seekrit.dev/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seekrit.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seekrit.dev/privacy
coverage:
  checked: '2026-10-30'
  detail: The provider's documentation lists API endpoints but no public OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 401
    url: https://api.seekrit.dev/v1/openapi.json
  - status: 401
    url: https://api.seekrit.dev/v1/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Seekrit provides an end‑to‑end encrypted, multi‑tenant secrets management service built on Cloudflare Workers. It allows developers and organizations to store, retrieve, and rotate secrets such as API keys, passwords, and certificates without ever exposing the plaintext to the server. The platform offers client‑side encryption, zero‑knowledge architecture, fine‑grained access controls, and a simple HTTP API for programmatic secret management. Seekrit’s service is designed for modern cloud‑native applications, offering scalability, low latency, and compliance‑friendly data handling.
image: https://seekrit.dev/icon.svg
json_schemas:
- name: DeleteV1AgentsSessionsSessionIdRequest
  property_count: 2
  slug: seekrit-dev-delete-v1-agents-sessions-session-id-request
- name: GetSecretsResponse
  property_count: 1
  slug: seekrit-dev-get-secrets-response
- name: GetV1AgentsEnvironmentsEnvironmentidResponse
  property_count: 3
  slug: seekrit-dev-get-v1-agents-environments-environmentid-response
- name: GetV1ModelsResponse
  property_count: 1
  slug: seekrit-dev-get-v1-models-response
- name: GetV1SecretsResponse
  property_count: 1
  slug: seekrit-dev-get-v1-secrets-response
- name: PostSignupRequest
  property_count: 2
  slug: seekrit-dev-post-signup-request
- name: PostSyncBindingsRequest
  property_count: 10
  slug: seekrit-dev-post-sync-bindings-request
- name: PostV1AgentsAutomationsRequest
  property_count: 5
  slug: seekrit-dev-post-v1-agents-automations-request
- name: PostV1AgentsEnvironmentsRequest
  property_count: 1
  slug: seekrit-dev-post-v1-agents-environments-request
- name: PostV1AgentsSessionsRequest
  property_count: 3
  slug: seekrit-dev-post-v1-agents-sessions-request
- name: PostV1AgentsSessionsSessionIdEventsRequest
  property_count: 1
  slug: seekrit-dev-post-v1-agents-sessions-session-id-events-request
- name: PostV1CliLoginPollResponse
  property_count: 4
  slug: seekrit-dev-post-v1-cli-login-poll-response
- name: PostV1CliLoginRequest
  property_count: 4
  slug: seekrit-dev-post-v1-cli-login-request
- name: PostV1CliLoginResponse
  property_count: 4
  slug: seekrit-dev-post-v1-cli-login-response
- name: PostV1ConnectionsIdRevokeRequest
  property_count: 1
  slug: seekrit-dev-post-v1-connections-id-revoke-request
- name: PostV1OrgsOrgidEnvsEnvidBranchesRequest
  property_count: 6
  slug: seekrit-dev-post-v1-orgs-orgid-envs-envid-branches-request
- name: PostV1OrgsOrgidKmsKeysRequest
  property_count: 7
  slug: seekrit-dev-post-v1-orgs-orgid-kms-keys-request
- name: PutV1OrgsRequest
  property_count: 3
  slug: seekrit-dev-put-v1-orgs-request
jsonld:
- class_count: 112
  name: Seekrit Dev Context
  property_count: 123
  slug: seekrit-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.seekrit.dev requiring an API key.
  name: seekrit-dev MCP Server
  slug: seekrit-dev-mcp-yml
modified: '2026-10-30'
name: seekrit-dev
nav: Providers
network: true
overview: 'seekrit-dev is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including docs API, guides API, reference API, and 1 more. Tagged areas include Company, Security, Secrets Management, Encryption, and Cloudflare.


  The seekrit-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  seekrit-dev''s developer surface includes CLI, API reference, getting-started guide, documentation, pricing, engineering blog, and 23 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: seekrit-dev API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: seekrit-dev-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 24.5
    developer_ergonomics: 51.7
    discoverability: 70.0
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 29
      marker_coverage: 100.0
      total: 29
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Seekrit Dev Domain Security
  slug: seekrit-dev-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Seekrit Dev Vulnerability Disclosure
  slug: seekrit-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Seekrit Dev Trust Center
  slug: seekrit-dev-trust-center
  summary_line: SOC 2, ISO 27001
slug: seekrit-dev
tags:
- Company
- Security
- Secrets Management
- Encryption
- Cloudflare
website: https://seekrit.dev/
---
