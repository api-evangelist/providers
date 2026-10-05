---
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 26
  human_in_the_loop: 1
  name: Asapp3 Agentic Access
  operation_count: 56
  slug: asapp3-agentic-access
  summary_line: 56 operations · 26 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.sandbox.asapp.com
  baseurl_source: declared
  description: Improve agent productivity with AutoCompose API
  name: Asapp3 Auto Compose API
  slug: asapp3-autocompose-api
- baseURL: https://api.sandbox.asapp.com
  baseurl_source: declared
  description: Endpoints for summarizing conversations and retrieving structured data
  name: Asapp3 Auto Summary API
  slug: asapp3-autosummary-api
- baseURL: https://api.sandbox.asapp.com
  baseurl_source: declared
  description: Get streaming URL to transcribe audio
  name: Asapp3 Auto Transcribe API
  slug: asapp3-autotranscribe-api
- baseURL: https://api.sandbox.asapp.com
  baseurl_source: declared
  description: Operations for controlling AutoTranscribe Media Gateway transcription and streaming
  name: Asapp3 AutoTranscribe Media Gateway API
  slug: asapp3-autotranscribe-media-gateway-api
- baseURL: https://api.sandbox.asapp.com
  baseurl_source: declared
  description: Operations to send conversational inputs to ASAPP AI services
  name: Asapp3 Conversations API
  slug: asapp3-conversations-api
- baseURL: https://api.sandbox.asapp.com
  baseurl_source: declared
  description: API to get client exports
  name: Asapp3 File Exporter API
  slug: asapp3-file-exporter-api
- baseURL: https://api.sandbox.asapp.com
  baseurl_source: declared
  description: Operations to send messages and trigger GenerativeAgent to respond or query the current state
  name: Asapp3 Generative Agent API
  slug: asapp3-generativeagent-api
- baseURL: https://api.sandbox.asapp.com
  baseurl_source: declared
  description: Operations to ensure that ASAPP APIs are up and running.
  name: Asapp3 Health Check API
  slug: asapp3-health-check-api
- baseURL: https://api.sandbox.asapp.com
  baseurl_source: declared
  description: Operations to submit and retrieve Articles to the GenerativeAgent Knowledge Base.
  name: Asapp3 Knowledge Base API
  slug: asapp3-knowledge-base-api
- baseURL: https://api.sandbox.asapp.com
  baseurl_source: declared
  description: API to submit entity's attributes to ASAPP
  name: Asapp3 Metadata API
  slug: asapp3-metadata-api
artifact_total: 24
asyncapis:
- description: ''
  name: Asapp3 Webhooks
  slug: asapp3-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/capabilities/asapp3-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/asapp3-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/agentic-access/asapp3-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/asapp3-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/rate-limits/asapp3-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/asapp3-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/rules/asapp3-rules.yml
  title: ''
  type: Spectral
  url: rules/asapp3-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/json-ld/asapp3-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/asapp3-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/vocabulary/asapp3-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asapp3-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/asyncapi/asapp3-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/asapp3-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/data-model/asapp3-data-model.yml
  title: ''
  type: DataModel
  url: data-model/asapp3-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.asapp.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/authentication/asapp3-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asapp3-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/errors/asapp3-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/asapp3-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/conformance/asapp3-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asapp3-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/llms/asapp3-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asapp3-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/a2a/asapp3-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/asapp3-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/well-known/asapp3-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/asapp3-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/well-known/asapp3-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asapp3-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/hosts/asapp3-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asapp3-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/vendors/asapp3-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asapp3-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.asapp.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.asapp.com/access/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.asapp.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.asapp.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/asappinc
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.asapp.com/releases/overview
- group: company
  title: ''
  type: Blog
  url: https://www.asapp.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.asapp.com/generativeagent/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.asapp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.asapp.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/security/asapp3-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/asapp3-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asapp3/refs/heads/main/security/asapp3-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asapp3-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.asapp.com
created: '2026-09-26'
description: ASAPP (formerly Asapp3) is a leading AI‑powered customer experience platform for enterprise contact centers. It provides generative AI agents, human‑in‑the‑loop workflows, and real‑time interaction intelligence to automate and augment customer service across voice, digital and human channels. The platform integrates with existing systems, offers safety and security guardrails, and is backed by extensive AI research and patents, serving industries such as finance, healthcare, retail, and telecommunications.
image: https://cdn.prod.website-files.com/6436aca7069acc764910d397/685d7d32c1b63f6563bf2fd7_Primary%20Opengraph.png
json_schemas:
- name: AgentMetadata
  property_count: 22
  slug: asapp3-agent-metadata
- name: Article
  property_count: 14
  slug: asapp3-article
- name: ConversationMetadata
  property_count: 18
  slug: asapp3-conversation-metadata
- name: MessageAnalyticEvent
  property_count: 7
  slug: asapp3-message-analytic-event
- name: MessageSentEvent
  property_count: 13
  slug: asapp3-message-sent-event
- name: SubmissionRequest
  property_count: 7
  slug: asapp3-submission-request
jsonld:
- class_count: 101
  name: Asapp3 Context
  property_count: 178
  slug: asapp3-context
layout: provider
modified: '2026-09-26'
name: Asapp3
nav: Providers
network: true
overview: 'Asapp3 publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Auto Compose API, Auto Summary API, Auto Transcribe API, and 7 more. Tagged areas include Artificial Intelligence, Customer Experience, Enterprise, Contact Center, and Platform.


  The Asapp3 catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Asapp3''s developer surface includes authentication, support, changelog, engineering blog, getting-started guide, documentation, API reference, and 25 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 2
  name: Asapp3 Rate Limits
  slug: asapp3-rate-limits
rules:
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Asapp3 API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 5
  slug: asapp3-rules
score:
  band: strong
  composite: 58.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 35.6
    contract_quality: 71.2
    developer_ergonomics: 49.4
    discoverability: 75.0
    operational_transparency: 65.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 50.0
security:
- kind: authentication
  name: Asapp3 Authentication
  slug: asapp3-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Asapp3 Domain Security
  slug: asapp3-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Asapp3 Trust Center
  slug: asapp3-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
slug: asapp3
tags:
- Artificial Intelligence
- Customer Experience
- Enterprise
- Contact Center
- Platform
- Company
website: https://www.asapp.com
---
