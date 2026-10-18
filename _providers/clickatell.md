---
agent_readiness:
  band: agent-aware
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Clickatell Agentic Access
  operation_count: 29
  slug: clickatell-agentic-access
  summary_line: 29 operations · 20 acting
api_count: 7
apis:
- baseURL: https://your-server.com
  baseurl_source: declared
  description: The Chat 2 Pay API API from Clickatell — 8 operation(s) for chat 2 pay api.
  name: Clickatell Chat 2 Pay API
  slug: clickatell-chat-2-pay-api-api
- baseURL: https://your-server.com
  baseurl_source: declared
  description: The Chat 2 Pay API Client Callbacks API from Clickatell — 3 operation(s) for chat 2 pay api client callbacks.
  name: Clickatell Chat 2 Pay API Client Callbacks API
  slug: clickatell-chat-2-pay-api-client-callbacks-api
- baseURL: https://your-server.com
  baseurl_source: declared
  description: The External Link Callback API from Clickatell — 1 operation(s) for external link callback.
  name: Clickatell External Link Callback API
  slug: clickatell-external-link-callback-api
- baseURL: https://your-server.com
  baseurl_source: declared
  description: The One API API from Clickatell — 6 operation(s) for one api.
  name: Clickatell One API
  slug: clickatell-one-api-api
- baseURL: https://your-server.com
  baseurl_source: declared
  description: '<b>Forward Compatibility</b><br>While the basic callback structure will remain constant:<br><pre> { "integrationId": "string", "integrationName": "string", "event": {} }</pre>There are constant additi'
  name: Clickatell One API Client Callbacks API
  slug: clickatell-one-api-client-callbacks-api
- baseURL: https://your-server.com
  baseurl_source: declared
  description: The SMS API API from Clickatell — 3 operation(s) for sms api.
  name: Clickatell SMS API
  slug: clickatell-sms-api-api
- baseURL: https://your-server.com
  baseurl_source: declared
  description: The SMS Client Callbacks API from Clickatell — 2 operation(s) for sms client callbacks.
  name: Clickatell SMS Client Callbacks API
  slug: clickatell-sms-client-callbacks-api
- baseURL: https://your-server.com
  baseurl_source: declared
  description: The Wait for Callback API from Clickatell — 1 operation(s) for wait for callback.
  name: Clickatell Wait for Callback API
  slug: clickatell-wait-for-callback-api
artifact_total: 37
common:
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/integrations/clickatell-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/clickatell-integration-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/agentic-access/clickatell-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clickatell-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/rules/clickatell-rules.yml
  title: ''
  type: Spectral
  url: rules/clickatell-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/json-ld/clickatell-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clickatell-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/vocabulary/clickatell-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clickatell-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/data-model/clickatell-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clickatell-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/errors/clickatell-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clickatell-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/conformance/clickatell-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clickatell-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/llms/clickatell-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clickatell-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/well-known/clickatell-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clickatell-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/hosts/clickatell-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clickatell-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/vendors/clickatell-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clickatell-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/packages/clickatell-packages.yml
  title: ''
  type: SDKs
  url: packages/clickatell-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/packages/clickatell-packages.yml
  title: ''
  type: Packages
  url: packages/clickatell-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.clickatell.com/whatsapp/getting-started/whatsapp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/authentication/clickatell-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clickatell-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clickatell/refs/heads/main/security/clickatell-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clickatell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clickatell.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.clickatell.com/developers-api-reference/reference/clickatell-api-reference
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.clickatell.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.clickatell.com/release-notes
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clickatell.com/packages/
- group: operate
  title: ''
  type: Support
  url: https://help.clickatell.com/
- group: auth
  title: ''
  type: Security
  url: https://www.clickatell.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: https://help.clickatell.com/llms.txt
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.clickatell.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Clickatell is a chat commerce and CPaaS company offering SMS and WhatsApp messaging (One API), the SMS API, Chat 2 Pay payments-in-chat, and Chat Flow workflow APIs for businesses.
json_schemas:
- name: DetailedWidgetConfigResponse
  property_count: 7
  slug: clickatell-detailed-widget-config-response
- name: Externallink
  property_count: 3
  slug: clickatell-externallink
- name: OmniMediaUploadResponse
  property_count: 3
  slug: clickatell-omni-media-upload-response
- name: OmniMessageListResponse
  property_count: 3
  slug: clickatell-omni-message-list-response
- name: OmniMessageStatusResponse
  property_count: 2
  slug: clickatell-omni-message-status-response
- name: OmniReplyCallbackRequest
  property_count: 3
  slug: clickatell-omni-reply-callback-request
- name: OmniStatusCallbackRequest
  property_count: 3
  slug: clickatell-omni-status-callback-request
- name: PayByLinkRequest
  property_count: 18
  slug: clickatell-pay-by-link-request
- name: PayByLinkTransactionLogResponse
  property_count: 8
  slug: clickatell-pay-by-link-transaction-log-response
- name: PaymentGatewayOperationResultResponse
  property_count: 13
  slug: clickatell-payment-gateway-operation-result-response
- name: PaymentReceiptResponse
  property_count: 6
  slug: clickatell-payment-receipt-response
- name: ReplyStatusNotificationRequest
  property_count: 1
  slug: clickatell-reply-status-notification-request
- name: SendBulkMessageRequest
  property_count: 1
  slug: clickatell-send-bulk-message-request
- name: SendMessageRequest
  property_count: 9
  slug: clickatell-send-message-request
- name: SendMessagesListResponse
  property_count: 4
  slug: clickatell-send-messages-list-response
- name: SendOmniChannelMessagesRequest
  property_count: 1
  slug: clickatell-send-omni-channel-messages-request
- name: SendPaymentOutcomeRequest
  property_count: 12
  slug: clickatell-send-payment-outcome-request
- name: SendReplyMessageRequest
  property_count: 11
  slug: clickatell-send-reply-message-request
- name: Sms status callback
  property_count: 10
  slug: clickatell-sms-status-callback
- name: TransactionStatusEndpointResponse
  property_count: 22
  slug: clickatell-transaction-status-endpoint-response
- name: TransactionStatusNotificationResponse
  property_count: 21
  slug: clickatell-transaction-status-notification-response
- name: Waitforcallback
  property_count: 0
  slug: clickatell-waitforcallback
- name: WhatsAppNotificationListResponse
  property_count: 3
  slug: clickatell-whats-app-notification-list-response
- name: WidgetConfigResponse
  property_count: 7
  slug: clickatell-widget-config-response
jsonld:
- class_count: 93
  name: Clickatell Context
  property_count: 190
  slug: clickatell-context
layout: provider
modified: '2026-10-13'
name: Clickatell
nav: Providers
network: true
overview: 'Clickatell publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chat 2 Pay API, Chat 2 Pay API Client Callbacks API, External Link Callback API, and 5 more. Tagged areas include Company, SMS, WhatsApp, Messaging, and CPaaS.


  The Clickatell catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clickatell''s developer surface includes getting-started guide, authentication, documentation, changelog, pricing, support, and 19 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Clickatell API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 2
  slug: clickatell-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 58.8
    catalog_earned_first_party: 0.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 57.1
    developer_ergonomics: 54.8
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 14.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Clickatell Authentication
  slug: clickatell-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Clickatell Domain Security
  slug: clickatell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clickatell
tags:
- Company
- SMS
- WhatsApp
- Messaging
- CPaaS
- Chat Commerce
- Payments
website: https://www.clickatell.com
---
