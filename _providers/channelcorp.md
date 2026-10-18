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
- description: Channelcorp does not expose a public API.
  name: Channelcorp API
  slug: channelcorp-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/channelcorp/refs/heads/main/hosts/channelcorp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/channelcorp-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/channelcorp/refs/heads/main/vendors/channelcorp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/channelcorp-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/channelcorp/refs/heads/main/security/channelcorp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/channelcorp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://channelcor.com
coverage:
  checked: '2026-10-08'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.channelcor.com/openapi.json
  - status: 404
    url: https://channelcor.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Channelcorp is a global leader in channel economics, partner finance, and channel growth consulting. Founded in 1989 and based in Vancouver, Canada, it provides strategic education, in‑house executive training, and public workshops across 29 countries, helping technology vendors and partners improve performance and revenue.
image: https://channelcor.com/wp-content/uploads/2026/03/cropped-LIUC-logos-1-1-150x150.png
layout: provider
modified: '2026-10-08'
name: Channelcorp
nav: Providers
network: true
overview: Channelcorp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consulting, Channel Economics, Partner Finance, and AI Tools.
random_paper: 21
score:
  band: minimal
  composite: 4.3
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
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Channelcorp Domain Security
  slug: channelcorp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: channelcorp
tags:
- Company
- Consulting
- Channel Economics
- Partner Finance
- AI Tools
website: https://channelcor.com
---
