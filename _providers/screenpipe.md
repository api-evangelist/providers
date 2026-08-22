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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.6
  scored_at: '2026-08-19'
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
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Screenpipe Activity API
  slug: open-screenpipe-activity-api
- collection_type: open
  name: Screenpipe Activity Audio API
  slug: open-screenpipe-audio-api
- collection_type: open
  name: Screenpipe Activity Cloud Archive API
  slug: open-screenpipe-cloud-archive-api
- collection_type: open
  name: Screenpipe Activity Cloud Sync API
  slug: open-screenpipe-cloud-sync-api
- collection_type: open
  name: Screenpipe Activity Data Management API
  slug: open-screenpipe-data-management-api
- collection_type: open
  name: Screenpipe Activity Data Retention API
  slug: open-screenpipe-data-retention-api
- collection_type: open
  name: Screenpipe Activity Database API
  slug: open-screenpipe-database-api
- collection_type: open
  name: Screenpipe Activity Elements API
  slug: open-screenpipe-elements-api
- collection_type: open
  name: Screenpipe Activity Experimental API
  slug: open-screenpipe-experimental-api
- collection_type: open
  name: Screenpipe Activity Frames API
  slug: open-screenpipe-frames-api
- collection_type: open
  name: Screenpipe Activity Meetings API
  slug: open-screenpipe-meetings-api
- collection_type: open
  name: Screenpipe Activity Memories API
  slug: open-screenpipe-memories-api
- collection_type: open
  name: Screenpipe Activity Search API
  slug: open-screenpipe-search-api
- collection_type: open
  name: Screenpipe Activity Speakers API
  slug: open-screenpipe-speakers-api
- collection_type: open
  name: Screenpipe Activity System API
  slug: open-screenpipe-system-api
- collection_type: open
  name: Screenpipe Activity Tags API
  slug: open-screenpipe-tags-api
- collection_type: open
  name: Screenpipe Activity Vault API
  slug: open-screenpipe-vault-api
- collection_type: open
  name: Screenpipe Activity Vision API
  slug: open-screenpipe-vision-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/screenpipe-openapi-overlay.yaml
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


  Screenpipe''s developer surface includes documentation, API reference, getting-started guide, quickstart, changelog, pricing, support, and 25 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 43.8
  delta: -0.5
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 16.7
    contract_quality: 41.4
    developer_ergonomics: 70.8
    discoverability: 72.2
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 44.3
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/screenpipe/refs/heads/main/screenshots/screenpipe-2026-08-17T081738.png
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
