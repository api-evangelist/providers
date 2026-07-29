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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: One REST API to detect AI-generated and manipulated images, audio, and documents — and fact-check media against the public record. Bearer API-token auth with per-key detection scopes (image, audio, fa
  name: Raid AI Detection & Fact-Checking API
  slug: raid-ai-detection-fact-checking-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raid-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://raidxai.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.raidxai.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.raidxai.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.raidxai.com/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.raidxai.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.raidxai.com/docs/support
- group: company
  title: ''
  type: Blog
  url: https://raidxai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://raidxai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.raidxai.com/dashboard
- group: start
  title: ''
  type: Login
  url: https://app.raidxai.com/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://raidxai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://raidxai.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/raid-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/raid-ai-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/raid-ai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/raid-ai-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/raid-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/raid-ai-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/raid-ai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.raidxai.com/docs/versioning
- group: design
  title: ''
  type: Conformance
  url: conformance/raid-ai-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/raid-ai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/104616241/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Raidxai
created: '2026-07-17'
description: Raid AI (RAID AI, Inc.) is an enterprise-grade deepfake and AI-content forensics platform covering audio, image, document, and video. Its REST API detects AI-generated, cloned, deepfaked, and digitally edited media — returning a verdict, a confidence score, and (on detailed plans) generator attribution — across image forensics, voice analysis, document tampering detection, and asynchronous fact-checking against the public record. Audio detection claims 98% accuracy and sub-50ms latency across 100+ languages with specialized Arabic dialect coverage. Raid AI runs a zero-retention pipeline (media analyzed in memory and discarded), offers cloud API plus on-premise air-gapped deployment, and ships native integrations with Microsoft Teams, Zoom, Google Meet, Slack, Webex, and WhatsApp for financial services, call centers, enterprise meetings, and government use cases.
image: https://raidxai.com/raid-ai-icon.png
layout: provider
mcp_servers:
- description: ''
  name: raid-ai-mcp.yml
  slug: raid-ai-mcpyml
modified: '2026-07-20'
name: Raid AI
nav: Providers
network: true
overview: 'Raid AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Deepfake Detection, AI Content Detection, Media Forensics, and Voice / Audio Detection.


  Raid AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 23
scopes:
- name: Raid Ai Scopes
  scope_count: 0
  slug: raid-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.4
  delta: -1.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 56.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 7.9
  previous_composite: 32.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Raid Ai Authentication
  slug: raid-ai-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Raid Ai Domain Security
  slug: raid-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: raid-ai
tags:
- Company
- Deepfake Detection
- AI Content Detection
- Media Forensics
- Voice / Audio Detection
- Image Forensics
- Document Forensics
- Fact-Checking
- Trust & Safety
- Security
website: https://raidxai.com
---
