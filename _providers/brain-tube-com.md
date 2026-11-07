---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Personal knowledge corpus API covering search, corpus stats, bookmarks, ingest, and Brains over plain HTTP for use by web apps, mobile clients, and chat widgets.
  name: BrainTube REST API
  slug: braintube-rest-api
- baseURL: https://mcp.brain-tube.com
  baseurl_source: declared
  description: Personal knowledge corpus API covering search, corpus stats, bookmarks, ingest, and Brains over plain HTTP for use by web apps, mobile clients, and chat widgets. This is a subset of the full BrainTube
  name: BrainTube REST API API
  slug: braintube-rest-api-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/brain-tube-com/rules/brain-tube-com-rules.yml
  title: ''
  type: Spectral
  url: rules/brain-tube-com-rules.yml
- group: design
  href: https://artifacts.apis.io/brain-tube-com/json-ld/brain-tube-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/brain-tube-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/brain-tube-com/vocabulary/brain-tube-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brain-tube-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/brain-tube-com/conformance/brain-tube-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brain-tube-com-conformance.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://brain-tube.com/guide/give-your-ai-memory-mcp
- group: commercial
  href: https://artifacts.apis.io/brain-tube-com/plans/brain-tube-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brain-tube-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/brain-tube-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/brain-tube-com/data-model/brain-tube-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brain-tube-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/brain-tube-com/changelog/brain-tube-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/brain-tube-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/brain-tube-com/authentication/brain-tube-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brain-tube-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/brain-tube-com/errors/brain-tube-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brain-tube-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/brain-tube-com/llms/brain-tube-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brain-tube-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/brain-tube-com/mcp/brain-tube-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brain-tube-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/brain-tube-com/well-known/brain-tube-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brain-tube-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/brain-tube-com/hosts/brain-tube-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brain-tube-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/brain-tube-com/vendors/brain-tube-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brain-tube-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://brain-tube.com/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://brain-tube.com/changelog
- group: auth
  href: https://artifacts.apis.io/brain-tube-com/security/brain-tube-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brain-tube-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brain-tube.com/
- group: operate
  title: ''
  type: Support
  url: https://brain-tube.com/support
- group: company
  title: ''
  type: Blog
  url: https://brain-tube.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://brain-tube.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brain-tube.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brain-tube.com/privacy
created: '2026-11-02'
description: BrainTube is a platform that saves videos, podcasts, articles, PDFs and other content in a personal library, transcribes and indexes it, and lets users query the saved material via AI assistants like Claude, ChatGPT, or Cursor. Users can add content via a Chrome extension, iPhone app, or direct links, and then ask AI to retrieve specific moments or summaries. The service offers free and paid plans, includes MCP (Machine‑Content‑Protocol) integration for AI tools, and emphasizes data ownership, allowing full export of the library. BrainTube is operated by VR EXPRESS OOD, a Bulgarian company.
image: https://brain-tube.com/og-image.png
json_schemas:
- name: Bookmark
  property_count: 7
  slug: brain-tube-com-bookmark
- name: BulkIngestRequest
  property_count: 2
  slug: brain-tube-com-bulk-ingest-request
- name: BulkIngestResponse
  property_count: 4
  slug: brain-tube-com-bulk-ingest-response
- name: IngestRequest
  property_count: 6
  slug: brain-tube-com-ingest-request
- name: Stats
  property_count: 4
  slug: brain-tube-com-stats
- name: TaintedSearchResponse
  property_count: 3
  slug: brain-tube-com-tainted-search-response
jsonld:
- class_count: 9
  name: Brain Tube Com Context
  property_count: 29
  slug: brain-tube-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.brain-tube.com.
  name: BrainTube MCP Server
  slug: brain-tube-com-mcp-yml
modified: '2026-11-02'
name: BrainTube
nav: Providers
network: true
overview: 'BrainTube publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including REST API API, and 1 more. Tagged areas include AI Integration and MCP.


  The BrainTube catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BrainTube''s developer surface includes getting-started guide, changelog, authentication, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Brain Tube Com Plans Pricing
  plan_count: 4
  slug: brain-tube-com-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: BrainTube API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: brain-tube-com-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 58.9
    developer_ergonomics: 32.6
    discoverability: 56.7
    operational_transparency: 7.9
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Brain Tube Com Authentication
  slug: brain-tube-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Brain Tube Com Domain Security
  slug: brain-tube-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brain-tube-com
tags:
- AI Integration
- MCP
website: https://brain-tube.com/
---
