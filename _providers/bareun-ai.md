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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Bareun AI spell‑checking and grammar‑checking service. Documentation at https://bareun.ai/docs. No public machine‑readable contract found.
  name: Bareun AI API
  slug: bareun-ai-api-2
- baseURL: https://api.bareun.ai
  baseurl_source: declared
  description: 'Bareun AI API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Bareun AI API
  slug: bareun-ai-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/bareun-ai/rules/bareun-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bareun-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bareun-ai/json-ld/bareun-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bareun-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/bareun-ai/vocabulary/bareun-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bareun-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bareun-ai/data-model/bareun-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bareun-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/bareun-ai/conformance/bareun-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bareun-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bareun-ai/llms/bareun-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bareun-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/bareun-ai/mcp/bareun-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bareun-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bareun-ai/well-known/bareun-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bareun-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bareun-ai/hosts/bareun-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bareun-ai-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://api.bareun.ai/support/
- group: auth
  href: https://artifacts.apis.io/bareun-ai/security/bareun-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bareun-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bareun.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://bareun.ai/docs
- group: operate
  title: ''
  type: FAQ
  url: https://bareun.ai/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bareun.ai/privacy
- group: other
  title: ''
  type: RefundPolicy
  url: https://bareun.ai/refund-policy
coverage:
  checked: '2026-11-02'
  detail: Documentation exists but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract could be found.
  evidence:
  - status: 200
    url: https://bareun.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bareun AI provides a free AI‑powered Korean spell‑checking and grammar‑checking service. It corrects spelling, spacing, and grammar errors in real time, supports long documents such as cover letters and reports without splitting them, and explains each correction with underlying Korean orthography rules. The platform offers a custom dictionary and an API for team integration, with no sign‑up required for trial use. It also supplies documentation, FAQs, privacy policy, and refund policy pages.
image: https://bareun.ai/static/images/og-default.png
json_schemas:
- name: PostBareunApiV1AnalyzeListRequest
  property_count: 3
  slug: bareun-ai-post-bareun-api-v1-analyze-list-request
- name: PostBareunApiV1AnalyzeRequest
  property_count: 3
  slug: bareun-ai-post-bareun-api-v1-analyze-request
- name: PostBareunApiV1CorrectErrorRequest
  property_count: 3
  slug: bareun-ai-post-bareun-api-v1-correct-error-request
- name: PostBareunDictsearchserviceSearchdictRequest
  property_count: 6
  slug: bareun-ai-post-bareun-dictsearchservice-searchdict-request
- name: PostBareunLanguageserviceAnalyzesyntaxRequest
  property_count: 3
  slug: bareun-ai-post-bareun-languageservice-analyzesyntax-request
- name: PostBareunLanguageserviceAnalyzesyntaxlistRequest
  property_count: 3
  slug: bareun-ai-post-bareun-languageservice-analyzesyntaxlist-request
jsonld:
- class_count: 14
  name: Bareun Ai Context
  property_count: 12
  slug: bareun-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.bareun.ai:443 requiring an API key.
  name: Bareun AI MCP Server
  slug: bareun-ai-mcp-yml
modified: '2026-11-02'
name: Bareun AI
nav: Providers
network: true
overview: 'Bareun AI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Korean, Spellchecking, Grammar, Artificial Intelligence, and Language Tools.


  The Bareun AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bareun AI''s developer surface includes support, documentation, FAQ, and 13 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Bareun AI API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: bareun-ai-rules
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 7.1
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bareun Ai Domain Security
  slug: bareun-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bareun-ai
tags:
- Korean
- Spellchecking
- Grammar
- Artificial Intelligence
- Language Tools
- Company
website: https://bareun.ai/
---
