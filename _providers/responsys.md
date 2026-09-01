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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The Event Notification API pushes real-time campaign event data to a customer-owned callback URL. Register a callback, verify it, then subscribe it to any of the 26 supported event types across email,
  name: Oracle Responsys Event Notification API
  slug: oracle-responsys-event-notification-api
- description: The AFTM (Automatic Failover for Transactional Messaging) REST API provides asynchronous, high-availability alternatives to the synchronous merge and trigger operations — HA Merge List Members, HA Mer
  name: Oracle Responsys AFTM / Asynchronous API
  slug: oracle-responsys-aftm-asynchronous-api
- description: API endpoints to enable managing your Responsys account.
  name: Responsys Account API
  slug: responsys-account-api
- description: Send Responsys Email Campaigns with Attachments
  name: Responsys Attachments API
  slug: responsys-attachments-api
- description: Campaign Attributes API endpoints.
  name: Responsys Campaign Attributes API
  slug: responsys-campaign-attributes-api
- description: Responsys Campaign API Endpoints
  name: Responsys Campaigns API
  slug: responsys-campaigns-api
- description: Content Library Document Images
  name: Responsys Content Library Document Images API
  slug: responsys-content-library-document-images-api
- description: Documents in the Responsys Interact Suite Content Library.
  name: Responsys Content Library Documents API
  slug: responsys-content-library-documents-api
- description: Content Library Folders in the Responsys Interact Suite Content Library.
  name: Responsys Content Library Folders API
  slug: responsys-content-library-folders-api
- description: Media Files in the Responsys Interact Suite Content Library.
  name: Responsys Content Library Media Items API
  slug: responsys-content-library-media-items-api
- description: Schedule an Email or a Push Campaign
  name: Responsys Email or Push Campaign Schedule API
  slug: responsys-email-or-push-campaign-schedule-api
- description: Raise Events for Cross-channel Marketing Programs.
  name: Responsys Events API
  slug: responsys-events-api
- description: Filters in the Responsys Interact Suite
  name: Responsys Filters API
  slug: responsys-filters-api
- description: Responsys Account Folder API Endpoints
  name: Responsys Folders API
  slug: responsys-folders-api
- description: Profile Extensions for a Profile List in the Responsys Interact Suite
  name: Responsys List Extensions API
  slug: responsys-list-extensions-api
- description: Merge Members to a Profile List and Send Responsys Email Campaigns to them.
  name: Responsys Merge Trigger Email API
  slug: responsys-merge-trigger-email-api
- description: Merge Members to a Profile List and Send Responsys SMS Campaigns to them
  name: Responsys Merge Trigger SMS API
  slug: responsys-merge-trigger-sms-api
- description: Responsys Organizations
  name: Responsys Organizations API
  slug: responsys-organizations-api
- description: One or more Recipients within a Profile Extension Table in the Responsys Interact Suite.
  name: Responsys Profile Extension Recipients API
  slug: responsys-profile-extension-recipients-api
- description: One or more Recipients within a Profile List in the Responsys Interact Suite.
  name: Responsys Profile List Recipients API
  slug: responsys-profile-list-recipients-api
- description: Profile Lists in the Responsys Interact Suite
  name: Responsys Profile Lists API
  slug: responsys-profile-lists-api
- description: Responsys Program API Endpoints
  name: Responsys Programs API
  slug: responsys-programs-api
- description: Members of a Supplemental Data Table in the Responsys Interact Suite.
  name: Responsys Supplemental Table Members API
  slug: responsys-supplemental-table-members-api
- description: Supplemental table objects.
  name: Responsys Supplemental Tables API
  slug: responsys-supplemental-tables-api
- description: Send Responsys Email Campaigns to existing members of a Profile List.
  name: Responsys Trigger Email Message API
  slug: responsys-trigger-email-message-api
- description: Send Responsys Push Campaigns to existing members of a Profile List
  name: Responsys Trigger Push Message API
  slug: responsys-trigger-push-message-api
- description: Trigger SMS messages to existing members of a profile list.
  name: Responsys Trigger SMS Message API
  slug: responsys-trigger-sms-message-api
artifact_total: 35
asyncapis:
- description: ''
  name: Responsys Event Notification Webhooks
  slug: responsys-event-notification-webhooks
collections:
- collection_type: open
  name: REST API for Oracle Responsys Marketing Cloud Service
  slug: open-responsys
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/responsys-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/oracle/
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
modified: '2026-08-21'
name: Responsys
nav: Providers
network: true
overview: 'Responsys publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Account API, Attachments API, Campaign Attributes API, and 22 more. Tagged areas include Company, Marketing, Email Marketing, Marketing Automation, and Campaign Management.


  The Responsys catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Responsys'' developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, and 27 more developer resources.'
plans:
- name: Responsys Plans Pricing
  plan_count: 0
  slug: responsys-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 7
  name: Responsys Rate Limits
  slug: responsys-rate-limits
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 49.4
    developer_ergonomics: 63.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 68.4
  previous_composite: 51.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/responsys/refs/heads/main/screenshots/responsys-2026-08-17T081535.png
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
- Webhook
- Oracle
- MarTech
website: https://www.oracle.com/cx/marketing/campaign-management/
---
