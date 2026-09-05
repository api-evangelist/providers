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
  - sandbox
  trial: false
  try_now: false
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
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://eu.rest.relexsolutions.com
  baseurl_source: declared
  description: Endpoints for managing and retrieving customer-specific environment configurations.
  name: RELEX Solutions Environments API
  slug: relex-environments-api
- baseURL: https://eu.rest.relexsolutions.com
  baseurl_source: declared
  description: Endpoints for fetching files and jobs event data.
  name: RELEX Solutions Events API
  slug: relex-events-api
- baseURL: https://eu.rest.relexsolutions.com
  baseurl_source: declared
  description: Endpoint that report on the Monitoring API operational and readiness status.
  name: RELEX Solutions Health API
  slug: relex-health-api
- baseURL: https://eu.rest.relexsolutions.com
  baseurl_source: declared
  description: The namespace for master data contains the different endpoints for transferring master data.
  name: RELEX Solutions Master data API
  slug: relex-master-data-api
- baseURL: https://eu.rest.relexsolutions.com
  baseurl_source: declared
  description: The namespace for metadata contains the different endpoints for API metadata.
  name: RELEX Solutions Metadata API
  slug: relex-metadata-api
- baseURL: https://eu.rest.relexsolutions.com
  baseurl_source: declared
  description: The Monitoring API exposes a Prometheus-compatible metrics endpoint at `/api/v1/{customer_id}/metrics`. The metrics available over this endpoint give quantitative insight into the throughput, latency,
  name: RELEX Solutions Metrics API
  slug: relex-metrics-api
- baseURL: https://eu.rest.relexsolutions.com
  baseurl_source: declared
  description: The namespace for transaction data contains the different endpoints for inventory transactions, balance and open order information.
  name: RELEX Solutions Transactions API
  slug: relex-transactions-api
artifact_total: 15
asyncapis:
- description: ''
  name: Relex Data Api Webhooks
  slug: relex-data-api-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/relex-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/relex-data-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/relex-monitoring-api-overlay.yaml
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
overview: 'RELEX Solutions publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Environments API, Events API, Health API, and 4 more. Tagged areas include Supply Chain, Retail, Demand Planning, Inventory Management, and Forecasting.


  The RELEX Solutions catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  RELEX Solutions'' developer surface includes documentation, API reference, support, engineering blog, authentication, sandbox, and 31 more developer resources.'
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
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 65.7
    developer_ergonomics: 49.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 51.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/relex/refs/heads/main/screenshots/relex-2026-09-02T153336.png
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
