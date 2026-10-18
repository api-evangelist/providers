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
- description: Curavit Clinical Research API
  name: Curavit API
  slug: curavit-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curavit/refs/heads/main/hosts/curavit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curavit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curavit/refs/heads/main/vendors/curavit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/curavit-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://curavit.io/about/press/
- group: other
  title: ''
  type: Leadership
  url: https://curavit.io/about/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curavit/refs/heads/main/security/curavit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curavit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://curavit.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://curavit.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://curavit.io/privacy-policy
coverage:
  checked: '2026-10-12'
  detail: The Curavit website provides documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract was found.
  evidence:
  - status: 200
    url: https://curavit.io
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Curavit Clinical Research is a remote clinical site and contract research organization (CRO) that designs, develops, and executes decentralized clinical trials. Founded in 2019 and based in Boston, Curavit offers feasibility, protocol development, virtual site technology, and end‑to‑end trial management services for sponsors across therapeutics, diagnostics, medical devices, and digital health. Their platform integrates regulatory guidance, participant‑centric tools, and scalable recruitment to accelerate study timelines and improve data quality.
image: https://curavit.io/wp-content/uploads/2025/07/Screen-Shot-2025-06-24-at-1.23.00-PM.png
layout: provider
modified: '2026-10-12'
name: Curavit
nav: Providers
network: true
overview: Curavit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRO, Clinical Trials, Decentralized, and Remote.
random_paper: 18
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Curavit Domain Security
  slug: curavit-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: curavit
tags:
- Company
- CRO
- Clinical Trials
- Decentralized
- Remote
website: https://curavit.io
---
