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
  href: https://raw.githubusercontent.com/api-evangelist/cordis/refs/heads/main/hosts/cordis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cordis-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cordis/refs/heads/main/security/cordis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cordis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cordis.com/
coverage:
  checked: '2026-10-11'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found at the API host or documentation sites.
  evidence:
  - status: 0
    url: https://api.cordis.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Cordis is a global medical device company specializing in interventional cardiology solutions. It offers a wide range of products such as drug‑eluting balloons, guidewires, sheaths, and stents for vascular procedures. The company’s website provides detailed product information, regulatory approvals, and corporate news, confirming its identity as a leading provider in the cardiovascular market.
image: https://cordis.com/uploads/images/Cordis-Logos/_1200x630_crop_center-center_82_none/Cordis_Logo-1.png?mtime=1758835439
layout: provider
modified: '2026-10-10'
name: Cordis
nav: Providers
network: true
overview: Cordis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Interventional Cardiology, Healthcare, and Cardiovascular.
random_paper: 6
score:
  band: minimal
  composite: 3.7
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
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cordis Domain Security
  slug: cordis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cordis
tags:
- Company
- Medical Devices
- Interventional Cardiology
- Healthcare
- Cardiovascular
website: https://cordis.com/
---
