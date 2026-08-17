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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
  score: 41.9
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: The Responsys REST API (v1.3) manages profile lists and recipients, profile extension tables, supplemental data tables, campaigns and campaign schedules, programs, folders, the content library, trigge
  name: Oracle Responsys REST API
  slug: oracle-responsys-rest-api
- description: The Event Notification API pushes real-time campaign event data to a customer-owned callback URL. Register a callback, verify it, then subscribe it to any of the 26 supported event types across email,
  name: Oracle Responsys Event Notification API
  slug: oracle-responsys-event-notification-api
- description: The AFTM (Automatic Failover for Transactional Messaging) REST API provides asynchronous, high-availability alternatives to the synchronous merge and trigger operations — HA Merge List Members, HA Mer
  name: Oracle Responsys AFTM / Asynchronous API
  slug: oracle-responsys-aftm-asynchronous-api
artifact_total: 11
asyncapis:
- description: ''
  name: Responsys Event Notification Webhooks
  slug: responsys-event-notification-webhooks
collections:
- collection_type: open
  name: REST API for Oracle Responsys Marketing Cloud Service
  slug: open-responsys
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/responsys-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/cx/marketing/campaign-management/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.oracle.com/en/cloud/saas/marketing/responsys-develop/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/saas/marketing/responsys-rest-api/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/en/cloud/saas/marketing/responsys-rest-api/rest-endpoints.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/cloud/saas/marketing/responsys-develop/API/api.htm
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: other
  title: ''
  type: SOAP
  url: https://docs.oracle.com/en/cloud/saas/marketing/responsys-soap-api/index.html
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/responsys-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/responsys-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/responsys-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/responsys-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.oracle.com/corporate/cloud-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/responsys-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/responsys-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.oracle.com/corporate/security-practices/assurance/vulnerability/reporting.html
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/responsys-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/responsys-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/responsys-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/responsys-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/responsys-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/responsys-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/responsys-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/responsys-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/responsys-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/responsys-event-notification-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/responsys-llms.txt
created: '2026-07-17'
description: Oracle Responsys (Oracle Responsys Campaign Management) is a B2C cross-channel marketing orchestration platform, originally founded as Responsys and acquired by Oracle in 2014, now part of Oracle Marketing. It lets marketing teams design and deliver targeted, personalized customer experiences across email, mobile push, SMS, MMS, web push, display, and web channels, unifying data from disparate sources into precisely targeted audiences delivered in near real-time. Responsys exposes a REST API (v1.3, published as a Swagger 2.0 document with 88 operations), an asynchronous AFTM API, an Event Notification webhook API covering 26 campaign event types, and a legacy SOAP API — managing profile lists and recipients, profile extension tables, supplemental tables, campaigns and schedules, programs, folders, the content library, triggered email/SMS/push messages, events, and account settings. This profile catalogs the public Oracle Responsys developer surface for the API Evangelist network.
image: https://www.oracle.com/asset/web/favicons/favicon-192.png
layout: provider
modified: '2026-08-13'
name: Responsys
nav: Providers
network: true
overview: 'Responsys publishes 1 API on the [APIs.io](https://apis.io/) network: Oracle Responsys REST API. Tagged areas include Company, Marketing, Email Marketing, Marketing Automation, and Campaign Management.


  The Responsys catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Responsys'' developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, and 25 more developer resources.'
plans:
- name: Responsys Plans Pricing
  plan_count: 0
  slug: responsys-plans-pricing
random_paper: 120
rate_limits:
- limit_count: 7
  name: Responsys Rate Limits
  slug: responsys-rate-limits
score:
  band: developing
  composite: 49.5
  delta: 34.1
  facets:
    commercial_clarity: 36.8
    contract_quality: 42.5
    developer_ergonomics: 63.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 71.1
  previous_composite: 15.4
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: authentication
  name: Responsys Authentication
  slug: responsys-authentication
  summary_line: token · 1 scheme
- kind: domain-security
  name: Responsys Domain Security
  slug: responsys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Responsys Vulnerability Disclosure
  slug: responsys-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Responsys Trust Center
  slug: responsys-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR, FIPS 140, HITRUST, C5, IRAP
slug: responsys
tags:
- Company
- Marketing
- Email Marketing
- Marketing Automation
- Campaign Management
- Cross-Channel Marketing
- Customer Engagement
- Push Notifications
- SMS
- Webhooks
- Oracle
- Martech
website: https://www.oracle.com/cx/marketing/campaign-management/
---
