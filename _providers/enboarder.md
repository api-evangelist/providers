---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: REST API for launching basic and advanced Enboarder workflows, updating and cancelling running workflows, managing employee profiles and photos, and exporting workflow and form reporting data. Paths a
  name: Enboarder REST API
  slug: enboarder-rest-api
- description: SCIM 2.0 user provisioning and management API for creating, reading, updating and deactivating Enboarder users from an identity provider. Exposes the standard discovery endpoints (/scim/v2/ServiceProv
  name: Enboarder SCIM 2.0 API
  slug: enboarder-scim-api
artifact_total: 10
asyncapis:
- description: ''
  name: Enboarder Webhooks
  slug: enboarder-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/enboarder-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://enboarder.com/legal/vulnerability/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enboarder-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/enboarder-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://enboarder.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.enboarder.com/en/collections/2404029-enboarder-api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://help.enboarder.com/en/collections/1706630-integration-information
- group: docs
  title: ''
  type: APIReference
  url: https://help.enboarder.com/en/collections/2404029-enboarder-api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://help.enboarder.com/en/articles/4151199-enboarder-api-docs-authentication-overview
- group: operate
  title: ''
  type: Support
  url: https://help.enboarder.com/en/
- group: company
  title: ''
  type: Blog
  url: https://enboarder.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enboarder
- group: commercial
  title: ''
  type: Pricing
  url: https://enboarder.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://enboarder.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://enboarder.com/legal/privacy/
- group: auth
  title: ''
  type: Trust
  url: https://enboarder.com/trust/
- group: auth
  title: ''
  type: Compliance
  url: https://enboarder.com/legal/security/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enboarder-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/enboarder-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/enboarder-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/enboarder-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/enboarder-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/enboarder-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/enboarder-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/enboarder-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/enboarder-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enboarder-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/enboarder-plans-pricing.yml
created: '2026-08-12'
description: Enboarder is an employee onboarding and people-activation platform used by HR teams, managers and IT to design, automate and measure personalized employee journeys across preboarding, onboarding, compliance, internal transitions, offboarding and enablement. It exposes a regional REST API for launching, updating, cancelling and reporting on workflows, managing employee profiles and exporting form data, a SCIM 2.0 endpoint for user provisioning, and an outbound Webhook module that posts configurable JSON payloads to downstream systems such as Slack, Jira and ServiceNow. API access is region-scoped across Australia, the EU, the United States and Canada, and is authenticated with either an account API key or OAuth 2.0 client credentials.
image: https://enboarder.com/wp-content/uploads/og-home.jpg
layout: provider
modified: '2026-08-12'
name: Enboarder
nav: Providers
network: true
overview: 'Enboarder publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, Employee Onboarding, Employee Experience, and HR Technology.


  The Enboarder catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Enboarder''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 21 more developer resources.'
plans:
- name: Enboarder Plans Pricing
  plan_count: 0
  slug: enboarder-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 0
  name: Enboarder Rate Limits
  slug: enboarder-rate-limits
scopes:
- name: Enboarder Scopes
  scope_count: 3
  slug: enboarder-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 45.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 23.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Enboarder Authentication
  slug: enboarder-authentication
  summary_line: apiKey/oauth2/http · 4 schemes
- kind: domain-security
  name: Enboarder Domain Security
  slug: enboarder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Enboarder Vulnerability Disclosure
  slug: enboarder-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Enboarder Trust Center
  slug: enboarder-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, GDPR, CCPA
slug: enboarder
tags:
- Company
- Human Resources
- Employee Onboarding
- Employee Experience
- HR Technology
- Workflow Automation
- SCIM
- Identity Provisioning
- Webhooks
- Offboarding
website: https://enboarder.com/
---
