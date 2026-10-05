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
- description: Recruiting marketplace API (no public documentation found)
  name: Bountyjobs API
  slug: bountyjobs-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bountyjobs/refs/heads/main/hosts/bountyjobs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bountyjobs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bountyjobs/refs/heads/main/vendors/bountyjobs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bountyjobs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bountyjobs.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bountyjobs.com/privacy-policy?hsLang=en
- group: company
  title: ''
  type: Blog
  url: https://blog.bountyjobs.com/?hsLang=en
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bountyjobs/refs/heads/main/security/bountyjobs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bountyjobs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bountyjobs.com
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on any discovered host.
  evidence:
  - status: 404
    url: https://api.bountyjobs.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: BountyJobs is a recruiting marketplace and extended workforce platform that connects employers with over 14,000 vetted search firms, independent recruiters, and provides a purpose‑built Vendor Management System (VMS). It offers solutions for recruiting, contracting, SOW projects, and contingent talent, with integrated analytics, compliance, and a single‑contract, single‑invoice workflow for both employers and agencies.
layout: provider
modified: '2026-10-03'
name: Bountyjobs
nav: Providers
network: true
overview: 'Bountyjobs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Recruiting Marketplace, Extended Workforce, Vendor Management, Staffing Platform, and Recruiter Network.


  Bountyjobs'' developer surface includes engineering blog and 6 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bountyjobs Domain Security
  slug: bountyjobs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bountyjobs
tags:
- Recruiting Marketplace
- Extended Workforce
- Vendor Management
- Staffing Platform
- Recruiter Network
website: https://bountyjobs.com
---
