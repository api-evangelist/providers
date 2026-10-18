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
  href: https://raw.githubusercontent.com/api-evangelist/continuumrx/refs/heads/main/hosts/continuumrx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/continuumrx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/continuumrx/refs/heads/main/vendors/continuumrx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/continuumrx-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://continuumrx.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/continuumrx/refs/heads/main/security/continuumrx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/continuumrx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://continuumrx.com/
coverage:
  checked: '2026-10-10'
  detail: No OpenAPI, AsyncAPI, GraphQL, or MCP spec found on api.continuumrx.com despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.continuumrx.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: ContinuumRx provides home and site-based infusion therapies and services, partnering with healthcare systems to improve post-acute care coordination, patient outcomes, and financial performance. With over twenty years of experience, they offer antibiotic, enteral, parenteral, IVIG, heart‑failure, and biologic therapies, along with patient education and referral resources.
layout: provider
modified: '2026-10-10'
name: ContinuumRx
nav: Providers
network: true
overview: 'ContinuumRx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, InfusionTherapy, Home Care, and PostAcute.


  ContinuumRx''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Continuumrx Domain Security
  slug: continuumrx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: continuumrx
tags:
- Company
- Healthcare
- InfusionTherapy
- Home Care
- PostAcute
website: https://continuumrx.com/
---
