---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Trove Agentic Access
  operation_count: 14
  slug: trove-agentic-access
  summary_line: 14 operations
api_count: 2
apis:
- baseURL: https://api.trove.nla.gov.au/v3
  baseurl_source: declared
  description: Contributors
  name: Trove Contributor API
  slug: trove-contributor-api
- baseURL: https://api.trove.nla.gov.au/v3
  baseurl_source: declared
  description: Lists
  name: Trove List API
  slug: trove-list-api
- baseURL: https://api.trove.nla.gov.au/v3
  baseurl_source: declared
  description: Newspapers and Gazettes
  name: Trove Newspaper API
  slug: trove-newspaper-api
- baseURL: https://api.trove.nla.gov.au/v3
  baseurl_source: declared
  description: People and Organisations
  name: Trove People API
  slug: trove-people-api
- baseURL: https://api.trove.nla.gov.au/v3
  baseurl_source: declared
  description: Search
  name: Trove Search API
  slug: trove-search-api
- baseURL: https://api.trove.nla.gov.au/v3
  baseurl_source: declared
  description: Works
  name: Trove Work API
  slug: trove-work-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/trove/agentic-access/trove-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trove-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/trove/rate-limits/trove-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trove-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/trove/rules/trove-rules.yml
  title: ''
  type: Spectral
  url: rules/trove-rules.yml
- group: design
  href: https://artifacts.apis.io/trove/json-ld/trove-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trove-context.jsonld
- group: design
  href: https://artifacts.apis.io/trove/vocabulary/trove-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trove-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/trove/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/trove/data-model/trove-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trove-data-model.yml
- group: operate
  href: https://artifacts.apis.io/trove/changelog/trove-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/trove-changelog.yml
- group: design
  href: https://artifacts.apis.io/trove/conventions/trove-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trove-conventions.yml
- group: operate
  href: https://artifacts.apis.io/trove/lifecycle/trove-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/trove-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/trove/lifecycle/trove-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trove-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/trove/errors/trove-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trove-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trove/conformance/trove-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trove-conformance.yml
- group: other
  href: https://artifacts.apis.io/trove/overlays/trove-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trove-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/trove/well-known/trove-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trove-well-known.yml
- group: other
  href: https://artifacts.apis.io/trove/hosts/trove-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trove-hosts.yml
- group: other
  href: https://artifacts.apis.io/trove/vendors/trove-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trove-vendors.yml
- group: auth
  href: https://artifacts.apis.io/trove/authentication/trove-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trove-authentication.yml
- group: auth
  href: https://artifacts.apis.io/trove/security/trove-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trove-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trove.nla.gov.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://trove.nla.gov.au/about/create-something
- group: operate
  title: ''
  type: Support
  url: https://trove.nla.gov.au/help
- group: operate
  title: ''
  type: Contact
  url: https://trove.nla.gov.au/about/contact-us
- group: company
  title: ''
  type: Blog
  url: https://trove.nla.gov.au/news?type=trove_blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://trove.nla.gov.au/about/what-trove/technical-ecosystem/trove-system-updates
- group: start
  title: ''
  type: Login
  url: https://login.nla.gov.au/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trove.nla.gov.au/about/policies/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trove.nla.gov.au/about/policies/privacy
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Trove is the National Library of Australia's discovery service. It gives a single point of entry to more than 14 billion digital items from hundreds of Australian libraries, museums, galleries, media, government and community partners. Its public API (version 3) returns machine-readable search results and metadata records for digitised newspaper and gazette articles, magazines and newsletters, lists, works (books, images, maps, music, sound, video, archives, journal articles), people and organisations, newspaper titles and contributors. A free Trove account and an API key are required.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trove.png
json_schemas:
- name: article
  property_count: 31
  slug: trove-article
- name: articleTitle
  property_count: 11
  slug: trove-article-title
- name: contributor
  property_count: 11
  slug: trove-contributor
- name: list
  property_count: 18
  slug: trove-list
- name: people
  property_count: 25
  slug: trove-people
- name: work
  property_count: 36
  slug: trove-work
jsonld:
- class_count: 18
  name: Trove Context
  property_count: 95
  slug: trove-context
layout: provider
modified: '2026-10-21'
name: Trove
nav: Providers
network: true
overview: 'Trove publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Contributor API, List API, Newspaper API, and 3 more. Tagged areas include News, Public APIs, Library, Cultural Heritage, and Digitised Newspapers.


  The Trove catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Trove''s developer surface includes changelog, authentication, support, engineering blog, and 25 more developer resources.'
plans:
- name: Trove Plans Pricing
  plan_count: 0
  slug: trove-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Trove Rate Limits
  slug: trove-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Trove API Rules
  rule_count: 57
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 3
  slug: trove-rules
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 59.0
    developer_ergonomics: 41.1
    discoverability: 73.2
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/trove/trove-2026-06-20T195747.png
security:
- kind: authentication
  name: Trove Authentication
  slug: trove-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Trove Domain Security
  slug: trove-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: trove-browse-magazines
  slug: trove-browse-magazines
- name: trove-browse-newspaper-titles
  slug: trove-browse-newspaper-titles
- name: trove-find-contributors
  slug: trove-find-contributors
- name: trove-search-collection
  slug: trove-search-collection
slug: trove
tags:
- News
- Public APIs
- Library
- Cultural Heritage
- Digitised Newspapers
- Archives
- Open Data
- Australia
- Search
website: https://trove.nla.gov.au/
---
