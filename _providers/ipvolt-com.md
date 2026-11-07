---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Proxy infrastructure API (no public machine-readable spec)
  name: ipvolt Proxy API
  slug: ipvolt-proxy-api
- description: 'ipvolt-com API as documented publicly: 23 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: ipvolt-com API
  slug: ipvolt-com-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/ipvolt-com/plans/ipvolt-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ipvolt-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ipvolt-com/rules/ipvolt-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ipvolt-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ipvolt-com/json-ld/ipvolt-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ipvolt-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ipvolt-com/vocabulary/ipvolt-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ipvolt-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ipvolt-com/data-model/ipvolt-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ipvolt-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/ipvolt-com/conformance/ipvolt-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ipvolt-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ipvolt-com/llms/ipvolt-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ipvolt-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ipvolt-com/mcp/ipvolt-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ipvolt-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/ipvolt-com/hosts/ipvolt-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ipvolt-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ipvolt-com/vendors/ipvolt-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ipvolt-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/ipvolt-com/packages/ipvolt-com-packages.yml
  title: ''
  type: SDKs
  url: packages/ipvolt-com-packages.yml
- group: build
  href: https://artifacts.apis.io/ipvolt-com/packages/ipvolt-com-packages.yml
  title: ''
  type: Packages
  url: packages/ipvolt-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ipvolt.com/terms
- group: operate
  title: ''
  type: Support
  url: https://ipvolt.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ipvolt.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ipvolt
- group: start
  title: ''
  type: GettingStarted
  url: https://ipvolt.com/guides/curl-proxy-setup
- group: auth
  href: https://artifacts.apis.io/ipvolt-com/security/ipvolt-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ipvolt-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ipvolt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ipvolt.com/guides
- group: company
  title: ''
  type: Blog
  url: https://ipvolt.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ipvolt.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://ipvolt.com/#waitlist-closing
- group: build
  title: ''
  type: Tools
  url: https://ipvolt.com/tools
coverage:
  checked: '2026-10-31'
  detail: The provider's documentation is public but no OpenAPI/AsyncAPI/GraphQL spec is published; attempts to fetch common spec URLs returned 404.
  evidence:
  - status: 404
    url: https://ipvolt.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: ipvolt provides a proxy infrastructure platform tailored for developers and data teams. It offers residential, datacenter, ISP (static residential) and mobile proxies that enable reliable web research, site monitoring, and application testing. The service emphasizes easy integration, transparent pricing starting at $3.50 per GB, and supports payment by card and major cryptocurrencies. ipvolt also publishes guides, free tools, and a blog to help users get started and optimize their proxy usage.
image: https://ipvolt.com/brand/ipvolt.svg
json_schemas:
- name: GetDownloadsAcceptEncodingDefaultsHarnessSnippetsCurlVerifyS
  property_count: 1
  slug: ipvolt-com-get-downloads-accept-encoding-defaults-harness-snippets-curl-verify-s
jsonld:
- class_count: 1
  name: Ipvolt Com Context
  property_count: 0
  slug: ipvolt-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.ipvolt.com.
  name: ipvolt-com MCP Server
  slug: ipvolt-com-mcp-yml
modified: '2026-10-30'
name: ipvolt-com
nav: Providers
network: true
overview: 'ipvolt-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Proxy, Developer Tools, Infrastructure, Networking, and Data.


  The ipvolt-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ipvolt-com''s developer surface includes support, getting-started guide, documentation, engineering blog, pricing, signup flow, tooling, and 17 more developer resources.'
plans:
- name: Ipvolt Com Plans Pricing
  plan_count: 1
  slug: ipvolt-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Ipvolt Com Rate Limits
  slug: ipvolt-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: ipvolt-com API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: ipvolt-com-rules
scopes:
- name: Ipvolt Com Scopes
  scope_count: 0
  slug: ipvolt-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.2
    catalog_earned_first_party: 8.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 16.4
    developer_ergonomics: 21.4
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 35.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ipvolt-com/ipvolt-com-2026-11-03T134032.png
security:
- kind: authentication
  name: Ipvolt Com Authentication
  slug: ipvolt-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ipvolt Com Domain Security
  slug: ipvolt-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ipvolt-com
tags:
- Proxy
- Developer Tools
- Infrastructure
- Networking
- Data
website: https://ipvolt.com/
---
