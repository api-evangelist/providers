---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Supported automation paths, hosted MCP API-key and OAuth authentication, and the exact routes exposed by the optional local HTTP gateway.
  name: ContextStream API
  slug: contextstream-api
- baseURL: https://api.contextstream.io
  baseurl_source: declared
  description: 'contextstream-io API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: contextstream-io API
  slug: contextstream-io-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/contextstream-io/rules/contextstream-io-rules.yml
  title: ''
  type: Spectral
  url: rules/contextstream-io-rules.yml
- group: design
  href: https://artifacts.apis.io/contextstream-io/json-ld/contextstream-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/contextstream-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/contextstream-io/vocabulary/contextstream-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contextstream-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/contextstream-io/data-model/contextstream-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/contextstream-io-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://contextstream.io/trust
- group: design
  href: https://artifacts.apis.io/contextstream-io/conformance/contextstream-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contextstream-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contextstream-io/llms/contextstream-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextstream-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/contextstream-io/well-known/contextstream-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contextstream-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/contextstream-io/hosts/contextstream-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextstream-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/contextstream-io/vendors/contextstream-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contextstream-io-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.contextstream.io/
- group: auth
  title: ''
  type: Security
  url: https://contextstream.io/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://contextstream.io/changelog
- group: auth
  href: https://artifacts.apis.io/contextstream-io/security/contextstream-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/contextstream-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/contextstream-io/security/contextstream-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/contextstream-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/contextstream-io/security/contextstream-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextstream-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contextstream.io/
- group: docs
  title: ''
  type: Documentation
  url: https://contextstream.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://contextstream.io/quickstart
- group: operate
  title: ''
  type: Support
  url: https://contextstream.io/contact
- group: company
  title: ''
  type: Blog
  url: https://contextstream.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contextstream
- group: commercial
  title: ''
  type: Pricing
  url: https://contextstream.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contextstream.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contextstream.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://contextstream.io/signup
- group: start
  title: ''
  type: Login
  url: https://contextstream.io/login
coverage:
  checked: '2026-10-30'
  detail: Docs are rendered via JavaScript and no machine‑readable OpenAPI/GraphQL/AsyncAPI spec was found.
  evidence:
  - status: 200
    url: https://contextstream.io/docs/platform/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: ContextStream is a platform that captures and preserves the reasoning, decisions, and context behind software development work, enabling AI agents and humans to access shared knowledge. Founded in 2024 by Erik Scott, it offers tools for indexing code, storing project decisions, and providing contextual prompts, aiming to reduce knowledge loss and improve productivity for developers, teams, and AI agents.
image: https://contextstream.io/opengraph-image
json_schemas:
- name: GetApiV1ProjectsResponse
  property_count: 6
  slug: contextstream-io-get-api-v1-projects-response
- name: GetApiV1WorkspacesResponse
  property_count: 6
  slug: contextstream-io-get-api-v1-workspaces-response
- name: GetCsInstallShResponse
  property_count: 1
  slug: contextstream-io-get-cs-install-sh-response
- name: GetScriptsMcpShResponse
  property_count: 1
  slug: contextstream-io-get-scripts-mcp-sh-response
jsonld:
- class_count: 4
  name: stream Io Context
  property_count: 7
  slug: contextstream-io-context
layout: provider
modified: '2026-10-29'
name: contextstream-io
nav: Providers
network: true
overview: 'contextstream-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Context Management, Collaboration, Knowledge Base, and Productivity.


  The contextstream-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  contextstream-io''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: contextstream-io API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: contextstream-io-rules
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 51.0
    catalog_earned_first_party: 0.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.1
  facets:
    access_clarity: 34.2
    contract_governance: 19.7
    contract_quality: 20.2
    developer_ergonomics: 14.3
    discoverability: 64.3
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 39.8
  provenance:
    conformance: derived
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
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/contextstream-io/contextstream-io-2026-11-03T125207.png
security:
- kind: domain-security
  name: Contextstream Io Domain Security
  slug: contextstream-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Contextstream Io Vulnerability Disclosure
  slug: contextstream-io-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Contextstream Io Trust Center
  slug: contextstream-io-trust-center
  summary_line: SOC 2, HIPAA, FedRAMP, GDPR
slug: contextstream-io
tags:
- Artificial Intelligence
- Context Management
- Collaboration
- Knowledge Base
- Productivity
website: https://contextstream.io/
---
