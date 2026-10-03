---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
  score: 6.5
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API documentation is behind Cloudflare Access login, no machine-readable spec discovered.
  name: AstroLab API
  slug: astrolab-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astrolab/refs/heads/main/security/astrolab-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/astrolab-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astrolab/refs/heads/main/well-known/astrolab-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/astrolab-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astrolab/refs/heads/main/well-known/astrolab-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/astrolab-docs-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/astrolab/refs/heads/main/well-known/astrolab-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astrolab-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/astrolab/refs/heads/main/hosts/astrolab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astrolab-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/astrolab/refs/heads/main/vendors/astrolab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astrolab-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.astrolab.space/login/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astrolab/refs/heads/main/security/astrolab-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/astrolab-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astrolab/refs/heads/main/security/astrolab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astrolab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.astrolab.space/
- group: docs
  title: ''
  type: Documentation
  url: https://www.astrolab.space/about/
- group: company
  title: ''
  type: Blog
  url: https://www.astrolab.space/news/
- group: operate
  title: ''
  type: Support
  url: https://www.astrolab.space/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.astrolab.space/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astrolab.space/legal/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Astrolab designs, builds, and operates planetary surface mobility platforms and infrastructure for sustained human and commercial activities on the Moon and Mars. Their flagship rovers, FLIP and FLEX, aim to deliver payloads, power, and logistics support for lunar missions, with upcoming launches scheduled for 2026 and beyond.
layout: provider
modified: '2026-09-26'
name: AstroLab
nav: Providers
network: true
overview: 'AstroLab publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Robotics, Lunar, and Exploration.


  AstroLab''s developer surface includes documentation, engineering blog, support, and 12 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 18.4
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
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Astrolab Domain Security
  slug: astrolab-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Astrolab Vulnerability Disclosure
  slug: astrolab-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: astrolab
tags:
- Company
- Space
- Robotics
- Lunar
- Exploration
website: https://www.astrolab.space/
---
