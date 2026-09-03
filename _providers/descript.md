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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Descript Agentic Access
  operation_count: 11
  slug: descript-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 1
apis:
- baseURL: https://descriptapi.com/v1
  baseurl_source: declared
  description: Import media, edit projects with AI, and query jobs and projects.
  name: Descript API Endpoints API
  slug: descript-api-endpoints-api
- baseURL: https://descriptapi.com/v1
  baseurl_source: declared
  description: '> **Note:** The Edit in Descript integration requires contacting Descript for access. [Reach out to us](https://descript.com/api) to get started. Edit in Descript API enables partners to give their us'
  name: Descript Edit in Descript API
  slug: descript-edit-in-descript-api
- baseURL: https://descriptapi.com/v1
  baseurl_source: declared
  description: Users of Descript currently have three options to export their edited content. They can export files in various formats, share a Descript link, or use our [one-click cloud export](https://help.descrip
  name: Descript Export from Descript API
  slug: descript-export-from-descript-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Descript API Endpoints API
  slug: open-descript-api-endpoints-api
- collection_type: open
  name: Descript API Endpoints Edit in Descript API
  slug: open-descript-edit-in-descript-api
- collection_type: open
  name: Descript API Endpoints Export from Descript API
  slug: open-descript-export-from-descript-api
- collection_type: open
  name: Descript API
  slug: open-descript
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/descript-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/descript-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/descript-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/descript-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/descript-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/descript-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/descript
- group: start
  title: ''
  type: Portal
  url: https://www.descript.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.descriptapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.descriptapi.com/openapi-experimental.html
- group: start
  title: ''
  type: Signup
  url: https://web.descript.com/signup
- group: start
  title: ''
  type: Login
  url: https://web.descript.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.descript.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/descript-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/descript-rate-limits.yml
- group: other
  title: FinOps Framework Profile
  type: Resources
  url: finops/descript-finops.yml
- group: build
  title: ''
  type: CLI
  url: https://www.npmjs.com/package/@descript/platform-cli
- group: operate
  title: ''
  type: Support
  url: https://help.descript.com/
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://help.descript.com/
- group: company
  title: ''
  type: Blog
  url: https://www.descript.com/blog
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@descriptapp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.descript.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.descript.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.descript.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/descriptinc
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-06'
description: Descript is an AI-powered video and audio editing platform. Descript's API lets you programmatically create projects, import media, run AI ("Underlord") edits, publish compositions, and export transcripts — all without opening the desktop app. The API surfaces the same job model that backs the desktop editor and is currently in early access.
features:
- description: Create new projects in a Drive and import media from public or pre-signed URLs in a single API request.
  name: Project Creation
- description: Receive 3-hour signed upload URLs from the import endpoint and PUT media bytes directly to storage.
  name: Direct File Upload
- description: Send natural-language prompts to the Underlord agent to apply Studio Sound, captions, filler-word removal, translation, dubbing, and rough-cut building.
  name: AI Agent Editing
- description: All long-running operations return a job_id; clients poll GET /v1/jobs/{job_id} or supply a callback_url for webhook delivery.
  name: Asynchronous Jobs
- description: Publish compositions to public, unlisted, drive, or private access levels with configurable resolution (480p–4K) for video.
  name: Composition Publishing
- description: Export composition transcripts in txt, markdown, html, rtf, or docx with configurable speaker labels, markers, and timecodes.
  name: Transcript Export
- description: Automatically transcribe imported media in 25 languages with multi-speaker detection on paid plans.
  name: Multi-Language Transcription
- description: Generate one-time import URLs for partner integrations so users can hand off media into Descript with a single click.
  name: Edit-in-Descript Partner Flow
- description: Retrieve metadata (download URL, privacy, subtitles in WebVTT) for published projects via a public slug endpoint.
  name: Published Project Metadata
- description: 429 responses include Retry-After, X-RateLimit-Remaining, and X-RateLimit-Consumed for client-side budgeting.
  name: Rate-Limit Headers
finops:
- name: Descript Finops
  service_category: Media Editing
  slug: descript-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/descript.png
layout: provider
modified: '2026-05-19'
name: Descript
nav: Providers
network: true
overview: 'Descript publishes 3 APIs on the [APIs.io](https://apis.io/) network: API Endpoints API, Edit in Descript API, and Export from Descript API. Tagged areas include Artificial Intelligence, Audio Editing, Captions, Media, and Podcasting.


  Descript''s developer surface includes authentication, developer portal, documentation, API reference, signup flow, pricing, CLI, and 18 more developer resources.'
plans:
- name: Descript Plans Pricing
  plan_count: 5
  slug: descript-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Descript Rate Limits
  slug: descript-rate-limits
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 52.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/descript/refs/heads/main/screenshots/descript-2026-06-20T175933.png
security:
- kind: authentication
  name: Descript Authentication
  slug: descript-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Descript Domain Security
  slug: descript-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Descript Vulnerability Disclosure
  slug: descript-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Descript Trust Center
  slug: descript-trust-center
  summary_line: SOC 2, GDPR
slug: descript
tags:
- Artificial Intelligence
- Audio Editing
- Captions
- Media
- Podcasting
- Transcription
- Video Editing
use_cases:
- description: Import recordings, run Studio Sound and filler-word removal, and publish episodes without opening the desktop app.
  name: Podcast Production Automation
- description: Programmatically caption a backlog of videos in 25 languages and export captions for downstream platforms.
  name: Bulk Video Captioning
- description: Send raw multitrack recordings to the agent with a prompt like "build a rough cut" and retrieve a near-finished timeline.
  name: AI-Driven Rough Cuts
- description: Translate and dub video content into 30+ languages with proofread review using the Business plan's translation pipeline.
  name: Translation and Dubbing
- description: Generate clips, social cuts, and shorts from long-form recordings using Underlord prompts.
  name: Content Repurposing
- description: Use the Edit-in-Descript partner endpoint to embed Descript editing into third-party recording tools (Ecamm, Restream, SquadCast, Zoom, Captivate).
  name: Embedded Video Workflows
website: https://www.descript.com/api
---
