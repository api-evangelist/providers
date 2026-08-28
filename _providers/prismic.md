---
access_model:
  confidence: high
  label: Public self-service with a free tier
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://prismic.io/pricing
  - https://prismic.io/dashboard/signup
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-08-26'
api_count: 8
apis:
- description: The Content API is Prismic's primary read surface. It queries published documents from a repository with a bracketed filter language (`q`), orderings, locale selection, link expansion (`fetchLinks`) a
  name: Prismic Content API
  slug: content-api
- description: The Repository API is the gateway to a Prismic repository. A single unauthenticated GET returns the repository's available refs (including the master ref every Content API query needs), its custom typ
  name: Prismic Repository API
  slug: repository-api
- description: 'A read-only GraphQL endpoint for deep and selective fetching of content from a Prismic repository. The schema is generated per repository: every custom type and shared slice produces its own object ty'
  name: Prismic GraphQL API
  slug: graphql-api
- description: The Types API reads and writes a repository's content models — custom types and Slice Machine shared slices — as JSON. It is how content models are backed up, versioned, generated into TypeScript type
  name: Prismic Types API
  slug: types-api
- description: 'The Asset API manages a repository''s media library: list and search assets by keyword, upload a new asset as multipart form data, patch its alt text, notes and credits, or delete it. One asset per req'
  name: Prismic Asset API
  slug: asset-api
- description: The Migration API creates and updates Prismic pages programmatically, using the same document shape the Content API returns. Everything it writes lands in a migration release as a draft for human revi
  name: Prismic Migration API
  slug: migration-api
- description: A single-endpoint beta API that returns every tag used across a repository's pages, including tags on drafts and pages staged in releases, as a flat array. Access is activated on request via the commu
  name: Prismic Tags API
  slug: tags-api
- description: 'A remote, OAuth-protected Model Context Protocol server that lets an AI assistant search, read, create and publish Prismic content in conversation. Sixteen tools across discovery, read and write. MCP '
  name: Prismic MCP Server
  slug: mcp
artifact_total: 17
asyncapis:
- description: ''
  name: Prismic Webhooks
  slug: prismic-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://prismic.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://prismic.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://prismic.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://prismic.io/docs/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://prismic.io/docs/nextjs
- group: operate
  title: ''
  type: Support
  url: https://prismic.io/docs/help-center
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.prismic.io/
- group: company
  title: ''
  type: Blog
  url: https://prismic.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prismicio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prismic-io
- group: commercial
  title: ''
  type: Pricing
  url: https://prismic.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://prismic.io/dashboard/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prismic.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prismic.io/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/5743666/TzCHBqbH
- group: operate
  title: ''
  type: ChangeLog
  url: https://prismic.io/updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/prismic-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.prismic.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prismic-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://prismic.io/legal/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/prismic-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/prismic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prismic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prismic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prismic-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/prismic-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/prismic-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/prismic-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/prismic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/prismic-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/prismic-cli.yml
- group: design
  title: ''
  type: Components
  url: components/prismic-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/prismic-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/prismic-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prismic-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prismic-well-known.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/prismic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prismic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/prismic-finops.md
created: 2026-06-14
description: 'Prismic is a headless CMS and page builder that lets marketing teams create and manage website content independently while developers work in their preferred stack. Content is modelled as custom types and reusable "slices", authored in a visual Page Builder or locally in Slice Machine, and delivered over a CDN-backed API. Prismic runs seven public HTTP APIs across four hosts: a Content API and Repository API for reads, a beta Tags API, a Types API for content models, an Asset API for the media library, a Migration API for bulk content creation, and a read-only GraphQL endpoint whose schema is generated per repository from the customer''s own content model. Every read is addressed to a content "ref" naming a specific published version. Prismic also ships a first-party CLI, a published Agent Skill, and a remote OAuth-protected MCP server with sixteen tools, and supports Next.js, Nuxt and SvelteKit with first-party rendering components.'
graphqls:
- description: 'generated: ''2026-08-13'''
  name: Prismic GraphQL API
  slug: prismic-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prismic.png
layout: provider
mcp_servers:
- description: ''
  name: Prismic MCP Server
  slug: prismic-mcp-server
modified: 2026-08-13
name: Prismic
nav: Providers
network: true
overview: 'Prismic publishes 1 API on the [APIs.io](https://apis.io/) network: Types API. Tagged areas include GraphQL, Headless CMS, Content Management, Page Builder, and JAMstack.


  The Prismic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Prismic''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Prismic Plans Pricing
  plan_count: 6
  slug: prismic-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Prismic Rate Limits
  slug: prismic-rate-limits
score:
  band: exemplar
  composite: 70.3
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 48.9
    developer_ergonomics: 90.5
    discoverability: 100.0
    governance: 18.2
    operational_transparency: 84.2
  previous_composite: 70.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prismic/refs/heads/main/screenshots/prismic-2026-06-20T192117.png
security:
- kind: authentication
  name: Prismic Authentication
  slug: prismic-authentication
  summary_line: apiKey/http/oauth2 · 6 schemes
- kind: domain-security
  name: Prismic Domain Security
  slug: prismic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prismic Vulnerability Disclosure
  slug: prismic-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Prismic Trust Center
  slug: prismic-trust-center
  summary_line: trust center published
slug: prismic
tags:
- GraphQL
- Headless CMS
- Content Management
- Page Builder
- JAMstack
- Marketing
- Content Delivery
- Developer Tools
- MCP
- Webhook
- Localization
- Digital Asset Management
website: https://prismic.io
---
