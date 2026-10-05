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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blue-note-therapeutics/refs/heads/main/hosts/blue-note-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blue-note-therapeutics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blue-note-therapeutics/refs/heads/main/vendors/blue-note-therapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blue-note-therapeutics-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dtxalliance.org/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blue-note-therapeutics/refs/heads/main/security/blue-note-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blue-note-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dtxalliance.org/members/bluenotetherapeutics/
coverage:
  checked: '2026-09-29'
  detail: The provider's documentation is only static HTML pages without any machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://dtxalliance.org/members/bluenotetherapeutics/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: Blue Note Therapeutics is a digital therapeutics company focused on developing innovative treatments for cancer patients. Listed as a member of the Digital Therapeutics Alliance, the company aims to address cancer-related distress through digital interventions. While its own website is not publicly reachable, the alliance member page confirms its identity and mission, providing a basis for API profiling.
image: https://dtxalliance.org/wp-content/uploads/2021/01/social.jpg
layout: provider
modified: '2026-09-29'
name: Blue Note Therapeutics
nav: Providers
network: true
overview: Blue Note Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Therapeutics, Cancer, Health, and Biotechnology.
random_paper: 5
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blue Note Therapeutics Domain Security
  slug: blue-note-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: blue-note-therapeutics
tags:
- Company
- Digital Therapeutics
- Cancer
- Health
- Biotechnology
website: https://dtxalliance.org/members/bluenotetherapeutics/
---
