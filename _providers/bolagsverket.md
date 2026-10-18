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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bolagsverket/refs/heads/main/security/bolagsverket-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bolagsverket-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bolagsverket/refs/heads/main/well-known/bolagsverket-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bolagsverket-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bolagsverket/refs/heads/main/well-known/bolagsverket-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bolagsverket-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bolagsverket/refs/heads/main/hosts/bolagsverket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bolagsverket-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bolagsverket/refs/heads/main/vendors/bolagsverket-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bolagsverket-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bolagsverket
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bolagsverket/refs/heads/main/security/bolagsverket-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bolagsverket-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bolagsverket/refs/heads/main/security/bolagsverket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bolagsverket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bolagsverket.se/
- group: docs
  title: ''
  type: Documentation
  url: https://bolagsverket.se/apierochoppnadata.2531.html
- group: docs
  title: ''
  type: APIReference
  url: https://bolagsverket.se/apierochoppnadata.2531.html
- group: start
  title: ''
  type: GettingStarted
  url: https://bolagsverket.se/apierochoppnadata/hamtaforetagsinformation.5841.html
- group: operate
  title: ''
  type: Support
  url: https://bolagsverket.se/omoss/kontaktaoss.2049.html
- group: company
  title: ''
  type: Blog
  url: https://bolagsverket.se/nyheterochreleaser.5497.html
- group: commercial
  title: ''
  type: Pricing
  url: https://bolagsverket.se/apierochoppnadata.2531.html
- group: start
  title: ''
  type: SignUp
  url: https://bolagsverket.se/apierochoppnadata/hamtaforetagsinformation.5841.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/bolagsverket/workspace
coverage:
  checked: '2026-10-15'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://bolagsverket.se/apierochoppnadata.2531.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Bolagsverket is Sweden’s official register of companies, providing public access to corporate information, filings, and open data APIs. It enables businesses, authorities, and developers to retrieve and submit company data such as registration details, annual reports, and ownership information. The agency supports digital services for company formation, changes, and compliance, offering both free and fee‑based APIs, downloadable datasets, and XML feeds for integration into external systems.
image: https://bolagsverket.se/images/18.6535432417e0f20712753fb6/1643036634043/bolagsverket-logotype-social.png
layout: provider
modified: '2026-10-15'
name: Bolagsverket
nav: Providers
network: true
overview: 'Bolagsverket is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Registry, Sweden, and Business.


  Bolagsverket''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 10 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bolagsverket Domain Security
  slug: bolagsverket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bolagsverket Vulnerability Disclosure
  slug: bolagsverket-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bolagsverket
tags:
- Company
- Government
- Registry
- Sweden
- Business
website: https://bolagsverket.se/
---
