---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Company profiles, funding rounds, SEC filings and fund formations, keyed to real-time business events.
  name: Fundz API
  slug: fundz-api
- description: Company acquisitions and M&A events, with acquirer and target organization records where disclosed.
  name: Fundz Acquisitions API
  slug: fundz-acquisitions-api
- description: Business agreements and partnerships announced by companies — distribution, licensing, joint ventures and similar.
  name: Fundz Agreements API
  slug: fundz-agreements-api
- description: Regulation CF and Regulation A crowdfunding campaigns, sourced from SEC Form C and Form 1-A filings.
  name: Fundz Crowdfundings API
  slug: fundz-crowdfundings-api
- description: Executive hires and appointments — new C-level, VP and board appointments at private and public companies.
  name: Fundz Executives API
  slug: fundz-executives-api
- description: Funding rounds — seed through late-stage venture and private equity — with the investors on the round and the full organization record.
  name: Fundz Fundings API
  slug: fundz-fundings-api
- description: Product launches and major product announcements.
  name: Fundz Products API
  slug: fundz-products-api
- description: 'The agent-facing Fundz surface, served on the same host under /v1/watch/*: AI-scored leads matched to an ICP, a raw business-event feed, a company watchlist, nightly market aggregates, and signed webh'
  name: FundzWatch API
  slug: fundzwatch-api
artifact_total: 21
asyncapis:
- description: ''
  name: Fundz Webhooks
  slug: fundz-webhooks
collections:
- collection_type: open
  name: Fundz Acquisitions API
  slug: open-fundz-acquisitions-api
- collection_type: open
  name: Fundz Agreements API
  slug: open-fundz-agreements-api
- collection_type: open
  name: Fundz Crowdfundings API
  slug: open-fundz-crowdfundings-api
- collection_type: open
  name: Fundz Executives API
  slug: open-fundz-executives-api
- collection_type: open
  name: Fundz Fundings API
  slug: open-fundz-fundings-api
- collection_type: open
  name: Fundz Products API
  slug: open-fundz-products-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fundz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fundz.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fundz.net/fundz-api
- group: commercial
  title: ''
  type: Pricing
  url: https://fundz.net/pricing
- group: start
  title: ''
  type: Signup
  url: https://fundz.net/api-trial
- group: agent
  title: ''
  type: LlmsText
  url: https://app.fundz.net/llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fundz-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fundz-plans-pricing.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fundz-authentication.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Fund-z/fundzwatch-mcp
- group: build
  title: ''
  type: Packages
  url: packages/fundz-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fundz-packages.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/fundz-tool-crosswalk.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fundz-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fundz-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fundz-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fundz-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fundz-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fundz-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fundz-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fundz-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fundz-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://app.fundz.net/knowledge/api-references
- group: start
  title: ''
  type: GettingStarted
  url: https://app.fundz.net/knowledge/api-references/authentication
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fundz.net/fundz-api
- group: other
  title: ''
  type: KnowledgeBase
  url: https://app.fundz.net/knowledge
- group: operate
  title: ''
  type: Support
  url: https://www.fundz.net/contact
- group: company
  title: ''
  type: Blog
  url: https://www.fundz.net/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fund-z
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Fund-z/fundz-api-spec
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fundz.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fundz.net/privacy
- group: other
  title: ''
  type: Licensing
  url: https://www.fundz.net/fundz-data-licensing
created: '2026-08-03'
description: 'Fundz is an event-first business intelligence platform, founded 2015, tracking 200,000+ companies and surfacing funding rounds, executive changes, M&A activity, SEC filings (8-K, 10-K, 10-Q, Form D) and website modifications in real time. Rather than storing millions of static records it focuses on companies showing active signals, and scores them against each user''s criteria. The API exposes company profiles, fundings, SEC filings and fund formations from api.fundz.net with an API key in the Authorization header. It sits in the same category as Harmonic and Crunchbase, and competes explicitly on access: an API key is free and issued instantly with no card and no sales call, and pricing is published rather than quoted. Fundz also ships an MCP server listed on the official Model Context Protocol registry, and publishes an llms.txt.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fundz.png
layout: provider
mcp_servers:
- description: 'FundzWatch MCP server, listed on the OFFICIAL Model Context Protocol registry — not only a third-party directory. It is distributed as an npm package over stdio: an agent operator installs and runs it'
  name: io.github.Fund-z/fundzwatch
  slug: iogithubfund-zfundzwatch
modified: '2026-08-14'
name: Fundz
nav: Providers
network: true
overview: 'Fundz publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Acquisitions API, Agreements API, Crowdfundings API, and 3 more. Tagged areas include Business Intelligence, Funding, Private Markets, Mergers and Acquisitions, and SEC Filings.


  The Fundz catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fundz''s developer surface includes documentation, pricing, signup flow, authentication, sandbox, API reference, getting-started guide, and 27 more developer resources.'
plans:
- name: Fundz Plans Pricing
  plan_count: 4
  slug: fundz-plans-pricing
- name: Fundz Plans
  plan_count: 0
  slug: fundz-plans
random_paper: 5
rate_limits:
- limit_count: 5
  name: Fundz Rate Limits
  slug: fundz-rate-limits
score:
  band: strong
  composite: 63.3
  coverage:
    artifact_dirs: 21
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 67.8
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 63.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fundz/refs/heads/main/screenshots/fundz-2026-08-17T123449.png
security:
- kind: authentication
  name: Fundz Authentication
  slug: fundz-authentication
  summary_line: apiKey/http-bearer · 4 schemes
- kind: domain-security
  name: Fundz Domain Security
  slug: fundz-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fundz
tags:
- Business Intelligence
- Funding
- Private Markets
- Mergers and Acquisitions
- SEC Filings
- Signals
- Sales Intelligence
- MCP
- Agents
website: https://www.fundz.net/
---
