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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.crowelogic.com
  baseurl_source: declared
  description: 'Crowe Logic API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Crowe Logic API
  slug: crowelogic-com-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/crowelogic-com/rules/crowelogic-com-rules.yml
  title: ''
  type: Spectral
  url: rules/crowelogic-com-rules.yml
- group: design
  href: https://artifacts.apis.io/crowelogic-com/json-ld/crowelogic-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crowelogic-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/crowelogic-com/vocabulary/crowelogic-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crowelogic-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/crowelogic-com/data-model/crowelogic-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crowelogic-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/crowelogic-com/conformance/crowelogic-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crowelogic-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crowelogic-com/mcp/crowelogic-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crowelogic-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/crowelogic-com/hosts/crowelogic-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowelogic-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/crowelogic-com/vendors/crowelogic-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crowelogic-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/MichaelCrowe11/crowe-logic-desktop/releases
- group: auth
  href: https://artifacts.apis.io/crowelogic-com/security/crowelogic-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowelogic-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crowelogic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://crowelogic.com/foundry/
- group: commercial
  title: ''
  type: Pricing
  url: https://crowelogic.com/foundry/#pricing
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://crowelogic.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: 'Crowe Logic is a coding agent for your repositories, in the terminal and on the desktop. You set the operating mode, review every diff before it lands, and see the engine behind every model tier by name. Free tier: CroweLM Flash, 20 turns a day, no card and no keys. The platform offers 750 credits and various flagship turns, providing flexible AI assistance for code tasks.'
image: https://crowelogic.com/foundry/brand/og-image.png
json_schemas:
- name: GetHealthzResponse
  property_count: 2
  slug: crowelogic-com-get-healthz-response
- name: PostMcpRequest
  property_count: 4
  slug: crowelogic-com-post-mcp-request
- name: PostV1ChatCompletionsRequest
  property_count: 2
  slug: crowelogic-com-post-v1-chat-completions-request
jsonld:
- class_count: 3
  name: Crowelogic Com Context
  property_count: 8
  slug: crowelogic-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.crowelogic.com requiring an API key.
  name: Crowe Logic MCP Server
  slug: crowelogic-com-mcp-yml
modified: '2026-11-04'
name: Crowe Logic
nav: Providers
network: true
overview: 'Crowe Logic is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Coding, Automation, Developer Tools, and Productivity.


  The Crowe Logic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Crowe Logic''s developer surface includes changelog, documentation, pricing, and 10 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Crowe Logic API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: crowelogic-com-rules
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 20.2
    developer_ergonomics: 9.5
    discoverability: 65.0
    operational_transparency: 15.8
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
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crowelogic Com Domain Security
  slug: crowelogic-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crowelogic-com
tags:
- Artificial Intelligence
- Coding
- Automation
- Developer Tools
- Productivity
- Company
website: https://crowelogic.com/
---
