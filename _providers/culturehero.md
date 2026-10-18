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
- description: Culturehero API
  name: Culturehero API
  slug: culturehero-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/culturehero/refs/heads/main/llms/culturehero-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/culturehero-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/culturehero/refs/heads/main/hosts/culturehero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/culturehero-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/culturehero/refs/heads/main/vendors/culturehero-vendors.yml
  title: ''
  type: Vendors
  url: vendors/culturehero-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.culturehero.co/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/culturehero/refs/heads/main/security/culturehero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/culturehero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.culturehero.co
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the API host.
  evidence:
  - status: 0
    url: https://api.culturehero.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Transform workplace culture with Culture Hero's expert solutions. We specialise in workplace culture improvement, team collaboration, employee engagement strategies, and leadership development. Our tailored workshops, executive coaching, and research-backed programs drive productivity, employee retention, and organizational success.
image: https://static.wixstatic.com/media/db8e88_c26f5ceb29754e08870133cdca36a810%7Emv2.png/v1/fit/w_2500,h_1330,al_c/db8e88_c26f5ceb29754e08870133cdca36a810%7Emv2.png
layout: provider
modified: '2026-10-12'
name: Culturehero
nav: Providers
network: true
overview: Culturehero is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Employee Engagement, Mental Health, Leadership Development, Workshops, and Consulting.
random_paper: 14
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Culturehero Domain Security
  slug: culturehero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: culturehero
tags:
- Employee Engagement
- Mental Health
- Leadership Development
- Workshops
- Consulting
- Culture Programs
website: https://www.culturehero.co
---
