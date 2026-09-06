---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.makeswift.com
  baseurl_source: declared
  description: The locale API from Makeswift — 3 operation(s) for locale.
  name: Makeswift locale API
  slug: makeswift-locale-api
- baseURL: https://api.makeswift.com
  baseurl_source: declared
  description: The page API from Makeswift — 2 operation(s) for page.
  name: Makeswift page API
  slug: makeswift-page-api
- baseURL: https://api.makeswift.com
  baseurl_source: declared
  description: The site API from Makeswift — 3 operation(s) for site.
  name: Makeswift site API
  slug: makeswift-site-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: REST locale API
  slug: open-makeswift-locale-api
- collection_type: open
  name: REST locale page API
  slug: open-makeswift-page-api
- collection_type: open
  name: REST locale site API
  slug: open-makeswift-site-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/makeswift-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://makeswift.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.makeswift.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.makeswift.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.makeswift.com/developer/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.makeswift.com/developer/docs/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://makeswift.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://makeswift.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.makeswift.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.makeswift.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/makeswift
- group: operate
  title: ''
  type: StatusPage
  url: https://status.makeswift.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.makeswift.com/developer/changelog
- group: build
  title: ''
  type: Packages
  url: packages/makeswift-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/makeswift-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/makeswift-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/makeswift-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/makeswift-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/makeswift-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/makeswift-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/makeswift-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/makeswift-authentication.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Makeswift is a composable visual page builder for marketing teams and developers, built for Next.js. It lets marketers visually design, edit, and publish modern web frontends while developers register their own React components and keep full control over hosting and code. Makeswift ships an official React runtime SDK (@makeswift/runtime), a CLI, and a REST API at api.makeswift.com for programmatically managing sites, pages, and locales, plus a hosted documentation MCP server for AI clients. Makeswift is backed by Techstars and partners closely with BigCommerce for composable commerce.
image: https://makeswift.com/
layout: provider
mcp_servers:
- description: ''
  name: Makeswift MCP Server
  slug: makeswift-mcp-server
modified: '2026-07-20'
name: Makeswift
nav: Providers
network: true
overview: 'Makeswift publishes 3 APIs on the [APIs.io](https://apis.io/) network: locale API, page API, and site API. Tagged areas include Company, Visual Page Builder, Website Builder, Next.js, and Headless CMS.


  Makeswift''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 16 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 57.8
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 45.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/makeswift/refs/heads/main/screenshots/makeswift-2026-07-25T225954.png
security:
- kind: authentication
  name: Makeswift Authentication
  slug: makeswift-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Makeswift Domain Security
  slug: makeswift-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: makeswift
tags:
- Company
- Visual Page Builder
- Website Builder
- Next.js
- Headless CMS
- Composable
- Content Management
- Web Development
- Developer Tools
website: https://makeswift.com/
---
