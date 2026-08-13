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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Flagsmith Agentic Access
  operation_count: 35
  slug: flagsmith-agentic-access
  summary_line: 35 operations · 17 acting
api_count: 9
apis:
- description: The Flagsmith Flags API is the public-facing REST API that client-side and server-side SDKs use to retrieve feature flag values and remote configuration for environments and users. It uses a non-secre
  name: Flagsmith Flags API
  slug: flags-api
- description: Manage environments within a project. Environments represent deployment stages such as development, staging, and production.
  name: flagsmith Environments API
  slug: flagsmith-environments-api
- description: Manage feature flags within a project. Features can be toggled on or off and can have remote configuration values.
  name: flagsmith Features API
  slug: flagsmith-features-api
- description: Manage user identities within an environment. Identities represent individual users and their associated traits.
  name: flagsmith Identities API
  slug: flagsmith-identities-api
- description: Manage organisations within Flagsmith. Organisations are the top-level container for projects, users, and billing.
  name: flagsmith Organisations API
  slug: flagsmith-organisations-api
- description: Manage projects within an organisation. Projects contain environments and feature flags.
  name: flagsmith Projects API
  slug: flagsmith-projects-api
- description: Manage segments within a project. Segments define groups of users based on traits and rules for targeted flag delivery.
  name: flagsmith Segments API
  slug: flagsmith-segments-api
- description: Manage organisation users and their permissions within Flagsmith.
  name: flagsmith Users API
  slug: flagsmith-users-api
- description: Configure webhooks for environments and organisations to receive notifications about flag changes and audit log events.
  name: flagsmith Webhooks API
  slug: flagsmith-webhooks-api
artifact_total: 22
asyncapis:
- description: Flagsmith provides two types of webhooks for receiving event notifications. Environment webhooks automatically send flag evaluations for identified users whenever an identity's flags are evaluated via
  name: Flagsmith Webhook Events
  slug: flagsmith-webhooks-asyncapi
collections:
- collection_type: open
  name: Flagsmith Admin API
  slug: open-flagsmith-admin-api
- collection_type: open
  name: Flagsmith Flags API
  slug: open-flagsmith-flags-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flagsmith-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flagsmith-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flagsmith-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flagsmith
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flagsmith
- group: design
  title: ''
  type: JSONLD
  url: json-ld/flagsmith-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/flagsmith-feature-flag-schema.json
- group: company
  title: ''
  type: Blog
  url: https://flagsmith.com/blog
description: Flagsmith is an open-source feature flag and remote configuration platform that helps developers manage feature flags across web, mobile, and server-side applications.
finops:
- name: Flagsmith Finops
  service_category: API
  slug: flagsmith-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flagsmith.png
json_schemas:
- name: Flagsmith Feature Flag
  property_count: 12
  slug: flagsmith-feature-flag
jsonld:
- class_count: 0
  name: Flagsmith Context
  property_count: 9
  slug: flagsmith-context
layout: provider
modified: '2026-05-19'
name: flagsmith
nav: Providers
network: true
overview: 'flagsmith publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Flags API, Environments API, Features API, and 6 more.


  The flagsmith catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  flagsmith''s developer surface includes authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Flagsmith Plans Pricing
  plan_count: 3
  slug: flagsmith-plans-pricing
random_paper: 119
rate_limits:
- limit_count: 5
  name: Flagsmith Rate Limits
  slug: flagsmith-rate-limits
rules:
- name: flagsmith API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: flagsmith-asyncapi-spectral-rules
- name: flagsmith API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: flagsmith-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 75.4
    developer_ergonomics: 13.0
    discoverability: 50.0
    governance: 41.7
    operational_transparency: 13.2
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/screenshots/flagsmith-2026-06-20T181306.png
security:
- kind: authentication
  name: Flagsmith Authentication
  slug: flagsmith-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Flagsmith Domain Security
  slug: flagsmith-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flagsmith
---
