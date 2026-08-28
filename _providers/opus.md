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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 13
  human_in_the_loop: 13
  name: Opus Agentic Access
  operation_count: 22
  slug: opus-agentic-access
  summary_line: 22 operations · 13 acting · 13 human-in-the-loop
api_count: 11
apis:
- description: The brand-templates API from Opus — 1 operation(s) for brand-templates.
  name: Opus brand-templates API
  slug: opus-brand-templates-api
- description: The censor-jobs API from Opus — 2 operation(s) for censor-jobs.
  name: Opus censor-jobs API
  slug: opus-censor-jobs-api
- description: The clip-project API from Opus — 3 operation(s) for clip-project.
  name: Opus clip-project API
  slug: opus-clip-project-api
- description: The collection API from Opus — 3 operation(s) for collection.
  name: Opus collection API
  slug: opus-collection-api
- description: The collection-content API from Opus — 2 operation(s) for collection-content.
  name: Opus collection-content API
  slug: opus-collection-content-api
- description: The enterprise API from Opus — 18 operation(s) for enterprise.
  name: Opus enterprise API
  slug: opus-enterprise-api
- description: The exportable-clips API from Opus — 1 operation(s) for exportable-clips.
  name: Opus exportable-clips API
  slug: opus-exportable-clips-api
- description: The ExportableClip API from Opus — 1 operation(s) for exportableclip.
  name: Opus ExportableClip API
  slug: opus-exportableclip-api
- description: The generative-jobs API from Opus — 2 operation(s) for generative-jobs.
  name: Opus generative-jobs API
  slug: opus-generative-jobs-api
- description: The social-posting API from Opus — 6 operation(s) for social-posting.
  name: Opus social-posting API
  slug: opus-social-posting-api
- description: The transcripts API from Opus — 1 operation(s) for transcripts.
  name: Opus transcripts API
  slug: opus-transcripts-api
arazzos:
- description: Submit a long-form video, wait for clipping, list clips, and export a collection.
  name: OpusClip — clip a video and export clips
  slug: opus-clip-and-export
- description: Clip a video, generate social copy, and publish a clip to a connected social account.
  name: OpusClip — clip a video and publish to social
  slug: opus-clip-and-publish
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clip brand-templates API
  slug: open-opus-brand-templates-api
- collection_type: open
  name: Clip brand-templates censor-jobs API
  slug: open-opus-censor-jobs-api
- collection_type: open
  name: Clip brand-templates clip-project API
  slug: open-opus-clip-project-api
- collection_type: open
  name: Clip brand-templates collection API
  slug: open-opus-collection-api
- collection_type: open
  name: Clip brand-templates collection-content API
  slug: open-opus-collection-content-api
- collection_type: open
  name: Clip brand-templates enterprise API
  slug: open-opus-enterprise-api
- collection_type: open
  name: Clip brand-templates exportable-clips API
  slug: open-opus-exportable-clips-api
- collection_type: open
  name: Clip brand-templates ExportableClip API
  slug: open-opus-exportableclip-api
- collection_type: open
  name: Clip brand-templates generative-jobs API
  slug: open-opus-generative-jobs-api
- collection_type: open
  name: Clip brand-templates social-posting API
  slug: open-opus-social-posting-api
- collection_type: open
  name: Clip brand-templates transcripts API
  slug: open-opus-transcripts-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/opus-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opus-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/opus-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/opus-security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://trust.opus.pro/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opus-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: https://help.opus.pro/api-reference/webhook
- group: company
  title: ''
  type: Website
  url: https://www.opus.pro/
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
- group: operate
  title: ''
  type: Support
  url: https://www.opus.pro/contact-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.opus.pro/
- group: company
  title: ''
  type: Blog
  url: https://www.opus.pro/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opus-pro
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opus.pro/pricing
- group: start
  title: ''
  type: SignUp
  url: https://clip.opus.pro/dashboard
- group: start
  title: ''
  type: Login
  url: https://clip.opus.pro/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opus.pro/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opus.pro/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opus.pro
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opus-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opus-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/opus-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/opus-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/opus-security.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/opus-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opus-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opus-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/opus-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/opus-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/opus-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/opus-conventions.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/opus-clip-and-export.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/opus-clip-and-publish.yml
- group: other
  title: ''
  type: AICatalog
  url: ai-catalog/opus-ai-catalog.yml
created: '2026-07-17'
description: OpusClip (Opus) is an AI video platform that turns long-form videos into short-form, viral clips and publishes them to social platforms. The OpusClip API lets developers submit a source video by URL or upload, create a clipping project, tune curation/import/render preferences, apply brand templates, retrieve exportable clips and transcripts, organize clips into collections, run censor and generative thumbnail jobs, and generate, publish, or schedule social posts to connected accounts. The API is REST over JSON at https://api.opus.pro, authenticated with a bearer API key, with HMAC-signed webhooks, page-based pagination, and a hosted MCP server plus an Agent Skill for agent-native access. API access is available on the Pro (Beta), Max, and Business plans.
image: https://cdn.prod.website-files.com/6388604483b03a9ecb34d695/6435197bfb1d6e486e04c37b_webclip.png
layout: provider
mcp_servers:
- description: ''
  name: Opus MCP Server
  slug: opus-mcp-server
modified: '2026-07-20'
name: Opus
nav: Providers
network: true
overview: 'Opus publishes 11 APIs on the [APIs.io](https://apis.io/) network, including brand-templates API, censor-jobs API, clip-project API, and 8 more. Tagged areas include Company, Frontier Tech, Video, Artificial Intelligence, and Video Editing.


  Opus'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 49.3
  delta: 2.4
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 16.7
    contract_quality: 46.1
    developer_ergonomics: 66.1
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 21.1
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opus/refs/heads/main/screenshots/opus-2026-08-07T190821.png
security:
- kind: authentication
  name: Opus Authentication
  slug: opus-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opus Domain Security
  slug: opus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Opus Vulnerability Disclosure
  slug: opus-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Opus Trust Center
  slug: opus-trust-center
  summary_line: SOC 2, GDPR
slug: opus
tags:
- Company
- Frontier Tech
- Video
- Artificial Intelligence
- Video Editing
- Short-Form Video
- Content Creation
- Social-Media
- Media
- Agents
website: https://www.opus.pro/
---
