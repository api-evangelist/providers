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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visiba-care/refs/heads/main/llms/visiba-care-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/visiba-care-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visiba-care/refs/heads/main/well-known/visiba-care-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/visiba-care-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/visiba-care/refs/heads/main/hosts/visiba-care-hosts.yml
  title: ''
  type: Hosts
  url: hosts/visiba-care-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/visiba-care/refs/heads/main/vendors/visiba-care-vendors.yml
  title: ''
  type: Vendors
  url: vendors/visiba-care-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.visibacare.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.visibagroup.com/en/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.visibagroup.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VisibaCare
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visiba-care/refs/heads/main/security/visiba-care-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/visiba-care-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.visibacare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.visibagroup.com/en/about-us
- group: company
  title: ''
  type: AboutUs
  url: https://www.visibagroup.com/en/about-us
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.visibacare.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Visiba Care provides intelligent software solutions for digital transformation in healthcare, enabling organisations to deliver resource‑efficient, high‑quality care. Their platform supports patient triage, scheduling, and remote consultations, helping providers improve access, reduce costs, and enhance outcomes across Sweden and other markets.
image: https://www.visibagroup.com/hubfs/New%20brand%20profile%202022/Images-Brand-Healthcare-Professionals/iStock-837226484%201200x849.jpg
layout: provider
modified: '2026-10-12'
name: Visiba Care
nav: Providers
network: true
overview: 'Visiba Care is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Software-as-a-Service, Digital Transformation, Telehealth, and Sweden.


  Visiba Care''s developer surface includes documentation and 11 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Visiba Care Domain Security
  slug: visiba-care-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: visiba-care
tags:
- Healthcare
- Software-as-a-Service
- Digital Transformation
- Telehealth
- Sweden
website: https://www.visibacare.com/
---
