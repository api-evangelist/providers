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
  band_gated_from: agent-native
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for accessing Circleback meeting data, actions, calendar, companies, folders, people, and tags.
  name: Circleback API
  slug: circleback-api
- description: 'Circleback API as documented publicly: 24 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Circleback API
  slug: circleback-ai-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/circleback-ai/plans/circleback-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/circleback-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/circleback-ai/rules/circleback-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/circleback-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/circleback-ai/json-ld/circleback-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/circleback-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/circleback-ai/vocabulary/circleback-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/circleback-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/circleback-ai/data-model/circleback-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/circleback-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/circleback-ai/cli/circleback-ai-cli.yml
  title: ''
  type: CLI
  url: cli/circleback-ai-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://circleback.ai/docs/support/security/security
- group: auth
  href: https://artifacts.apis.io/circleback-ai/security/circleback-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/circleback-ai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/circleback-ai/conformance/circleback-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/circleback-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/circleback-ai/llms/circleback-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/circleback-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/circleback-ai/mcp/circleback-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/circleback-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/circleback-ai/well-known/circleback-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/circleback-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/circleback-ai/well-known/circleback-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/circleback-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/circleback-ai/hosts/circleback-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/circleback-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/circleback-ai/vendors/circleback-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/circleback-ai-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://circleback.ai/integrations/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://circleback.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://support.circleback.ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.circleback.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://circleback.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://circleback.ai/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://circleback.ai/releases
- group: company
  title: ''
  type: Blog
  url: https://circleback.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://circleback.ai/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://circleback.ai/docs/support/recording/getting-started-with-recording
- group: docs
  title: ''
  type: APIReference
  url: https://circleback.ai/docs/api
- group: auth
  href: https://artifacts.apis.io/circleback-ai/security/circleback-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/circleback-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/circleback-ai/security/circleback-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/circleback-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/circleback-ai/security/circleback-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/circleback-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://circleback.ai/
coverage:
  checked: '2026-11-04'
  detail: Provider documentation lists API endpoints but no machine‑readable OpenAPI, GraphQL, AsyncAPI or gRPC spec is publicly available.
  evidence:
  - status: 200
    url: https://circleback.ai/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Turn every conversation into clear meeting notes, action items, and searchable company knowledge. Circleback records and transcribes virtual and in-person meetings in 100+ languages, with support for Zoom, Google Meet, Microsoft Teams, and Slack huddles. Extract custom insights and automate updates to your CRM, issue tracker, and other apps. Ask questions across your team’s conversations, connect your AI agents, and automatically give the right people and agents the context they need.
image: https://circleback.ai/marketing/og/default.png
json_schemas:
- name: GetFolderStringResponse
  property_count: 16
  slug: circleback-ai-get-folder-string-response
- name: PostFolderStringShareResponse
  property_count: 18
  slug: circleback-ai-post-folder-string-share-response
- name: PostMeetingsResponse
  property_count: 8
  slug: circleback-ai-post-meetings-response
- name: PutFolderStringResponse
  property_count: 16
  slug: circleback-ai-put-folder-string-response
- name: PutMeetingStringResponse
  property_count: 18
  slug: circleback-ai-put-meeting-string-response
- name: PutMeetingStringShareResponse
  property_count: 18
  slug: circleback-ai-put-meeting-string-share-response
jsonld:
- class_count: 22
  name: Circleback Ai Context
  property_count: 72
  slug: circleback-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at circleback.ai.
  name: Circleback MCP Server
  slug: circleback-ai-mcp-yml
modified: '2026-11-03'
name: Circleback
nav: Providers
network: true
overview: 'Circleback is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Notetaker, Automation, Meetings, and Transcription.


  The Circleback catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Circleback''s developer surface includes CLI, support, changelog, engineering blog, pricing, getting-started guide, API reference, and 23 more developer resources.'
plans:
- name: Circleback Ai Plans Pricing
  plan_count: 4
  slug: circleback-ai-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Circleback API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: circleback-ai-rules
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 20.2
    discoverability: 56.7
    operational_transparency: 30.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Circleback Ai Domain Security
  slug: circleback-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Circleback Ai Vulnerability Disclosure
  slug: circleback-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Circleback Ai Trust Center
  slug: circleback-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: circleback-ai
tags:
- Artificial Intelligence
- Notetaker
- Automation
- Meetings
- Transcription
website: https://circleback.ai/
---
