---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Crosbynews Com Agentic Access
  operation_count: 11
  slug: crosbynews-com-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- description: Provides weather, water, alerts, and community data for Crosby, Texas.
  name: Crosby News API
  slug: crosby-news-api
- baseURL: https://crosbynews.com
  baseurl_source: declared
  description: The Air API from Crosby News — 1 operation(s) for air.
  name: Crosby News Air API
  slug: crosbynews-com-air-api
- baseURL: https://crosbynews.com
  baseurl_source: declared
  description: The Burn Ban API from Crosby News — 1 operation(s) for burn ban.
  name: Crosby News Burn Ban API
  slug: crosbynews-com-burn-ban-api
- baseURL: https://crosbynews.com
  baseurl_source: declared
  description: The Calendar API from Crosby News — 1 operation(s) for calendar.
  name: Crosby News Calendar API
  slug: crosbynews-com-calendar-api
- baseURL: https://crosbynews.com
  baseurl_source: declared
  description: The Fishing API from Crosby News — 1 operation(s) for fishing.
  name: Crosby News Fishing API
  slug: crosbynews-com-fishing-api
- baseURL: https://crosbynews.com
  baseurl_source: declared
  description: The Health API from Crosby News — 1 operation(s) for health.
  name: Crosby News Health API
  slug: crosbynews-com-health-api
- baseURL: https://crosbynews.com
  baseurl_source: declared
  description: The News API from Crosby News — 1 operation(s) for news.
  name: Crosby News News API
  slug: crosbynews-com-news-api
- baseURL: https://crosbynews.com
  baseurl_source: declared
  description: The Pollen API from Crosby News — 1 operation(s) for pollen.
  name: Crosby News Pollen API
  slug: crosbynews-com-pollen-api
- baseURL: https://crosbynews.com
  baseurl_source: declared
  description: The Traffic API from Crosby News — 1 operation(s) for traffic.
  name: Crosby News Traffic API
  slug: crosbynews-com-traffic-api
- baseURL: https://crosbynews.com
  baseurl_source: declared
  description: The Tropics API from Crosby News — 1 operation(s) for tropics.
  name: Crosby News Tropics API
  slug: crosbynews-com-tropics-api
- baseURL: https://crosbynews.com
  baseurl_source: declared
  description: The Water API from Crosby News — 1 operation(s) for water.
  name: Crosby News Water API
  slug: crosbynews-com-water-api
- baseURL: https://crosbynews.com
  baseurl_source: declared
  description: The Weather API from Crosby News — 1 operation(s) for weather.
  name: Crosby News Weather API
  slug: crosbynews-com-weather-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/crosbynews-com/agentic-access/crosbynews-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crosbynews-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/crosbynews-com/rules/crosbynews-com-rules.yml
  title: ''
  type: Spectral
  url: rules/crosbynews-com-rules.yml
- group: design
  href: https://artifacts.apis.io/crosbynews-com/json-ld/crosbynews-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crosbynews-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/crosbynews-com/vocabulary/crosbynews-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crosbynews-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/crosbynews-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/crosbynews-com/data-model/crosbynews-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crosbynews-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/crosbynews-com/security/crosbynews-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/crosbynews-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/crosbynews-com/errors/crosbynews-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crosbynews-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crosbynews-com/conformance/crosbynews-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crosbynews-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crosbynews-com/llms/crosbynews-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crosbynews-com-llms.txt
- group: build
  href: https://artifacts.apis.io/crosbynews-com/mcp/crosbynews-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/crosbynews-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/crosbynews-com/mcp/crosbynews-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crosbynews-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/crosbynews-com/well-known/crosbynews-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crosbynews-com-security.txt
- group: agent
  href: https://artifacts.apis.io/crosbynews-com/well-known/crosbynews-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crosbynews-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/crosbynews-com/hosts/crosbynews-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crosbynews-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/crosbynews-com/vendors/crosbynews-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crosbynews-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://crosbynews.com/news
- group: auth
  href: https://artifacts.apis.io/crosbynews-com/security/crosbynews-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crosbynews-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crosbynews-com/security/crosbynews-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crosbynews-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crosbynews.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://crosbynews.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://crosbynews.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://crosbynews.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://crosbynews.com/developers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crosbynews.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://crosbynews.com/contact
created: '2026-11-04'
description: Crosby News provides localized weather, water, news, and community information for Crosby, Texas. The site offers forecasts, radar, alerts, water levels, fishing conditions, pollen counts, air quality, burn bans, traffic updates, school calendars, and emergency notices. It serves residents with up-to-date environmental data and community news, supporting informed decisions about daily activities and safety.
image: https://crosbynews.com/og-image.png
jsonld:
- class_count: 21
  name: Crosbynews Com Context
  property_count: 122
  slug: crosbynews-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at crosbynews.com.
  name: Crosby News MCP Server
  slug: crosbynews-com-mcp-yml
modified: '2026-11-04'
name: Crosby News
nav: Providers
network: true
overview: 'Crosby News publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Air API, Burn Ban API, Calendar API, and 9 more. Tagged areas include Company.


  The Crosby News catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Crosby News'' developer surface includes documentation, API reference, getting-started guide, support, and 22 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Crosby News API Rules
  rule_count: 37
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 2
  slug: crosbynews-com-rules
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 49.0
    developer_ergonomics: 49.3
    discoverability: 58.3
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crosbynews Com Domain Security
  slug: crosbynews-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Crosbynews Com Vulnerability Disclosure
  slug: crosbynews-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crosbynews-com
tags:
- Company
website: https://crosbynews.com/
---
