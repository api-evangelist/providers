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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Churn Solution API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Churn Solution API
  slug: churnsolution-com-api
artifact_total: 7
asyncapis:
- description: ''
  name: Churnsolution Com Webhooks
  slug: churnsolution-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/churnsolution-com/plans/churnsolution-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/churnsolution-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/churnsolution-com/rules/churnsolution-com-rules.yml
  title: ''
  type: Spectral
  url: rules/churnsolution-com-rules.yml
- group: design
  href: https://artifacts.apis.io/churnsolution-com/json-ld/churnsolution-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/churnsolution-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/churnsolution-com/vocabulary/churnsolution-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/churnsolution-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/churnsolution-com/asyncapi/churnsolution-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/churnsolution-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/churnsolution-com/data-model/churnsolution-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/churnsolution-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/churnsolution-com/conformance/churnsolution-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/churnsolution-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/churnsolution-com/llms/churnsolution-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/churnsolution-com-llms.txt
- group: other
  href: https://artifacts.apis.io/churnsolution-com/hosts/churnsolution-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/churnsolution-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/churnsolution-com/vendors/churnsolution-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/churnsolution-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://churnsolution.com/terms-of-use/
- group: start
  title: ''
  type: SignUp
  url: https://app.churnsolution.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://churnsolution.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://churnsolution.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://churnsolution.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://churnsolution.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://churnsolution.com/products/easy-setup/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Churnsolution
- group: auth
  href: https://artifacts.apis.io/churnsolution-com/security/churnsolution-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/churnsolution-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://churnsolution.com/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://churnsolution.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Churn Solution provides AI‑powered tools to reduce subscription cancellations and boost customer retention. Their platform offers automated cancellation flows, payment recovery, win‑back campaigns, and a 3‑month money‑back guarantee, promising up to a 52% reduction in churn. The service targets SaaS businesses seeking to keep more customers and increase revenue through intelligent, data‑driven engagement.
image: https://churnsolution.com/wp-content/uploads/2023/09/cropped-logo-1-2.png
json_schemas:
- name: PostApiChurnSolutionResponse
  property_count: 2
  slug: churnsolution-com-post-api-churn-solution-response
jsonld:
- class_count: 1
  name: Churnsolution Com Context
  property_count: 2
  slug: churnsolution-com-context
layout: provider
modified: '2026-11-03'
name: Churn Solution
nav: Providers
network: true
overview: 'Churn Solution is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Software-as-a-Service, Customer Retention, Artificial Intelligence, Subscription Management, and Marketing.


  The Churn Solution catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Churn Solution''s developer surface includes signup flow, pricing, documentation, engineering blog, getting-started guide, and 15 more developer resources.'
plans:
- name: Churnsolution Com Plans Pricing
  plan_count: 2
  slug: churnsolution-com-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Churn Solution API Rules
  rule_count: 28
  severity_counts:
    error: 26
    hint: 0
    info: 1
    warn: 1
  slug: churnsolution-com-rules
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.2
    catalog_earned_first_party: 8.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 24.3
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Churnsolution Com Domain Security
  slug: churnsolution-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: churnsolution-com
tags:
- Software-as-a-Service
- Customer Retention
- Artificial Intelligence
- Subscription Management
- Marketing
website: https://churnsolution.com/
---
