---
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.thebrief.ai
  baseurl_source: declared
  description: 'TheBrief API as documented publicly: 51 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: TheBrief API
  slug: creatopy-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/creatopy-com/plans/creatopy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/creatopy-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/creatopy-com/rules/creatopy-com-rules.yml
  title: ''
  type: Spectral
  url: rules/creatopy-com-rules.yml
- group: design
  href: https://artifacts.apis.io/creatopy-com/json-ld/creatopy-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/creatopy-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/creatopy-com/vocabulary/creatopy-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/creatopy-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/creatopy-com/data-model/creatopy-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/creatopy-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.thebrief.ai/security/
- group: design
  href: https://artifacts.apis.io/creatopy-com/conformance/creatopy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/creatopy-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/creatopy-com/llms/creatopy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/creatopy-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/creatopy-com/well-known/creatopy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/creatopy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/creatopy-com/hosts/creatopy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/creatopy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/creatopy-com/vendors/creatopy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/creatopy-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.thebrief.ai/security/
- group: operate
  title: ''
  type: Roadmap
  url: https://community.thebrief.ai/roadmap
- group: company
  title: ''
  type: Newsroom
  url: https://www.thebrief.ai/press/
- group: operate
  title: ''
  type: ChangeLog
  url: https://community.thebrief.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.thebrief.ai/hc/en-us/categories/22257101202588-Getting-Started-Managing-Your-Account
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thebrief.ai/
- group: auth
  href: https://artifacts.apis.io/creatopy-com/security/creatopy-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/creatopy-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/creatopy-com/security/creatopy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/creatopy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thebrief.ai
- group: company
  title: ''
  type: Blog
  url: https://www.thebrief.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thebrief.ai/pricing/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.thebrief.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.thebrief.ai/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thebrief.ai/legal-information/business-subscription-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thebrief.ai/legal-information/privacy-policy/
coverage:
  checked: '2026-10-30'
  detail: The developer portal at https://app.thebrief.ai/ serves a JavaScript‑rendered SPA with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://app.thebrief.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: The Brief (formerly Creatopy) is an AI‑powered advertising creation platform that helps brands generate, adapt, and deploy on‑brand ads at scale. Leveraging generative AI, the service offers tools for design, animation, resizing, and multi‑format output, integrating with over 40 ad networks. It serves enterprises and agencies, providing a unified workflow from concept to launch, with features like AI‑driven copywriting, brand‑trained models, and collaborative editing. The platform aims to reduce creative production time and cost while maintaining brand consistency across campaigns.
image: https://cdn.sanity.io/images/8wzdrx7x/production/d9d93597b665708876d106aed92e87d0addafc41-760x175.svg
json_schemas:
- name: GetV1BrandkitBrandkitidAssetsResponse
  property_count: 1
  slug: creatopy-com-get-v1-brandkit-brandkitid-assets-response
- name: GetV1CreditsSubscriptionInfoResponse
  property_count: 7
  slug: creatopy-com-get-v1-credits-subscription-info-response
- name: GetV1FoldersResponse
  property_count: 1
  slug: creatopy-com-get-v1-folders-response
- name: PostV1BrandkitUploadassetsResponse
  property_count: 1
  slug: creatopy-com-post-v1-brandkit-uploadassets-response
- name: PostV1BrandkitUploadlogosResponse
  property_count: 1
  slug: creatopy-com-post-v1-brandkit-uploadlogos-response
- name: PutV1FoldersResponse
  property_count: 1
  slug: creatopy-com-put-v1-folders-response
jsonld:
- class_count: 68
  name: Creatopy Com Context
  property_count: 44
  slug: creatopy-com-context
layout: provider
modified: '2026-10-28'
name: TheBrief
nav: Providers
network: true
overview: 'TheBrief is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, AI, Marketing, Creative, and Platform.


  The TheBrief catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TheBrief''s developer surface includes changelog, getting-started guide, documentation, engineering blog, pricing, support, and 20 more developer resources.'
plans:
- name: Creatopy Com Plans Pricing
  plan_count: 4
  slug: creatopy-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: TheBrief API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: creatopy-com-rules
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 38.1
    discoverability: 67.9
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 19
      marker_coverage: 100.0
      total: 19
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Creatopy Com Domain Security
  slug: creatopy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Creatopy Com Trust Center
  slug: creatopy-com-trust-center
  summary_line: ISO 27001, GDPR
slug: creatopy-com
tags:
- Advertising
- AI
- Marketing
- Creative
- Platform
- Company
website: https://www.thebrief.ai
---
