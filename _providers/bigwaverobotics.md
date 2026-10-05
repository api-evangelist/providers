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
  href: https://raw.githubusercontent.com/api-evangelist/bigwaverobotics/refs/heads/main/hosts/bigwaverobotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bigwaverobotics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigwaverobotics/refs/heads/main/vendors/bigwaverobotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bigwaverobotics-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigwaverobotics/refs/heads/main/security/bigwaverobotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigwaverobotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bigwaverobotics.com
coverage:
  checked: '2026-09-28'
  detail: The company website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://bigwaverobotics.com
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Bigwaverobotics is a robotics and AI company focused on building physical artificial intelligence solutions for industrial automation. Their platform integrates hardware and software to deliver real-time AI-driven robotics, targeting sectors such as manufacturing, logistics, and smart infrastructure. The company emphasizes a global standard for industrial physical AI, offering products like Marosol and SOLlink to enhance automation efficiency and safety.
image: https://cdn.imweb.me/upload/S20241024b5cd9ce78e7f8/f5071e3d9954d.png
layout: provider
modified: '2026-09-28'
name: Bigwaverobotics
nav: Providers
network: true
overview: Bigwaverobotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Artificial Intelligence, Industrial Automation, and Manufacturing.
random_paper: 4
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Bigwaverobotics Domain Security
  slug: bigwaverobotics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bigwaverobotics
tags:
- Company
- Robotics
- Artificial Intelligence
- Industrial Automation
- Manufacturing
website: https://bigwaverobotics.com
---
