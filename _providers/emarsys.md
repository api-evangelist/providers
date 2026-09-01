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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 80
  human_in_the_loop: 1
  name: Emarsys Agentic Access
  operation_count: 136
  slug: emarsys-agentic-access
  summary_line: 136 operations · 80 acting · 1 human-in-the-loop
api_count: 25
apis:
- description: The Ac API from SAP Emarsys — 2 operation(s) for ac.
  name: SAP Emarsys Ac API
  slug: emarsys-ac-api
- description: The Administrator API from SAP Emarsys — 7 operation(s) for administrator.
  name: SAP Emarsys Administrator API
  slug: emarsys-administrator-api
- description: The Blocklist API from SAP Emarsys — 1 operation(s) for blocklist.
  name: SAP Emarsys Blocklist API
  slug: emarsys-blocklist-api
- description: The Campaigns API from SAP Emarsys — 1 operation(s) for campaigns.
  name: SAP Emarsys Campaigns API
  slug: emarsys-campaigns-api
- description: The Client Configuration API from SAP Emarsys — 1 operation(s) for client configuration.
  name: SAP Emarsys Client Configuration API
  slug: emarsys-client-configuration-api
- description: The Client Configuration Test API from SAP Emarsys — 1 operation(s) for client configuration test.
  name: SAP Emarsys Client Configuration Test API
  slug: emarsys-client-configuration-test-api
- description: The Condition API from SAP Emarsys — 1 operation(s) for condition.
  name: SAP Emarsys Condition API
  slug: emarsys-condition-api
- description: The Contact API from SAP Emarsys — 10 operation(s) for contact.
  name: SAP Emarsys Contact API
  slug: emarsys-contact-api
- description: The Contactlist API from SAP Emarsys — 10 operation(s) for contactlist.
  name: SAP Emarsys Contactlist API
  slug: emarsys-contactlist-api
- description: The Delivery Reports API from SAP Emarsys — 1 operation(s) for delivery reports.
  name: SAP Emarsys Delivery Reports API
  slug: emarsys-delivery-reports-api
- description: The Email API from SAP Emarsys — 34 operation(s) for email.
  name: SAP Emarsys Email API
  slug: emarsys-email-api
- description: The Emailcategory API from SAP Emarsys — 1 operation(s) for emailcategory.
  name: SAP Emarsys Emailcategory API
  slug: emarsys-emailcategory-api
- description: The Event API from SAP Emarsys — 6 operation(s) for event.
  name: SAP Emarsys Event API
  slug: emarsys-event-api
- description: The Export API from SAP Emarsys — 3 operation(s) for export.
  name: SAP Emarsys Export API
  slug: emarsys-export-api
- description: The Field API from SAP Emarsys — 5 operation(s) for field.
  name: SAP Emarsys Field API
  slug: emarsys-field-api
- description: The File API from SAP Emarsys — 4 operation(s) for file.
  name: SAP Emarsys File API
  slug: emarsys-file-api
- description: The Filter API from SAP Emarsys — 10 operation(s) for filter.
  name: SAP Emarsys Filter API
  slug: emarsys-filter-api
- description: The Folder API from SAP Emarsys — 1 operation(s) for folder.
  name: SAP Emarsys Folder API
  slug: emarsys-folder-api
- description: The Form API from SAP Emarsys — 2 operation(s) for form.
  name: SAP Emarsys Form API
  slug: emarsys-form-api
- description: 'The Https: API from SAP Emarsys — 1 operation(s) for https:.'
  name: 'SAP Emarsys Https: API'
  slug: emarsys-https-api
- description: The inbound-messages API from SAP Emarsys — 1 operation(s) for inbound-messages.
  name: SAP Emarsys Inbound Messages API
  slug: emarsys-inbound-messages-api
- description: The Keyring API from SAP Emarsys — 2 operation(s) for keyring.
  name: SAP Emarsys Keyring API
  slug: emarsys-keyring-api
- description: The Language API from SAP Emarsys — 1 operation(s) for language.
  name: SAP Emarsys Language API
  slug: emarsys-language-api
- description: The Outbound Message Sending API from SAP Emarsys — 1 operation(s) for outbound message sending.
  name: SAP Emarsys Outbound Message Sending API
  slug: emarsys-outbound-message-sending-api
- description: The Programresource API from SAP Emarsys — 1 operation(s) for programresource.
  name: SAP Emarsys Programresource API
  slug: emarsys-programresource-api
- description: The Rds API from SAP Emarsys — 3 operation(s) for rds.
  name: SAP Emarsys Rds API
  slug: emarsys-rds-api
- description: The Settings API from SAP Emarsys — 9 operation(s) for settings.
  name: SAP Emarsys Settings API
  slug: emarsys-settings-api
- description: The Source API from SAP Emarsys — 2 operation(s) for source.
  name: SAP Emarsys Source API
  slug: emarsys-source-api
- description: The Trendreporting API from SAP Emarsys — 1 operation(s) for trendreporting.
  name: SAP Emarsys Trendreporting API
  slug: emarsys-trendreporting-api
- description: The Wishlist API from SAP Emarsys — 1 operation(s) for wishlist.
  name: SAP Emarsys Wishlist API
  slug: emarsys-wishlist-api
artifact_total: 64
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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sap/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/emarsys-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-accounts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-auto-import-profiles-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-bulk-response-summary-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-conditional-text-rules-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-contact-and-email-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-contact-lists-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-contact-sources-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-contacts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-email-campaign-lifecycle-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-email-campaigns-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-email-reporting-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-email-templates-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-events-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-external-content-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-fields-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-forms-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-keys-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-media-database-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-programs-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-relational-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-sections-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-segments-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-sms-partner-callbacks-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-sms-partner-service-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/emarsys-tracked-links-overlay.yaml
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
overview: 'SAP Emarsys publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Ac API, Administrator API, Blocklist API, and 27 more. Tagged areas include Marketing Automation, Customer Engagement, Email Marketing, Omnichannel, and Customer Data Platform.


  The SAP Emarsys catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SAP Emarsys'' developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, support, and 65 more developer resources.'
plans:
- name: Emarsys Plans Pricing
  plan_count: 0
  slug: emarsys-plans-pricing
random_paper: 16
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
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 25
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 62.1
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 65.8
  previous_composite: 64.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 96.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 80.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
