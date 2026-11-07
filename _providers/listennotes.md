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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Listennotes Agentic Access
  operation_count: 26
  slug: listennotes-agentic-access
  summary_line: 26 operations · 5 acting
api_count: 3
apis:
- baseURL: https://listen-api.listennotes.com/api/v2
  baseurl_source: declared
  description: Endpoints to get insights of podcasts, e.g., audience demographics.
  name: Listen Notes Insights API
  slug: insights-api
- baseURL: https://listen-api.listennotes.com/api/v2
  baseurl_source: declared
  description: Endpoints to fetch Listen Later playlists data.
  name: Listen Notes Playlist API
  slug: playlist-api
- baseURL: https://listen-api.listennotes.com/api/v2
  baseurl_source: declared
  description: Endpoints to improve the podcast database.
  name: Listen Notes Podcaster API
  slug: listennotes-podcaster-api-api
- baseURL: https://listen-api.listennotes.com/api/v2
  baseurl_source: declared
  description: Endpoints to search podcasts and episodes.
  name: Listen Notes Search API
  slug: listennotes-search-api-api
- baseURL: https://listen-api.listennotes.com/api/v2
  baseurl_source: declared
  description: Endpoints to fetch podcasts, episodes, charts, and reference data.
  name: Listen Notes Directory API
  slug: listennotes-directory-api-api
- baseURL: https://listen-api.listennotes.com/api/v2
  baseurl_source: declared
  description: 'The Listen API: Podcast Search, Directory, And Insights API API from Listen Notes — 0 operation(s) for listen api: podcast search, directory, and insights api.'
  name: 'Listen Notes Listen API: Podcast Search, Directory, And Insights API'
  slug: listennotes-listen-api-podcast-search-directory-and-insights-api-api
artifact_total: 25
asyncapis:
- description: ''
  name: Listennotes Webhooks
  slug: listennotes-webhooks
collections:
- collection_type: open
  name: 'Listen API: Podcast Search, Directory, and Insights Directory API API'
  slug: open-listennotes-directory-api-api
- collection_type: open
  name: 'Listen API: Podcast Search, Directory, and Insights Directory API Insights API API'
  slug: open-listennotes-insights-api-api
- collection_type: open
  name: 'Listen API: Podcast Search, Directory, and Insights Directory API Playlist API API'
  slug: open-listennotes-playlist-api-api
- collection_type: open
  name: 'Listen API: Podcast Search, Directory, and Insights Directory API Podcaster API API'
  slug: open-listennotes-podcaster-api-api
- collection_type: open
  name: 'Listen API: Podcast Search, Directory, and Insights Directory API Search API API'
  slug: open-listennotes-search-api-api
- collection_type: open
  name: Listen API (Listen Notes)
  slug: open-listennotes
common:
- group: design
  href: https://artifacts.apis.io/listennotes/json-ld/listennotes-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/listennotes-context.jsonld
- group: design
  href: https://artifacts.apis.io/listennotes/asyncapi/listennotes-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/listennotes-webhooks.yml
- group: design
  href: https://artifacts.apis.io/listennotes/data-model/listennotes-data-model.yml
  title: ''
  type: DataModel
  url: data-model/listennotes-data-model.yml
- group: design
  href: https://artifacts.apis.io/listennotes/errors/listennotes-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/listennotes-problem-types.yml
- group: other
  href: https://artifacts.apis.io/listennotes/overlays/listennotes-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/listennotes-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/listennotes/rules/listennotes-rules.yml
  title: ''
  type: Spectral
  url: rules/listennotes-rules.yml
- group: design
  href: https://artifacts.apis.io/listennotes/vocabulary/listennotes-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/listennotes-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/listennotes/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/listennotes/conformance/listennotes-conformance.yml
  title: ''
  type: Conformance
  url: conformance/listennotes-conformance.yml
- group: agent
  href: https://artifacts.apis.io/listennotes/llms/listennotes-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/listennotes-llms.txt
- group: agent
  href: https://artifacts.apis.io/listennotes/well-known/listennotes-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/listennotes-well-known.yml
- group: other
  href: https://artifacts.apis.io/listennotes/hosts/listennotes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/listennotes-hosts.yml
- group: other
  href: https://artifacts.apis.io/listennotes/vendors/listennotes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/listennotes-vendors.yml
- group: build
  href: https://artifacts.apis.io/listennotes/packages/listennotes-packages.yml
  title: ''
  type: SDKs
  url: packages/listennotes-packages.yml
- group: build
  href: https://artifacts.apis.io/listennotes/packages/listennotes-packages.yml
  title: ''
  type: Packages
  url: packages/listennotes-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.listennotes.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://www.listennotes.com/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.listennotes.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.listennotes.com/api/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.listennotes.com/blog/
- group: other
  href: https://artifacts.apis.io/listennotes/capabilities/listennotes-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/listennotes-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/listennotes/agentic-access/listennotes-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/listennotes-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/listennotes/security/listennotes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/listennotes-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/listennotes/authentication/listennotes-authentication.yml
  title: ''
  type: Authentication
  url: authentication/listennotes-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ListenNotes
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/listen-notes
- group: company
  title: ''
  type: Website
  url: https://www.listennotes.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.listennotes.com/api/docs/
- group: commercial
  href: https://artifacts.apis.io/listennotes/plans/listennotes-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/listennotes-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/listennotes/rate-limits/listennotes-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/listennotes-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/listennotes/finops/listennotes-finops.yml
  title: ''
  type: FinOps
  url: finops/listennotes-finops.yml
- group: other
  title: ''
  type: APIsJSON
  url: https://www.podcastapi.com/apis.json
- group: agent
  title: ''
  type: APIsJSONWellKnown
  url: https://www.podcastapi.com/.well-known/apis.json
- group: other
  title: ''
  type: ApiCatalog
  url: https://www.podcastapi.com/.well-known/api-catalog
- group: docs
  href: https://artifacts.apis.io/listennotes/openapi/listennotes-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/listennotes-openapi.json
- group: docs
  title: ''
  type: OpenAPIYaml
  url: https://listen-api.listennotes.com/api/v2/openapi.yaml
- group: agent
  title: ''
  type: LLMsTXT
  url: https://www.podcastapi.com/llms.txt
- group: agent
  title: ''
  type: LLMsFullTXT
  url: https://www.podcastapi.com/llms-full.txt
- group: agent
  title: ''
  type: SkillsRepo
  url: https://github.com/PodcastAPI/skills
created: '2026-07-03'
description: Listen Notes runs the largest podcast search engine and database, and exposes it as the Listen API - a simple, no-nonsense podcast search, directory, and insights REST API. It lets developers full-text search millions of podcasts and episodes by people, places, and topics; fetch podcast and episode metadata; browse best-podcasts charts, curated lists, and genres; retrieve podcast/episode recommendations; power typeahead autocomplete; and pull audience demographics and publisher-domain insights. The API is served at https://listen-api.listennotes.com/api/v2 and authenticated with an X-ListenAPI-Key header, with FREE, PRO, and ENTERPRISE plans billed on a request basis.
finops:
- has_sources: true
  method: derived
  name: Listennotes Finops
  primary_unit: requests/month
  service_category: ''
  slug: listennotes-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/listennotes.png
jsonld:
- class_count: 47
  name: Listennotes Context
  property_count: 104
  slug: listennotes-context
layout: provider
modified: '2026-09-16'
name: Listen Notes
nav: Providers
network: true
overview: 'Listen Notes publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Insights API, Playlist API, Podcaster API, and 3 more. Tagged areas include Podcasts, Podcast Search, Podcast Directory, Search, and Audio.


  The Listen Notes catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Listen Notes'' developer surface includes support, pricing, engineering blog, authentication, documentation, and 34 more developer resources.'
plans:
- name: Listennotes Plans Pricing
  plan_count: 3
  slug: listennotes-plans-pricing
- name: Listennotes Price Estimates
  plan_count: 0
  slug: listennotes-price-estimates
random_paper: 8
rate_limits:
- limit_count: 8
  name: Listennotes Rate Limits
  slug: listennotes-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Listen Notes API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: listennotes-rules
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 71.5
    developer_ergonomics: 42.3
    discoverability: 78.6
    operational_transparency: 18.4
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 41.7
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/listennotes/listennotes-2026-07-25T225323.png
security:
- kind: authentication
  name: Listennotes Authentication
  slug: listennotes-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Listennotes Domain Security
  slug: listennotes-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: listennotes-fetch-podcast-details
  slug: listennotes-fetch-podcast-details
- name: listennotes-manage-podcast
  slug: listennotes-manage-podcast
- name: search
  slug: listennotes-search
slug: listennotes
tags:
- Podcasts
- Podcast Search
- Podcast Directory
- Search
- Audio
- Media
- Podcast Insights
website: https://www.listennotes.com/api/
---
