---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.4
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: REST API over api.feedly.com/v3 for the Feedly Threat Intelligence platform. Collect articles from AI Feeds, Folders and Boards by streamId; search and query the corpus with the Ask AI (RAG) endpoints
  name: Feedly API
  slug: feedly-api
- description: Hosted, remote Model Context Protocol server exposing the Feedly Real-Time Threat Graph to AI agents. Feedly documents 16 tools covering threat actors, malware, vulnerabilities, TTPs, IoCs and cyberat
  name: Feedly Threat Graph MCP Server
  slug: feedly-threat-graph-mcp-server
artifact_total: 27
asyncapis:
- description: ''
  name: Feedly Webhooks
  slug: feedly-webhooks
collections:
- collection_type: open
  name: Feedly API
  slug: open-feedly-agents
- collection_type: open
  name: Alerts API
  slug: open-feedly-alerts
- collection_type: open
  name: Annotations API
  slug: open-feedly-annotations
- collection_type: open
  name: Enterprise Collections
  slug: open-feedly-enterprise-collections
- collection_type: open
  name: Enterprise Users API
  slug: open-feedly-enterprise-users
- collection_type: open
  name: Enterprise API
  slug: open-feedly-enterprise
- collection_type: open
  name: Entities API
  slug: open-feedly-entities
- collection_type: open
  name: Entries
  slug: open-feedly-entries
- collection_type: open
  name: Get Intel Profiles
  slug: open-feedly-intel-profiles
- collection_type: open
  name: IoCs
  slug: open-feedly-iocs
- collection_type: open
  name: Memes API
  slug: open-feedly-memes
- collection_type: open
  name: ML Endpoint
  slug: open-feedly-ml
- collection_type: open
  name: Search API
  slug: open-feedly-search
- collection_type: open
  name: Streams API
  slug: open-feedly-streams
- collection_type: open
  name: Tags API
  slug: open-feedly-tags
- collection_type: open
  name: TI Endpoints
  slug: open-feedly-ti-endpoints
- collection_type: open
  name: Trends API
  slug: open-feedly-trends
- collection_type: open
  name: Feedly Vulnerability Agent API
  slug: open-feedly-vulnerability-agent
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/feedly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/feedly-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://feedly.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.feedly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.feedly.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.feedly.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.feedly.com/reference/building-your-first-ti-integration
- group: operate
  title: ''
  type: Support
  url: https://docs.feedly.com/
- group: company
  title: ''
  type: Blog
  url: https://feedly.com/new-features
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/feedly
- group: commercial
  title: ''
  type: Pricing
  url: https://feedly.com/threat-intelligence/pricing
- group: start
  title: ''
  type: SignUp
  url: https://feedly.com/i/team/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://feedly.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://feedly.com/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.feedly.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.feedly.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/feedly-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/feedly-api-catalog.json
- group: build
  title: ''
  type: Packages
  url: packages/feedly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/feedly-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/feedly-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/feedly-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.feedly.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/feedly-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/feedly-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/feedly-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://feedly.com/legal/security
- group: design
  title: ''
  type: Conventions
  url: conventions/feedly-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/feedly-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.feedly.com/changelog/
- group: design
  title: ''
  type: DataModel
  url: data-model/feedly-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/feedly-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/feedly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/feedly-rate-limits.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/feedly-trust-center.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-streams-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-search-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-entries-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-entities-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-ml-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-trends-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-enterprise-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-enterprise-users-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-enterprise-collections-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-intel-profiles-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-iocs-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-ti-endpoints-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-agents-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-alerts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-annotations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-tags-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-memes-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/feedly-vulnerability-agent-overlay.yaml
created: '2026-08-12'
description: Feedly is a content aggregation and threat intelligence platform that reads millions of open sources and turns them into structured, machine-readable intelligence. Its consumer product is a feed reader built on RSS/Atom; its commercial product, Feedly Threat Intelligence, applies a family of AI models ("Leo") to build a Real-Time Threat Graph covering threat actors, malware families, CVEs, indicators of compromise, MITRE ATT&CK techniques, and cyberattacks. The Feedly API is a REST API over api.feedly.com/v3 that exposes those objects to security teams for SOAR/SIEM automation — collecting articles from AI Feeds, Folders and Boards, searching and asking questions of the corpus with LLMs, pulling CVE/malware/threat-actor insight cards and their relationships, exporting IoCs with context, and registering webhooks for saved-article and annotation events. Feedly also operates a hosted, OAuth-protected Model Context Protocol server over its Threat Graph, and publishes an open-source
  library of CTI Agent Skills and prompts for Claude.
image: https://feedly.com/favicon.ico
layout: provider
mcp_servers:
- description: 'Feedly operates a hosted, remote Model Context Protocol server over its Real-Time Threat Graph, marketed as the "Threat Graph MCP Server" and bundled with the Advanced Threat Intelligence plan. It is '
  name: Feedly MCP Server
  slug: feedly-mcp-server
modified: '2026-08-12'
name: Feedly
nav: Providers
network: true
overview: 'Feedly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Threat Intelligence, Cybersecurity, cyber-threat-intelligence, Content Aggregation, and RSS.


  The Feedly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Feedly''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 47 more developer resources.'
plans:
- name: Feedly Plans Pricing
  plan_count: 2
  slug: feedly-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Feedly Rate Limits
  slug: feedly-rate-limits
score:
  band: strong
  composite: 58.0
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 30.3
    contract_quality: 62.2
    developer_ergonomics: 51.2
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 47.4
  previous_composite: 58.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/feedly/refs/heads/main/screenshots/feedly-2026-08-17T080410.png
security:
- kind: authentication
  name: Feedly Authentication
  slug: feedly-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Feedly Domain Security
  slug: feedly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Feedly Trust Center
  slug: feedly-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2
slug: feedly
tags:
- Threat Intelligence
- Cybersecurity
- cyber-threat-intelligence
- Content Aggregation
- RSS
- News
- Vulnerability Management
- Indicators of Compromise
- Malware
- threat-actors
- mitre-attack
- Security Automation
- Artificial Intelligence
- MCP
- agent-native
- Webhook
website: https://feedly.com/
---
