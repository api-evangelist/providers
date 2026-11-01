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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/letsmend-com/hosts/letsmend-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/letsmend-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/letsmend-com/vendors/letsmend-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/letsmend-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/letsmend
- group: auth
  href: https://artifacts.apis.io/letsmend-com/security/letsmend-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/letsmend-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://letsmend.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.letsmend.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.letsmend.com/terms
coverage:
  checked: '2026-10-29'
  detail: Unable to retrieve OpenAPI spec from https://api.letsmend.com despite probing known endpoints.
  evidence:
  - status: network_error
    url: https://api.letsmend.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Mend provides a digital platform that helps individuals navigate breakups and relationship challenges through personalized advice, journaling tools, and community support. The service offers curated content, mental‑health resources, and interactive features designed to aid emotional recovery and personal growth after a relationship ends.
image: https://cdn.prod.website-files.com/6282d4ebdc8ff2090ba2f90d/62c5ffe1d1e959671b99bc57_logo_green_text.png
layout: provider
modified: '2026-10-29'
name: Mend
nav: Providers
network: true
overview: Mend is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Breakup, MentalHealth, Advice, and Community.
random_paper: 0
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Letsmend Com Domain Security
  slug: letsmend-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: letsmend-com
tags:
- Company
- Breakup
- MentalHealth
- Advice
- Community
website: https://letsmend.com
---
