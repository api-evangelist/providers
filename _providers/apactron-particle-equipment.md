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
  href: https://raw.githubusercontent.com/api-evangelist/apactron-particle-equipment/refs/heads/main/hosts/apactron-particle-equipment-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apactron-particle-equipment-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apactron-particle-equipment/refs/heads/main/vendors/apactron-particle-equipment-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apactron-particle-equipment-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apactron-particle-equipment/refs/heads/main/security/apactron-particle-equipment-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apactron-particle-equipment-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-09-25'
  detail: Attempts to reach the company's website (https://www.apactron.com) failed, indicating no public API documentation or contracts.
  evidence:
  - status: unreachable
    url: https://www.apactron.com
  reason: not-a-software-company
  state: none
created: '2026-09-25'
description: APACTRON Particle Equipment, based in Shanghai, China, manufactures proton therapy and particle accelerator equipment. Established in 2011, it is controlled by Shanghai Lianhe Investment and jointly invested by the Shanghai Institute of Applied Physics. The company provides advanced medical equipment for cancer treatment and research.
layout: provider
modified: '2026-09-25'
name: APACTRON Particle Equipment
nav: Providers
network: true
overview: APACTRON Particle Equipment is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Equipment, Proton Therapy, Particle Accelerators, and China.
random_paper: 10
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
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apactron Particle Equipment Domain Security
  slug: apactron-particle-equipment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apactron-particle-equipment
tags:
- Company
- Medical Equipment
- Proton Therapy
- Particle Accelerators
- China
website: https://www.nasdaqprivatemarket.com/
---
