---
access_model:
  confidence: high
  label: Public read-only content API, no signup
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - authentication
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-09-08'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Denbury Resources Agentic Access
  operation_count: 12
  slug: denbury-resources-agentic-access
  summary_line: 12 operations
api_count: 5
apis:
- baseURL: https://www.denbury.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the Denbury Inc. corporate website page archive — 48 published pages covering carbon solutions, EOR operations, the CO2 pipeline network, sustainability and owne
  name: Denbury Resources Pages API
  slug: denbury-resources-pages-api
- baseURL: https://www.denbury.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the Denbury Inc. media library — 432 items including corporate presentations, ESG and corporate responsibility reports, PDFs and imagery — via the WordPress core
  name: Denbury Resources Media API
  slug: denbury-resources-media-api
- baseURL: https://www.denbury.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated full-text search over the Denbury Inc. website — 105 indexed objects at capture — returning lightweight result objects via the WordPress core REST API.
  name: Denbury Resources Search API
  slug: denbury-resources-search-api
- baseURL: https://www.denbury.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated access to the self-describing surface of the Denbury Inc. WordPress REST API — registered content types, taxonomies and category terms.
  name: Denbury Resources Discovery API
  slug: denbury-resources-discovery-api
- baseURL: https://www.denbury.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated oEmbed 1.0 endpoint for Denbury Inc. website URLs, served by WordPress core. Verified live against https://www.denbury.com/ on 2026-09-06.
  name: Denbury Resources oEmbed API
  slug: denbury-resources-oembed-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.denbury.com/
- group: operate
  title: ''
  type: Support
  url: https://www.denbury.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.denbury.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.denbury.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/denbury-resources
- group: company
  title: ''
  type: Twitter
  url: https://x.com/DenburyInc
- group: other
  title: ''
  type: ParentCompany
  url: https://corporate.exxonmobil.com/news/news-releases/2023/0713_exxonmobil-announces-acquisition-of-denbury
- group: other
  title: ''
  type: SECFilings
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000945764
- group: other
  title: ''
  type: Notes
  url: https://en.wikipedia.org/wiki/Denbury_Resources
- group: auth
  title: ''
  type: Authentication
  url: authentication/denbury-resources-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/denbury-resources-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/denbury-resources-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/denbury-resources-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/denbury-resources-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/denbury-resources-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/denbury-resources-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/denbury-resources-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/denbury-resources-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/denbury-resources-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/denbury-resources-domain-security.yml
- group: build
  title: ''
  type: Examples
  url: examples/denbury-resources-examples.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/denbury-resources-agentic-access.yml
created: '2024-12-03'
description: Denbury Resources (now Denbury Inc.) was an independent oil and natural gas company headquartered in Plano, Texas, focused on enhanced oil recovery (EOR) using carbon dioxide injection in mature oil fields across the Gulf Coast and Rocky Mountain regions, and on carbon capture, transport and sequestration through the largest CO2 pipeline network in the United States. ExxonMobil acquired Denbury in November 2023 and it now operates as a subsidiary inside ExxonMobil's Low Carbon Solutions business; Denbury filed a Form 15-12G to deregister its securities on 2023-11-22 and has filed nothing with the SEC since. Denbury is an energy operator rather than a software vendor and publishes no commercial or developer-facing product API, no developer portal, and no SDKs. The only machine-readable interface it exposes is the WordPress core REST content API behind its corporate website at www.denbury.com, which is captured here for discovery purposes and is anonymously readable but read-only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/denbury-resources.png
layout: provider
modified: '2026-09-06'
name: Denbury Resources
nav: Providers
network: true
overview: 'Denbury Resources publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Pages API, Media API, Search API, and 2 more. Tagged areas include Acquired, Carbon Capture, CO2 EOR, Energy, and Enhanced Oil Recovery.


  Denbury Resources'' developer surface includes support, authentication, code examples, and 20 more developer resources.'
plans:
- name: Denbury Resources Plans Pricing
  plan_count: 0
  slug: denbury-resources-plans-pricing
press:
- date: '2026-05-25'
  title: 'Denbury Inc: Carbon Solutions for a Sustainable Future'
  url: https://www.denbury.com/
- date: '2026-05-25'
  title: ExxonMobil announces acquisition of Denbury
  url: https://corporate.exxonmobil.com/news/news-releases/2023/0713_exxonmobil-announces-acquisition-of-denbury
- date: '2026-05-25'
  title: Denbury Inc.
  url: https://www.linkedin.com/company/denbury
- date: '2026-05-25'
  title: 'Exxon''s Acquisition Of Denbury: Neither One Is Worth $4.9 ...'
  url: https://www.forbes.com/sites/bryceerickson1/2023/07/21/exxons-acquisition-of-denbury-a-tale-of-two-businesses-and-neither-one-is-worth-49-billion/
- date: '2026-05-25'
  title: Denbury Resources
  url: https://en.wikipedia.org/wiki/Denbury_Resources
random_paper: 8
rate_limits:
- limit_count: 0
  name: Denbury Resources Rate Limits
  slug: denbury-resources-rate-limits
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 16.0
    developer_ergonomics: 18.5
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 23.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/denbury-resources/refs/heads/main/screenshots/denbury-resources-2026-06-20T175910.png
security:
- kind: authentication
  name: Denbury Resources Authentication
  slug: denbury-resources-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Denbury Resources Domain Security
  slug: denbury-resources-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: denbury-resources
tags:
- Acquired
- Carbon Capture
- CO2 EOR
- Energy
- Enhanced Oil Recovery
- ExxonMobil
- Oil and Gas
- Fortune 1000
- Content
- Carbon Sequestration
website: https://www.denbury.com/
---
