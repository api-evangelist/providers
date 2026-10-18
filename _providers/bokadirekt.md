---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.bokadirekt.se/articles/security-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bokadirekt/refs/heads/main/llms/bokadirekt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bokadirekt-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bokadirekt/refs/heads/main/well-known/bokadirekt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bokadirekt-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bokadirekt/refs/heads/main/well-known/bokadirekt-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bokadirekt-help-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bokadirekt/refs/heads/main/well-known/bokadirekt-business-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bokadirekt-business-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bokadirekt/refs/heads/main/well-known/bokadirekt-bokadirekt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bokadirekt-bokadirekt-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bokadirekt/refs/heads/main/well-known/bokadirekt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bokadirekt-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bokadirekt/refs/heads/main/hosts/bokadirekt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bokadirekt-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bokadirekt/refs/heads/main/vendors/bokadirekt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bokadirekt-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.bokadirekt.se/support
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.bokadirekt.se/
- group: docs
  title: ''
  type: Documentation
  url: https://help.bokadirekt.se/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bokadirekt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bokadirekt/refs/heads/main/security/bokadirekt-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bokadirekt-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bokadirekt/refs/heads/main/security/bokadirekt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bokadirekt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bokadirekt.se/
- group: docs
  title: ''
  type: APIReference
  url: https://www.bokadirekt.se/api/
coverage:
  checked: '2026-10-15'
  detail: Documentation is provided as HTML pages without a machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contract.
  evidence:
  - status: 200
    url: https://help.bokadirekt.se/sv/collections/2792293-bokadirekt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Bokadirekt is a Swedish online platform that connects customers with beauty and wellness service providers such as massage therapists, naprapaths, hairdressers and more. Users can search for nearby professionals, view availability, and book appointments directly through the website. The service aims to simplify finding and scheduling personal care treatments, offering a convenient digital marketplace for both clients and service providers across Sweden.
image: https://www.bokadirekt.se/images/home-background.jpeg
layout: provider
modified: '2026-10-15'
name: Bokadirekt
nav: Providers
network: true
overview: 'Bokadirekt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beauty, Wellness, Booking, and Sweden.


  Bokadirekt''s developer surface includes support, documentation, API reference, and 14 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bokadirekt Domain Security
  slug: bokadirekt-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bokadirekt Vulnerability Disclosure
  slug: bokadirekt-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bokadirekt
tags:
- Company
- Beauty
- Wellness
- Booking
- Sweden
website: https://bokadirekt.se/
---
