---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Envia Agentic Access
  operation_count: 71
  slug: envia-agentic-access
  summary_line: 71 operations · 26 acting
api_count: 3
apis:
- baseURL: https://geocodes.envia.com/
  baseurl_source: declared
  description: Validate zip codes and locate cities for accurate address information
  name: Envia.com Address Validation API
  slug: envia-address-validation-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: Look up carrier branches by country and filters
  name: Envia.com Branches API
  slug: envia-branches-api
- baseURL: https://api-test.envia.com
  baseurl_source: declared
  description: Cancel shipments and request refunds
  name: Envia.com Cancel API
  slug: envia-cancel-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: Get available carriers by country
  name: Envia.com Carriers API
  slug: envia-carriers-api
- baseURL: https://api-test.envia.com
  baseurl_source: declared
  description: The Commercial Invoice API from Envia.com — 2 operation(s) for commercial invoice.
  name: Envia.com Commercial Invoice API
  slug: envia-commercial-invoice-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: The Company API from Envia.com — 1 operation(s) for company.
  name: Envia.com Company API
  slug: envia-company-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: The Configuration API from Envia.com — 4 operation(s) for configuration.
  name: Envia.com Configuration API
  slug: envia-configuration-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: Get country information and exchange rates
  name: Envia.com Countries API
  slug: envia-countries-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: Single-courier availability lookups (by country/shipment type)
  name: Envia.com Courier API
  slug: envia-courier-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: Get available services by carrier and country
  name: Envia.com Courier Services API
  slug: envia-courier-services-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: Brazil DC-e (Declaração de Conteúdo Eletrônica) management operations
  name: Envia.com DC E API
  slug: envia-dc-e-api
- baseURL: https://api-test.envia.com
  baseurl_source: declared
  description: Create shipping labels and generate tracking numbers
  name: Envia.com Labels API
  slug: envia-labels-api
- baseURL: https://api-test.envia.com
  baseurl_source: declared
  description: The Manifest API from Envia.com — 1 operation(s) for manifest.
  name: Envia.com Manifest API
  slug: envia-manifest-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: The NDR (India) API from Envia.com — 3 operation(s) for ndr (india).
  name: Envia.com NDR (India) API
  slug: envia-ndr-india-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: The Notifications API from Envia.com — 1 operation(s) for notifications.
  name: Envia.com Notifications API
  slug: envia-notifications-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: The Orders API from Envia.com — 1 operation(s) for orders.
  name: Envia.com Orders API
  slug: envia-orders-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: The Packages API from Envia.com — 3 operation(s) for packages.
  name: Envia.com Packages API
  slug: envia-packages-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: The Payment API from Envia.com — 2 operation(s) for payment.
  name: Envia.com Payment API
  slug: envia-payment-api
- baseURL: https://api-test.envia.com
  baseurl_source: declared
  description: Schedule package pickups with carriers
  name: Envia.com Pickups API
  slug: envia-pickups-api
- baseURL: https://api-test.envia.com
  baseurl_source: declared
  description: The Quotes & Rates API from Envia.com — 1 operation(s) for quotes & rates.
  name: Envia.com Quotes & Rates API
  slug: envia-quotes-rates-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: Get available services by carrier and country
  name: Envia.com Services API
  slug: envia-services-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: Retrieve shipment details, history, and download labels
  name: Envia.com Shipments API
  slug: envia-shipments-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: Shop information lookups (e.g., Shopify store URL)
  name: Envia.com Shops / E-commerce API
  slug: envia-shops-e-commerce-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: Get state/province information by country
  name: Envia.com States API
  slug: envia-states-api
- baseURL: https://api-test.envia.com
  baseurl_source: declared
  description: Track shipments and view delivery status
  name: Envia.com Tracking & Logs API
  slug: envia-tracking-logs-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: The User Management API from Envia.com — 6 operation(s) for user management.
  name: Envia.com User Management API
  slug: envia-user-management-api
- baseURL: https://api-test.envia.com
  baseurl_source: declared
  description: Utility endpoints for shipping operations
  name: Envia.com Utilities API
  slug: envia-utilities-api
- baseURL: https://queries.test.envia.com/
  baseurl_source: declared
  description: The Webhooks API from Envia.com — 4 operation(s) for webhooks.
  name: Envia.com Webhooks API
  slug: envia-webhooks-api
artifact_total: 36
asyncapis:
- description: ''
  name: Envia Webhooks
  slug: envia-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/envia/agentic-access/envia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/envia-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/envia/rules/envia-rules.yml
  title: ''
  type: Spectral
  url: rules/envia-rules.yml
- group: design
  href: https://artifacts.apis.io/envia/vocabulary/envia-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/envia-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/envia/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/envia/asyncapi/envia-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/envia-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/envia/changelog/envia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/envia-changelog.yml
- group: auth
  href: https://artifacts.apis.io/envia/security/envia-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/envia-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/envia/authentication/envia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/envia-authentication.yml
- group: design
  href: https://artifacts.apis.io/envia/errors/envia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/envia-problem-types.yml
- group: design
  href: https://artifacts.apis.io/envia/conformance/envia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/envia-conformance.yml
- group: agent
  href: https://artifacts.apis.io/envia/llms/envia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/envia-llms.txt
- group: agent
  href: https://artifacts.apis.io/envia/well-known/envia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/envia-well-known.yml
- group: other
  href: https://artifacts.apis.io/envia/hosts/envia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/envia-hosts.yml
- group: other
  href: https://artifacts.apis.io/envia/vendors/envia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/envia-vendors.yml
- group: build
  href: https://artifacts.apis.io/envia/packages/envia-packages.yml
  title: ''
  type: SDKs
  url: packages/envia-packages.yml
- group: build
  href: https://artifacts.apis.io/envia/packages/envia-packages.yml
  title: ''
  type: Packages
  url: packages/envia-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.envia.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.envia.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/envia/security/envia-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/envia-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/envia/security/envia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/envia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://envia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://envia.com/en-US/developers
- group: docs
  title: ''
  type: APIReference
  url: https://envia.com/en-US/developers
- group: company
  title: ''
  type: Blog
  url: https://envia.com/en-US/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://envia.com/en-US/pricing
created: '2026-10-27'
description: Envia.com provides a comprehensive shipping logistics platform for businesses in the United States, offering multi‑courier shipping, fulfillment, warehouse management, returns handling, and e‑commerce integrations. The service includes a developer portal with API documentation, SDKs, and tools for automating order processing, rate calculation, and shipment tracking, enabling merchants to streamline their shipping operations across domestic and international carriers.
image: https://assets.envia.com/uploads/landing/images/android-chrome-384x384.png
layout: provider
modified: '2026-10-27'
name: Envia.com
nav: Providers
network: true
overview: 'Envia.com publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including Address Validation API, Branches API, Cancel API, and 25 more. Tagged areas include Company, Shipping, Logistics, and E-Commerce.


  The Envia.com catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Envia.com''s developer surface includes changelog, authentication, support, getting-started guide, documentation, API reference, engineering blog, and 18 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Envia.com API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 4
  slug: envia-rules
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 63.7
    developer_ergonomics: 38.7
    discoverability: 69.6
    operational_transparency: 34.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 28
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/envia/envia-2026-11-03T131547.png
security:
- kind: authentication
  name: Envia Authentication
  slug: envia-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Envia Domain Security
  slug: envia-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Envia Vulnerability Disclosure
  slug: envia-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 2
skills:
- name: envia-create-commercial-invoice-with-documents
  slug: envia-create-commercial-invoice-with-documents
- name: envia-manage-user-address
  slug: envia-manage-user-address
slug: envia
tags:
- Company
- Shipping
- Logistics
- E-Commerce
website: https://envia.com/
---
