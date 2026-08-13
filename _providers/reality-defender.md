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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Asynchronous REST API for deepfake and manipulated-media detection. Request a pre-signed upload URL or submit a social-media URL, then poll for an ensemble detection verdict across image, video, audio
  name: Reality Defender Detection API
  slug: reality-defender-detection-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reality-defender-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.realitydefender.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.realitydefender.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.realitydefender.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.realitydefender.com/api-reference/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.realitydefender.com/sdks/quickstart
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/reality-defender/en/
- group: company
  title: ''
  type: Blog
  url: https://www.realitydefender.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Reality-Defender
- group: start
  title: ''
  type: SignUp
  url: https://app.realitydefender.ai/
- group: start
  title: ''
  type: Login
  url: https://auth.app.realitydefender.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.realitydefender.com/t-c/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.realitydefender.com/terms
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.realitydefender.com/
- group: build
  title: ''
  type: Packages
  url: packages/reality-defender-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reality-defender-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reality-defender-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reality-defender-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reality-defender-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reality-defender-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reality-defender-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reality-defender-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reality-defender-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reality-defender-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reality-defender-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Reality Defender is an enterprise deepfake and AI-generated media detection platform that identifies manipulated images, video, audio, and text across calls, meetings, onboarding, and access workflows in real time. Its detection API accepts uploaded media or social-media URLs and returns an ensemble verdict aggregating multiple purpose-built detection models, letting platforms, financial institutions, and governments block deepfakes before they authorize payments, spread disinformation, or deceive AI agents. Reality Defender ships official SDKs for TypeScript, Python, Go, Rust, and Java, an open-source MCP server for agent integrations, and a Slack app. It was surfaced as a portfolio company of DCVC.
image: https://www.datocms-assets.com/157377/1744045826-og-image.jpg?auto=format&fit=max&w=1200
layout: provider
mcp_servers:
- description: ''
  name: reality-defender-mcp.yml
  slug: reality-defender-mcpyml
modified: '2026-07-20'
name: Reality Defender
nav: Providers
network: true
overview: 'Reality Defender publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Deepfake Detection, Artificial Intelligence, Media Authentication, and Content Moderation.


  Reality Defender''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 19 more developer resources.'
random_paper: 76
score:
  band: thin
  composite: 32.0
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 32.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Reality Defender Authentication
  slug: reality-defender-authentication
  summary_line: apiKey/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Reality Defender Domain Security
  slug: reality-defender-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reality-defender
tags:
- Company
- Deepfake Detection
- Artificial Intelligence
- Media Authentication
- Content Moderation
- Security
- Fraud Prevention
- Synthetic Media
- Machine Learning
website: https://www.realitydefender.com
---
