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
api_count: 1
apis:
- description: Business Intelligence Services API
  name: Blackcube API
  slug: blackcube-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackcube/refs/heads/main/hosts/blackcube-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackcube-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackcube/refs/heads/main/vendors/blackcube-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blackcube-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackcube/refs/heads/main/security/blackcube-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackcube-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blackcube.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.blackcube.com/services
- group: operate
  title: ''
  type: Support
  url: https://www.blackcube.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.blackcube.com/careers
- group: company
  title: ''
  type: About
  url: https://www.blackcube.com/about-us
coverage:
  checked: '2026-09-29'
  detail: The provider's documentation site is a Webflow page rendered with JavaScript, and no machine‑readable OpenAPI spec was found on api.blackcube.com or the docs host.
  evidence:
  - status: 0
    url: https://api.blackcube.com/openapi.json
  - status: 200
    url: https://www.blackcube.com/services
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: Blackcube is a global boutique intelligence firm offering sophisticated human intelligence (HUMINT) and open source (OSINT) services for high‑profile litigations, arbitrations, and white‑collar crime investigations. With offices in London, Tel‑Aviv, Madrid and Singapore, the company leverages former Israeli intelligence officers and legal experts to provide evidence‑gathering, asset recovery, and counter‑intelligence solutions worldwide.
layout: provider
modified: '2026-09-29'
name: Blackcube
nav: Providers
network: true
overview: 'Blackcube publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Intelligence, Consulting, Litigation Support, HUMINT, and OSINT.


  Blackcube''s developer surface includes documentation, support, and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blackcube Domain Security
  slug: blackcube-domain-security
  summary_line: TLSv1.3 · HSTS
slug: blackcube
tags:
- Intelligence
- Consulting
- Litigation Support
- HUMINT
- OSINT
website: https://www.blackcube.com
---
