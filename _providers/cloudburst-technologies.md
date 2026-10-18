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
- description: Solutions offered by Cloudburst Technologies
  name: Solutions
  slug: solutions
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudburst-technologies/refs/heads/main/hosts/cloudburst-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudburst-technologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudburst-technologies/refs/heads/main/vendors/cloudburst-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudburst-technologies-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://cloudbursttechnologies.com/security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudburst-technologies/refs/heads/main/security/cloudburst-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudburst-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudbursttechnologies.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cloudbursttechnologies.com/solutions/
- group: company
  title: ''
  type: About
  url: https://cloudbursttechnologies.com/about/
coverage:
  checked: '2026-10-09'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://cloudbursttechnologies.com/solutions/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Cloudburst Technologies is a Texas‑based provider of next‑generation IT solutions, offering cloud, SaaS, unified communications, and security services. They help enterprises with network assessment, cloud migration, and digital transformation, delivering voice, data, and security products to Fortune‑100 companies and midsize businesses.
layout: provider
modified: '2026-10-09'
name: Cloudburst Technologies
nav: Providers
network: true
overview: 'Cloudburst Technologies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include IT Services, Cloud, Software-as-a-Service, Unified Communications, and Security.


  Cloudburst Technologies'' developer surface includes documentation and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudburst Technologies Domain Security
  slug: cloudburst-technologies-domain-security
  summary_line: TLSv1.3
slug: cloudburst-technologies
tags:
- IT Services
- Cloud
- Software-as-a-Service
- Unified Communications
- Security
website: https://cloudbursttechnologies.com/
---
