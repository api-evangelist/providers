---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: BoardMark provides a SaaS issue board platform with AI agents. Documentation is available at the public docs site.
  name: BoardMark API
  slug: boardmark-api
- description: 'BoardMark API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BoardMark API
  slug: boardmark-ai-api
artifact_total: 9
asyncapis:
- description: ''
  name: Boardmark Ai Webhooks
  slug: boardmark-ai-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/boardmark-ai/plans/boardmark-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boardmark-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/boardmark-ai/rules/boardmark-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/boardmark-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/boardmark-ai/json-ld/boardmark-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/boardmark-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/boardmark-ai/vocabulary/boardmark-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/boardmark-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/boardmark-ai/asyncapi/boardmark-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/boardmark-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/boardmark-ai/data-model/boardmark-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/boardmark-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/boardmark-ai/conformance/boardmark-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boardmark-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boardmark-ai/llms/boardmark-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boardmark-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/boardmark-ai/well-known/boardmark-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boardmark-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/boardmark-ai/hosts/boardmark-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boardmark-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/boardmark-ai/vendors/boardmark-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boardmark-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boardmark.ai/legal/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.boardmark.ai/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boardmark.ai/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.boardmark.ai/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.boardmark.ai/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.boardmark.ai/docs/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://www.boardmark.ai/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/boardmark-ai/security/boardmark-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boardmark-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boardmark.ai/
coverage:
  checked: '2026-11-02'
  detail: Documentation is public but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://www.boardmark.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BoardMark is a SaaS issue board platform offering Scrum, Kanban, and delivery pipeline boards enhanced with AI agents. Operated by I C Develop Company Limited in Thailand, it provides markdown‑based issue tracking, AI‑driven automation, integrations with GitHub, GitLab, and webhooks, and supports billing via card, PromptPay, or bank transfer. The service runs on AWS in the Thailand region.
image: https://www.boardmark.ai/og.png
json_schemas:
- name: PostBoardmarkRequest
  property_count: 6
  slug: boardmark-ai-post-boardmark-request
- name: PostBoardmarkResponse
  property_count: 1
  slug: boardmark-ai-post-boardmark-response
jsonld:
- class_count: 2
  name: Boardmark Ai Context
  property_count: 7
  slug: boardmark-ai-context
layout: provider
modified: '2026-11-02'
name: BoardMark
nav: Providers
network: true
overview: 'BoardMark is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Project Management, Artificial Intelligence, and Collaboration.


  The BoardMark catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BoardMark''s developer surface includes signup flow, pricing, documentation, changelog, getting-started guide, and 15 more developer resources.'
plans:
- name: Boardmark Ai Plans Pricing
  plan_count: 3
  slug: boardmark-ai-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: BoardMark API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: boardmark-ai-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 26.7
    developer_ergonomics: 10.7
    discoverability: 57.1
    operational_transparency: 15.8
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boardmark Ai Domain Security
  slug: boardmark-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boardmark-ai
tags:
- Company
- Software-as-a-Service
- Project Management
- Artificial Intelligence
- Collaboration
website: https://www.boardmark.ai/
---
