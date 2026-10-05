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
  href: https://raw.githubusercontent.com/api-evangelist/bone-health-technologies/refs/heads/main/hosts/bone-health-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bone-health-technologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bone-health-technologies/refs/heads/main/vendors/bone-health-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bone-health-technologies-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bone-health-technologies/refs/heads/main/security/bone-health-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bone-health-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-10-02'
  detail: No public developer documentation or API endpoints were found for Bone Health Technologies.
  evidence:
  - status: unreachable
    url: https://www.bonehealthtechnologies.com
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Bone Health Technologies develops innovative diagnostic and monitoring solutions for bone health, focusing on advanced imaging, biomarkers, and data-driven platforms to help clinicians assess bone density, fracture risk, and treatment efficacy. The company aims to improve patient outcomes through technology integration and research collaborations, offering APIs for data access and integration with healthcare systems.
layout: provider
modified: '2026-10-02'
name: Bone Health Technologies
nav: Providers
network: true
overview: Bone Health Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Diagnostics, Imaging, Biomarkers, and Data Integration.
random_paper: 4
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
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bone Health Technologies Domain Security
  slug: bone-health-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bone-health-technologies
tags:
- Health
- Diagnostics
- Imaging
- Biomarkers
- Data Integration
- Healthcare
website: https://www.nasdaqprivatemarket.com/
---
