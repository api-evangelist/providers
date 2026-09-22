---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://agriaku.com/
- group: company
  title: ''
  type: About
  url: https://agriaku.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://agriaku.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://agriaku.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://agriaku.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agriaku.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agriaku.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Agriaku
- group: company
  title: ''
  type: Partners
  url: https://agriaku.com/mitra/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agriaku/refs/heads/main/security/agriaku-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agriaku-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agriaku/refs/heads/main/plans/agriaku-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agriaku-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agriaku/refs/heads/main/rate-limits/agriaku-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agriaku-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agriaku/refs/heads/main/llms/agriaku-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agriaku-llms.txt
coverage:
  checked: '2026-09-12'
  detail: AgriAku ships only first-party end-user apps (Mitra, Logistik Kurir, a vendor platform) - there is no developer portal, API reference or published contract on agriaku.com or on any of the 19 subdomains in its certificate-transparency record, every spec path 404s, and the one API host it ever named, api.agriaku.com, is now a dangling CNAME to an AWS load balancer that no longer resolves.
  evidence:
  - status: 404
    url: https://agriaku.com/openapi.json
  - status: 404
    url: https://agriaku.com/.well-known/api-catalog
  - status: 401
    url: https://agriaku.com/wp-json/
  - status: 404
    url: https://agriaku.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: 'AgriAku (PT Agriaku Digital Indonesia) is a Jakarta-based agritech company founded in 2021 that digitizes the distribution of agricultural inputs - seeds, fertilizers, crop protection, nutrients and farm tools - to Indonesia''s network of independent farm-supply shops (toko tani). Partner shops order from a catalog of more than 15,000 agricultural products through the AgriAku Mitra Android app, while separate vendor, seller and courier applications cover the rest of the supply chain. The company reports more than 23,390 partners across Indonesia and has raised roughly USD 46M from Alpha JWC Ventures, Go-Ventures and MDI Ventures. AgriAku operates no public developer program: every API host it runs is a private backend for its own first-party mobile and web applications.'
image: https://agriaku.com/wp-content/uploads/2021/06/Final-Logo-Highres-full-color-min.png
layout: provider
modified: '2026-09-12'
name: AgriAku
nav: Providers
network: true
overview: 'AgriAku is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, E-Commerce, and Marketplace.


  AgriAku''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Agriaku Plans Pricing
  plan_count: 0
  slug: agriaku-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Agriaku Rate Limits
  slug: agriaku-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 11.0
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agriaku Domain Security
  slug: agriaku-domain-security
  summary_line: TLSv1.3
slug: agriaku
tags:
- Company
- Agriculture
- AgTech
- E-Commerce
- Marketplace
- Supply Chain
- Distribution
- Indonesia
- B2B
- Mobile
website: https://agriaku.com/
---
