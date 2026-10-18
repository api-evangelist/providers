---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cortec/refs/heads/main/well-known/cortec-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cortec-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cortec/refs/heads/main/hosts/cortec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cortec-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cortec/refs/heads/main/vendors/cortec-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cortec-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cortec/refs/heads/main/security/cortec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cortec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cortecvci.com
coverage:
  checked: '2026-10-11'
  detail: No public API documentation or machine‑readable contract was found for Cortec.
  evidence:
  - status: 0
    url: https://api.cortecvci.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Cortec Corporation provides advanced corrosion inhibition technologies, including VpCI® and MCI® solutions for packaging, metalworking, construction, electronics, oil & gas, and many other industries. Founded in 1977, Cortex has grown to a global leader with over 400 products and 60+ patents, offering environmentally responsible, cost‑effective corrosion control. The company operates worldwide, serving customers with R&D, ISO‑accredited labs, and extensive technical support.
image: https://www.cortecvci.com/wp-content/uploads/Cortec-VpCI®_logo_ISO-1.png
layout: provider
modified: '2026-10-11'
name: Cortec
nav: Providers
network: true
overview: Cortec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Corrosion, Chemicals, Manufacturing, and VpCI.
random_paper: 2
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 6
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
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cortec Domain Security
  slug: cortec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cortec
tags:
- Company
- Corrosion
- Chemicals
- Manufacturing
- VpCI
- MCI
website: https://www.cortecvci.com
---
