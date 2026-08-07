---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Madhive Agentic Access
  operation_count: 78
  slug: madhive-agentic-access
  summary_line: 78 operations · 49 acting
api_count: 2
apis:
- description: 'The Madhive Public API is a REST interface for digital advertising clients and services, fronted by Apigee and authenticated with OAuth 2.0 client credentials. It covers the full campaign lifecycle — '
  name: Madhive API
  slug: madhive-api
- description: The Madhive MCP API is a hosted Model Context Protocol server that exposes Madhive campaign management to AI assistants over JSON-RPC 2.0, authenticated with OAuth 2.0 via Apigee. It supports both mac
  name: Madhive MCP API
  slug: madhive-mcp
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/madhive-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/madhive-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/madhive-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/madhive-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.madhive.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.madhive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.madhive.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.madhive.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.madhive.com/get-started
- group: start
  title: ''
  type: SignUp
  url: https://developer.madhive.com/login
- group: operate
  title: ''
  type: FAQ
  url: https://developer.madhive.com/faq
- group: operate
  title: ''
  type: StatusPage
  url: https://madhive.checkly-status-page.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.madhive.com/scheduled-updates
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.madhive.com/files/API_Terms_of_Use_Nov_21.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.madhive.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.madhive.com/insights
- group: company
  title: ''
  type: NewsRoom
  url: https://www.madhive.com/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MadHive
- group: auth
  title: ''
  type: Compliance
  url: https://www.madhive.com/insights/madhive-renews-soc-1-2-and-3
- group: operate
  title: ''
  type: Support
  url: https://developer.madhive.com/faq
- group: company
  title: ''
  type: Careers
  url: https://www.madhive.com/careers
- group: company
  title: ''
  type: About
  url: https://www.madhive.com/about-us
- group: agent
  title: ''
  type: WellKnown
  url: well-known/madhive-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/madhive-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/madhive-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/madhive-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/madhive-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.madhive.com/scheduled-updates
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/madhive-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/madhive-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/madhive-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/madhive-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/madhive-examples.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/madhive-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/madhive-mcp-overlay.yaml
created: '2026-08-04'
description: Madhive is a New York-based advertising technology company that operates a demand-side platform (DSP) and end-to-end software stack built for local and connected TV (CTV/OTT) advertising. Broadcasters, local media sellers, agencies and political advertisers use Madhive to plan campaigns, activate premium streaming and broadcast inventory, build cookieless audiences from first-party and offline data, manage creatives, and measure outcomes from a single unified DSP. Madhive publishes a public developer program at developer.madhive.com — an Apigee-fronted REST API covering campaigns, line items, advertisers, agencies, creatives, audiences, segments, retargeting, publishers, publisher groups, tracking pixels, products, metros and optimization templates — alongside a hosted Model Context Protocol (MCP) server that exposes the same campaign-management surface to AI assistants such as Claude and Gemini over JSON-RPC 2.0 with OAuth 2.0.
image: https://cdn.prod.website-files.com/66f4642913b966635efd9666/675750501cfd31ca8779c1a9_og%20image.jpg
layout: provider
mcp_servers:
- description: ''
  name: madhive-mcp.yml
  slug: madhive-mcpyml
modified: '2026-08-04'
name: MadHive
nav: Providers
network: true
overview: 'MadHive publishes 2 APIs on the [APIs.io](https://apis.io/) network, including MCP API, and 1 more. Tagged areas include Company, Advertising, AdTech, Connected TV, and CTV.


  MadHive''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, FAQ, changelog, and 29 more developer resources.'
random_paper: 56
rate_limits:
- limit_count: 5
  name: Madhive Rate Limits
  slug: madhive-rate-limits
scopes:
- name: Madhive Scopes
  scope_count: 0
  slug: madhive-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.1
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 59.6
    developer_ergonomics: 53.8
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 76.3
  previous_composite: 54.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Madhive Authentication
  slug: madhive-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Madhive Domain Security
  slug: madhive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: madhive
tags:
- Company
- Advertising
- AdTech
- Connected TV
- CTV
- OTT
- Demand-Side Platform
- Programmatic Advertising
- Media
- Marketing
- Audiences
- Campaign Management
- Model Context Protocol
website: https://www.madhive.com/
---
