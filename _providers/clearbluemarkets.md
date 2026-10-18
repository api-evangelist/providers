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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Provides carbon market data and services; API details are not publicly documented.
  name: Clearbluemarkets API
  slug: clearbluemarkets-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearbluemarkets/refs/heads/main/hosts/clearbluemarkets-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearbluemarkets-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearbluemarkets/refs/heads/main/vendors/clearbluemarkets-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearbluemarkets-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearbluemarkets/refs/heads/main/security/clearbluemarkets-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearbluemarkets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clearbluemarkets.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.clearbluemarkets.com/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://www.clearbluemarkets.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.clearbluemarkets.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearbluemarkets.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearbluemarkets.com/privacy-policy
coverage:
  checked: '2026-10-09'
  detail: Documentation pages are rendered via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://www.clearbluemarkets.com/knowledge-base
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Clearbluemarkets provides carbon market intelligence and services, helping companies navigate compliance and voluntary carbon markets worldwide. Their platform offers market data, analytics, advisory, and tools for offset insight, position optimization, and EV credits aggregation, aiming to simplify decarbonization efforts and maximize financial benefits for clients.
image: https://www.clearbluemarkets.com/hubfs/CBM%20home.png
layout: provider
modified: '2026-10-08'
name: Clearbluemarkets
nav: Providers
network: true
overview: 'Clearbluemarkets is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CarbonMarkets, Analytics, Advisory, and CleanEnergy.


  Clearbluemarkets'' developer surface includes documentation, engineering blog, support, and 6 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clearbluemarkets Domain Security
  slug: clearbluemarkets-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: clearbluemarkets
tags:
- Company
- CarbonMarkets
- Analytics
- Advisory
- CleanEnergy
website: https://www.clearbluemarkets.com
---
