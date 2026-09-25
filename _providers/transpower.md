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
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: Developer resources for landowners and developers provided by Transpower New Zealand.
  name: Transpower Developer Portal
  slug: transpower-developer-portal
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/transpower/refs/heads/main/hosts/transpower-hosts.yml
  title: ''
  type: Hosts
  url: hosts/transpower-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/transpower/refs/heads/main/vendors/transpower-vendors.yml
  title: ''
  type: Vendors
  url: vendors/transpower-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.transpower.co.nz/user/register
- group: company
  title: ''
  type: Newsroom
  url: https://www.transpower.co.nz/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.transpower.co.nz/our-work/landowners-and-developers/developers
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/transpower/refs/heads/main/security/transpower-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transpower-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.transpower.co.nz/
- group: operate
  title: ''
  type: Support
  url: https://www.transpower.co.nz/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.transpower.co.nz/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.transpower.co.nz/privacy-policy
created: '2026-09-23'
description: Transpower New Zealand is the national electricity transmission system operator, owning and operating the high‑voltage grid that delivers power across the country. It ensures reliable supply, manages grid connections, and supports New Zealand’s transition to a low‑carbon, renewable energy future. The company provides market data, system operator services, and works closely with industry, government and communities to secure the nation’s electricity infrastructure.
layout: provider
modified: '2026-09-23'
name: Transpower New Zealand
nav: Providers
network: true
overview: 'Transpower New Zealand publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Grid, Infrastructure, and New Zealand.


  Transpower New Zealand''s developer surface includes signup flow, support, and 8 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - new-zealand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Transpower Domain Security
  slug: transpower-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: transpower
tags:
- Company
- Energy
- Grid
- Infrastructure
- New Zealand
website: https://www.transpower.co.nz/
---
