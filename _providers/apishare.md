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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: ApiShare provides a unified catalog of APIs, applications, assets, MCP servers, and AI agents with role-based visibility, configurable lifecycle workflows, subscription management, and built-in audita
  name: ApiShare
  slug: apishare
artifact_total: 27
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apishare-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.apishare.cloud/documentation-1.12
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apishare.cloud/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.apishare.cloud/blog
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.apishare.cloud/release-note
- group: operate
  title: ''
  type: Contact
  url: https://www.apishare.cloud/contacts
created: '2025-01-08'
description: ApiShare is an API governance platform that provides a unified operational model for API lifecycle management, access control, catalog management, and asset reuse across organizations. It operates as a native component of an Internal Developer Platform, enabling self-service, standardized, and secure API governance without replacing existing systems.
features:
- description: Active catalog of APIs, applications, assets, MCP servers, and AI agents with role-based visibility.
  name: Unified API Catalog
- description: Full digital product lifecycle governance from design through retirement with version control.
  name: Lifecycle Management
- description: Configurable workflows for product lifecycle, usage approvals, and ownership management.
  name: Workflow Orchestration
- description: Structured request approval workflows with automated keyset management, key rotation, grace periods, and revocation.
  name: Subscription Management
- description: Role-based permissions and catalog visibility controls defining who can view digital products.
  name: Access Control
- description: Built-in auditability and evidence collection by design.
  name: Traceability and Audit
- description: Exposes digital products in governed, structured format for AI agent consumption.
  name: AI-Ready Architecture
- description: Interactive API testing directly from the portal with live documentation.
  name: Live API Testing
- description: AI-powered assistant for creating OpenAPI specifications.
  name: AI-Powered Agent Design Expert
- description: Public API discovery and showcase functionality for external consumers.
  name: Public Marketplace Showcase
finops:
- name: Apishare Finops
  service_category: API
  slug: apishare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apishare.png
integrations:
- description: Connector for governing APIs managed through the Boomi API Management gateway.
  name: Boomi API Management
- description: Connector for governing APIs managed through the Red Hat 3scale API gateway.
  name: Red Hat 3scale
- description: Integration with Microsoft Azure API Gateway for unified governance.
  name: Microsoft Azure API Management
- description: Connector for governing APIs managed through the Kong API gateway.
  name: Kong
- description: Identity provider integration for authentication and authorization.
  name: Microsoft Azure Entra ID
- description: Open-source identity provider integration for authentication.
  name: KeyCloak
- description: Enterprise identity provider integration for access management.
  name: Oracle Access Management
layout: provider
modified: '2026-04-19'
name: ApiShare
nav: Providers
network: true
overview: 'ApiShare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Governance, API Lifecycle, API Management, Catalog, and Governance.


  ApiShare''s developer surface includes documentation, pricing, engineering blog, release notes, and 2 more developer resources.'
plans:
- name: Apishare Plans Pricing
  plan_count: 3
  slug: apishare-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Apishare Rate Limits
  slug: apishare-rate-limits
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 19.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apishare/refs/heads/main/screenshots/apishare-2026-06-20T172257.png
security:
- kind: domain-security
  name: Apishare Domain Security
  slug: apishare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apishare
tags:
- API Governance
- API Lifecycle
- API Management
- Catalog
- Governance
- Internal Developer Platform
- Platform
use_cases:
- description: Enforce API policies, track lifecycle changes, and ensure compliance without slowing down development teams.
  name: API Governance at Scale
- description: Operate as a native governance component within an existing Internal Developer Platform.
  name: Internal Developer Platform Integration
- description: Apply governance to non-human users including AI agents consuming APIs and MCP servers.
  name: AI Agent Governance
- description: Govern APIs and digital products across multiple organizational domains with consistent policies.
  name: Multi-Domain Governance
- description: Manage consumer subscriptions, approvals, and keyset lifecycle for API access control.
  name: API Access Management
---
