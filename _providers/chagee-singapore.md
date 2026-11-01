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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/chagee-singapore/hosts/chagee-singapore-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chagee-singapore-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chagee.com.sg/en/privacy
- group: auth
  href: https://artifacts.apis.io/chagee-singapore/security/chagee-singapore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chagee-singapore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chagee.com.sg/en
coverage:
  checked: '2026-10-25'
  detail: The documentation site loads content via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://www.chagee.com/en
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: CHAGEE Singapore is a tea brand based in Singapore, offering a wide range of Chinese‑style milk tea, fresh fruit tea, and derivative tea products. Originating from Yunnan, the birthplace of tea, CHAGEE blends traditional tea heritage with modern flavors, operating over 6,000 stores worldwide. The company focuses on original leaf fresh milk tea, integrating oriental culture and innovation to create a new oriental tea shop experience.
image: https://oss.chagee.com.sg/website2025/uploads/20240712/998f1cc8-c575-4463-9577-fe268aa01c22.png
layout: provider
modified: '2026-10-25'
name: CHAGEE Singapore
nav: Providers
network: true
overview: CHAGEE Singapore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tea, Beverage, Singapore, and Retail.
random_paper: 10
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chagee Singapore Domain Security
  slug: chagee-singapore-domain-security
  summary_line: TLSv1.2 · HSTS
slug: chagee-singapore
tags:
- Company
- Tea
- Beverage
- Singapore
- Retail
- Food
website: https://www.chagee.com.sg/en
---
