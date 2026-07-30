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
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 64.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 13
  name: Opusclip Agentic Access
  operation_count: 22
  slug: opusclip-agentic-access
  summary_line: 22 operations · 13 acting · 13 human-in-the-loop
api_count: 11
apis:
- description: The brand-templates API from OpusClip — 1 operation(s) for brand-templates.
  name: OpusClip brand-templates API
  slug: opusclip-brand-templates-api
- description: The censor-jobs API from OpusClip — 2 operation(s) for censor-jobs.
  name: OpusClip censor-jobs API
  slug: opusclip-censor-jobs-api
- description: The clip-project API from OpusClip — 3 operation(s) for clip-project.
  name: OpusClip clip-project API
  slug: opusclip-clip-project-api
- description: The collection API from OpusClip — 3 operation(s) for collection.
  name: OpusClip collection API
  slug: opusclip-collection-api
- description: The collection-content API from OpusClip — 2 operation(s) for collection-content.
  name: OpusClip collection-content API
  slug: opusclip-collection-content-api
- description: The enterprise API from OpusClip — 18 operation(s) for enterprise.
  name: OpusClip enterprise API
  slug: opusclip-enterprise-api
- description: The exportable-clips API from OpusClip — 1 operation(s) for exportable-clips.
  name: OpusClip exportable-clips API
  slug: opusclip-exportable-clips-api
- description: The ExportableClip API from OpusClip — 1 operation(s) for exportableclip.
  name: OpusClip ExportableClip API
  slug: opusclip-exportableclip-api
- description: The generative-jobs API from OpusClip — 2 operation(s) for generative-jobs.
  name: OpusClip generative-jobs API
  slug: opusclip-generative-jobs-api
- description: The social-posting API from OpusClip — 6 operation(s) for social-posting.
  name: OpusClip social-posting API
  slug: opusclip-social-posting-api
- description: The transcripts API from OpusClip — 1 operation(s) for transcripts.
  name: OpusClip transcripts API
  slug: opusclip-transcripts-api
artifact_total: 18
asyncapis:
- description: ''
  name: Opusclip Webhooks
  slug: opusclip-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.opus.pro/api-reference/overview
- group: docs
  title: ''
  type: Documentation
  url: https://help.opus.pro/api-reference/overview
- group: docs
  title: ''
  type: APIReference
  url: https://help.opus.pro/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://help.opus.pro/api-reference/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.opus.pro/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://opusclip.canny.io/changelog
- group: operate
  title: ''
  type: Roadmap
  url: https://opusclip.canny.io/feature-requests
- group: operate
  title: ''
  type: Support
  url: https://www.opus.pro/contact-support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opus.pro/pricing
- group: start
  title: ''
  type: SignUp
  url: https://clip.opus.pro/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opus.pro/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opus.pro/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opus-pro
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opus.pro
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opusclip-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opusclip-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opusclip-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/opusclip-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opusclip-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opusclip-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/opusclip-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/opusclip-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/opusclip-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/opusclip-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/opusclip-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opusclip-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opusclip-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opusclip-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/opusclip-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/opusclip-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opusclip-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.opus.pro/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opusclip-domain-security.yml
created: '2026-07-17'
description: 'OpusClip (opus.pro), operated by Opusclip Inc. of Mountain View, California, is an AI video platform used by 16M+ creators and businesses. It spans two products: OpusClip, an AI video-clipping tool that turns long-form videos into viral short clips with animated captions, AI reframing, virality scoring, AI B-roll, and multi-platform scheduling; and Agent Opus, an end-to-end AI video agent. OpusClip ships a public REST "Clip API" (https://api.opus.pro) authenticated with Bearer API keys, a hosted MCP server exposing 26 tools, a bundled CLI, a published Agent Skill, webhooks signed with HMAC-SHA256, an OpenAPI 3.0 spec, llms.txt, and security.txt. API access requires an Enterprise, Pro (Beta), or Max plan.'
image: https://avatars.githubusercontent.com/u/94627721?v=4
layout: provider
mcp_servers:
- description: ''
  name: opusclip-mcp.yml
  slug: opusclip-mcpyml
modified: '2026-07-20'
name: OpusClip
nav: Providers
network: true
overview: 'OpusClip publishes 11 APIs on the [APIs.io](https://apis.io/) network, including brand-templates API, censor-jobs API, clip-project API, and 8 more. Tagged areas include Company, Consumer, Video, AI, and Video Editing.


  The OpusClip catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OpusClip''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, support, pricing, and 27 more developer resources.'
random_paper: 59
rate_limits:
- limit_count: 1
  name: Opusclip Rate Limits
  slug: opusclip-rate-limits
score:
  band: strong
  composite: 59.1
  delta: 0.4
  facets:
    commercial_clarity: 44.7
    contract_quality: 56.4
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 81.6
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Opusclip Authentication
  slug: opusclip-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opusclip Domain Security
  slug: opusclip-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Opusclip Vulnerability Disclosure
  slug: opusclip-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: opusclip
tags:
- Company
- Consumer
- Video
- AI
- Video Editing
- Short-Form Video
- Social Media
- Content Creation
- MCP
- Developer API
website: https://help.opus.pro/api-reference/overview
---
