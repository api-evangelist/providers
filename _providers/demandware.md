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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 26.0
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: The modern Salesforce Commerce API (SCAPI) — Shopper APIs (products, search, baskets, orders, customers), Admin APIs, and the Shopper Login and API Access Service (SLAS). Published as OpenAPI, secured
  name: B2C Commerce API (SCAPI)
  slug: b2c-commerce-api-scapi
- description: The legacy Open Commerce API (OCAPI, deprecated in favor of SCAPI) — the Shop API for shopper interactions, the Data API for CRUD against instance data, and the Meta API for retrieving formal API desc
  name: Open Commerce API (OCAPI)
  slug: open-commerce-api-ocapi
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/demandware-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://security.salesforce.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demandware-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.salesforce.com/products/commerce/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.salesforce.com/docs/commerce
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs/commerce/commerce-api/guide
- group: docs
  title: ''
  type: APIReference
  url: https://developer.salesforce.com/docs/commerce/commerce-api/references
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.salesforce.com/docs/commerce/commerce-api/guide/get-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SalesforceCommerceCloud
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/s/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.salesforce.com/products/commerce/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://developer.salesforce.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/legal/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/salesforce-developers/salesforce-developers/documentation/1qkzgik/salesforce-commerce-b2c
- group: build
  title: ''
  type: Packages
  url: packages/demandware-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/demandware-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/demandware-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/demandware-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/demandware-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/demandware-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/demandware-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/demandware-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.salesforce.com/en/compliance/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/demandware-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.salesforce.com/docs/commerce/b2c-commerce/references/b2c-commerce-ocapi
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/demandware-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.salesforce.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/demandware-llms.txt
created: '2026-07-17'
description: 'Demandware is the cloud commerce platform now sold by Salesforce as Salesforce B2C Commerce Cloud. Founded in 2004 and taken public on the NYSE (DWRE) in 2012, Demandware was acquired by Salesforce in 2016 for roughly $2.8B and rebranded as Salesforce Commerce Cloud. Its developer surface centers on two REST API families: the modern B2C Commerce API (SCAPI) — Shopper APIs, Admin APIs, and the Shopper Login and API Access Service (SLAS) — published as OpenAPI, and the older Open Commerce API (OCAPI, now deprecated) with its Shop, Data, and Meta APIs. The platform ships first-party SDKs (commerce-sdk, commerce-sdk-isomorphic, PWA Kit), a B2C CLI (sfcc-ci and the newer @salesforce/b2c-cli), a developer-experience MCP server, packaged Agent Skills, and Account Manager / SLAS OAuth2 authentication.'
image: https://developer.salesforce.com/resources2/logos/salesforce-developers-logo.png
layout: provider
mcp_servers:
- description: ''
  name: demandware-mcp.yml
  slug: demandware-mcpyml
modified: '2026-07-18'
name: Demandware
nav: Providers
network: true
overview: 'Demandware publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-commerce, Retail, and Commerce Cloud.


  Demandware''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 25 more developer resources.'
random_paper: 28
scopes:
- name: Demandware Scopes
  scope_count: 0
  slug: demandware-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 84.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 45.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Demandware Authentication
  slug: demandware-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Demandware Domain Security
  slug: demandware-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Demandware Vulnerability Disclosure
  slug: demandware-vulnerability-disclosure
  summary_line: disclosure policy published
slug: demandware
tags:
- Company
- Commerce
- E-commerce
- Retail
- Commerce Cloud
- Storefront
- Shopper
- Catalog
- Orders
- SaaS
- Salesforce
website: https://www.salesforce.com/products/commerce/
---
