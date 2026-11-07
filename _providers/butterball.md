---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/butterball/hosts/butterball-hosts.yml
  title: ''
  type: Hosts
  url: hosts/butterball-hosts.yml
- group: other
  href: https://artifacts.apis.io/butterball/vendors/butterball-vendors.yml
  title: ''
  type: Vendors
  url: vendors/butterball-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.butterball.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.butterball.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/butterball/security/butterball-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/butterball-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.butterball.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.butterball.com/recipes
- group: start
  title: ''
  type: GettingStarted
  url: https://www.butterball.com/how-to
coverage:
  checked: '2026-10-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 530
    url: https://api.butterball.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Butterball is a leading turkey producer in the United States, offering a wide range of turkey products for holidays and everyday meals. The company provides recipes, cooking guides, and product information through its website, helping consumers prepare delicious turkey dishes. Butterball emphasizes quality, sustainability, and community involvement, with resources for food safety, cooking tips, and charitable initiatives.
layout: provider
modified: '2026-10-06'
name: Butterball
nav: Providers
network: true
overview: 'Butterball is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Consumer Goods, Retail, and Turkey.


  Butterball''s developer surface includes documentation, getting-started guide, and 6 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - turkey
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 12.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/butterball/butterball-2026-11-03T122822.png
security:
- kind: domain-security
  name: Butterball Domain Security
  slug: butterball-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: butterball
tags:
- Company
- Food
- Consumer Goods
- Retail
- Turkey
website: https://www.butterball.com
---
