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
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/cirrus-logic/conformance/cirrus-logic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cirrus-logic-conformance.yml
- group: other
  href: https://artifacts.apis.io/cirrus-logic/hosts/cirrus-logic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cirrus-logic-hosts.yml
- group: other
  href: https://artifacts.apis.io/cirrus-logic/vendors/cirrus-logic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cirrus-logic-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cirrus.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cirrus.com/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cirrus.com/company/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://www.cirrus.com/docs/ds/cs5341-datasheet.pdf
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cirrus.com/docs/ug/voice-capture-dev-kit-for-avs-quick-start-guide.pdf
- group: auth
  href: https://artifacts.apis.io/cirrus-logic/security/cirrus-logic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cirrus-logic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cirrus.com/
coverage:
  checked: '2026-10-26'
  detail: The developer portal at https://www.cirrus.com/developers returns a JavaScript‑rendered page with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.cirrus.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Cirrus Logic designs and manufactures high-performance analog and mixed-signal semiconductors for audio, voice, and IoT applications. The company provides audio codecs, amplifiers, and digital signal processors used in consumer electronics, automotive, and industrial devices. Its solutions enable high-fidelity sound, efficient power management, and advanced connectivity across a wide range of products worldwide.
image: https://www.cirrus.com/images/cirrus-logic-logo.webp
layout: provider
modified: '2026-10-26'
name: Cirrus Logic
nav: Providers
network: true
overview: 'Cirrus Logic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductor, Audio, IoT, and Automotive.


  Cirrus Logic''s developer surface includes documentation, getting-started guide, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cirrus Logic Domain Security
  slug: cirrus-logic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cirrus-logic
tags:
- Company
- Semiconductor
- Audio
- IoT
- Automotive
website: https://www.cirrus.com/
---
