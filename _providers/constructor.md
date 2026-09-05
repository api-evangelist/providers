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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'REST API for AI-powered product discovery — autocomplete, search, browse, recommendations, quizzes, catalog management, searchandising, and behavioral tracking. A public API key identifies the index; '
  name: Constructor API
  slug: constructor-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://constructor.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.constructor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.constructor.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.constructor.com/reference/main-readme
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.constructor.com/docs
- group: auth
  title: ''
  type: Authentication
  url: authentication/constructor-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/constructor-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/constructor-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/constructor-cli.yml
- group: design
  title: ''
  type: Components
  url: components/constructor-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/constructor-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/constructor-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/constructor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/constructor-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/constructor-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/constructor-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://releases.constructor.io/
- group: design
  title: ''
  type: Conformance
  url: conformance/constructor-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://constructor.com/security-and-compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/constructor-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/constructor-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://constructor.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Constructor-io
- group: start
  title: ''
  type: SignUp
  url: https://app.constructor.io/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://constructor.com/terms-of-service-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://constructor.com/privacy-policy
created: '2026-07-17'
description: Constructor is an AI-powered ecommerce product discovery and search platform. Its Commerce Reasoning Engine interprets shopper behavior, context, and intent to personalize results across Autocomplete, Search (including Natural Language and Image Search), Browse, Recommendations, Quizzes, Collections, Retail Media (Sponsored Listings and Display Ads), and AI Shopping Agents. Retailers integrate over a REST API at ac.cnstrc.com plus first-party SDKs (JavaScript, Node, Python, Ruby, Java, .NET, Swift, Android) and React UI component libraries, manage catalogs and searchandising configuration, and track behavioral beacons. Constructor is a portfolio company of Sapphire Ventures.
image: https://constructor.com/hubfs/constructor-featured-image-2026.png
layout: provider
mcp_servers:
- description: Official remote MCP server hosted by Constructor. Gives AI development tools (Cursor, Windsurf, Claude Desktop, Claude Code) direct access to Constructor documentation and API functionality — searchin
  name: Constructor MCP Server
  slug: constructor-mcp-server
modified: '2026-07-18'
name: Constructor
nav: Providers
network: true
overview: 'Constructor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Search, Product Discovery, and Recommendations.


  Constructor''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, release notes, and 19 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 41.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 30.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/constructor/refs/heads/main/screenshots/constructor-2026-07-25T210311.png
security:
- kind: authentication
  name: Constructor Authentication
  slug: constructor-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Constructor Domain Security
  slug: constructor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Constructor Trust Center
  slug: constructor-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, CCPA, MACH Certified
slug: constructor
tags:
- Company
- E-Commerce
- Search
- Product Discovery
- Recommendations
- Personalization
- Retail
- Artificial Intelligence
website: https://constructor.com/
---
