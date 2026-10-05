---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.jitterbit.com/harmony/pricing/
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Jitterbit Agentic Access
  operation_count: 19
  slug: jitterbit-agentic-access
  summary_line: 19 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: APIs for registering and managing connectors created with the Jitterbit Connector SDK — log in to Harmony, register a custom connector, list registered connectors, delete a connector registration, del
  name: Jitterbit Connector SDK REST API
  slug: connector-sdk-api
- description: An asynchronous REST API for retrieving API Manager log files as CSV or JSON, as an alternative to the Download as CSV button on the API Logs page. A request submits a time range, an organization ID a
  name: Jitterbit API Manager Log Service API (Beta)
  slug: api-manager-log-service-api
- baseURL: https://harmony-api.na-east.jitterbit.com/{endpoint}
  baseurl_source: declared
  description: The Login API from Jitterbit — 1 operation(s) for login.
  name: Jitterbit Login API
  phrasing_intents:
  - id: authenticate
    intent: Log in and get a Harmony auth token
    question: How do I get an auth token for the Jitterbit Harmony API with my username and password?
  - id: convertAuthtokenToJwt
    intent: Exchange an auth token for a JWT
    question: Can I turn my Harmony auth token into a JSON Web Token?
  phrasing_ops: 2
  slug: jitterbit-login-api
- baseURL: https://harmony-api.na-east.jitterbit.com/{endpoint}
  baseurl_source: declared
  description: The Operations API from Jitterbit — 1 operation(s) for operations.
  name: Jitterbit Operations API
  phrasing_intents:
  - id: getOperationLogDetails
    intent: Get log details for one operation run
    question: How do I see the log details for a single execution of an Integration Studio operation?
  - id: getOperationLogs
    intent: List operation logs for an organization
    question: Where can I retrieve the operation logs across my Harmony organization?
  phrasing_ops: 2
  slug: jitterbit-operations-api
- baseURL: https://harmony-api.na-east.jitterbit.com/{endpoint}
  baseurl_source: declared
  description: The Projects API from Jitterbit — 4 operation(s) for projects.
  name: Jitterbit Projects API
  phrasing_intents:
  - id: getProject
    intent: Get an Integration Studio project
    question: How do I retrieve the details of an Integration Studio project by its GUID?
  - id: deployProject
    intent: Deploy an Integration Studio project
    question: How do I deploy an Integration Studio project so its changes go live?
  - id: createProject
    intent: Create a new Integration Studio project
    question: Can I create a brand-new Integration Studio project through the Jitterbit API?
  - id: deleteProject
    intent: Delete an Integration Studio project
    question: Can I permanently delete an Integration Studio project I no longer need?
  - id: projectVariablesGet
    intent: List a project's variables
    question: Which project variables are defined on my Integration Studio project?
  - id: projectVariablesSet
    intent: Set the value of a project variable
    question: Can I change a project variable's value or description through the API?
  - id: exportProject
    intent: Export a project to a JSON file
    question: How do I export an Integration Studio project as a JSON file?
  - id: importProject
    intent: Import an exported project into an environment
    question: Can I import a previously exported project file into another environment?
  phrasing_ops: 10
  slug: jitterbit-projects-api
- baseURL: https://harmony-api.na-east.jitterbit.com/{endpoint}
  baseurl_source: declared
  description: The Schedules API from Jitterbit — 2 operation(s) for schedules.
  name: Jitterbit Schedules API
  phrasing_intents:
  - id: getSchedules
    intent: List a project's operation schedules
    question: How do I see all the operation schedules set up for an Integration Studio project?
  - id: updateSchedule
    intent: Update an existing operation schedule
    question: Can I change the timing of an operation schedule that already exists?
  - id: createSchedule
    intent: Create an operation schedule for a project
    question: Can I create a new schedule so my Jitterbit operations run automatically?
  - id: deleteSchedules
    intent: Delete an operation schedule
    question: How do I permanently remove an operation schedule from an environment?
  - id: enableDisableSchedule
    intent: Turn an operation schedule on or off
    question: Can I pause a schedule without deleting it?
  phrasing_ops: 5
  slug: jitterbit-schedules-api
artifact_total: 15
asyncapis:
- description: ''
  name: Jitterbit Webhooks
  slug: jitterbit-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/agentic-access/jitterbit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jitterbit-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/finops/jitterbit-finops.yml
  title: ''
  type: FinOps
  url: finops/jitterbit-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/rules/jitterbit-rules.yml
  title: ''
  type: Spectral
  url: rules/jitterbit-rules.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/hosts/jitterbit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jitterbit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/vendors/jitterbit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jitterbit-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/packages/jitterbit-packages.yml
  title: ''
  type: SDKs
  url: packages/jitterbit-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.jitterbit.com/security/
- group: company
  title: ''
  type: Newsroom
  url: http://www.jitterbit.com/company/news
- group: other
  title: ''
  type: Leadership
  url: https://www.jitterbit.com/leadership/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/overlays/jitterbit-harmony-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jitterbit-harmony-platform-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.jitterbit.com
- group: start
  title: ''
  type: Portal
  url: https://developer.jitterbit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.jitterbit.com/developer-portal/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jitterbit.com/developer-portal/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.jitterbit.com/harmony-platform-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jitterbit.com/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://www.jitterbit.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jitterbit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jitterbit
- group: operate
  title: ''
  type: Support
  url: https://www.jitterbit.com/support-services/
- group: operate
  title: ''
  type: Community
  url: https://community.jitterbit.com/s/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jitterbit.com/harmony/pricing/
- group: start
  title: ''
  type: Login
  url: https://login.jitterbit.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jitterbit.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jitterbit.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.jitterbit.com/getting-started/jitterbit-security/iso-certification/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/security/jitterbit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/jitterbit-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/security/jitterbit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jitterbit-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.jitterbit.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.jitterbit.com/release-notes/end-of-life-policy/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/lifecycle/jitterbit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jitterbit-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/changelog/jitterbit-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/jitterbit-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/authentication/jitterbit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jitterbit-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/conventions/jitterbit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jitterbit-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/conformance/jitterbit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jitterbit-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/errors/jitterbit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jitterbit-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/rate-limits/jitterbit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jitterbit-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/plans/jitterbit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jitterbit-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/data-model/jitterbit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jitterbit-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/packages/jitterbit-packages.yml
  title: ''
  type: Packages
  url: packages/jitterbit-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/cli/jitterbit-cli.yml
  title: ''
  type: CLI
  url: cli/jitterbit-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/components/jitterbit-components.yml
  title: ''
  type: Components
  url: components/jitterbit-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/sandbox/jitterbit-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/jitterbit-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/asyncapi/jitterbit-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jitterbit-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-03-16'
description: Jitterbit is an enterprise integration platform as a service (iPaaS) vendor. Its Harmony platform spans application and data integration (Integration Studio and the legacy Design Studio), full API management (API Manager with a Jitterbit-hosted cloud API gateway and an installable private gateway), EDI with AS2 and X12/EDIFACT trading-partner management, low-code application development (App Builder, formerly Vinyl), a multi-tenant Message Queue service, a connector marketplace, and an AI layer of agents, assistants and a Model Context Protocol offering. Jitterbit publishes one machine-readable contract of its own — the Harmony platform APIs, an OpenAPI 3.0.3 document covering Integration Studio projects, project variables, operation logs and schedules — alongside a prose-documented Connector SDK REST API and an asynchronous API log service. The developer surface includes a Java Connector SDK with Javadocs, a Connector Builder, downloadable recipes and process templates, and
  the jbcli command line tool.
finops:
- name: Jitterbit Finops
  service_category: API
  slug: jitterbit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jitterbit.png
layout: provider
modified: '2026-08-27'
name: Jitterbit
nav: Providers
network: true
overview: 'Jitterbit publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Login API, Operations API, Projects API, and 3 more. Tagged areas include API Management, Automation, Integration, iPaaS, and EDI.


  The Jitterbit catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Jitterbit''s developer surface includes developer portal, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 38 more developer resources.'
plans:
- name: Jitterbit Plans Pricing
  plan_count: 7
  slug: jitterbit-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Jitterbit Rate Limits
  slug: jitterbit-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Jitterbit API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: jitterbit-rules
score:
  band: exemplar
  composite: 74.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.9
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 57.6
    developer_ergonomics: 80.4
    discoverability: 76.8
    operational_transparency: 92.1
  previous_composite: 70.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/jitterbit/refs/heads/main/screenshots/jitterbit-2026-06-20T183742.png
security:
- kind: authentication
  name: Jitterbit Authentication
  slug: jitterbit-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Jitterbit Domain Security
  slug: jitterbit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Jitterbit Trust Center
  slug: jitterbit-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR
slug: jitterbit
tags:
- API Management
- Automation
- Integration
- iPaaS
- EDI
- Low-Code
- Enterprise
- API Gateway
- Workflow Automation
- Connectors
website: https://www.jitterbit.com
---
