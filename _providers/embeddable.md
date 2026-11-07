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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Server-side REST APIs for managing Embeddable deployments — mint short-lived JWT security tokens for embeds, list embeddables (dashboards), manage published versions, and read data-model schemas. All '
  name: Embeddable Public APIs
  slug: embeddable-public-apis
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/embeddable/security/embeddable-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/embeddable-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://embeddable.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.embeddable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.embeddable.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.embeddable.com/deployment/embeddables-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.embeddable.com/getting-started/get-set-up/quick-start-guide
- group: company
  title: ''
  type: Blog
  url: https://embeddable.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://embeddable.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://embeddable.com/log-in
- group: operate
  title: ''
  type: Support
  url: https://join.slack.com/t/embeddablecommunity/shared_invite/zt-20b4f6s10-gULqO6riqutJcbUi_FJmZA
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/embeddable-hq
- group: auth
  title: ''
  type: Security
  url: https://embeddable.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://embeddable.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://embeddable.com/policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://embeddable.com/policies
- group: agent
  href: https://artifacts.apis.io/embeddable/llms/embeddable-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/embeddable-llms.txt
- group: build
  href: https://artifacts.apis.io/embeddable/packages/embeddable-packages.yml
  title: ''
  type: Packages
  url: packages/embeddable-packages.yml
- group: build
  href: https://artifacts.apis.io/embeddable/packages/embeddable-packages.yml
  title: ''
  type: SDKs
  url: packages/embeddable-packages.yml
- group: design
  href: https://artifacts.apis.io/embeddable/components/embeddable-components.yml
  title: ''
  type: Components
  url: components/embeddable-components.yml
- group: auth
  href: https://artifacts.apis.io/embeddable/authentication/embeddable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/embeddable-authentication.yml
- group: design
  href: https://artifacts.apis.io/embeddable/conformance/embeddable-conformance.yml
  title: ''
  type: Conformance
  url: conformance/embeddable-conformance.yml
- group: design
  href: https://artifacts.apis.io/embeddable/lifecycle/embeddable-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/embeddable-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.embeddable.com/
- group: design
  href: https://artifacts.apis.io/embeddable/conventions/embeddable-conventions.yml
  title: ''
  type: Conventions
  url: conventions/embeddable-conventions.yml
- group: operate
  href: https://artifacts.apis.io/embeddable/changelog/embeddable-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/embeddable-changelog.yml
- group: build
  href: https://artifacts.apis.io/embeddable/cli/embeddable-cli.yml
  title: ''
  type: CLI
  url: cli/embeddable-cli.yml
- group: agent
  href: https://artifacts.apis.io/embeddable/skills/embeddable-dashboard-as-code.md
  title: ''
  type: AgentSkill
  url: skills/embeddable-dashboard-as-code.md
- group: auth
  href: https://artifacts.apis.io/embeddable/security/embeddable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/embeddable-domain-security.yml
created: '2026-07-17'
description: Embeddable is a developer toolkit for building customer-facing, embedded analytics into your own application. Engineers define components, data models, and themes in code (version-controlled in their own repo), and their team assembles and publishes dashboards with either a no-code builder or directly in code. A governed semantic layer built on the open-source Cube modeling language defines metrics, dimensions, and joins once so every chart, dashboard, and AI experience reuses the same trusted definitions. Dashboards embed as native web components (no iframes) authorized with short-lived JWT security tokens, with server-side row-level security for multi-tenant isolation. Embeddable ships the Remarkable Pro React component suite, open-source component libraries, a code-first CLI workflow, and a small set of server-side REST Public APIs (tokens, embeddables, versions, schemas). The platform is SOC 2 Type II certified and GDPR compliant. Embeddable is built by the London team behind
  Trevor.io.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/embeddable.png
layout: provider
modified: '2026-07-19'
name: Embeddable
nav: Providers
network: true
overview: 'Embeddable is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Embedded Analytics, Business Intelligence, and Dashboards.


  Embeddable''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 21 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 73.2
    operational_transparency: 36.8
  previous_composite: 50.6
  provenance:
    conformance: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/concept-embeddable/embeddable-2026-07-25T213227.png
security:
- kind: authentication
  name: Embeddable Authentication
  slug: embeddable-authentication
  summary_line: http/jwt · 2 schemes
- kind: domain-security
  name: Embeddable Domain Security
  slug: embeddable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Embeddable Trust Center
  slug: embeddable-trust-center
  summary_line: SOC 2, GDPR
skill_count: 1
skills:
- name: dashboard-as-code
  slug: embeddable-dashboard-as-code
slug: embeddable
tags:
- Company
- Analytics
- Embedded Analytics
- Business Intelligence
- Dashboards
- Data Visualization
- Semantic Layer
- Developer Tools
- Software-as-a-Service
website: https://embeddable.com/
---
