---
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
  scored_at: '2026-09-07'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Addis Energy Agentic Access
  operation_count: 21
  slug: addis-energy-agentic-access
  summary_line: 21 operations
api_count: 8
apis:
- baseURL: https://addisenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the Addis Energy news and press-coverage archive via the WordPress core REST API. Verified live at 13 published posts across 3 categories on 2026-09-07.
  name: Addis Energy Posts API
  slug: addis-energy-posts-api
- baseURL: https://addisenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the static pages of addisenergy.com — Home, Technology, News, Careers, Contact, Privacy Policy and Terms & Conditions. Verified live at 7 published pages on 2026
  name: Addis Energy Pages API
  slug: addis-energy-pages-api
- baseURL: https://addisenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the media library behind addisenergy.com — site photography, technology diagrams, team headshots and press assets with their generated size variants. Verified li
  name: Addis Energy Media API
  slug: addis-energy-media-api
- baseURL: https://addisenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated read access to the taxonomies that classify Addis Energy content — the category taxonomy (Press Coverage, Blog, Uncategorized) and the post_tag taxonomy. Verified live at 3 cat
  name: Addis Energy Taxonomy API
  slug: addis-energy-taxonomy-api
- baseURL: https://addisenergy.com/wp-json
  baseurl_source: declared
  description: 'Public, unauthenticated read access to the public author records behind addisenergy.com — the people credited on published news posts. Anonymous responses are limited to the WordPress view context: no'
  name: Addis Energy Users API
  slug: addis-energy-users-api
- baseURL: https://addisenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated cross-content search over addisenergy.com — posts and pages together — returning lightweight id / title / url / type / subtype records. Verified live at 20 searchable objects o
  name: Addis Energy Search API
  slug: addis-energy-search-api
- baseURL: https://addisenergy.com/wp-json
  baseurl_source: declared
  description: Public, unauthenticated discovery metadata for addisenergy.com — the self-describing route index (218 routes across 9 namespaces at capture), the registered content types and taxonomies, and the publi
  name: Addis Energy Discovery API
  slug: addis-energy-discovery-api
- baseURL: https://addisenergy.com/wp-json
  baseurl_source: declared
  description: Public oEmbed 1.0 provider endpoint for addisenergy.com URLs, returning embeddable rich metadata — title, author, thumbnail and iframe HTML — for any post or page on the site. Verified live (HTTP 200)
  name: Addis Energy oEmbed API
  slug: addis-energy-oembed-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://addisenergy.com/
- group: company
  title: ''
  type: About
  url: https://addisenergy.com/technology/
- group: other
  title: ''
  type: x-team
  url: https://addisenergy.com/team/
- group: company
  title: ''
  type: Blog
  url: https://addisenergy.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://addisenergy.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://addisenergy.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://addisenergy.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://addisenergy.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://addisenergy.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/addisenergy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/addis-energy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/addis-energy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/addis-energy-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/addis-energy-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/addis-energy-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/addis-energy-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/addis-energy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/addis-energy-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/addis-energy-llms.txt
- group: build
  title: ''
  type: Examples
  url: examples/addis-energy-examples.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/addis-energy-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/addis-energy-agentic-access.yml
created: '2026-09-07'
description: 'Addis Energy is a Somerville, Massachusetts deep-tech energy company founded in January 2025 out of research in the MIT Department of Materials Science and Engineering. It is developing Stimulated Geologic Ammonia — injecting nitrogen, water and engineered fluids into iron-rich subsurface rock and using the earth''s own heat and pressure as the reactor to produce ammonia underground rather than in a Haber-Bosch plant. Founded by Michael Alexander (CEO), Charlie Mitchell (COO), Iwnetim Abate (Chief Science Officer) and Yet-Ming Chiang (Chief Strategy Officer), it has raised an $8.3M seed round plus a $4.5M ARPA-E award, backed by Engine Ventures, At One Ventures, Pillar VC, Voyager VC, Blindspot Ventures and Emerson Collective. It is not a software vendor: no developer program, portal, SDKs or product API. The only machine-readable interface it exposes is the WordPress core REST content API behind addisenergy.com, captured here for discovery and anonymously readable but read-only.'
image: https://addisenergy.com/wp-content/uploads/fbrfg/apple-touch-icon.png
layout: provider
modified: '2026-09-07'
name: Addis Energy
nav: Providers
network: true
overview: 'Addis Energy publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 5 more. Tagged areas include Company, Energy, Clean Energy, Ammonia, and Climate Tech.


  Addis Energy''s developer surface includes engineering blog, authentication, code examples, and 20 more developer resources.'
plans:
- name: Addis Energy Plans Pricing
  plan_count: 0
  slug: addis-energy-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Addis Energy Rate Limits
  slug: addis-energy-rate-limits
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 16.0
    developer_ergonomics: 16.1
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 44.6
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Addis Energy Authentication
  slug: addis-energy-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Addis Energy Domain Security
  slug: addis-energy-domain-security
  summary_line: TLSv1.2
slug: addis-energy
tags:
- Company
- Energy
- Clean Energy
- Ammonia
- Climate Tech
- Deep Tech
- Geoscience
- Subsurface
- Materials Science
- Hydrogen
- Fertilizer
- Content
website: https://addisenergy.com/
---
