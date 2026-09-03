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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 120
  human_in_the_loop: 3
  name: Metronome Agentic Access
  operation_count: 133
  slug: metronome-agentic-access
  summary_line: 133 operations · 120 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: '[Alerts](https://docs.metronome.com/connecting-metronome/alerts/) monitor customer spending, balances, and other billing factors. Use these endpoints to create, retrieve, and archive customer alerts. '
  name: Metronome Alerts API
  slug: metronome-alerts-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: The Billable Metrics API from Metronome — 5 operation(s) for billable metrics.
  name: Metronome Billable Metrics API
  slug: metronome-billable-metrics-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: A contract defines a customer’s products, pricing, discounts, commitments, and more. Use these endpoints to create and update contracts data.
  name: Metronome Contracts API
  slug: metronome-contracts-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: Credits and commits are used to manage customer balances.
  name: Metronome Credits and commits API
  slug: metronome-credits-and-commits-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: '[Custom fields](https://docs.metronome.com/integrations/custom-fields/) enable adding additional data to Metronome entities. Use these endpoints to create, retrieve, update, and delete custom fields.'
  name: Metronome Custom fields API
  slug: metronome-custom-fields-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: '[Customers](https://docs.metronome.com/provisioning/create-customers/) in Metronome represent your users for all billing and reporting. Use these endpoints to create, retrieve, update, and archive cus'
  name: Metronome Customers API
  slug: metronome-customers-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: The Integrations API from Metronome — 1 operation(s) for integrations.
  name: Metronome Integrations API
  slug: metronome-integrations-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: '[Invoices](https://docs.metronome.com/invoicing/) reflect how much a customer spent during a period, which is the basis for billing. Metronome automatically generates invoices based upon your pricing,'
  name: Metronome Invoices API
  slug: metronome-invoices-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: Named schedules are used for storing custom data that can change over time. Named schedules are often used in custom pricing logic.
  name: Metronome Named schedules API
  slug: metronome-named-schedules-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: The Notifications API from Metronome — 6 operation(s) for notifications.
  name: Metronome Notifications API
  slug: metronome-notifications-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: The Packages API from Metronome — 3 operation(s) for packages.
  name: Metronome Packages API
  slug: metronome-packages-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: The Payments API from Metronome — 3 operation(s) for payments.
  name: Metronome Payments API
  slug: metronome-payments-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: Products are the items that customers purchase.
  name: Metronome Products API
  slug: metronome-products-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: Rate cards are used to define default pricing for products.
  name: Metronome Rate cards API
  slug: metronome-rate-cards-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: '[Security](https://docs.metronome.com/developer-resources/security/) endpoints allow you to retrieve security-related data.'
  name: Metronome Security API
  slug: metronome-security-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: Use these endpoints to configure a billing API key, a webhook secret, or invoice finalization behavior.
  name: Metronome Settings API
  slug: metronome-settings-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: The Threshold billing API from Metronome — 1 operation(s) for threshold billing.
  name: Metronome Threshold billing API
  slug: metronome-threshold-billing-api
- baseURL: https://api.metronome.com
  baseurl_source: declared
  description: '[Usage events](https://docs.metronome.com/connecting-metronome/send-usage-data/) are the basis for billable metrics. Use these endpoints to send usage events to Metronome and retrieve aggregated event'
  name: Metronome Usage API
  slug: metronome-usage-api
artifact_total: 45
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Metronome Alerts API
  slug: open-metronome-alerts-api
- collection_type: open
  name: Metronome Alerts Billable Metrics API
  slug: open-metronome-billable-metrics-api
- collection_type: open
  name: Metronome Alerts Contracts API
  slug: open-metronome-contracts-api
- collection_type: open
  name: Metronome Alerts Credits and commits API
  slug: open-metronome-credits-and-commits-api
- collection_type: open
  name: Metronome Alerts Custom fields API
  slug: open-metronome-custom-fields-api
- collection_type: open
  name: Metronome Alerts Customers API
  slug: open-metronome-customers-api
- collection_type: open
  name: Metronome Alerts Integrations API
  slug: open-metronome-integrations-api
- collection_type: open
  name: Metronome Alerts Invoices API
  slug: open-metronome-invoices-api
- collection_type: open
  name: Metronome Alerts Named schedules API
  slug: open-metronome-named-schedules-api
- collection_type: open
  name: Metronome Alerts Notifications API
  slug: open-metronome-notifications-api
- collection_type: open
  name: Metronome Alerts Packages API
  slug: open-metronome-packages-api
- collection_type: open
  name: Metronome Alerts Payments API
  slug: open-metronome-payments-api
- collection_type: open
  name: Metronome Alerts Products API
  slug: open-metronome-products-api
- collection_type: open
  name: Metronome Alerts Rate cards API
  slug: open-metronome-rate-cards-api
- collection_type: open
  name: Metronome Alerts Security API
  slug: open-metronome-security-api
- collection_type: open
  name: Metronome Alerts Settings API
  slug: open-metronome-settings-api
- collection_type: open
  name: Metronome Alerts Threshold billing API
  slug: open-metronome-threshold-billing-api
- collection_type: open
  name: Metronome Alerts Usage API
  slug: open-metronome-usage-api
- collection_type: open
  name: Metronome
  slug: open-metronome
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metronome-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/metronome-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metronome-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metronome-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Metronome-Industries
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getmetronome
- group: company
  title: ''
  type: Website
  url: https://metronome.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metronome.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.metronome.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.metronome.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://metronome.com/blog
created: '2026-03-27'
description: Metronome is a usage-based billing platform providing real-time metering, pricing, invoicing, and revenue recognition for API and cloud services.
finops:
- name: Metronome Finops
  service_category: API
  slug: metronome-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metronome.png
layout: provider
modified: '2026-05-19'
name: Metronome
nav: Providers
network: true
overview: 'Metronome publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Billable Metrics API, Contracts API, and 15 more. Tagged areas include Billing, FinOps, Metering, Pricing, and Usage-Based Billing.


  Metronome''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Metronome Plans Pricing
  plan_count: 3
  slug: metronome-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Metronome Rate Limits
  slug: metronome-rate-limits
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 56.9
    developer_ergonomics: 35.7
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metronome/refs/heads/main/screenshots/metronome-2026-06-20T185311.png
security:
- kind: authentication
  name: Metronome Authentication
  slug: metronome-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Metronome Domain Security
  slug: metronome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Metronome Trust Center
  slug: metronome-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: metronome
tags:
- Billing
- FinOps
- Metering
- Pricing
- Usage-Based Billing
website: https://metronome.com/
---
