---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  - sandbox
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Maplith provides a company brain platform with an API documented at the developer docs.
  name: Maplith API
  slug: maplith-api
- baseURL: https://app.maplith.com
  baseurl_source: declared
  description: 'maplith-com API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: maplith-com API
  slug: maplith-com-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/maplith-com/plans/maplith-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/maplith-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/maplith-com/rules/maplith-com-rules.yml
  title: ''
  type: Spectral
  url: rules/maplith-com-rules.yml
- group: design
  href: https://artifacts.apis.io/maplith-com/json-ld/maplith-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/maplith-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/maplith-com/vocabulary/maplith-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/maplith-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/maplith-com/data-model/maplith-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/maplith-com-data-model.yml
- group: start
  href: https://artifacts.apis.io/maplith-com/sandbox/maplith-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/maplith-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/maplith-com/conformance/maplith-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/maplith-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/maplith-com/llms/maplith-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/maplith-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/maplith-com/well-known/maplith-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/maplith-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/maplith-com/hosts/maplith-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/maplith-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/maplith-com/vendors/maplith-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/maplith-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://maplith.com/security
- group: other
  title: ''
  type: Leadership
  url: https://maplith.com/team
- group: auth
  href: https://artifacts.apis.io/maplith-com/security/maplith-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maplith-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://maplith.com/
- group: docs
  title: ''
  type: Documentation
  url: https://maplith.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://maplith.com/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://maplith.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://maplith.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://maplith.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://maplith.com/support
coverage:
  checked: '2026-10-30'
  detail: Docs are served via a JavaScript login page that redirects OpenAPI requests to a login flow.
  evidence:
  - status: 307
    url: https://maplith.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Maplith provides a company brain platform that integrates data across systems, enabling AI agents to access unified knowledge graphs, automate workflows, and generate insights. It offers tools for building, managing, and querying a centralized map of objects, fields, and relationships, supporting automation, data integration, and AI-driven decision making across enterprises.
image: https://maplith.com/og.png
json_schemas:
- name: PostMcpRequest
  property_count: 3
  slug: maplith-com-post-mcp-request
- name: PostRequest
  property_count: 3
  slug: maplith-com-post-request
jsonld:
- class_count: 2
  name: Maplith Com Context
  property_count: 3
  slug: maplith-com-context
layout: provider
modified: '2026-10-30'
name: maplith-com
nav: Providers
network: true
overview: 'maplith-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Data Integration, and Knowledge Graph.


  The maplith-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  maplith-com''s developer surface includes sandbox, documentation, getting-started guide, pricing, support, and 16 more developer resources.'
plans:
- name: Maplith Com Plans Pricing
  plan_count: 1
  slug: maplith-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: maplith-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: maplith-com-rules
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 20.2
    developer_ergonomics: 20.2
    discoverability: 65.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.3
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/maplith-com/maplith-com-2026-11-03T135321.png
security:
- kind: domain-security
  name: Maplith Com Domain Security
  slug: maplith-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: maplith-com
tags:
- Company
- Artificial Intelligence
- Automation
- Data Integration
- Knowledge Graph
- Platform
website: https://maplith.com/
---
