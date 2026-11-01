---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Scrapefield Com Agentic Access
  operation_count: 52
  slug: scrapefield-com-agentic-access
  summary_line: 52 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.scrapefield.com/v1
  baseurl_source: declared
  description: The Account API from scrapefield-com — 3 operation(s) for account.
  name: scrapefield-com Account API
  slug: scrapefield-com-account-api
- baseURL: https://api.scrapefield.com/v1
  baseurl_source: declared
  description: The Catalogue API from scrapefield-com — 3 operation(s) for catalogue.
  name: scrapefield-com Catalogue API
  slug: scrapefield-com-catalogue-api
- baseURL: https://api.scrapefield.com/v1
  baseurl_source: declared
  description: The Google Maps API from scrapefield-com — 5 operation(s) for google maps.
  name: scrapefield-com Google Maps API
  slug: scrapefield-com-google-maps-api
- baseURL: https://api.scrapefield.com/v1
  baseurl_source: declared
  description: The Instagram API from scrapefield-com — 6 operation(s) for instagram.
  name: scrapefield-com Instagram API
  slug: scrapefield-com-instagram-api
- baseURL: https://api.scrapefield.com/v1
  baseurl_source: declared
  description: The TikTok API from scrapefield-com — 8 operation(s) for tiktok.
  name: scrapefield-com Tik Tok API
  slug: scrapefield-com-tiktok-api
- baseURL: https://api.scrapefield.com/v1
  baseurl_source: declared
  description: The X API from scrapefield-com — 8 operation(s) for x.
  name: scrapefield-com X API
  slug: scrapefield-com-x-api
- baseURL: https://api.scrapefield.com/v1
  baseurl_source: declared
  description: The Linked In API from scrapefield-com — 18 operation(s) for linked in.
  name: scrapefield-com Linked In API
  slug: scrapefield-com-linked-in-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/scrapefield-com/agentic-access/scrapefield-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scrapefield-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/scrapefield-com/rate-limits/scrapefield-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scrapefield-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/scrapefield-com/plans/scrapefield-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scrapefield-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/scrapefield-com/rules/scrapefield-com-rules.yml
  title: ''
  type: Spectral
  url: rules/scrapefield-com-rules.yml
- group: design
  href: https://artifacts.apis.io/scrapefield-com/json-ld/scrapefield-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/scrapefield-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/scrapefield-com/vocabulary/scrapefield-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/scrapefield-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/scrapefield-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/scrapefield-com/data-model/scrapefield-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scrapefield-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/scrapefield-com/changelog/scrapefield-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/scrapefield-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/scrapefield-com/security/scrapefield-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/scrapefield-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/scrapefield-com/authentication/scrapefield-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scrapefield-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/scrapefield-com/errors/scrapefield-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scrapefield-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/scrapefield-com/conformance/scrapefield-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scrapefield-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/scrapefield-com/llms/scrapefield-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scrapefield-com-llms.txt
- group: build
  href: https://artifacts.apis.io/scrapefield-com/mcp/scrapefield-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/scrapefield-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/scrapefield-com/mcp/scrapefield-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scrapefield-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/scrapefield-com/well-known/scrapefield-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scrapefield-com-security.txt
- group: auth
  href: https://artifacts.apis.io/scrapefield-com/well-known/scrapefield-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scrapefield-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/scrapefield-com/well-known/scrapefield-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scrapefield-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/scrapefield-com/hosts/scrapefield-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scrapefield-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/scrapefield-com/vendors/scrapefield-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scrapefield-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://scrapefield.com/status
- group: start
  title: ''
  type: SignUp
  url: https://api.scrapefield.com/v1/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://scrapefield.com/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://scrapefield.com/changelog
- group: auth
  href: https://artifacts.apis.io/scrapefield-com/security/scrapefield-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/scrapefield-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/scrapefield-com/security/scrapefield-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scrapefield-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scrapefield.com/
- group: docs
  title: ''
  type: Documentation
  url: https://scrapefield.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://scrapefield.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://scrapefield.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scrapefield.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scrapefield.com/privacy
- group: other
  title: ''
  type: SignIn
  url: https://scrapefield.com/login
- group: operate
  title: ''
  type: Contact
  url: https://scrapefield.com/contact
created: '2026-10-31'
description: ScrapeField provides a unified API to scrape data from multiple platforms including Google Maps, LinkedIn, Instagram, TikTok, and X (formerly Twitter). The service abstracts the complexities of each platform, handling proxies, browsers, and retries to deliver clean JSON responses. It offers a credit‑based pricing model, refunds for failed calls, and guarantees that credits never expire. The platform is designed for developers and AI agents needing reliable, anonymized access to social and location data.
image: https://scrapefield.com/og?p=%2F
json_schemas:
- name: google_maps_place
  property_count: 22
  slug: scrapefield-com-google-maps-place
- name: instagram_post
  property_count: 19
  slug: scrapefield-com-instagram-post
- name: linkedin_activity
  property_count: 7
  slug: scrapefield-com-linkedin-activity
- name: linkedin_post
  property_count: 14
  slug: scrapefield-com-linkedin-post
- name: linkedin_profile
  property_count: 17
  slug: scrapefield-com-linkedin-profile
- name: x_post
  property_count: 12
  slug: scrapefield-com-x-post
jsonld:
- class_count: 31
  name: Scrapefield Com Context
  property_count: 191
  slug: scrapefield-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at scrapefield.com.
  name: scrapefield-com MCP Server
  slug: scrapefield-com-mcp-yml
modified: '2026-10-31'
name: scrapefield-com
nav: Providers
network: true
overview: 'scrapefield-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Catalogue API, Google Maps API, and 4 more. Tagged areas include API, Data, Scraping, SocialMedia, and Automation.


  The scrapefield-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  scrapefield-com''s developer surface includes changelog, authentication, signup flow, getting-started guide, API reference, documentation, pricing, and 28 more developer resources.'
plans:
- name: Scrapefield Com Plans Pricing
  plan_count: 5
  slug: scrapefield-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Scrapefield Com Rate Limits
  slug: scrapefield-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: scrapefield-com API Rules
  rule_count: 19
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 5
  slug: scrapefield-com-rules
scopes:
- name: Scrapefield Com Scopes
  scope_count: 0
  slug: scrapefield-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 95.7
    catalog_earned_first_party: 0.0
    catalog_gap: 19.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 61.9
    developer_ergonomics: 49.3
    discoverability: 65.0
    operational_transparency: 61.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Scrapefield Com Authentication
  slug: scrapefield-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Scrapefield Com Domain Security
  slug: scrapefield-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Scrapefield Com Vulnerability Disclosure
  slug: scrapefield-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: search-places
  slug: scrapefield-com-search_places
slug: scrapefield-com
tags:
- API
- Data
- Scraping
- SocialMedia
- Automation
website: https://scrapefield.com/
---
