---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Monkedo provides a no-code automation platform with an API for managing workflows and integrations.
  name: Monkedo API
  slug: monkedo-api-2
- baseURL: https://app.monkedo.com
  baseurl_source: declared
  description: 'Z Yazilim API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Z Yazilim API
  slug: monkedo-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/monkedo/plans/monkedo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/monkedo-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/monkedo/rules/monkedo-rules.yml
  title: ''
  type: Spectral
  url: rules/monkedo-rules.yml
- group: design
  href: https://artifacts.apis.io/monkedo/json-ld/monkedo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/monkedo-context.jsonld
- group: design
  href: https://artifacts.apis.io/monkedo/vocabulary/monkedo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/monkedo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/monkedo/data-model/monkedo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/monkedo-data-model.yml
- group: auth
  href: https://artifacts.apis.io/monkedo/authentication/monkedo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/monkedo-authentication.yml
- group: design
  href: https://artifacts.apis.io/monkedo/conformance/monkedo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/monkedo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/monkedo/llms/monkedo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/monkedo-llms.txt
- group: other
  href: https://artifacts.apis.io/monkedo/hosts/monkedo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/monkedo-hosts.yml
- group: other
  href: https://artifacts.apis.io/monkedo/vendors/monkedo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/monkedo-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://monkedo.com/integrations/security
- group: company
  title: ''
  type: Newsroom
  url: https://monkedo.com/integrations/media
- group: auth
  href: https://artifacts.apis.io/monkedo/security/monkedo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monkedo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://monkedo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://monkedo.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://monkedo.com/docs/what-is-monkedo
- group: operate
  title: ''
  type: Support
  url: https://monkedo.com/contact.html
- group: company
  title: ''
  type: Blog
  url: https://monkedo.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://monkedo.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://monkedo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://monkedo.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monkedo.com/privacy.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/monkedo/workspace/monkedo-api
coverage:
  checked: '2026-10-21'
  detail: The provider's website returns HTML pages for typical spec URLs (e.g., /swagger.yaml) instead of a machine‑readable OpenAPI document.
  evidence:
  - status: 200
    url: https://monkedo.com/swagger.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Z Yazilim, operating under the brand Monkedo, provides a no-code automation platform that enables users to build workflows, integrate apps, and automate business processes without writing code. The platform offers embedded iPaaS capabilities, a library of templates, and extensive documentation to help users get started quickly. Monkedo targets businesses seeking alternatives to Zapier, Make, and Power Automate, emphasizing ease of use and flexibility across various integrations.
image: https://cloud-1de12d.becdn.net/media/iW=1200&iH=630/38edc3a3a16b74f04f2c75e172e86400.jpg
json_schemas:
- name: GetApiV1ComponentsAppsResponse
  property_count: 3
  slug: monkedo-get-api-v1-components-apps-response
- name: GetApiV1ComponentsTriggersResponse
  property_count: 5
  slug: monkedo-get-api-v1-components-triggers-response
- name: PostApiApiKeysInputOptionsRequest
  property_count: 4
  slug: monkedo-post-api-api-keys-input-options-request
- name: PostApiApiKeysInputOptionsResponse
  property_count: 3
  slug: monkedo-post-api-api-keys-input-options-response
- name: PostApiV1ComponentsTriggersRequest
  property_count: 3
  slug: monkedo-post-api-v1-components-triggers-request
- name: PostApiV1FilesUploadLinkResponse
  property_count: 3
  slug: monkedo-post-api-v1-files-upload-link-response
jsonld:
- class_count: 9
  name: Monkedo Context
  property_count: 18
  slug: monkedo-context
layout: provider
modified: '2026-10-21'
name: Z Yazilim
nav: Providers
network: true
overview: 'Z Yazilim is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, No-Code, Integration, and Workflows.


  The Z Yazilim catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Z Yazilim''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Monkedo Plans Pricing
  plan_count: 6
  slug: monkedo-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Z Yazilim API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: monkedo-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 28.6
    discoverability: 65.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/monkedo/monkedo-2026-11-03T135837.png
security:
- kind: authentication
  name: Monkedo Authentication
  slug: monkedo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Monkedo Domain Security
  slug: monkedo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: monkedo
tags:
- Company
- Automation
- No-Code
- Integration
- Workflows
website: https://monkedo.com/
---
