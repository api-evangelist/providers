---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: SeaWeb provides a context API for AI agents, delivering entity search, indexed extraction, and disruption monitoring.
  name: SeaWeb Context API
  slug: seaweb-context-api
- baseURL: https://api.seaweb.tech
  baseurl_source: declared
  description: 'seaweb-tech API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: seaweb-tech API
  slug: seaweb-tech-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: Security
  url: https://github.com/aritroBh/SeaWeb/blob/main/SECURITY.md
- group: design
  href: https://artifacts.apis.io/seaweb-tech/rules/seaweb-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/seaweb-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/seaweb-tech/json-ld/seaweb-tech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/seaweb-tech-context.jsonld
- group: design
  href: https://artifacts.apis.io/seaweb-tech/vocabulary/seaweb-tech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/seaweb-tech-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/seaweb-tech/data-model/seaweb-tech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/seaweb-tech-data-model.yml
- group: operate
  href: https://artifacts.apis.io/seaweb-tech/changelog/seaweb-tech-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/seaweb-tech-changelog.yml
- group: design
  href: https://artifacts.apis.io/seaweb-tech/conformance/seaweb-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/seaweb-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/seaweb-tech/llms/seaweb-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seaweb-tech-llms.txt
- group: auth
  href: https://artifacts.apis.io/seaweb-tech/well-known/seaweb-tech-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/seaweb-tech-security.txt
- group: agent
  href: https://artifacts.apis.io/seaweb-tech/well-known/seaweb-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/seaweb-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/seaweb-tech/hosts/seaweb-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seaweb-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/seaweb-tech/vendors/seaweb-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seaweb-tech-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://seaweb.tech/signin
- group: auth
  href: https://artifacts.apis.io/seaweb-tech/security/seaweb-tech-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/seaweb-tech-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/seaweb-tech/security/seaweb-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seaweb-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seaweb.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://seaweb.tech/docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://seaweb.tech/docs-mcp.html
- group: start
  title: ''
  type: GettingStarted
  url: https://seaweb.tech/docs.html
- group: operate
  title: ''
  type: Support
  url: https://seaweb.tech/contact.html
- group: company
  title: ''
  type: Blog
  url: https://seaweb.tech/blog.html
- group: commercial
  title: ''
  type: Pricing
  url: https://seaweb.tech/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seaweb.tech/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seaweb.tech/privacy.html
coverage:
  checked: '2026-10-31'
  detail: Documentation is public and readable but no OpenAPI, GraphQL, AsyncAPI, or other machine-readable spec is published.
  evidence:
  - status: 200
    url: https://seaweb.tech/docs-mcp.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: SeaWeb provides a context API for AI agents, delivering entity search, indexed extraction, and disruption monitoring. The platform offers structured web content with honest labels, allowing agents to retrieve searchable passages, extract data, and receive real-time alerts on travel or event disruptions. It supports both anonymous read‑only access and authenticated tool calls via a simple JSON‑RPC MCP endpoint.
image: https://seaweb.tech/og-v2.jpg
json_schemas:
- name: PostMcpRequest
  property_count: 4
  slug: seaweb-tech-post-mcp-request
jsonld:
- class_count: 1
  name: Seaweb Tech Context
  property_count: 4
  slug: seaweb-tech-context
layout: provider
modified: '2026-10-31'
name: seaweb-tech
nav: Providers
network: true
overview: 'seaweb-tech is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, ContextAPI, Search, Extraction, and Monitoring.


  The seaweb-tech catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  seaweb-tech''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: seaweb-tech API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: seaweb-tech-rules
scopes:
- name: Seaweb Tech Scopes
  scope_count: 0
  slug: seaweb-tech-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 17.9
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 36.0
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
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/seaweb-tech/seaweb-tech-2026-11-03T142923.png
security:
- kind: authentication
  name: Seaweb Tech Authentication
  slug: seaweb-tech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Seaweb Tech Domain Security
  slug: seaweb-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Seaweb Tech Vulnerability Disclosure
  slug: seaweb-tech-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: seaweb-tech
tags:
- Artificial Intelligence
- ContextAPI
- Search
- Extraction
- Monitoring
website: https://seaweb.tech/
---
