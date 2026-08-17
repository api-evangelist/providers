---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 68.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Fireflies Agentic Access
  operation_count: 1
  slug: fireflies-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 6
apis:
- description: Access AI-generated app outputs for transcripts
  name: Fireflies.ai AI Apps API
  slug: fireflies-ai-apps-api
- description: Upload audio files for transcription
  name: Fireflies.ai Audio Upload API
  slug: fireflies-audio-upload-api
- description: Create and retrieve meeting clips (bites)
  name: Fireflies.ai Bites API
  slug: fireflies-bites-api
- description: Add Fireflies bot to live meetings
  name: Fireflies.ai Live Meetings API
  slug: fireflies-live-meetings-api
- description: Retrieve and manage meeting transcripts and their content
  name: Fireflies.ai Transcripts API
  slug: fireflies-transcripts-api
- description: Query user account information and manage user roles
  name: Fireflies.ai Users API
  slug: fireflies-users-api
artifact_total: 30
asyncapis:
- description: ''
  name: Fireflies Webhooks
  slug: fireflies-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fireflies GraphQL AI Apps API
  slug: open-fireflies-ai-apps-api
- collection_type: open
  name: Fireflies GraphQL AI Apps Audio Upload API
  slug: open-fireflies-audio-upload-api
- collection_type: open
  name: Fireflies GraphQL AI Apps Bites API
  slug: open-fireflies-bites-api
- collection_type: open
  name: Fireflies GraphQL AI Apps Live Meetings API
  slug: open-fireflies-live-meetings-api
- collection_type: open
  name: Fireflies GraphQL AI Apps Transcripts API
  slug: open-fireflies-transcripts-api
- collection_type: open
  name: Fireflies GraphQL AI Apps Users API
  slug: open-fireflies-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fireflies-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fireflies-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fireflies-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fireflies-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fireflies-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://fireflies.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fireflies.ai
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/firefliesai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fireflies-inc/
- group: company
  title: ''
  type: Blog
  url: https://fireflies.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://fireflies.ai/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fireflies.ai/
- group: other
  title: ''
  type: X
  url: https://twitter.com/firefliesai
- group: commercial
  title: ''
  type: Plans
  url: plans/fireflies-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fireflies-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fireflies-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/fireflies-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/fireflies-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: other
  title: ''
  type: AgentCard
  url: a2a/fireflies-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fireflies-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/fireflies-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fireflies-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fireflies-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/fireflies-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fireflies-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fireflies-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fireflies-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fireflies-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fireflies-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.fireflies.ai/getting-started/whats-new
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fireflies-scopes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fireflies-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fireflies-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fireflies.ai/
- group: auth
  title: ''
  type: Security
  url: https://fireflies.ai/bug-bounty
- group: design
  title: ''
  type: DataModel
  url: data-model/fireflies-data-model.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/fireflies-schema.graphql
- group: other
  title: ''
  type: Overlay
  url: overlays/fireflies-ai-apps-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fireflies-audio-upload-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fireflies-bites-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fireflies-live-meetings-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fireflies-transcripts-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fireflies-users-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fireflies.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fireflies.ai/graphql-api/query/transcripts
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fireflies.ai/getting-started/introduction
- group: start
  title: ''
  type: Quickstart
  url: https://docs.fireflies.ai/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://guide.fireflies.ai/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fireflies.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fireflies.ai/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.fireflies.ai/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firefliesai
created: '2026-06-13'
description: Fireflies.ai is an AI meeting assistant that automatically joins video calls, records, transcribes, and summarizes meetings across platforms such as Zoom, Google Meet, and Microsoft Teams. The platform provides a GraphQL API giving developers structured access to call recordings, transcripts, summaries, action items, speaker analytics, and meeting intelligence. Teams can retrieve and search transcript data, manage meetings programmatically, and integrate meeting context into CRM, project management, and workflow automation tools. Advanced features include AskFred AI for natural language queries against meeting content, real-time transcription via a live API, webhooks for event-driven integrations, and an MCP server for connecting AI tooling directly to meeting data.
examples:
- key_count: 4
  name: Fireflies Get Transcript Example
  slug: fireflies-get-transcript-example
- key_count: 4
  name: Fireflies Upload Audio Example
  slug: fireflies-upload-audio-example
finops:
- name: Fireflies Finops
  service_category: ''
  slug: fireflies-finops
graphqls:
- description: 'The Fireflies.ai GraphQL API provides a single endpoint at `https://api.fireflies.ai/graphql` for querying and mutating all meeting intelligence data. The API exposes rich access to transcripts (with '
  name: Fireflies.ai GraphQL API
  slug: fireflies-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fireflies.png
json_schemas:
- name: FirefliesTranscript
  property_count: 17
  slug: fireflies-transcript
jsonld:
- class_count: 15
  name: Fireflies Context
  property_count: 70
  slug: fireflies-context
layout: provider
mcp_servers:
- description: ''
  name: fireflies-mcp.yml
  slug: fireflies-mcpyml
modified: '2026-08-14'
name: Fireflies.ai
nav: Providers
network: true
overview: 'Fireflies.ai publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AI Apps API, Audio Upload API, Bites API, and 3 more. Tagged areas include AI, Meeting Assistant, Transcription, Summaries, and Action Items.


  The Fireflies.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Fireflies.ai''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, API reference, getting-started guide, and 47 more developer resources.'
plans:
- name: Fireflies Plans Pricing
  plan_count: 4
  slug: fireflies-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 0
  name: Fireflies Rate Limits
  slug: fireflies-rate-limits
rules:
- name: Fireflies.ai API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fireflies-jsonschema-spectral-rules
scopes:
- name: Fireflies Scopes
  scope_count: 2
  slug: fireflies-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: exemplar
  composite: 83.2
  delta: 29.6
  facets:
    commercial_clarity: 100.0
    contract_quality: 85.0
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 89.6
    operational_transparency: 55.3
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/fireflies/refs/heads/main/screenshots/fireflies-2026-06-20T181230.png
security:
- kind: authentication
  name: Fireflies Authentication
  slug: fireflies-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Fireflies Domain Security
  slug: fireflies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fireflies Vulnerability Disclosure
  slug: fireflies-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Fireflies Trust Center
  slug: fireflies-trust-center
  summary_line: SOC 2 Type II, HIPAA, GDPR
slug: fireflies
tags:
- AI
- Meeting Assistant
- Transcription
- Summaries
- Action Items
- GraphQL
- Meetings
- Productivity
- Collaboration
- Conversation Intelligence
website: https://fireflies.ai
---
