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
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 94
  human_in_the_loop: 1
  name: Popp Agentic Access
  operation_count: 149
  slug: popp-agentic-access
  summary_line: 149 operations · 94 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Agents API from Popp — 1 operation(s) for agents.
  name: Popp Agents API
  slug: popp-agents-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Analysis API from Popp — 6 operation(s) for analysis.
  name: Popp Analysis API
  slug: popp-analysis-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The ATS API from Popp — 3 operation(s) for ats.
  name: Popp ATS API
  slug: popp-ats-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Campaigns API from Popp — 5 operation(s) for campaigns.
  name: Popp Campaigns API
  slug: popp-campaigns-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Candidate Lists API from Popp — 5 operation(s) for candidate lists.
  name: Popp Candidate Lists API
  slug: popp-candidate-lists-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Candidates API from Popp — 12 operation(s) for candidates.
  name: Popp Candidates API
  slug: popp-candidates-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Conversations API from Popp — 6 operation(s) for conversations.
  name: Popp Conversations API
  slug: popp-conversations-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Custom Fields (Beta) API from Popp — 2 operation(s) for custom fields (beta).
  name: Popp Custom Fields (Beta) API
  slug: popp-custom-fields-beta-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Document Credentials API from Popp — 2 operation(s) for document credentials.
  name: Popp Document Credentials API
  slug: popp-document-credentials-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Documents API from Popp — 8 operation(s) for documents.
  name: Popp Documents API
  slug: popp-documents-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Organization Configuration API from Popp — 2 operation(s) for organization configuration.
  name: Popp Organization Configuration API
  slug: popp-organization-configuration-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Organizations API from Popp — 2 operation(s) for organizations.
  name: Popp Organizations API
  slug: popp-organizations-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Scheduling API from Popp — 12 operation(s) for scheduling.
  name: Popp Scheduling API
  slug: popp-scheduling-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Tags API from Popp — 2 operation(s) for tags.
  name: Popp Tags API
  slug: popp-tags-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Templates API from Popp — 1 operation(s) for templates.
  name: Popp Templates API
  slug: popp-templates-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Users API from Popp — 10 operation(s) for users.
  name: Popp Users API
  slug: popp-users-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Webhooks API from Popp — 3 operation(s) for webhooks.
  name: Popp Webhooks API
  slug: popp-webhooks-api
- baseURL: https://api.joinpopp.com/v1
  baseurl_source: declared
  description: The Workflows API from Popp — 20 operation(s) for workflows.
  name: Popp Workflows API
  slug: popp-workflows-api
artifact_total: 31
asyncapis:
- description: ''
  name: Popp Webhooks
  slug: popp-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/agentic-access/popp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/popp-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/rules/popp-rules.yml
  title: ''
  type: Spectral
  url: rules/popp-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/json-ld/popp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/popp-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/vocabulary/popp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/popp-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/well-known/popp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/popp-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/hosts/popp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/popp-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/vendors/popp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/popp-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.joinpopp.com/
- group: company
  title: ''
  type: Website
  url: https://joinpopp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.joinpopp.com/developer/keys
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joinpopp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.joinpopp.com/docs/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.joinpopp.com/docs/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://ai.joinpopp.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joinpopp.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joinpopp.com/privacy-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/mcp/popp-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/popp-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/authentication/popp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/popp-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/asyncapi/popp-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/popp-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/conventions/popp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/popp-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/errors/popp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/popp-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/lifecycle/popp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/popp-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/data-model/popp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/popp-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/conformance/popp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/popp-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/security/popp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/popp-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/llms/popp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/popp-llms.txt
created: '2026-07-17'
description: Popp (Popp AI) is an API-first conversation engine for staffing and recruitment firms. It automates high-volume candidate interactions — screening tens of thousands of applicants, collecting and validating right-to-work and certification documents, running AI candidate analysis, auto-scheduling interviews with calendar sync, and re-qualifying dormant candidate databases — through a drag-and-drop workflow builder and a REST API. The platform exposes conversations, campaigns, documents, analysis, scheduling, and multi-step workflows over https://api.joinpopp.com/v1 with API-key authentication, SHA256-signed webhooks across four event categories, and a published remote MCP server for agent access. Backed by Techstars.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/popp.png
json_schemas:
- name: CreateCampaignRequest
  property_count: 27
  slug: popp-create-campaign-request
- name: CreateMeetingTemplateInput
  property_count: 16
  slug: popp-create-meeting-template-input
- name: CreateSchedulingConversationInput
  property_count: 12
  slug: popp-create-scheduling-conversation-input
- name: ListAtsJobsResponse
  property_count: 2
  slug: popp-list-ats-jobs-response
- name: List Campaigns Response
  property_count: 2
  slug: popp-list-campaigns-response
- name: UpdateMeetingTemplateInput
  property_count: 16
  slug: popp-update-meeting-template-input
jsonld:
- class_count: 120
  name: Popp Context
  property_count: 216
  slug: popp-context
layout: provider
mcp_servers:
- description: Popp AI hosts a remote MCP server that lets AI code editors (Cursor, Windsurf) and general-purpose agents (Claude Desktop) interact directly with the Popp API and documentation. Provides direct API ac
  name: Popp MCP Server
  slug: popp-api
modified: '2026-07-20'
name: Popp
nav: Providers
network: true
overview: 'Popp publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Analysis API, ATS API, and 15 more. Tagged areas include Company, Recruiting, Staffing, Hiring, and Conversational AI.


  The Popp catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Popp''s developer surface includes support, documentation, API reference, getting-started guide, signup flow, authentication, and 20 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Popp API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: popp-rules
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.4
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 73.7
    developer_ergonomics: 31.0
    discoverability: 71.7
    operational_transparency: 7.9
  previous_composite: 29.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 18
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 77.8
screenshot: https://raw.githubusercontent.com/api-evangelist/popp/refs/heads/main/screenshots/popp-2026-09-02T151750.png
security:
- kind: authentication
  name: Popp Authentication
  slug: popp-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Popp Domain Security
  slug: popp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: popp
tags:
- Company
- Recruiting
- Staffing
- Hiring
- Conversational AI
- Automation
- Scheduling
- Workflows
- Webhook
- MCP
- Agents
website: https://joinpopp.com/
---
