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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudcover/refs/heads/main/hosts/cloudcover-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudcover-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudcover/refs/heads/main/vendors/cloudcover-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudcover-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudcover/refs/heads/main/security/cloudcover-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudcover-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudcover.cc
- group: company
  title: ''
  type: Blog
  url: https://cloudcover.cc/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://cloudcover.cc/about-us/
- group: operate
  title: ''
  type: Support
  url: https://cloudcover.cc/contact/
- group: start
  title: ''
  type: PartnerPortal
  url: https://cloudcover.partnerportal.io/register
created: '2026-10-09'
description: Cloudcover provides a cyber safety and security platform that unifies security tools across enterprises, governments, and various industry sectors. Their AI‑secure edge compute solution, the C3C Trust Control Platform, offers real‑time risk quantification, automated policy enforcement, and comprehensive threat visibility. Cloudcover serves sectors including banking, broadcast, education, energy, healthcare, and public sector, delivering integrated protection, insurance, and compliance capabilities through a single coordinated platform.
layout: provider
modified: '2026-10-09'
name: Cloudcover
nav: Providers
network: true
overview: 'Cloudcover is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Artificial Intelligence, Cloud, and Platform.


  Cloudcover''s developer surface includes engineering blog, documentation, support, and 5 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudcover Domain Security
  slug: cloudcover-domain-security
  summary_line: TLSv1.3
slug: cloudcover
tags:
- Company
- Cybersecurity
- Artificial Intelligence
- Cloud
- Platform
website: https://cloudcover.cc
---
