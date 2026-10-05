---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bhanzu Agentic Access
  operation_count: 6
  slug: bhanzu-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- baseURL: https://bhanzu.com
  baseurl_source: spec
  description: AI-readable content files and tools
  name: Bhanzu AI API
  slug: bhanzu-ai-api
- baseURL: https://bhanzu.com
  baseurl_source: spec
  description: Published article content
  name: Bhanzu Content API
  slug: bhanzu-content-api
artifact_total: 11
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/agentic-access/bhanzu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bhanzu-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/rules/bhanzu-rules.yml
  title: ''
  type: Spectral
  url: rules/bhanzu-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/json-ld/bhanzu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bhanzu-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/vocabulary/bhanzu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bhanzu-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/data-model/bhanzu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bhanzu-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/errors/bhanzu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bhanzu-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/conformance/bhanzu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bhanzu-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/llms/bhanzu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bhanzu-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/mcp/bhanzu-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bhanzu-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/mcp/bhanzu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bhanzu-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/well-known/bhanzu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bhanzu-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/hosts/bhanzu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bhanzu-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/vendors/bhanzu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bhanzu-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.bhanzu.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bhanzu/refs/heads/main/security/bhanzu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bhanzu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bhanzu.com
- group: company
  title: ''
  type: Blog
  url: https://bhanzu.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bhanzu.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bhanzu.com/terms-and-conditions
created: '2026-09-28'
description: Bhanzu provides online math education platforms offering personalized, AI‑enhanced learning experiences for students across K‑12. Founded by world‑record‑holding mental calculator Neelakantha Bhanu Prakash, the company delivers live interactive classes, practice tools, and a suite of AI assistants to make math engaging and accessible worldwide. With over 50,000 students served, 3 million teaching hours, and presence in 16 countries, Bhanzu aims to transform math fear into confidence through concept‑first teaching, growth‑mindset cultivation, and data‑driven insights.
image: https://bhanzu.com/og-images/book-demo-og.webp
json_schemas:
- name: ArticleFull
  property_count: 0
  slug: bhanzu-article-full
- name: ArticleSummary
  property_count: 13
  slug: bhanzu-article-summary
- name: JsonRpcRequest
  property_count: 4
  slug: bhanzu-json-rpc-request
- name: JsonRpcResponse
  property_count: 4
  slug: bhanzu-json-rpc-response
jsonld:
- class_count: 4
  name: Bhanzu Context
  property_count: 18
  slug: bhanzu-context
layout: provider
mcp_servers:
- description: Remote MCP server at bhanzu.com.
  name: Bhanzu MCP Server
  slug: bhanzu-mcp-yml
modified: '2026-09-28'
name: Bhanzu
nav: Providers
network: true
overview: 'Bhanzu publishes 2 APIs on the [APIs.io](https://apis.io/) network: AI API and Content API. Tagged areas include Education, Math, E-Learning, Artificial Intelligence, and K-12.


  The Bhanzu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bhanzu''s developer surface includes documentation, engineering blog, and 17 more developer resources.'
random_paper: 10
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Bhanzu API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: bhanzu-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 55.9
    developer_ergonomics: 11.9
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 17.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Bhanzu Domain Security
  slug: bhanzu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bhanzu
tags:
- Education
- Math
- E-Learning
- Artificial Intelligence
- K-12
website: https://bhanzu.com
---
