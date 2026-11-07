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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 65.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Valjeanspecialty Agentic Access
  operation_count: 32
  slug: valjeanspecialty-agentic-access
  summary_line: 32 operations · 15 acting
api_count: 1
apis:
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: Check a key and what it can do.
  name: Valjean Specialty Account API
  slug: valjeanspecialty-account-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: Answer what's needed, once for every market.
  name: Valjean Specialty Answers API
  slug: valjeanspecialty-answers-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: Will Valjean likely be able to place a risk.
  name: Valjean Specialty Appetite API
  slug: valjeanspecialty-appetite-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: Your written instruction to bind, and its progress.
  name: Valjean Specialty Bind API
  slug: valjeanspecialty-bind-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: Upload and download documents.
  name: Valjean Specialty Documents API
  slug: valjeanspecialty-documents-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: A cursor feed of everything that changed.
  name: Valjean Specialty Events API
  slug: valjeanspecialty-events-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: Ask markets connected by API for instant quotes.
  name: Valjean Specialty Instant quotes API
  slug: valjeanspecialty-instant-quotes-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: Invoices sent to your agency.
  name: Valjean Specialty Invoices API
  slug: valjeanspecialty-invoices-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: Policies placed through Valjean.
  name: Valjean Specialty Policies API
  slug: valjeanspecialty-policies-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: 'No key needed: the website''s appetite check and class guides.'
  name: Valjean Specialty Public API
  slug: valjeanspecialty-public-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: Quotes your broker has presented.
  name: Valjean Specialty Quotes API
  slug: valjeanspecialty-quotes-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: What a class of risk needs, before a file exists.
  name: Valjean Specialty Requirements API
  slug: valjeanspecialty-requirements-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: Send files and follow them.
  name: Valjean Specialty Submissions API
  slug: valjeanspecialty-submissions-api
- baseURL: https://api.valjeanspecialty.com/api/agent/v1
  baseurl_source: declared
  description: Signed pushes of the same events.
  name: Valjean Specialty Webhooks API
  slug: valjeanspecialty-webhooks-api
artifact_total: 33
asyncapis:
- description: Events about your agency's files, POSTed to each webhook you register (POST /webhooks in the agent API). Reply 2xx within 8 seconds. Failures retry after 1, 5, 30, 120, 360, 720 and 1440 minutes; a we
  name: Valjean Specialty webhooks
  slug: valjeanspecialty-asyncapi
- description: ''
  name: Valjeanspecialty Webhooks
  slug: valjeanspecialty-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/valjeanspecialty/agentic-access/valjeanspecialty-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/valjeanspecialty-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/valjeanspecialty/rules/valjeanspecialty-rules.yml
  title: ''
  type: Spectral
  url: rules/valjeanspecialty-rules.yml
- group: design
  href: https://artifacts.apis.io/valjeanspecialty/json-ld/valjeanspecialty-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/valjeanspecialty-context.jsonld
- group: design
  href: https://artifacts.apis.io/valjeanspecialty/vocabulary/valjeanspecialty-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/valjeanspecialty-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/valjeanspecialty/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/valjeanspecialty/asyncapi/valjeanspecialty-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/valjeanspecialty-webhooks.yml
- group: docs
  href: https://artifacts.apis.io/valjeanspecialty/asyncapi/valjeanspecialty-asyncapi.yaml
  title: ''
  type: AsyncAPI
  url: asyncapi/valjeanspecialty-asyncapi.yaml
- group: design
  href: https://artifacts.apis.io/valjeanspecialty/data-model/valjeanspecialty-data-model.yml
  title: ''
  type: DataModel
  url: data-model/valjeanspecialty-data-model.yml
- group: build
  href: https://artifacts.apis.io/valjeanspecialty/cli/valjeanspecialty-cli.yml
  title: ''
  type: CLI
  url: cli/valjeanspecialty-cli.yml
- group: design
  href: https://artifacts.apis.io/valjeanspecialty/conventions/valjeanspecialty-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/valjeanspecialty-conventions.yml
- group: design
  href: https://artifacts.apis.io/valjeanspecialty/conventions/valjeanspecialty-conventions.yml
  title: ''
  type: Conventions
  url: conventions/valjeanspecialty-conventions.yml
- group: auth
  href: https://artifacts.apis.io/valjeanspecialty/authentication/valjeanspecialty-authentication.yml
  title: ''
  type: Authentication
  url: authentication/valjeanspecialty-authentication.yml
- group: design
  href: https://artifacts.apis.io/valjeanspecialty/errors/valjeanspecialty-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/valjeanspecialty-problem-types.yml
- group: design
  href: https://artifacts.apis.io/valjeanspecialty/conformance/valjeanspecialty-conformance.yml
  title: ''
  type: Conformance
  url: conformance/valjeanspecialty-conformance.yml
- group: agent
  href: https://artifacts.apis.io/valjeanspecialty/llms/valjeanspecialty-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/valjeanspecialty-llms.txt
- group: agent
  href: https://artifacts.apis.io/valjeanspecialty/mcp/valjeanspecialty-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/valjeanspecialty-mcp.yml
- group: agent
  href: https://artifacts.apis.io/valjeanspecialty/well-known/valjeanspecialty-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/valjeanspecialty-well-known.yml
- group: other
  href: https://artifacts.apis.io/valjeanspecialty/hosts/valjeanspecialty-hosts.yml
  title: ''
  type: Hosts
  url: hosts/valjeanspecialty-hosts.yml
- group: other
  href: https://artifacts.apis.io/valjeanspecialty/vendors/valjeanspecialty-vendors.yml
  title: ''
  type: Vendors
  url: vendors/valjeanspecialty-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.valjeanspecialty.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.valjeanspecialty.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.valjeanspecialty.com/guides/quickstart/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.valjeanspecialty.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/valjeanspecialty/scopes/valjeanspecialty-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/valjeanspecialty-scopes.yml
- group: auth
  href: https://artifacts.apis.io/valjeanspecialty/security/valjeanspecialty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/valjeanspecialty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://valjeanspecialty.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.valjeanspecialty.com
created: '2026-11-03'
description: Valjean Specialty is a wholesale insurance broker serving licensed retail agents with excess and surplus (E&S) property and casualty coverage. They specialize in hard‑to‑place risks, offering a range of lines such as general liability, commercial property, excess‑umbrella, and commercial auto. Their platform provides agents with tools to quote, bind, and manage policies, backed by a dedicated team focused on tailored risk solutions for the insurance market.
json_schemas:
- name: AnswerResult
  property_count: 9
  slug: valjeanspecialty-answer-result
- name: AppetiteAnswer
  property_count: 12
  slug: valjeanspecialty-appetite-answer
- name: DryRun
  property_count: 4
  slug: valjeanspecialty-dry-run
- name: Guide
  property_count: 11
  slug: valjeanspecialty-guide
- name: Submission
  property_count: 14
  slug: valjeanspecialty-submission
- name: UnderwriterFlags
  property_count: 3
  slug: valjeanspecialty-underwriter-flags
jsonld:
- class_count: 42
  name: Valjeanspecialty Context
  property_count: 127
  slug: valjeanspecialty-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.valjeansspecialty.com requiring an API key.
  name: Valjean Specialty MCP Server
  slug: valjeanspecialty-mcp-yml
modified: '2026-11-03'
name: Valjean Specialty
nav: Providers
network: true
overview: 'Valjean Specialty publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Answers API, Appetite API, and 11 more. Tagged areas include Insurance, Wholesale, Brokerage, E&S, and Insurance Tech.


  The Valjean Specialty catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Valjean Specialty''s developer surface includes CLI, authentication, getting-started guide, API reference, documentation, and 22 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 122
  extends:
  - spectral:oas
  name: Valjean Specialty API Rules
  rule_count: 81
  severity_counts:
    error: 71
    hint: 0
    info: 4
    warn: 6
  slug: valjeanspecialty-rules
scopes:
- name: Valjeanspecialty Scopes
  scope_count: 2
  slug: valjeanspecialty-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 75.0
    developer_ergonomics: 35.1
    discoverability: 61.7
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 33.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Valjeanspecialty Authentication
  slug: valjeanspecialty-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Valjeanspecialty Domain Security
  slug: valjeanspecialty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: valjeanspecialty-bind-quote
  slug: valjeanspecialty-bind-quote
- name: valjeanspecialty-create-and-send-submission
  slug: valjeanspecialty-create-and-send-submission
- name: valjeanspecialty-manage-webhooks
  slug: valjeanspecialty-manage-webhooks
- name: valjeanspecialty-upload-document
  slug: valjeanspecialty-upload-document
slug: valjeanspecialty
tags:
- Insurance
- Wholesale
- Brokerage
- E&S
- Insurance Tech
website: https://valjeanspecialty.com
---
