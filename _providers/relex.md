---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: 'The RELEX Data API is the near-real-time REST interface for exchanging master data, transactional data and customer-specific custom resources between a customer''s ERP, POS, WMS or MDM systems and the '
  name: RELEX Data API
  slug: relex-data-api
- description: 'The RELEX Monitoring API lets customers observe the status of their own RELEX environments programmatically: file ingestion events, planning job events, environment inventory and platform metrics. It '
  name: RELEX Monitoring API
  slug: relex-monitoring-api
artifact_total: 10
asyncapis:
- description: ''
  name: Relex Data Api Webhooks
  slug: relex-data-api-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/relex-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/relex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/relex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.relexsolutions.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.relexsolutions.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.relexsolutions.com/integrations/
- group: docs
  title: ''
  type: APIReference
  url: https://www.relexsolutions.com/api/retail-restapi-example-customer.html
- group: operate
  title: ''
  type: Support
  url: https://www.relexsolutions.com/customer-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.relexsolutions.com/community-portal/
- group: company
  title: ''
  type: Blog
  url: https://www.relexsolutions.com/careers/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/relex
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.relexsolutions.com/policy/terms-of-use-website/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.relexsolutions.com/policy/privacy-policy-relex-website/
- group: auth
  title: ''
  type: Compliance
  url: https://www.relexsolutions.com/security-compliance/
- group: auth
  title: ''
  type: Security
  url: https://www.relexsolutions.com/policy/vulnerability-disclosure/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.relexsolutions.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/relex-data-api-openapi.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/relex-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/relex-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/relex-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/relex-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/relex-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/relex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/relex-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/relex-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/relex-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/relex-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/relex-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/relex-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/relex-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/relex-data-api-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/relex-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/relex-packages.yml
created: '2026-08-26'
description: 'RELEX Solutions is a Helsinki-headquartered supply chain and retail planning software company whose unified platform covers demand forecasting, inventory and replenishment, space and assortment, pricing and promotions, workforce and store operations, and integrated business planning for retailers, wholesalers and consumer goods manufacturers. Its developer surface is deliberately narrow and integration-centric: customer data reaches the platform through the RELEX Data API (an OpenAPI 3.1 REST contract with 91 operations across master data, transactions, metadata and customer-specific custom resources), a Batch API over Azure Blob Storage or SFTP, a bi-directional SAP Connector, and Snowflake data sharing, while operational visibility is exposed through the RELEX Monitoring API for file and job events. Both APIs are secured with OAuth 2.0 client credentials against RELEX Identity, publish RFC 7807 problem responses, and are documented publicly as ReDoc reference pages, while
  the full RELEX Developer Portal at docs.relexsolutions.com sits behind an Auth0 login.'
image: https://s32519.pcdn.co/wp-content/uploads/2024/01/RELEX-logo-1200x627-social.png
layout: provider
modified: '2026-08-26'
name: RELEX Solutions
nav: Providers
network: true
overview: 'RELEX Solutions publishes 2 APIs on the [APIs.io](https://apis.io/) network: RELEX Data API and RELEX Monitoring API. Tagged areas include Supply Chain, Retail, Demand Planning, Inventory Management, and Forecasting.


  The RELEX Solutions catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  RELEX Solutions'' developer surface includes documentation, API reference, support, engineering blog, authentication, sandbox, and 28 more developer resources.'
plans:
- name: Relex Plans Pricing
  plan_count: 0
  slug: relex-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Relex Rate Limits
  slug: relex-rate-limits
scopes:
- name: Relex Scopes
  scope_count: 51
  slug: relex-scopes
  summary_line: 51 scopes
score:
  band: strong
  composite: 54.3
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 30.3
    contract_quality: 67.5
    developer_ergonomics: 49.4
    discoverability: 79.6
    governance: 30.3
    operational_transparency: 65.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Relex Authentication
  slug: relex-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Relex Domain Security
  slug: relex-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Relex Vulnerability Disclosure
  slug: relex-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Relex Trust Center
  slug: relex-trust-center
  summary_line: ISO/IEC 27001:2013, SOC 2 (ISAE 3000), GDPR
slug: relex
tags:
- Supply Chain
- Retail
- Demand Planning
- Inventory Management
- Forecasting
- Pricing
- Enterprise Software
- Data Integration
- Company
website: https://www.relexsolutions.com/
---
