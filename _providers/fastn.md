---
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Fastn HTTP API reference
  name: Fastn API
  slug: fastn-api-2
- baseURL: https://api.fastn.dev
  baseurl_source: declared
  description: 'Fastn API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Fastn API
  slug: fastn-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/fastn/plans/fastn-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fastn-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fastn/rules/fastn-rules.yml
  title: ''
  type: Spectral
  url: rules/fastn-rules.yml
- group: design
  href: https://artifacts.apis.io/fastn/json-ld/fastn-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fastn-context.jsonld
- group: design
  href: https://artifacts.apis.io/fastn/vocabulary/fastn-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fastn-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fastn/data-model/fastn-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fastn-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fastn.ai/
- group: auth
  href: https://artifacts.apis.io/fastn/authentication/fastn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fastn-authentication.yml
- group: design
  href: https://artifacts.apis.io/fastn/conformance/fastn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fastn-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fastn/llms/fastn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fastn-llms.txt
- group: agent
  href: https://artifacts.apis.io/fastn/well-known/fastn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fastn-well-known.yml
- group: other
  href: https://artifacts.apis.io/fastn/hosts/fastn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fastn-hosts.yml
- group: other
  href: https://artifacts.apis.io/fastn/vendors/fastn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fastn-vendors.yml
- group: auth
  href: https://artifacts.apis.io/fastn/security/fastn-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fastn-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fastn/security/fastn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fastn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fastn.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fastn.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fastn.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fastn.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fastn.ai/fastn/readme/getting-started
- group: operate
  title: ''
  type: Support
  url: https://fastn.ai/support
- group: company
  title: ''
  type: Blog
  url: https://fastn.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fastn-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://fastn.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fastn.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fastn.ai/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/fastn/workspace/fastn-api
coverage:
  detail: API reference page renders via JavaScript, no machine‑readable OpenAPI found.
  evidence:
  - status: 200
    url: https://docs.fastn.ai/reference/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: Fastn provides an integration layer for SaaS applications, enabling unified APIs, workflow automation, and a marketplace for integration agents. It offers a platform where developers can build, version, and govern data pipelines across various SaaS tools, with features like MCP gateway, tool access controls, and AI‑driven agents to simplify complex integrations. Fastn’s solution targets sales, CRM, and product teams seeking to synchronize revenue apps, embed customer integrations, and accelerate product development through a single schema across apps.
image: https://fastn.ai/og.png
json_schemas:
- name: PostApiV1EmbedTokenRefreshResponse
  property_count: 2
  slug: fastn-post-api-v1-embed-token-refresh-response
- name: PostApiV1EmbedTokenRequest
  property_count: 3
  slug: fastn-post-api-v1-embed-token-request
- name: PostApiV1EmbedTokenResponse
  property_count: 4
  slug: fastn-post-api-v1-embed-token-response
- name: PostApiV1WorkflowsWorkflowidExecuteRequest
  property_count: 1
  slug: fastn-post-api-v1-workflows-workflowid-execute-request
- name: PostApiV1WorkflowsWorkflowidExecuteResponse
  property_count: 2
  slug: fastn-post-api-v1-workflows-workflowid-execute-response
- name: PostRequest
  property_count: 1
  slug: fastn-post-request
jsonld:
- class_count: 8
  name: Fastn Context
  property_count: 6
  slug: fastn-context
layout: provider
modified: '2026-10-20'
name: Fastn
nav: Providers
network: true
overview: 'Fastn is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Integration Platform, B2B SaaS, Embedded Widget, Unified API, and Data Integration.


  The Fastn catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fastn''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Fastn Plans Pricing
  plan_count: 3
  slug: fastn-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Fastn API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: fastn-rules
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 35.6
    contract_quality: 24.1
    developer_ergonomics: 61.9
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Fastn Authentication
  slug: fastn-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fastn Domain Security
  slug: fastn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fastn Trust Center
  slug: fastn-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: fastn
tags:
- Integration Platform
- B2B SaaS
- Embedded Widget
- Unified API
- Data Integration
- AI Agents
- CRM Integration
- Security
website: https://fastn.ai/
---
