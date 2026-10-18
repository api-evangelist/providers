---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 129
  human_in_the_loop: 9
  name: Netcorecloud Agentic Access
  operation_count: 202
  slug: netcorecloud-agentic-access
  summary_line: 202 operations · 129 acting · 9 human-in-the-loop
api_count: 9
apis:
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: Contacts API from Netcore Cloud.
  name: Netcore Cloud Contacts API
  slug: netcore-cloud-contacts-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: Attributes API from Netcore Cloud.
  name: Netcore Cloud Attributes API
  slug: netcore-cloud-attributes-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: Trigger API from Netcore Cloud.
  name: Netcore Cloud Trigger API
  slug: netcore-cloud-trigger-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The API Management API from Netcore Cloud — 2 operation(s) for api management.
  name: Netcore Cloud API Management API
  slug: netcorecloud-api-management-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The APN Template API from Netcore Cloud — 3 operation(s) for apn template.
  name: Netcore Cloud APN Template API
  slug: netcorecloud-apn-template-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Auth API from Netcore Cloud — 12 operation(s) for auth.
  name: Netcore Cloud Auth API
  slug: netcorecloud-auth-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Campaign API from Netcore Cloud — 7 operation(s) for campaign.
  name: Netcore Cloud Campaign API
  slug: netcorecloud-campaign-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Clients API from Netcore Cloud — 3 operation(s) for clients.
  name: Netcore Cloud Clients API
  slug: netcorecloud-clients-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Configuration API from Netcore Cloud — 6 operation(s) for configuration.
  name: Netcore Cloud Configuration API
  slug: netcorecloud-configuration-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Consent Management API from Netcore Cloud — 2 operation(s) for consent management.
  name: Netcore Cloud Consent Management API
  slug: netcorecloud-consent-management-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Conversion Tracking API from Netcore Cloud — 1 operation(s) for conversion tracking.
  name: Netcore Cloud Conversion Tracking API
  slug: netcorecloud-conversion-tracking-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Dashboard & Audit API from Netcore Cloud — 3 operation(s) for dashboard & audit.
  name: Netcore Cloud Dashboard & Audit API
  slug: netcorecloud-dashboard-audit-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Domain APIs API from Netcore Cloud — 4 operation(s) for domain apis.
  name: Netcore Cloud Domain APIs API
  slug: netcorecloud-domain-apis-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: Cache refresh endpoints for immediate config propagation.
  name: Netcore Cloud Engine — Cache API
  slug: netcorecloud-engine-cache-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Engine — Health API from Netcore Cloud — 3 operation(s) for engine — health.
  name: Netcore Cloud Engine — Health API
  slug: netcorecloud-engine-health-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Engine — Send API from Netcore Cloud — 2 operation(s) for engine — send.
  name: Netcore Cloud Engine — Send API
  slug: netcorecloud-engine-send-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Engine — Test API from Netcore Cloud — 1 operation(s) for engine — test.
  name: Netcore Cloud Engine — Test API
  slug: netcorecloud-engine-test-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Events API API from Netcore Cloud — 5 operation(s) for events api.
  name: Netcore Cloud Events API
  slug: netcorecloud-events-api-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Export Report API from Netcore Cloud — 1 operation(s) for export report.
  name: Netcore Cloud Export Report API
  slug: netcorecloud-export-report-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Export Templates API from Netcore Cloud — 4 operation(s) for export templates.
  name: Netcore Cloud Export Templates API
  slug: netcorecloud-export-templates-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The IP Management API API from Netcore Cloud — 15 operation(s) for ip management api.
  name: Netcore Cloud IP Management API
  slug: netcorecloud-ip-management-api-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The JSON Message API from Netcore Cloud — 1 operation(s) for json message.
  name: Netcore Cloud JSON Message API
  slug: netcorecloud-json-message-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Message Samples API from Netcore Cloud — 1 operation(s) for message samples.
  name: Netcore Cloud Message Samples API
  slug: netcorecloud-message-samples-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Message Sending API from Netcore Cloud — 1 operation(s) for message sending.
  name: Netcore Cloud Message Sending API
  slug: netcorecloud-message-sending-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Message Sending APIs API from Netcore Cloud — 1 operation(s) for message sending apis.
  name: Netcore Cloud Message Sending APIs API
  slug: netcorecloud-message-sending-apis-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Profile API API from Netcore Cloud — 1 operation(s) for profile api.
  name: Netcore Cloud Profile API
  slug: netcorecloud-profile-api-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Providers API from Netcore Cloud — 2 operation(s) for providers.
  name: Netcore Cloud Providers API
  slug: netcorecloud-providers-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: DLR consolidated report
  name: Netcore Cloud Report API
  slug: netcorecloud-report-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Routes API from Netcore Cloud — 2 operation(s) for routes.
  name: Netcore Cloud Routes API
  slug: netcorecloud-routes-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Rules API from Netcore Cloud — 3 operation(s) for rules.
  name: Netcore Cloud Rules API
  slug: netcorecloud-rules-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Scope API API from Netcore Cloud — 1 operation(s) for scope api.
  name: Netcore Cloud Scope API
  slug: netcorecloud-scope-api-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Send Mail API API from Netcore Cloud — 1 operation(s) for send mail api.
  name: Netcore Cloud Send Mail API
  slug: netcorecloud-send-mail-api-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Stats API API from Netcore Cloud — 1 operation(s) for stats api.
  name: Netcore Cloud Stats API
  slug: netcorecloud-stats-api-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: Subaccount management
  name: Netcore Cloud Subaccount API
  slug: netcorecloud-subaccount-api-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Subaccount APIs API from Netcore Cloud — 5 operation(s) for subaccount apis.
  name: Netcore Cloud Subaccount APIs API
  slug: netcorecloud-subaccount-apis-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Suppression APIs API from Netcore Cloud — 4 operation(s) for suppression apis.
  name: Netcore Cloud Suppression APIs API
  slug: netcorecloud-suppression-apis-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Tags API API from Netcore Cloud — 3 operation(s) for tags api.
  name: Netcore Cloud Tags API
  slug: netcorecloud-tags-api-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Template API API from Netcore Cloud — 2 operation(s) for template api.
  name: Netcore Cloud Template API
  slug: netcorecloud-template-api-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Template APIs API from Netcore Cloud — 7 operation(s) for template apis.
  name: Netcore Cloud Template APIs API
  slug: netcorecloud-template-apis-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Users API from Netcore Cloud — 3 operation(s) for users.
  name: Netcore Cloud Users API
  slug: netcorecloud-users-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Webhook APIs API from Netcore Cloud — 2 operation(s) for webhook apis.
  name: Netcore Cloud Webhook APIs API
  slug: netcorecloud-webhook-apis-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The Webhook Management API from Netcore Cloud — 3 operation(s) for webhook management.
  name: Netcore Cloud Webhook Management API
  slug: netcorecloud-webhook-management-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The WhatsApp Analytics API from Netcore Cloud — 1 operation(s) for whatsapp analytics.
  name: Netcore Cloud WhatsApp Analytics API
  slug: netcorecloud-whatsapp-analytics-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The WhatsApp Flows API from Netcore Cloud — 8 operation(s) for whatsapp flows.
  name: Netcore Cloud WhatsApp Flows API
  slug: netcorecloud-whatsapp-flows-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The WhatsApp Payments API from Netcore Cloud — 4 operation(s) for whatsapp payments.
  name: Netcore Cloud WhatsApp Payments API
  slug: netcorecloud-whatsapp-payments-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The WhatsApp Reach Estimate API from Netcore Cloud — 1 operation(s) for whatsapp reach estimate.
  name: Netcore Cloud WhatsApp Reach Estimate API
  slug: netcorecloud-whatsapp-reach-estimate-api
- baseURL: https://netcoreapi-main-prod-us.netcorein.com/v5/
  baseurl_source: declared
  description: The WhatsApp Templates API from Netcore Cloud — 11 operation(s) for whatsapp templates.
  name: Netcore Cloud WhatsApp Templates API
  slug: netcorecloud-whatsapp-templates-api
artifact_total: 74
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/agentic-access/netcorecloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/netcorecloud-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/rules/netcorecloud-rules.yml
  title: ''
  type: Spectral
  url: rules/netcorecloud-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/json-ld/netcorecloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/netcorecloud-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/vocabulary/netcorecloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/netcorecloud-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/data-model/netcorecloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/netcorecloud-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://netcore.ai/security/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/errors/netcorecloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/netcorecloud-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/llms/netcorecloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/netcorecloud-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/well-known/netcorecloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/netcorecloud-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/hosts/netcorecloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netcorecloud-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/integrations/netcorecloud-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/netcorecloud-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/vendors/netcorecloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/netcorecloud-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://netcore.ai/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://netcore.ai/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://netcore.ai/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://netcore.ai/newsroom/
- group: start
  title: ''
  type: Login
  url: https://netcore.ai/login/
- group: other
  title: ''
  type: Leadership
  url: https://netcore.ai/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/authentication/netcorecloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/netcorecloud-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/security/netcorecloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/netcorecloud-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/security/netcorecloud-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/netcorecloud-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netcorecloud/refs/heads/main/security/netcorecloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netcorecloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://netcorecloud.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.netcorecloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://emaildocs.netcorecloud.com/
- group: docs
  title: ''
  type: APIReference
  url: https://emaildocs.netcorecloud.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://cedocs.netcorecloud.com/
- group: company
  title: ''
  type: Blog
  url: https://netcore.ai/blog/
created: '2026-10-13'
description: Netcore Cloud (Netcore) is a customer engagement and CPaaS platform offering transactional and marketing email delivery (formerly Pepipost), SMS, WhatsApp and RCS messaging, email routing (Orbit Router), and a customer engagement suite with contacts, attributes, campaigns, templates, exports and event trigger APIs, documented publicly on ReadMe-hosted developer portals.
image: https://netcore.ai/wp-content/uploads/2024/03/NC_WebsitePreview_01.webp
json_schemas:
- name: AudienceDetails
  property_count: 2
  slug: netcorecloud-audience-details
- name: CampaignSpecific
  property_count: 20
  slug: netcorecloud-campaign-specific
- name: ConsentResponse
  property_count: 3
  slug: netcorecloud-consent-response
- name: ConversionTracking
  property_count: 5
  slug: netcorecloud-conversion-tracking
- name: DLRReportResponse
  property_count: 4
  slug: netcorecloud-dlrreport-response
- name: FilterBlock
  property_count: 2
  slug: netcorecloud-filter-block
- name: FlowListSuccessResponse
  property_count: 4
  slug: netcorecloud-flow-list-success-response
- name: GoogleAnalytics
  property_count: 7
  slug: netcorecloud-google-analytics
- name: IncomingAuthUpsert
  property_count: 7
  slug: netcorecloud-incoming-auth-upsert
- name: JsonSingleApiV2Request
  property_count: 26
  slug: netcorecloud-json-single-api-v2-request
- name: NetcorePayload
  property_count: 6
  slug: netcorecloud-netcore-payload
- name: OutputBlock
  property_count: 4
  slug: netcorecloud-output-block
- name: PaymentStatusResponse
  property_count: 3
  slug: netcorecloud-payment-status-response
- name: RefundRequest
  property_count: 4
  slug: netcorecloud-refund-request
- name: RefundResponse
  property_count: 3
  slug: netcorecloud-refund-response
- name: RouteCreate
  property_count: 13
  slug: netcorecloud-route-create
- name: Route
  property_count: 15
  slug: netcorecloud-route
- name: RuleCreate
  property_count: 6
  slug: netcorecloud-rule-create
- name: Rule
  property_count: 9
  slug: netcorecloud-rule
- name: TemplateListSuccessResponse
  property_count: 3
  slug: netcorecloud-template-list-success-response
jsonld:
- class_count: 86
  name: Netcorecloud Context
  property_count: 220
  slug: netcorecloud-context
layout: provider
modified: '2026-10-13'
name: Netcore Cloud
nav: Providers
network: true
overview: 'Netcore Cloud publishes 47 API contracts indexed on the [APIs.io](https://apis.io/) network, including Contacts API, Attributes API, Trigger API, and 44 more. Tagged areas include Company, Email, SMS, WhatsApp, and RCS.


  The Netcore Cloud catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Netcore Cloud''s developer surface includes authentication, documentation, API reference, engineering blog, and 24 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Netcore Cloud API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 5
  slug: netcorecloud-rules
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 17.4
    contract_quality: 65.4
    developer_ergonomics: 40.5
    discoverability: 82.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 47
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 30.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 33.3
security:
- kind: authentication
  name: Netcorecloud Authentication
  slug: netcorecloud-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Netcorecloud Domain Security
  slug: netcorecloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Netcorecloud Vulnerability Disclosure
  slug: netcorecloud-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Netcorecloud Trust Center
  slug: netcorecloud-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: netcorecloud
tags:
- Company
- Email
- SMS
- WhatsApp
- RCS
- CPaaS
- Customer Engagement
- Marketing Automation
- Messaging
website: https://netcorecloud.com
---
