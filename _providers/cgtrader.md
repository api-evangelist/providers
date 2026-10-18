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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cgtrader/refs/heads/main/well-known/cgtrader-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cgtrader-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cgtrader/refs/heads/main/well-known/cgtrader-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cgtrader-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cgtrader/refs/heads/main/hosts/cgtrader-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cgtrader-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cgtrader/refs/heads/main/vendors/cgtrader-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cgtrader-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cgtrader.com/pages/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://help.cgtrader.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cgtrader.com/pages/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.cgtrader.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cgtrader.com/hc/en-us/sections/360004404518-Getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.cgtrader.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cgtrader/refs/heads/main/security/cgtrader-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cgtrader-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cgtrader/refs/heads/main/security/cgtrader-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cgtrader-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cgtrader.com/
coverage:
  checked: '2026-10-08'
  detail: No public API documentation or machine-readable contract is available; attempts to access https://api.cgtrader.com/mcp returned 403.
  evidence:
  - status: 403
    url: https://api.cgtrader.com/mcp
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Cgtrader operates a large online marketplace for 3D models, offering designers a platform to sell, buy, and share 3D assets for printing, rendering, and game development. The site features AI‑assisted model generation, a subscription model for frequent users, and extensive categories ranging from vehicles to characters. It serves a global community of creators and manufacturers, providing tools for model upload, licensing, and marketplace analytics.
image: https://assets.cgtrader.com/assets/branding/avatar-d9199bb4f8e1938e1bd58ba746948741ce297b4174526fa3a18eefd0d5bbc03f.jpg
layout: provider
modified: '2026-10-07'
name: Cgtrader
nav: Providers
network: true
overview: 'Cgtrader is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, 3DModels, Artificial Intelligence, and Community.


  Cgtrader''s developer surface includes support, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cgtrader Domain Security
  slug: cgtrader-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cgtrader Vulnerability Disclosure
  slug: cgtrader-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cgtrader
tags:
- Company
- Marketplace
- 3DModels
- Artificial Intelligence
- Community
website: https://www.cgtrader.com/
---
