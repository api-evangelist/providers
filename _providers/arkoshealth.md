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
  href: https://raw.githubusercontent.com/api-evangelist/arkoshealth/refs/heads/main/hosts/arkoshealth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arkoshealth-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: http://arkoshealth.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arkoshealth.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: http://arkoshealth.com/category/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arkoshealth/refs/heads/main/security/arkoshealth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arkoshealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arkoshealth.com
coverage:
  checked: 2026-09-26
  detail: Arkoshealth provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://arkoshealth.com
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Arkos Health is a healthcare technology company that partners with payers, providers, and patients to deliver value‑based care solutions. Since 2018, it offers integrated clinical services, care coordination, and data‑driven insights through its proprietary Arkos360 platform, aiming to simplify complex healthcare processes, reduce costs, and improve outcomes across its network of providers and members.
image: https://arkoshealth.com/wp-content/uploads/2021/10/care-net-10.jpg
layout: provider
modified: '2026-09-26'
name: Arkoshealth
nav: Providers
network: true
overview: Arkoshealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Technology, Value-Based Care, and Platform.
random_paper: 8
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arkoshealth Domain Security
  slug: arkoshealth-domain-security
  summary_line: TLSv1.2 · DMARC
slug: arkoshealth
tags:
- Company
- Healthcare
- Technology
- Value-Based Care
- Platform
website: https://arkoshealth.com
---
