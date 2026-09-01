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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: APIs for registering and managing connectors created with the Jitterbit Connector SDK — log in to Harmony, register a custom connector, list registered connectors, delete a connector registration, del
  name: Jitterbit Connector SDK REST API
  slug: connector-sdk-api
- description: An asynchronous REST API for retrieving API Manager log files as CSV or JSON, as an alternative to the Download as CSV button on the API Logs page. A request submits a time range, an organization ID a
  name: Jitterbit API Manager Log Service API (Beta)
  slug: api-manager-log-service-api
- description: The Login API from Jitterbit — 1 operation(s) for login.
  name: Jitterbit Login API
  slug: jitterbit-login-api
- description: The Operations API from Jitterbit — 1 operation(s) for operations.
  name: Jitterbit Operations API
  slug: jitterbit-operations-api
- description: The Projects API from Jitterbit — 4 operation(s) for projects.
  name: Jitterbit Projects API
  slug: jitterbit-projects-api
- description: The Schedules API from Jitterbit — 2 operation(s) for schedules.
  name: Jitterbit Schedules API
  slug: jitterbit-schedules-api
artifact_total: 13
asyncapis:
- description: ''
  name: Jitterbit Webhooks
  slug: jitterbit-webhooks
common:
- group: other
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
  title: ''
  type: TrustCenter
  url: security/jitterbit-trust-center.yml
- group: auth
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
  title: ''
  type: Lifecycle
  url: lifecycle/jitterbit-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/jitterbit-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jitterbit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jitterbit-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jitterbit-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jitterbit-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jitterbit-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jitterbit-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jitterbit-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/jitterbit-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/jitterbit-cli.yml
- group: design
  title: ''
  type: Components
  url: components/jitterbit-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/jitterbit-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/jitterbit-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jitterbit-llms.txt
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
overview: 'Jitterbit publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Login API, Operations API, Projects API, and 1 more. Tagged areas include API Management, Automation, Integration, iPaaS, and EDI.


  The Jitterbit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Jitterbit''s developer surface includes developer portal, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 30 more developer resources.'
plans:
- name: Jitterbit Plans Pricing
  plan_count: 7
  slug: jitterbit-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Jitterbit Rate Limits
  slug: jitterbit-rate-limits
score:
  band: strong
  composite: 62.6
  coverage:
    artifact_dirs: 24
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 56.8
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 62.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
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
- Workflow-Automation
- Connectors
website: https://www.jitterbit.com
---
