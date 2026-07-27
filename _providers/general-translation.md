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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 81.7
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: General Translation Agentic Access
  operation_count: 21
  slug: general-translation-agentic-access
  summary_line: 21 operations · 16 acting
api_count: 7
apis:
- description: Read and create project branches.
  name: General Translation Branches API
  slug: general-translation-branches-api
- description: Generate translation context such as glossaries and instructions.
  name: General Translation Context API
  slug: general-translation-context-api
- description: Upload, download, publish, move, and inspect project files.
  name: General Translation Files API
  slug: general-translation-files-api
- description: Read background job status.
  name: General Translation Jobs API
  slug: general-translation-jobs-api
- description: Read and update project information.
  name: General Translation Project API
  slug: general-translation-project-api
- description: Tag file versions.
  name: General Translation Tags API
  slug: general-translation-tags-api
- description: Translate content at runtime and queue files for translation.
  name: General Translation Translation API
  slug: general-translation-translation-api
artifact_total: 13
asyncapis:
- description: ''
  name: General Translation Webhooks
  slug: general-translation-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://generaltranslation.com/en-US/docs
- group: docs
  title: ''
  type: Documentation
  url: https://generaltranslation.com/en-US/docs
- group: docs
  title: ''
  type: APIReference
  url: https://generaltranslation.com/en-US/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://generaltranslation.com/en-US/docs/cli/quickstart
- group: company
  title: ''
  type: Blog
  url: https://generaltranslation.com/en-US/blog
- group: operate
  title: ''
  type: Support
  url: https://generaltranslation.com/discord
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/generaltranslation
- group: commercial
  title: ''
  type: Pricing
  url: https://generaltranslation.com/en-US/pricing
- group: start
  title: ''
  type: SignUp
  url: https://generaltranslation.com/en-US/dashboard
- group: start
  title: ''
  type: Login
  url: https://dash.generaltranslation.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://generaltranslation.com/en-US/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://generaltranslation.com/en-US/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://generaltranslation.com
- group: operate
  title: ''
  type: StatusPage
  url: https://gt-status.com
- group: build
  title: ''
  type: Packages
  url: packages/general-translation-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/general-translation-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/general-translation-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/general-translation-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/general-translation-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/general-translation-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/general-translation-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/general-translation-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/general-translation-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/general-translation-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/general-translation-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/general-translation-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/general-translation-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/general-translation-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/general-translation-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/general-translation-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://generaltranslation.com/en-US/pricing
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/general-translation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/general-translation-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/general-translation-well-known.yml
created: '2026-07-17'
description: General Translation is an end-to-end internationalization (i18n) and localization platform for developers, backed by a16z. It combines open-source i18n libraries for React, Next.js, React Native, Node.js, and Python with an AI-powered translation API, a context platform (glossaries and translation instructions), and Locadex, an AI coding agent that internationalizes source code and opens pull requests. The public REST API (api2.gtx.dev, plus the runtime host runtime2.gtx.dev) uploads source files, queues and downloads translations, manages branches and tags, reads project and job status, and translates content at runtime. It is used by developer-first teams including Cursor, Windsurf, Ramp, Mintlify, and ClickHouse.
image: https://avatars.githubusercontent.com/u/153253056?v=4
layout: provider
mcp_servers:
- description: ''
  name: general-translation-mcp.yml
  slug: general-translation-mcpyml
modified: '2026-07-19'
name: General Translation
nav: Providers
network: true
overview: 'General Translation publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Branches API, Context API, Files API, and 4 more. Tagged areas include Company, Internationalization, Localization, Translation, and Developer Tools.


  The General Translation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  General Translation''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 28 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 0
  name: General Translation Rate Limits
  slug: general-translation-rate-limits
score:
  band: strong
  composite: 60.8
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 68.3
    developer_ergonomics: 87.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 60.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/general-translation/refs/heads/main/screenshots/general-translation-2026-07-25T215549.png
security:
- kind: authentication
  name: General Translation Authentication
  slug: general-translation-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: General Translation Domain Security
  slug: general-translation-domain-security
  summary_line: TLSv1.3
slug: general-translation
tags:
- Company
- Internationalization
- Localization
- Translation
- Developer Tools
- Artificial Intelligence
- i18n
- SDKs
- Machine Translation
website: https://generaltranslation.com
---
