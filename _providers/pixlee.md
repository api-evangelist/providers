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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pixlee Agentic Access
  operation_count: 4
  slug: pixlee-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 3
apis:
- description: Consume approved UGC media from albums (with filters/sorts and pagination), ingest new content from a URL or file, and add or update products. API key in query plus HMAC-SHA1 signature for writes; res
  name: Pixlee Content API
  slug: pixlee-content-api
- description: Create albums and add or update products
  name: Pixlee Albums API
  slug: pixlee-albums-api
- description: Upload new content from a URL or a file
  name: Pixlee Media API
  slug: pixlee-media-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pixlee Content Albums API
  slug: open-pixlee-albums-api
- collection_type: open
  name: Pixlee Albums Content API
  slug: open-pixlee-content-api
- collection_type: open
  name: Pixlee Content Albums Media API
  slug: open-pixlee-media-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.pixlee.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pixlee.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.pixlee.com/reference/about-the-content-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.pixlee.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.pixlee.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pixlee-changelog.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pixlee
- group: operate
  title: ''
  type: Support
  url: https://support.emplifi.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://emplifi.io/resource-type/blogs/
- group: commercial
  title: ''
  type: Pricing
  url: https://emplifi.io/pricing/
- group: start
  title: ''
  type: Login
  url: https://emplifi.io/login/
- group: start
  title: ''
  type: SignUp
  url: https://emplifi.io/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emplifi.io/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emplifi.io/legal/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://emplifi.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pixlee-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/pixlee-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pixlee-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pixlee-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pixlee-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pixlee-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pixlee-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pixlee-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pixlee-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixlee-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pixlee-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pixlee-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/pixlee-components.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pixlee-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Pixlee (Pixlee TurnTo, now part of Emplifi) is a visual and social user-generated content (UGC) marketing platform that helps brands collect, curate, moderate, and display customer photos and videos across their website, mobile apps, and email. The Pixlee Content API (v2) gives brands programmatic access to their approved media in albums with rich filtering and sorting, lets them ingest new content from a URL or an uploaded file, and add or update commerce products that media can be tagged with. Authentication is via an account API key passed as a query parameter, with HMAC-SHA1 request signing required for all writes. Pixlee also ships embeddable JavaScript display widgets, email display blocks, and native iOS/Android UI SDKs. Originally an a16z-backed startup, Pixlee was acquired by Emplifi.
image: https://files.readme.io/9160404-small-transparentLogo.png
layout: provider
mcp_servers:
- description: ''
  name: Pixlee MCP Server
  slug: pixlee-mcp-server
modified: '2026-07-20'
name: Pixlee
nav: Providers
network: true
overview: 'Pixlee publishes 3 APIs on the [APIs.io](https://apis.io/) network: Content API, Albums API, and Media API. Tagged areas include Company, User Generated Content, Social Commerce, Visual Marketing, and Content.


  Pixlee''s developer surface includes documentation, API reference, getting-started guide, changelog, support, engineering blog, pricing, and 23 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 13.3
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/screenshots/pixlee-2026-08-17T081245.png
security:
- kind: authentication
  name: Pixlee Authentication
  slug: pixlee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pixlee Domain Security
  slug: pixlee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pixlee
tags:
- Company
- User Generated Content
- Social Commerce
- Visual Marketing
- Content
- Media
- E-Commerce
- Widgets
- Emplifi
website: https://emplifi.io/
---
