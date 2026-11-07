---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Ausca Com Agentic Access
  operation_count: 27
  slug: ausca-com-agentic-access
  summary_line: 27 operations · 14 acting
api_count: 1
apis:
- baseURL: https://ausca.com
  baseurl_source: declared
  description: The Agent Inboxes API from Ausca — 4 operation(s) for agent inboxes.
  name: Ausca Agent Inboxes API
  slug: ausca-com-agent-inboxes-api
- baseURL: https://ausca.com
  baseurl_source: declared
  description: The Analyze Document API from Ausca — 1 operation(s) for analyze document.
  name: Ausca Analyze Document API
  slug: ausca-com-analyze-document-api
- baseURL: https://ausca.com
  baseurl_source: declared
  description: The Artifacts API from Ausca — 2 operation(s) for artifacts.
  name: Ausca Artifacts API
  slug: ausca-com-artifacts-api
- baseURL: https://ausca.com
  baseurl_source: declared
  description: The Browser Sessions API from Ausca — 2 operation(s) for browser sessions.
  name: Ausca Browser Sessions API
  slug: ausca-com-browser-sessions-api
- baseURL: https://ausca.com
  baseurl_source: declared
  description: The Extend Inbox API from Ausca — 1 operation(s) for extend inbox.
  name: Ausca Extend Inbox API
  slug: ausca-com-extend-inbox-api
- baseURL: https://ausca.com
  baseurl_source: declared
  description: The Extract Text API from Ausca — 1 operation(s) for extract text.
  name: Ausca Extract Text API
  slug: ausca-com-extract-text-api
- baseURL: https://ausca.com
  baseurl_source: declared
  description: The Invocations API from Ausca — 3 operation(s) for invocations.
  name: Ausca Invocations API
  slug: ausca-com-invocations-api
- baseURL: https://ausca.com
  baseurl_source: declared
  description: The Lease Browser API from Ausca — 1 operation(s) for lease browser.
  name: Ausca Lease Browser API
  slug: ausca-com-lease-browser-api
- baseURL: https://ausca.com
  baseurl_source: declared
  description: The Offers API from Ausca — 2 operation(s) for offers.
  name: Ausca Offers API
  slug: ausca-com-offers-api
- baseURL: https://ausca.com
  baseurl_source: declared
  description: The Open Inbox API from Ausca — 1 operation(s) for open inbox.
  name: Ausca Open Inbox API
  slug: ausca-com-open-inbox-api
- baseURL: https://ausca.com
  baseurl_source: declared
  description: The Transcribe Media API from Ausca — 1 operation(s) for transcribe media.
  name: Ausca Transcribe Media API
  slug: ausca-com-transcribe-media-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/ausca-com/agentic-access/ausca-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ausca-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ausca-com/rules/ausca-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ausca-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ausca-com/json-ld/ausca-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ausca-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ausca-com/vocabulary/ausca-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ausca-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ausca-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ausca-com/data-model/ausca-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ausca-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/ausca-com/conventions/ausca-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ausca-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/ausca-com/conventions/ausca-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ausca-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/ausca-com/errors/ausca-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ausca-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ausca-com/conformance/ausca-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ausca-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ausca-com/llms/ausca-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ausca-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ausca-com/well-known/ausca-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ausca-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ausca-com/hosts/ausca-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ausca-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ausca-com/vendors/ausca-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ausca-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ausca-com/authentication/ausca-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ausca-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ausca-com/security/ausca-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ausca-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ausca.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ausca.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ausca.com/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://ausca.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://ausca.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ausca.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ausca.com/terms
created: '2026-11-02'
description: Ausca provides pay‑per‑call APIs and MCP services enabling agents to purchase on‑demand infrastructure such as document OCR, media transcription, browser sessions, and inbox handling. The platform offers transparent pricing, receipt‑backed execution, and detailed retry rules, allowing developers to integrate AI‑driven capabilities without managing underlying resources. Services are described via SKILL.md files and an OpenAPI specification, with comprehensive documentation, privacy policy, terms of service, and support resources publicly available.
json_schemas:
- name: ArtifactUploadRequest
  property_count: 4
  slug: ausca-com-artifact-upload-request
- name: CancelInvocationResult
  property_count: 0
  slug: ausca-com-cancel-invocation-result
- name: CloseBrowserSessionResult
  property_count: 2
  slug: ausca-com-close-browser-session-result
- name: GetInvocationResult
  property_count: 0
  slug: ausca-com-get-invocation-result
- name: ListAgentInboxMessagesResult
  property_count: 3
  slug: ausca-com-list-agent-inbox-messages-result
- name: SearchOffersResult
  property_count: 3
  slug: ausca-com-search-offers-result
jsonld:
- class_count: 46
  name: Ausca Com Context
  property_count: 85
  slug: ausca-com-context
layout: provider
modified: '2026-11-02'
name: Ausca
nav: Providers
network: true
overview: 'Ausca publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Inboxes API, Analyze Document API, Artifacts API, and 8 more. Tagged areas include Pay-per-call APIs, Agent Infrastructure, Document OCR, Media transcription, and Inbox verification.


  The Ausca catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ausca''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 18 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Ausca API Rules
  rule_count: 53
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 5
  slug: ausca-com-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 62.6
    developer_ergonomics: 30.4
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ausca Com Authentication
  slug: ausca-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ausca Com Domain Security
  slug: ausca-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: ausca-com-process-agent-inbox
  slug: ausca-com-process-agent-inbox
slug: ausca-com
tags:
- Pay-per-call APIs
- Agent Infrastructure
- Document OCR
- Media transcription
- Inbox verification
website: https://ausca.com/
---
