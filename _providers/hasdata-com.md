---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.4
  scored_at: '2026-10-31'
api_count: 6
apis:
- baseURL: https://api.hasdata.com
  baseurl_source: declared
  description: 'hasdata-com amazon API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: hasdata-com amazon API
  slug: amazon-api
- baseURL: https://api.hasdata.com
  baseurl_source: declared
  description: 'hasdata-com core API as documented publicly: 24 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: hasdata-com core API
  slug: core-api
- baseURL: https://api.hasdata.com
  baseurl_source: declared
  description: 'hasdata-com tiktok API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: hasdata-com tiktok API
  slug: tiktok-api
- baseURL: https://api.hasdata.com
  baseurl_source: declared
  description: 'hasdata-com walmart API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: hasdata-com walmart API
  slug: walmart-api
- baseURL: https://api.hasdata.com
  baseurl_source: declared
  description: 'hasdata-com yelp API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: hasdata-com yelp API
  slug: yelp-api
- baseURL: https://api.hasdata.com
  baseurl_source: declared
  description: 'hasdata-com youtube API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: hasdata-com youtube API
  slug: youtube-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/hasdata-com/rules/hasdata-com-rules.yml
  title: ''
  type: Spectral
  url: rules/hasdata-com-rules.yml
- group: design
  href: https://artifacts.apis.io/hasdata-com/vocabulary/hasdata-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hasdata-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hasdata-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/hasdata-com/cli/hasdata-com-cli.yml
  title: ''
  type: CLI
  url: cli/hasdata-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/hasdata-com/authentication/hasdata-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hasdata-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/hasdata-com/errors/hasdata-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hasdata-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hasdata-com/conformance/hasdata-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hasdata-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hasdata-com/llms/hasdata-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hasdata-com-llms.txt
- group: other
  href: https://artifacts.apis.io/hasdata-com/a2a/hasdata-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hasdata-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/hasdata-com/mcp/hasdata-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hasdata-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/hasdata-com/mcp/hasdata-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hasdata-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hasdata-com/well-known/hasdata-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hasdata-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/hasdata-com/hosts/hasdata-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hasdata-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/hasdata-com/vendors/hasdata-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hasdata-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HasData
- group: start
  title: ''
  type: Login
  url: http://app.hasdata.com/sign-in
- group: start
  title: ''
  type: SignUp
  url: https://app.hasdata.com/sign-up
- group: auth
  href: https://artifacts.apis.io/hasdata-com/security/hasdata-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hasdata-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hasdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hasdata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hasdata.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hasdata.com/quickstart.md
- group: company
  title: ''
  type: Blog
  url: https://hasdata.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.hasdata.com/basics/pricing.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hasdata.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hasdata.com/privacy-policy
created: '2026-10-29'
description: HasData provides a web scraping service for data pipelines and AI, offering a suite of APIs that transform any URL into structured JSON or Markdown. The platform includes specialized APIs for Google SERP, Maps, News, Amazon, Zillow, and more, with pricing per 1k requests. It supports no‑code scrapers, MCP servers for LLM integration, and a CLI tool. Users can get started quickly via a quickstart guide, and the service handles proxies, rendering, and retries automatically.
image: https://hasdata.com/og-home.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.hasdata.com.
  name: hasdata-com MCP Server
  slug: hasdata-com-mcp-yml
modified: '2026-10-29'
name: hasdata-com
nav: Providers
network: true
overview: 'hasdata-com is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including amazon API, core API, tiktok API, and 3 more. Tagged areas include Web Scraping, Data Pipelines, AI, API, and Automation.


  The hasdata-com catalog on APIs.io includes 1 Spectral governance ruleset.


  hasdata-com''s developer surface includes CLI, authentication, signup flow, documentation, API reference, getting-started guide, engineering blog, and 19 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 0
  name: Hasdata Com Rate Limits
  slug: hasdata-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: hasdata-com API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: hasdata-com-rules
scopes:
- name: Hasdata Com Scopes
  scope_count: 0
  slug: hasdata-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 45.0
    catalog_earned_first_party: 0.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 19.7
    contract_quality: 11.9
    developer_ergonomics: 56.4
    discoverability: 70.0
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hasdata Com Authentication
  slug: hasdata-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hasdata Com Domain Security
  slug: hasdata-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: hasdata-com-hasdata-cli
  slug: hasdata-com-hasdata-cli
- name: hasdata-com-hasdata
  slug: hasdata-com-hasdata
slug: hasdata-com
tags:
- Web Scraping
- Data Pipelines
- AI
- API
- Automation
website: https://hasdata.com/
---
