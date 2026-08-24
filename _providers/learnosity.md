---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 12
apis:
- description: Server-side JSON API for the Learnosity platform. Endpoint families cover Item bank content (Items, Questions, Features, Activities, Tags, Pools, Templates, Workflows), learner sessions and responses,
  name: Learnosity Data API
  slug: data-api
- description: Client-side JavaScript API that renders and runs an assessment from an Activity in the Item bank, handling navigation, save and resume, response storage and submission.
  name: Learnosity Items API
  slug: items-api
- description: The assessment player layer used by Items API in assess rendering mode, drivable directly for bespoke player experiences.
  name: Learnosity Assess API
  slug: assess-api
- description: Renders individual Questions and Features inline without the surrounding assessment player - the lowest-level Learnosity rendering component.
  name: Learnosity Questions API
  slug: questions-api
- description: Full embeddable authoring environment for browsing, creating and editing Items, Questions, Features and Activities in the Item bank.
  name: Learnosity Author API
  slug: author-api
- description: The single-Question editing widget, embeddable on its own inside a custom authoring UI.
  name: Learnosity Question Editor API
  slug: question-editor-api
- description: Renders prebuilt learner and aggregate reports - individual reports, live progress and learner-centric reports - into the host application.
  name: Learnosity Reports API
  slug: reports-api
- description: Real-time client-side event channel used for live progress monitoring across in-flight assessment sessions.
  name: Learnosity Events API
  slug: events-api
- description: Adds annotation and markup capability - highlighting, notes - over assessment content.
  name: Learnosity Annotations API
  slug: annotations-api
- description: Embeddable manual grading UI for scoring learner responses.
  name: Learnosity Grading API
  slug: grading-api
- description: AI-assisted authoring component for generating and improving assessment content inside the host product.
  name: Learnosity Author Aide API
  slug: author-aide-api
- description: Embeddable AI scoring and feedback surface for open-response work, exposed through feedbackSession and feedbackSessionUI configuration.
  name: Learnosity Feedback Aide
  slug: feedback-aide
artifact_total: 18
common:
- group: start
  title: ''
  type: Portal
  url: https://help.learnosity.com/hc/en-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.learnosity.com/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://help.learnosity.com/hc/en-us/categories/16266193425053-Developer-Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://help.learnosity.com/hc/en-us/categories/16266193425053-Developer-Documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://help.learnosity.com/hc/en-us/articles/360000758637-Getting-Started-With-the-Data-API
- group: operate
  title: ''
  type: Support
  url: https://learnosity.com/platform/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.learnosity.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://learnosity.com/edtech-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://learnosity.com/edtech-blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Learnosity
- group: commercial
  title: ''
  type: Pricing
  url: https://learnosity.com/licenses/
- group: start
  title: ''
  type: SignUp
  url: https://learnosity.com/contact-sales/
- group: start
  title: ''
  type: Login
  url: https://console.learnosity.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://learnosity.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://learnosity.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://learnosity.com/
- group: company
  title: ''
  type: Partners
  url: https://learnosity.com/company/partners/
- group: start
  title: ''
  type: Demos
  url: https://demos.learnosity.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.learnosity.com
- group: operate
  title: ''
  type: Deprecation
  url: https://help.learnosity.com/hc/en-us/articles/360001268538-Release-Cadence-and-Version-Lifecycle
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.learnosity.com/hc/en-us/articles/19629981258653-Developer-Release-Logs
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/learnosity-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/learnosity-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/learnosity-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/learnosity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/learnosity-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/learnosity-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/learnosity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/learnosity-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/learnosity-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/learnosity-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/learnosity-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/learnosity-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://learnosity.com/platform/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/learnosity-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://learnosity.com/product-security-policy/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/learnosity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/learnosity-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/learnosity-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/learnosity-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/learnosity-mcp.yml
created: '2026-07-17'
description: 'Learnosity is an Irish-founded assessment infrastructure company whose APIs are embedded into other companies'' learning products rather than sold as a finished platform. The surface is split in two: a family of versioned client-side JavaScript APIs - Items, Assess, Questions, Question Editor, Author, Author Aide, Annotations, Events, Reports, Grading, Rubric Editor and Feedback Aide - that render assessment, authoring, grading and reporting experiences inside a host application, and a server-side Data API for Item bank content, learner sessions, responses, scoring, jobs, reports and consumer administration. Learnosity is explicitly not a REST API: every Data API call is an HTTP POST whose operation is chosen by an `action` parameter, and every request across every API carries an HMAC-SHA256 signed `security` object generated server-side by one of six official SDKs. Versions ship on a dated Long Term Support train (vYYYY.X.LTS) pinned in the URL, with regional endpoints in
  Virginia, Dublin, Sydney, California and Oregon.'
image: https://learnosity.com/images/learnosity_logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Learnosity MCP Server
  slug: learnosity-mcp-server
modified: '2026-07-19'
name: Learnosity
nav: Providers
network: true
overview: 'Learnosity publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Assessment, EdTech, Learning, and Analytics.


  Learnosity''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 34 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 15
  name: Learnosity Rate Limits
  slug: learnosity-rate-limits
score:
  band: developing
  composite: 53.9
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 1.4
    developer_ergonomics: 71.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 84.2
  previous_composite: 53.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 66.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/learnosity/refs/heads/main/screenshots/learnosity-2026-07-25T224755.png
security:
- kind: authentication
  name: Learnosity Authentication
  slug: learnosity-authentication
  summary_line: custom-hmac-signature · 1 scheme
- kind: domain-security
  name: Learnosity Domain Security
  slug: learnosity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Learnosity Vulnerability Disclosure
  slug: learnosity-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Learnosity Trust Center
  slug: learnosity-trust-center
  summary_line: ISO 27001, CSA STAR, EU-U.S. Data Privacy Framework (incl. UK Extension and Swiss-U.S. DPF)
slug: learnosity
tags:
- Education
- Assessment
- EdTech
- Learning
- Analytics
- Content Authoring
- Artificial Intelligence
- Accessibility
- Company
website: https://learnosity.com/
---
