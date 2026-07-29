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
    agent_skills: true
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Supabase Agentic Access
  operation_count: 78
  slug: supabase-agentic-access
  summary_line: 78 operations · 49 acting
api_count: 21
apis:
- description: 'The Supabase Realtime API provides WebSocket-based subscriptions for real-time data changes from PostgreSQL databases. It supports three channel types: database change events (INSERT/UPDATE/DELETE on '
  name: Supabase Realtime API
  slug: realtime-api
- description: Administrative endpoints for managing users. Requires service_role key.
  name: Supabase Admin API
  slug: supabase-admin-api
- description: User signup, signin, and token management endpoints.
  name: Supabase Authentication API
  slug: supabase-authentication-api
- description: Manage storage buckets that organize files and folders. Buckets can be public or private and have configurable file size limits and allowed MIME types.
  name: Supabase Buckets API
  slug: supabase-buckets-api
- description: Server configuration and settings endpoints.
  name: Supabase Configuration API
  slug: supabase-configuration-api
- description: Manage database configurations, migrations, and extensions.
  name: Supabase Database API
  slug: supabase-database-api
- description: Configure custom domains and vanity subdomains for projects.
  name: Supabase Domains API
  slug: supabase-domains-api
- description: Deploy and manage Edge Functions for serverless compute at the edge.
  name: Supabase Functions API
  slug: supabase-functions-api
- description: Invoke deployed Edge Functions via HTTP requests. Each function is accessible at its own URL path based on its slug.
  name: Supabase Invocation API
  slug: supabase-invocation-api
- description: Multi-factor authentication enrollment and verification endpoints.
  name: Supabase MFA API
  slug: supabase-mfa-api
- description: Manage network restrictions, bans, and SSL enforcement.
  name: Supabase Network API
  slug: supabase-network-api
- description: OAuth social login provider endpoints.
  name: Supabase OAuth API
  slug: supabase-oauth-api
- description: Upload, download, move, copy, and delete files within storage buckets.
  name: Supabase Objects API
  slug: supabase-objects-api
- description: Manage organizations including membership, billing, and settings.
  name: Supabase Organizations API
  slug: supabase-organizations-api
- description: Manage Supabase projects including creation, configuration, pausing, restoring, and deletion.
  name: Supabase Projects API
  slug: supabase-projects-api
- description: Serve and transform stored files including image resizing and format conversion.
  name: Supabase Rendering API
  slug: supabase-rendering-api
- description: Invoke PostgreSQL functions via remote procedure calls.
  name: Supabase RPC API
  slug: supabase-rpc-api
- description: Manage project secrets used by Edge Functions and other services.
  name: Supabase Secrets API
  slug: supabase-secrets-api
- description: SAML-based single sign-on endpoints.
  name: Supabase SSO API
  slug: supabase-sso-api
- description: CRUD operations on database tables. Paths are auto-generated based on your database schema.
  name: Supabase Tables API
  slug: supabase-tables-api
- description: Endpoints for managing the currently authenticated user profile.
  name: Supabase User Management API
  slug: supabase-user-management-api
artifact_total: 64
asyncapis:
- description: 'The Supabase Realtime API enables real-time communication over WebSocket connections using the Phoenix Channel protocol (v2). It supports three main features: Postgres Changes for subscribing to INSER'
  name: Supabase Realtime API
  slug: supabase-realtime-api-asyncapi
collections:
- collection_type: open
  name: Supabase Auth API
  slug: open-supabase-auth-api
- collection_type: open
  name: Supabase Database REST API
  slug: open-supabase-database-rest-api
- collection_type: open
  name: Supabase Edge Functions API
  slug: open-supabase-edge-functions-api
- collection_type: open
  name: Supabase Management API
  slug: open-supabase-management-api
- collection_type: open
  name: Supabase Storage API
  slug: open-supabase-storage-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/supabase-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/supabase-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/supabase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supabase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/supabase-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/supabase
- group: company
  title: ''
  type: Website
  url: https://supabase.com
- group: docs
  title: ''
  type: Documentation
  url: https://supabase.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/supabase
- group: operate
  title: ''
  type: StatusPage
  url: https://status.supabase.com
- group: commercial
  title: ''
  type: Pricing
  url: https://supabase.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://supabase.com/blog
- group: operate
  title: ''
  type: Community
  url: https://github.com/supabase/supabase/discussions
- group: other
  title: ''
  type: X
  url: https://twitter.com/supabase
- group: agent
  title: ''
  type: MCPServer
  url: https://supabase.com/blog/remote-mcp-server
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/supabase/agent-skills
created: '2026-05-02'
description: Supabase is an open-source Firebase alternative that provides a suite of backend services built on top of PostgreSQL. It offers a managed PostgreSQL database with auto-generated REST and GraphQL APIs via PostgREST, real-time data subscriptions via WebSockets, user authentication with JWT (GoTrue), file storage with S3-compatible object storage, edge compute via globally distributed TypeScript functions on the Deno runtime, and a management API for programmatic control of projects and organizations. Supabase is available as a fully managed cloud service (app.supabase.com) and as a self-hosted open-source deployment.
examples:
- key_count: 4
  name: Supabase List Projects Example
  slug: supabase-list-projects-example
- key_count: 4
  name: Supabase Select Rows Example
  slug: supabase-select-rows-example
- key_count: 4
  name: Supabase Sign Up Example
  slug: supabase-sign-up-example
features:
- Hosted Postgres (1 GB Free, 8 GB Pro included)
- PostgREST auto-generated REST API over your schema
- Realtime API for Postgres replication and presence
- Auth (email/password, OAuth, magic links, SAML SSO)
- Storage (S3-compatible object store with policies)
- Edge Functions (Deno-based, 500k free invocations)
- Vector embeddings via pgvector
- 'Free tier: 2 projects, auto-pause after 7 days'
- Pro at $25/mo + usage (8GB DB, 100GB storage, 100k MAU)
- Team at $599/mo with SOC 2, SSO, 14-day backups
- Enterprise with HIPAA, BAA, dedicated infra
- Storage overage $0.021/GB; egress $0.09/GB; MAU $0.00325 each
- Extra micro compute add-on at $10/month
- 'Auth signup rate limits: 30/hr Free, 150/hr Pro'
- 'Realtime: 200 concurrent (Free), 500 (Pro)'
- Read replicas, branching, and Vault add-ons
finops:
- name: Supabase Finops
  service_category: Backend Platform
  slug: supabase-finops
graphqls:
- description: ''
  name: Supabase GraphQL API
  slug: supabase-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/supabase.png
json_schemas:
- name: Supabase Project
  property_count: 12
  slug: supabase-project
json_structures:
- name: Supabase Project Structure
  property_count: 0
  slug: supabase-project-structure
jsonld:
- class_count: 0
  name: Supabase Context
  property_count: 9
  slug: supabase-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Supabase
nav: Providers
network: true
overview: 'Supabase publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Realtime API, Admin API, Authentication API, and 18 more. Tagged areas include Backend As A Service, PostgreSQL, Open Source, Authentication, and Real Time.


  The Supabase catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Supabase''s developer surface includes authentication, documentation, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Supabase Plans Pricing
  plan_count: 4
  slug: supabase-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 8
  name: Supabase Rate Limits
  slug: supabase-rate-limits
rules:
- name: Supabase API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: supabase-asyncapi-spectral-rules
- name: Supabase API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: supabase-jsonschema-spectral-rules
- name: Supabase API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 8
  slug: supabase-rules
score:
  band: developing
  composite: 55.7
  delta: -3.3
  facets:
    commercial_clarity: 57.9
    contract_quality: 75.5
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 41.7
    operational_transparency: 52.6
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/supabase/refs/heads/main/screenshots/supabase-2026-06-20T194707.png
security:
- kind: authentication
  name: Supabase Authentication
  slug: supabase-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Supabase Domain Security
  slug: supabase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Supabase Vulnerability Disclosure
  slug: supabase-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Supabase Trust Center
  slug: supabase-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
skill_count: 2
skills:
- name: supabase-postgres-best-practices
  slug: supabase-postgres-best-practices
- name: supabase
  slug: supabase
slug: supabase
tags:
- Backend As A Service
- PostgreSQL
- Open Source
- Authentication
- Real Time
- Storage
- Edge Functions
- Database
website: https://supabase.com
---
