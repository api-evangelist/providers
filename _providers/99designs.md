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
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: 99Designs Agentic Access
  operation_count: 8
  slug: 99designs-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 5
apis:
- description: Collect design briefs.
  name: 99designs Briefs API
  slug: 99designs-briefs-api
- description: Generate partner coupon tokens.
  name: 99designs Coupons API
  slug: 99designs-coupons-api
- description: Search and retrieve designers, reviews, and portfolios.
  name: 99designs Designers API
  slug: 99designs-designers-api
- description: List the 99designs products a partner has available for sale, with prices and the brief schema each product version requires.
  name: 99designs Products API
  slug: 99designs-products-api
- description: Place orders against 99designs products.
  name: 99designs Orders API
  slug: 99designs-orders-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 99designs Briefs API
  slug: open-99designs-briefs-api
- collection_type: open
  name: 99designs Coupons API
  slug: open-99designs-coupons-api
- collection_type: open
  name: 99designs Briefs Designers API
  slug: open-99designs-designers-api
- collection_type: open
  name: 99designs Briefs Orders API
  slug: open-99designs-orders-api
- collection_type: open
  name: 99designs Products API
  slug: open-99designs-products-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/99designs-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/99designs-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/99designs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/99designs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/99designs-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/99designs-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/99designs-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/99designs-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/99designs-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/99designs-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/99designs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/99designs-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/99designs-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/99designs-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/99designs-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/99designs-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/99designs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://99designs.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/99designs-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://99designs.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://api.99designs.com/resources/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.99designs.com/resources/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.99designs.com/resources/docs/#getting-started
- group: start
  title: ''
  type: SignUp
  url: https://99designs.com/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/99designs
- group: commercial
  title: ''
  type: Pricing
  url: https://99designs.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://99designs.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.99designs.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://99designs.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://99designs.com/legal/privacy
- group: company
  title: ''
  type: Website
  url: https://www.99designs.com
created: '2026-07-17'
description: '99designs by Vista is a global creative marketplace connecting clients with a worldwide network of freelance designers for logos, brand identity, web and packaging design, illustration, and more, using both a design-contest model and one-to-one projects. Its partner API (base https://api.99designs.com/resources/v1) lets platforms embed a fully-managed creative marketplace: search and match designers, retrieve designer profiles, reviews and portfolios, collect design briefs, list the products a partner has available for sale, place orders against those product versions, and generate partner coupons. Authentication uses a pair of API key headers (Api-Key-Id and Api-Key-Secret) issued to partners on request — access is sales-gated rather than self-serve, and no API plans or pricing are published. Founded in 2008 as a SitePoint spin-off and acquired by Cimpress/Vista in 2020.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/99designs.png
layout: provider
mcp_servers:
- description: ''
  name: 99designs MCP Server
  slug: 99designs-mcp-server
modified: '2026-08-13'
name: 99designs
nav: Providers
network: true
overview: '99designs publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Briefs API, Coupons API, Designers API, and 2 more. Tagged areas include Company, Media, Design, Marketplace, and Creative.


  99designs'' developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, and 25 more developer resources.'
plans:
- name: 99Designs Plans Pricing
  plan_count: 0
  slug: 99designs-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: 99Designs Rate Limits
  slug: 99designs-rate-limits
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 57.8
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/99designs/refs/heads/main/screenshots/99designs-2026-07-25T181252.png
security:
- kind: authentication
  name: 99Designs Authentication
  slug: 99designs-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: 99Designs Domain Security
  slug: 99designs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 99Designs Vulnerability Disclosure
  slug: 99designs-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 99designs
tags:
- Company
- Media
- Design
- Marketplace
- Creative
- Freelance
- Graphic Design
- Branding
website: https://www.99designs.com
---
