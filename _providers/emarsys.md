---
access_model:
  confidence: high
  label: Enterprise sales, no self-serve signup
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://emarsys.com/request-pricing/
  - https://emarsys.com/demo/
  - plans/emarsys-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 80
  human_in_the_loop: 1
  name: Emarsys Agentic Access
  operation_count: 136
  slug: emarsys-agentic-access
  summary_line: 136 operations · 80 acting · 1 human-in-the-loop
api_count: 25
apis:
- description: In this batch you may find endpoints related to accounts. Published by SAP Emarsys as a Swagger 2.0 document with 10 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy X-WSSE
  name: SAP Emarsys Accounts API
  slug: emarsys-accounts-api
- description: In this batch you may find endpoints related to auto-import profiles. Published by SAP Emarsys as a Swagger 2.0 document with 4 operation(s). Part of the SAP Emarsys Core API. Authentication is the le
  name: SAP Emarsys Auto-import Profiles API
  slug: emarsys-auto-import-profiles-api
- description: In this chapter you may find the bulk response summary endpoint. Published by SAP Emarsys as OpenAPI 3.0.3 with 1 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy X-WSSE Us
  name: SAP Emarsys Bulk Response Summary API
  slug: emarsys-bulk-response-summary-api
- description: 'In this batch you may find endpoints related to conditional text rules. Published by SAP Emarsys as a Swagger 2.0 document with 1 operation(s). Part of the SAP Emarsys Core API. Authentication is the '
  name: SAP Emarsys Conditional Text Rules API
  slug: emarsys-conditional-text-rules-api
- description: 'In this batch you may find endpoints related to contact and email data. Published by SAP Emarsys as a Swagger 2.0 document with 7 operation(s). Part of the SAP Emarsys Core API. Authentication is the '
  name: SAP Emarsys Contact and Email Data API
  slug: emarsys-contact-and-email-data-api
- description: In this batch you may find endpoints related to contact lists. Published by SAP Emarsys as a Swagger 2.0 document with 11 operation(s), 2 of them marked deprecated. Part of the SAP Emarsys Core API. A
  name: SAP Emarsys Contact Lists API
  slug: emarsys-contact-lists-api
- description: 'In this batch you may find endpoints related to contact sources. Published by SAP Emarsys as a Swagger 2.0 document with 2 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy '
  name: SAP Emarsys Contact Sources API
  slug: emarsys-contact-sources-api
- description: 'In this batch you may find endpoints related to contacts. Published by SAP Emarsys as a Swagger 2.0 document with 7 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy X-WSSE '
  name: SAP Emarsys Contacts API
  slug: emarsys-contacts-api
- description: 'In this batch you may find endpoints related to email campaign lifecycle. Published by SAP Emarsys as a Swagger 2.0 document with 13 operation(s), 1 of them marked deprecated. Part of the SAP Emarsys '
  name: SAP Emarsys Email Campaign Lifecycle API
  slug: emarsys-email-campaign-lifecycle-api
- description: In this batch you may find endpoints related to email campaigns. Published by SAP Emarsys as a Swagger 2.0 document with 13 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy
  name: SAP Emarsys Email Campaigns API
  slug: emarsys-email-campaigns-api
- description: This document contains all of the email reporting related API endpoints. Published by SAP Emarsys as OpenAPI 3.0.1 with 1 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy X
  name: SAP Emarsys Email Reporting API
  slug: emarsys-email-reporting-api-api
- description: 'In this batch you may find endpoints related to email templates. Published by SAP Emarsys as a Swagger 2.0 document with 2 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy '
  name: SAP Emarsys Email Templates API
  slug: emarsys-email-templates-api
- description: In this batch you may find endpoints related to events. Published by SAP Emarsys as a Swagger 2.0 document with 8 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy X-WSSE Us
  name: SAP Emarsys Events API
  slug: emarsys-events-api
- description: In this batch you may find endpoints related to External Content. Published by SAP Emarsys as a Swagger 2.0 document with 1 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy
  name: SAP Emarsys External Content API
  slug: emarsys-external-content-api
- description: In this batch you may find endpoints related to fields. Published by SAP Emarsys as a Swagger 2.0 document with 6 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy X-WSSE Us
  name: SAP Emarsys Fields API
  slug: emarsys-fields-api
- description: In this batch you may find endpoints related to forms. Published by SAP Emarsys as a Swagger 2.0 document with 2 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy X-WSSE Use
  name: SAP Emarsys Forms API
  slug: emarsys-forms-api
- description: In this batch you may find endpoints related to keys. Published by SAP Emarsys as a Swagger 2.0 document with 4 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy X-WSSE User
  name: SAP Emarsys Keys API
  slug: emarsys-keys-api
- description: In this batch you may find endpoints related to the Media Database. Published by SAP Emarsys as a Swagger 2.0 document with 6 operation(s). Part of the SAP Emarsys Core API. Authentication is the lega
  name: SAP Emarsys Media Database API
  slug: emarsys-media-database-api
- description: 'In this batch you may find endpoints related to programs. Published by SAP Emarsys as a Swagger 2.0 document with 3 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy X-WSSE '
  name: SAP Emarsys Programs API
  slug: emarsys-programs-api
- description: 'In this batch you may find endpoints related to Relational Data. Published by SAP Emarsys as a Swagger 2.0 document with 6 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy '
  name: SAP Emarsys Relational Data (RDS) API
  slug: emarsys-relational-data-api
- description: 'In this batch you may find endpoints related to sections. Published by SAP Emarsys as a Swagger 2.0 document with 5 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy X-WSSE '
  name: SAP Emarsys Sections API
  slug: emarsys-sections-api
- description: In this batch you may find endpoints related to segments. Published by SAP Emarsys as a Swagger 2.0 document with 11 operation(s). Part of the SAP Emarsys Core API. Authentication is the legacy X-WSSE
  name: SAP Emarsys Segments API
  slug: emarsys-segments-api
- description: Published by SAP Emarsys as OpenAPI 3.0.3 with 2 operation(s). Part of the SMS Partner API, which SAP Emarsys publishes openly at github.com/emartech/sms-partner-api-spec so SMS aggregation partners c
  name: SAP Emarsys SMS Partner Callbacks API
  slug: emarsys-sms-partner-callbacks-api
- description: Published by SAP Emarsys as OpenAPI 3.0.3 with 5 operation(s). Part of the SMS Partner API, which SAP Emarsys publishes openly at github.com/emartech/sms-partner-api-spec so SMS aggregation partners c
  name: SAP Emarsys SMS Partner Service API
  slug: emarsys-sms-partner-service-api
- description: In this batch you may find endpoints related to tracked links. Published by SAP Emarsys as a Swagger 2.0 document with 5 operation(s), 1 of them marked deprecated. Part of the SAP Emarsys Core API. Au
  name: SAP Emarsys Tracked Links API
  slug: emarsys-tracked-links-api
artifact_total: 59
asyncapis:
- description: ''
  name: Emarsys Webhooks
  slug: emarsys-webhooks
collections:
- collection_type: open
  name: Emarsys Core API - Accounts endpoint batch
  slug: open-emarsys-accounts
- collection_type: open
  name: Emarsys Core API - Auto-import profiles endpoint batch
  slug: open-emarsys-auto-import-profiles
- collection_type: open
  name: Bulk Response Summary
  slug: open-emarsys-bulk-response-summary
- collection_type: open
  name: Emarsys Core API - Conditional text rules endpoint batch
  slug: open-emarsys-conditional-text-rules
- collection_type: open
  name: Emarsys Core API - Contact and email data endpoint batch
  slug: open-emarsys-contact-and-email-data
- collection_type: open
  name: Emarsys Core API - Contact lists endpoint batch
  slug: open-emarsys-contact-lists
- collection_type: open
  name: Emarsys Core API - Contact sources endpoint batch
  slug: open-emarsys-contact-sources
- collection_type: open
  name: Emarsys Core API - Contacts endpoint batch
  slug: open-emarsys-contacts
- collection_type: open
  name: Emarsys Core API - Email campaign lifecycle endpoint batch
  slug: open-emarsys-email-campaign-lifecycle
- collection_type: open
  name: Emarsys Core API - Email campaigns endpoint batch
  slug: open-emarsys-email-campaigns
- collection_type: open
  name: Email Reporting API
  slug: open-emarsys-email-reporting-api
- collection_type: open
  name: Emarsys Core API - Email templates endpoint batch
  slug: open-emarsys-email-templates
- collection_type: open
  name: Emarsys Core API - Events endpoint batch
  slug: open-emarsys-events
- collection_type: open
  name: Emarsys Core API - External Content endpoint batch
  slug: open-emarsys-external-content
- collection_type: open
  name: Emarsys Core API - Fields endpoint batch
  slug: open-emarsys-fields
- collection_type: open
  name: Emarsys Core API - Forms endpoint batch
  slug: open-emarsys-forms
- collection_type: open
  name: Emarsys Core API - Keys endpoint batch
  slug: open-emarsys-keys
- collection_type: open
  name: Emarsys Core API - Media Database endpoint batch
  slug: open-emarsys-media-database
- collection_type: open
  name: Emarsys Core API - Programs endpoint batch
  slug: open-emarsys-programs
- collection_type: open
  name: Emarsys Core API - Relational Data endpoint batch
  slug: open-emarsys-relational-data
- collection_type: open
  name: Emarsys Core API - Sections endpoint batch
  slug: open-emarsys-sections
- collection_type: open
  name: Emarsys Core API - Segments endpoint batch
  slug: open-emarsys-segments
- collection_type: open
  name: Provider callbacks
  slug: open-emarsys-sms-partner-callbacks
- collection_type: open
  name: SAP Emarsys SMS Partner Service
  slug: open-emarsys-sms-partner-service
- collection_type: open
  name: Emarsys Core API - Tracked links endpoint batch
  slug: open-emarsys-tracked-links
common:
- group: build
  title: ''
  type: Packages
  url: packages/emarsys-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/emarsys-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/emarsys-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/emarsys-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/emarsys-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/emarsys-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.sap.com/about/trust-center/certification-compliance.html
- group: auth
  title: ''
  type: TrustCenter
  url: security/emarsys-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/emarsys-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/emarsys-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.emarsys.com
- group: operate
  title: ''
  type: Deprecation
  url: https://dev.emarsys.com/docs/changelog/z1yoegvlz20pg-changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/emarsys-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/emarsys-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/emarsys-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/emarsys-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/emarsys-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/emarsys-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/emarsys-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/emarsys-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/emarsys-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/emarsys-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sap.com/report-a-vulnerability
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emarsys-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://emarsys.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.emarsys.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.emarsys.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.emarsys.com/docs/core-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.emarsys.com/docs/emarsys-core-api-guides/tv7m82af5d5hn-1-prerequisites
- group: auth
  title: ''
  type: Authentication
  url: https://dev.emarsys.com/docs/emarsys-core-api-guides/b3c3a1eba8515-authentication
- group: start
  title: ''
  type: SAP Help Portal
  url: https://help.sap.com/docs/SAP_EMARSYS
- group: other
  title: ''
  type: API Credentials
  url: https://help.sap.com/docs/SAP_EMARSYS/5d44574160f44536b0130abf58cb87cc/fdf4b58974c110149353957a3e7ef453.html
- group: build
  title: ''
  type: Postman
  url: https://github.com/emartech/SAP-Engagement-Cloud-postman-collection
- group: build
  title: ''
  type: PostmanCollection
  url: https://github.com/emartech/Emarsys-postman-collection
- group: commercial
  title: ''
  type: Pricing
  url: https://emarsys.com/request-pricing/
- group: start
  title: ''
  type: Login
  url: https://login.emarsys.net/
- group: operate
  title: ''
  type: Support
  url: https://emarsys.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.emarsys.com/
- group: company
  title: ''
  type: Blog
  url: https://emarsys.com/learn/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emarsys.com/privacy-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emarsys.com/legal-notice/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emartech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/emarsys
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/emarsys
created: '2026-05-11'
description: SAP Emarsys (formerly Emarsys, acquired by SAP in 2020 and now marketed as part of SAP Engagement Cloud) is an omnichannel customer engagement and marketing automation platform used by retail and consumer brands to run personalized email, SMS, mobile, web and ads campaigns from a unified customer data layer with AI-driven segmentation. The developer surface is the Emarsys Core API — 23 published endpoint batches covering contacts and custom contact fields, static contact lists and rule-based segments, email campaign creation, preview, test-send, launch and stop, delivery status and response-metric reporting, external event triggers that start Automation Centre programs, media assets, tracked links, account and API-user administration, and the Relational Data Store (RDS) custom-object layer for purchase and product data. A separately published SMS Partner API lets SMS aggregators integrate with the Emarsys SMS channel. Authentication is the legacy X-WSSE UsernameToken header,
  which SAP Emarsys has deprecated with a final sunset at the end of 2026 in favour of OAuth 2.0 client credentials / OpenID Connect on the v3 surface. Rate limiting is 1000 requests per minute per API user with published X-RateLimit-* headers, and errors are returned as a proprietary replyCode/replyText/data envelope that can carry failures inside HTTP 200 responses.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emarsys.png
layout: provider
modified: '2026-08-13'
name: SAP Emarsys
nav: Providers
network: true
overview: 'SAP Emarsys publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Auto-import Profiles API, Bulk Response Summary API, and 22 more. Tagged areas include Marketing Automation, Customer Engagement, Email Marketing, Omnichannel, and Customer Data Platform.


  The SAP Emarsys catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SAP Emarsys'' developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, support, and 38 more developer resources.'
plans:
- name: Emarsys Plans Pricing
  plan_count: 0
  slug: emarsys-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 1
  name: Emarsys Rate Limits
  slug: emarsys-rate-limits
scopes:
- name: Emarsys Scopes
  scope_count: 156
  slug: emarsys-scopes
  summary_line: 156 scopes · clientCredentials
score:
  band: exemplar
  composite: 66.8
  delta: 1.3
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 16.7
    contract_quality: 59.6
    developer_ergonomics: 70.8
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 65.8
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 80.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emarsys/refs/heads/main/screenshots/emarsys-2026-06-20T180628.png
security:
- kind: authentication
  name: Emarsys Authentication
  slug: emarsys-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Emarsys Domain Security
  slug: emarsys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Emarsys Vulnerability Disclosure
  slug: emarsys-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Emarsys Trust Center
  slug: emarsys-trust-center
  summary_line: SOC 1, SOC 2, ISO 27001, ISO 22301, PCI DSS, FedRAMP, BSI C5, TISAX, CSA STAR
slug: emarsys
tags:
- Marketing Automation
- Customer Engagement
- Email Marketing
- Omnichannel
- Customer Data Platform
- SAP
- Segmentation
- SMS
- Marketing Analytics
- Retail
- Personalization
- Campaign Management
website: https://emarsys.com
---
