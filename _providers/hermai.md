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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Branding and marketing tools API
  name: Hermai Brand API
  slug: hermai-brand-api
- baseURL: https://api.hermai.ai
  baseurl_source: declared
  description: Public schema registry lookup and schema request intake for agent workflows.
  name: Hermai Agent-Native API API
  slug: hermai-agent-native-api-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/hermai/llms/hermai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hermai-llms.txt
- group: other
  href: https://artifacts.apis.io/hermai/vendors/hermai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hermai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hermai.ai/legal/terms
- group: start
  title: ''
  type: Login
  url: https://hermai.ai/login
- group: commercial
  href: https://artifacts.apis.io/hermai/plans/hermai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hermai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hermai/rules/hermai-rules.yml
  title: ''
  type: Spectral
  url: rules/hermai-rules.yml
- group: design
  href: https://artifacts.apis.io/hermai/json-ld/hermai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hermai-context.jsonld
- group: design
  href: https://artifacts.apis.io/hermai/vocabulary/hermai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hermai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/hermai/data-model/hermai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hermai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/hermai/authentication/hermai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hermai-authentication.yml
- group: design
  href: https://artifacts.apis.io/hermai/errors/hermai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hermai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hermai/conformance/hermai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hermai-conformance.yml
- group: other
  href: https://artifacts.apis.io/hermai/a2a/hermai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hermai-a2a.yml
- group: other
  href: https://artifacts.apis.io/hermai/hosts/hermai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hermai-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://hermai.ai/trust
- group: start
  title: ''
  type: Sandbox
  url: https://hermai.ai/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://hermai.ai/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hermai-ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hermai.ai/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hermai.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://hermai.ai/changelog
- group: company
  title: ''
  type: Website
  url: https://hermai.ai/
- group: auth
  href: https://artifacts.apis.io/hermai/security/hermai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hermai-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://hermai.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hermai.ai/privacy
created: '2026-10-17'
description: Hermai Brand API provides a suite of branding and marketing tools designed to help businesses create, manage, and analyze their brand assets. The platform offers APIs for logo generation, color palette selection, brand guidelines management, and performance analytics. It aims to streamline brand consistency across digital channels, enabling developers to integrate branding capabilities directly into their applications and workflows. With robust documentation and support, Hermai empowers companies to maintain a cohesive visual identity and measure brand impact effectively.
image: https://hermai.ai/opengraph-image.jpg?opengraph-image.13wwxpach21ly.jpg
json_schemas:
- name: BrandDemoPending
  property_count: 3
  slug: hermai-brand-demo-pending
- name: BrandDemoRequest
  property_count: 1
  slug: hermai-brand-demo-request
- name: BrandDemoResponse
  property_count: 3
  slug: hermai-brand-demo-response
- name: BrandEnvelope
  property_count: 9
  slug: hermai-brand-envelope
- name: BrandRetrieveRequest
  property_count: 6
  slug: hermai-brand-retrieve-request
jsonld:
- class_count: 14
  name: Hermai Context
  property_count: 53
  slug: hermai-context
layout: provider
modified: '2026-10-17'
name: Hermai Brand API
nav: Providers
network: true
overview: 'Hermai Brand API publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Hermai Agent-Native API API, and 1 more. Tagged areas include Company, Branding, Marketing, and Software-as-a-Service.


  The Hermai Brand API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hermai Brand API''s developer surface includes authentication, sandbox, pricing, getting-started guide, documentation, API reference, engineering blog, and 18 more developer resources.'
plans:
- name: Hermai Plans Pricing
  plan_count: 3
  slug: hermai-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Hermai Brand API API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: hermai-rules
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.8
  facets:
    access_clarity: 57.9
    contract_governance: 22.0
    contract_quality: 51.0
    developer_ergonomics: 31.0
    discoverability: 64.3
    operational_transparency: 2.6
  previous_composite: 53.2
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hermai/hermai-2026-11-03T133352.png
security:
- kind: authentication
  name: Hermai Authentication
  slug: hermai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hermai Domain Security
  slug: hermai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: hermai
tags:
- Company
- Branding
- Marketing
- Software-as-a-Service
website: https://hermai.ai/
---
