---
api_count: 2
apis:
- description: The Worksome public GraphQL API — a single POST endpoint at https://api.worksome.com/graphql exposing 87 queries and 113 mutations across 496 types. Covers hires and contracts, jobs and candidates, pr
  name: Worksome GraphQL API
  slug: graphql
- description: Worksome outbound webhooks deliver real-time notifications for 17 event types across hires and contracts, the talent pool, payment requests and invoicing. Each delivery is an HTTP POST with a JSON bod
  name: Worksome Webhooks
  slug: webhooks
artifact_total: 8
asyncapis:
- description: ''
  name: Worksome Webhooks
  slug: worksome-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/worksome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.worksome.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.worksome.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.worksome.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.worksome.com/graphql/reference/queries/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.worksome.com/graphql/
- group: auth
  title: ''
  type: Authentication
  url: authentication/worksome-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://docs.worksome.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.worksome.dk/en
- group: company
  title: ''
  type: Blog
  url: https://www.worksome.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/worksome
- group: commercial
  title: ''
  type: Pricing
  url: https://www.worksome.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.worksome.com/demo
- group: start
  title: ''
  type: Login
  url: https://use.worksome.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.worksome.com/service-specific-terms/api-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.worksome.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.worksome.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/worksome-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/worksome-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/worksome-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/worksome-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/worksome-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/worksome-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/worksome-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/worksome-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/worksome-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/worksome-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/worksome-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/worksome-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/worksome-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/worksome-data-model.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/worksome-timesheet-registration.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/worksome-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/worksome-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/worksome-webhooks.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/worksome.graphql
- group: company
  title: ''
  type: BlogRSS
  url: https://www.worksome.com/blog/rss.xml
created: '2026-09-04'
description: Worksome is a Copenhagen-headquartered external workforce platform (Freelancer Management System) used by enterprise and mid-market teams to source, contract, classify, and pay contingent workers across 150+ countries. It ships a public GraphQL API at api.worksome.com/graphql covering hires, contracts, jobs, candidates, projects, timesheets, payment requests, invoices, compliance gates and worker classification, alongside 17 HMAC-signed webhook events, an official PHP SDK, a Go CLI with 170+ operations, a Zapier app, and an early-access MCP server for AI agents.
image: https://cdn.prod.website-files.com/60a21be3147bde7a6ece004d/60e44e338953920e5aafcd66_Worksome%20Webclip.png
json_schemas:
- name: Worksome Timesheet Registration
  property_count: 0
  slug: worksome-timesheet-registration
layout: provider
modified: '2026-09-04'
name: Worksome
nav: Providers
network: true
overview: 'Worksome publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Freelancer Management System, Contingent Workforce, Human Resources, and Staffing.


  The Worksome catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Worksome''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 31 more developer resources.'
plans:
- name: Worksome Plans Pricing
  plan_count: 0
  slug: worksome-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Worksome Rate Limits
  slug: worksome-rate-limits
security:
- kind: authentication
  name: Worksome Authentication
  slug: worksome-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Worksome Domain Security
  slug: worksome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: worksome
tags:
- Company
- Freelancer Management System
- Contingent Workforce
- Human Resources
- Staffing
- Workforce Compliance
- Payments
- GraphQL
- Webhooks
- Denmark
website: https://www.worksome.com/
---
