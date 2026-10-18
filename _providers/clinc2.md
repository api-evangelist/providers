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
  href: https://raw.githubusercontent.com/api-evangelist/clinc2/refs/heads/main/hosts/clinc2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clinc2-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clinc2/refs/heads/main/vendors/clinc2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clinc2-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clinc2/refs/heads/main/security/clinc2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clinc2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/clinc2
coverage:
  checked: '2026-10-09'
  detail: The provider's website and API references are only reachable via JavaScript‑rendered pages, preventing machine‑readable discovery.
  evidence:
  - status: unreachable
    url: https://www.clinc.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Clinc2 is a nascent technology company focused on developing advanced conversational AI platforms for healthcare and finance sectors. Founded in 2022, the firm aims to integrate natural language understanding with secure data handling to enable seamless patient‑clinician interactions and compliant financial advisory services. While still early in its product rollout, Clinc2 emphasizes privacy‑by‑design, leveraging on‑premise deployment options and robust API ecosystems to serve enterprise clients seeking AI‑driven conversational solutions.
layout: provider
modified: '2026-10-08'
name: Clinc2
nav: Providers
network: true
overview: Clinc2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Healthcare, Finance, ConversationalAI, and Privacy.
random_paper: 21
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clinc2 Domain Security
  slug: clinc2-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clinc2
tags:
- Artificial Intelligence
- Healthcare
- Finance
- ConversationalAI
- Privacy
website: https://equityzen.com/company/clinc2
---
