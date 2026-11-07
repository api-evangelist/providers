---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Anecast provides daily weather forecasts for US cities via its website.
  name: Anecast API
  slug: anecast-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/anecast-app/mcp/anecast-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anecast-app-mcp.yml
- group: other
  href: https://artifacts.apis.io/anecast-app/hosts/anecast-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anecast-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/anecast-app/vendors/anecast-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anecast-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/anecast-app/security/anecast-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anecast-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anecast.app/
- group: operate
  title: ''
  type: Support
  url: https://www.anecast.app/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anecast.app/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.anecast.app/subscribe
coverage:
  checked: '2026-11-01'
  detail: The provider's website offers weather forecasts but no public machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.anecast.app/
  - status: 404
    url: https://www.anecast.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Anecast is a small, independent weather publication that delivers a daily morning forecast for 39 US cities. Each story is built from raw data saved first, preserving exact inputs. The numbers shown blend official forecasts with model outputs, and the site displays yesterday’s forecast alongside the official prediction. Founded by Brendan Heberton, the creator of Weather5280, Anecast aims to provide better weather insight. Users can subscribe to receive a daily email with changes, unusual conditions, and a recap of yesterday’s weather.
image: https://www.anecast.app/favicon-32.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.anecast.app.
  name: Anecast MCP Server
  slug: anecast-app-mcp-yml
modified: '2026-11-01'
name: Anecast
nav: Providers
network: true
overview: 'Anecast is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather, Publication, Forecast, Independent, and Weather Data.


  Anecast''s developer surface includes support, signup flow, and 6 more developer resources.'
plans:
- name: Anecast App Plans Pricing
  plan_count: 0
  slug: anecast-app-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Anecast App Rate Limits
  slug: anecast-app-rate-limits
scopes:
- name: Anecast App Scopes
  scope_count: 0
  slug: anecast-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 12.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anecast App Authentication
  slug: anecast-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anecast App Domain Security
  slug: anecast-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: anecast-app
tags:
- Weather
- Publication
- Forecast
- Independent
- Weather Data
website: https://anecast.app/
---
