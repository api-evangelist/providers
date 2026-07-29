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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: 99Designs Agentic Access
  operation_count: 7
  slug: 99designs-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 4
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
- description: Place orders against 99designs products.
  name: 99designs Orders API
  slug: 99designs-orders-api
artifact_total: 9
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/99designs-openapi.yml
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
description: '99designs by Vista is a global creative marketplace connecting clients with a worldwide network of freelance designers for logos, brand identity, web and packaging design, illustration, and more, using both a design-contest model and one-to-one projects. Its partner API (base https://api.99designs.com/resources/v1) lets platforms embed a fully-managed creative marketplace: search and match designers, retrieve designer profiles, reviews and portfolios, collect design briefs, place orders against 99designs products, and generate partner coupons. Authentication uses a pair of API key headers (Api-Key-Id and Api-Key-Secret) issued to partners on request. Founded in 2008 as a SitePoint spin-off and acquired by Cimpress/Vista in 2020.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/99designs.png
layout: provider
mcp_servers:
- description: ''
  name: 99designs-mcp.yml
  slug: 99designs-mcpyml
modified: '2026-07-17'
name: 99designs
nav: Providers
network: true
overview: '99designs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Briefs API, Coupons API, Designers API, and 1 more. Tagged areas include Company, Media, Design, Marketplace, and Creative.


  99designs'' developer surface includes authentication, documentation, API reference, signup flow, pricing, engineering blog, support, and 21 more developer resources.'
random_paper: 73
score:
  band: developing
  composite: 42.5
  delta: -4.4
  facets:
    commercial_clarity: 44.7
    contract_quality: 47.5
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
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
