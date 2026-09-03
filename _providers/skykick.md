---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Partner Integration API is the SkyKick / ConnectWise Cloud Services partner-facing REST API. The provider's own Get Started page documents an OAuth 2.0 client-credentials token exchange at /auth/t
  name: SkyKick Partner Integration API
  slug: skykick-partner-integration-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skykick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.connectwise.com/platform/bcdr/cloud-backup
- group: start
  title: ''
  type: DeveloperPortal
  url: https://skykick.developer.azure-api.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://skykick.developer.azure-api.net/getstarted
- group: start
  title: ''
  type: Login
  url: https://portal.cloudservices.connectwise.com/
- group: operate
  title: ''
  type: Support
  url: https://www.connectwise.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SkyKick
- group: operate
  title: ''
  type: StatusPage
  url: https://status.connectwise.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.connectwise.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.connectwise.com/company/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.connectwise.com/company/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.connectwise.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/skykick-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/skykick-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skykick-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/skykick-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skykick-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skykick-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.connectwise.com/company/trust/compliance
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/skykick-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/skykick-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/skykick-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/skykick-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/skykick-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skykick-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skykick-llms.txt
created: '2026-08-28'
description: 'SkyKick is a Seattle-based cloud automation company whose Microsoft 365 migration, cloud backup, SaaS security and cloud automation products for managed service providers were acquired by ConnectWise in September 2024. The SkyKick brand''s own domain no longer serves a website — skykick.com answers HTTP 404 "Site Not Configured" and www.skykick.com no longer resolves — and the products now ship as ConnectWise Cloud Backup and ConnectWise SaaS Security. The SkyKick Partner Integration API is still live, on ConnectWise Cloud Services: an Azure API Management gateway at apis.cloudservices.connectwise.com, fronted by the ConnectWise Developer Portal running on SkyKick''s own APIM instance (skykick.developer.azure-api.net, also served as developers.cloudservices.connectwise.com). Authentication is OAuth 2.0 client credentials plus an Azure APIM subscription key. The API reference itself is gated: developer access must be provisioned by an administrator inside the Cloud Services
  partner portal, so no OpenAPI, AsyncAPI, MCP server or agent card is published anonymously.'
image: https://avatars.githubusercontent.com/u/15131071?v=4
layout: provider
modified: '2026-08-28'
name: SkyKick
nav: Providers
network: true
overview: 'SkyKick publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Backup, Migration, Microsoft-365, and Managed Service Providers.


  SkyKick''s developer surface includes getting-started guide, support, pricing, authentication, and 22 more developer resources.'
plans:
- name: Skykick Plans Pricing
  plan_count: 0
  slug: skykick-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Skykick Rate Limits
  slug: skykick-rate-limits
scopes:
- name: Skykick Scopes
  scope_count: 0
  slug: skykick-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 29.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skykick/refs/heads/main/screenshots/skykick-2026-09-02T155808.png
security:
- kind: authentication
  name: Skykick Authentication
  slug: skykick-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Skykick Domain Security
  slug: skykick-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Skykick Vulnerability Disclosure
  slug: skykick-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Skykick Trust Center
  slug: skykick-trust-center
  summary_line: ISO/IEC 27001:2013, ISO/IEC 27701:2019, Cloud Security Alliance STAR Level 2, SOC 2, SOC 3
slug: skykick
tags:
- Company
- Backup
- Migration
- Microsoft-365
- Managed Service Providers
- SaaS Security
- Cloud Automation
- Data Protection
- Azure API Management
website: https://www.connectwise.com/platform/bcdr/cloud-backup
---
