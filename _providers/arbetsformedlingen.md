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
- description: Public employment service API (no machine-readable spec found)
  name: Arbetsförmedlingen API
  slug: arbetsf-rmedlingen-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arbetsformedlingen/refs/heads/main/security/arbetsformedlingen-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/arbetsformedlingen-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arbetsformedlingen/refs/heads/main/well-known/arbetsformedlingen-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arbetsformedlingen-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arbetsformedlingen/refs/heads/main/well-known/arbetsformedlingen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arbetsformedlingen-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arbetsformedlingen/refs/heads/main/hosts/arbetsformedlingen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arbetsformedlingen-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arbetsformedlingen/refs/heads/main/vendors/arbetsformedlingen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arbetsformedlingen-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/arbetsformedlingen/refs/heads/main/packages/arbetsformedlingen-packages.yml
  title: ''
  type: SDKs
  url: packages/arbetsformedlingen-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/arbetsformedlingen/refs/heads/main/packages/arbetsformedlingen-packages.yml
  title: ''
  type: Packages
  url: packages/arbetsformedlingen-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://arbetsformedlingen.se/om-oss/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arbetsformedlingen
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arbetsformedlingen/refs/heads/main/security/arbetsformedlingen-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arbetsformedlingen-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arbetsformedlingen/refs/heads/main/security/arbetsformedlingen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arbetsformedlingen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arbetsformedlingen.se/
- group: docs
  title: ''
  type: Documentation
  url: https://data.arbetsformedlingen.se/
- group: docs
  title: ''
  type: APIReference
  url: https://arbetsformedlingen.se/other-languages/english-engelska/about-the-website/apis-and-open-data
- group: start
  title: ''
  type: GettingStarted
  url: https://arbetsformedlingen.se/for-arbetssokande/mina-sidor
- group: operate
  title: ''
  type: Support
  url: https://arbetsformedlingen.se/kontakt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arbetsformedlingen.se/om-webbplatsen/juridisk-information/sa-hanterar-vi-dina-personuppgifter
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://data.arbetsformedlingen.se/mcp
  - status: 200
    url: https://arbetsformedlingen.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Arbetsförmedlingen is Sweden’s public employment service, offering job seekers access to job listings, career guidance, and support programs, while providing employers tools for recruitment and labor market analytics. The agency operates a comprehensive digital platform (arbetsformedlingen.se) with multilingual support, extensive statistics, and services for municipalities and partners, aiming to improve employment outcomes across the country.
layout: provider
modified: '2026-10-15'
name: Arbetsförmedlingen
nav: Providers
network: true
overview: 'Arbetsförmedlingen is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employment, Government, Sweden, and JobSearch.


  Arbetsförmedlingen''s developer surface includes documentation, API reference, getting-started guide, support, and 13 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arbetsformedlingen Domain Security
  slug: arbetsformedlingen-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Arbetsformedlingen Vulnerability Disclosure
  slug: arbetsformedlingen-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arbetsformedlingen
tags:
- Company
- Employment
- Government
- Sweden
- JobSearch
website: https://arbetsformedlingen.se/
---
