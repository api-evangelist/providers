---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Profit Rhino Agentic Access
  operation_count: 23
  slug: profit-rhino-agentic-access
  summary_line: 23 operations · 1 acting
api_count: 1
apis:
- baseURL: https://secure.profitrhino.com/api
  baseurl_source: declared
  description: The Auth API from Profit Rhino — 1 operation(s) for auth.
  name: Profit Rhino Auth API
  slug: profit-rhino-auth-api
- baseURL: https://secure.profitrhino.com/api
  baseurl_source: declared
  description: The BusinessInformation API from Profit Rhino — 1 operation(s) for businessinformation.
  name: Profit Rhino Business Information API
  slug: profit-rhino-businessinformation-api
- baseURL: https://secure.profitrhino.com/api
  baseurl_source: declared
  description: The Manufacturer API from Profit Rhino — 2 operation(s) for manufacturer.
  name: Profit Rhino Manufacturer API
  slug: profit-rhino-manufacturer-api
- baseURL: https://secure.profitrhino.com/api
  baseurl_source: declared
  description: The OptionBoard API from Profit Rhino — 2 operation(s) for optionboard.
  name: Profit Rhino Option Board API
  slug: profit-rhino-optionboard-api
- baseURL: https://secure.profitrhino.com/api
  baseurl_source: declared
  description: The PartCategory API from Profit Rhino — 5 operation(s) for partcategory.
  name: Profit Rhino Part Category API
  slug: profit-rhino-partcategory-api
- baseURL: https://secure.profitrhino.com/api
  baseurl_source: declared
  description: The Parts API from Profit Rhino — 4 operation(s) for parts.
  name: Profit Rhino Parts API
  slug: profit-rhino-parts-api
- baseURL: https://secure.profitrhino.com/api
  baseurl_source: declared
  description: The PartsMarkup API from Profit Rhino — 1 operation(s) for partsmarkup.
  name: Profit Rhino Parts Markup API
  slug: profit-rhino-partsmarkup-api
- baseURL: https://secure.profitrhino.com/api
  baseurl_source: declared
  description: The TaskCategory API from Profit Rhino — 3 operation(s) for taskcategory.
  name: Profit Rhino Task Category API
  slug: profit-rhino-taskcategory-api
- baseURL: https://secure.profitrhino.com/api
  baseurl_source: declared
  description: The Tasks API from Profit Rhino — 2 operation(s) for tasks.
  name: Profit Rhino Tasks API
  slug: profit-rhino-tasks-api
- baseURL: https://secure.profitrhino.com/api
  baseurl_source: declared
  description: The Vendors API from Profit Rhino — 2 operation(s) for vendors.
  name: Profit Rhino Vendors API
  slug: profit-rhino-vendors-api
artifact_total: 33
common:
- group: other
  href: https://artifacts.apis.io/profit-rhino/capabilities/profit-rhino-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/profit-rhino-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/profit-rhino/agentic-access/profit-rhino-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/profit-rhino-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/profit-rhino/plans/profit-rhino-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/profit-rhino-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/profit-rhino/rules/profit-rhino-rules.yml
  title: ''
  type: Spectral
  url: rules/profit-rhino-rules.yml
- group: design
  href: https://artifacts.apis.io/profit-rhino/json-ld/profit-rhino-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/profit-rhino-context.jsonld
- group: design
  href: https://artifacts.apis.io/profit-rhino/vocabulary/profit-rhino-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/profit-rhino-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/profit-rhino/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/profit-rhino/data-model/profit-rhino-data-model.yml
  title: ''
  type: DataModel
  url: data-model/profit-rhino-data-model.yml
- group: auth
  href: https://artifacts.apis.io/profit-rhino/authentication/profit-rhino-authentication.yml
  title: ''
  type: Authentication
  url: authentication/profit-rhino-authentication.yml
- group: design
  href: https://artifacts.apis.io/profit-rhino/errors/profit-rhino-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/profit-rhino-problem-types.yml
- group: design
  href: https://artifacts.apis.io/profit-rhino/conformance/profit-rhino-conformance.yml
  title: ''
  type: Conformance
  url: conformance/profit-rhino-conformance.yml
- group: agent
  href: https://artifacts.apis.io/profit-rhino/llms/profit-rhino-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/profit-rhino-llms.txt
- group: auth
  href: https://artifacts.apis.io/profit-rhino/well-known/profit-rhino-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/profit-rhino-support-security.txt
- group: agent
  href: https://artifacts.apis.io/profit-rhino/well-known/profit-rhino-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/profit-rhino-well-known.yml
- group: other
  href: https://artifacts.apis.io/profit-rhino/hosts/profit-rhino-hosts.yml
  title: ''
  type: Hosts
  url: hosts/profit-rhino-hosts.yml
- group: other
  href: https://artifacts.apis.io/profit-rhino/vendors/profit-rhino-vendors.yml
  title: ''
  type: Vendors
  url: vendors/profit-rhino-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://profitrhino.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://profitrhino.com/privacy-policy/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.profitrhino.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.profitrhino.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/profit-rhino/security/profit-rhino-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/profit-rhino-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://profitrhino.com/
- group: docs
  title: ''
  type: Documentation
  url: https://profitrhino.com/products/
- group: commercial
  title: ''
  type: Pricing
  url: https://profitrhino.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.profitrhino.com/
- group: company
  title: ''
  type: Blog
  url: https://profitrhino.com/blog/
created: '2026-10-28'
description: Profit Rhino is a flat‑rate service platform that partners with Callahan Roach, the pioneer of flat‑rate pricing in the HVAC industry. Founded in 2019, the platform provides contractors with tools to simplify quoting, increase profitability, and streamline operations. By integrating Callahan Roach’s extensive flat‑rate guides—covering over 60 million repairs—and modern technology, Profit Rhino offers features such as SmartPrice, Integrate, and C.A.P to help residential trade professionals manage pricing, scheduling, and customer communication, reducing diagnostic fees and growing contractor businesses.
json_schemas:
- name: PRResponse_BusinessInformationViewModelV2_
  property_count: 3
  slug: profit-rhino-prresponse-business-information-view-model-v2
- name: PRResponse_List_VendorsViewModel_
  property_count: 3
  slug: profit-rhino-prresponse-list-vendors-view-model
- name: PRResponse_PartCategoryProductLinesModel_
  property_count: 3
  slug: profit-rhino-prresponse-part-category-product-lines-model
- name: PRResponse_PartVendorsResultModel_
  property_count: 3
  slug: profit-rhino-prresponse-part-vendors-result-model
- name: PRResponse_ProductLineDescriptionModel_
  property_count: 3
  slug: profit-rhino-prresponse-product-line-description-model
- name: PRResponse_ProductLineDescriptionsModel_
  property_count: 3
  slug: profit-rhino-prresponse-product-line-descriptions-model
jsonld:
- class_count: 62
  name: Profit Rhino Context
  property_count: 159
  slug: profit-rhino-context
layout: provider
modified: '2026-10-28'
name: Profit Rhino
nav: Providers
network: true
overview: 'Profit Rhino publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Business Information API, Manufacturer API, and 7 more. Tagged areas include Company, flat-rate, contractor, HVAC, and software.


  The Profit Rhino catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Profit Rhino''s developer surface includes authentication, API reference, getting-started guide, documentation, pricing, support, engineering blog, and 19 more developer resources.'
plans:
- name: Profit Rhino Plans Pricing
  plan_count: 3
  slug: profit-rhino-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Profit Rhino API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: profit-rhino-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 72.0
    catalog_earned_first_party: 12.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 19.7
    contract_quality: 52.1
    developer_ergonomics: 54.0
    discoverability: 62.5
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Profit Rhino Authentication
  slug: profit-rhino-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Profit Rhino Domain Security
  slug: profit-rhino-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 11
skills:
- name: '0'
  slug: '0'
- name: auth
  slug: auth
- name: business-information
  slug: business-information
- name: manufacturer
  slug: manufacturer
- name: option-board
  slug: option-board
- name: part-category
  slug: part-category
- name: parts-markup
  slug: parts-markup
- name: parts
  slug: parts
- name: task-category
  slug: task-category
- name: tasks
  slug: tasks
- name: vendors
  slug: vendors
slug: profit-rhino
tags:
- Company
- flat-rate
- contractor
- HVAC
- software
- sales-tool
website: https://profitrhino.com/
---
