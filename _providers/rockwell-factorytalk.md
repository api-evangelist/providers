---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Rockwell Factorytalk Agentic Access
  operation_count: 10
  slug: rockwell-factorytalk-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.factorytalk.example.com
  baseurl_source: declared
  description: Rockwell FactoryTalk Hub provides cloud-based industrial API services for connecting FactoryTalk software applications, enabling centralized identity management, software licensing, and connected fact
  name: Rockwell FactoryTalk Hub API
  slug: factorytalk-hub-api
- description: Rockwell Automation FactoryTalk Logix Designer provides programmatic access to Logix controller programming, allowing version control integration, CI/CD pipeline automation, and export of L5X controll
  name: Rockwell FactoryTalk Logix Designer API
  slug: logix-designer-api
- baseURL: https://api.factorytalk.example.com
  baseurl_source: declared
  description: Alarm and event management
  name: rockwell-factorytalk Alarms API
  slug: rockwell-factorytalk-alarms-api
- baseURL: https://api.factorytalk.example.com
  baseurl_source: declared
  description: Recipe management
  name: rockwell-factorytalk Recipes API
  slug: rockwell-factorytalk-recipes-api
- baseURL: https://api.factorytalk.example.com
  baseurl_source: declared
  description: The Tags API from rockwell-factorytalk — 3 operation(s) for tags.
  name: rockwell-factorytalk Tags API
  slug: rockwell-factorytalk-tags-api
- baseURL: https://api.factorytalk.example.com
  baseurl_source: declared
  description: Historical trend data retrieval
  name: rockwell-factorytalk TrendData API
  slug: rockwell-factorytalk-trenddata-api
artifact_total: 28
asyncapis:
- description: Rockwell FactoryTalk Hub provides real-time industrial event streaming via webhooks and subscriptions. Events include tag value changes, alarm activations, and device connectivity notifications for co
  name: Rockwell FactoryTalk Hub Real-Time Events API
  slug: rockwell-factorytalk-realtime-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rockwell FactoryTalk Optix REST Alarms API
  slug: open-rockwell-factorytalk-alarms-api
- collection_type: open
  name: Rockwell FactoryTalk Optix REST API
  slug: open-rockwell-factorytalk-optix
- collection_type: open
  name: Rockwell FactoryTalk Optix REST Alarms Recipes API
  slug: open-rockwell-factorytalk-recipes-api
- collection_type: open
  name: Rockwell FactoryTalk Optix REST Alarms Tags API
  slug: open-rockwell-factorytalk-tags-api
- collection_type: open
  name: Rockwell FactoryTalk Optix REST Alarms TrendData API
  slug: open-rockwell-factorytalk-trenddata-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rockwell-factorytalk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rockwell-factorytalk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rockwell-factorytalk-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rockwell-factorytalk-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.rockwellautomation.com/en-us/products/software/factorytalk.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rockwellautomation.com/en/products/software/factorytalk/
- group: company
  title: ''
  type: Website
  url: https://www.rockwellautomation.com/en-us/
- group: operate
  title: ''
  type: Support
  url: https://www.rockwellautomation.com/en-us/support/
- group: company
  title: ''
  type: Blog
  url: https://www.rockwellautomation.com/en-us/company/news/blogs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rockwellautomation.com/en-us/company/about-us/legal-notices/privacy-and-cookies-policy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rockwellautomation
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/rockwell-factorytalk-optix-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/rockwell-factorytalk-realtime-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/rockwell-factorytalk-tag-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/rockwell-factorytalk-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/rockwell-factorytalk-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rockwell-factorytalk-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/rockwell-factorytalk-rules.yml
description: Rockwell FactoryTalk is a portfolio of software products by Rockwell Automation that supports the design, operation, and maintenance of industrial control systems and connected manufacturing operations.
examples:
- key_count: 5
  name: Factorytalk List Alarms Example
  slug: factorytalk-list-alarms-example
- key_count: 5
  name: Factorytalk Read Tag Values Example
  slug: factorytalk-read-tag-values-example
finops:
- name: Rockwell Factorytalk Finops
  service_category: Industrial Automation Software
  slug: rockwell-factorytalk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rockwell-factorytalk.png
json_schemas:
- name: Rockwell FactoryTalk Tag
  property_count: 9
  slug: rockwell-factorytalk-tag
json_structures:
- name: Rockwell Factorytalk Structure
  property_count: 0
  slug: rockwell-factorytalk-structure
jsonld:
- class_count: 0
  name: Rockwell Factorytalk Context
  property_count: 26
  slug: rockwell-factorytalk-context
layout: provider
modified: '2026-05-19'
name: Rockwell FactoryTalk
nav: Providers
network: true
overview: 'Rockwell FactoryTalk publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Hub API, rockwell-factorytalk Alarms API, rockwell-factorytalk Recipes API, and 2 more.


  The Rockwell FactoryTalk catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Rockwell FactoryTalk''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 13 more developer resources.'
plans:
- name: Rockwell Factorytalk Plans Pricing
  plan_count: 1
  slug: rockwell-factorytalk-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Rockwell Factorytalk Rate Limits
  slug: rockwell-factorytalk-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Rockwell FactoryTalk API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: rockwell-factorytalk-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Rockwell FactoryTalk API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rockwell-factorytalk-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Rockwell FactoryTalk API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 5
  slug: rockwell-factorytalk-rules
scopes:
- name: Rockwell Factorytalk Scopes
  scope_count: 3
  slug: rockwell-factorytalk-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 56.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 28.8
    contract_quality: 64.3
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rockwell-factorytalk/refs/heads/main/screenshots/rockwell-factorytalk-2026-06-20T193201.png
security:
- kind: authentication
  name: Rockwell Factorytalk Authentication
  slug: rockwell-factorytalk-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Rockwell Factorytalk Domain Security
  slug: rockwell-factorytalk-domain-security
  summary_line: TLSv1.3 · HSTS
slug: rockwell-factorytalk
website: https://www.rockwellautomation.com/en-us/
---
