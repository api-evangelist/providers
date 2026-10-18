---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Token-authenticated POST endpoints (get-products.php, get-os.php, buy-vps.php, upgrade-vps.php, reinstall-vps.php, vps-action.php, get-user-info.php) for managing TaiVPS VPS services and account balan
  name: TaiVPS API
  slug: taivps-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taivps/refs/heads/main/authentication/taivps-authentication.yml
  title: ''
  type: Authentication
  url: authentication/taivps-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/taivps/refs/heads/main/llms/taivps-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/taivps-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/taivps/refs/heads/main/hosts/taivps-hosts.yml
  title: ''
  type: Hosts
  url: hosts/taivps-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/taivps/refs/heads/main/vendors/taivps-vendors.yml
  title: ''
  type: Vendors
  url: vendors/taivps-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://taivps.net/blog/nat-vps-la-gi-
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/taivps/refs/heads/main/security/taivps-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/taivps-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://taivps.net/
- group: docs
  title: ''
  type: Documentation
  url: https://taivps.net/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://taivps.net/store-vps
- group: start
  title: ''
  type: SignUp
  url: https://taivps.net/register
- group: start
  title: ''
  type: Login
  url: https://taivps.net/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taivps.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taivps.net/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://taivps.net/contact
coverage:
  checked: '2026-10-09'
  detail: TaiVPS documents 7 token-authenticated POST endpoints under https://taivps.net/api/*.php only as a Vietnamese HTML page; no OpenAPI is served on taivps.net or api.taivps.net and the docs generator found no METHOD+path pairs to gate.
  evidence:
  - status: 200
    url: https://taivps.net/api-docs
  - status: 200
    url: https://taivps.net/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: TaiVPS (taivps.net) is a Vietnamese hosting provider selling Cloud VPS, VMware Windows/Linux VPS, web hosting, reseller hosting and domain names. It publishes a Vietnamese-language API reference (taivps.net/api-docs) describing token-authenticated POST endpoints under https://taivps.net/api/ for listing products and OS images, buying, upgrading, reinstalling and controlling VPS instances, and reading account balance.
image: https://taivps.net/assets/images/anhbia.jpg
layout: provider
modified: '2026-10-09'
name: TaiVPS
nav: Providers
network: true
overview: 'TaiVPS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud VPS, Web Hosting, Reseller Hosting, and Domains.


  TaiVPS''s developer surface includes authentication, engineering blog, documentation, pricing, signup flow, support, and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 73.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - vietnam
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 21.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/taivps/refs/heads/main/screenshots/taivps-2026-10-11T130618.png
security:
- kind: authentication
  name: Taivps Authentication
  slug: taivps-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Taivps Domain Security
  slug: taivps-domain-security
  summary_line: TLSv1.3 · DMARC
slug: taivps
tags:
- Company
- Cloud VPS
- Web Hosting
- Reseller Hosting
- Domains
- Infrastructure
- Vietnam
website: https://taivps.net/
---
