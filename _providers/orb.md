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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Orb Agentic Access
  operation_count: 14
  slug: orb-agentic-access
  summary_line: 14 operations · 11 acting
api_count: 10
apis:
- description: The Alerts API from Orb — 3 operation(s) for alerts.
  name: Orb Alerts API
  slug: orb-alerts-api
- description: The Availability API from Orb — 1 operation(s) for availability.
  name: Orb Availability API
  slug: orb-availability-api
- description: The Coupons API from Orb — 1 operation(s) for coupons.
  name: Orb Coupons API
  slug: orb-coupons-api
- description: The Credit Notes API from Orb — 1 operation(s) for credit notes.
  name: Orb Credit Notes API
  slug: orb-credit-notes-api
- description: The Customers API from Orb — 2 operation(s) for customers.
  name: Orb Customers API
  slug: orb-customers-api
- description: The Events API from Orb — 1 operation(s) for events.
  name: Orb Events API
  slug: orb-events-api
- description: The Invoices API from Orb — 1 operation(s) for invoices.
  name: Orb Invoices API
  slug: orb-invoices-api
- description: The Plans API from Orb — 1 operation(s) for plans.
  name: Orb Plans API
  slug: orb-plans-api
- description: The Prices API from Orb — 1 operation(s) for prices.
  name: Orb Prices API
  slug: orb-prices-api
- description: The Subscriptions API from Orb — 2 operation(s) for subscriptions.
  name: Orb Subscriptions API
  slug: orb-subscriptions-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Orb Alerts API
  slug: open-orb-alerts-api
- collection_type: open
  name: Orb Alerts Availability API
  slug: open-orb-availability-api
- collection_type: open
  name: Orb Alerts Coupons API
  slug: open-orb-coupons-api
- collection_type: open
  name: Orb Alerts Credit Notes API
  slug: open-orb-credit-notes-api
- collection_type: open
  name: Orb Alerts Customers API
  slug: open-orb-customers-api
- collection_type: open
  name: Orb Alerts Events API
  slug: open-orb-events-api
- collection_type: open
  name: Orb Alerts Invoices API
  slug: open-orb-invoices-api
- collection_type: open
  name: Orb Alerts Plans API
  slug: open-orb-plans-api
- collection_type: open
  name: Orb Alerts Prices API
  slug: open-orb-prices-api
- collection_type: open
  name: Orb Alerts Subscriptions API
  slug: open-orb-subscriptions-api
- collection_type: open
  name: Orb API
  slug: open-orb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/orb-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orb-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orbcorp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orbhq
- group: company
  title: ''
  type: Website
  url: https://www.withorb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.withorb.com/
created: '2026-03-27'
description: Orb is a billing infrastructure platform providing usage-based pricing, metering, and invoicing for API and cloud products.
finops:
- name: Orb Finops
  service_category: API
  slug: orb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orb.png
layout: provider
modified: '2026-05-19'
name: Orb
nav: Providers
network: true
overview: 'Orb publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Availability API, Coupons API, and 7 more. Tagged areas include FinOps and Usage-Based Billing.


  Orb''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Orb Plans Pricing
  plan_count: 3
  slug: orb-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Orb Rate Limits
  slug: orb-rate-limits
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 42.9
    developer_ergonomics: 21.4
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 25.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orb/refs/heads/main/screenshots/orb-2026-06-20T191155.png
security:
- kind: domain-security
  name: Orb Domain Security
  slug: orb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Orb Vulnerability Disclosure
  slug: orb-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Orb Trust Center
  slug: orb-trust-center
  summary_line: SOC 2
slug: orb
tags:
- FinOps
- Usage-Based Billing
website: https://www.withorb.com/
---
