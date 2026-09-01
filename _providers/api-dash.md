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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: API Dash is an open source AI-powered cross-platform API client built with Flutter for desktop and mobile. Supports HTTP, GraphQL, and WebSocket with code generation, folder organization, and rich res
  name: API Dash
  slug: api-dash
artifact_total: 15
common:
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
- group: agent
  title: ''
  type: LlmsText
  url: https://apidash.dev/llms.txt
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
- description: ''
  name: API Dash GraphQL API
  slug: api-dash-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/api-dash.png
layout: provider
modified: '2026-04-19'
name: API Dash
nav: Providers
network: true
overview: 'API Dash publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Client, Open-Source, Flutter, Desktop, and Mobile.


  API Dash''s developer surface includes documentation, support, and 12 more developer resources.'
plans:
- name: Api Dash Plans Pricing
  plan_count: 3
  slug: api-dash-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Api Dash Rate Limits
  slug: api-dash-rate-limits
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 28.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/api-dash/refs/heads/main/screenshots/api-dash-2026-06-20T172202.png
security:
- kind: domain-security
  name: Api Dash Domain Security
  slug: api-dash-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
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
