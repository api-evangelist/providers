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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitwiseassetmanagement/refs/heads/main/hosts/bitwiseassetmanagement-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitwiseassetmanagement-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitwiseassetmanagement/refs/heads/main/vendors/bitwiseassetmanagement-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitwiseassetmanagement-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://experts.bitwiseinvestments.com/sign-up
- group: company
  title: ''
  type: Newsroom
  url: https://bitwiseinvestments.com/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bitwiseinvestments.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitwiseassetmanagement/refs/heads/main/security/bitwiseassetmanagement-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitwiseassetmanagement-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitwiseinvestments.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitwiseinvestments.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitwiseinvestments.com/privacy-policy
- group: other
  title: ''
  type: Sitemap
  url: https://bitwiseinvestments.com/sitemap
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI or other machine‑readable contract found on the website or API subdomains.
  evidence:
  - status: 200
    url: https://bitwiseinvestments.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bitwise Asset Management provides crypto index funds and ETFs, offering institutional and retail investors diversified exposure to the cryptocurrency market. The firm delivers research, portfolio simulation tools, and a suite of crypto‑focused investment products, operating from its headquarters in the United States and serving global clients through its website and investor portals.
image: https://www.datocms-assets.com/62087/1674679915-insights.png?auto=format&fit=max&w=1200
layout: provider
modified: '2026-09-28'
name: Bitwiseassetmanagement
nav: Providers
network: true
overview: 'Bitwiseassetmanagement is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, ETFs, Investment, and Asset Management.


  Bitwiseassetmanagement''s developer surface includes signup flow, documentation, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 0
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.0
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitwiseassetmanagement Domain Security
  slug: bitwiseassetmanagement-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitwiseassetmanagement
tags:
- Company
- Crypto
- ETFs
- Investment
- Asset Management
website: https://bitwiseinvestments.com
---
