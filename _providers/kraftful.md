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
- description: Kraftful provides a developer API documented at the Kraftful help center.
  name: Kraftful API
  slug: kraftful-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kraftful/refs/heads/main/vendors/kraftful-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kraftful-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kraftful/refs/heads/main/a2a/kraftful-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kraftful-a2a.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kraftful/refs/heads/main/hosts/kraftful-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kraftful-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kraftful.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kraftful/refs/heads/main/security/kraftful-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kraftful-domain-security.yml
coverage:
  checked: '2026-10-12'
  detail: OpenAPI spec not found at known endpoints; docs are markdown without machine-readable spec.
  evidence:
  - status: 404
    url: https://docs.kraftful.com/api-reference/openapi.json
  - status: 200
    url: https://docs.kraftful.com/start.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Kraftful is a startup focused on providing a platform for managing smart home devices and IoT integrations. The company offers APIs that enable developers to connect, control, and monitor a variety of connected products, aiming to simplify the creation of unified smart home experiences. Backed by leadout-capital, Kraftful targets both consumer and enterprise markets, delivering tools for device onboarding, state synchronization, and automation workflows.
layout: provider
modified: '2026-10-12'
name: Kraftful
nav: Providers
network: true
overview: 'Kraftful is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Smart Home, Platform, and Startups.


  Kraftful''s developer surface includes documentation and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.9
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
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kraftful Domain Security
  slug: kraftful-domain-security
  summary_line: TLSv1.3
slug: kraftful
tags:
- Company
- IoT
- Smart Home
- Platform
- Startups
---
