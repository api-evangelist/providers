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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API documented on Booost Technologies website
  name: Booost Technologies API
  slug: booost-technologies-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/booosttechnologies/refs/heads/main/hosts/booosttechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/booosttechnologies-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booosttechnologies/refs/heads/main/security/booosttechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/booosttechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://booost.inc
- group: docs
  title: ''
  type: Documentation
  url: https://booost.inc/COMPANY
- group: operate
  title: ''
  type: Support
  url: https://booost.inc/CONTACT
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://booost.inc/PrivacyPolicy
coverage:
  checked: '2026-10-02'
  detail: The Booost Technologies website returns a JavaScript shell with no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://booost.inc/COMPANY
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: Booost Technologies is a Japanese sustainability‑focused enterprise software company offering the Booost Sustainability ERP platform. The platform helps organizations integrate environmental, social and governance (ESG) data into their operations, driving scalable growth and net‑zero initiatives across more than 95 countries. With multilingual support and a global client base, Booost delivers a comprehensive suite for sustainability reporting, risk management, and value creation.
image: https://storage.googleapis.com/production-os-assets/assets/9eb5b8b8-5632-494d-9bbf-91810b7ac80c
layout: provider
modified: '2026-10-02'
name: Booosttechnologies
nav: Providers
network: true
overview: 'Booosttechnologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sustainability, ERP, ESG, and Japan.


  Booosttechnologies'' developer surface includes documentation, support, and 4 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Booosttechnologies Domain Security
  slug: booosttechnologies-domain-security
  summary_line: TLSv1.3
slug: booosttechnologies
tags:
- Company
- Sustainability
- ERP
- ESG
- Japan
- Software
website: https://booost.inc
---
