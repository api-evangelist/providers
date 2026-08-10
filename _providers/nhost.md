---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 39
  human_in_the_loop: 1
  name: Nhost Agentic Access
  operation_count: 54
  slug: nhost-agentic-access
  summary_line: 54 operations · 39 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: Instant, real-time GraphQL API auto-generated from PostgreSQL database schemas via Hasura. Supports queries, mutations, and live subscriptions with row- and column-level role-based access control.
  name: Nhost GraphQL API
  slug: nhost-graphql-api
- description: Deploy JavaScript and TypeScript serverless functions as HTTP API endpoints for webhooks, event triggers, and custom backend logic. Each file in the functions directory becomes an endpoint, auto-deplo
  name: Nhost Serverless Functions API
  slug: nhost-serverless-functions-api
- description: AI toolkit providing GraphQL-based assistant management, auto-embeddings, session handling, and file stores. Enables developers to turn any Nhost project into an agentic service with built-in vector s
  name: Nhost AI API
  slug: nhost-ai-api
- description: User authentication operations including sign-in, sign-up, and various authentication methods (email/password, passwordless, OAuth, WebAuthn, MFA)
  name: Nhost authentication API
  slug: nhost-authentication-api
- description: API documentation
  name: Nhost documentation API
  slug: nhost-documentation-api
- description: These operations are not intended to be used directly by clients and should be excluded from client SDKs
  name: Nhost excludeme API
  slug: nhost-excludeme-api
- description: File management operations
  name: Nhost files API
  slug: nhost-files-api
- description: Administrative operations
  name: Nhost operations API
  slug: nhost-operations-api
- description: Security-related operations including Personal Access Tokens, WebAuthn management, account elevation, and account linking
  name: Nhost security API
  slug: nhost-security-api
- description: Session management operations including token refresh, verification, and sign-out
  name: Nhost session API
  slug: nhost-session-api
- description: Storage operations and presigned URLs
  name: Nhost storage API
  slug: nhost-storage-api
- description: System operations including health checks, service version, and public key endpoints
  name: Nhost system API
  slug: nhost-system-api
- description: User profile and account management operations including email/password changes, MFA configuration, and profile updates
  name: Nhost user API
  slug: nhost-user-api
- description: Email and ticket verification operations for confirming user actions
  name: Nhost verification API
  slug: nhost-verification-api
artifact_total: 31
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nhost-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nhost-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nhost-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nhost-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nhost-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://nhost.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nhost.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nhost
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nhost
- group: company
  title: ''
  type: Blog
  url: https://nhost.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://nhost.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nhost.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/nhost
- group: commercial
  title: ''
  type: Plans
  url: plans/nhost-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nhost-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nhost-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/nhost-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/nhost-context.jsonld
created: '2026-06-12'
description: Nhost is an open-source Firebase alternative that provides a fully managed backend platform built on PostgreSQL, GraphQL, and modern open-source tools. Developers get instant REST and GraphQL APIs auto-generated from their database schema, along with authentication supporting email/password, OAuth, magic links, WebAuthn, and one-time passwords. The platform includes S3- compatible file storage with CDN delivery and image transformation, serverless functions deployable as HTTP endpoints, and real-time GraphQL subscriptions. Nhost also offers a local development CLI, GitHub-based automated deployments, an AI toolkit with auto-embeddings and assistants, and managed container services—enabling teams to launch production-ready backends without infrastructure management.
examples:
- key_count: 4
  name: Nhost Auth Signin Example
  slug: nhost-auth-signin-example
- key_count: 4
  name: Nhost Storage Upload Example
  slug: nhost-storage-upload-example
- key_count: 4
  name: Nhost Token Refresh Example
  slug: nhost-token-refresh-example
finops:
- name: Nhost Finops
  service_category: ''
  slug: nhost-finops
graphqls:
- description: Nhost provides an instant, auto-generated GraphQL API powered by Hasura GraphQL Engine running on top of PostgreSQL. Every Nhost project receives a dedicated GraphQL endpoint at `https://{subdomain}.h
  name: Nhost GraphQL API
  slug: nhost-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nhost.png
json_schemas:
- name: ErrorResponse
  property_count: 3
  slug: nhost-error-response
- name: FileMetadata
  property_count: 10
  slug: nhost-file-metadata
- name: Session
  property_count: 5
  slug: nhost-session
jsonld:
- class_count: 14
  name: Nhost Context
  property_count: 4
  slug: nhost-context
layout: provider
modified: '2026-06-12'
name: Nhost
nav: Providers
network: true
overview: 'Nhost publishes 11 APIs on the [APIs.io](https://apis.io/) network, including authentication API, documentation API, excludeme API, and 8 more. Tagged areas include GraphQL, PostgreSQL, Authentication, File Storage, and Serverless Functions.


  The Nhost catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nhost''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Nhost Plans Pricing
  plan_count: 4
  slug: nhost-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 0
  name: Nhost Rate Limits
  slug: nhost-rate-limits
rules:
- name: Nhost API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nhost-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.1
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 67.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nhost/refs/heads/main/screenshots/nhost-2026-06-20T190311.png
security:
- kind: authentication
  name: Nhost Authentication
  slug: nhost-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Nhost Domain Security
  slug: nhost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nhost Vulnerability Disclosure
  slug: nhost-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Nhost Trust Center
  slug: nhost-trust-center
  summary_line: SOC 2, HIPAA
slug: nhost
tags:
- GraphQL
- PostgreSQL
- Authentication
- File Storage
- Serverless Functions
- Real-Time
- Open Source
- Firebase Alternative
- Backend as a Service
- BaaS
website: https://nhost.io/
---
