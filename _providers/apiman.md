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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 76
  human_in_the_loop: 2
  name: Apiman Agentic Access
  operation_count: 177
  slug: apiman-agentic-access
  summary_line: 177 operations · 76 acting · 2 human-in-the-loop
api_count: 16
apis:
- description: Apiman is an open source API management platform with a developer portal, API gateway, and management UI supporting policies, plans, organizations, multi-tenancy, and extensible Java-based plugin arch
  name: Apiman
  slug: apiman
- description: The Actions API from Apiman — 2 operation(s) for actions.
  name: Apiman Actions API
  slug: apiman-actions-api
- description: The Blobs API from Apiman — 2 operation(s) for blobs.
  name: Apiman Blobs API
  slug: apiman-blobs-api
- description: The Developers API from Apiman — 8 operation(s) for developers.
  name: Apiman Developers API
  slug: apiman-developers-api
- description: The Devportal API from Apiman — 22 operation(s) for devportal.
  name: Apiman Devportal API
  slug: apiman-devportal-api
- description: The Downloads API from Apiman — 1 operation(s) for downloads.
  name: Apiman Downloads API
  slug: apiman-downloads-api
- description: The Events API from Apiman — 1 operation(s) for events.
  name: Apiman Events API
  slug: apiman-events-api
- description: The Experimental API from Apiman — 22 operation(s) for experimental.
  name: Apiman Experimental API
  slug: apiman-experimental-api
- description: The Gateways API from Apiman — 3 operation(s) for gateways.
  name: Apiman Gateways API
  slug: apiman-gateways-api
- description: The Organizations API from Apiman — 57 operation(s) for organizations.
  name: Apiman Organizations API
  slug: apiman-organizations-api
- description: The Plugins API from Apiman — 5 operation(s) for plugins.
  name: Apiman Plugins API
  slug: apiman-plugins-api
- description: The Policy Definitions API from Apiman — 2 operation(s) for policy definitions.
  name: Apiman Policy Definitions API
  slug: apiman-policy-definitions-api
- description: The Roles API from Apiman — 2 operation(s) for roles.
  name: Apiman Roles API
  slug: apiman-roles-api
- description: The Search API from Apiman — 7 operation(s) for search.
  name: Apiman Search API
  slug: apiman-search-api
- description: The System API from Apiman — 3 operation(s) for system.
  name: Apiman System API
  slug: apiman-system-api
- description: The Users API from Apiman — 13 operation(s) for users.
  name: Apiman Users API
  slug: apiman-users-api
artifact_total: 43
collections:
- collection_type: open
  name: API Manager REST API
  slug: open-apiman
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apiman-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apiman-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apiman.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.apiman.io/api-manager/latest/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apiman
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apiman/apiman
- group: company
  title: ''
  type: Blog
  url: https://www.apiman.io/blog
created: '2026-03-25'
description: Apiman is an open source API management platform featuring a REST API, manager UI, and standalone developer portal with multi-tenancy, events, notifications, permissions, and approval workflows. It provides extensible API gateway capabilities through a simple Java plugin architecture with support for policies, plans, organizations, and client management.
examples:
- key_count: 8
  name: Apiman Api Example
  slug: apiman-api-example
- key_count: 7
  name: Apiman Plan Example
  slug: apiman-plan-example
features:
- description: Full REST API for managing organizations, APIs, plans, clients, and policies programmatically.
  name: REST API Manager
- description: Extensible API gateway that enforces policies at runtime for authentication, rate limiting, and transformation.
  name: API Gateway
- description: Standalone developer portal for API discovery, documentation, and self-service subscription management.
  name: Developer Portal
- description: Pluggable Java-based policy engine supporting rate limiting, quotas, IP whitelisting, authentication, and custom policies.
  name: Policy Engine
- description: Organization-based multi-tenancy allowing separate API management namespaces within a single platform.
  name: Multi-Tenancy
- description: Configurable approval workflows for API subscriptions with notification and event support.
  name: Approval Workflows
finops:
- name: Apiman Finops
  service_category: API
  slug: apiman-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apiman.png
json_schemas:
- name: Apiman API
  property_count: 8
  slug: apiman-api
- name: Apiman Plan
  property_count: 7
  slug: apiman-plan
json_structures:
- name: Apiman Api Structure
  property_count: 8
  slug: apiman-api-structure
- name: Apiman Plan Structure
  property_count: 7
  slug: apiman-plan-structure
jsonld:
- class_count: 11
  name: Apiman Context
  property_count: 1
  slug: apiman-context
layout: provider
modified: '2026-04-19'
name: Apiman
nav: Providers
network: true
overview: 'Apiman publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Blobs API, Developers API, and 12 more. Tagged areas include API Gateway, API Management, Developer Portal, Java, and Open Source.


  The Apiman catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apiman''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Apiman Plans Pricing
  plan_count: 3
  slug: apiman-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 5
  name: Apiman Rate Limits
  slug: apiman-rate-limits
rules:
- name: Apiman API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apiman-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.5
  delta: -4.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.5
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apiman/refs/heads/main/screenshots/apiman-2026-06-20T172245.png
security:
- kind: domain-security
  name: Apiman Domain Security
  slug: apiman-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apiman
solutions:
- description: Free, Apache-licensed API management platform deployable on any JVM-based infrastructure.
  name: Open Source
- description: High-performance async API gateway implementation using Eclipse Vert.x.
  name: Vert.x Gateway
- description: Apiman overlay for WildFly/EAP application server deployments.
  name: WildFly Overlay
tags:
- API Gateway
- API Management
- Developer Portal
- Java
- Open Source
use_cases:
- description: Deploy Apiman on-premise to manage APIs across internal services with full control over infrastructure.
  name: On-Premise API Management
- description: Provide developers with a self-service portal for discovering and subscribing to APIs.
  name: Developer Portal Hosting
- description: Enforce security, rate limiting, and transformation policies on API traffic through the gateway.
  name: API Policy Enforcement
- description: Use organizations and plans to provide isolated API management environments for multiple teams.
  name: Multi-Team API Governance
website: https://www.apiman.io
---
