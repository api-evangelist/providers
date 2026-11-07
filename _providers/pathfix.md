---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Unified integration platform API
  name: Pathfix API
  slug: pathfix-api-2
- baseURL: https://labs.pathfix.com
  baseurl_source: declared
  description: 'Pathfix API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Pathfix API
  slug: pathfix-api
artifact_total: 9
asyncapis:
- description: ''
  name: Pathfix Webhooks
  slug: pathfix-webhooks
common:
- group: other
  href: https://artifacts.apis.io/pathfix/vendors/pathfix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pathfix-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/pathfix/plans/pathfix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pathfix-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pathfix/rules/pathfix-rules.yml
  title: ''
  type: Spectral
  url: rules/pathfix-rules.yml
- group: design
  href: https://artifacts.apis.io/pathfix/json-ld/pathfix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pathfix-context.jsonld
- group: design
  href: https://artifacts.apis.io/pathfix/vocabulary/pathfix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pathfix-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pathfix/asyncapi/pathfix-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pathfix-webhooks.yml
- group: design
  href: https://artifacts.apis.io/pathfix/data-model/pathfix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pathfix-data-model.yml
- group: design
  href: https://artifacts.apis.io/pathfix/conformance/pathfix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pathfix-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pathfix/llms/pathfix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pathfix-llms.txt
- group: other
  href: https://artifacts.apis.io/pathfix/hosts/pathfix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pathfix-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pathfix.com/terms
- group: auth
  title: ''
  type: Security
  url: https://pathfix.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://app.pathfix.com/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pathfix.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://pathfix.com/pricing/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pathfix.com/developers/
- group: company
  title: ''
  type: Blog
  url: https://blog.pathfix.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pathfix.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pathfix.com/
- group: auth
  href: https://artifacts.apis.io/pathfix/security/pathfix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pathfix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pathfix.com/
coverage:
  checked: '2026-10-18'
  detail: Docs at https://docs.pathfix.com return HTML pages and no OpenAPI/AsyncAPI/GraphQL spec
  evidence:
  - status: 200
    url: https://docs.pathfix.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Pathfix provides a unified integration platform that enables businesses to quickly build, secure, and manage API connections. Their OAuth Platform offers authentication services, while the Automation Platform lets users create no‑code workflows. The solution supports a wide range of integrations, detailed documentation, and pricing plans for both OAuth and Automation services, helping companies streamline data exchange and operational efficiency.
image: https://pathfix.com/wp-content/uploads/2020/04/Slide1.png
json_schemas:
- name: PostOauthMethodProvidernameCallRequest
  property_count: 4
  slug: pathfix-post-oauth-method-providername-call-request
- name: PostOauthMethodProvidernameCallResponse
  property_count: 7
  slug: pathfix-post-oauth-method-providername-call-response
jsonld:
- class_count: 2
  name: Pathfix Context
  property_count: 5
  slug: pathfix-context
layout: provider
modified: '2026-10-18'
name: Pathfix
nav: Providers
network: true
overview: 'Pathfix is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration Platform, OAuth, Automation, and API Management.


  The Pathfix catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Pathfix''s developer surface includes sandbox, pricing, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
plans:
- name: Pathfix Plans Pricing
  plan_count: 8
  slug: pathfix-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Pathfix API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: pathfix-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 28.0
    developer_ergonomics: 20.2
    discoverability: 64.3
    operational_transparency: 13.2
  previous_composite: 40.7
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
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pathfix/pathfix-2026-11-03T141003.png
security:
- kind: domain-security
  name: Pathfix Domain Security
  slug: pathfix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pathfix
tags:
- Company
- Integration Platform
- OAuth
- Automation
- API Management
- Authentication
website: https://pathfix.com/
---
