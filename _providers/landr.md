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
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: API for LANDR services (mastering, distribution, samples).
  name: LANDR API
  slug: landr-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/landr/refs/heads/main/well-known/landr-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/landr-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/landr/refs/heads/main/well-known/landr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/landr-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/landr/refs/heads/main/hosts/landr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/landr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/landr/refs/heads/main/vendors/landr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/landr-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.landr.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.landr.com/en/press/?utm_source=blog&utm_medium=organic_post&utm_campaign=Engagement_General_EN_Core_Blog&utm_term=BlogFooter&utm_content=PressPage
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/landr/refs/heads/main/security/landr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/landr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://landr.com/
- group: operate
  title: ''
  type: Support
  url: https://support.landr.com
- group: company
  title: ''
  type: Blog
  url: https://blog.landr.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.landr.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.landr.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.landr.com/privacy
coverage:
  checked: 2026-09-23
  detail: API documentation redirects to a partner login page requiring credentials.
  evidence:
  - status: 200
    url: https://app.landr.com/api-docs
  reason: partner-login
  state: gated
created: '2026-09-23'
description: LANDR is a creative platform for musicians offering AI‑powered mastering, distribution, sample libraries, plugins, and collaborative tools. It provides a suite of services including LANDR Studio, mastering plugins, a marketplace for samples and plugins, online courses, and tools for music creators to release and monetize their work worldwide.
layout: provider
modified: '2026-09-23'
name: LANDR
nav: Providers
network: true
overview: 'LANDR publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Artificial Intelligence, Audio, and Distribution.


  LANDR''s developer surface includes support, engineering blog, pricing, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.6
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Landr Domain Security
  slug: landr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: landr
tags:
- Company
- Music
- Artificial Intelligence
- Audio
- Distribution
website: https://landr.com/
---
