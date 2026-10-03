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
  href: https://raw.githubusercontent.com/api-evangelist/arsenal-medical/refs/heads/main/hosts/arsenal-medical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arsenal-medical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arsenal-medical/refs/heads/main/vendors/arsenal-medical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arsenal-medical-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://arsenalmedical.com/about/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arsenal-medical/refs/heads/main/security/arsenal-medical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arsenal-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arsenalmedical.com
- group: operate
  title: ''
  type: Support
  url: https://arsenalmedical.com/contact/
- group: docs
  title: ''
  type: Documentation
  url: https://arsenalmedical.com/platform/
coverage:
  checked: 2026-09-26
  detail: The platform documentation page provides only HTML without any machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract.
  evidence:
  - status: 200
    url: https://arsenalmedical.com/platform/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Arsenal Medical develops innovative biomaterials and medical devices, including injectable foams and neurovascular occlusion solutions. The company focuses on transformative medicine, delivering products such as NeoCast™ and ResQFoam® to address unmet clinical needs across therapeutic areas. Their platform combines material science and medical expertise to create local therapies for critical conditions.
layout: provider
modified: '2026-09-26'
name: Arsenal Medical
nav: Providers
network: true
overview: 'Arsenal Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Biomaterials, Healthcare, Innovation, and Company.


  Arsenal Medical''s developer surface includes support, documentation, and 5 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 6.3
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
    developer_ergonomics: 14.3
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Arsenal Medical Domain Security
  slug: arsenal-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arsenal-medical
tags:
- Medical Devices
- Biomaterials
- Healthcare
- Innovation
- Company
website: https://arsenalmedical.com
---
