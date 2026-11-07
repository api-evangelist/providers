---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: General Translation Agentic Access
  operation_count: 21
  slug: general-translation-agentic-access
  summary_line: 21 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api2.gtx.dev
  baseurl_source: declared
  description: Generate translation context such as glossaries and instructions.
  name: General Translation Context API
  slug: general-translation-context-api
- baseURL: https://api2.gtx.dev
  baseurl_source: declared
  description: Upload, download, publish, move, and inspect project files.
  name: General Translation Files API
  slug: general-translation-files-api
- baseURL: https://api2.gtx.dev
  baseurl_source: declared
  description: Read and update project information.
  name: General Translation Project API
  slug: general-translation-project-api
- baseURL: https://api2.gtx.dev
  baseurl_source: declared
  description: Translate content at runtime and queue files for translation.
  name: General Translation API
  slug: general-translation-translation-api
- baseURL: https://api2.gtx.dev
  baseurl_source: declared
  description: Manage context groups, glossary terms, custom prompts, and project assignments.
  name: General Translation Context Management API
  slug: general-translation-context-management-api
artifact_total: 30
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
- group: commercial
  href: https://artifacts.apis.io/general-translation/plans/general-translation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/general-translation-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://generaltranslation.com/rss.xml
- group: other
  href: https://artifacts.apis.io/general-translation/overlays/general-translation-openapi-overlay.yaml
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
  href: https://artifacts.apis.io/general-translation/packages/general-translation-packages.yml
  title: ''
  type: Packages
  url: packages/general-translation-packages.yml
- group: build
  href: https://artifacts.apis.io/general-translation/packages/general-translation-packages.yml
  title: ''
  type: SDKs
  url: packages/general-translation-packages.yml
- group: build
  href: https://artifacts.apis.io/general-translation/cli/general-translation-cli.yml
  title: ''
  type: CLI
  url: cli/general-translation-cli.yml
- group: agent
  href: https://artifacts.apis.io/general-translation/mcp/general-translation-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/general-translation-mcp.yml
- group: agent
  href: https://artifacts.apis.io/general-translation/llms/general-translation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/general-translation-llms.txt
- group: agent
  href: https://artifacts.apis.io/general-translation/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/general-translation/authentication/general-translation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/general-translation-authentication.yml
- group: design
  href: https://artifacts.apis.io/general-translation/conventions/general-translation-conventions.yml
  title: ''
  type: Conventions
  url: conventions/general-translation-conventions.yml
- group: operate
  href: https://artifacts.apis.io/general-translation/rate-limits/general-translation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/general-translation-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/general-translation/errors/general-translation-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/general-translation-problem-types.yml
- group: design
  href: https://artifacts.apis.io/general-translation/lifecycle/general-translation-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/general-translation-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/general-translation/changelog/general-translation-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/general-translation-changelog.yml
- group: start
  href: https://artifacts.apis.io/general-translation/sandbox/general-translation-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/general-translation-sandbox.yml
- group: design
  href: https://artifacts.apis.io/general-translation/components/general-translation-components.yml
  title: ''
  type: Components
  url: components/general-translation-components.yml
- group: design
  href: https://artifacts.apis.io/general-translation/data-model/general-translation-data-model.yml
  title: ''
  type: DataModel
  url: data-model/general-translation-data-model.yml
- group: design
  href: https://artifacts.apis.io/general-translation/asyncapi/general-translation-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/general-translation-webhooks.yml
- group: design
  href: https://artifacts.apis.io/general-translation/conformance/general-translation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/general-translation-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://generaltranslation.com/en-US/pricing
- group: agent
  href: https://artifacts.apis.io/general-translation/agentic-access/general-translation-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/general-translation-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/general-translation/security/general-translation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/general-translation-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/general-translation/well-known/general-translation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/general-translation-well-known.yml
created: '2026-07-17'
description: General Translation is an end-to-end internationalization (i18n) and localization platform for developers, backed by a16z. It combines open-source i18n libraries for React, Next.js, React Native, Node.js, and Python with an AI-powered translation API, a context platform (glossaries and translation instructions), and Locadex, an AI coding agent that internationalizes source code and opens pull requests. The public REST API (api2.gtx.dev, plus the runtime host runtime2.gtx.dev) uploads source files, queues and downloads translations, manages branches and tags, reads project and job status, and translates content at runtime. It is used by developer-first teams including Cursor, Windsurf, Ramp, Mintlify, and ClickHouse.
finops:
- has_sources: true
  method: derived
  name: General Translation Finops
  primary_unit: subscription
  service_category: ''
  slug: general-translation-finops
  template: false
image: https://avatars.githubusercontent.com/u/153253056?v=4
layout: provider
modified: '2026-10-06'
name: General Translation
nav: Providers
network: true
overview: 'General Translation publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Context API, Files API, Project API, and 2 more. Tagged areas include Company, Internationalization, Localization, Translation, and Developer Tools.


  The General Translation catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  General Translation''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 32 more developer resources.'
plans:
- name: General Translation Plans Pricing
  plan_count: 2
  slug: general-translation-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: General Translation Rate Limits
  slug: general-translation-rate-limits
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: General Translation API Rules
  rule_count: 70
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 7
  slug: general-translation-rules
score:
  band: exemplar
  composite: 76.0
  coverage:
    artifact_dirs: 33
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 61.7
    developer_ergonomics: 81.5
    discoverability: 73.2
    operational_transparency: 73.7
  previous_composite: 75.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 38.5
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/general-translation/general-translation-2026-07-25T215549.png
security:
- kind: authentication
  name: General Translation Authentication
  slug: general-translation-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: General Translation Domain Security
  slug: general-translation-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: Generate translation context for a project
  slug: general-translation-generate-context
- name: Translate content at runtime
  slug: general-translation-runtime-translate
- name: Translate a project's source files
  slug: general-translation-translate-files
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
