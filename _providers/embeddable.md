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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.1
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'Server-side REST APIs for managing Embeddable deployments — mint short-lived JWT security tokens for embeds, list embeddables (dashboards), manage published versions, and read data-model schemas. All '
  name: Embeddable Public APIs
  slug: embeddable-public-apis
artifact_total: 4
common:
- group: auth
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
  title: ''
  type: LLMsTxt
  url: llms/embeddable-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/embeddable-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/embeddable-packages.yml
- group: design
  title: ''
  type: Components
  url: components/embeddable-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/embeddable-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/embeddable-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/embeddable-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.embeddable.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/embeddable-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/embeddable-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/embeddable-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/embeddable-dashboard-as-code.md
- group: auth
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
overview: 'Embeddable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Embedded Analytics, Business Intelligence, and Dashboards.


  Embeddable''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 21 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 41.4
  provenance:
    conformance: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/embeddable/refs/heads/main/screenshots/embeddable-2026-07-25T213227.png
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
