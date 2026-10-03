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
api_count: 1
apis:
- description: API documentation hosted on the provider's help site.
  name: Bathhouse API
  slug: bathhouse-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bathhouse/refs/heads/main/hosts/bathhouse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bathhouse-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bathhouse/refs/heads/main/vendors/bathhouse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bathhouse-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abathhouse.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.abathhouse.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abathhouse.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://help.abathhouse.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bathhouse/refs/heads/main/security/bathhouse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bathhouse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.abathhouse.com
coverage:
  checked: '2026-09-27'
  detail: Help site renders documentation via JavaScript, no machine‑readable spec was found.
  evidence:
  - status: 403
    url: https://help.abathhouse.com/hc/en-us
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Bathhouse is a wellness brand operating boutique bathhouse locations offering sauna, steam, cold plunge, massage, and body treatments across major US cities. The company focuses on health, relaxation, and community experiences, providing membership and day‑pass options, as well as retail products. While primarily a physical‑service business, it maintains a digital presence for bookings, information, and community engagement.
image: http://static1.squarespace.com/static/5f627ccbb290eb31d9234aee/t/69d54e1eee588532aa09eb93/1668716808324/BATHHOUSE_Pools+02_Adrian+Gaut.jpg?format=1500w
layout: provider
modified: '2026-09-27'
name: Bathhouse
nav: Providers
network: true
overview: 'Bathhouse publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Wellness, Spa, Sauna, Membership, and Health.


  Bathhouse''s developer surface includes support, documentation, and 6 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bathhouse Domain Security
  slug: bathhouse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bathhouse
tags:
- Wellness
- Spa
- Sauna
- Membership
- Health
website: https://www.abathhouse.com
---
