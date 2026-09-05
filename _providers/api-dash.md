---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Api Dash Agentic Access
  operation_count: 57
  slug: api-dash-agentic-access
  summary_line: 57 operations · 15 acting
api_count: 1
apis:
- baseURL: https://api.apidash.dev
  baseurl_source: spec
  description: API Dash is an open source AI-powered cross-platform API client built with Flutter for desktop and mobile. Supports HTTP, GraphQL, and WebSocket with code generation, folder organization, and rich res
  name: API Dash
  slug: api-dash
- baseURL: https://api.apidash.dev
  baseurl_source: declared
  description: The API Dash APIs are a free, keyless, open-source REST utility API published by foss42 alongside the API Dash client and served from the company's own host at api.apidash.dev. OpenAPI 3.1.0, 57 opera
  name: API Dash APIs
  slug: api-dash-apis
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/api-dash-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/api-dash-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/api-dash-authentication.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/foss42/apidash/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/foss42/apidash/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/foss42/apidash/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/foss42/apidash/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/foss42/apidash/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/api-dash-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apidash
- group: company
  title: ''
  type: Website
  url: https://apidash.dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/foss42
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/foss42/apidash
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/foss42/apidash#readme
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/apidash
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/foss42/apidash/blob/main/LICENSE
- group: build
  title: ''
  type: Packages
  url: packages/api-dash-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/api-dash-packages.yml
- group: design
  title: ''
  type: Components
  url: components/api-dash-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/api-dash-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/api-dash-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/api-dash-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/api-dash-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/api-dash-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/api-dash-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/api-dash-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/api-dash-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/api-dash-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/api-dash-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/api-dash-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/api-dash-plans-pricing.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/api-dash-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.apidash.dev/docs
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/foss42/apidash/blob/main/ROADMAP.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apidash.dev/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/foss42/apidash/blob/main/INSTALLATION.md
created: '2026-03-25'
description: API Dash is a beautiful AI-powered open-source cross-platform API client built with Flutter, available on Desktop (macOS, Windows, Linux) and Mobile. It provides HTTP and GraphQL request creation, response visualization, folder and collection organization, code generation for multiple languages, and support for 40+ MIME types including image, audio, and PDF preview. Developed by the foss42 organization, API Dash is a lightweight alternative to Postman and Insomnia with an active open source community.
features:
- description: Create, customize, and send HTTP and GraphQL API requests with full control over headers, parameters, body, and authentication.
  name: HTTP and GraphQL Support
- description: AI-powered features help developers work more efficiently with API requests, responses, and integration code generation.
  name: AI-Powered Integration
- description: Generate API integration code in multiple languages including JavaScript, Python, Dart, and Kotlin from any request.
  name: Code Generation
- description: Visualize API responses across 40+ MIME types including images, audio, PDFs, and JSON with built-in search functionality.
  name: Rich Response Visualization
- description: Organize API requests into folders and collections for structured API workflow management.
  name: Collections and Folders
- description: Runs natively on macOS, Windows, Linux (Intel/AMD 64-bit and ARM 64-bit), with mobile support as well.
  name: Cross-Platform
finops:
- name: Api Dash Finops
  service_category: API
  slug: api-dash-finops
graphqls:
- description: 'generated: ''2026-09-02'''
  name: API Dash and GraphQL — no GraphQL API is published
  slug: api-dash-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/api-dash.png
integrations:
- description: Built with Flutter, API Dash integrates with the Dart/Flutter ecosystem and publishes packages to pub.dev.
  name: Flutter Ecosystem
- description: Import and export OpenAPI specifications for structured API request collection management.
  name: OpenAPI
layout: provider
mcp_servers:
- description: ''
  name: API Dash MCP Server
  slug: api-dash-mcp-server
modified: '2026-09-02'
name: API Dash
nav: Providers
network: true
overview: 'API Dash publishes 2 APIs on the [APIs.io](https://apis.io/) network, including API Dash, and 1 more. Tagged areas include API Client, Open-Source, Flutter, Desktop, and Mobile.


  API Dash''s developer surface includes authentication, documentation, support, changelog, sandbox, API reference, getting-started guide, and 30 more developer resources.'
plans:
- name: Api Dash Plans Pricing
  plan_count: 0
  slug: api-dash-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Api Dash Rate Limits
  slug: api-dash-rate-limits
scopes:
- name: Api Dash Scopes
  scope_count: 0
  slug: api-dash-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 56.5
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 100.0
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/api-dash/refs/heads/main/screenshots/api-dash-2026-06-20T172202.png
security:
- kind: authentication
  name: Api Dash Authentication
  slug: api-dash-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Api Dash Domain Security
  slug: api-dash-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Api Dash Vulnerability Disclosure
  slug: api-dash-vulnerability-disclosure
  summary_line: Hackerone
slug: api-dash
tags:
- API Client
- Open-Source
- Flutter
- Desktop
- Mobile
use_cases:
- description: Test REST and GraphQL APIs with a fully featured desktop client as a lightweight alternative to Postman and Insomnia.
  name: API Testing
- description: Generate boilerplate integration code in multiple languages to accelerate API client development.
  name: API Integration Development
- description: Visually inspect and search API responses across many content types including JSON, images, and documents.
  name: API Response Inspection
website: https://apidash.dev
---
