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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Testmail App Agentic Access
  operation_count: 2
  slug: testmail-app-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: 'Full-featured GraphQL API for querying test emails from Testmail programmable inboxes. Supports advanced filtering, custom sorting, field selection, live queries, pagination, and spam reports. Bearer '
  name: Testmail GraphQL API
  slug: testmail-graphql-api
- description: Retrieve test emails from programmable inboxes
  name: Testmail Inbox API
  slug: testmail-app-inbox-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/testmail-app-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/testmail-app-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/testmail-app-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://testmail.app
- group: docs
  title: ''
  type: Documentation
  url: https://testmail.app/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/testmail-app
- group: other
  title: ''
  type: X
  url: https://x.com/testmailapp
- group: company
  title: ''
  type: Blog
  url: https://testmail.app/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://testmail.app/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.testmail.app
- group: commercial
  title: ''
  type: Plans
  url: plans/testmail-app-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/testmail-app-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/testmail-app-finops.yml
created: '2026-06-13'
description: Testmail is an email testing API platform for developers and QA teams that provides programmable inboxes with unlimited email addresses via a namespace.tag routing scheme. It offers both a JSON REST API and a GraphQL API for instant, programmatic retrieval of test emails, supporting automated end-to-end email testing in development workflows and CI/CD pipelines. Key capabilities include wildcard tag searches, live queries, pagination, spam score testing via SpamAssassin, and attachment handling.
examples:
- key_count: 4
  name: Graphql Inbox Query
  slug: graphql-inbox-query
- key_count: 5
  name: Graphql Livequery
  slug: graphql-livequery
- key_count: 4
  name: Json Api Get Emails
  slug: json-api-get-emails
- key_count: 4
  name: Json Api Spam Report
  slug: json-api-spam-report
finops:
- name: Testmail App Finops
  service_category: ''
  slug: testmail-app-finops
graphqls:
- description: The Testmail.app GraphQL API provides a full-featured interface for querying test emails from programmable inboxes. Emails are routed to addresses in the format `{namespace}.{tag}@inbox.testmail.app`,
  name: Testmail.app GraphQL API
  slug: testmail-app-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/testmail-app.png
json_schemas:
- name: Email
  property_count: 11
  slug: email
- name: FilterInput
  property_count: 4
  slug: filter-input
- name: InboxResponse
  property_count: 6
  slug: inbox-response
jsonld:
- class_count: 6
  name: Testmail App Context
  property_count: 38
  slug: testmail-app-context
layout: provider
modified: '2026-06-13'
name: Testmail
nav: Providers
network: true
overview: 'Testmail publishes 2 APIs on the [APIs.io](https://apis.io/) network: GraphQL API and Inbox API. Tagged areas include Email Testing, Developer Tools, API Testing, GraphQL, and REST API.


  The Testmail catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Testmail''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Testmail App Plans Pricing
  plan_count: 4
  slug: testmail-app-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 5
  name: Testmail App Rate Limits
  slug: testmail-app-rate-limits
rules:
- name: Testmail API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: testmail-app-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 72.5
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/testmail-app/refs/heads/main/screenshots/testmail-app-2026-06-20T195154.png
security:
- kind: authentication
  name: Testmail App Authentication
  slug: testmail-app-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Testmail App Domain Security
  slug: testmail-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: testmail-app
tags:
- Email Testing
- Developer Tools
- API Testing
- GraphQL
- REST API
- CI/CD
- QA Automation
- Programmable Inboxes
website: https://testmail.app
---
