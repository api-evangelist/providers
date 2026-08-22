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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Public GraphQL API for verified Nivoda customers to search live natural and lab-grown diamond, gemstone and jewelry inventory, retrieve real-time pricing, certificates and media, and (with Pro access)
  name: Nivoda Diamonds GraphQL API (Production)
  slug: nivoda-diamonds-graphql-api-production
- description: Staging / sandbox GraphQL endpoint mirroring production, with a GraphiQL explorer for browsing queries and mutations and testing code. Staging username and password are shared on request by a Nivoda a
  name: Nivoda Diamonds GraphQL API (Staging)
  slug: nivoda-diamonds-graphql-api-staging
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nivoda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nivoda.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bitbucket.org/nivoda/nivoda-api/src/main/
- group: docs
  title: ''
  type: Documentation
  url: https://bitbucket.org/nivoda/nivoda-api/src/main/
- group: docs
  title: ''
  type: APIReference
  url: https://integrations.nivoda.net/api/diamonds-graphiql
- group: start
  title: ''
  type: GettingStarted
  url: https://bitbucket.org/nivoda/nivoda-api/src/main/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nivoda
- group: operate
  title: ''
  type: Support
  url: https://buyerhelp.nivoda.com/
- group: company
  title: ''
  type: Blog
  url: https://nivoda.com/category/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.nivoda.net/
- group: start
  title: ''
  type: Login
  url: https://app.nivoda.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nivoda.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nivoda.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/nivoda-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nivoda-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nivoda-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nivoda-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nivoda-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nivoda-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nivoda-error-codes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nivoda-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nivoda-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nivoda-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Nivoda is a global B2B marketplace for the diamond, gemstone and jewelry trade, connecting jewelry retailers directly with suppliers of natural and lab-grown diamonds, colored gemstones, melee and made-to-order finished jewelry without the retailer having to hold stock. The platform provides real-time pricing, high-resolution imagery and video, advanced search and quality control, consolidated shipping and invoicing, flexible credit terms and risk-free returns. Nivoda exposes a public GraphQL API that verified customers use to integrate live supplier inventory into their own websites and storefronts, mirroring the same search capabilities as the Nivoda platform and mobile apps, with Pro access adding orders, holds, diamond requests and concierge requests.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nivoda.png
layout: provider
mcp_servers:
- description: ''
  name: nivoda-mcp.yml
  slug: nivoda-mcpyml
modified: '2026-07-20'
name: Nivoda
nav: Providers
network: true
overview: 'Nivoda publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diamonds, Gemstones, Jewelry, and Marketplace.


  Nivoda''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 25.2
  delta: -2.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 28.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nivoda/refs/heads/main/screenshots/nivoda-2026-08-07T185352.png
security:
- kind: authentication
  name: Nivoda Authentication
  slug: nivoda-authentication
  summary_line: bearer · 2 schemes
- kind: domain-security
  name: Nivoda Domain Security
  slug: nivoda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nivoda
tags:
- Company
- Diamonds
- Gemstones
- Jewelry
- Marketplace
- B2B
- GraphQL
- Inventory
- E-commerce
website: https://nivoda.com
---
