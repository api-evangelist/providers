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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/ujoin/hosts/ujoin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ujoin-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ujoin/security/ujoin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ujoin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ujoin.co/
- group: docs
  title: ''
  type: Documentation
  url: https://ujoin.co/
- group: company
  title: ''
  type: Blog
  url: https://join.ujoin.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ujoin.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ujoin.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ujoin.co/privacy
coverage:
  checked: '2026-10-27'
  detail: The provider's documentation site https://ujoin.co/ offers only HTML pages with no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract.
  evidence:
  - status: 200
    url: https://ujoin.co/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Ujoin Advocacy provides grassroots policy advocacy software that enables nonprofits, public affairs firms, corporations, associations, and citizen groups to track legislation, mobilize supporters, and drive policy impact. The platform offers AI‑enabled legislative intelligence, customizable action pages, real‑time bill tracking, and collaborative tools for teams, all delivered through an easy‑to‑use web interface and integrations with CRM systems.
image: https://ujoin.co/pubassets/images/ujoin-sbluewhite-logo.png
layout: provider
modified: '2026-10-27'
name: Ujoin Advocacy
nav: Providers
network: true
overview: 'Ujoin Advocacy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advocacy, Grassroots, Policy, and Software.


  Ujoin Advocacy''s developer surface includes documentation, engineering blog, pricing, and 5 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ujoin Domain Security
  slug: ujoin-domain-security
  summary_line: TLSv1.2 · DMARC
slug: ujoin
tags:
- Company
- Advocacy
- Grassroots
- Policy
- Software
website: https://ujoin.co/
---
