---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://gateway.tollbit.com
  baseurl_source: declared
  description: The Auth Tokens API from Tollbit — 3 operation(s) for auth tokens.
  name: Tollbit Auth Tokens API
  slug: tollbit-auth-tokens-api
- baseURL: https://gateway.tollbit.com
  baseurl_source: declared
  description: The Dev API from Tollbit — 1 operation(s) for dev.
  name: Tollbit Dev API
  slug: tollbit-dev-api
- baseURL: https://gateway.tollbit.com
  baseurl_source: declared
  description: The Reporting API from Tollbit — 1 operation(s) for reporting.
  name: Tollbit Reporting API
  slug: tollbit-reporting-api
- baseURL: https://gateway.tollbit.com
  baseurl_source: declared
  description: The Search API from Tollbit — 1 operation(s) for search.
  name: Tollbit Search API
  slug: tollbit-search-api
- baseURL: https://gateway.tollbit.com
  baseurl_source: declared
  description: The Tollbit Content API from Tollbit — 4 operation(s) for tollbit content.
  name: Tollbit Tollbit Content API
  slug: tollbit-tollbit-content-api
- baseURL: https://gateway.tollbit.com
  baseurl_source: declared
  description: The Tollbit Subdomain API from Tollbit — 1 operation(s) for tollbit subdomain.
  name: Tollbit Tollbit Subdomain API
  slug: tollbit-tollbit-subdomain-api
artifact_total: 22
asyncapis:
- description: TollBit pushes real-time webhook notifications to subscriber applications when content becomes available (created or updated) from TollBit publisher properties, so consumers do not have to poll. Deliv
  name: TollBit Content Events (Webhooks)
  slug: tollbit-content-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TollBit Auth Tokens API
  slug: open-tollbit-auth-tokens-api
- collection_type: open
  name: TollBit Auth Tokens Dev API
  slug: open-tollbit-dev-api
- collection_type: open
  name: TollBit Auth Tokens Get Catalog of Pages for Property API
  slug: open-tollbit-get-catalog-of-pages-for-property-api
- collection_type: open
  name: TollBit Auth Tokens Get Tollbit Content API
  slug: open-tollbit-get-tollbit-content-api
- collection_type: open
  name: TollBit Auth Tokens Get Tollbit Rates API
  slug: open-tollbit-get-tollbit-rates-api
- collection_type: open
  name: TollBit Auth Tokens Report Content Usage API
  slug: open-tollbit-report-content-usage-api
- collection_type: open
  name: TollBit Auth Tokens Reporting API
  slug: open-tollbit-reporting-api
- collection_type: open
  name: TollBit Auth Tokens Search API
  slug: open-tollbit-search-api
- collection_type: open
  name: TollBit Auth Tokens Search Content API
  slug: open-tollbit-search-content-api
- collection_type: open
  name: TollBit Auth Tokens Tollbit Content API
  slug: open-tollbit-tollbit-content-api
- collection_type: open
  name: TollBit Auth Tokens Tollbit Subdomain API
  slug: open-tollbit-tollbit-subdomain-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/tollbit-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tollbit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tollbit-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/tollbit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tollbit-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tollbit-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tollbit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tollbit-llms.txt
- group: design
  title: ''
  type: Components
  url: components/tollbit-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tollbit-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tollbit-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tollbit-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tollbit-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hack.tollbit.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tollbit.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tollbit.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tollbit.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.tollbit.com/docs/feedback-support
- group: company
  title: ''
  type: Blog
  url: https://tollbit.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tollbit
- group: start
  title: ''
  type: SignUp
  url: https://app.tollbit.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.tollbit.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tollbit.com/legal/developer-platform-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tollbit.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://tollbit.com
created: '2026-07-17'
description: TollBit is the web stack for the agentic internet, giving publishers and commerce sites the infrastructure to analyze, control, and monetize AI agent access to their content. Publishers verify a property, stream logs for AI-bot analytics, and stand up an "Agent Site" front door (the tollbit.<domain> subdomain) that separates bot traffic from humans and applies content controls, licensing, and usage-based paywalls. Its developer API lets AI agents and builders discover licensable content through Licensed Search, fetch rates and license options, mint cryptographically signed one-time access tokens, retrieve licensed or indexed content as markdown or HTML, self-report usage, and receive webhook notifications when content changes. TollBit ships official Python and Node SDKs, a native CLI with a bundled Agent Skill, an MCP toolbox server, and additional agent access methods (NLWeb, Agent2Agent). Added to the API Evangelist network as a portfolio company of Lightspeed Venture Partners
  and enriched from its public developer surface.
image: https://avatars.githubusercontent.com/u/159727288?v=4
layout: provider
mcp_servers:
- description: TollBit ships an official Model Context Protocol server ("MCP Toolbox") that connects AI agents to TollBit's dynamic toolbox — licensed search and authorized content access across TollBit publisher pr
  name: TollBit MCP Toolbox
  slug: tollbit-mcp-toolbox
modified: '2026-07-21'
name: Tollbit
nav: Providers
network: true
overview: 'Tollbit publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Auth Tokens API, Dev API, Reporting API, and 3 more. Tagged areas include Company, Content Licensing, Content Monetization, AI Agents, and Agentic Web.


  The Tollbit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tollbit''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 57.6
    developer_ergonomics: 58.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 42.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: unknown
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tollbit/refs/heads/main/screenshots/tollbit-2026-08-17T082402.png
security:
- kind: authentication
  name: Tollbit Authentication
  slug: tollbit-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Tollbit Domain Security
  slug: tollbit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tollbit
tags:
- Company
- Content Licensing
- Content Monetization
- AI Agents
- Agentic Web
- Search
- Bot Management
- Web Infrastructure
- Developer API
website: https://tollbit.com
---
