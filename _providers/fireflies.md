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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
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
artifact_total: 20
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
modified: '2026-06-13'
name: Fireflies.ai
nav: Providers
network: true
overview: 'Fireflies.ai publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AI Apps API, Audio Upload API, Bites API, and 3 more. Tagged areas include AI, Meeting Assistant, Transcription, Summaries, and Action Items.


  The Fireflies.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fireflies.ai''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Fireflies Plans Pricing
  plan_count: 4
  slug: fireflies-plans-pricing
random_paper: 25
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
score:
  band: developing
  composite: 54.3
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 79.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fireflies/refs/heads/main/screenshots/fireflies-2026-06-20T181230.png
security:
- kind: authentication
  name: Fireflies Authentication
  slug: fireflies-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fireflies Domain Security
  slug: fireflies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fireflies Vulnerability Disclosure
  slug: fireflies-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Fireflies Trust Center
  slug: fireflies-trust-center
  summary_line: SOC 2, HIPAA, GDPR
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
