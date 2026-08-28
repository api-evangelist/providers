---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Noun Project Agentic Access
  operation_count: 11
  slug: noun-project-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 5
apis:
- description: Suggest search terms based on a query prefix.
  name: Noun Project Autocomplete API
  slug: noun-project-autocomplete-api
- description: Manage per-client blocklists for icon IDs, collection IDs, and terms.
  name: Noun Project Blocklist API
  slug: noun-project-blocklist-api
- description: Search and retrieve curated icon collections (icon sets).
  name: Noun Project Collection API
  slug: noun-project-collection-api
- description: Search, filter, retrieve, and download icons from the Noun Project library.
  name: Noun Project Icon API
  slug: noun-project-icon-api
- description: Inspect current API key usage against documented quotas.
  name: Noun Project Usage API
  slug: noun-project-usage-api
artifact_total: 69
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Noun Project API V2 Autocomplete API
  slug: open-noun-project-autocomplete-api
- collection_type: open
  name: Noun Project API V2 Autocomplete Blocklist API
  slug: open-noun-project-blocklist-api
- collection_type: open
  name: Noun Project API V2 Autocomplete Collection API
  slug: open-noun-project-collection-api
- collection_type: open
  name: Noun Project API V2 Autocomplete Icon API
  slug: open-noun-project-icon-api
- collection_type: open
  name: Noun Project API V2 Autocomplete Usage API
  slug: open-noun-project-usage-api
- collection_type: open
  name: Noun Project API V2
  slug: open-noun-project
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/noun-project-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noun-project-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/noun-project-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://thenounproject.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://thenounproject.com/api/
- group: start
  title: ''
  type: Signup
  url: https://thenounproject.com/developers/apps/
- group: operate
  title: ''
  type: Support
  url: https://thenounproject.zendesk.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.thenounproject.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheNounProject
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thenounproject.com/legal/api-terms-of-use/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/noun-project-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/noun-project-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/noun-project-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/noun-project-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/noun-project-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.thenounproject.com/feed/
created: '2026-05-28'
description: The Noun Project is a visual language platform providing access to nearly 10 million royalty-free PNG and SVG icons through an OAuth 1.0a-secured REST API. The v2 API supports icon search with style and line-weight filtering, similar-icon lookup, collection browsing, custom recoloring, autocomplete, per-client blocklists, and usage telemetry. Built on AWS, it serves more than 300 million requests per month at 99.99% uptime.
examples:
- key_count: 2
  name: Noun Project Autocomplete Response Example
  slug: noun-project-autocomplete-response-example
- key_count: 4
  name: Noun Project Blocklist Example
  slug: noun-project-blocklist-example
- key_count: 2
  name: Noun Project Blocklist Id Request Example
  slug: noun-project-blocklist-id-request-example
- key_count: 2
  name: Noun Project Blocklist Response Example
  slug: noun-project-blocklist-response-example
- key_count: 2
  name: Noun Project Blocklist Term Request Example
  slug: noun-project-blocklist-term-request-example
- key_count: 13
  name: Noun Project Collection Example
  slug: noun-project-collection-example
- key_count: 2
  name: Noun Project Collection Response Example
  slug: noun-project-collection-response-example
- key_count: 5
  name: Noun Project Collection Search Response Example
  slug: noun-project-collection-search-response-example
- key_count: 7
  name: Noun Project Icon Creator Example
  slug: noun-project-icon-creator-example
- key_count: 25
  name: Noun Project Icon Example
  slug: noun-project-icon-example
- key_count: 2
  name: Noun Project Icon Response Example
  slug: noun-project-icon-response-example
- key_count: 5
  name: Noun Project Icon Search Response Example
  slug: noun-project-icon-search-response-example
- key_count: 2
  name: Noun Project Tag Example
  slug: noun-project-tag-example
- key_count: 3
  name: Noun Project Usage Example
  slug: noun-project-usage-example
- key_count: 2
  name: Noun Project Usage Response Example
  slug: noun-project-usage-response-example
- key_count: 6
  name: Noun Project Usage Window Example
  slug: noun-project-usage-window-example
finops:
- name: Noun Project Finops
  service_category: Design Assets
  slug: noun-project-finops
image: https://thenounproject.com/icon.png
json_schemas:
- name: AutocompleteResponse
  property_count: 2
  slug: noun-project-autocomplete-response
- name: BlocklistIdRequest
  property_count: 2
  slug: noun-project-blocklist-id-request
- name: BlocklistResponse
  property_count: 2
  slug: noun-project-blocklist-response
- name: Blocklist
  property_count: 4
  slug: noun-project-blocklist
- name: BlocklistTermRequest
  property_count: 2
  slug: noun-project-blocklist-term-request
- name: CollectionResponse
  property_count: 2
  slug: noun-project-collection-response
- name: Collection
  property_count: 13
  slug: noun-project-collection
- name: CollectionSearchResponse
  property_count: 5
  slug: noun-project-collection-search-response
- name: IconCreator
  property_count: 7
  slug: noun-project-icon-creator
- name: IconResponse
  property_count: 2
  slug: noun-project-icon-response
- name: Icon
  property_count: 25
  slug: noun-project-icon
- name: IconSearchResponse
  property_count: 5
  slug: noun-project-icon-search-response
- name: Tag
  property_count: 2
  slug: noun-project-tag
- name: UsageResponse
  property_count: 2
  slug: noun-project-usage-response
- name: Usage
  property_count: 3
  slug: noun-project-usage
- name: UsageWindow
  property_count: 6
  slug: noun-project-usage-window
json_structures:
- name: Noun Project Autocomplete Response Structure
  property_count: 2
  slug: noun-project-autocomplete-response-structure
- name: Noun Project Blocklist Id Request Structure
  property_count: 2
  slug: noun-project-blocklist-id-request-structure
- name: Noun Project Blocklist Response Structure
  property_count: 2
  slug: noun-project-blocklist-response-structure
- name: Noun Project Blocklist Structure
  property_count: 4
  slug: noun-project-blocklist-structure
- name: Noun Project Blocklist Term Request Structure
  property_count: 2
  slug: noun-project-blocklist-term-request-structure
- name: Noun Project Collection Response Structure
  property_count: 2
  slug: noun-project-collection-response-structure
- name: Noun Project Collection Search Response Structure
  property_count: 5
  slug: noun-project-collection-search-response-structure
- name: Noun Project Collection Structure
  property_count: 13
  slug: noun-project-collection-structure
- name: Noun Project Icon Creator Structure
  property_count: 7
  slug: noun-project-icon-creator-structure
- name: Noun Project Icon Response Structure
  property_count: 2
  slug: noun-project-icon-response-structure
- name: Noun Project Icon Search Response Structure
  property_count: 5
  slug: noun-project-icon-search-response-structure
- name: Noun Project Icon Structure
  property_count: 25
  slug: noun-project-icon-structure
- name: Noun Project Tag Structure
  property_count: 2
  slug: noun-project-tag-structure
- name: Noun Project Usage Response Structure
  property_count: 2
  slug: noun-project-usage-response-structure
- name: Noun Project Usage Structure
  property_count: 3
  slug: noun-project-usage-structure
- name: Noun Project Usage Window Structure
  property_count: 6
  slug: noun-project-usage-window-structure
jsonld:
- class_count: 16
  name: Noun Project Context
  property_count: 61
  slug: noun-project-context
layout: provider
modified: '2026-05-28'
name: Noun Project
nav: Providers
network: true
overview: 'Noun Project publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Blocklist API, Collection API, and 2 more. Tagged areas include Art And Design, Icons, SVG, Visual Language, and Design Assets.


  The Noun Project catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Noun Project''s developer surface includes authentication, pricing, signup flow, support, engineering blog, and 12 more developer resources.'
plans:
- name: Noun Project Plans Pricing
  plan_count: 3
  slug: noun-project-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 12
  name: Noun Project Rate Limits
  slug: noun-project-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Noun Project API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: noun-project-jsonschema-spectral-rules
- effective_rule_count: 90
  extends:
  - spectral:oas
  name: Noun Project API Rules
  rule_count: 49
  severity_counts:
    error: 18
    hint: 0
    info: 7
    warn: 24
  slug: noun-project-rules
score:
  band: developing
  composite: 40.2
  delta: 4.3
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 28.8
    contract_quality: 22.1
    developer_ergonomics: 40.5
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 34.2
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/noun-project/refs/heads/main/screenshots/noun-project-2026-06-20T190429.png
security:
- kind: authentication
  name: Noun Project Authentication
  slug: noun-project-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Noun Project Domain Security
  slug: noun-project-domain-security
  summary_line: TLSv1.3 · DMARC
slug: noun-project
tags:
- Art And Design
- Icons
- SVG
- Visual Language
- Design Assets
- Public APIs
website: https://thenounproject.com/
---
