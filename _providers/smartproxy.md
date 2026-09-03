---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
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
  description: Manage proxy sub-user accounts
  name: Smartproxy Sub-Users API
  slug: smartproxy-sub-users-api
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
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: AgenticAccess
  url: agentic-access/smartproxy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartproxy-domain-security.yml
- group: auth
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
  title: ''
  type: OpenAPI
  url: openapi/_original/smartproxy-openapi.yml
- group: design
  title: ''
  type: Spectral
  url: rules/smartproxy-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/smartproxy-sub-user-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/smartproxy-endpoint-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/smartproxy-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/smartproxy-context.jsonld
- group: design
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
- name: Smartproxy Finops
  service_category: API
  slug: smartproxy-finops
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
overview: 'Smartproxy publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Endpoints API, Sub-Users API, and 3 more. Tagged areas include Proxies, Web Scraping, Data Collection, Residential Proxies, and Datacenter Proxies.


  The Smartproxy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Smartproxy''s developer surface includes authentication, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Smartproxy Plans Pricing
  plan_count: 3
  slug: smartproxy-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Smartproxy Rate Limits
  slug: smartproxy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Smartproxy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: smartproxy-jsonschema-spectral-rules
- effective_rule_count: 47
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
  composite: 33.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 59.9
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  open_source:
    applies: true
    score: 15.0
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smartproxy/refs/heads/main/screenshots/smartproxy-2026-06-20T194046.png
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
