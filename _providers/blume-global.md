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
    well_known_catalog: true
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blume-global/refs/heads/main/security/blume-global-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/blume-global-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blume-global/refs/heads/main/well-known/blume-global-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blume-global-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blume-global/refs/heads/main/well-known/blume-global-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blume-global-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blume-global/refs/heads/main/hosts/blume-global-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blume-global-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blume-global/refs/heads/main/vendors/blume-global-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blume-global-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blumeglobal.com/terms-of-use/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blume-global/refs/heads/main/security/blume-global-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blume-global-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blume-global/refs/heads/main/security/blume-global-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blume-global-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blumeglobal.com
- group: company
  title: ''
  type: Blog
  url: https://www.blumeglobal.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.blumeglobal.com/about-us/
- group: operate
  title: ''
  type: Support
  url: https://www.blumeglobal.com/resource-center/
- group: company
  title: ''
  type: Newsroom
  url: https://www.blumeglobal.com/newsroom/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://forgeglobal.com/blume-global_stock/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: Blume Global provides a cloud-based supply chain visibility platform that empowers partners across logistics, manufacturing, and distribution to detect risks early, act decisively, and protect performance. Their solutions include real-time visibility, strategic sourcing, part quality management, and carrier integrations, helping enterprises streamline operations and improve decision-making throughout the supply chain.
image: https://www.blumeglobal.com/media/knzla54g/ship-passing-under-bridge-with-truck-on-it-arial-view.png?width=1200&height=630&v=1db52810a126c80
layout: provider
modified: '2026-09-29'
name: Blume Global
nav: Providers
network: true
overview: 'Blume Global is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain, Logistics, Software-as-a-Service, and Visibility.


  Blume Global''s developer surface includes engineering blog, documentation, support, and 10 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 0
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blume Global Domain Security
  slug: blume-global-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Blume Global Vulnerability Disclosure
  slug: blume-global-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: blume-global
tags:
- Company
- Supply Chain
- Logistics
- Software-as-a-Service
- Visibility
website: https://www.blumeglobal.com
---
