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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Obsidian Agentic Access
  operation_count: 31
  slug: obsidian-agentic-access
  summary_line: 31 operations · 20 acting
api_count: 10
apis:
- description: In-app TypeScript/JavaScript Plugin API for building Obsidian plugins. Plugins access the Vault, Workspace, MetadataCache, file system, command palette, settings, editor, and Markdown post-processing.
  name: Obsidian Plugin API
  slug: obsidian-plugin-api
- description: The Active File API from Obsidian — 1 operation(s) for active file.
  name: Obsidian Active File API
  slug: obsidian-active-file-api
- description: The Commands API from Obsidian — 2 operation(s) for commands.
  name: Obsidian Commands API
  slug: obsidian-commands-api
- description: The Open API from Obsidian — 1 operation(s) for open.
  name: Obsidian Open API
  slug: obsidian-open-api
- description: The Periodic Notes API from Obsidian — 2 operation(s) for periodic notes.
  name: Obsidian Periodic Notes API
  slug: obsidian-periodic-notes-api
- description: The Search API from Obsidian — 2 operation(s) for search.
  name: Obsidian Search API
  slug: obsidian-search-api
- description: The System API from Obsidian — 3 operation(s) for system.
  name: Obsidian System API
  slug: obsidian-system-api
- description: The Tags API from Obsidian — 1 operation(s) for tags.
  name: Obsidian Tags API
  slug: obsidian-tags-api
- description: The Vault Directories API from Obsidian — 2 operation(s) for vault directories.
  name: Obsidian Vault Directories API
  slug: obsidian-vault-directories-api
- description: The Vault Files API from Obsidian — 1 operation(s) for vault files.
  name: Obsidian Vault Files API
  slug: obsidian-vault-files-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/obsidian-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/obsidian-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/obsidian-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/obsidian-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/obsidianmd
- group: company
  title: ''
  type: Website
  url: https://obsidian.md/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.obsidian.md/Home
- group: commercial
  title: ''
  type: Pricing
  url: https://obsidian.md/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/obsidianmd
- group: commercial
  title: ''
  type: Plans
  url: plans/obsidian-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/obsidian-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/obsidian-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.obsidian.md/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://obsidian.md/feed.xml
- group: other
  title: ''
  type: ProductPage
  url: https://obsidian.md/sync
- group: other
  title: ''
  type: ProductPage
  url: https://obsidian.md/publish
created: '2026-05-08'
description: Obsidian is a local-first knowledge base and note-taking app built on plain Markdown files. Obsidian itself does not publish a hosted SaaS API; programmatic access is provided through (1) the in-app Plugin API for community plugins, (2) the community-built Local REST API plugin that exposes vault operations over localhost HTTPS, and (3) optional paid add-on services Obsidian Sync and Obsidian Publish.
finops:
- name: Obsidian Finops
  service_category: Productivity
  slug: obsidian-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/obsidian.png
layout: provider
modified: '2026-07-25'
name: Obsidian
nav: Providers
network: true
overview: 'Obsidian publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Active File API, Commands API, Open API, and 6 more. Tagged areas include Productivity, Knowledge Management, Markdown, Notes, and Local-First.


  Obsidian''s developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 11 more developer resources.'
plans:
- name: Obsidian Plans Pricing
  plan_count: 5
  slug: obsidian-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 4
  name: Obsidian Rate Limits
  slug: obsidian-rate-limits
score:
  band: thin
  composite: 38.3
  delta: -3.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 46.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/obsidian/refs/heads/main/screenshots/obsidian-2026-06-20T190555.png
security:
- kind: authentication
  name: Obsidian Authentication
  slug: obsidian-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Obsidian Domain Security
  slug: obsidian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Obsidian Vulnerability Disclosure
  slug: obsidian-vulnerability-disclosure
  summary_line: disclosure policy published
slug: obsidian
tags:
- Productivity
- Knowledge Management
- Markdown
- Notes
- Local-First
website: https://obsidian.md/
---
