---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Astraluno Com Agentic Access
  operation_count: 9
  slug: astraluno-com-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- description: Free, read‑only tropical geocentric astrology and Whole Sign birth charts via MCP JSON‑RPC.
  name: Astraluno MCP API
  slug: astraluno-mcp
- baseURL: https://astraluno.com
  baseurl_source: declared
  description: The Chart API from Astraluno — 1 operation(s) for chart.
  name: Astraluno Chart API
  slug: astraluno-com-chart-api
- baseURL: https://astraluno.com
  baseurl_source: declared
  description: The Ingresses API from Astraluno — 1 operation(s) for ingresses.
  name: Astraluno Ingresses API
  slug: astraluno-com-ingresses-api
- baseURL: https://astraluno.com
  baseurl_source: declared
  description: The Lunations API from Astraluno — 1 operation(s) for lunations.
  name: Astraluno Lunations API
  slug: astraluno-com-lunations-api
- baseURL: https://astraluno.com
  baseurl_source: declared
  description: The Openapi.json API from Astraluno — 1 operation(s) for openapi.json.
  name: Astraluno Openapi.json API
  slug: astraluno-com-openapi-json-api
- baseURL: https://astraluno.com
  baseurl_source: declared
  description: The Places API from Astraluno — 1 operation(s) for places.
  name: Astraluno Places API
  slug: astraluno-com-places-api
- baseURL: https://astraluno.com
  baseurl_source: declared
  description: The Readings API from Astraluno — 1 operation(s) for readings.
  name: Astraluno Readings API
  slug: astraluno-com-readings-api
- baseURL: https://astraluno.com
  baseurl_source: declared
  description: The Retrogrades API from Astraluno — 1 operation(s) for retrogrades.
  name: Astraluno Retrogrades API
  slug: astraluno-com-retrogrades-api
- baseURL: https://astraluno.com
  baseurl_source: declared
  description: The Sky API from Astraluno — 1 operation(s) for sky.
  name: Astraluno Sky API
  slug: astraluno-com-sky-api
- baseURL: https://astraluno.com
  baseurl_source: declared
  description: The Sun Sign API from Astraluno — 1 operation(s) for sun sign.
  name: Astraluno Sun Sign API
  slug: astraluno-com-sun-sign-api
artifact_total: 28
common:
- group: agent
  href: https://artifacts.apis.io/astraluno-com/agentic-access/astraluno-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/astraluno-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/astraluno-com/rate-limits/astraluno-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/astraluno-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/astraluno-com/rules/astraluno-com-rules.yml
  title: ''
  type: Spectral
  url: rules/astraluno-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/astraluno-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/astraluno-com/errors/astraluno-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/astraluno-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/astraluno-com/conformance/astraluno-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astraluno-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/astraluno-com/llms/astraluno-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astraluno-com-llms.txt
- group: build
  href: https://artifacts.apis.io/astraluno-com/mcp/astraluno-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/astraluno-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/astraluno-com/mcp/astraluno-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/astraluno-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/astraluno-com/hosts/astraluno-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astraluno-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/astraluno-com/security/astraluno-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astraluno-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astraluno.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astraluno.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astraluno.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astraluno.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astraluno.com/terms/
coverage:
  checked: '2026-11-02'
  detail: The provider’s public developer portal describes an API but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://astraluno.com/api/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Astraluno offers a free, browser‑based birth chart calculator that generates detailed astrological readings, including Sun, Moon, and rising sign positions. The service runs entirely client‑side, does not store personal data, and provides a REST‑style API for developers to integrate chart calculations into their applications. It supports up to 60 compute or MCP POST requests per minute per IP and enforces CORS without credentials.
image: https://astraluno.com/og/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at astraluno.com.
  name: Astraluno MCP Server
  slug: astraluno-com-mcp-yml
modified: '2026-11-01'
name: Astraluno
nav: Providers
network: true
overview: 'Astraluno publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chart API, Ingresses API, Lunations API, and 7 more. Tagged areas include Astrology, BirthChart, and Horoscope.


  The Astraluno catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Astraluno Com Plans Pricing
  plan_count: 0
  slug: astraluno-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Astraluno Com Rate Limits
  slug: astraluno-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Astraluno API Rules
  rule_count: 41
  severity_counts:
    error: 30
    hint: 0
    info: 9
    warn: 2
  slug: astraluno-com-rules
scopes:
- name: Astraluno Com Scopes
  scope_count: 0
  slug: astraluno-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 44.5
    catalog_earned_first_party: 8.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 46.2
    developer_ergonomics: 11.2
    discoverability: 56.7
    operational_transparency: 21.1
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Astraluno Com Authentication
  slug: astraluno-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Astraluno Com Domain Security
  slug: astraluno-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 10
skills:
- name: chart
  slug: astraluno-com-chart
- name: ingresses
  slug: astraluno-com-ingresses
- name: lunations
  slug: astraluno-com-lunations
- name: openapi
  slug: astraluno-com-openapi
- name: places
  slug: astraluno-com-places
- name: readings-kind-key
  slug: astraluno-com-readings-kind-key
- name: retrogrades
  slug: astraluno-com-retrogrades
- name: sky
  slug: astraluno-com-sky
- name: sun-sign
  slug: astraluno-com-sun-sign
- name: sun-sign
  slug: astraluno-com-sun_sign
slug: astraluno-com
tags:
- Astrology
- BirthChart
- Horoscope
website: https://astraluno.com/
---
