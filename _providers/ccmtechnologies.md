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
  href: https://raw.githubusercontent.com/api-evangelist/ccmtechnologies/refs/heads/main/hosts/ccmtechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ccmtechnologies-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ccmtechnologies.co.uk/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.ccmtechnologies.co.uk/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ccmtechnologies/refs/heads/main/security/ccmtechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ccmtechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ccmtechnologies.co.uk
coverage:
  checked: '2026-10-07'
  detail: The company provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.ccmtechnologies.co.uk/
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: CCm Technologies is an award‑winning cleantech company that optimises resource use through Carbon Capture and Utilisation (CCU) solutions. It converts captured CO₂ and other waste streams into stable, low‑carbon fertiliser and material products for agriculture, food manufacturing, bio‑char and water treatment sectors, aligning with UN Sustainable Development Goals and delivering commercial value while reducing scope 1‑3 emissions.
layout: provider
modified: '2026-10-07'
name: Ccmtechnologies
nav: Providers
network: true
overview: Ccmtechnologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cleantech, Carbon Capture, Fertiliser, and Sustainability.
random_paper: 7
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ccmtechnologies Domain Security
  slug: ccmtechnologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ccmtechnologies
tags:
- Company
- Cleantech
- Carbon Capture
- Fertiliser
- Sustainability
website: https://www.ccmtechnologies.co.uk
---
