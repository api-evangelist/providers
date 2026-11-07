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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.getnoded.ai
  baseurl_source: declared
  description: 'Noded AI API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-25); not the provider''s own document.'
  name: Noded AI API
  slug: noded-so-api
- description: 'The Noded (Apollo) GraphQL API behind the Customer Context Graph. One POST endpoint serving people and accounts (both modelled as tags), the unified activity timeline (blocks: notes, emails, tasks, me'
  name: Noded GraphQL API
  slug: noded-graphql-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/noded-so/plans/noded-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/noded-so-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/noded-so/rules/noded-so-rules.yml
  title: ''
  type: Spectral
  url: rules/noded-so-rules.yml
- group: design
  href: https://artifacts.apis.io/noded-so/json-ld/noded-so-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/noded-so-context.jsonld
- group: design
  href: https://artifacts.apis.io/noded-so/vocabulary/noded-so-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/noded-so-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/noded-so/data-model/noded-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/noded-so-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.getnoded.ai/security
- group: design
  href: https://artifacts.apis.io/noded-so/conformance/noded-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/noded-so-conformance.yml
- group: agent
  href: https://artifacts.apis.io/noded-so/llms/noded-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/noded-so-llms.txt
- group: agent
  href: https://artifacts.apis.io/noded-so/well-known/noded-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/noded-so-well-known.yml
- group: other
  href: https://artifacts.apis.io/noded-so/hosts/noded-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/noded-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/noded-so/vendors/noded-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/noded-so-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getnoded.ai/terms
- group: auth
  title: ''
  type: Security
  url: https://www.getnoded.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getnoded.ai/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.getnoded.ai/developers/workspace-setup
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.getnoded.ai/api/v1/graph</code
- group: auth
  href: https://artifacts.apis.io/noded-so/security/noded-so-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/noded-so-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/noded-so/security/noded-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/noded-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getnoded.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.getnoded.ai/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getnoded.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.getnoded.ai/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.getnoded.ai/developers#reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Notify-AI
coverage:
  checked: '2026-10-25'
  detail: API spec endpoints return HTTP 403, indicating authentication is required.
  evidence:
  - status: 403
    url: https://api.noded.so/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-25'
description: Noded AI provides a Customer Context Graph that unifies data from over 20 tools into a living story for each account. By automatically weaving together customer data, Noded enables teams, agents, and large language models to access comprehensive, up-to-date context, improving AI-driven interactions and decision-making. The platform emphasizes zero admin setup and delivers a unified view of customer information across services.
image: https://www.getnoded.ai/favicon.svg
json_schemas:
- name: GetAuthConnectResponse
  property_count: 3
  slug: noded-so-get-auth-connect-response
- name: PostApplicationLinkRequest
  property_count: 3
  slug: noded-so-post-application-link-request
- name: PostExecuteFunctionRequest
  property_count: 5
  slug: noded-so-post-execute-function-request
- name: PostExecuteQueryRequest
  property_count: 4
  slug: noded-so-post-execute-query-request
- name: PostSyncTranscriptionRequest
  property_count: 2
  slug: noded-so-post-sync-transcription-request
- name: PostTagRequest
  property_count: 4
  slug: noded-so-post-tag-request
jsonld:
- class_count: 36
  name: Noded So Context
  property_count: 46
  slug: noded-so-context
layout: provider
mcp_servers:
- description: ''
  name: Noded AI MCP Server
  slug: noded-ai-mcp-yml
modified: '2026-10-25'
name: Noded AI
nav: Providers
network: true
overview: 'Noded AI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Customer Data, Context Graph, Integration, and Automation.


  The Noded AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Noded AI''s developer surface includes getting-started guide, documentation, pricing, engineering blog, API reference, and 19 more developer resources.'
plans:
- name: Noded So Plans Pricing
  plan_count: 2
  slug: noded-so-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Noded AI API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: noded-so-rules
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 70.0
    catalog_earned_first_party: 8.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 64.5
    contract_governance: 33.3
    contract_quality: 25.2
    developer_ergonomics: 40.5
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 45.4
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
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/noded-so/noded-so-2026-11-03T140244.png
security:
- kind: domain-security
  name: Noded So Domain Security
  slug: noded-so-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Noded So Trust Center
  slug: noded-so-trust-center
  summary_line: SOC 2, GDPR
slug: noded-so
tags:
- Artificial Intelligence
- Customer Data
- Context Graph
- Integration
- Automation
- Company
website: https://www.getnoded.ai/
---
