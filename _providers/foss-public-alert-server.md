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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: KDE provides a comprehensive API reference for its libraries and services.
  name: KDE API
  slug: kde-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: Security
  url: https://community.kde.org/Policies/Security_Policy
- group: agent
  href: https://artifacts.apis.io/foss-public-alert-server/well-known/foss-public-alert-server-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/foss-public-alert-server-well-known.yml
- group: other
  href: https://artifacts.apis.io/foss-public-alert-server/hosts/foss-public-alert-server-hosts.yml
  title: ''
  type: Hosts
  url: hosts/foss-public-alert-server-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kde.org/
- group: auth
  href: https://artifacts.apis.io/foss-public-alert-server/security/foss-public-alert-server-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/foss-public-alert-server-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/foss-public-alert-server/security/foss-public-alert-server-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/foss-public-alert-server-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alerts.kde.org/
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation at https://api.kde.org/ is public but offers no machine‑readable OpenAPI, GraphQL, or AsyncAPI specifications.
  evidence:
  - status: 200
    url: https://api.kde.org/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'FOSS Public Alert Server is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling. No public website or detailed information was found for this entity during probing, and the only URL associated (https://alerts.kde.org/) appears unrelated, returning a 400 error. Consequently, the description remains limited to its identification as a harvested stub without further publicly available details.'
layout: provider
modified: '2026-10-28'
name: FOSS Public Alert Server
nav: Providers
network: true
overview: 'FOSS Public Alert Server is listed with 1 API on the [APIs.io](https://apis.io/) network: KDE API. Tagged areas include Company, Alert, OpenSource, Monitoring, and Public.


  FOSS Public Alert Server''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Foss Public Alert Server Plans Pricing
  plan_count: 0
  slug: foss-public-alert-server-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Foss Public Alert Server Rate Limits
  slug: foss-public-alert-server-rate-limits
scopes:
- name: Foss Public Alert Server Scopes
  scope_count: 0
  slug: foss-public-alert-server-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 37.6
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Foss Public Alert Server Authentication
  slug: foss-public-alert-server-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Foss Public Alert Server Domain Security
  slug: foss-public-alert-server-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: Foss Public Alert Server Vulnerability Disclosure
  slug: foss-public-alert-server-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: foss-public-alert-server
tags:
- Company
- Alert
- OpenSource
- Monitoring
- Public
website: https://alerts.kde.org/
---
