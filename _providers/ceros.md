---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-08-12'
api_count: 6
apis:
- description: The accounts API from Ceros — 1 operation(s) for accounts.
  name: Ceros Accounts API
  slug: ceros-accounts-api
- description: The embedCodes API from Ceros — 1 operation(s) for embedcodes.
  name: Ceros Embed Codes API
  slug: ceros-embedcodes-api
- description: The experience API from Ceros — 1 operation(s) for experience.
  name: Ceros Experience API
  slug: ceros-experience-api
- description: The experiencePage API from Ceros — 6 operation(s) for experiencepage.
  name: Ceros Experience Page API
  slug: ceros-experiencepage-api
- description: The folders API from Ceros — 1 operation(s) for folders.
  name: Ceros Folders API
  slug: ceros-folders-api
- description: The oembed API from Ceros — 1 operation(s) for oembed.
  name: Ceros Oembed API
  slug: ceros-oembed-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ceros-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ceros-public-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.ceros.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.ceros.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.ceros.com/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developers.ceros.com/api/public/ceros-public-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.ceros.com/guides/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://educate.ceros.com/en/
- group: operate
  title: ''
  type: Support
  url: https://www.ceros.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.ceros.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ceros
- group: operate
  title: ''
  type: Roadmap
  url: https://portal.productboard.com/ceros/7-ceros-staging-roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ceros.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://www.ceros.com/login/
- group: start
  title: ''
  type: SignUp
  url: https://www.ceros.com/demo-request/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ceros.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ceros.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ceros.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/ceros-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/ceros-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ceros-packages.yml
- group: design
  title: ''
  type: Components
  url: components/ceros-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ceros-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ceros-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ceros-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ceros-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ceros-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ceros-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ceros-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ceros-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ceros-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ceros-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-09'
description: Ceros is an experiential content platform used by marketing, design and agency teams to build interactive, no-code web content — microsites, landing pages, interactive reports, infographics, pitch decks and embeddable experiences — in a browser design studio and publish them to a CDN. Its developer surface is three separate things. A small read-only REST Public API at rest.ceros.com walks accounts, folders, experiences and embed codes behind a bearer API key, versioned by dated snapshots selected with the x-ceros-api-version header. A browser-side Flex Experience SDK, delivered as an ES module from the Ceros CDN, scripts a published experience at runtime — setting text, controlling media and states, toggling visibility and navigating pages. And a public oEmbed 1.0 endpoint on view.ceros.com, together with first-party connectors for Adobe Experience Manager, Contentful, Optimizely and WordPress, places an experience inside another platform. Ceros also operates MarkUp, its visual
  commenting and collaboration product.
examples:
- key_count: 10
  name: Ceros Oembed Response
  slug: ceros-oembed-response
image: https://www.ceros.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: ceros-mcp.yml
  slug: ceros-mcpyml
modified: '2026-08-09'
name: Ceros
nav: Providers
network: true
overview: 'Ceros publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Embed Codes API, Experience API, and 3 more. Tagged areas include Content Management, Interactive Content, Digital Experience, Embed, and oEmbed.


  Ceros'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 60
score:
  band: developing
  composite: 52.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 58.6
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 42.1
  previous_composite: 52.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 16.7
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Ceros Authentication
  slug: ceros-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ceros Domain Security
  slug: ceros-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Ceros Trust Center
  slug: ceros-trust-center
  summary_line: trust center published
slug: ceros
tags:
- Content Management
- Interactive Content
- Digital Experience
- Embed
- oEmbed
- CMS Integration
- Marketing
- Design
- No Code
- Content Delivery
- Media and Publishing
- SDK
website: https://www.ceros.com/
---
