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
    delegated_identity: served
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
  score: 14.4
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aryakanetworks/refs/heads/main/llms/aryakanetworks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aryakanetworks-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aryakanetworks/refs/heads/main/well-known/aryakanetworks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aryakanetworks-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aryakanetworks/refs/heads/main/hosts/aryakanetworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aryakanetworks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aryakanetworks/refs/heads/main/vendors/aryakanetworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aryakanetworks-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aryaka.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aryaka.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.aryaka.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.aryaka.com/about-us/leadership/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aryaka.com/get-started/unified-sase/
- group: company
  title: ''
  type: Blog
  url: https://www.aryaka.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aryaka.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aryakanetworks/refs/heads/main/security/aryakanetworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aryakanetworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aryaka.com
coverage:
  checked: 2026-09-26
  detail: Documentation at https://docs.aryaka.com is rendered via JavaScript, preventing machine-readable contract extraction.
  evidence:
  - status: 200
    url: https://docs.aryaka.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Aryaka Networks offers a Unified Secure Access Service Edge (SASE) platform delivered as a service, combining networking and security functions such as SD‑WAN, zero‑trust network access, next‑gen firewall, and multi‑cloud SaaS acceleration. The solution is targeted at enterprise customers seeking to modernize, scale, and secure global WAN connectivity without trade‑offs between performance and protection.
image: https://www.aryaka.com/wp-content/uploads/2025/11/Home-Page-Feature-Image.webp
layout: provider
modified: '2026-09-26'
name: Aryakanetworks
nav: Providers
network: true
overview: 'Aryakanetworks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include SASE, SD-WAN, Network Security, Cloud Acceleration, and Enterprise Networking.


  Aryakanetworks'' developer surface includes getting-started guide, engineering blog, documentation, and 10 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 15.5
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
    developer_ergonomics: 23.8
    discoverability: 58.9
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aryakanetworks Domain Security
  slug: aryakanetworks-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aryakanetworks
tags:
- SASE
- SD-WAN
- Network Security
- Cloud Acceleration
- Enterprise Networking
website: https://www.aryaka.com
---
