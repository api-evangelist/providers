---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Datacircle Agentic Access
  operation_count: 8
  slug: datacircle-agentic-access
  summary_line: 8 operations · 3 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Remote Streamable HTTP MCP server exposing five tools that each wrap one Datacircle REST call; OAuth sign-in or API key.
  name: Datacircle MCP Server
  slug: datacircle-mcp
- baseURL: https://api.datacircle.dev
  baseurl_source: declared
  description: 'Your Datacircle account: balance, adding funds, files, API key.'
  name: Datacircle Datacircle API
  slug: datacircle-datacircle-api
- baseURL: https://api.datacircle.dev
  baseurl_source: declared
  description: 'LinkedIn Profile API: HarvestAPI''s own request, sent to api.datacircle.dev with your Datacircle key and `X-Data-Provider: harvestapi`.'
  name: Datacircle Harvest API
  slug: datacircle-harvestapi-api
- baseURL: https://api.datacircle.dev
  baseurl_source: declared
  description: 'LinkedIn Profile API: Up2Data''s own request, sent to api.datacircle.dev with your Datacircle key and `X-Data-Provider: up2data`.'
  name: Datacircle Up2 Data API
  slug: datacircle-up2data-api
- baseURL: https://api.datacircle.dev
  baseurl_source: declared
  description: 'LinkedIn Profile API: Fetchin''s own request, sent to api.datacircle.dev with your Datacircle key and `X-Data-Provider: fetchin`.'
  name: Datacircle Fetchin API
  slug: datacircle-fetchin-api
artifact_total: 18
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/agentic-access/datacircle-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/datacircle-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/rate-limits/datacircle-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/datacircle-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/plans/datacircle-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datacircle-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/rules/datacircle-rules.yml
  title: ''
  type: Spectral
  url: rules/datacircle-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/json-ld/datacircle-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datacircle-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/vocabulary/datacircle-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datacircle-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/data-model/datacircle-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datacircle-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/errors/datacircle-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/datacircle-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/conformance/datacircle-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datacircle-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/llms/datacircle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datacircle-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/a2a/datacircle-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/datacircle-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/mcp/datacircle-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/datacircle-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/mcp/datacircle-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/datacircle-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/well-known/datacircle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datacircle-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/hosts/datacircle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datacircle-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/vendors/datacircle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datacircle-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/authentication/datacircle-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datacircle-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/security/datacircle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datacircle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datacircle.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datacircle.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datacircle.dev/quickstart
- group: company
  title: ''
  type: Blog
  url: https://datacircle.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/waynehamadi/datacircle
- group: start
  title: ''
  type: Login
  url: https://datacircle.dev/login
- group: commercial
  title: ''
  type: Pricing
  url: https://datacircle.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datacircle.dev/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datacircle-org
- group: other
  title: ''
  type: X
  url: https://x.com/datacircle_dev
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datacircle.dev/privacy
- group: operate
  title: ''
  type: Support
  url: https://datacircle.dev/support
- group: docs
  title: ''
  type: APIReference
  url: https://docs.datacircle.dev/api-reference/datacircle/reset-your-api-key
created: '2026-10-09'
description: 'Datacircle is a B2B data co-op API: customers send the original request of a supported data provider (currently the Up2Data, HarvestAPI and Fetchin LinkedIn profile APIs) to api.datacircle.dev with a Datacircle key at the provider''s own price with no markup, and receive a daily flat file of pooled co-op data. It also ships a remote MCP server at api.datacircle.dev/mcp.'
image: https://datacircle.dev/og-co-op.jpg
json_schemas:
- name: Balance
  property_count: 5
  slug: datacircle-balance
- name: FetchinProfileResponse
  property_count: 67
  slug: datacircle-fetchin-profile-response
- name: File
  property_count: 8
  slug: datacircle-file
- name: HarvestApiProfileResponse
  property_count: 11
  slug: datacircle-harvest-api-profile-response
- name: Up2DataEnrichResponse
  property_count: 3
  slug: datacircle-up2-data-enrich-response
jsonld:
- class_count: 10
  name: Datacircle Context
  property_count: 102
  slug: datacircle-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.datacircle.dev over streamable HTTP requiring OAuth; 5 tools listed.
  name: Datacircle MCP Server
  slug: datacircle-mcp-server
modified: '2026-10-11'
name: Datacircle
nav: Providers
network: true
overview: 'Datacircle publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Datacircle API, Harvest API, Up2 Data API, and 2 more. Tagged areas include Company, B2B Data, Data Enrichment, LinkedIn, and Profiles.


  The Datacircle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Datacircle''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, support, API reference, and 24 more developer resources.'
plans:
- name: Datacircle Plans Pricing
  plan_count: 3
  slug: datacircle-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Datacircle Rate Limits
  slug: datacircle-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Datacircle API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: datacircle-rules
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.5
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 64.4
    developer_ergonomics: 47.6
    discoverability: 75.0
    operational_transparency: 26.3
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/datacircle/refs/heads/main/screenshots/datacircle-2026-10-11T103549.png
security:
- kind: authentication
  name: Datacircle Authentication
  slug: datacircle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Datacircle Domain Security
  slug: datacircle-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datacircle
tags:
- Company
- B2B Data
- Data Enrichment
- LinkedIn
- Profiles
- MCP
- Data Co-op
website: https://datacircle.dev
---
