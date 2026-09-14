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
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Openmeter Agentic Access
  operation_count: 36
  slug: openmeter-agentic-access
  summary_line: 36 operations · 14 acting
api_count: 1
apis:
- baseURL: https://openmeter.cloud/api/v1
  baseurl_source: declared
  description: Billing profiles, invoices, and customer overrides.
  name: OpenMeter Billing API
  slug: openmeter-billing-api
- baseURL: https://openmeter.cloud/api/v1
  baseurl_source: declared
  description: Customers used for entitlements, subscriptions, and billing.
  name: OpenMeter Customers API
  slug: openmeter-customers-api
- baseURL: https://openmeter.cloud/api/v1
  baseurl_source: declared
  description: Metered, boolean, and static entitlements that gate access.
  name: OpenMeter Entitlements API
  slug: openmeter-entitlements-api
- baseURL: https://openmeter.cloud/api/v1
  baseurl_source: declared
  description: Ingest usage events as CloudEvents and list ingested events.
  name: OpenMeter Events API
  slug: openmeter-events-api
- baseURL: https://openmeter.cloud/api/v1
  baseurl_source: declared
  description: Features that entitlements are attached to.
  name: OpenMeter Features API
  slug: openmeter-features-api
- baseURL: https://openmeter.cloud/api/v1
  baseurl_source: declared
  description: Usage grants that top up metered entitlement balances.
  name: OpenMeter Grants API
  slug: openmeter-grants-api
- baseURL: https://openmeter.cloud/api/v1
  baseurl_source: declared
  description: Define meters that aggregate events and query usage.
  name: OpenMeter Meters API
  slug: openmeter-meters-api
- baseURL: https://openmeter.cloud/api/v1
  baseurl_source: declared
  description: Notification channels, rules, and events for usage-driven alerts.
  name: OpenMeter Notifications API
  slug: openmeter-notifications-api
- baseURL: https://openmeter.cloud/api/v1
  baseurl_source: declared
  description: Product catalog plans for subscriptions.
  name: OpenMeter Plans API
  slug: openmeter-plans-api
- baseURL: https://openmeter.cloud/api/v1
  baseurl_source: declared
  description: Subjects that usage is metered against.
  name: OpenMeter Subjects API
  slug: openmeter-subjects-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenMeter Billing API
  slug: open-openmeter-billing-api
- collection_type: open
  name: OpenMeter Billing Customers API
  slug: open-openmeter-customers-api
- collection_type: open
  name: OpenMeter Billing Entitlements API
  slug: open-openmeter-entitlements-api
- collection_type: open
  name: OpenMeter Billing Events API
  slug: open-openmeter-events-api
- collection_type: open
  name: OpenMeter Billing Features API
  slug: open-openmeter-features-api
- collection_type: open
  name: OpenMeter Billing Grants API
  slug: open-openmeter-grants-api
- collection_type: open
  name: OpenMeter Billing Meters API
  slug: open-openmeter-meters-api
- collection_type: open
  name: OpenMeter Billing Notifications API
  slug: open-openmeter-notifications-api
- collection_type: open
  name: OpenMeter Billing Plans API
  slug: open-openmeter-plans-api
- collection_type: open
  name: OpenMeter Billing Subjects API
  slug: open-openmeter-subjects-api
- collection_type: open
  name: OpenMeter API
  slug: open-openmeter
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openmeter-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/openmeter-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openmeter-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openmeter-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openmeterio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openmeter
- group: company
  title: ''
  type: Website
  url: https://openmeter.io/
- group: docs
  title: ''
  type: Documentation
  url: https://openmeter.io/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/openmeter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openmeter-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openmeter-finops.yml
created: '2026-07-01'
description: OpenMeter is open-source usage metering and billing for AI and API products. It ingests usage events as CloudEvents, aggregates them through meters, answers usage queries, and turns that usage into entitlements, balances, grants, usage-driven notifications, and Stripe-backed billing. Available as an open-source project and as OpenMeter Cloud with a Bearer-token REST API at https://openmeter.cloud/api/v1.
finops:
- name: Openmeter Finops
  service_category: Analytics and Metering
  slug: openmeter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openmeter.png
layout: provider
modified: '2026-07-01'
name: OpenMeter
nav: Providers
network: true
overview: 'OpenMeter publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Customers API, Entitlements API, and 7 more. Tagged areas include Usage Metering, Billing, Entitlements, CloudEvents, and Open-Source.


  OpenMeter''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Openmeter Plans Pricing
  plan_count: 4
  slug: openmeter-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Openmeter Rate Limits
  slug: openmeter-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/openmeter/refs/heads/main/screenshots/openmeter-2026-08-07T190632.png
security:
- kind: authentication
  name: Openmeter Authentication
  slug: openmeter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openmeter Domain Security
  slug: openmeter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Openmeter Trust Center
  slug: openmeter-trust-center
  summary_line: SOC 2
slug: openmeter
tags:
- Usage Metering
- Billing
- Entitlements
- CloudEvents
- Open-Source
- Artificial Intelligence
website: https://openmeter.io/
---
