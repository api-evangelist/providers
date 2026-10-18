---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: Dexio provides a hosted wiki platform for AI agents with an MCP endpoint. Documentation is at https://dexio.wiki/docs.
  name: Dexio API
  slug: dexio-api-2
- baseURL: https://app.dexio.wiki
  baseurl_source: declared
  description: The Dexio API API from Dexio — 1 operation(s) for dexio api.
  name: Dexio Dexio API
  slug: dexio-dexio-api-api
- baseURL: https://app.dexio.wiki
  baseurl_source: declared
  description: The Install API from Dexio — 1 operation(s) for install.
  name: Dexio Install API
  slug: dexio-install-api
- baseURL: https://app.dexio.wiki
  baseurl_source: declared
  description: The Mcp API from Dexio — 1 operation(s) for mcp.
  name: Dexio MCP API
  slug: dexio-mcp-api
artifact_total: 11
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/plans/dexio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dexio-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/rules/dexio-rules.yml
  title: ''
  type: Spectral
  url: rules/dexio-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/json-ld/dexio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dexio-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/vocabulary/dexio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dexio-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/data-model/dexio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dexio-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/authentication/dexio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dexio-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/conformance/dexio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dexio-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/llms/dexio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dexio-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/mcp/dexio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dexio-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/well-known/dexio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dexio-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/hosts/dexio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dexio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/vendors/dexio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dexio-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://dexio.wiki/guides/codex-mcp/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dexio/refs/heads/main/security/dexio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dexio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dexio.wiki
- group: docs
  title: ''
  type: Documentation
  url: https://dexio.wiki/docs
- group: company
  title: ''
  type: Blog
  url: https://dexio.wiki/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dexio.wiki/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dexio.wiki/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dexio.wiki/privacy
- group: operate
  title: ''
  type: Support
  url: https://dexio.wiki/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.dexio.wiki/signup
- group: start
  title: ''
  type: Login
  url: https://app.dexio.wiki/login
coverage:
  checked: '2026-10-05'
  detail: MCP endpoint requires authentication and no OpenAPI spec is published.
  evidence:
  - status: 401
    url: https://app.dexio.wiki/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-05'
description: Dexio provides a hosted wiki platform designed for AI agents to read and write markdown pages through a Memory Control Protocol (MCP). It enables agents like Claude, ChatGPT, Hermes, OpenClaw, and others to share knowledge, maintain histories, and collaborate via a unified, searchable graph of pages. The service offers free access for individual users and tiered pricing for teams, with features such as export to markdown, versioned history, file attachments, and integration guides for various AI models. Dexio emphasizes open-source licensing (AGPL-3.0) for its core and aims to simplify agent memory management across deployments.
image: https://dexio.wiki/og/site/home.png
json_schemas:
- name: PostMcpRequest
  property_count: 4
  slug: dexio-post-mcp-request
jsonld:
- class_count: 1
  name: Dexio Context
  property_count: 4
  slug: dexio-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.dexio.wiki requiring OAuth.
  name: Dexio MCP Server
  slug: dexio-mcp-yml
modified: '2026-10-05'
name: Dexio
nav: Providers
network: true
overview: 'Dexio is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Dexio API, Install API, MCP API, and 1 more. Tagged areas include Artificial Intelligence, Wiki, Knowledge Management, Agent-Integration, and Open Source.


  The Dexio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dexio''s developer surface includes authentication, getting-started guide, documentation, engineering blog, pricing, support, signup flow, and 16 more developer resources.'
plans:
- name: Dexio Plans Pricing
  plan_count: 4
  slug: dexio-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Dexio API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: dexio-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 63.2
    catalog_earned_first_party: 12.0
    catalog_gap: 51.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 19.0
    developer_ergonomics: 40.5
    discoverability: 71.7
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Dexio Authentication
  slug: dexio-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dexio Domain Security
  slug: dexio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dexio
tags:
- Artificial Intelligence
- Wiki
- Knowledge Management
- Agent-Integration
- Open Source
website: https://dexio.wiki
---
