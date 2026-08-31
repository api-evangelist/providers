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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: General Translation Agentic Access
  operation_count: 21
  slug: general-translation-agentic-access
  summary_line: 21 operations · 16 acting
api_count: 1
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
artifact_total: 28
asyncapis:
- description: ''
  name: General Translation Webhooks
  slug: general-translation-webhooks
collections:
- collection_type: postman
  name: General Translation Branches API
  slug: postman-general-translation-branches-api
- collection_type: postman
  name: General Translation Branches Context API
  slug: postman-general-translation-context-api
- collection_type: postman
  name: General Translation Branches Files API
  slug: postman-general-translation-files-api
- collection_type: postman
  name: General Translation Branches Jobs API
  slug: postman-general-translation-jobs-api
- collection_type: postman
  name: General Translation Branches Project API
  slug: postman-general-translation-project-api
- collection_type: postman
  name: General Translation Branches Tags API
  slug: postman-general-translation-tags-api
- collection_type: postman
  name: General Branches Translation API
  slug: postman-general-translation-translation-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: General Translation Branches API
  slug: open-general-translation-branches-api
- collection_type: open
  name: General Translation Branches Context API
  slug: open-general-translation-context-api
- collection_type: open
  name: General Translation Branches Files API
  slug: open-general-translation-files-api
- collection_type: open
  name: General Translation Branches Jobs API
  slug: open-general-translation-jobs-api
- collection_type: open
  name: General Translation Branches Project API
  slug: open-general-translation-project-api
- collection_type: open
  name: General Translation Branches Tags API
  slug: open-general-translation-tags-api
- collection_type: open
  name: General Branches Translation API
  slug: open-general-translation-translation-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/general-translation-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/general-translation/overview
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
  name: General Translation MCP Server
  slug: general-translation-mcp-server
modified: '2026-07-19'
name: General Translation
nav: Providers
network: true
overview: 'General Translation publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Branches API, Context API, Files API, and 4 more. Tagged areas include Company, Internationalization, Localization, Translation, and Developer Tools.


  The General Translation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  General Translation''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 30 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 4
  name: General Translation Rate Limits
  slug: general-translation-rate-limits
score:
  band: strong
  composite: 62.6
  coverage:
    artifact_dirs: 25
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 63.0
    developer_ergonomics: 85.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 63.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- SDK
- Machine Translation
website: https://generaltranslation.com
---
