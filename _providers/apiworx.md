---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'APIWorx API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: APIWorx API
  slug: apiworx-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/apiworx/rules/apiworx-rules.yml
  title: ''
  type: Spectral
  url: rules/apiworx-rules.yml
- group: design
  href: https://artifacts.apis.io/apiworx/json-ld/apiworx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apiworx-context.jsonld
- group: design
  href: https://artifacts.apis.io/apiworx/vocabulary/apiworx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apiworx-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apiworx/data-model/apiworx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apiworx-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://apiworx.com/security
- group: design
  href: https://artifacts.apis.io/apiworx/conformance/apiworx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apiworx-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apiworx/llms/apiworx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiworx-llms.txt
- group: agent
  href: https://artifacts.apis.io/apiworx/well-known/apiworx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apiworx-well-known.yml
- group: other
  href: https://artifacts.apis.io/apiworx/hosts/apiworx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apiworx-hosts.yml
- group: other
  href: https://artifacts.apis.io/apiworx/vendors/apiworx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apiworx-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://apiworx.com/security
- group: commercial
  title: ''
  type: Pricing
  url: https://apiworx.com/pricing
- group: other
  title: ''
  type: Leadership
  url: https://apiworx.com/team
- group: auth
  href: https://artifacts.apis.io/apiworx/security/apiworx-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/apiworx-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/apiworx/security/apiworx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiworx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiworx.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.apiworx.com
- group: docs
  title: ''
  type: Documentation
  url: https://apiworx.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://apiworx.com/docs#getting-started
- group: operate
  title: ''
  type: Support
  url: https://portal.apiworx.com
- group: company
  title: ''
  type: Blog
  url: https://apiworx.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apiworx.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apiworx.com/privacy
- group: other
  title: ''
  type: SignIn
  url: https://app.apiworx.com
coverage:
  checked: '2026-10-20'
  detail: API documentation at https://apiworx.com/api-docs returns HTML instead of a machine‑readable spec.
  evidence:
  - status: 200
    url: https://apiworx.com/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: APIWorx is a commerce operations automation platform that connects ERP, ecommerce, marketplaces, EDI, fulfillment, suppliers, and financial systems. It enables businesses to automate and orchestrate complex commerce processes, providing flat‑fee pricing and a free architecture assessment to help integrate systems seamlessly. The platform supports record syncs, app flows, and integration runs across numerous customers, delivering scalable, end‑to‑end automation for modern commerce operations.
image: https://apiworx.com/og-home.jpg?v=20261017
json_schemas:
- name: PostApiV1FlowsRequest
  property_count: 6
  slug: apiworx-post-api-v1-flows-request
jsonld:
- class_count: 1
  name: Apiworx Context
  property_count: 6
  slug: apiworx-context
layout: provider
modified: '2026-10-19'
name: APIWorx
nav: Providers
network: true
overview: 'APIWorx is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, Integration, Automation, and ERP.


  The APIWorx catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIWorx''s developer surface includes pricing, documentation, getting-started guide, support, engineering blog, and 19 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: APIWorx API Rules
  rule_count: 8
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 0
  slug: apiworx-rules
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.4
    catalog_earned_first_party: 0.0
    catalog_gap: 67.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 27.6
    contract_governance: 33.3
    contract_quality: 16.4
    developer_ergonomics: 19.0
    discoverability: 65.2
    operational_transparency: 5.3
  previous_composite: 33.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
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
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/apiworx/apiworx-2026-11-03T121014.png
security:
- kind: domain-security
  name: Apiworx Domain Security
  slug: apiworx-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Apiworx Trust Center
  slug: apiworx-trust-center
  summary_line: SOC 2, GDPR
slug: apiworx
tags:
- Company
- Commerce
- Integration
- Automation
- ERP
- E-Commerce
website: https://apiworx.com/
---
