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
api_count: 1
apis:
- description: Data platform API for Aunalytics
  name: Aunalytics API
  slug: aunalytics-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aunalytics/refs/heads/main/conformance/aunalytics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aunalytics-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aunalytics/refs/heads/main/well-known/aunalytics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aunalytics-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aunalytics/refs/heads/main/hosts/aunalytics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aunalytics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aunalytics/refs/heads/main/vendors/aunalytics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aunalytics-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aunalytics.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.aunalytics.com/resources/news/
- group: company
  title: ''
  type: Blog
  url: https://www.aunalytics.com/category/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aunalytics/refs/heads/main/security/aunalytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aunalytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aunalytics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aunalytics.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://www.aunalytics.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aunalytics.com/terms-of-use/
coverage:
  checked: 2026-09-26
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.aunalytics.com/portals/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Aunalytics provides AI agents and AI‑powered solutions tailored for financial institutions and IT departments. Their platform offers an intelligent data warehouse, analytics services, and a suite of AI tools that help banks, credit unions, healthcare providers, and government agencies streamline data processing, improve decision‑making, and automate routine tasks. By combining secure infrastructure with proprietary data models, Aunalytics enables organizations to make data AI‑ready and put it to work across a range of enterprise cloud services, backup, disaster recovery, and managed security solutions.
layout: provider
modified: '2026-09-26'
name: Aunalytics
nav: Providers
network: true
overview: 'Aunalytics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Financial Services, Data Analytics, and Cloud.


  Aunalytics'' developer surface includes engineering blog, documentation, support, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aunalytics Domain Security
  slug: aunalytics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aunalytics
tags:
- Company
- Artificial Intelligence
- Financial Services
- Data Analytics
- Cloud
website: https://www.aunalytics.com/
---
