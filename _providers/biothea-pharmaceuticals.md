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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biothea-pharmaceuticals/refs/heads/main/hosts/biothea-pharmaceuticals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biothea-pharmaceuticals-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biothea-pharmaceuticals/refs/heads/main/security/biothea-pharmaceuticals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biothea-pharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.biotheapharma.com/
coverage:
  checked: '2026-09-28'
  detail: The website provides only static HTML with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.biotheapharma.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Biothea Pharmaceuticals (Biothea Pharma Inc.) is a biopharmaceutical company focused on developing needle‑free, convenient, and cost‑effective treatments for severe allergic reactions and anaphylaxis. Their mission is to revolutionize the management of life‑threatening allergic events by providing innovative, patient‑friendly therapies. The company’s website is currently under construction, offering information about their technology, research focus, and contact details.
layout: provider
modified: '2026-09-28'
name: Biothea Pharmaceuticals
nav: Providers
network: true
overview: Biothea Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Pharmaceuticals, Healthcare, Anaphylaxis, and NeedleFree.
random_paper: 13
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 4
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biothea Pharmaceuticals Domain Security
  slug: biothea-pharmaceuticals-domain-security
  summary_line: TLSv1.2
slug: biothea-pharmaceuticals
tags:
- Biotechnology
- Pharmaceuticals
- Healthcare
- Anaphylaxis
- NeedleFree
website: http://www.biotheapharma.com/
---
