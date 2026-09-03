---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    well_known_catalog: false
  schema_version: 0.2
  score: 19.6
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: The Pocus core API is a GraphQL endpoint at https://api.pocus.com/graphql, confirmed live and authoritatively named as POCUS_CORE_API_ENDPOINT in Pocus' own published @pocus/cli package. Introspection
  name: Pocus Core API
  slug: pocus-core-api
- description: Pocus operates an OAuth 2.0 authorization server and OpenID Connect provider at auth.pocus.com, publishing RFC 8414 authorization-server metadata, OIDC discovery and a JWKS document anonymously. It su
  name: Pocus Identity (OAuth 2.0 / OpenID Connect)
  slug: pocus-identity
artifact_total: 8
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/apollo/
- group: company
  title: ''
  type: Website
  url: https://www.pocus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pocus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pocus.com/docs/what-is-pocus
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pocus.com/docs/pocus-data-share-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pocus.com/docs/getting-started-with-ai-strategy
- group: operate
  title: ''
  type: Support
  url: https://docs.pocus.com/docs/frequently-asked-questions
- group: company
  title: ''
  type: Blog
  url: https://www.pocus.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PocusHQ
- group: start
  title: ''
  type: SignUp
  url: https://app.pocus.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pocus.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pocus.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pocus.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pocus-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pocus-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pocus-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/pocus-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/pocus-cli.yml
- group: design
  title: ''
  type: Components
  url: components/pocus-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pocus-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pocus-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pocus-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pocus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pocus-rate-limits.yml
created: '2026-08-26'
description: Pocus is an AI sales intelligence and product-led sales platform that turns product usage, CRM and third-party buying signals into prioritized action for revenue teams. It ingests data from customer data warehouses (Snowflake, Redshift, Postgres, Athena, Databricks) and CRMs (Salesforce, HubSpot), scores and enriches accounts and contacts, and surfaces recommendations to reps through an Intelligent Inbox, Playbooks, Lists, SmartMap and a Chrome extension, with write-back and sequencing into Salesforce, HubSpot, Outreach, Salesloft, Apollo, Gong and Slack. Its programmable surface is a GraphQL core API at api.pocus.com, an OAuth 2.0 / OpenID Connect authorization server at auth.pocus.com, SCIM 2.0 user provisioning and SAML SSO, plus a Snowflake data share for warehouse-native delivery. Pocus was acquired by Apollo.io, announced 2026-03-19.
image: https://cdn.prod.website-files.com/643354ef999e7685d54b670e/643355a73f44a743d66fa045_apple-icon-256.png
layout: provider
mcp_servers:
- description: Pocus serves a Model Context Protocol endpoint at https://docs.pocus.com/mcp. A POST of {"jsonrpc":"2.0","id":1,"method":"tools/list"} returns HTTP 401 with a well-formed JSON-RPC error ({"jsonrpc":"2
  name: Pocus Documentation MCP Server
  slug: pocus-documentation-mcp-server
modified: '2026-08-26'
name: Pocus
nav: Providers
network: true
overview: 'Pocus publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales Intelligence, Product-Led Sales, Revenue Operations, and Go-To-Market.


  Pocus'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 17 more developer resources.'
plans:
- name: Pocus Plans Pricing
  plan_count: 0
  slug: pocus-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Pocus Rate Limits
  slug: pocus-rate-limits
scopes:
- name: Pocus Scopes
  scope_count: 0
  slug: pocus-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 25.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pocus/refs/heads/main/screenshots/pocus-2026-09-02T151605.png
security:
- kind: authentication
  name: Pocus Authentication
  slug: pocus-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Pocus Domain Security
  slug: pocus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pocus
tags:
- Company
- Sales Intelligence
- Product-Led Sales
- Revenue Operations
- Go-To-Market
- Data Enrichment
- CRM
- Artificial Intelligence
- GraphQL
website: https://www.pocus.com/
---
