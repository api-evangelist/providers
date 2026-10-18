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
  href: https://raw.githubusercontent.com/api-evangelist/afi/refs/heads/main/hosts/afi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/afi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/afi/refs/heads/main/vendors/afi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/afi-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.afipayments.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afi/refs/heads/main/security/afi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://afipayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.afipayments.com/about
- group: start
  title: ''
  type: SignUp
  url: https://app.afipayments.com/signup
coverage:
  checked: '2026-10-12'
  detail: The provider's documentation pages render only via JavaScript, preventing machine‑readable extraction of an API contract.
  evidence:
  - status: 200
    url: https://app.afipayments.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: AFi provides a platform for sending and receiving commercial payments across Africa. Targeting unbanked and underbanked small businesses, AFi enables B2B transactions via mobile phones, supporting mobile money and bank accounts. Currently operating in Ghana and Togo, with plans to expand to WAEMU, Nigeria, and the US, the service offers secure, swift, and affordable cross‑border payments, along with tools for document submission and capital management.
image: http://static1.squarespace.com/static/65849a740bc71944ab3fda58/t/658609d4501c977c16905f7d/1703283156520/Afi_social+sharing+image+01.jpg?format=1500w
layout: provider
modified: '2026-10-12'
name: AFi
nav: Providers
network: true
overview: 'AFi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Africa, B2B, and Mobile.


  AFi''s developer surface includes documentation, signup flow, and 5 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afi Domain Security
  slug: afi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: afi
tags:
- Fintech
- Payments
- Africa
- B2B
- Mobile
website: https://afipayments.com/
---
