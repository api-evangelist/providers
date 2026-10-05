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
  href: https://raw.githubusercontent.com/api-evangelist/beekeeperai/refs/heads/main/hosts/beekeeperai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beekeeperai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beekeeperai/refs/heads/main/vendors/beekeeperai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beekeeperai-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beekeeperai/refs/heads/main/security/beekeeperai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beekeeperai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-09-27'
  detail: The BeeKeeperAI website is a JavaScript‑rendered single‑page app with no machine‑readable OpenAPI or other contract discovered.
  evidence:
  - status: 200
    url: https://www.beekeeperai.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: BeeKeeperAI provides a confidential execution platform, EscrowAI®, that protects sensitive data and proprietary AI models by leveraging confidential computing. It helps organizations mitigate cybersecurity risks associated with agentic AI while ensuring ROI and compliance. The platform offers secure AI and data processing for enterprises seeking to harness AI safely.
layout: provider
modified: '2026-09-27'
name: BeeKeeperAI
nav: Providers
network: true
overview: BeeKeeperAI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Confidential Computing, Enterprise, and Security.
random_paper: 16
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 5
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beekeeperai Domain Security
  slug: beekeeperai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beekeeperai
tags:
- Company
- Artificial Intelligence
- Confidential Computing
- Enterprise
- Security
website: https://www.nasdaqprivatemarket.com/
---
