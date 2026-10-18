---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Fellow Agentic Access
  operation_count: 23
  slug: fellow-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 1
apis:
- baseURL: https://{subdomain}.fellow.app/api/v1
  baseurl_source: declared
  description: Access and manage action items from meetings. Retrieve, list, complete, or archive action items with optional filters and pagination.
  name: Fellow Action Items API
  slug: fellow-action-items-api
- baseURL: https://{subdomain}.fellow.app/api/v1
  baseurl_source: declared
  description: Access and manage meeting notes and their agendas. Retrieve individual notes, list notes with filters and pagination, delete notes (privileged access required), or edit agenda content as Fellow Markdo
  name: Fellow Notes API
  slug: fellow-notes-api
- baseURL: https://{subdomain}.fellow.app/api/v1
  baseurl_source: declared
  description: Access and manage meeting recordings. Retrieve individual recordings, list recordings with filters and pagination, or delete recordings (privileged access required).
  name: Fellow Recordings API
  slug: fellow-recordings-api
- baseURL: https://{subdomain}.fellow.app/api/v1
  baseurl_source: declared
  description: Retrieve information about the currently authenticated user and their workspace.
  name: Fellow Users API
  slug: fellow-users-api
- baseURL: https://{subdomain}.fellow.app/api/v1
  baseurl_source: declared
  description: Create and manage webhook endpoints to receive real-time notifications when events occur in your Fellow workspace.
  name: Fellow Webhooks API
  slug: fellow-webhooks-api
artifact_total: 21
asyncapis:
- description: Real-time webhook events delivered by Fellow when meeting AI notes and action items change. Fellow POSTs JSON to a registered HTTPS endpoint. Deliveries are svix-signed (HMAC-SHA256 over `{svix-id}.{s
  name: Fellow Webhooks
  slug: fellow-webhooks-asyncapi
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/agentic-access/fellow-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fellow-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/rules/fellow-rules.yml
  title: ''
  type: Spectral
  url: rules/fellow-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/json-ld/fellow-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fellow-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/vocabulary/fellow-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fellow-vocabulary.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/hosts/fellow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fellow-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/vendors/fellow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fellow-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/packages/fellow-packages.yml
  title: ''
  type: SDKs
  url: packages/fellow-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://fellow.ai/security
- group: company
  title: ''
  type: Newsroom
  url: https://fellow.ai/integrations/media
- group: other
  title: ''
  type: Leadership
  url: https://fellow.ai/meeting-templates/category/leadership
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/plans/fellow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fellow-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/security/fellow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fellow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fellow.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.fellow.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fellow.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.fellow.ai/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.fellow.ai/reference/authentication-1
- group: operate
  title: ''
  type: Support
  url: https://help.fellow.ai/
- group: company
  title: ''
  type: Blog
  url: https://fellow.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fellowapp
- group: commercial
  title: ''
  type: Pricing
  url: https://fellow.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://fellow.app/auth/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fellow.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fellow.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fellow.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.fellow.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://help.fellow.ai/en/articles/4302231-security-and-compliance
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/mcp/fellow-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fellow-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/authentication/fellow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fellow-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/scopes/fellow-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fellow-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/asyncapi/fellow-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/fellow-webhooks-asyncapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/asyncapi/fellow-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/fellow-webhooks-asyncapi.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/rate-limits/fellow-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fellow-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/errors/fellow-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fellow-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/conventions/fellow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fellow-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/lifecycle/fellow-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fellow-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/conformance/fellow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fellow-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/data-model/fellow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fellow-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/llms/fellow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fellow-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/changelog/fellow-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fellow-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/packages/fellow-packages.yml
  title: ''
  type: Packages
  url: packages/fellow-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/well-known/fellow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fellow-well-known.yml
created: '2026-07-17'
description: 'Fellow is an AI meeting assistant and meeting-management platform that records, transcribes, and summarizes meetings, then captures structured notes, action items, and decisions across a team''s calendar. Fellow''s Developer API opens that meeting data through a REST interface: authenticated workspace users generate personal API keys and retrieve recordings, transcripts, notes, and action items, upload recordings, and manage webhook subscriptions for real-time events. Fellow also publishes a hosted, OAuth-secured Model Context Protocol (MCP) server so AI assistants like Claude and ChatGPT can query meeting context in natural language. Backed by Craft Ventures and Felicis. The API requires a paid workspace plan and is governed by workspace admins under Security settings, with a 90-day audit log, SOC 2 Type II, HIPAA BAA availability, and GDPR/CCPA support.'
image: https://framerusercontent.com/assets/J0X2qL3rwf819TDwjCc8iG9UjUk.png
json_schemas:
- name: CreateWebhookRequest
  property_count: 5
  slug: fellow-create-webhook-request
- name: FindReplaceNoteAgendaRequest
  property_count: 2
  slug: fellow-find-replace-note-agenda-request
- name: GetActionItemsRequest
  property_count: 4
  slug: fellow-get-action-items-request
- name: RecordingUploadRequest
  property_count: 6
  slug: fellow-recording-upload-request
- name: UpdateWebhookRequest
  property_count: 4
  slug: fellow-update-webhook-request
- name: WriteNoteAgendaRequest
  property_count: 2
  slug: fellow-write-note-agenda-request
jsonld:
- class_count: 69
  name: Fellow Context
  property_count: 90
  slug: fellow-context
layout: provider
mcp_servers:
- description: Remote MCP server at fellow.app over HTTP; 5 tools listed.
  name: Fellow MCP Server
  slug: fellow
modified: '2026-07-19'
name: Fellow
nav: Providers
network: true
overview: 'Fellow publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Action Items API, Notes API, Recordings API, and 2 more. Tagged areas include Company, Software-as-a-Service, Meetings, Artificial Intelligence, and Meeting Notes.


  The Fellow catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Fellow''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
plans:
- name: Fellow Plans Pricing
  plan_count: 6
  slug: fellow-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Fellow Rate Limits
  slug: fellow-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Fellow API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: fellow-rules
scopes:
- name: Fellow Scopes
  scope_count: 5
  slug: fellow-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: exemplar
  composite: 68.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.6
  facets:
    access_clarity: 84.2
    contract_governance: 35.6
    contract_quality: 70.5
    developer_ergonomics: 47.0
    discoverability: 78.3
    operational_transparency: 73.7
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/fellow/refs/heads/main/screenshots/fellow-2026-07-25T214332.png
security:
- kind: authentication
  name: Fellow Authentication
  slug: fellow-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Fellow Domain Security
  slug: fellow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fellow
tags:
- Company
- Software-as-a-Service
- Meetings
- Artificial Intelligence
- Meeting Notes
- Transcription
- Productivity
- Action Items
- Webhook
- MCP
website: https://fellow.ai
---
