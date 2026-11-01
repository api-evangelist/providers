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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation is hosted on Zhone's Salesforce community portal.
  name: Zhone API
  slug: zhone-api
artifact_total: 2
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zhone.com/privacy-policy/
- group: agent
  href: https://artifacts.apis.io/zhone-technologies/well-known/zhone-technologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zhone-technologies-well-known.yml
- group: other
  href: https://artifacts.apis.io/zhone-technologies/hosts/zhone-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zhone-technologies-hosts.yml
- group: other
  href: https://artifacts.apis.io/zhone-technologies/vendors/zhone-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zhone-technologies-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://zhone.com/company/news/
- group: other
  title: ''
  type: Leadership
  url: https://zhone.com/company/about/leadership/
- group: auth
  href: https://artifacts.apis.io/zhone-technologies/security/zhone-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zhone-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zhone.com
- group: docs
  title: ''
  type: Documentation
  url: https://dzs.my.site.com/kmcc/s/documentation
- group: operate
  title: ''
  type: Support
  url: https://zhone.com/support-center/
- group: company
  title: ''
  type: Blog
  url: https://zhone.com/company/resources/blogs/
- group: commercial
  title: ''
  type: Pricing
  url: https://zhone.com/support-center/support-plans/
coverage:
  checked: '2026-10-23'
  detail: Documentation portal returns HTML shells for OpenAPI endpoints, no machine‑readable spec.
  evidence:
  - status: 404
    url: https://dzs.my.site.com/kmcc/s/documentation/openapi.json
  - status: 200
    url: https://dzs.my.site.com/kmcc/s/documentation/openapi.yaml
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Zhone Technologies provides broadband and networking solutions, enabling multi‑gigabit in‑home experiences while reducing OPEX for service providers. The company focuses on accelerating time‑to‑market for new services, offering hardware, software, and managed services to telecom operators worldwide.
image: https://zhone.com/wp-content/uploads/DZS-Homepage-1200x627-1.jpg
layout: provider
modified: '2026-10-22'
name: Zhone Technologies
nav: Providers
network: true
overview: 'Zhone Technologies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Broadband, Networking, Telecom, and Managed Services.


  Zhone Technologies'' developer surface includes documentation, support, engineering blog, pricing, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 13.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zhone Technologies Domain Security
  slug: zhone-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zhone-technologies
tags:
- Company
- Broadband
- Networking
- Telecom
- Managed Services
website: https://zhone.com
---
