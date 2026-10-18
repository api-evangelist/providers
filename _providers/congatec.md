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
  href: https://raw.githubusercontent.com/api-evangelist/congatec/refs/heads/main/hosts/congatec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/congatec-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.congatec.com/en/congatec/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.congatec.com/en/congatec/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://www.congatec.com/en/login/
- group: company
  title: ''
  type: Blog
  url: https://blog.congatec.com/en
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/congatec/refs/heads/main/security/congatec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/congatec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.congatec.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.congatec.com/en/technologies/knowledge-base/
- group: operate
  title: ''
  type: Support
  url: https://www.congatec.com/en/congatec-support/
coverage:
  checked: '2026-10-10'
  detail: The developer documentation is only available as rendered HTML pages without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.congatec.com/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-10'
description: Congatec designs and manufactures embedded computer-on-modules (COM) and system-in-package solutions for industrial, automotive, and IoT applications. Their product portfolio includes COM-HPC, COM Express, SMARC, and Qseven modules, along with aReady services, design‑in training, and support resources. Congatec serves sectors such as automation, medical technology, and transportation, offering customizable modules and carrier board designs to meet performance, low‑power, and server‑class requirements.
layout: provider
modified: '2026-10-10'
name: Congatec
nav: Providers
network: true
overview: 'Congatec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Embedded, Hardware, IoT, and Industrial.


  Congatec''s developer surface includes engineering blog, documentation, support, and 6 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Congatec Domain Security
  slug: congatec-domain-security
  summary_line: TLSv1.3 · DMARC
slug: congatec
tags:
- Company
- Embedded
- Hardware
- IoT
- Industrial
website: https://www.congatec.com
---
