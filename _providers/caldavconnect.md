---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: CalDAVConnect provides calendar synchronization via CalDAV; documentation is available but no machine‑readable API contract was found.
  name: CalDAVConnect API
  slug: caldavconnect-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/caldavconnect/refs/heads/main/plans/caldavconnect-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/caldavconnect-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caldavconnect/refs/heads/main/authentication/caldavconnect-authentication.yml
  title: ''
  type: Authentication
  url: authentication/caldavconnect-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caldavconnect/refs/heads/main/llms/caldavconnect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caldavconnect-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caldavconnect/refs/heads/main/hosts/caldavconnect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caldavconnect-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://caldavconnect.de/de/login
- group: start
  title: ''
  type: GettingStarted
  url: https://caldavconnect.de/de/docs/getting-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caldavconnect/refs/heads/main/security/caldavconnect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caldavconnect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caldavconnect.de/
- group: docs
  title: ''
  type: Documentation
  url: https://caldavconnect.de/en/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://caldavconnect.de/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://caldavconnect.de/en/blog
- group: operate
  title: ''
  type: Support
  url: https://caldavconnect.de/en/login
coverage:
  checked: '2026-10-16'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was discovered on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.caldavconnect.de/openapi.json
  - status: 404
    url: https://caldavconnect.de/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Mediakreativ UG provides CalDAVConnect, a service that synchronizes CalDAV calendars with major platforms such as Google Calendar and Microsoft 365. Hosted in Germany, it supports Nextcloud, SOGo, Radicale, Baïkal, Synology, Infomaniak and more, offering GDPR‑compliant calendar syncing for individuals and businesses. Users can start a free trial, choose from various plans, and access comprehensive documentation and support.
image: https://caldavconnect.de/images/og-default.png
layout: provider
modified: '2026-10-16'
name: Mediakreativ UG
nav: Providers
network: true
overview: 'Mediakreativ UG is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CalDAV, Sync, Calendar, and GDPR.


  Mediakreativ UG''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, support, and 6 more developer resources.'
plans:
- name: Caldavconnect Plans Pricing
  plan_count: 4
  slug: caldavconnect-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Caldavconnect Authentication
  slug: caldavconnect-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Caldavconnect Domain Security
  slug: caldavconnect-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: caldavconnect
tags:
- Company
- CalDAV
- Sync
- Calendar
- GDPR
website: https://caldavconnect.de/
---
