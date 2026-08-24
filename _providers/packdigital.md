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
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.3
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: GraphQL API to programmatically manage Shopify Hydrogen storefront content — pages, product pages, collection pages, blogs, articles, sections, templates, site settings, schedules, and revisions — wit
  name: Pack Content Management API
  slug: pack-content-management-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/packdigital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://packdigital.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.packdigital.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.packdigital.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.packdigital.com/api-reference/content-management-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.packdigital.com/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.packdigital.com/getting-started/faq
- group: company
  title: ''
  type: Blog
  url: https://packdigital.com/blogs/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/packdigital
- group: commercial
  title: ''
  type: Pricing
  url: https://packdigital.com/pages/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.packdigital.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.packdigital.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://packdigital.com/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://packdigital.com/pages/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/packdigital-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/packdigital-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/packdigital-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/packdigital-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/packdigital-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/packdigital-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/packdigital-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/packdigital-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/packdigital-problem-types.yml
- group: design
  title: ''
  type: Components
  url: components/packdigital-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Pack Digital is a digital experience platform purpose-built for Shopify Hydrogen that lets AI agents and human teams collaborate on headless storefronts: agents draft changes, the team reviews them in content releases, and you ship when ready. Pack pairs a visual Customizer, server-side A/B testing, media and localization, and the open-source Blueprint Hydrogen theme with a developer surface — a GraphQL Content Management API, JavaScript SDKs (@pack/client, @pack/react, @pack/hydrogen, @pack/types), and an official hosted MCP server for agent-native content editing, publishing, scheduling, and testing. Backed by Norwest Venture Partners.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/packdigital.png
layout: provider
mcp_servers:
- description: Official remote MCP server that connects AI assistants to Pack to search, edit, preview, publish, schedule, and A/B test Shopify Hydrogen storefront content. Backed by the Pack GraphQL Content Managem
  name: Packdigital MCP Server
  slug: packdigital-mcp-server
modified: '2026-07-20'
name: Packdigital
nav: Providers
network: true
overview: 'Packdigital publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Content Management, Headless Commerce, Shopify, and Hydrogen.


  Packdigital''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 29.3
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 29.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/packdigital/refs/heads/main/screenshots/packdigital-2026-08-07T191242.png
security:
- kind: authentication
  name: Packdigital Authentication
  slug: packdigital-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Packdigital Domain Security
  slug: packdigital-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: packdigital
tags:
- Company
- Content Management
- Headless Commerce
- Shopify
- Hydrogen
- CMS
- A/B Testing
- GraphQL
- MCP
- Agents
- Storefront
website: https://packdigital.com
---
