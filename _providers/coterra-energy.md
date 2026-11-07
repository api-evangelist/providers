---
access_model:
  confidence: high
  label: No public API surface — nothing to onboard to
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.coterra.com/'', ''status'': 200, ''note'': ''five-page corporate stub (home, contact, owners, legal notice, safety handbooks) carrying the notice "Coterra completed its merger with Devon Energy on May 7, 2026" (probed 2026-09-19)''}'
  - '{''url'': ''https://developer.coterra.com/'', ''status'': 0, ''note'': ''does not resolve in DNS — the previously recorded developer portal never existed''}'
  - '{''url'': ''https://api.coterra.com/'', ''status'': 0, ''note'': ''does not resolve in DNS — the previously recorded API base never existed''}'
  - '{''url'': ''https://www.coterra.com/openapi.json'', ''status'': 404, ''note'': ''no OpenAPI on the corporate host''}'
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Machine-readable filing data for Coterra Energy is available from the U.S. Securities and Exchange Commission, not from the company. The SEC EDGAR submissions API returns the full filing history for C
  name: SEC EDGAR Filings (Coterra Energy, CIK 858470)
  slug: sec-edgar-filings
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/coterra-energy/plans/coterra-energy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coterra-energy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/coterra-energy/rate-limits/coterra-energy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coterra-energy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/coterra-energy/finops/coterra-energy-finops.yml
  title: ''
  type: FinOps
  url: finops/coterra-energy-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.coterra.com
- group: other
  title: ''
  type: Successor
  url: https://www.devonenergy.com
- group: company
  title: ''
  type: News
  url: https://www.devonenergy.com/news/2026/Devon-Energy-and-Coterra-Energy-Complete-Merger
- group: operate
  title: ''
  type: Contact
  url: https://www.coterra.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coterra.com/legal-notice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coterra-energy
- group: build
  href: https://artifacts.apis.io/coterra-energy/packages/coterra-energy-packages.yml
  title: ''
  type: Packages
  url: packages/coterra-energy-packages.yml
- group: other
  href: https://artifacts.apis.io/coterra-energy/regulatory/coterra-energy-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/coterra-energy-regulatory-posture.yml
- group: agent
  href: https://artifacts.apis.io/coterra-energy/llms/coterra-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coterra-energy-llms.txt
- group: auth
  href: https://artifacts.apis.io/coterra-energy/security/coterra-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coterra-energy-domain-security.yml
coverage:
  checked: '2026-09-19'
  detail: Coterra Energy was absorbed into Devon Energy on 2026-05-07 and deregistered its shares (Form 15-12G, 2026-05-19); coterra.com is now a five-page holding site for interest owners whose own WordPress page index lists only home, contact-us, legal-notice, owners and safety-handbooks, investors.coterra.com 301s to investors.devonenergy.com, and the developer.coterra.com and api.coterra.com hosts this profile previously recorded do not resolve in DNS at all.
  evidence:
  - status: 200
    url: https://www.coterra.com/
  - status: 200
    url: https://www.coterra.com/wp-json/wp/v2/pages?per_page=100
  - status: 0
    url: https://developer.coterra.com/
  - status: 0
    url: https://api.coterra.com/
  - status: 404
    url: https://www.coterra.com/openapi.json
  - status: 403
    url: https://www.coterra.com/.well-known/api-catalog
  - status: 301
    url: https://investors.coterra.com/
  - status: 404
    url: https://api.github.com/orgs/coterra-energy
  reason: defunct
  state: none
created: '2026-04-19'
description: 'Coterra Energy Inc. (formerly Cabot Oil & Gas, combined with Cimarex Energy in October 2021) was a Houston-headquartered independent oil and natural gas exploration and production company with positions in the Permian Basin, the Marcellus Shale and the Anadarko Basin. On May 7, 2026 Coterra completed an all-stock merger with Devon Energy; the combined company operates as Devon Energy (NYSE: DVN), Coterra''s shares were deregistered (Form 15-12G filed 2026-05-19) and investors.coterra.com now redirects to investors.devonenergy.com. The coterra.com site has been reduced to a five-page holding site for interest owners. Coterra never operated a public developer program or API: owner statements are delivered through EnergyLink and production data through PDS Energy, both third-party platforms. The only programmatic access to Coterra data is the SEC''s own EDGAR API, listed here as a clearly labeled third-party government API.'
finops:
- has_sources: true
  method: generated
  name: Coterra Energy Finops
  primary_unit: ''
  service_category: Oil & Gas Exploration and Production
  slug: coterra-energy-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coterra-energy.png
layout: provider
modified: '2026-09-19'
name: Coterra Energy
nav: Providers
network: true
overview: 'Coterra Energy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Oil and Gas, Exploration and Production, Natural Gas, and Fortune 1000.


  Coterra Energy''s developer surface includes product news and 12 more developer resources.'
plans:
- name: Coterra Energy Plans Pricing
  plan_count: 0
  slug: coterra-energy-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Coterra Energy Rate Limits
  slug: coterra-energy-rate-limits
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  previous_composite: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/coterra-energy/coterra-energy-2026-06-20T175054.png
security:
- kind: domain-security
  name: Coterra Energy Domain Security
  slug: coterra-energy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: coterra-energy
tags:
- Energy
- Oil and Gas
- Exploration and Production
- Natural Gas
- Fortune 1000
- Merger
- Defunct
website: https://www.coterra.com
---
