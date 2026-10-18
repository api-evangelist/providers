---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crytek/refs/heads/main/llms/crytek-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crytek-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crytek/refs/heads/main/well-known/crytek-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crytek-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crytek/refs/heads/main/hosts/crytek-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crytek-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crytek/refs/heads/main/vendors/crytek-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crytek-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crytek/refs/heads/main/packages/crytek-packages.yml
  title: ''
  type: SDKs
  url: packages/crytek-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crytek/refs/heads/main/packages/crytek-packages.yml
  title: ''
  type: Packages
  url: packages/crytek-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.crytek.com/news/hunt-showdown-update-112-delivers-new-player-onboarding-tutorials-adds-questlines-with-all-new-rewards-and-more
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CRYTEK
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crytek/refs/heads/main/security/crytek-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crytek-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crytek.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.crytek.com/cryengine
- group: operate
  title: ''
  type: Support
  url: https://www.crytek.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.crytek.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crytek.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crytek.com/privacy-policy
coverage:
  checked: '2026-10-11'
  detail: Crytek's website provides no developer API documentation or program.
  evidence:
  - status: 200
    url: https://www.crytek.com
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: 'Crytek is a German video game developer and publisher, known for creating the CryEngine and titles such as Far Cry, Crysis, and Hunt: Showdown. The company focuses on cutting‑edge graphics technology and immersive gaming experiences, operating globally with offices in Frankfurt, Berlin, and international studios. Crytek provides developer tools, game updates, and community support through its official website and various digital platforms.'
image: https://www.crytek.com/static/logo.png
layout: provider
modified: '2026-10-11'
name: Crytek
nav: Providers
network: true
overview: 'Crytek is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video Games, GameDevelopment, CryEngine, and Gaming.


  Crytek''s developer surface includes getting-started guide, documentation, support, engineering blog, and 11 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 55.4
    operational_transparency: 5.3
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
  name: Crytek Domain Security
  slug: crytek-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crytek
tags:
- Company
- Video Games
- GameDevelopment
- CryEngine
- Gaming
website: https://www.crytek.com
---
