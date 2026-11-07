---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
  score: 25.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Besot Com Agentic Access
  operation_count: 8
  slug: besot-com-agentic-access
  summary_line: 8 operations
api_count: 5
apis:
- baseURL: https://thebesot.com/catalogue
  baseurl_source: declared
  description: The Artists API from besot — 1 operation(s) for artists.
  name: besot Artists API
  slug: besot-com-artists-api
- baseURL: https://bestaffiliateprograms.cc/v1
  baseurl_source: declared
  description: The Categories API from besot — 1 operation(s) for categories.
  name: besot Categories API
  slug: besot-com-categories-api
- baseURL: https://thebesot.com/catalogue
  baseurl_source: declared
  description: The Collections API from besot — 2 operation(s) for collections.
  name: besot Collections API
  slug: besot-com-collections-api
- baseURL: https://thebesot.com/catalogue
  baseurl_source: declared
  description: The Designers API from besot — 1 operation(s) for designers.
  name: besot Designers API
  slug: besot-com-designers-api
- baseURL: https://thebesot.com/catalogue
  baseurl_source: declared
  description: The Facets API from besot — 1 operation(s) for facets.
  name: besot Facets API
  slug: besot-com-facets-api
- baseURL: https://bestaffiliateprograms.cc/v1
  baseurl_source: declared
  description: The Networks API from besot — 1 operation(s) for networks.
  name: besot Networks API
  slug: besot-com-networks-api
- baseURL: https://thebesot.com/catalogue
  baseurl_source: declared
  description: The Pieces API from besot — 2 operation(s) for pieces.
  name: besot Pieces API
  slug: besot-com-pieces-api
- baseURL: https://bestaffiliateprograms.cc/v1
  baseurl_source: declared
  description: The Programs API from besot — 2 operation(s) for programs.
  name: besot Programs API
  slug: besot-com-programs-api
- baseURL: https://thebesot.com/catalogue
  baseurl_source: declared
  description: The Search API from besot — 1 operation(s) for search.
  name: besot Search API
  slug: besot-com-search-api
- baseURL: https://bestaffiliateprograms.cc/v1
  baseurl_source: declared
  description: The Stats API from besot — 1 operation(s) for stats.
  name: besot Stats API
  slug: besot-com-stats-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/besot-com/llms/besot-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/besot-com-llms.txt
- group: other
  href: https://artifacts.apis.io/besot-com/hosts/besot-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/besot-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/besot-com/vendors/besot-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/besot-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://besot.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://besot.com/privacy
- group: auth
  href: https://artifacts.apis.io/besot-com/security/besot-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/besot-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://besot.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://besot.com/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Besot is a catalog of fandom style across the resale market, indexing resale listings for clothing designed, worn, or inspired by notable people. It provides lineage and source information for each piece, offering a searchable database for fans and collectors to discover the origins of fashion items.
image: https://besot.com/opengraph-image?2ea24f03543d1884
layout: provider
modified: '2026-11-02'
name: besot
nav: Providers
network: true
overview: 'besot publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Artists API, Categories API, Collections API, and 7 more. Tagged areas include Company, Fashion, Resale, Catalog, and Fandom.


  The besot catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 17
rate_limits:
- limit_count: 0
  name: Besot Com Rate Limits
  slug: besot-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 70
  extends:
  - spectral:oas
  name: besot API Rules
  rule_count: 29
  severity_counts:
    error: 27
    hint: 0
    info: 1
    warn: 1
  slug: besot-com-rules
scopes:
- name: Besot Com Scopes
  scope_count: 0
  slug: besot-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 29.9
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 40.0
      total: 10
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Besot Com Authentication
  slug: besot-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Besot Com Domain Security
  slug: besot-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: search-pieces
  slug: besot-com-search-pieces
slug: besot-com
tags:
- Company
- Fashion
- Resale
- Catalog
- Fandom
- Clothing
website: https://besot.com/
---
