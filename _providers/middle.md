---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://test.middle.app
  baseurl_source: declared
  description: 'Middle API as documented publicly: 34 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Middle API
  slug: middle-api
artifact_total: 12
common:
- group: auth
  href: https://artifacts.apis.io/middle/well-known/middle-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/middle-developers-security.txt
- group: commercial
  href: https://artifacts.apis.io/middle/plans/middle-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/middle-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/middle/rules/middle-rules.yml
  title: ''
  type: Spectral
  url: rules/middle-rules.yml
- group: design
  href: https://artifacts.apis.io/middle/json-ld/middle-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/middle-context.jsonld
- group: design
  href: https://artifacts.apis.io/middle/vocabulary/middle-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/middle-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/middle/data-model/middle-data-model.yml
  title: ''
  type: DataModel
  url: data-model/middle-data-model.yml
- group: operate
  href: https://artifacts.apis.io/middle/changelog/middle-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/middle-changelog.yml
- group: auth
  href: https://artifacts.apis.io/middle/authentication/middle-authentication.yml
  title: ''
  type: Authentication
  url: authentication/middle-authentication.yml
- group: design
  href: https://artifacts.apis.io/middle/conformance/middle-conformance.yml
  title: ''
  type: Conformance
  url: conformance/middle-conformance.yml
- group: agent
  href: https://artifacts.apis.io/middle/llms/middle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/middle-llms.txt
- group: agent
  href: https://artifacts.apis.io/middle/well-known/middle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/middle-well-known.yml
- group: other
  href: https://artifacts.apis.io/middle/hosts/middle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/middle-hosts.yml
- group: other
  href: https://artifacts.apis.io/middle/vendors/middle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/middle-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.middle.app/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.middle.app/middle-docs/release-notes/june-3-2026
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.hubspot.com/blog/arrows-enhances-customer-onboarding-with-hubspots-ui-extensions
- group: auth
  href: https://artifacts.apis.io/middle/security/middle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/middle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://middle.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.middle.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.middle.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.middle.app/middle-docs/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.middle.app/blog
- group: operate
  title: ''
  type: Support
  url: https://41cefa.share-na2.hsforms.com/2gtvFGHa0RySQwJD5k843cg
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://middle.app/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Middle is an integration platform as a service (iPaaS) that helps businesses and their customers connect apps, enabling them to focus on product and service excellence rather than building integrations. The platform offers pre‑built integrations, agency, enterprise, and SaaS solutions, along with developer resources, pricing details, and support channels.
image: https://cdn.prod.website-files.com/60cbf2e9c2e97574ee123d6e/61904cc194f49c7d0f78d651_Middle%20header.png
json_schemas:
- name: GetApiWorkflowInvokeOptionsListsResponse
  property_count: 7
  slug: middle-get-api-workflow-invoke-options-lists-response
- name: GetMiddleDocsGuidesAppReferenceClubreadyMdResponse
  property_count: 3
  slug: middle-get-middle-docs-guides-app-reference-clubready-md-response
- name: GetMiddleDocsGuidesAppReferenceKlaviyoMdResponse
  property_count: 3
  slug: middle-get-middle-docs-guides-app-reference-klaviyo-md-response
- name: GetMiddleDocsGuidesAppReferenceMdResponse
  property_count: 3
  slug: middle-get-middle-docs-guides-app-reference-md-response
- name: PostApiWorkflowInvokePathtokenRunsRequest
  property_count: 1
  slug: middle-post-api-workflow-invoke-pathtoken-runs-request
- name: PostApiWorkflowInvokePathtokenRunsResponse
  property_count: 6
  slug: middle-post-api-workflow-invoke-pathtoken-runs-response
jsonld:
- class_count: 6
  name: Middle Context
  property_count: 10
  slug: middle-context
layout: provider
modified: '2026-10-21'
name: Middle
nav: Providers
network: true
overview: 'Middle is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Integration Platform, iPaaS, and Data Integration.


  The Middle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Middle''s developer surface includes changelog, authentication, getting-started guide, documentation, API reference, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Middle Plans Pricing
  plan_count: 2
  slug: middle-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Middle API Rules
  rule_count: 46
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 7
  slug: middle-rules
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 26.3
    contract_governance: 35.6
    contract_quality: 25.2
    developer_ergonomics: 34.5
    discoverability: 64.3
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/middle/middle-2026-11-03T135554.png
security:
- kind: authentication
  name: Middle Authentication
  slug: middle-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Middle Domain Security
  slug: middle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: middle
tags:
- Integration Platform
- iPaaS
- Data Integration
website: https://middle.app/
---
