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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for managing projects, tasks, sections, and related resources in BasicOps.
  name: BasicOps API
  slug: basicops-api
- baseURL: https://api.basicops.com
  baseurl_source: declared
  description: 'BasicOps API as documented publicly: 49 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BasicOps API
  slug: basicops-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/basicops-com/plans/basicops-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/basicops-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/basicops-com/rules/basicops-com-rules.yml
  title: ''
  type: Spectral
  url: rules/basicops-com-rules.yml
- group: design
  href: https://artifacts.apis.io/basicops-com/json-ld/basicops-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/basicops-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/basicops-com/vocabulary/basicops-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/basicops-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/basicops-com/data-model/basicops-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/basicops-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/basicops-com/conformance/basicops-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/basicops-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/basicops-com/llms/basicops-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/basicops-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/basicops-com/well-known/basicops-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/basicops-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/basicops-com/hosts/basicops-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/basicops-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/basicops-com/vendors/basicops-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/basicops-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.basicops.com/terms-policy/
- group: start
  title: ''
  type: SignUp
  url: https://app.basicops.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.basicops.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.basicops.com/press/
- group: company
  title: ''
  type: Blog
  url: https://www.basicops.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.basicops.com/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://developer.basicops.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BasicOps
- group: auth
  href: https://artifacts.apis.io/basicops-com/security/basicops-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/basicops-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://basicops.com/
coverage:
  checked: '2026-11-02'
  detail: Documentation is provided as HTML pages without any machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://developer.basicops.com/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BasicOps provides a collaborative workspace where human teams and AI agents work together seamlessly. The platform combines project management, task tracking, and chat in a unified interface, enabling users to plan, collaborate, and execute work with AI assistance. Features include integrated tools such as Slack, Zoom, Google Drive, and many others, offering unlimited tasks, messages, and storage across various plans. BasicOps aims to reduce context-switching and improve productivity by bringing all work contexts into one place.
image: https://www.basicops.com/assets/img/appwin-hero-home.png
json_schemas:
- name: GetV1WebhookResponse
  property_count: 9
  slug: basicops-com-get-v1-webhook-response
- name: PostV1ChatResponse
  property_count: 3
  slug: basicops-com-post-v1-chat-response
- name: PostV1GroupchatResponse
  property_count: 3
  slug: basicops-com-post-v1-groupchat-response
- name: PostV1ProjectProjectidResponse
  property_count: 10
  slug: basicops-com-post-v1-project-projectid-response
- name: PostV1WebhookRequest
  property_count: 8
  slug: basicops-com-post-v1-webhook-request
- name: PutV1WebhookResponse
  property_count: 10
  slug: basicops-com-put-v1-webhook-response
jsonld:
- class_count: 65
  name: Basicops Com Context
  property_count: 71
  slug: basicops-com-context
layout: provider
modified: '2026-11-02'
name: BasicOps
nav: Providers
network: true
overview: 'BasicOps is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Project Management, AI Agents, Productivity, and Software-as-a-Service.


  The BasicOps catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BasicOps'' developer surface includes signup flow, pricing, engineering blog, API reference, documentation, and 15 more developer resources.'
plans:
- name: Basicops Com Plans Pricing
  plan_count: 4
  slug: basicops-com-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: BasicOps API Rules
  rule_count: 45
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 2
  slug: basicops-com-rules
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 9.5
    discoverability: 58.0
    operational_transparency: 2.6
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
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Basicops Com Domain Security
  slug: basicops-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: basicops-com
tags:
- Collaboration
- Project Management
- AI Agents
- Productivity
- Software-as-a-Service
website: https://basicops.com/
---
