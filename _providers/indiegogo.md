---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Indiegogo Agentic Access
  operation_count: 3
  slug: indiegogo-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: The Creators API from Indiegogo — 1 operation(s) for creators.
  name: Indiegogo Creators API
  slug: indiegogo-creators-api
- description: The Projects API from Indiegogo — 2 operation(s) for projects.
  name: Indiegogo Projects API
  slug: indiegogo-projects-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Indiegogo Public Creators API
  slug: open-indiegogo-creators-api
- collection_type: open
  name: Indiegogo Public Creators Projects API
  slug: open-indiegogo-projects-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/indiegogo-public-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.indiegogo.com/category/617-developer-resources
- group: docs
  title: ''
  type: Documentation
  url: https://help.indiegogo.com/article/616-indiegogo-public-api
- group: docs
  title: ''
  type: APIReference
  url: https://help.indiegogo.com/category/617-developer-resources
- group: operate
  title: ''
  type: Support
  url: https://support.indiegogo.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.indiegogo.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/indiegogo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.indiegogo.com/en/info/fees
- group: start
  title: ''
  type: SignUp
  url: https://www.indiegogo.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.indiegogo.com/about/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.indiegogo.com/about/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/indiegogo-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/indiegogo-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/indiegogo-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/indiegogo-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/indiegogo-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/indiegogo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/indiegogo-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/indiegogo-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/indiegogo-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/indiegogo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/indiegogo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/indiegogo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.indiegogo.com/
created: '2026-07-17'
description: Indiegogo is a global crowdfunding platform where entrepreneurs, inventors, and creators raise money for products, creative works, and community projects through campaigns backed by individual contributors. Founded in 2008, it is one of the largest reward-based crowdfunding sites alongside Kickstarter, and it also runs InDemand for ongoing post-campaign fundraising. For developers, Indiegogo publishes a read-only Public API (https://www.indiegogo.com/api/public) that returns creators and active crowdfunding projects without authentication, with responses cached for a short duration. A separate, now-deprecated Partner API (api.indiegogo.com) previously offered token-authenticated access to campaign, perk, contribution, and comment data. This profile was seeded from VC-portfolio sourcing and enriched by the API Evangelist pipeline against the live public endpoints.
image: https://avatars.githubusercontent.com/u/889441?v=4
layout: provider
mcp_servers:
- description: ''
  name: Indiegogo MCP Server
  slug: indiegogo-mcp-server
modified: '2026-07-19'
name: Indiegogo
nav: Providers
network: true
overview: 'Indiegogo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Creators API and Projects API. Tagged areas include Company, Consumer, Crowdfunding, Fundraising, and Campaigns.


  Indiegogo''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 53.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/indiegogo/refs/heads/main/screenshots/indiegogo-2026-07-25T222320.png
security:
- kind: authentication
  name: Indiegogo Authentication
  slug: indiegogo-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Indiegogo Domain Security
  slug: indiegogo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: indiegogo
tags:
- Company
- Consumer
- Crowdfunding
- Fundraising
- Campaigns
- Payments
- Marketplace
- Creators
website: https://www.indiegogo.com/
---
