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
  href: https://raw.githubusercontent.com/api-evangelist/nintendo/refs/heads/main/hosts/nintendo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nintendo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nintendo/refs/heads/main/vendors/nintendo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nintendo-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nintendo.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nintendo/refs/heads/main/security/nintendo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nintendo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nintendo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.nintendo.com
- group: operate
  title: ''
  type: Support
  url: https://support.nintendo.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nintendo.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nintendo.com/privacy-policy/
coverage:
  checked: '2026-10-13'
  detail: Developer portal pages are rendered via JavaScript and provide no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.nintendo.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Nintendo Co., Ltd. is a Japanese multinational consumer electronics and video game company headquartered in Kyoto, Japan. It creates and publishes some of the most iconic gaming franchises, including Mario, Zelda, and Pokémon, and manufactures dedicated gaming hardware such as the Nintendo Switch. The company operates a global online presence, offering e‑commerce, developer resources, and support services through its official website and developer portal.
image: https://assets.nintendo.com/image/upload/v1643742733/ncom/global/social-share.jpg
layout: provider
modified: '2026-10-13'
name: Nintendo
nav: Providers
network: true
overview: 'Nintendo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Electronics, Entertainment, and Japan.


  Nintendo''s developer surface includes documentation, support, and 7 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nintendo Domain Security
  slug: nintendo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nintendo
tags:
- Company
- Gaming
- Electronics
- Entertainment
- Japan
website: https://www.nintendo.com
---
