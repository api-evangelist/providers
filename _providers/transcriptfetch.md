---
api_count: 1
apis:
- baseURL: https://transcriptfetch.com
  baseurl_source: declared
  description: REST API (current version v2, path-prefixed) for fetching timestamped transcripts from YouTube, TikTok, Instagram, Spotify, Apple Podcasts, podcast RSS feeds, and direct media files, with AI audio tra
  name: TranscriptFetch REST API
  slug: transcriptfetch-rest-api
artifact_total: 11
asyncapis:
- description: ''
  name: Transcriptfetch Webhooks
  slug: transcriptfetch-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://transcriptfetch.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/transcriptfetch-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/transcriptfetch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transcriptfetch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transcriptfetch-authentication.yml
- group: auth
  title: ''
  type: Security
  url: security/transcriptfetch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/transcriptfetch-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/transcriptfetch-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/transcriptfetch-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/transcriptfetch-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/transcriptfetch-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/transcriptfetch-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/transcriptfetch-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.transcriptfetch.com
- group: operate
  title: ''
  type: Deprecation
  url: https://transcriptfetch.com/docs/v1
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/transcriptfetch-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/transcriptfetch-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/transcriptfetch-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://transcriptfetch.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/transcriptfetch-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/transcriptfetch-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/transcriptfetch-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/transcriptfetch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/transcriptfetch-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://transcriptfetch.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://transcriptfetch.com/blog
- group: operate
  title: ''
  type: Support
  url: https://transcriptfetch.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://transcriptfetch.com/help
- group: operate
  title: ''
  type: Roadmap
  url: https://transcriptfetch.com/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transcriptfetch.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://transcriptfetch.com/legal
- group: start
  title: ''
  type: SignUp
  url: https://transcriptfetch.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://transcriptfetch.com/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TranscriptFetch
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/transcriptfetch
- group: start
  title: ''
  type: GettingStarted
  url: https://transcriptfetch.com/docs
created: '2026-09-09'
description: Social video & audio to text API for builders. Returns timestamped, structured JSON transcripts for YouTube, TikTok, Instagram, Spotify, Apple Podcasts, and direct media files — captions when available, AI audio transcription as fallback — plus YouTube channel/playlist/search discovery. Delivered via REST and a hosted MCP server for LLM pipelines, RAG, and agents.
layout: provider
mcp_servers:
- description: ''
  name: TranscriptFetch MCP Server
  slug: transcriptfetch-mcp-server
- description: ''
  name: TranscriptFetch MCP Server
  slug: transcriptfetch-mcp-server-2
modified: '2026-09-09'
name: TranscriptFetch
nav: Providers
network: true
overview: 'TranscriptFetch publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include transcripts, speech-to-text, captions, youtube, and tiktok.


  The TranscriptFetch catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TranscriptFetch''s developer surface includes authentication, changelog, pricing, engineering blog, support, signup flow, getting-started guide, and 30 more developer resources.'
plans:
- name: Transcriptfetch Plans Pricing
  plan_count: 6
  slug: transcriptfetch-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Transcriptfetch Rate Limits
  slug: transcriptfetch-rate-limits
scopes:
- name: Transcriptfetch Scopes
  scope_count: 0
  slug: transcriptfetch-scopes
  summary_line: OAuth 2.0 · no documented scopes
security:
- kind: authentication
  name: Transcriptfetch Authentication
  slug: transcriptfetch-authentication
  summary_line: http/oauth2 (MCP surface) · 2 schemes
- kind: domain-security
  name: Transcriptfetch Domain Security
  slug: transcriptfetch-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Transcriptfetch Vulnerability Disclosure
  slug: transcriptfetch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Transcriptfetch Trust Center
  slug: transcriptfetch-trust-center
  summary_line: trust center published
slug: transcriptfetch
tags:
- transcripts
- speech-to-text
- captions
- youtube
- tiktok
- instagram
- podcasts
- mcp
- llms-txt
- openapi
- Transcription
- Speech-to-Text
- Video
- Podcasts
- AI/LLM
- RAG
- Agents
- MCP
- Developer Tools
- Media
- Content
- YouTube
- TikTok
- Instagram
- Spotify
- Apple Podcasts
website: https://transcriptfetch.com
---
