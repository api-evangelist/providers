---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sentry Agentic Access
  operation_count: 12
  slug: sentry-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 8
apis:
- description: 'Sentry provides official SDKs for 22+ platforms including JavaScript, Python, PHP, .NET, Java, Go, Ruby, Rust, Android, Apple, React Native, Unity, and Unreal Engine. Each SDK provides error capture, '
  name: Sentry SDK API
  slug: sentry-sdk-api
- description: 'The Sentry Integration Platform API enables building public and internal integrations with Sentry. Supports OAuth2 with PKCE, device authorization flow for CLI/CI environments, webhook notifications, '
  name: Sentry Integration Platform API
  slug: sentry-integration-platform-api
- description: Alert rules and notifications
  name: Sentry Alerts API
  slug: sentry-alerts-api
- description: Raw error events
  name: Sentry Events API
  slug: sentry-events-api
- description: Error issues and aggregated events
  name: Sentry Issues API
  slug: sentry-issues-api
- description: Organization-level resources
  name: Sentry Organizations API
  slug: sentry-organizations-api
- description: Project management
  name: Sentry Projects API
  slug: sentry-projects-api
- description: Release and deployment tracking
  name: Sentry Releases API
  slug: sentry-releases-api
arazzos:
- description: Find a high-severity unresolved issue, review its events, then escalate priority and assign an owner.
  name: Sentry Escalate and Assign an Issue
  slug: sentry-escalate-issue-workflow
- description: Confirm a project, list its issues, then drill into the top issue's detail and events.
  name: Sentry Investigate a Project's Issues
  slug: sentry-investigate-project-issues-workflow
- description: Resolve an organization, then inventory its projects, releases, and alert rules.
  name: Sentry Organization Monitoring Survey
  slug: sentry-organization-survey-workflow
- description: Create a release, then mark the noisiest unresolved issues as resolved in that next release.
  name: Sentry Resolve Issues in the Next Release
  slug: sentry-resolve-issues-in-release-workflow
- description: Idempotently record a release for a project, creating it only when it does not already exist.
  name: Sentry Track a Deployment Release
  slug: sentry-track-deployment-release-workflow
- description: Find the most relevant unresolved issue, inspect its events, then resolve or reprioritize it.
  name: Sentry Triage and Resolve an Issue
  slug: sentry-triage-issue-workflow
artifact_total: 58
asyncapis:
- description: Sentry Integration Platform delivers webhook notifications to registered integrations when events occur in Sentry. Webhooks are sent as HTTP POST requests signed with HMAC-SHA256 using the client secr
  name: Sentry Integration Platform Webhooks
  slug: sentry-webhooks-asyncapi
collections:
- collection_type: postman
  name: Sentry Error Monitoring API
  slug: postman-sentry-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sentry Error Monitoring Alerts API
  slug: open-sentry-alerts-api
- collection_type: open
  name: Sentry Error Monitoring API
  slug: open-sentry-api
- collection_type: open
  name: Sentry Error Monitoring Alerts Events API
  slug: open-sentry-events-api
- collection_type: open
  name: Sentry Error Monitoring Alerts Issues API
  slug: open-sentry-issues-api
- collection_type: open
  name: Sentry Error Monitoring Alerts Organizations API
  slug: open-sentry-organizations-api
- collection_type: open
  name: Sentry Error Monitoring Alerts Projects API
  slug: open-sentry-projects-api
- collection_type: open
  name: Sentry Error Monitoring Alerts Releases API
  slug: open-sentry-releases-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sentry-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sentry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sentry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sentry-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sentry/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-escalate-issue-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-investigate-project-issues-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-organization-survey-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-resolve-issues-in-release-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-track-deployment-release-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-triage-issue-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getsentry
- group: company
  title: ''
  type: Website
  url: https://sentry.io/
- group: start
  title: ''
  type: Portal
  url: https://docs.sentry.io/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sentry.io/api/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.sentry.io/api/auth/
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.sentry.io/api/ratelimits/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sentry.io/api/guides/create-auth-token/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sentry.io/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sentry.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sentry.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sentry.io/legal/privacy/
- group: company
  title: ''
  type: Blog
  url: https://sentry.io/blog/
- group: build
  title: ''
  type: SDKs
  url: https://docs.sentry.io/platforms/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getsentry
- group: build
  title: ''
  type: DeveloperTools
  url: https://sandbox.sentry.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://sentry.io/pricing/
- group: start
  title: ''
  type: Signup
  url: https://sentry.io/signup/
- group: start
  title: ''
  type: Login
  url: https://sentry.io/auth/login/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sentry-issue-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/sentry-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sentry-issue-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sentry-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/sentry-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.sentry.io/llms.txt
created: '2026-03-18'
description: Sentry is a developer-first application monitoring platform that helps software teams discover, triage, and prioritize errors and performance issues in production. Sentry provides real-time error monitoring, performance tracing, session replay, profiling, and release tracking for web, mobile, and backend applications across 22+ platforms and languages.
examples:
- key_count: 2
  name: Sentry Create Release Example
  slug: sentry-create-release-example
- key_count: 2
  name: Sentry List Organization Issues Example
  slug: sentry-list-organization-issues-example
- key_count: 2
  name: Sentry List Organizations Example
  slug: sentry-list-organizations-example
- key_count: 2
  name: Sentry Update Issue Example
  slug: sentry-update-issue-example
features:
- 'Developer: free with 5K errors, 5M spans, 50 replays'
- 'Team at $26/mo annual: 50K errors, 5M spans, unlimited users'
- 'Business at $80/mo: insights, anomaly detection, SAML/SCIM'
- 'Enterprise: custom retention, residency, TAM'
- Pay-as-you-go for additional volume on Team+
- 'Web API: 40 req/sec read and write per auth token'
- SDK ingest per-DSN with configurable spike protection
- OAuth 2.0 (Sentry Apps) and auth tokens
- Webhooks for issues, alerts, deployments
- 100+ language/framework SDKs
- Tracing with distributed context
- Profiling for CPU and memory
- Session Replay (web and mobile)
- Uptime and Cron monitoring
- Performance/Insights dashboards (Business+)
- AI debugging agent (Team+ add-on)
finops:
- name: Sentry Finops
  service_category: Error Monitoring
  slug: sentry-finops
graphqls:
- description: Sentry does not currently expose a public GraphQL API. Their external developer API is a REST API versioned at `/api/0/`. This directory contains a **conceptual GraphQL SDL** (`sentry-schema.graphql`)
  name: Sentry GraphQL Schema
  slug: sentry-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sentry.png
json_schemas:
- name: Sentry Issue
  property_count: 24
  slug: sentry-issue
json_structures:
- name: Sentry Issue Structure
  property_count: 0
  slug: sentry-issue-structure
jsonld:
- class_count: 25
  name: Sentry Context
  property_count: 8
  slug: sentry-context
layout: provider
modified: '2026-05-19'
name: Sentry
nav: Providers
network: true
overview: 'Sentry publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Integration Platform API, Alerts API, Events API, and 4 more. Tagged areas include Error Monitoring, Debugging, Observability, Application Performance Management, and Developer Tools.


  The Sentry catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Sentry''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, engineering blog, pricing, and 28 more developer resources.'
plans:
- name: Sentry Plans Pricing
  plan_count: 4
  slug: sentry-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 4
  name: Sentry Rate Limits
  slug: sentry-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Sentry API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 6
  slug: sentry-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Sentry API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sentry-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Sentry API Rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 7
  slug: sentry-rules
score:
  band: developing
  composite: 53.8
  delta: -9.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 28.8
    contract_quality: 71.9
    developer_ergonomics: 54.8
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 42.1
  previous_composite: 62.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sentry/refs/heads/main/screenshots/sentry-2026-06-20T193811.png
security:
- kind: authentication
  name: Sentry Authentication
  slug: sentry-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sentry Domain Security
  slug: sentry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sentry Vulnerability Disclosure
  slug: sentry-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sentry
tags:
- Error Monitoring
- Debugging
- Observability
- Application Performance Management
- Developer Tools
website: https://sentry.io/
---
