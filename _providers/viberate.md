---
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: Provides music analytics and data via REST endpoints.
  name: Viberate Music Data API
  slug: viberate-music-data-api
- baseURL: https://data.viberate.com/api/v1
  baseurl_source: declared
  description: The Artist API from Viberate — 4 operation(s) for artist.
  name: Viberate Artist API
  slug: viberate-artist-api
- baseURL: https://data.viberate.com/api/v1
  baseurl_source: declared
  description: The Rate Limit API from Viberate — 1 operation(s) for rate limit.
  name: Viberate Rate Limit API
  slug: viberate-rate-limit-api
- baseURL: https://data.viberate.com/api/v1
  baseurl_source: declared
  description: The Share API from Viberate — 1 operation(s) for share.
  name: Viberate Share API
  slug: viberate-share-api
artifact_total: 16
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/viberate/refs/heads/main/plans/viberate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/viberate-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/viberate/refs/heads/main/rules/viberate-rules.yml
  title: ''
  type: Spectral
  url: rules/viberate-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/viberate/refs/heads/main/json-ld/viberate-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/viberate-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/viberate/refs/heads/main/vocabulary/viberate-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/viberate-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/viberate/refs/heads/main/data-model/viberate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/viberate-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/viberate/refs/heads/main/conformance/viberate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/viberate-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/viberate/refs/heads/main/llms/viberate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/viberate-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/viberate/refs/heads/main/mcp/viberate-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/viberate-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/viberate/refs/heads/main/hosts/viberate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/viberate-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/viberate/refs/heads/main/vendors/viberate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/viberate-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.viberate.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://www.viberate.com/help/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.viberate.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.viberate.com/privacy-and-cookie-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.viberate.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/viberate/refs/heads/main/authentication/viberate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/viberate-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/viberate/refs/heads/main/security/viberate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/viberate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://viberate.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.viberate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.viberate.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.viberate.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.viberate.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.viberate.com/signup/
- group: start
  title: ''
  type: Login
  url: https://app.viberate.com/login/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://viberate.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Viberate provides music analytics and data services, offering insights across platforms such as Spotify, TikTok, Apple Music, YouTube, and radio. Their platform delivers artist, song, playlist, audience, and festival analytics, along with industry trends and market intelligence, enabling A&R teams, event organizers, and artists to make data‑driven decisions.
image: https://viberate.ams3.cdn.digitaloceanspaces.com/com/analytics-share.jpg
json_schemas:
- name: GetArtistAdvancedSearchResponse
  property_count: 7
  slug: viberate-get-artist-advanced-search-response
- name: GetArtistByChannelChannelnameLinkidResponse
  property_count: 13
  slug: viberate-get-artist-by-channel-channelname-linkid-response
- name: GetArtistSearchResponse
  property_count: 15
  slug: viberate-get-artist-search-response
- name: GetArtistViberateChartResponse
  property_count: 3
  slug: viberate-get-artist-viberate-chart-response
- name: GetRateLimitStatusResponse
  property_count: 5
  slug: viberate-get-rate-limit-status-response
- name: GetShareDocsLogoPngResponse
  property_count: 2
  slug: viberate-get-share-docs-logo-png-response
jsonld:
- class_count: 6
  name: Viberate Context
  property_count: 18
  slug: viberate-context
layout: provider
mcp_servers:
- description: Remote MCP server at api-docs.viberate.com.
  name: Viberate MCP Server
  slug: viberate-mcp-yml
modified: '2026-10-12'
name: Viberate
nav: Providers
network: true
overview: 'Viberate is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Artist API, Rate Limit API, Share API, and 1 more. Tagged areas include Music, Analytics, Data, and Platform.


  The Viberate catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Viberate''s developer surface includes support, engineering blog, authentication, documentation, API reference, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Viberate Plans Pricing
  plan_count: 3
  slug: viberate-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Viberate API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: viberate-rules
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 45.2
    discoverability: 71.7
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
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
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Viberate Authentication
  slug: viberate-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Viberate Domain Security
  slug: viberate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: viberate
tags:
- Music
- Analytics
- Data
- Platform
website: https://viberate.com/
---
