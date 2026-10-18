---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Programmatic access to Petra Security data and functionality.
  name: Petra Security API
  slug: petra-security-api
artifact_total: 3
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/petra/refs/heads/main/changelog/petra-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/petra-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/petra/refs/heads/main/authentication/petra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/petra-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/petra/refs/heads/main/conformance/petra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/petra-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/petra/refs/heads/main/llms/petra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/petra-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/petra/refs/heads/main/a2a/petra-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/petra-a2a.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/petra/refs/heads/main/hosts/petra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/petra-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/petra/refs/heads/main/vendors/petra-vendors.yml
  title: ''
  type: Vendors
  url: vendors/petra-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.petrasecurity.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.petrasecurity.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.petrasecurity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.petrasecurity.com/docs/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/petra/refs/heads/main/security/petra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/petra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.petrasecurity.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://support.petrasecurity.com/mcp
  - status: 200
    url: https://www.petrasecurity.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Petra Security provides modern ITDR (Identity Threat Detection and Response) solutions, helping organizations detect, investigate, and remediate security incidents across email, documents, and user accounts. Their platform offers real‑time alerts, automated response playbooks, and detailed forensic data, catering to MSPs, resellers, and internal security teams. Founded with backing from Lemnos Labs, Petra aims to simplify complex security operations and improve overall threat visibility for enterprises.
image: https://www.petrasecurity.com/opengraph-image?c5d151ee11ca9e2c
layout: provider
modified: '2026-10-12'
name: Petra
nav: Providers
network: true
overview: 'Petra is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, ITDR, Software-as-a-Service, and ThreatDetection.


  Petra''s developer surface includes changelog, authentication, support, documentation, API reference, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 73.2
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Petra Authentication
  slug: petra-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Petra Domain Security
  slug: petra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: petra
tags:
- Company
- Security
- ITDR
- Software-as-a-Service
- ThreatDetection
website: https://www.petrasecurity.com
---
