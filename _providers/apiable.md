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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Apiable provides a self-service API portal platform for API product managers and developers. It offers single-tenant dedicated portals with custom domains, automated API documentation with try-out fun
  name: Apiable API Portal Platform
  slug: api-portal-platform
artifact_total: 17
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/apiable-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apiable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apiable.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apiable.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.apiable.io/resources
created: '2025-01-08'
description: Apiable is an API portal platform that enables businesses to create single-tenant, white-label developer portals with custom domains, branding, and API product management. It supports API monetization, developer self-service onboarding, usage metrics, subscription lifecycle management, and integrates with API gateways including Amazon API Gateway and Kong.
features:
- description: Single-tenant dedicated portals with custom domains, branding, logos, and CSS whitelabeling.
  name: API Portal Generation
- description: Bundle APIs into products and plans with monetization options and subscription lifecycle management.
  name: API Product Management
- description: Automatically generate API documentation from specs with interactive try-out functionality and code samples.
  name: Auto-Generated API Documentation
- description: Self-service account creation, API subscription, and credential generation for developers.
  name: Developer Self-Service Onboarding
- description: Real-time API consumption tracking and usage dashboards for developers and administrators.
  name: Usage Metrics and Dashboards
- description: Team access control with role-based permissions and shared API credential management.
  name: Role-Based Access Control
- description: Deploy analytics and tracking tags via Google Tag Manager integration in developer portals.
  name: Google Tag Manager Integration
finops:
- name: Apiable Finops
  service_category: API
  slug: apiable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apiable.png
layout: provider
modified: '2026-04-19'
name: Apiable
nav: Providers
network: true
overview: 'Apiable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Amazon API Gateway, API Gateway, API Monetization, API Portal, and Developer Experience.


  Apiable''s developer surface includes pricing, engineering blog, and 3 more developer resources.'
plans:
- name: Apiable Plans Pricing
  plan_count: 3
  slug: apiable-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Apiable Rate Limits
  slug: apiable-rate-limits
score:
  band: emerging
  composite: 14.2
  delta: -7.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 22.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/screenshots/apiable-2026-06-20T172223.png
security:
- kind: domain-security
  name: Apiable Domain Security
  slug: apiable-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Apiable Trust Center
  slug: apiable-trust-center
  summary_line: ISO 27001, GDPR
slug: apiable
tags:
- Amazon API Gateway
- API Gateway
- API Monetization
- API Portal
- Developer Experience
- Developer Portal
- Kong
- Platform
- Self-Service
use_cases:
- description: Streamline partner API access with self-service portals and automated credential provisioning.
  name: Partner API Onboarding
- description: Implement usage-based billing and subscription plans for API product revenue generation.
  name: API Product Monetization
- description: Create branded developer portals where consumers can discover, subscribe to, and manage API access independently.
  name: Developer Self-Service Portals
- description: Scale API adoption by reducing onboarding friction through self-service workflows and automated access management.
  name: API Adoption Scaling
website: https://www.apiable.io/
---
