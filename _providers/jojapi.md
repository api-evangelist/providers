---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: JoJ API is a marketplace offering web‑scraping, search, and social‑media data APIs with unified billing and wallet management.
  name: JoJ API Marketplace
  slug: joj-api-marketplace
- baseURL: https://app.jojapi.com
  baseurl_source: declared
  description: 'APRYCO API as documented publicly: 61 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: APRYCO API
  slug: jojapi-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/jojapi/rules/jojapi-rules.yml
  title: ''
  type: Spectral
  url: rules/jojapi-rules.yml
- group: design
  href: https://artifacts.apis.io/jojapi/json-ld/jojapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jojapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/jojapi/vocabulary/jojapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jojapi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/jojapi/data-model/jojapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jojapi-data-model.yml
- group: build
  href: https://artifacts.apis.io/jojapi/cli/jojapi-cli.yml
  title: ''
  type: CLI
  url: cli/jojapi-cli.yml
- group: operate
  href: https://artifacts.apis.io/jojapi/changelog/jojapi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/jojapi-changelog.yml
- group: auth
  href: https://artifacts.apis.io/jojapi/authentication/jojapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jojapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/jojapi/conformance/jojapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jojapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jojapi/llms/jojapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jojapi-llms.txt
- group: other
  href: https://artifacts.apis.io/jojapi/a2a/jojapi-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/jojapi-a2a.yml
- group: agent
  href: https://artifacts.apis.io/jojapi/mcp/jojapi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jojapi-mcp.yml
- group: agent
  href: https://artifacts.apis.io/jojapi/well-known/jojapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jojapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/jojapi/hosts/jojapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jojapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/jojapi/vendors/jojapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jojapi-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jojapicom
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.jojapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/jojapi/security/jojapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jojapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jojapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jojapi.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.jojapi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://jojapi.com/hub
- group: start
  title: ''
  type: GettingStarted
  url: https://jojapi.com/about
- group: operate
  title: ''
  type: Support
  url: https://jojapi.com/contact
- group: company
  title: ''
  type: Blog
  url: https://jojapi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://jojapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.jojapi.com/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.jojapi.com/legal/privacy
coverage:
  checked: '2026-10-18'
  detail: Documentation is rendered via Mintlify JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.jojapi.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-17'
description: APRYCO operates JoJ API, a marketplace that aggregates and provides access to a wide range of web‑scraping, search, and social‑media data APIs through a unified gateway. Developers can obtain scoped API keys, manage usage and billing per object, and integrate services such as Google Web Search, Twitter/X, YouTube, TikTok, and custom data extraction APIs. The platform offers transparent per‑object pricing, a single wallet for multiple APIs, and tools for rapid prototyping, making it easier to build data‑driven applications without managing individual provider accounts.
image: https://jojapi.com/og/jojapi-og.png
json_schemas:
- name: PostJojapiAgentTopupRequest
  property_count: 2
  slug: jojapi-post-jojapi-agent-topup-request
jsonld:
- class_count: 1
  name: Jojapi Context
  property_count: 2
  slug: jojapi-context
layout: provider
mcp_servers:
- description: Remote MCP server at jojapi.main-kill-isr.mintlify.me.
  name: APRYCO MCP Server
  slug: jojapi-mcp-yml
modified: '2026-10-17'
name: APRYCO
nav: Providers
network: true
overview: 'APRYCO is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Data, and Web Scraping.


  The APRYCO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APRYCO''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, support, and 20 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: APRYCO API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: jojapi-rules
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 43.2
    catalog_earned_first_party: 0.0
    catalog_gap: 71.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 64.3
    discoverability: 48.3
    operational_transparency: 21.1
  previous_composite: 36.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 43
      marker_coverage: 100.0
      total: 43
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Jojapi Authentication
  slug: jojapi-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Jojapi Domain Security
  slug: jojapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jojapi
tags:
- Company
- Marketplace
- Data
- Web Scraping
website: https://jojapi.com/
---
