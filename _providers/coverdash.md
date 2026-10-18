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
api_count: 1
apis:
- description: API for Coverdash digital business insurance platform
  name: Coverdash API
  slug: coverdash-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coverdash/refs/heads/main/llms/coverdash-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coverdash-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coverdash/refs/heads/main/well-known/coverdash-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coverdash-support-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coverdash/refs/heads/main/well-known/coverdash-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coverdash-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coverdash/refs/heads/main/hosts/coverdash-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coverdash-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coverdash/refs/heads/main/vendors/coverdash-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coverdash-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coverdash.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.coverdash.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coverdash.com/privacy
- group: start
  title: ''
  type: Login
  url: https://app.coverdash.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.coverdash.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coverdash.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coverdash
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coverdash/refs/heads/main/security/coverdash-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coverdash-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coverdash.com/
coverage:
  checked: '2026-10-11'
  detail: Docs are public but attempts to fetch OpenAPI spec returned 401/404, no machine‑readable contract found.
  evidence:
  - status: 401
    url: https://api.coverdash.com/openapi.json
  - status: 404
    url: https://api.coverdash.com/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Coverdash is a digital business insurance agency that provides fully‑digital, instant business insurance solutions for small and medium‑sized enterprises. Founded in 2022 and based in New York City, Coverdash offers a range of coverages—including General Liability, Workers’ Compensation, Cyber, Professional Liability, and Commercial Auto—through a streamlined online platform that connects businesses with top‑rated carriers, delivering quotes and policies in minutes without brokers or paperwork.
image: https://www.coverdash.com/og/coverdash-og.jpg
layout: provider
modified: '2026-10-11'
name: Coverdash
nav: Providers
network: true
overview: 'Coverdash is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurtech, Business Insurance, Software-as-a-Service, API Platform, and Small Business.


  Coverdash''s developer surface includes support, engineering blog, documentation, and 11 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coverdash Domain Security
  slug: coverdash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coverdash
tags:
- Insurtech
- Business Insurance
- Software-as-a-Service
- API Platform
- Small Business
website: https://www.coverdash.com/
---
