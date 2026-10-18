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
  href: https://raw.githubusercontent.com/api-evangelist/surecheck/refs/heads/main/hosts/surecheck-hosts.yml
  title: ''
  type: Hosts
  url: hosts/surecheck-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/surecheck/refs/heads/main/vendors/surecheck-vendors.yml
  title: ''
  type: Vendors
  url: vendors/surecheck-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/surecheck/refs/heads/main/security/surecheck-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/surecheck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://surecheck-live-040.onrender.com
- group: docs
  title: ''
  type: Documentation
  url: https://surecheck-live-040.onrender.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://surecheck-live-040.onrender.com/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://surecheck-live-040.onrender.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://surecheck-live-040.onrender.com/privacy
created: '2026-10-14'
description: SureCheck provides a simple API for validating phone numbers and email addresses. It offers international phone formatting, carrier detection, and email syntax plus DNS checks, including disposable domain detection. The service runs on a free Render.com host, offering a free beta and paid plans for higher volume. It is designed for developers needing quick validation before storing user data.
layout: provider
modified: '2026-10-14'
name: SureCheck
nav: Providers
network: true
overview: 'SureCheck is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Validation, Phone, and Email.


  SureCheck''s developer surface includes documentation, API reference, and 6 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Surecheck Domain Security
  slug: surecheck-domain-security
  summary_line: TLSv1.3 · DMARC
slug: surecheck
tags:
- Company
- Validation
- Phone
- Email
website: https://surecheck-live-040.onrender.com
---
