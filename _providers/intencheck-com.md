---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Intencheck Com Agentic Access
  operation_count: 21
  slug: intencheck-com-agentic-access
  summary_line: 21 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Analyze API from intencheck-com — 6 operation(s) for analyze.
  name: intencheck-com Analyze API
  slug: intencheck-com-analyze-api
- description: API Key Management for your integrations
  name: intencheck-com API Keys API
  slug: intencheck-com-api-keys-api
- description: The Checkout API from intencheck-com — 1 operation(s) for checkout.
  name: intencheck-com Checkout API
  slug: intencheck-com-checkout-api
- description: The Demo API from intencheck-com — 2 operation(s) for demo.
  name: intencheck-com Demo API
  slug: intencheck-com-demo-api
- description: The docs API from intencheck-com — 1 operation(s) for docs.
  name: intencheck-com Docs API
  slug: intencheck-com-docs-api
- description: The Mcp API from intencheck-com — 1 operation(s) for mcp.
  name: intencheck-com MCP API
  slug: intencheck-com-mcp-api
- description: The Reply API from intencheck-com — 1 operation(s) for reply.
  name: intencheck-com Reply API
  slug: intencheck-com-reply-api
- description: The Report Error API from intencheck-com — 1 operation(s) for report error.
  name: intencheck-com Report Error API
  slug: intencheck-com-report-error-api
- description: The Transactions API from intencheck-com — 1 operation(s) for transactions.
  name: intencheck-com Transactions API
  slug: intencheck-com-transactions-api
- description: The Webhooks API from intencheck-com — 1 operation(s) for webhooks.
  name: intencheck-com Webhooks API
  slug: intencheck-com-webhooks-api
artifact_total: 26
common:
- group: other
  href: https://artifacts.apis.io/intencheck-com/vendors/intencheck-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/intencheck-com-vendors.yml
- group: agent
  href: https://artifacts.apis.io/intencheck-com/agentic-access/intencheck-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/intencheck-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/intencheck-com/rules/intencheck-com-rules.yml
  title: ''
  type: Spectral
  url: rules/intencheck-com-rules.yml
- group: design
  href: https://artifacts.apis.io/intencheck-com/json-ld/intencheck-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/intencheck-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/intencheck-com/vocabulary/intencheck-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/intencheck-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/intencheck-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/intencheck-com/data-model/intencheck-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/intencheck-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/intencheck-com/errors/intencheck-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/intencheck-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/intencheck-com/conformance/intencheck-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/intencheck-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/intencheck-com/mcp/intencheck-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/intencheck-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/intencheck-com/hosts/intencheck-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intencheck-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://intencheck.com/api/v1/oauth/login/google
- group: docs
  title: ''
  type: Documentation
  url: https://docs.github.com
- group: auth
  href: https://artifacts.apis.io/intencheck-com/authentication/intencheck-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/intencheck-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/intencheck-com/security/intencheck-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intencheck-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://intencheck.com/
- group: docs
  title: ''
  type: APIReference
  url: https://intencheck.com/docs
- group: company
  title: ''
  type: Blog
  url: https://blog.intencheck.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://intencheck.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Reload
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://intencheck.com/openapi.json
  - status: 401
    url: https://intencheck.com/mcp
  - status: 200
    url: https://intencheck.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: IntenCheck provides a comprehensive suite of Deep NLP text analysis endpoints that detect meta-programs, emotions, moods, and communication styles. It supports multiple input and output languages natively. The API offers endpoints for analyzing text, extracting sentiment, and more, enabling developers to integrate advanced language understanding into applications.
json_schemas:
- name: AnalyzeRequest
  property_count: 3
  slug: intencheck-com-analyze-request
- name: ApiKeyOut
  property_count: 10
  slug: intencheck-com-api-key-out
- name: BatchJobOut
  property_count: 8
  slug: intencheck-com-batch-job-out
- name: BulkAnalyzeRequest
  property_count: 3
  slug: intencheck-com-bulk-analyze-request
- name: McpStatusResponse
  property_count: 7
  slug: intencheck-com-mcp-status-response
- name: ReplyRequest
  property_count: 7
  slug: intencheck-com-reply-request
jsonld:
- class_count: 31
  name: Intencheck Com Context
  property_count: 111
  slug: intencheck-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at intencheck.com.
  name: intencheck-com MCP Server
  slug: intencheck-com-mcp-yml
modified: '2026-10-30'
name: intencheck-com
nav: Providers
network: true
overview: 'intencheck-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analyze API, API Keys API, Checkout API, and 7 more. Tagged areas include Artificial Intelligence, Natural Language Processing, Text Analysis, Sentiment, and Emotion.


  The intencheck-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  intencheck-com''s developer surface includes documentation, authentication, API reference, engineering blog, getting-started guide, and 15 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: intencheck-com API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 2
  slug: intencheck-com-rules
scopes:
- name: Intencheck Com Scopes
  scope_count: 0
  slug: intencheck-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 54.9
    developer_ergonomics: 33.8
    discoverability: 53.3
    operational_transparency: 2.6
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/intencheck-com/intencheck-com-2026-11-03T133925.png
security:
- kind: authentication
  name: Intencheck Com Authentication
  slug: intencheck-com-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Intencheck Com Domain Security
  slug: intencheck-com-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: analyze
  slug: intencheck-com-analyze
- name: api-keys
  slug: intencheck-com-api-keys
- name: reply
  slug: intencheck-com-reply
slug: intencheck-com
tags:
- Artificial Intelligence
- Natural Language Processing
- Text Analysis
- Sentiment
- Emotion
website: https://intencheck.com/
---
