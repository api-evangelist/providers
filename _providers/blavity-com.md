---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/blavity-com/security/blavity-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/blavity-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/blavity-com/llms/blavity-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blavity-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/blavity-com/well-known/blavity-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blavity-com-security.txt
- group: agent
  href: https://artifacts.apis.io/blavity-com/well-known/blavity-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blavity-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blavity-com/hosts/blavity-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blavity-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blavity-com/vendors/blavity-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blavity-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blavity
- group: auth
  href: https://artifacts.apis.io/blavity-com/security/blavity-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blavity-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blavity-com/security/blavity-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blavity-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blavity.com
- group: company
  title: ''
  type: Blog
  url: https://blavity.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://blavity.com/developers
coverage:
  checked: '2026-10-22'
  detail: Blavity provides no public developer portal or API documentation.
  evidence:
  - status: error
    url: https://developer.blavity.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Blavity is a digital media company that creates content, experiences, and products for Black millennials and Gen Z. It operates a network of brands including Blavity News, AfroTech, Travel Noire, and More, delivering news, entertainment, culture, health, and lifestyle coverage. The company focuses on community-driven storytelling, technology, and entrepreneurship, fostering a platform for Black voices and creators across the internet.
image: https://blavity.com/images/logo-blavity.png
layout: provider
modified: '2026-10-22'
name: Blavity
nav: Providers
network: true
overview: 'Blavity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Digital, Community, and BlackCulture.


  Blavity''s developer surface includes engineering blog, documentation, and 10 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blavity Com Domain Security
  slug: blavity-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Blavity Com Vulnerability Disclosure
  slug: blavity-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: blavity-com
tags:
- Company
- Media
- Digital
- Community
- BlackCulture
website: https://blavity.com
---
