---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://services-catalog.melorra.com/api
  baseurl_source: declared
  description: The Collections API from Melorra — 3 operation(s) for collections.
  name: Melorra Collections API
  slug: melorra-collections-api
- baseURL: https://services-catalog.melorra.com/api
  baseurl_source: declared
  description: The Product API from Melorra — 2 operation(s) for product.
  name: Melorra Product API
  slug: melorra-product-api
artifact_total: 9
common:
- group: operate
  href: https://artifacts.apis.io/melorra/rate-limits/melorra-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/melorra-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/melorra/overlays/melorra-catalog-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/melorra-catalog-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/melorra/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.melorra.com/
- group: other
  title: ''
  type: APICatalog
  url: https://www.melorra.com/.well-known/api-catalog
- group: agent
  href: https://artifacts.apis.io/melorra/well-known/melorra-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/melorra-well-known.yml
- group: agent
  href: https://artifacts.apis.io/melorra/llms/melorra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/melorra-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://www.melorra.com/.well-known/api-catalog
- group: operate
  title: ''
  type: Support
  url: https://www.melorra.com/contactus/
- group: start
  title: ''
  type: SignUp
  url: https://www.melorra.com/sign-in/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.melorra.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.melorra.com/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MelorraTech
- group: build
  href: https://artifacts.apis.io/melorra/packages/melorra-packages.yml
  title: ''
  type: Packages
  url: packages/melorra-packages.yml
- group: auth
  href: https://artifacts.apis.io/melorra/security/melorra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/melorra-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/melorra/plans/melorra-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/melorra-plans-pricing.yml
created: '2026-08-25'
description: Melorra is an Indian direct-to-consumer fine jewellery brand, founded in 2015 and operated by August Jewellery Pvt Ltd, selling lightweight, fashion-led gold, diamond, gemstone and silver jewellery designed for everyday and workwear rather than for weddings. It sells online at melorra.com and through an app and a network of experience centres, delivering BIS-hallmarked gold and IGI/SGL-certified stones across hundreds of Indian districts. Melorra runs a public, unauthenticated catalog API at services-catalog.melorra.com and — unusually for a retailer — publishes both an llms.txt and a machine-readable /.well-known/api-catalog document describing it, giving AI agents a documented path into a 21,000-product jewellery catalog. In January 2026 Senco Gold agreed to acquire a controlling 68% stake in August Jewellery.
image: https://assets.melorra.com/logo/favicon.ico
layout: provider
modified: '2026-08-25'
name: Melorra
nav: Providers
network: true
overview: 'Melorra publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Collections API and Product API. Tagged areas include Company, Jewellery, Retail, E-Commerce, and Product Catalog.


  The Melorra catalog on APIs.io includes 1 Spectral governance ruleset.


  Melorra''s developer surface includes documentation, support, signup flow, engineering blog, and 12 more developer resources.'
plans:
- name: Melorra Plans Pricing
  plan_count: 0
  slug: melorra-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Melorra Rate Limits
  slug: melorra-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Melorra API Rules
  rule_count: 46
  severity_counts:
    error: 43
    hint: 0
    info: 2
    warn: 1
  slug: melorra-rules
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 22.3
    developer_ergonomics: 30.4
    discoverability: 83.9
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 27.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 7
    mcp: derived
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
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/melorra/melorra-2026-09-02T150552.png
security:
- kind: authentication
  name: Melorra Authentication
  slug: melorra-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Melorra Domain Security
  slug: melorra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: melorra-browse-jewellery-catalog
  slug: melorra-browse-jewellery-catalog
- name: melorra-lookup-product-and-variants
  slug: melorra-lookup-product-and-variants
slug: melorra
tags:
- Company
- Jewellery
- Retail
- E-Commerce
- Product Catalog
- Direct to Consumer
- Fashion
- India
website: https://www.melorra.com/
---
