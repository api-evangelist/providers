---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Realtime Voice API provides streaming voice recognition and synthesis for web and mobile applications.
  name: Centerbeam Realtime Voice API
  slug: centerbeam-realtime-voice-api
- description: The Sessions API from Centerbeam Voice AI SDK — 4 operation(s) for sessions.
  name: Centerbeam Voice AI SDK Sessions API
  slug: centerbeam-sessions-api
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/centerbeam/refs/heads/main/plans/centerbeam-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/centerbeam-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centerbeam/refs/heads/main/rules/centerbeam-rules.yml
  title: ''
  type: Spectral
  url: rules/centerbeam-rules.yml
- group: auth
  title: ''
  type: Compliance
  url: https://centerbeam.ai/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centerbeam/refs/heads/main/conformance/centerbeam-conformance.yml
  title: ''
  type: Conformance
  url: conformance/centerbeam-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centerbeam/refs/heads/main/hosts/centerbeam-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centerbeam-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://centerbeam.ai/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centerbeam/refs/heads/main/security/centerbeam-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/centerbeam-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centerbeam/refs/heads/main/security/centerbeam-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centerbeam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centerbeam.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://centerbeam.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://centerbeam.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://centerbeam.ai/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://centerbeam.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://centerbeam.ai/sign-up
coverage:
  checked: '2026-10-16'
  detail: API documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://centerbeam.ai/realtime-voice-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Centerbeam Voice AI SDK provides a powerful Voice AI SDK enabling developers to integrate speech recognition, natural language understanding, and voice synthesis into applications. The platform offers real-time processing, multi-language support, and customizable voice models, targeting enterprises and developers building voice-enabled solutions across mobile, web, and IoT devices. It emphasizes privacy, scalability, and easy integration via comprehensive documentation and SDKs for multiple programming languages.
image: https://centerbeam.ai/centerbeam-logo-dark.png
layout: provider
modified: '2026-10-16'
name: Centerbeam Voice AI SDK
nav: Providers
network: true
overview: 'Centerbeam Voice AI SDK is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Sessions API, and 1 more. Tagged areas include Company, VoiceAI, SDK, Real-Time, and Multilingual.


  The Centerbeam Voice AI SDK catalog on APIs.io includes 1 Spectral governance ruleset.


  Centerbeam Voice AI SDK''s developer surface includes documentation, API reference, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Centerbeam Plans Pricing
  plan_count: 4
  slug: centerbeam-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Centerbeam Voice AI SDK API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: centerbeam-rules
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 9.4
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Centerbeam Domain Security
  slug: centerbeam-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Centerbeam Trust Center
  slug: centerbeam-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: centerbeam
tags:
- Company
- VoiceAI
- SDK
- Real-Time
- Multilingual
website: https://centerbeam.ai/
---
