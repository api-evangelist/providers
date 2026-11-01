---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/shearwell/hosts/shearwell-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shearwell-hosts.yml
- group: other
  href: https://artifacts.apis.io/shearwell/vendors/shearwell-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shearwell-vendors.yml
- group: auth
  href: https://artifacts.apis.io/shearwell/security/shearwell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shearwell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shearwell.co.uk/
- group: operate
  title: ''
  type: Support
  url: https://www.shearwell.co.uk/support
- group: company
  title: ''
  type: Blog
  url: https://www.shearwell.co.uk/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shearwell.co.uk/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shearwell.co.uk/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.shearwell.co.uk/login
coverage:
  checked: '2026-10-28'
  detail: No public developer program or API documentation was found on the website; attempts to locate API endpoints (e.g., /api, /developer) returned 404 and the sitemap contains no API links.
  evidence:
  - status: 404
    url: https://www.shearwell.co.uk/api
  - status: 404
    url: https://www.shearwell.co.uk/developer
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Shearwell Data, based in Wheddon Cross, Somerset, is a farmer‑owned company providing comprehensive livestock identification and management solutions. Since 1992 they have expanded from manufacturing animal tags to offering RFID/EID tags, handheld and race readers, software platforms, and data services that help farmers track up to 16,000 animals, improve breeding decisions, ensure accurate dosing, and enhance overall farm productivity worldwide.
image: https://media.shearwell.com/Content/UK/Images/Template/Logo/alidma-logo-430x100.png
layout: provider
modified: '2026-10-28'
name: Shearwell Data
nav: Providers
network: true
overview: 'Shearwell Data is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Livestock, Animal Identification, RFID, Farm Management, and UK.


  Shearwell Data''s developer surface includes support, engineering blog, signup flow, and 6 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 0
  name: Shearwell Rate Limits
  slug: shearwell-rate-limits
scopes:
- name: Shearwell Scopes
  scope_count: 0
  slug: shearwell-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Shearwell Authentication
  slug: shearwell-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Shearwell Domain Security
  slug: shearwell-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: shearwell
tags:
- Livestock
- Animal Identification
- RFID
- Farm Management
- UK
website: https://shearwell.co.uk/
---
