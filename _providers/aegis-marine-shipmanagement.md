---
access_model:
  confidence: high
  label: Anonymously readable, no signup, no key
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
    agentic_access: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-09-12'
api_count: 7
apis:
- baseURL: https://aegisships.com/wp-json
  baseurl_source: declared
  description: Anonymous, unauthenticated read access to the 15 published pages behind aegisships.com — Homepage, About and its Company Profile, CEO Note, Board of Directors and Operations children, Fleet, Fleet Sel
  name: Aegis Marine Shipmanagement Pages API
  slug: aegis-marine-shipmanagement-pages-api
- baseURL: https://aegisships.com/wp-json
  baseurl_source: declared
  description: Anonymous, unauthenticated read access to the media library behind aegisships.com — vessel and corporate photography, logos and page imagery with their generated size variants and MIME metadata. Verif
  name: Aegis Marine Shipmanagement Media API
  slug: aegis-marine-shipmanagement-media-api
- baseURL: https://aegisships.com/wp-json
  baseurl_source: declared
  description: Anonymous, unauthenticated read access to the two content taxonomies on aegisships.com — one category term (News) and 25 post tags. Every term reports a count of zero because the site publishes no pos
  name: Aegis Marine Shipmanagement Taxonomy API
  slug: aegis-marine-shipmanagement-taxonomy-api
- baseURL: https://aegisships.com/wp-json
  baseurl_source: declared
  description: Anonymous, unauthenticated cross-content search over aegisships.com, returning lightweight id, title, url, type and subtype records. Verified live at 15 searchable objects, all of them pages.
  name: Aegis Marine Shipmanagement Search API
  slug: aegis-marine-shipmanagement-search-api
- baseURL: https://aegisships.com/wp-json
  baseurl_source: declared
  description: Anonymous discovery metadata for aegisships.com — the self-describing route index (90 routes across 6 namespaces at capture), the registered content types and taxonomies, and the publication statuses.
  name: Aegis Marine Shipmanagement Discovery API
  slug: aegis-marine-shipmanagement-discovery-api
- baseURL: https://aegisships.com/wp-json
  baseurl_source: declared
  description: Public oEmbed 1.0 provider endpoint for aegisships.com URLs, returning embeddable rich metadata — title, provider, dimensions and iframe HTML — for any page on the site without parsing its markup.
  name: Aegis Marine Shipmanagement oEmbed API
  slug: aegis-marine-shipmanagement-oembed-api
- baseURL: https://aegisships.com/wp-json
  baseurl_source: declared
  description: Public Yoast SEO endpoint returning the rendered head metadata, and its parsed schema.org JSON-LD graph, for any aegisships.com URL — a structured-data view of every page without scraping the HTML. Pr
  name: Aegis Marine Shipmanagement SEO Metadata API
  slug: aegis-marine-shipmanagement-seo-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://aegisships.com/
- group: company
  title: ''
  type: About
  url: https://aegisships.com/about/
- group: other
  title: ''
  type: Services
  url: https://aegisships.com/services/
- group: company
  title: ''
  type: Newsroom
  url: https://aegisships.com/news/
- group: operate
  title: ''
  type: Contact
  url: https://aegisships.com/contact/
- group: company
  title: ''
  type: Partners
  url: https://aegisships.com/affiliate/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aegisships.com/privacy-policy-2/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aegisships.com/disclaimer/
- group: auth
  title: ''
  type: Authentication
  url: authentication/aegis-marine-shipmanagement-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aegis-marine-shipmanagement-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aegis-marine-shipmanagement-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aegis-marine-shipmanagement-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aegis-marine-shipmanagement-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aegis-marine-shipmanagement-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aegis-marine-shipmanagement-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aegis-marine-shipmanagement-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/aegis-marine-shipmanagement-packages.yml
- group: build
  title: ''
  type: Examples
  url: examples/aegis-marine-shipmanagement-examples.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aegis-marine-shipmanagement-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aegis-marine-shipmanagement-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aegis-marine-shipmanagement-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aegis-marine-shipmanagement-domain-security.yml
coverage:
  checked: '2026-09-09'
  detail: Aegis Marine Shipmanagement is a Georgetown, Guyana ship manager whose product is crude oil and LNG vessel operation under commercial contract, not software; every artifact in this repo was derived by API Evangelist from the WordPress core REST API behind its 2019-era marketing site, because the company itself publishes no OpenAPI, developer portal, SDK, changelog, status page or /.well-known/ document on any host.
  evidence:
  - status: 200
    url: https://aegisships.com/wp-json/
  - status: 404
    url: https://aegisships.com/openapi.json
  - status: 404
    url: https://aegisships.com/llms.txt
  - status: 404
    url: https://aegisships.com/.well-known/agent-card.json
  - status: 404
    url: https://aegisships.com/.well-known/security.txt
  - status: 200
    url: https://aegisships.com/wp-json/wp/v2/posts?per_page=1
  reason: not-a-software-company
  state: none
created: '2026-09-09'
description: 'Aegis Marine Shipmanagement Inc. is a privately owned marine vessel transportation and ship management company headquartered at 215 South Road and King Street, Lacytown, Georgetown, Guyana, with a secondary office in Brooklyn, New York. Founded in 2018 by Guyanese-American businessman Sean Clarke, it serves the oil and gas sector, operating crude oil tankers, liquefied natural gas tankers and offshore support service vessels on behalf of third-party owners, partners and investors. Its services span commercial, technical, safety and quality, and logistics ship management, delivered through partnerships with established marine service providers, and include vessel registration under various flags, technical inspection and marine engine spares, marine vessel chartering, commodity trader engagement, and crew management covering recruitment, familiarization, training, retention and career promotion. Aegis Marine Shipmanagement is a shipping operator rather than a software vendor.
  It publishes no developer portal, no API documentation, no SDKs and no commercial or partner-facing product API. The only machine-readable interface it exposes is the WordPress core REST content API behind its corporate website at aegisships.com, which is captured here for discovery purposes: it is anonymously readable, effectively read-only, and serves the marketing site''s own pages, media and taxonomy rather than any fleet, chartering or vessel-operations data.'
image: https://aegisships.com/wp-content/uploads/2018/11/cropped-favicon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: Aegis Marine Shipmanagement MCP Server
  slug: aegis-marine-shipmanagement-mcp-server
modified: '2026-09-09'
name: Aegis Marine Shipmanagement
nav: Providers
network: true
overview: 'Aegis Marine Shipmanagement publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Pages API, Media API, Taxonomy API, and 4 more. Tagged areas include Company, Shipping, Ship Management, Maritime, and Marine Transportation.


  Aegis Marine Shipmanagement''s developer surface includes authentication, code examples, and 21 more developer resources.'
plans:
- name: Aegis Marine Shipmanagement Plans Pricing
  plan_count: 0
  slug: aegis-marine-shipmanagement-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Aegis Marine Shipmanagement Rate Limits
  slug: aegis-marine-shipmanagement-rate-limits
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 16.4
    developer_ergonomics: 13.7
    discoverability: 81.5
    operational_transparency: 0.0
  previous_composite: 23.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Aegis Marine Shipmanagement Authentication
  slug: aegis-marine-shipmanagement-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aegis Marine Shipmanagement Domain Security
  slug: aegis-marine-shipmanagement-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: aegis-marine-shipmanagement
tags:
- Company
- Shipping
- Ship Management
- Maritime
- Marine Transportation
- Oil and Gas
- Crude Oil Tankers
- LNG
- Offshore
- Chartering
- Crew Management
- Logistics
- Guyana
- Content
website: https://aegisships.com/
---
