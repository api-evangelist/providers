---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://smartproxy.com/'', ''status'': 301, ''note'': ''declared website redirects to https://decodo.com/ — a different registrable domain (smartproxy.com -> decodo.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Smartproxy Agentic Access
  operation_count: 13
  slug: smartproxy-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.decodo.com/v1
  baseurl_source: spec
  description: Authenticate and obtain API access tokens
  name: Smartproxy Authentication API
  slug: smartproxy-authentication-api
- baseURL: https://api.decodo.com/v1
  baseurl_source: spec
  description: Discover available proxy endpoints and ports
  name: Smartproxy Endpoints API
  slug: smartproxy-endpoints-api
- baseURL: https://api.decodo.com/v1
  baseurl_source: spec
  description: View subscription details and limits
  name: Smartproxy Subscriptions API
  slug: smartproxy-subscriptions-api
- baseURL: https://api.decodo.com/v1
  baseurl_source: spec
  description: Monitor and control proxy traffic usage
  name: Smartproxy Traffic API
  slug: smartproxy-traffic-api
- baseURL: https://api.decodo.com/v1
  baseurl_source: spec
  description: Manage IP whitelist for proxy authentication
  name: Smartproxy Whitelisted IPs API
  slug: smartproxy-whitelisted-ips-api
- baseURL: https://api.decodo.com/v1
  baseurl_source: spec
  description: Manage proxy sub-user accounts
  name: Smartproxy Subusers API
  slug: smartproxy-subusers-api
artifact_total: 27
collections:
- collection_type: open
  name: Smartproxy Authentication API
  slug: open-smartproxy-authentication-api
- collection_type: open
  name: Smartproxy Authentication Endpoints API
  slug: open-smartproxy-endpoints-api
- collection_type: open
  name: Smartproxy Authentication Sub-Users API
  slug: open-smartproxy-sub-users-api
- collection_type: open
  name: Smartproxy Authentication Subscriptions API
  slug: open-smartproxy-subscriptions-api
- collection_type: open
  name: Smartproxy Authentication Traffic API
  slug: open-smartproxy-traffic-api
- collection_type: open
  name: Smartproxy Authentication Whitelisted IPs API
  slug: open-smartproxy-whitelisted-ips-api
- collection_type: open
  name: Smartproxy API
  slug: open-smartproxy
common:
- group: commercial
  href: https://artifacts.apis.io/smartproxy/plans/smartproxy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smartproxy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/smartproxy/rate-limits/smartproxy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/smartproxy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/smartproxy/finops/smartproxy-finops.yml
  title: ''
  type: FinOps
  url: finops/smartproxy-finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Smartproxy/Smartproxy-API/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Decodo/Decodo-API/blob/master/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Smartproxy/Smartproxy-API/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/smartproxy/agentic-access/smartproxy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/smartproxy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/smartproxy/security/smartproxy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smartproxy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/smartproxy/authentication/smartproxy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smartproxy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smartproxy
- group: company
  title: ''
  type: Website
  url: https://smartproxy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.smartproxy.com/reference/introduction-1
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Smartproxy
- group: commercial
  title: ''
  type: Pricing
  url: https://smartproxy.com/proxies/residential-proxies
- group: docs
  href: https://artifacts.apis.io/smartproxy/openapi/_original/smartproxy-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/smartproxy-openapi.yml
- group: design
  href: https://artifacts.apis.io/smartproxy/rules/smartproxy-rules.yml
  title: ''
  type: Spectral
  url: rules/smartproxy-rules.yml
- group: docs
  href: https://artifacts.apis.io/smartproxy/json-schema/smartproxy-sub-user-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/smartproxy-sub-user-schema.json
- group: docs
  href: https://artifacts.apis.io/smartproxy/json-schema/smartproxy-endpoint-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/smartproxy-endpoint-schema.json
- group: design
  href: https://artifacts.apis.io/smartproxy/json-structure/smartproxy-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/smartproxy-structure.json
- group: design
  href: https://artifacts.apis.io/smartproxy/json-ld/smartproxy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/smartproxy-context.jsonld
- group: design
  href: https://artifacts.apis.io/smartproxy/vocabulary/smartproxy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/smartproxy-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://decodo.com/blog
created: '2026-03-29'
description: Smartproxy (now also known as Decodo) is a proxy network and web scraping infrastructure platform providing residential, datacenter, mobile, and ISP proxies for web data collection at scale. The Smartproxy API enables programmatic management of proxy accounts, sub-users, traffic allocation, IP whitelisting, and endpoint discovery. The platform supports both rotating and sticky session proxy connections across global geographic locations.
examples:
- key_count: 2
  name: Smartproxy Create Sub User Example
  slug: smartproxy-create-sub-user-example
- key_count: 2
  name: Smartproxy Get Sub Users Example
  slug: smartproxy-get-sub-users-example
finops:
- has_sources: false
  method: generated
  name: Smartproxy Finops
  primary_unit: request
  service_category: API
  slug: smartproxy-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartproxy.png
json_schemas:
- name: Smartproxy Endpoint
  property_count: 5
  slug: smartproxy-endpoint
- name: Smartproxy Sub-User
  property_count: 7
  slug: smartproxy-sub-user
json_structures:
- name: Smartproxy Structure
  property_count: 0
  slug: smartproxy-structure
jsonld:
- class_count: 11
  name: Smartproxy Context
  property_count: 8
  slug: smartproxy-context
layout: provider
modified: '2026-05-19'
name: Smartproxy
nav: Providers
network: true
overview: 'Smartproxy publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Endpoints API, Subscriptions API, and 3 more. Tagged areas include Proxies, Web Scraping, Data Collection, Residential Proxies, and Datacenter Proxies.


  The Smartproxy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Smartproxy''s developer surface includes authentication, documentation, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Smartproxy Plans Pricing
  plan_count: 3
  slug: smartproxy-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Smartproxy Rate Limits
  slug: smartproxy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Smartproxy — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: smartproxy-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Smartproxy API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: smartproxy-rules
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 27.3
    contract_quality: 54.4
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 10.5
  open_source:
    applies: true
    score: 15.0
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/smartproxy/smartproxy-2026-06-20T194046.png
security:
- kind: authentication
  name: Smartproxy Authentication
  slug: smartproxy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Smartproxy Domain Security
  slug: smartproxy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smartproxy
tags:
- Proxies
- Web Scraping
- Data Collection
- Residential Proxies
- Datacenter Proxies
- Mobile Proxies
- Network Infrastructure
website: https://smartproxy.com/
---
