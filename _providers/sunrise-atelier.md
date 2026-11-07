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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://time.now/developer/api
  baseurl_source: declared
  description: The Ip API from Sunrise Atelier — 2 operation(s) for ip.
  name: Sunrise Atelier Ip API
  slug: sunrise-atelier-ip-api
- baseURL: https://time.now/developer/api
  baseurl_source: declared
  description: The Timezone API from Sunrise Atelier — 2 operation(s) for timezone.
  name: Sunrise Atelier Timezone API
  slug: sunrise-atelier-timezone-api
artifact_total: 8
collections:
- collection_type: open
  name: Sunrise.am World Time Ip API
  slug: open-sunrise-atelier-ip-api
- collection_type: open
  name: Sunrise.am World Time Ip Timezone API
  slug: open-sunrise-atelier-timezone-api
common:
- group: company
  title: ''
  type: Blog
  url: https://sunrise.am/articles/
- group: agent
  href: https://artifacts.apis.io/sunrise-atelier/mcp/sunrise-atelier-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sunrise-atelier-mcp.yml
- group: other
  href: https://artifacts.apis.io/sunrise-atelier/overlays/sunrise-atelier-world-time-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sunrise-atelier-world-time-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/sunrise-atelier/security/sunrise-atelier-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sunrise-atelier-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/sunrise-atelier/llms/sunrise-atelier-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sunrise-atelier-llms.txt
- group: agent
  href: https://artifacts.apis.io/sunrise-atelier/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://sunrise.am
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sunrise.am/developer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sunrise.am/info/terms-privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sunrise.am/info/terms-privacy
- group: operate
  title: ''
  type: Support
  url: https://sunrise.am/info/contact
created: '2026-07-17'
description: Sunrise Atelier operates Sunrise.am, a free consumer service that provides accurate sunrise, sunset, twilight, golden-hour and daylight times for every city and country worldwide, plus a solar calendar, an online clock, and educational articles. For developers, Sunrise.am publishes a free public World Time API (documented at https://sunrise.am/developer and served from the time.now host) that returns the current time, timezone information, daylight-saving data, and IP-based time geolocation as clean JSON with no API key required and CORS enabled. Surfaced as a portfolio company of 500 Global and enriched in the API Evangelist network from its live developer surface.
image: https://sunrise.am/static/sunrise-am-og.png
layout: provider
modified: '2026-10-06'
name: Sunrise Atelier
nav: Providers
network: true
overview: 'Sunrise Atelier publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Ip API and Timezone API. Tagged areas include Company, Time, Timezone, Astronomy, and Geolocation.


  The Sunrise Atelier catalog on APIs.io includes 1 Spectral governance ruleset.


  Sunrise Atelier''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Sunrise Atelier API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: sunrise-atelier-rules
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.1
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 47.0
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 44.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
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
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/sunrise-atelier/sunrise-atelier-2026-09-02T161146.png
security:
- kind: authentication
  name: Sunrise Atelier Authentication
  slug: sunrise-atelier-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sunrise Atelier Domain Security
  slug: sunrise-atelier-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: sunrise-atelier-get-current-time
  slug: sunrise-atelier-get-current-time
slug: sunrise-atelier
tags:
- Company
- Time
- Timezone
- Astronomy
- Geolocation
- Sunrise
- Sunset
- Developer API
website: https://sunrise.am
---
