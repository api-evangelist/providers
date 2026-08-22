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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 24
  human_in_the_loop: 2
  name: Arcadia Agentic Access
  operation_count: 46
  slug: arcadia-agentic-access
  summary_line: 46 operations · 24 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: Signal provides a tariff and energy rate calculation engine that allows developers to model the cost of any energy usage scenario against North American utility tariffs. It supports cost-benefit analy
  name: Arcadia Signal API
  slug: arcadia-signal-api
- description: Switch enables rate plan optimization by identifying the best utility rate plan for a customer based on their actual usage patterns. It supports customer-facing energy plan recommendation workflows fo
  name: Arcadia Switch API
  slug: arcadia-switch-api
- description: 'The Utility Cloud API provides enterprise-grade access to Arcadia''s full energy data warehouse, enabling clients to extract structured data on business entities at scale. It supports integration with '
  name: Arcadia Utility Cloud API
  slug: arcadia-utility-cloud-api
- description: The Auth API from Arcadia — 4 operation(s) for auth.
  name: Arcadia Auth API
  slug: arcadia-auth-api
- description: The Bundle (Beta) API from Arcadia — 8 operation(s) for bundle (beta).
  name: Arcadia Bundle (Beta) API
  slug: arcadia-bundle-beta-api
- description: The Plug API from Arcadia — 5 operation(s) for plug.
  name: Arcadia Plug API
  slug: arcadia-plug-api
- description: The Spark API from Arcadia — 8 operation(s) for spark.
  name: Arcadia Spark API
  slug: arcadia-spark-api
- description: The Users API from Arcadia — 2 operation(s) for users.
  name: Arcadia Users API
  slug: arcadia-users-api
- description: The Utility Accounts API from Arcadia — 2 operation(s) for utility accounts.
  name: Arcadia Utility Accounts API
  slug: arcadia-utility-accounts-api
- description: The Utility Credentials API from Arcadia — 3 operation(s) for utility credentials.
  name: Arcadia Utility Credentials API
  slug: arcadia-utility-credentials-api
- description: The Utility Meters (Beta) API from Arcadia — 2 operation(s) for utility meters (beta).
  name: Arcadia Utility Meters (Beta) API
  slug: arcadia-utility-meters-beta-api
- description: The Webhooks API from Arcadia — 8 operation(s) for webhooks.
  name: Arcadia Webhooks API
  slug: arcadia-webhooks-api
artifact_total: 58
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Arcadia API Reference Auth API
  slug: open-arcadia-auth-api
- collection_type: open
  name: Arcadia API Reference Auth Bundle (Beta) API
  slug: open-arcadia-bundle-beta-api
- collection_type: open
  name: Arcadia API Reference Auth Plug API
  slug: open-arcadia-plug-api
- collection_type: open
  name: Arcadia API Reference Auth Spark API
  slug: open-arcadia-spark-api
- collection_type: open
  name: Arcadia API Reference Auth Users API
  slug: open-arcadia-users-api
- collection_type: open
  name: Arcadia API Reference Auth Utility Accounts API
  slug: open-arcadia-utility-accounts-api
- collection_type: open
  name: Arcadia API Reference Auth Utility Credentials API
  slug: open-arcadia-utility-credentials-api
- collection_type: open
  name: Arcadia API Reference Auth Utility Meters (Beta) API
  slug: open-arcadia-utility-meters-beta-api
- collection_type: open
  name: Arcadia API Reference Auth Webhooks API
  slug: open-arcadia-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arcadia-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/arcadia-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arcadia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arcadia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arcadia-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.arcadia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ArcadiaPower
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arcadiahq/
- group: company
  title: ''
  type: Blog
  url: https://www.arcadia.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.arcadia.com/platform
- group: operate
  title: ''
  type: StatusPage
  url: https://status.arcadia.com/
- group: other
  title: ''
  type: X
  url: https://x.com/arcadiapower
- group: commercial
  title: ''
  type: Plans
  url: plans/arcadia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/arcadia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/arcadia-finops.yml
created: '2026-06-13'
description: Arcadia is the leading clean energy data platform that provides developers and businesses with programmatic access to utility billing data, real-time energy usage, and tariff intelligence across thousands of utility providers in the United States. The Arc Connect API enables applications to collect and synchronize utility account credentials, retrieve structured billing statements, and access granular interval meter data down to 15-minute readings. Arcadia's Plug API covers more than 95% of US utility accounts, supporting use cases including energy management, carbon accounting, solar savings analysis, EV charging optimization, and community solar enrollment. The platform also offers Signal for tariff rate calculation, Switch for plan recommendations, and DataHub for warehouse-native SQL access to aggregated energy datasets.
examples:
- key_count: 5
  name: Arcadia Access Token Example
  slug: arcadia-access-token-example
- key_count: 9
  name: Arcadia Bundle Enrollment Example
  slug: arcadia-bundle-enrollment-example
- key_count: 5
  name: Arcadia Charge Cost Example
  slug: arcadia-charge-cost-example
- key_count: 6
  name: Arcadia Tariff Example
  slug: arcadia-tariff-example
- key_count: 22
  name: Arcadia Utility Account Example
  slug: arcadia-utility-account-example
- key_count: 12
  name: Arcadia Utility Credential Example
  slug: arcadia-utility-credential-example
- key_count: 7
  name: Arcadia Utility Interval Example
  slug: arcadia-utility-interval-example
- key_count: 9
  name: Arcadia Utility Meter Example
  slug: arcadia-utility-meter-example
- key_count: 26
  name: Arcadia Utility Statement Example
  slug: arcadia-utility-statement-example
- key_count: 3
  name: Arcadia Webhook Event Example
  slug: arcadia-webhook-event-example
finops:
- name: Arcadia Finops
  service_category: ''
  slug: arcadia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arcadia.png
json_schemas:
- name: BundleEnrollment
  property_count: 9
  slug: arcadia-bundle-enrollment
- name: ChargeCostResponse
  property_count: 5
  slug: arcadia-charge-cost
- name: SmartChargeScheduleResponse
  property_count: 3
  slug: arcadia-smart-charge-schedule
- name: StorageOptimizationSchedulesResponse
  property_count: 11
  slug: arcadia-storage-optimization-schedules
- name: TariffRatesResponse
  property_count: 2
  slug: arcadia-tariff-rates
- name: Tariff
  property_count: 6
  slug: arcadia-tariff
- name: User
  property_count: 3
  slug: arcadia-user
- name: UtilityAccount
  property_count: 22
  slug: arcadia-utility-account
- name: UtilityCredential
  property_count: 12
  slug: arcadia-utility-credential
- name: UtilityIntervalDataResponse
  property_count: 8
  slug: arcadia-utility-interval-data
- name: UtilityIntervalItem
  property_count: 7
  slug: arcadia-utility-interval-item
- name: UtilityMeter
  property_count: 9
  slug: arcadia-utility-meter
- name: UtilityRemittanceItem
  property_count: 10
  slug: arcadia-utility-remittance-item
- name: UtilityStatement
  property_count: 26
  slug: arcadia-utility-statement
- name: WebhookEndpoint
  property_count: 8
  slug: arcadia-webhook-endpoint
- name: WebhookEvent
  property_count: 9
  slug: arcadia-webhook-event
jsonld:
- class_count: 15
  name: Arcadia Context
  property_count: 45
  slug: arcadia-context
layout: provider
modified: '2026-06-13'
name: Arcadia
nav: Providers
network: true
overview: 'Arcadia publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Bundle (Beta) API, Plug API, and 6 more. Tagged areas include Energy, Utilities, Clean Energy, Billing Data, and Interval Data.


  The Arcadia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arcadia''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Arcadia Plans Pricing
  plan_count: 2
  slug: arcadia-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Arcadia Rate Limits
  slug: arcadia-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Arcadia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: arcadia-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.4
  delta: -1.1
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 64.0
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 37.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arcadia/refs/heads/main/screenshots/arcadia-2026-06-20T172358.png
security:
- kind: authentication
  name: Arcadia Authentication
  slug: arcadia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Arcadia Domain Security
  slug: arcadia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arcadia Vulnerability Disclosure
  slug: arcadia-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Arcadia Trust Center
  slug: arcadia-trust-center
  summary_line: SOC 2, ISO 27001
slug: arcadia
tags:
- Energy
- Utilities
- Clean Energy
- Billing Data
- Interval Data
- Carbon
- Solar
- Tariff
website: https://www.arcadia.com/
---
