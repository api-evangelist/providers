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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.6
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The standard MediaWiki Action API served at /api.php on every Fandom wiki subdomain (e.g. community.fandom.com, starwars.fandom.com). Provides read/write access via 120 action modules including query,
  name: Fandom MediaWiki Action API
  slug: fandom-mediawiki-action-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.fandom.com/home
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.fandom.com/wiki/Fandom_Developers_Wiki
- group: docs
  title: ''
  type: Documentation
  url: https://community.fandom.com/wiki/Help:API
- group: docs
  title: ''
  type: APIReference
  url: https://www.mediawiki.org/wiki/API:Main_page
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mediawiki.org/wiki/API:Tutorial
- group: operate
  title: ''
  type: Support
  url: https://community.fandom.com/wiki/Community_Central
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Wikia
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fandom.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fandom.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/fandom-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fandom-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fandom-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fandom-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fandom-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fandom-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fandom-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/fandom-packages.yml
created: '2026-07-17'
description: Fandom (formerly Wikia) is the world's largest entertainment fan-wiki platform, hosting hundreds of thousands of community-run wikis covering television, film, games, anime, and pop culture. Every Fandom wiki runs on MediaWiki (currently 1.43.9, PHP 8.3) and exposes the standard MediaWiki Action API at /api.php on each wiki subdomain, giving programmatic read and write access to page content, revisions, full-text and OpenSearch search, media files, templates, and account operations. Fandom layers its own extension modules on top of core MediaWiki (create-new-wiki, theme designer, interactive maps, portable infoboxes, embedded video, notifications). Fandom does not publish a bespoke OpenAPI; the self-documenting api.php help endpoint, the Fandom Developers Wiki (dev.fandom.com), and the upstream MediaWiki API docs are the reference surface. This profile was surfaced as a portfolio company of Bessemer Venture Partners and enriched from Fandom's live, public API.
image: https://images.wikia.com/central/images/b/bc/Wiki.png
layout: provider
mcp_servers:
- description: ''
  name: Fandom MCP Server
  slug: fandom-mcp-server
modified: '2026-07-19'
name: Fandom
nav: Providers
network: true
overview: 'Fandom publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Wiki, MediaWiki, and Media.


  Fandom''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 13 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 24.0
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 24.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fandom/refs/heads/main/screenshots/fandom-2026-07-25T214221.png
security:
- kind: authentication
  name: Fandom Authentication
  slug: fandom-authentication
  summary_line: session/oauth2/oauth1 · 5 schemes
- kind: domain-security
  name: Fandom Domain Security
  slug: fandom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fandom
tags:
- Company
- Consumer
- Wiki
- MediaWiki
- Media
- Entertainment
- Community
- Content
- Fan Community
website: https://www.fandom.com/home
---
