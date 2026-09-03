---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 17.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Backend API for the hosted Intlayer CMS at back.intlayer.org — dictionaries, projects, organizations, environments and tags. Secured with OAuth 2.0 client_credentials (per-project access keys issued a
  name: Intlayer CMS API
  slug: intlayer-cms-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://intlayer.org
- group: docs
  title: ''
  type: Documentation
  url: https://intlayer.org/doc/
- group: start
  title: ''
  type: GettingStarted
  url: https://intlayer.org/doc/get-started
- group: company
  title: ''
  type: Blog
  url: https://intlayer.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aymericzip/intlayer
- group: commercial
  title: ''
  type: Pricing
  url: https://intlayer.org/pricing
- group: start
  title: ''
  type: Login
  url: https://app.intlayer.org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://intlayer.org/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://intlayer.org/privacy-notice
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intlayer-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/intlayer-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/intlayer-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/intlayer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/intlayer-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/intlayer-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: CLI
  url: cli/intlayer-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/intlayer-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/intlayer-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intlayer-domain-security.yml
created: '2026-08-26'
description: Intlayer is an internationalisation (i18n) framework for modern web applications, providing one way to manage multilingual content across React, Next.js, Vue, Svelte, Solid, Nuxt and Astro. Beyond the open-source (Apache-2.0) framework it operates a hosted CMS API at back.intlayer.org secured with OAuth 2.0 client credentials, publishes an RFC 9727 API catalog, a machine-readable agent authentication guide (auth.md), and ships an official MCP server both hosted (mcp.intlayer.org) and as a stdio package (@intlayer/mcp), alongside extensive documentation written for agents as well as humans.
image: https://intlayer.org/github-social-preview.png
layout: provider
mcp_servers:
- description: Official Intlayer MCP server, shipped both as a hosted remote server (Streamable HTTP at https://mcp.intlayer.org — public, no authentication, free to use, with a stated concurrent connection limit) a
  name: Intlayer MCP Server
  slug: intlayer-mcp-server
modified: '2026-09-03'
name: Intlayer
nav: Providers
network: true
overview: 'Intlayer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include i18n, Internationalization, Localization, React, and Next.js.


  Intlayer''s developer surface includes documentation, getting-started guide, engineering blog, pricing, CLI, changelog, and 14 more developer resources.'
plans:
- name: Intlayer Plans Pricing
  plan_count: 4
  slug: intlayer-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Intlayer Rate Limits
  slug: intlayer-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 31.9
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 7.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/intlayer/refs/heads/main/screenshots/intlayer-2026-09-02T145917.png
security:
- kind: authentication
  name: Intlayer Authentication
  slug: intlayer-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Intlayer Domain Security
  slug: intlayer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: intlayer
tags:
- i18n
- Internationalization
- Localization
- React
- Next.js
- CMS
- MCP
website: https://intlayer.org
---
