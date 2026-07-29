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
    asyncapi_events: false
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
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Quay Agentic Access
  operation_count: 16
  slug: quay-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 10
apis:
- description: Manage Dockerfile builds, build logs, build triggers, and build configuration.
  name: Quay Build API
  slug: quay-build-api
- description: Inspect image manifests, manifest layers, and labels associated with a pushed image.
  name: Quay Manifest API
  slug: quay-manifest-api
- description: Manage Quay organizations, organization members, billing, application tokens, and organization-wide settings.
  name: Quay Organization API
  slug: quay-organization-api
- description: Manage user and team permissions on repositories.
  name: Quay Permission API
  slug: quay-permission-api
- description: Manage container image repositories including create, list, update, delete, visibility, descriptions, and metadata.
  name: Quay Repository API
  slug: quay-repository-api
- description: Manage robot accounts used for automated repository access including credentials and permissions.
  name: Quay Robot API
  slug: quay-robot-api
- description: Retrieve vulnerability scan results for repository images.
  name: Quay Security API
  slug: quay-security-api
- description: Manage repository image tags including listing, restoring, expiring, and deleting tags.
  name: Quay Tag API
  slug: quay-tag-api
- description: Manage organization teams, team membership, team roles, and team permissions on repositories.
  name: Quay Team API
  slug: quay-team-api
- description: Manage Quay user accounts, profile, starred repositories, and personal OAuth tokens.
  name: Quay User API
  slug: quay-user-api
artifact_total: 24
collections:
- collection_type: open
  name: Quay Container Registry API
  slug: open-quay
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quay-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/quay-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://quay.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.quay.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.quay.io/guides/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quay
- group: commercial
  title: ''
  type: Pricing
  url: https://quay.io/plans/
- group: company
  title: ''
  type: Blog
  url: https://www.redhat.com/en/blog
- group: start
  title: ''
  type: Signup
  url: https://quay.io/signin/
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/products/red-hat-quay/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/quay/quay-mcp-server
created: '2026-03-26'
description: Quay is a container image registry that enables you to build, store, distribute, and deploy container images with built-in security scanning, access controls, and automated build triggers. Available as a hosted service at Quay.io or as a self-hosted solution through Red Hat Quay.
finops:
- name: Quay Finops
  service_category: API
  slug: quay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quay.png
json_schemas:
- name: Quay Manifest Security Scan
  property_count: 2
  slug: quay-manifest-security
- name: Quay Repository
  property_count: 11
  slug: quay-repository
- name: Quay Tag
  property_count: 9
  slug: quay-tag
jsonld:
- class_count: 5
  name: Quay Context
  property_count: 2
  slug: quay-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Quay
nav: Providers
network: true
overview: 'Quay publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Build API, Manifest API, Organization API, and 7 more. Tagged areas include Container Images, Containers, Red Hat, Registry, and Security Scanning.


  The Quay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Quay''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, signup flow, support, and 6 more developer resources.'
plans:
- name: Quay Plans Pricing
  plan_count: 3
  slug: quay-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 5
  name: Quay Rate Limits
  slug: quay-rate-limits
rules:
- name: Quay API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: quay-jsonschema-spectral-rules
scopes:
- name: Quay Scopes
  scope_count: 6
  slug: quay-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 55.5
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.6
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quay/refs/heads/main/screenshots/quay-2026-06-20T192420.png
security:
- kind: authentication
  name: Quay Authentication
  slug: quay-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Quay Domain Security
  slug: quay-domain-security
  summary_line: TLSv1.3 · HSTS
slug: quay
tags:
- Container Images
- Containers
- Red Hat
- Registry
- Security Scanning
website: https://quay.io/
---
