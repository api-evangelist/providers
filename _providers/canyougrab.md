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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Bulk Domain Availability API
  name: CanYouGrab API
  slug: canyougrab-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/canyougrab/refs/heads/main/plans/canyougrab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canyougrab-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canyougrab/refs/heads/main/conformance/canyougrab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canyougrab-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canyougrab/refs/heads/main/overlays/canyougrab-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/canyougrab-openapi-overlay.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canyougrab/refs/heads/main/well-known/canyougrab-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canyougrab-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canyougrab/refs/heads/main/hosts/canyougrab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canyougrab-hosts.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.canyougrab.it
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canyougrab/refs/heads/main/security/canyougrab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canyougrab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canyougrab.it/
- group: docs
  title: ''
  type: Documentation
  url: https://canyougrab.it/docs
- group: operate
  title: ''
  type: Support
  url: https://canyougrab.it/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://canyougrab.it/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canyougrab.it/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://canyougrab.it/guides/check-domain-availability-api/
created: '2026-10-16'
description: canyougrab.it provides a Bulk Domain Availability API that allows users to check the availability of multiple domain names in a single request. Leveraging real-time DNS and WHOIS lookups, the service returns structured JSON responses indicating registration status, expiry dates, and registrar information. It offers a free tier with generous rate limits, supports up to 100 domains per batch, and is designed for developers needing reliable bulk domain checks for brand monitoring, domain portfolio management, or automated registration workflows.
image: https://canyougrab.it/og-image.png
layout: provider
modified: '2026-10-16'
name: canyougrab.it
nav: Providers
network: true
overview: 'canyougrab.it is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Domain, Bulk, DNS, and WHOIS.


  canyougrab.it''s developer surface includes documentation, support, getting-started guide, and 10 more developer resources.'
plans:
- name: Canyougrab Plans Pricing
  plan_count: 4
  slug: canyougrab-plans-pricing
random_paper: 11
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Canyougrab Domain Security
  slug: canyougrab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canyougrab
tags:
- Company
- Domain
- Bulk
- DNS
- WHOIS
website: https://canyougrab.it/
---
