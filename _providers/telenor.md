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
  href: https://raw.githubusercontent.com/api-evangelist/telenor/refs/heads/main/hosts/telenor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/telenor-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telenor.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telenor.com/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://www.telenor.com/media/newsroom/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/telenor/refs/heads/main/security/telenor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/telenor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.telenor.com/
coverage:
  checked: '2026-10-13'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was discoverable on api.telenor.com or related hosts.
  evidence:
  - status: 0
    url: https://api.telenor.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Telenor Group is a leading telecommunications operator headquartered in Norway, providing mobile, broadband, and TV services across Scandinavia, Eastern Europe, and Asia. The company focuses on digital transformation, connectivity, and sustainable business practices, serving millions of customers worldwide. It offers a range of consumer and enterprise solutions, including IoT platforms, cloud services, and digital payment options, reflecting its commitment to innovation and responsible growth.
image: https://www.telenor.com/binaries/media/newsroom/Telenor-Symbol-on-dark-blue-background.jpg?w=879&h=585&mimeType=original
layout: provider
modified: '2026-10-13'
name: Telenor
nav: Providers
network: true
overview: Telenor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Norway, Mobile, Broadband, and Enterprise.
random_paper: 13
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 4
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
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 11.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Telenor Domain Security
  slug: telenor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telenor
tags:
- Telecommunications
- Norway
- Mobile
- Broadband
- Enterprise
website: https://www.telenor.com/
---
