---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 43
  human_in_the_loop: 3
  name: Screenpipe Agentic Access
  operation_count: 71
  slug: screenpipe-agentic-access
  summary_line: 71 operations · 43 acting · 3 human-in-the-loop
api_count: 18
apis:
- description: Activity summaries and analytics
  name: Screenpipe Activity API
  slug: screenpipe-activity-api
- description: Manage audio recording devices
  name: Screenpipe Audio API
  slug: screenpipe-audio-api
- description: Archive old data to cloud storage
  name: Screenpipe Cloud Archive API
  slug: screenpipe-cloud-archive-api
- description: Sync data across devices via cloud
  name: Screenpipe Cloud Sync API
  slug: screenpipe-cloud-sync-api
- description: Manual data deletion and storage info
  name: Screenpipe Data Management API
  slug: screenpipe-data-management-api
- description: Auto-delete old data locally
  name: Screenpipe Data Retention API
  slug: screenpipe-data-retention-api
- description: Direct database access
  name: Screenpipe Database API
  slug: screenpipe-database-api
- description: Query captured UI accessibility tree data
  name: Screenpipe Elements API
  slug: screenpipe-elements-api
- description: Experimental/unstable endpoints
  name: Screenpipe Experimental API
  slug: screenpipe-experimental-api
- description: Access captured screenshots and their extracted text
  name: Screenpipe Frames API
  slug: screenpipe-frames-api
- description: Detected and manual meeting transcriptions
  name: Screenpipe Meetings API
  slug: screenpipe-meetings-api
- description: AI-extracted knowledge from screen activity
  name: Screenpipe Memories API
  slug: screenpipe-memories-api
- description: Search through captured screen and audio content
  name: Screenpipe Search API
  slug: screenpipe-search-api
- description: Speaker identification and management
  name: Screenpipe Speakers API
  slug: screenpipe-speakers-api
- description: Health checks and system status
  name: Screenpipe System API
  slug: screenpipe-system-api
- description: Tag content items for organization
  name: Screenpipe Tags API
  slug: screenpipe-tags-api
- description: Encrypt/decrypt all data at rest
  name: Screenpipe Vault API
  slug: screenpipe-vault-api
- description: Manage screen capture monitors
  name: Screenpipe Vision API
  slug: screenpipe-vision-api
artifact_total: 24
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/screenpipe-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://screenpipe.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/screenpipe-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/screenpipe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://screenpipe.com/security
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/screenpipe-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.screenpipe.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.screenpipe.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.screenpipe.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.screenpipe.com/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.screenpipe.com/quickstart
- group: company
  title: ''
  type: Website
  url: https://screenpi.pe
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/screenpipe
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.screenpipe.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/screenpipe-changelog.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://screenpipe.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://docs.screenpipe.com/troubleshooting
- group: operate
  title: ''
  type: FAQ
  url: https://docs.screenpipe.com/faq
- group: agent
  title: ''
  type: MCPServer
  url: mcp/screenpipe-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/screenpipe-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/screenpipe-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/screenpipe-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/screenpipe-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/screenpipe-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/screenpipe-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/screenpipe-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/screenpipe-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/screenpipe-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/screenpipe-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/screenpipe-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Screenpipe is a local-first, source-available desktop application (by Mediar AI, Y Combinator S26) that continuously captures everything you see, say, and hear on your computer, reads on-screen text through OS accessibility APIs with an OCR fallback, transcribes system and microphone audio locally with Whisper, and stores it all in a local SQLite database as a private, searchable memory. It exposes a full local REST API at http://localhost:3030 (71 operations across search, frames, audio, meetings, memories, speakers, tags, vault, cloud sync, cloud archive, and data retention) and ships as an MCP server so agents like Claude, Cursor, Codex, and Cline can query screen history and meeting transcripts. Automations are built as "pipes" — scheduled AI agents written in plain markdown. It is positioned as an open, local-first alternative to Rewind.ai, Microsoft Recall, and cloud meeting bots.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/screenpipe.png
layout: provider
mcp_servers:
- description: ''
  name: screenpipe-mcp.yml
  slug: screenpipe-mcpyml
modified: '2026-07-21'
name: Screenpipe
nav: Providers
network: true
overview: 'Screenpipe publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Audio API, Cloud Archive API, and 15 more. Tagged areas include Company, Screen Recording, Screen Memory, Audio Transcription, and Meeting Intelligence.


  Screenpipe''s developer surface includes documentation, API reference, getting-started guide, quickstart, changelog, pricing, support, and 24 more developer resources.'
random_paper: 43
score:
  band: developing
  composite: 44.6
  delta: -0.4
  facets:
    commercial_clarity: 26.3
    contract_quality: 39.1
    developer_ergonomics: 73.4
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Screenpipe Authentication
  slug: screenpipe-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Screenpipe Domain Security
  slug: screenpipe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Screenpipe Vulnerability Disclosure
  slug: screenpipe-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Screenpipe Trust Center
  slug: screenpipe-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: screenpipe
tags:
- Company
- Screen Recording
- Screen Memory
- Audio Transcription
- Meeting Intelligence
- Local First
- Privacy
- AI Agents
- MCP
- Developer Tools
- Productivity
- Open Source
website: https://screenpi.pe
---
