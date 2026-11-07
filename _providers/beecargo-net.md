---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Beecargo Net Agentic Access
  operation_count: 31
  slug: beecargo-net-agentic-access
  summary_line: 31 operations · 20 acting
api_count: 1
apis:
- baseURL: https://api.beecargo.net
  baseurl_source: declared
  description: The Agent API from Beecargo — 3 operation(s) for agent.
  name: Beecargo Agent API
  slug: beecargo-net-agent-api
- baseURL: https://api.beecargo.net
  baseurl_source: declared
  description: The Connect API from Beecargo — 1 operation(s) for connect.
  name: Beecargo Connect API
  slug: beecargo-net-connect-api
- baseURL: https://api.beecargo.net
  baseurl_source: declared
  description: The Downloads API from Beecargo — 1 operation(s) for downloads.
  name: Beecargo Downloads API
  slug: beecargo-net-downloads-api
- baseURL: https://api.beecargo.net
  baseurl_source: declared
  description: The Files API from Beecargo — 23 operation(s) for files.
  name: Beecargo Files API
  slug: beecargo-net-files-api
- baseURL: https://api.beecargo.net
  baseurl_source: declared
  description: The Folders API from Beecargo — 2 operation(s) for folders.
  name: Beecargo Folders API
  slug: beecargo-net-folders-api
- baseURL: https://api.beecargo.net
  baseurl_source: declared
  description: The System API from Beecargo — 1 operation(s) for system.
  name: Beecargo System API
  slug: beecargo-net-system-api
artifact_total: 21
asyncapis:
- description: ''
  name: Beecargo Net Webhooks
  slug: beecargo-net-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/beecargo-net/agentic-access/beecargo-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/beecargo-net-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/beecargo-net/plans/beecargo-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beecargo-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/beecargo-net/rules/beecargo-net-rules.yml
  title: ''
  type: Spectral
  url: rules/beecargo-net-rules.yml
- group: design
  href: https://artifacts.apis.io/beecargo-net/json-ld/beecargo-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/beecargo-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/beecargo-net/vocabulary/beecargo-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/beecargo-net-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/beecargo-net/asyncapi/beecargo-net-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/beecargo-net-webhooks.yml
- group: design
  href: https://artifacts.apis.io/beecargo-net/data-model/beecargo-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beecargo-net-data-model.yml
- group: design
  href: https://artifacts.apis.io/beecargo-net/conventions/beecargo-net-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/beecargo-net-conventions.yml
- group: design
  href: https://artifacts.apis.io/beecargo-net/conventions/beecargo-net-conventions.yml
  title: ''
  type: Conventions
  url: conventions/beecargo-net-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://beecargo.net/docs/security
- group: auth
  href: https://artifacts.apis.io/beecargo-net/authentication/beecargo-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beecargo-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/beecargo-net/errors/beecargo-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beecargo-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/beecargo-net/conformance/beecargo-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beecargo-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/beecargo-net/llms/beecargo-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beecargo-net-llms.txt
- group: other
  href: https://artifacts.apis.io/beecargo-net/a2a/beecargo-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/beecargo-net-a2a.yml
- group: agent
  href: https://artifacts.apis.io/beecargo-net/mcp/beecargo-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/beecargo-net-mcp.yml
- group: auth
  href: https://artifacts.apis.io/beecargo-net/well-known/beecargo-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beecargo-net-security.txt
- group: auth
  href: https://artifacts.apis.io/beecargo-net/well-known/beecargo-net-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beecargo-net-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/beecargo-net/well-known/beecargo-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beecargo-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/beecargo-net/hosts/beecargo-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beecargo-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/beecargo-net/vendors/beecargo-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beecargo-net-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beecargo.net/docs/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beecargo.net/docs/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://beecargo.net/pricing
- group: company
  title: ''
  type: Blog
  url: https://beecargo.net/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://beecargo.net/agents/mcp-quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beecargo.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.beecargo.net\
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beecargo.net/llms.txt
- group: auth
  href: https://artifacts.apis.io/beecargo-net/security/beecargo-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/beecargo-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/beecargo-net/security/beecargo-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beecargo-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beecargo.net/
created: '2026-11-02'
description: Beecargo provides fast, secure file hosting with durable share links. Users can upload files via a web interface, REST API, MCP, or CLI, receiving lasting share links without requiring a dashboard login. The service emphasizes privacy, supports AI agents, and offers free starter usage, making file sharing simple and reliable for individuals and applications.
image: https://beecargo.net/og.png
json_schemas:
- name: AgentRegisterChallenge
  property_count: 3
  slug: beecargo-net-agent-register-challenge
- name: AgentRegisterResponse
  property_count: 6
  slug: beecargo-net-agent-register-response
- name: FileUploadRequest
  property_count: 14
  slug: beecargo-net-file-upload-request
- name: FileUploadResponse
  property_count: 2
  slug: beecargo-net-file-upload-response
- name: RemoteUploadRequest
  property_count: 14
  slug: beecargo-net-remote-upload-request
- name: ShareMetaResponse
  property_count: 10
  slug: beecargo-net-share-meta-response
jsonld:
- class_count: 11
  name: Beecargo Net Context
  property_count: 42
  slug: beecargo-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.beecargo.net.
  name: Beecargo MCP Server
  slug: beecargo-net-mcp-yml
modified: '2026-11-02'
name: Beecargo
nav: Providers
network: true
overview: 'Beecargo publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Connect API, Downloads API, and 3 more. Tagged areas include File Hosting, Share Links, Developers, and Agents.


  The Beecargo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Beecargo''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, API reference, and 26 more developer resources.'
plans:
- name: Beecargo Net Plans Pricing
  plan_count: 1
  slug: beecargo-net-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Beecargo API Rules
  rule_count: 45
  severity_counts:
    error: 42
    hint: 0
    info: 2
    warn: 1
  slug: beecargo-net-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 61.0
    developer_ergonomics: 32.1
    discoverability: 56.7
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
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
- kind: authentication
  name: Beecargo Net Authentication
  slug: beecargo-net-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Beecargo Net Domain Security
  slug: beecargo-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Beecargo Net Vulnerability Disclosure
  slug: beecargo-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: beecargo-net
tags:
- File Hosting
- Share Links
- Developers
- Agents
website: https://beecargo.net/
---
