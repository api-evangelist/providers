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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Mason Agentic Access
  operation_count: 16
  slug: mason-agentic-access
  summary_line: 16 operations · 11 acting
api_count: 8
apis:
- description: The Apps API from Mason — 2 operation(s) for apps.
  name: Mason Apps API
  slug: mason-apps-api
- description: The Create Image API from Mason — 1 operation(s) for create image.
  name: Mason Create Image API
  slug: mason-create-image-api
- description: The Images API from Mason — 2 operation(s) for images.
  name: Mason Images API
  slug: mason-images-api
- description: The Retrieve an Image API from Mason — 1 operation(s) for retrieve an image.
  name: Mason Retrieve an Image API
  slug: mason-retrieve-an-image-api
- description: The Search API from Mason — 1 operation(s) for search.
  name: Mason Search API
  slug: mason-search-api
- description: The Template Mappings API from Mason — 1 operation(s) for template mappings.
  name: Mason Template Mappings API
  slug: mason-template-mappings-api
- description: The Tiered Discounts API from Mason — 4 operation(s) for tiered discounts.
  name: Mason Tiered Discounts API
  slug: mason-tiered-discounts-api
- description: The Webhooks API from Mason — 2 operation(s) for webhooks.
  name: Mason Webhooks API
  slug: mason-webhooks-api
artifact_total: 24
asyncapis:
- description: ''
  name: Mason Webhooks
  slug: mason-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mason Apps API
  slug: open-mason-apps-api
- collection_type: open
  name: Mason Apps Create Image API
  slug: open-mason-create-image-api
- collection_type: open
  name: Mason Apps Images API
  slug: open-mason-images-api
- collection_type: open
  name: Mason Apps Retrieve an Image API
  slug: open-mason-retrieve-an-image-api
- collection_type: open
  name: Mason Apps Search API
  slug: open-mason-search-api
- collection_type: open
  name: Mason Apps Template Mappings API
  slug: open-mason-template-mappings-api
- collection_type: open
  name: Mason Apps Tiered Discounts API
  slug: open-mason-tiered-discounts-api
- collection_type: open
  name: Mason Apps Webhooks API
  slug: open-mason-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/mason-apps-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mason-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://getmason.io/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mason-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mason-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mason-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mason-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://getmason.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.getmason.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.getmason.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://www.getmason.dev/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.getmason.dev/docs/getting-to-know-mason
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.getmason.dev/changelog
- group: company
  title: ''
  type: Blog
  url: https://getmason.io/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://getmason.io/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.getmason.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getmason.io/termsofuse/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getmason.io/privacypolicy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kubric
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mason-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mason-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mason-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mason-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mason-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mason-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mason-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mason-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mason-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mason-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Mason (getmason.io), the company behind the ModeMagic Shopify app, is an AI-powered "agentic shopping engine" for ecommerce brands. Built by Kubric, the platform pairs merchandising, promotion, conversion and gamification AI agents with a developer platform for programmatic creative generation and commerce automation. Its public developer hub at getmason.dev documents a REST API (OAuth2 bearer, base host https://api.getmason.io) spanning app provisioning, template-driven image/creative generation (Genie), long-running creative tasks, asset search, webhook subscriptions, and a promotion/discount engine (Scrooge) for tiered, bulk and Buy-X-Get-Y discounts, plus a custom-checkout integration contract. Surfaced as a portfolio company of Accel, GGV Capital, Point Nine and Y Combinator; this profile was enriched by the API Evangelist pipeline from Mason's published OpenAPI, llms.txt and developer documentation.
image: https://media.getmason.io/api/assetlib/e5067013-1809-44f3-8847-8d66857625c7.png
layout: provider
mcp_servers:
- description: ''
  name: mason-mcp.yml
  slug: mason-mcpyml
modified: '2026-07-20'
name: Mason
nav: Providers
network: true
overview: 'Mason publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Create Image API, Images API, and 5 more. Tagged areas include Company, Ecommerce, Commerce, AI, and Agents.


  The Mason catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mason''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, engineering blog, pricing, and 23 more developer resources.'
random_paper: 17
scopes:
- name: Mason Scopes
  scope_count: 0
  slug: mason-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.9
  delta: -6.1
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 16.7
    contract_quality: 61.2
    developer_ergonomics: 35.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/mason/refs/heads/main/screenshots/mason-2026-07-25T230331.png
security:
- kind: authentication
  name: Mason Authentication
  slug: mason-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Mason Domain Security
  slug: mason-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mason Vulnerability Disclosure
  slug: mason-vulnerability-disclosure
  summary_line: disclosure policy published
slug: mason
tags:
- Company
- Ecommerce
- Commerce
- AI
- Agents
- Content Generation
- Discounts
- Promotions
- Webhooks
- Shopify
website: https://getmason.io/
---
