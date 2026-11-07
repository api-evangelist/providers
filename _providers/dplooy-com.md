---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Deploy HTML or a ZIP, then list, edit and delete sites and manage forms, data, bookings and media with the Dplooy REST API.
  name: dplooy REST API
  slug: dplooy-rest-api
- baseURL: https://api.dplooy.com
  baseurl_source: declared
  description: 'dplooy API as documented publicly: 27 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: dplooy API
  slug: dplooy-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/dplooy-com/plans/dplooy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dplooy-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dplooy-com/rules/dplooy-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dplooy-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dplooy-com/json-ld/dplooy-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dplooy-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dplooy-com/vocabulary/dplooy-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dplooy-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dplooy-com/data-model/dplooy-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dplooy-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/dplooy-com/conformance/dplooy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dplooy-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dplooy-com/llms/dplooy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dplooy-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dplooy-com/well-known/dplooy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dplooy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dplooy-com/hosts/dplooy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dplooy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dplooy-com/vendors/dplooy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dplooy-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dplooy.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.dplooy.com/auth/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dplooy.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dplooy.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.dplooy.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.dplooy.com/developers
- group: company
  title: ''
  type: Blog
  url: https://www.dplooy.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dplooy.com/guides/custom-domain-setup
- group: auth
  href: https://artifacts.apis.io/dplooy-com/security/dplooy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dplooy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dplooy.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.dplooy.com/mcp
  - status: 200
    url: https://dplooy.com/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: dplooy provides free website hosting for HTML and static sites, offering SSL, custom domains, forms, bookings, and an AI chatbot. Users can upload files, ZIPs, or folders and get a live site in seconds without credit card or signup. The service targets developers and hobbyists seeking simple, fast deployment.
image: https://www.dplooy.com/og-image.png
json_schemas:
- name: GetApiV1ProjectsA1B2C3D4Response
  property_count: 13
  slug: dplooy-com-get-api-v1-projects-a1-b2-c3-d4-response
- name: GetApiV1ProjectsResponse
  property_count: 4
  slug: dplooy-com-get-api-v1-projects-response
- name: PostApiV1DeployZipResponse
  property_count: 8
  slug: dplooy-com-post-api-v1-deploy-zip-response
- name: PostDeployRequest
  property_count: 4
  slug: dplooy-com-post-deploy-request
- name: PostDeployResponse
  property_count: 6
  slug: dplooy-com-post-deploy-response
- name: PostDeployZipResponse
  property_count: 8
  slug: dplooy-com-post-deploy-zip-response
jsonld:
- class_count: 14
  name: Dplooy Com Context
  property_count: 33
  slug: dplooy-com-context
layout: provider
modified: '2026-11-05'
name: dplooy
nav: Providers
network: true
overview: 'dplooy is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Hosting, Free, Static Sites, SSL, and Developer Tools.


  The dplooy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  dplooy''s developer surface includes signup flow, pricing, documentation, engineering blog, getting-started guide, and 15 more developer resources.'
plans:
- name: Dplooy Com Plans Pricing
  plan_count: 3
  slug: dplooy-com-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: dplooy API Rules
  rule_count: 46
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 2
  slug: dplooy-com-rules
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 26.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dplooy Com Domain Security
  slug: dplooy-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dplooy-com
tags:
- Hosting
- Free
- Static Sites
- SSL
- Developer Tools
website: https://www.dplooy.com/
---
