---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 52.9
  scored_at: '2026-07-27'
api_count: 13
apis:
- description: The Apis API from Resend — 2 operation(s) for apis.
  name: Resend Apis API
  slug: resend-apis-api
- description: The Audience API from Resend — 3 operation(s) for audience.
  name: Resend Audience API
  slug: resend-audience-api
- description: Create and manage Audiences through the Resend API.
  name: Resend Audiences API
  slug: resend-audiences-api
- description: The Batch API from Resend — 1 operation(s) for batch.
  name: Resend Batch API
  slug: resend-batch-api
- description: The Broadcasts API from Resend — 2 operation(s) for broadcasts.
  name: Resend Broadcasts API
  slug: resend-broadcasts-api
- description: The Cancel API from Resend — 1 operation(s) for cancel.
  name: Resend Cancel API
  slug: resend-cancel-api
- description: Create and manage Contacts through the Resend API.
  name: Resend Contacts API
  slug: resend-contacts-api
- description: Create and manage domains through the Resend API.
  name: Resend Domains API
  slug: resend-domains-api
- description: The Email API from Resend — 3 operation(s) for email.
  name: Resend Email API
  slug: resend-email-api
- description: Start sending emails through the Resend API.
  name: Resend Emails API
  slug: resend-emails-api
- description: The Keys API from Resend — 2 operation(s) for keys.
  name: Resend Keys API
  slug: resend-keys-api
- description: The Send API from Resend — 1 operation(s) for send.
  name: Resend Send API
  slug: resend-send-api
- description: The Verify API from Resend — 1 operation(s) for verify.
  name: Resend Verify API
  slug: resend-verify-api
artifact_total: 37
asyncapis:
- description: 'AsyncAPI 2.6 description of the Resend webhook surface. Resend delivers webhook events to subscriber-configured HTTPS endpoints using Svix as the underlying delivery and signing infrastructure. Every '
  name: Resend Webhooks
  slug: resend-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/resend-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/resend-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resend-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/resend
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/resend
- group: operate
  title: ''
  type: ChangeLog
  url: https://resend.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://resend.com/blog
- group: operate
  title: ''
  type: Migrations
  url: https://resend.com/migrate
- group: other
  title: ''
  type: Customers
  url: https://resend.com/customers
- group: company
  title: ''
  type: About
  url: https://resend.com/about
- group: auth
  title: ''
  type: Security
  url: https://resend.com/security
- group: build
  title: ''
  type: Examples
  url: https://resend.com/docs/examples
- group: build
  title: ''
  type: SDKs
  url: https://resend.com/docs/sdks
- group: commercial
  title: ''
  type: Pricing
  url: https://resend.com/pricing
- group: start
  title: ''
  type: Login
  url: https://resend.com/login
- group: start
  title: ''
  type: Signup
  url: https://resend.com/signup
- group: build
  title: ''
  type: SDKs
  url: https://github.com/resend/resend-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/resend/resend-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/resend/resend-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/resend/resend-dotnet
- group: build
  title: ''
  type: CLI
  url: https://github.com/resend/resend-cli
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/resend/resend-mcp
- group: build
  title: ''
  type: Library
  url: https://github.com/resend/react-email
- group: operate
  title: ''
  type: StatusPage
  url: https://resend-status.com/
- group: operate
  title: ''
  type: RateLimits
  url: https://resend.com/docs/api-reference/introduction
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/resend/resend-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://resend.com/llms.txt
created: '2024-11-07'
description: Resend is a developer-first email API platform that simplifies sending and managing transactional and marketing emails. It provides a clean REST API with bearer token authentication, supporting email sending, domain management, API key management, audience and contact management, and broadcast campaigns. Resend offers SDKs for Node.js, Python, Go, Ruby, PHP, Java, .NET, Rust, Elixir, and more, along with a React Email library and official MCP server.
examples:
- key_count: 3
  name: Resend Create Audience Example
  slug: resend-create-audience-example
- key_count: 4
  name: Resend Send Email Example
  slug: resend-send-email-example
finops:
- name: Resend Finops
  service_category: API
  slug: resend-finops
graphqls:
- description: Resend is a developer-first email API platform for sending and managing transactional and marketing emails. Resend's public API is REST-based; this GraphQL schema is a conceptual representation derive
  name: Resend GraphQL Schema
  slug: resend-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/resend.png
json_schemas:
- name: Resend Audience
  property_count: 4
  slug: resend-audience
- name: Resend Domain
  property_count: 7
  slug: resend-domain
- name: Resend Email
  property_count: 12
  slug: resend-email
json_structures:
- name: Resend Email Structure
  property_count: 0
  slug: resend-email-structure
jsonld:
- class_count: 21
  name: Resend Context
  property_count: 0
  slug: resend-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-29'
name: Resend
nav: Providers
network: true
overview: 'Resend publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Apis API, Audience API, Audiences API, and 10 more. Tagged areas include Email, Developer Tools, Transactional Email, and Marketing Email.


  The Resend catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Resend''s developer surface includes changelog, engineering blog, code examples, pricing, signup flow, CLI, and 21 more developer resources.'
plans:
- name: Resend Plans Pricing
  plan_count: 3
  slug: resend-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Resend Rate Limits
  slug: resend-rate-limits
rules:
- name: Resend API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: resend-asyncapi-spectral-rules
- name: Resend API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: resend-jsonschema-spectral-rules
- name: Resend API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 6
  slug: resend-rules
score:
  band: strong
  composite: 64.0
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 71.7
    developer_ergonomics: 32.6
    discoverability: 87.5
    governance: 52.6
    operational_transparency: 78.9
  previous_composite: 64.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Resend Domain Security
  slug: resend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Resend Vulnerability Disclosure
  slug: resend-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Resend Trust Center
  slug: resend-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 5
skills:
- name: agent-email-inbox
  slug: agent-email-inbox
- name: email-best-practices
  slug: email-best-practices
- name: react-email
  slug: react-email
- name: resend-cli
  slug: resend-cli
- name: resend
  slug: resend
slug: resend
tags:
- Email
- Developer Tools
- Transactional Email
- Marketing Email
---
