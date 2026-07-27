---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 72.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 419
  human_in_the_loop: 12
  name: Socotra Agentic Access
  operation_count: 722
  slug: socotra-agentic-access
  summary_line: 722 operations · 419 acting · 12 human-in-the-loop
api_count: 18
apis:
- description: The Auth API from Socotra — 41 operation(s) for auth.
  name: Socotra Auth API
  slug: socotra-auth-api
- description: The Auxdata API from Socotra — 16 operation(s) for auxdata.
  name: Socotra Auxdata API
  slug: socotra-auxdata-api
- description: The Billing API from Socotra — 124 operation(s) for billing.
  name: Socotra Billing API
  slug: socotra-billing-api
- description: The Business Stats API from Socotra — 16 operation(s) for business stats.
  name: Socotra Business Stats API
  slug: socotra-business-stats-api
- description: The Claim API from Socotra — 23 operation(s) for claim.
  name: Socotra Claim API
  slug: socotra-claim-api
- description: The Compliance API from Socotra — 4 operation(s) for compliance.
  name: Socotra Compliance API
  slug: socotra-compliance-api
- description: The Config API from Socotra — 19 operation(s) for config.
  name: Socotra Config API
  slug: socotra-config-api
- description: The Contact API from Socotra — 7 operation(s) for contact.
  name: Socotra Contact API
  slug: socotra-contact-api
- description: The Document API from Socotra — 28 operation(s) for document.
  name: Socotra Document API
  slug: socotra-document-api
- description: The Event API from Socotra — 18 operation(s) for event.
  name: Socotra Event API
  slug: socotra-event-api
- description: The Migration API from Socotra — 12 operation(s) for migration.
  name: Socotra Migration API
  slug: socotra-migration-api
- description: The Payment Execution API from Socotra — 5 operation(s) for payment execution.
  name: Socotra Payment Execution API
  slug: socotra-payment-execution-api
- description: The Plugin API from Socotra — 5 operation(s) for plugin.
  name: Socotra Plugin API
  slug: socotra-plugin-api
- description: The Policy API from Socotra — 180 operation(s) for policy.
  name: Socotra Policy API
  slug: socotra-policy-api
- description: The Producers API from Socotra — 31 operation(s) for producers.
  name: Socotra Producers API
  slug: socotra-producers-api
- description: The Resource API from Socotra — 33 operation(s) for resource.
  name: Socotra Resource API
  slug: socotra-resource-api
- description: The Search API from Socotra — 4 operation(s) for search.
  name: Socotra Search API
  slug: socotra-search-api
- description: The Work Management API from Socotra — 39 operation(s) for work management.
  name: Socotra Work Management API
  slug: socotra-work-management-api
artifact_total: 24
asyncapis:
- description: ''
  name: Socotra Webhooks
  slug: socotra-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/socotra-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/socotra-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/socotra-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://socotra.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.socotra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.socotra.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.socotra.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.socotra.com/getting-started/introduction-to-socotra
- group: company
  title: ''
  type: Blog
  url: https://www.socotra.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.socotra.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.socotra.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.socotra.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.socotra.com/other-resources/release-notes
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.socotra.com/other-resources/deprecations
- group: auth
  title: ''
  type: Compliance
  url: https://trust.socotra.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/socotra-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/socotra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/socotra-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/socotra-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/socotra-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/socotra-openapi-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/socotra-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/socotra-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/socotra-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/socotra-conformance.yml
- group: build
  title: ''
  type: CLI
  url: cli/socotra-cli.yml
- group: design
  title: ''
  type: Components
  url: components/socotra-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/socotra-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/socotra-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/socotra-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/socotra-changelog.yml
created: '2026-07-17'
description: Socotra is a cloud-native insurance core platform that lets carriers, MGAs, and program administrators configure, launch, and operate insurance products across any line, geography, or distribution channel. Its Connected Core / Insurance Suite exposes a broad REST API covering business accounts, accounts and contacts, quotes and quick quotes, policy management and transactions, billing, invoicing and payments, claims (FNOL), producer management, work management, documents, accounting, reporting, search, moratoriums, configuration, and an event/webhook system. The platform ships first-party npm SDKs and CLIs, a schema-driven React UI SDK, a hosted Model Context Protocol (MCP) server for AI agents, and per-tenant configuration deployment. Backed by 8VC and Insight Partners. This profile was enriched by the API Evangelist pipeline from Socotra's public developer surface.
image: https://www.socotra.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: socotra-mcp.yml
  slug: socotra-mcpyml
modified: '2026-07-21'
name: Socotra
nav: Providers
network: true
overview: 'Socotra publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Auxdata API, Billing API, and 15 more. Tagged areas include Company, Insurtech, Insurance, Core Platform, and Policy Administration.


  The Socotra catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Socotra''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 25 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 52.3
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 44.4
    developer_ergonomics: 87.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 52.3
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Socotra Authentication
  slug: socotra-authentication
  summary_line: http/oauth2/openIdConnect/saml · 3 schemes
- kind: domain-security
  name: Socotra Domain Security
  slug: socotra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Socotra Trust Center
  slug: socotra-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27001 Statement of Applicability, SOC 1, HIPAA, GDPR, CCPA, CPRA, AWS Qualified Software
slug: socotra
tags:
- Company
- Insurtech
- Insurance
- Core Platform
- Policy Administration
- Billing
- Claims
- Underwriting
- API
- MCP
website: https://socotra.com
---
