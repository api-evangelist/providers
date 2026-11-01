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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/galileohealth-com/llms/galileohealth-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/galileohealth-com-llms.txt
- group: other
  href: https://artifacts.apis.io/galileohealth-com/hosts/galileohealth-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/galileohealth-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/galileohealth-com/vendors/galileohealth-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/galileohealth-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://galileo.io/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://galileo.io/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://galileo.io/resources/press
- group: company
  title: ''
  type: Blog
  url: https://galileo.io/resources/blog
- group: auth
  href: https://artifacts.apis.io/galileohealth-com/security/galileohealth-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/galileohealth-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://galileo.io
coverage:
  checked: '2026-10-25'
  detail: Provider docs are served as JavaScript-rendered pages with no machine-readable spec discovered.
  evidence:
  - status: 200
    url: https://galileo.io
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Galileo provides a virtual care platform offering 24/7 urgent and primary telehealth services. Patients can access licensed doctors through video, phone, or chat for acute issues, chronic condition management, and preventive care. The service integrates with electronic health records, supports insurance billing, and offers a mobile app for seamless scheduling and follow‑up. Backed by leading venture firms, Galileo aims to improve access to quality healthcare across the United States.
layout: provider
modified: '2026-10-25'
name: Galileo
nav: Providers
network: true
overview: 'Galileo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Telehealth, VirtualCare, API, and Platform.


  Galileo''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Galileohealth Com Domain Security
  slug: galileohealth-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: galileohealth-com
tags:
- Healthcare
- Telehealth
- VirtualCare
- API
- Platform
website: https://galileo.io
---
