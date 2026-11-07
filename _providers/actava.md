---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Actava Agentic Access
  operation_count: 2
  slug: actava-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://inference.actava.ai/v1
  baseurl_source: declared
  description: Discover the models an API key can access.
  name: Actava.ai Models API
  slug: actava-models-api
- baseURL: https://inference.actava.ai/v1
  baseurl_source: declared
  description: Generate a model response for a conversation.
  name: Actava.ai Chat Completions API
  slug: actava-chat-completions-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/actava/plans/actava-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/actava-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/actava/data-model/actava-data-model.yml
  title: ''
  type: DataModel
  url: data-model/actava-data-model.yml
- group: auth
  href: https://artifacts.apis.io/actava/well-known/actava-actava-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/actava-actava-security.txt
- group: agent
  href: https://artifacts.apis.io/actava/agentic-access/actava-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/actava-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/actava/rules/actava-rules.yml
  title: ''
  type: Spectral
  url: rules/actava-rules.yml
- group: design
  href: https://artifacts.apis.io/actava/vocabulary/actava-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/actava-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/actava/changelog/actava-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/actava-changelog.yml
- group: auth
  href: https://artifacts.apis.io/actava/authentication/actava-authentication.yml
  title: ''
  type: Authentication
  url: authentication/actava-authentication.yml
- group: design
  href: https://artifacts.apis.io/actava/conformance/actava-conformance.yml
  title: ''
  type: Conformance
  url: conformance/actava-conformance.yml
- group: agent
  href: https://artifacts.apis.io/actava/llms/actava-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/actava-llms.txt
- group: agent
  href: https://artifacts.apis.io/actava/well-known/actava-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/actava-well-known.yml
- group: other
  href: https://artifacts.apis.io/actava/hosts/actava-hosts.yml
  title: ''
  type: Hosts
  url: hosts/actava-hosts.yml
- group: other
  href: https://artifacts.apis.io/actava/vendors/actava-vendors.yml
  title: ''
  type: Vendors
  url: vendors/actava-vendors.yml
- group: build
  href: https://artifacts.apis.io/actava/packages/actava-packages.yml
  title: ''
  type: SDKs
  url: packages/actava-packages.yml
- group: build
  href: https://artifacts.apis.io/actava/packages/actava-packages.yml
  title: ''
  type: Packages
  url: packages/actava-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.actava.ai/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://actava.statuspage.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.actava.ai/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.actava.ai/news
- group: other
  title: ''
  type: Leadership
  url: https://www.actava.ai/about/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.actava.ai/cura/docs/changelog
- group: auth
  href: https://artifacts.apis.io/actava/security/actava-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/actava-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://actava.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.actava.ai/cura/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.actava.ai/cura/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.actava.ai/products
- group: company
  title: ''
  type: Blog
  url: https://www.actava.ai/news?categories=Blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.actava.ai/aws-marketplace
created: '2026-10-15'
description: Actava.ai provides a healthcare workflow-to-model learning platform offering AI-driven lifecycle development, compliance, and custom intelligence solutions. Their suite includes model building, simulation, benchmarking, and integration with AWS Marketplace, targeting providers, payers, and pharma to accelerate AI transformation and governance.
finops:
- has_sources: true
  method: derived
  name: Actava Finops
  primary_unit: ''
  service_category: ''
  slug: actava-finops
  template: true
image: https://www.actava.ai/share-card.png
json_schemas:
- name: ChatCompletionRequest
  property_count: 0
  slug: actava-chat-completion-request
- name: ChatCompletion
  property_count: 0
  slug: actava-chat-completion
- name: ModelList
  property_count: 0
  slug: actava-model-list
layout: provider
modified: '2026-10-15'
name: Actava.ai
nav: Providers
network: true
overview: 'Actava.ai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Models API and Chat Completions API. Tagged areas include Company, Artificial Intelligence, Healthcare, Machine Learning, and Platform.


  The Actava.ai catalog on APIs.io includes 1 Spectral governance ruleset.


  Actava.ai''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Actava Plans Pricing
  plan_count: 0
  slug: actava-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Actava.ai API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: actava-rules
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 15.8
    contract_governance: 35.6
    contract_quality: 52.7
    developer_ergonomics: 34.5
    discoverability: 75.0
    operational_transparency: 26.3
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/actava/actava-2026-11-03T120233.png
security:
- kind: authentication
  name: Actava Authentication
  slug: actava-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Actava Domain Security
  slug: actava-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: actava
tags:
- Company
- Artificial Intelligence
- Healthcare
- Machine Learning
- Platform
website: https://actava.ai/
---
