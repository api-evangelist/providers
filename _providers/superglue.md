---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Superglue Agentic Access
  operation_count: 25
  slug: superglue-agentic-access
  summary_line: 25 operations · 14 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.superglue.cloud/v1
  baseurl_source: declared
  description: Configure identities and reusable OAuth apps.
  name: Index Commerce Connections API
  slug: superglue-connections-api
- baseURL: https://api.superglue.cloud/v1
  baseurl_source: declared
  description: Inspect execution state and retrieve run outputs.
  name: Index Commerce Runs API
  slug: superglue-runs-api
- baseURL: https://api.superglue.cloud/v1
  baseurl_source: declared
  description: Create, inspect, update, and execute saved tools.
  name: Index Commerce Tools API
  slug: superglue-tools-api
- baseURL: https://api.superglue.cloud/v1
  baseurl_source: declared
  description: Verify webhook subscriptions and trigger tools from incoming events.
  name: Index Commerce Webhooks API
  slug: superglue-webhooks-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/superglue/agentic-access/superglue-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/superglue-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/superglue/rules/superglue-rules.yml
  title: ''
  type: Spectral
  url: rules/superglue-rules.yml
- group: design
  href: https://artifacts.apis.io/superglue/json-ld/superglue-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/superglue-context.jsonld
- group: design
  href: https://artifacts.apis.io/superglue/vocabulary/superglue-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/superglue-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/superglue/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/superglue/data-model/superglue-data-model.yml
  title: ''
  type: DataModel
  url: data-model/superglue-data-model.yml
- group: design
  href: https://artifacts.apis.io/superglue/errors/superglue-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/superglue-problem-types.yml
- group: design
  href: https://artifacts.apis.io/superglue/conformance/superglue-conformance.yml
  title: ''
  type: Conformance
  url: conformance/superglue-conformance.yml
- group: agent
  href: https://artifacts.apis.io/superglue/llms/superglue-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/superglue-llms.txt
- group: agent
  href: https://artifacts.apis.io/superglue/well-known/superglue-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/superglue-well-known.yml
- group: other
  href: https://artifacts.apis.io/superglue/hosts/superglue-hosts.yml
  title: ''
  type: Hosts
  url: hosts/superglue-hosts.yml
- group: other
  href: https://artifacts.apis.io/superglue/vendors/superglue-vendors.yml
  title: ''
  type: Vendors
  url: vendors/superglue-vendors.yml
- group: build
  href: https://artifacts.apis.io/superglue/packages/superglue-packages.yml
  title: ''
  type: SDKs
  url: packages/superglue-packages.yml
- group: build
  href: https://artifacts.apis.io/superglue/packages/superglue-packages.yml
  title: ''
  type: Packages
  url: packages/superglue-packages.yml
- group: auth
  href: https://artifacts.apis.io/superglue/authentication/superglue-authentication.yml
  title: ''
  type: Authentication
  url: authentication/superglue-authentication.yml
- group: auth
  href: https://artifacts.apis.io/superglue/security/superglue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/superglue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://superglue.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://superglue.ai/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://superglue.ai/developers/
- group: company
  title: ''
  type: Blog
  url: https://superglue.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://superglue.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://superglue.ai/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://superglue.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://superglue.ai/privacy/
created: '2026-10-18'
description: Index Commerce provides a comprehensive e‑commerce platform that enables brands and retailers to create, manage, and scale online storefronts. The solution offers a suite of tools for product catalog management, checkout optimization, inventory synchronization, and analytics, helping merchants deliver seamless shopping experiences across web, mobile, and marketplace channels. Index Commerce focuses on flexibility, integration capabilities, and performance, supporting businesses from startups to enterprise-level operations.
image: https://superglue.ai/logos/sg_logo.png
json_schemas:
- name: Connection
  property_count: 15
  slug: superglue-connection
- name: CreateToolRequest
  property_count: 8
  slug: superglue-create-tool-request
- name: RunRequest
  property_count: 7
  slug: superglue-run-request
- name: Run
  property_count: 16
  slug: superglue-run
- name: Tool
  property_count: 14
  slug: superglue-tool
- name: UpdateToolRequest
  property_count: 8
  slug: superglue-update-tool-request
jsonld:
- class_count: 20
  name: Superglue Context
  property_count: 93
  slug: superglue-context
layout: provider
modified: '2026-10-18'
name: Index Commerce
nav: Providers
network: true
overview: 'Index Commerce publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Connections API, Runs API, Tools API, and 1 more. Tagged areas include Company, E-Commerce, Platform, Storefront, and Analytics.


  The Index Commerce catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Index Commerce''s developer surface includes authentication, documentation, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Index Commerce API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: superglue-rules
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 61.3
    developer_ergonomics: 42.3
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Superglue Authentication
  slug: superglue-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Superglue Domain Security
  slug: superglue-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: superglue-create-and-list-connections
  slug: superglue-create-and-list-connections
- name: superglue-get-run-results
  slug: superglue-get-run-results
- name: superglue-webhooks-setup
  slug: superglue-webhooks-setup
slug: superglue
tags:
- Company
- E-Commerce
- Platform
- Storefront
- Analytics
website: https://superglue.ai/
---
