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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/qnap/well-known/qnap-qnap-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/qnap-qnap-security.txt
- group: design
  href: https://artifacts.apis.io/qnap/conformance/qnap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qnap-conformance.yml
- group: agent
  href: https://artifacts.apis.io/qnap/llms/qnap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qnap-llms.txt
- group: auth
  href: https://artifacts.apis.io/qnap/well-known/qnap-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/qnap-www-security.txt
- group: auth
  href: https://artifacts.apis.io/qnap/well-known/qnap-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/qnap-security.txt
- group: agent
  href: https://artifacts.apis.io/qnap/well-known/qnap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qnap-well-known.yml
- group: other
  href: https://artifacts.apis.io/qnap/hosts/qnap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qnap-hosts.yml
- group: other
  href: https://artifacts.apis.io/qnap/vendors/qnap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qnap-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.qnap.com/en-us/security/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qnap.com/en-us/software/qvr-pro/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.qnap.com/go/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.qnap.com/go/developer/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.qnap.com/en-us/release-notes/
- group: docs
  title: ''
  type: APIReference
  url: https://www.qnap.com/go/reference/
- group: auth
  href: https://artifacts.apis.io/qnap/security/qnap-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/qnap-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/qnap/security/qnap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qnap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qnap.com/
coverage:
  checked: '2026-10-28'
  detail: Developer documentation pages are rendered via JavaScript and provide no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.qnap.com/en-us/developer/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: QNAP Systems, Inc. provides secure, intelligent data and storage solutions, including network attached storage (NAS), high‑availability systems, networking, edge AI servers, video surveillance, and myQNAPcloud services. Their products accelerate workflows, protect data, and strengthen IT/OT resilience for enterprises and consumers worldwide.
image: https://www.qnap.com/assets/img/logo/defualt-sharing.png?v=3
layout: provider
modified: '2026-10-28'
name: QNAP
nav: Providers
network: true
overview: 'QNAP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Storage, NAS, Enterprise, and Cloud.


  QNAP''s developer surface includes pricing, changelog, API reference, and 14 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Qnap Domain Security
  slug: qnap-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qnap Vulnerability Disclosure
  slug: qnap-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: qnap
tags:
- Company
- Storage
- NAS
- Enterprise
- Cloud
website: https://qnap.com/
---
