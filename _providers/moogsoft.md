---
access_model:
  confidence: high
  label: Contact sales — no public pricing, no free tier, no self-service sign-up
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans/moogsoft-plans-pricing.yml
  - https://www.moogsoft.com/pricing/ (HTTP 404)
  - https://app.moogsoft.ai/ (302 to Auth0 sign-in, no registration)
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-03'
api_count: 17
apis:
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: This API enables you to retrieve and update alerts and incidents, and other APIs relating to them
  name: Moogsoft Alerts/Incidents API
  slug: alerts-incidents
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: Use Apex AIOps Incident Management API for sending/receiving alerts, events, and incidents
  name: Moogsoft Azure Application Insights API
  slug: azure-app-insights
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: This API enables you to create and manage custom endpoints for inbound integrations.
  name: Moogsoft Create Your Own Integration API
  slug: create-your-own-integration
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: API for Apex AIOps Incident Management Cloudwatch Service
  name: Moogsoft Amazon CloudWatch API
  slug: cloudwatch
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: This API enables you to work with collectors
  name: Moogsoft Collector V2 API
  slug: collector
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: This API allows you to save and retrieve config, catalogs, credentials, watchers, menu actions, and maintenance windows
  name: Moogsoft Config API
  slug: config
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: API for Apex AIOps Incident Management Events Integration.
  name: Moogsoft Events Integration API
  slug: events-integration
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: This API allows you to save and retrieve on-call schedules, escalation policies
  name: Moogsoft On-Call API
  slug: on-call
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: Rollup Service API for the Moogsoft metric processor. The published contract carries development servers (http://localhost:3030) rather than the production host; the production base is api.moogsoft.ai
  name: Moogsoft Rollup Service API
  slug: rollup-service
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: This API enables you to create metrics and manage metrics policies.
  name: Moogsoft Metrics API
  slug: metrics
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: This API enables you to create and manage Pager Duty integrations.
  name: Moogsoft PagerDuty Integration API
  slug: pagerduty
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: This API enables you to retrieve and update Probable Root Cause, and other APIs relating to them
  name: Moogsoft Probable Root Cause API
  slug: probable-root-cause
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: API for the similar incidents service.
  name: Moogsoft Similar Incidents API
  slug: similar-incidents
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: APIs for handling features requests and some UI driven queries.
  name: Moogsoft UI Services API
  slug: ui-services
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: API for User Service
  name: Moogsoft User Management API
  slug: user-management
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: You can use this API to create, retrieve, update, delete, and test webhoook integrations.
  name: Moogsoft Webhook API
  slug: webhook
- baseURL: https://api.moogsoft.ai
  baseurl_source: declared
  description: This API enables you to create and manage workflows
  name: Moogsoft Workflow Engine API
  slug: workflow-engine
artifact_total: 25
asyncapis:
- description: ''
  name: Moogsoft Webhooks
  slug: moogsoft-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.moogsoft.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.docs.moogsoft.com/docs/latest/branches/main/1sy0hr6odnj10-incident-management-api-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moogsoft.com/moogsoft-cloud/moogsoft-cloud.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.moogsoft.com/moogsoft-cloud/en/apis.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moogsoft.com/moogsoft-cloud/en/get-started-with-apis.html
- group: operate
  title: ''
  type: Support
  url: https://www.moogsoft.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.moogsoft.com/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.moogsoft.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moogsoft
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moogsoft.com/legal-information/moogsoft-cloud-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moogsoft.com/legal-information/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://app.moogsoft.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moogsoft.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/moogsoft-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moogsoft-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moogsoft-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moogsoft-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/moogsoft-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/moogsoft-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moogsoft-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/moogsoft-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/moogsoft-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moogsoft-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/moogsoft-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moogsoft-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moogsoft-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/moogsoft-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moogsoft-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/moogsoft-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moogsoft-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/moogsoft-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/moogsoft-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moogsoft-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/moogsoft-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/moogsoft-finops.yml
created: '2026-03-27'
description: 'Moogsoft is an AIOps platform for IT operations, DevOps and SRE teams that ingests events, alerts and metrics from across a hybrid estate, deduplicates and reduces noise, correlates related alerts into incidents, detects anomalies in metric streams, and surfaces probable root cause and similar past incidents so responders can act faster. Founded in 2011 by Phil Tee and Mike Silvey, Moogsoft was acquired by Dell Technologies in October 2023 and the SaaS product is now sold as Dell APEX AIOps Incident Management, while the moogsoft.com brand, documentation and API surface remain live. The platform is API-first: seventeen public OpenAPI 3.1 contracts covering alerts and incidents, configuration, catalogs, correlation definitions, maintenance windows, collectors, inbound event/metric integrations, bring-your-own integrations, on-call scheduling, outbound webhooks, workflow automation, user and API-key management are published from api.moogsoft.ai and documented on a public Stoplight
  portal at api.docs.moogsoft.com.'
finops:
- name: Moogsoft Finops
  service_category: API
  slug: moogsoft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moogsoft.png
layout: provider
modified: '2026-08-29'
name: Moogsoft
nav: Providers
network: true
overview: 'Moogsoft publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Alerts/Incidents API, Azure Application Insights API, Create Your Own Integration API, and 14 more. Tagged areas include AIOps, Incident Management, Observability, Alerting, and Event Management.


  The Moogsoft catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Moogsoft''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 29 more developer resources.'
plans:
- name: Moogsoft Plans Pricing
  plan_count: 0
  slug: moogsoft-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Moogsoft Rate Limits
  slug: moogsoft-rate-limits
score:
  band: strong
  composite: 59.0
  coverage:
    artifact_dirs: 22
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 18.2
    contract_quality: 66.7
    developer_ergonomics: 73.2
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 59.0
  provenance:
    conformance: first-party
    contracts:
      callable: 94.1
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moogsoft/refs/heads/main/screenshots/moogsoft-2026-06-20T185754.png
security:
- kind: authentication
  name: Moogsoft Authentication
  slug: moogsoft-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Moogsoft Domain Security
  slug: moogsoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Moogsoft Vulnerability Disclosure
  slug: moogsoft-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Moogsoft Trust Center
  slug: moogsoft-trust-center
  summary_line: SOC 2, GDPR, CSA STAR
slug: moogsoft
tags:
- AIOps
- Incident Management
- Observability
- Alerting
- Event Management
- Anomaly Detection
- Correlation
- On-Call
- Monitoring
- IT Operations
- DevOps
- SRE
website: https://www.moogsoft.com
---
