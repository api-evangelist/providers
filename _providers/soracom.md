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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 616
  human_in_the_loop: 72
  name: Soracom Agentic Access
  operation_count: 960
  slug: soracom-agentic-access
  summary_line: 960 operations · 616 acting · 72 human-in-the-loop
api_count: 45
apis:
- description: Manage Soracom Air for Cellular SIMs (and Subscribers) — list, get, create Arc virtual SIMs, activate/deactivate/suspend/terminate, set group binding, set IMEI lock, view session events, manage SIM pr
  name: Soracom SIM Management API
  slug: soracom-sim-api
- description: 'Manage Soracom groups and per-service configuration. Groups bind SIMs and devices to namespaced configuration for SoracomAir, SoracomBeam, SoracomFunnel, SoracomFunk, SoracomHarvest, SoracomJunction, '
  name: Soracom Group Configuration API
  slug: soracom-group-api
- description: Retrieve usage charges (monthly bills, daily bill items, per-SIM and per-bill-item summaries), export bills to CSV, manage payment methods, register coupons, manage orders, and configure shipping addr
  name: Soracom Billing API
  slug: soracom-billing-api
- description: Retrieve cellular data usage statistics (per SIM/subscriber/group/account), API and Napter audit logs, operator error logs, and diagnostic features.
  name: Soracom Stats and Diagnostics API
  slug: soracom-stats-api
- description: Authenticate operators (email/password or AuthKey), issue short-lived API Keys + Tokens, manage operator profile, SAM (Soracom Access Management) users and roles, MFA settings, registered email addres
  name: Soracom Auth and Access Management API
  slug: soracom-auth-api
- description: Manage Soracom Lagoon (managed Grafana) subscription, plan tier, organization, dashboards, users, licenses, and data sources.
  name: Soracom Lagoon API
  slug: soracom-lagoon-api
- description: Manage Soracom Cloud Camera Services (SoraCam) devices, livestream URLs, image exports, recording exports, motion events, atomic timestamps, and dedicated cellular pack provisioning.
  name: Soracom Cloud Camera Services API
  slug: soracom-soracam-api
- description: Batch processing — create batch groups, define jobs that invoke API operations across many SIMs or devices, and inspect tasks for status and results.
  name: Soracom Batch API
  slug: soracom-batch-api
- description: '[Soracom Query](/en/docs/query/)'
  name: Soracom Analysis API
  slug: soracom-analysis-api
- description: 'The API Sandbox: Coupon API from Soracom — 1 operation(s) for api sandbox: coupon.'
  name: 'Soracom API Sandbox: Coupon API'
  slug: soracom-api-sandbox-coupon-api
- description: 'The API Sandbox: Operator API from Soracom — 3 operation(s) for api sandbox: operator.'
  name: 'Soracom API Sandbox: Operator API'
  slug: soracom-api-sandbox-operator-api
- description: 'The API Sandbox: Order API from Soracom — 1 operation(s) for api sandbox: order.'
  name: 'Soracom API Sandbox: Order API'
  slug: soracom-api-sandbox-order-api
- description: 'The API Sandbox: Stats API from Soracom — 2 operation(s) for api sandbox: stats.'
  name: 'Soracom API Sandbox: Stats API'
  slug: soracom-api-sandbox-stats-api
- description: 'The API Sandbox: Subscriber API from Soracom — 1 operation(s) for api sandbox: subscriber.'
  name: 'Soracom API Sandbox: Subscriber API'
  slug: soracom-api-sandbox-subscriber-api
- description: '[Audit logs](/en/docs/api-audit-logs/)'
  name: Soracom AuditLog API
  slug: soracom-auditlog-api
- description: '[Cell tower location information](/en/docs/air/get-location-info/#get-cell-tower-location-information)'
  name: Soracom CellLocation API
  slug: soracom-celllocation-api
- description: '[Credentials store](/en/docs/credentials-store/) Create, update, and delete credentials'
  name: Soracom Credential API
  slug: soracom-credential-api
- description: '[Soracom Harvest Data](/en/docs/harvest/)'
  name: Soracom DataEntry API
  slug: soracom-dataentry-api
- description: '[Soracom Inventory devices](/en/docs/inventory/)'
  name: Soracom Device API
  slug: soracom-device-api
- description: '[Soracom Inventory object model](/en/docs/inventory/define-custom-object/)'
  name: Soracom DeviceObjectModel API
  slug: soracom-deviceobjectmodel-api
- description: '[Diagnostic features](/en/guides/diagnostic/)'
  name: Soracom Diagnostic API
  slug: soracom-diagnostic-api
- description: '[Email addresses](/en/docs/email/)'
  name: Soracom Email API
  slug: soracom-email-api
- description: '[Event handlers](/en/docs/event-handler/)'
  name: Soracom EventHandler API
  slug: soracom-eventhandler-api
- description: '[Soracom Harvest Files](/en/docs/harvest/)'
  name: Soracom FileEntry API
  slug: soracom-fileentry-api
- description: 'Download files exported by the following APIs: - [Billing](#/Billing) - [Payment: exportPaymentStatement](#/Payment/exportPaymentStatement) - [Stats](#/Stats) - [Subscriber:exportSubscribers](#/Subscr'
  name: Soracom Files API
  slug: soracom-files-api
- description: Gadget API compatible devices<ul><li>[SoraCam dedicated cellular pack](/en/guides/soracom-cloud-camera-services/setting-cellular-pack/)</li></ul>
  name: Soracom Gadget API
  slug: soracom-gadget-api
- description: Error logs
  name: Soracom Log API
  slug: soracom-log-api
- description: '[Soracom Air for LoRaWAN](/en/docs/air-for-lorawan/) devices'
  name: Soracom LoraDevice API
  slug: soracom-loradevice-api
- description: '[Soracom Air for LoRaWAN](/en/docs/air-for-lorawan/) gateways'
  name: Soracom LoraGateway API
  slug: soracom-loragateway-api
- description: '[Soracom Air for LoRaWAN](/en/docs/air-for-lorawan/) network sets'
  name: Soracom LoraNetworkSet API
  slug: soracom-loranetworkset-api
- description: '- Operator management - Update registration information - Password changes - [Multi-factor authentication](/en/docs/mfa/)'
  name: Soracom Operator API
  slug: soracom-operator-api
- description: '- [Coupon codes](/en/guides/accounting/payment/register-coupon/) - [Long term discounts](/en/docs/air/volume-discount/) - Order management - Product catalog'
  name: Soracom Order API
  slug: soracom-order-api
- description: '- [Coupon codes](/en/guides/accounting/payment/register-coupon/) - [Usage charges (billing details)](/en/guides/accounting/check-usage/) - [Payment methods](/en/guides/accounting/payment/) - [Long ter'
  name: Soracom Payment API
  slug: soracom-payment-api
- description: '[Soracom Napter](/en/docs/napter/)'
  name: Soracom PortMapping API
  slug: soracom-portmapping-api
- description: Search SIMs, Soracom Inventory devices, and Sigfox devices
  name: Soracom Query API
  slug: soracom-query-api
- description: The ResourceSummary API from Soracom — 1 operation(s) for resourcesummary.
  name: Soracom ResourceSummary API
  slug: soracom-resourcesummary-api
- description: '[Access management (Soracom Access Management)](/en/docs/sam/)'
  name: Soracom Role API
  slug: soracom-role-api
- description: Shipping address operations for direct sales
  name: Soracom ShippingAddress API
  slug: soracom-shippingaddress-api
- description: '[Soracom Air for Sigfox](/en/docs/air-for-sigfox/) devices'
  name: Soracom SigfoxDevice API
  slug: soracom-sigfoxdevice-api
- description: '[eSIM profiles](/en/docs/air/provision-esim/)'
  name: Soracom SimProfileOrder API
  slug: soracom-simprofileorder-api
- description: '[Soracom Orbit](/en/docs/orbit/) Soralet'
  name: Soracom Soralet API
  slug: soracom-soralet-api
- description: '[Soracom Air for Cellular](/en/docs/air/) SIM information, operations, and cancellation'
  name: Soracom Subscriber API
  slug: soracom-subscriber-api
- description: '[Email addresses](/en/docs/email/)'
  name: Soracom SystemNotification API
  slug: soracom-systemnotification-api
- description: '- [Access management (Soracom Access Management)](/en/docs/sam/) - Password changes - [Multi-factor authentication](/en/docs/mfa/) - [Switch user](/en/docs/switch-user/) trust policy configuration'
  name: Soracom User API
  slug: soracom-user-api
- description: '- [Virtual Private Gateway (VPG)](/en/docs/vpg/) (Canal / Direct / Door / Gate) - [Soracom Junction](/en/docs/junction/) - [Soracom Peek](/en/docs/peek/)'
  name: Soracom VirtualPrivateGateway API
  slug: soracom-virtualprivategateway-api
arazzos:
- description: Confirm a SIM exists, read its current session status, and pull its session event history for an audit window.
  name: Soracom Audit SIM Session Events
  slug: soracom-audit-sim-session-events-workflow
- description: Confirm a SIM exists, pull its Harvest Data entries, and fall back to the generic Harvest endpoint when empty.
  name: Soracom Collect SIM Harvest Data
  slug: soracom-collect-sim-harvest-data-workflow
- description: Create an event handler that caps a group's monthly traffic and notifies the operator, then verify it.
  name: Soracom Create Monthly Traffic Event Handler
  slug: soracom-create-traffic-event-handler-workflow
- description: Read a SIM, deactivate it only when it is currently active, then confirm the inactive status.
  name: Soracom Deactivate IoT SIM with Guard
  slug: soracom-deactivate-sim-with-guard-workflow
- description: Read a finalized monthly bill, kick off an async detailed-billing CSV export, and poll until the download URL is ready.
  name: Soracom Export Monthly Billing CSV
  slug: soracom-export-monthly-billing-workflow
- description: Create a SIM group, apply a service configuration, attach an existing SIM, and verify the binding.
  name: Soracom Provision Group and Attach SIM
  slug: soracom-provision-group-and-attach-sim-workflow
- description: Register a physical IoT SIM to the operator, activate it, bind it to a SIM group, and confirm its state.
  name: Soracom Register and Activate IoT SIM
  slug: soracom-register-and-activate-sim-workflow
- description: List currently registered coupons, register a new coupon code, then re-list to confirm the credit applied.
  name: Soracom Register and Verify Coupon
  slug: soracom-register-and-verify-coupon-workflow
- description: Create a Soracom Inventory device, bind it to an Inventory group, and confirm the binding.
  name: Soracom Register Inventory Device to Group
  slug: soracom-register-device-to-group-workflow
- description: Register a subscriber by IMSI, activate it, bind it to a group, and confirm its state.
  name: Soracom Register Subscriber to Group
  slug: soracom-register-subscriber-to-group-workflow
- description: Look up a SIM, branch on whether it is active, and send a downlink SMS only when it can receive one.
  name: Soracom Send SMS to Active IoT SIM
  slug: soracom-send-sms-to-active-sim-workflow
artifact_total: 144
collections:
- collection_type: postman
  name: Soracom Analysis and Query API
  slug: postman-soracom-analysis-query-api
- collection_type: postman
  name: Soracom Auth and Access Management API
  slug: postman-soracom-auth-api
- collection_type: postman
  name: Soracom Batch API
  slug: postman-soracom-batch-api
- collection_type: postman
  name: Soracom Billing API
  slug: postman-soracom-billing-api
- collection_type: postman
  name: Soracom Event Handler API
  slug: postman-soracom-event-handler-api
- collection_type: postman
  name: Soracom Group Configuration API
  slug: postman-soracom-group-api
- collection_type: postman
  name: Soracom Harvest API
  slug: postman-soracom-harvest-api
- collection_type: postman
  name: Soracom Inventory API
  slug: postman-soracom-inventory-api
- collection_type: postman
  name: Soracom Lagoon API
  slug: postman-soracom-lagoon-api
- collection_type: postman
  name: Soracom Air for LoRaWAN API
  slug: postman-soracom-lorawan-api
- collection_type: postman
  name: Soracom Napter API
  slug: postman-soracom-napter-api
- collection_type: postman
  name: Soracom API
  slug: postman-soracom-platform-api
- collection_type: postman
  name: SORACOM SANDBOX API
  slug: postman-soracom-sandbox-api
- collection_type: postman
  name: Soracom Air for Sigfox API
  slug: postman-soracom-sigfox-api
- collection_type: postman
  name: Soracom SIM Management API
  slug: postman-soracom-sim-api
- collection_type: postman
  name: Soracom Cloud Camera Services API
  slug: postman-soracom-soracam-api
- collection_type: postman
  name: Soracom Stats and Diagnostics API
  slug: postman-soracom-stats-api
- collection_type: postman
  name: Soracom Virtual Private Gateway API
  slug: postman-soracom-vpg-api
- collection_type: open
  name: Soracom Analysis and Query API
  slug: open-soracom-analysis-query-api
- collection_type: open
  name: Soracom Auth and Access Management API
  slug: open-soracom-auth-api
- collection_type: open
  name: Soracom Batch API
  slug: open-soracom-batch-api
- collection_type: open
  name: Soracom Billing API
  slug: open-soracom-billing-api
- collection_type: open
  name: Soracom Event Handler API
  slug: open-soracom-event-handler-api
- collection_type: open
  name: Soracom Group Configuration API
  slug: open-soracom-group-api
- collection_type: open
  name: Soracom Harvest API
  slug: open-soracom-harvest-api
- collection_type: open
  name: Soracom Inventory API
  slug: open-soracom-inventory-api
- collection_type: open
  name: Soracom Lagoon API
  slug: open-soracom-lagoon-api
- collection_type: open
  name: Soracom Air for LoRaWAN API
  slug: open-soracom-lorawan-api
- collection_type: open
  name: Soracom Napter API
  slug: open-soracom-napter-api
- collection_type: open
  name: Soracom API
  slug: open-soracom-platform-api
- collection_type: open
  name: SORACOM SANDBOX API
  slug: open-soracom-sandbox-api
- collection_type: open
  name: Soracom Air for Sigfox API
  slug: open-soracom-sigfox-api
- collection_type: open
  name: Soracom SIM Management API
  slug: open-soracom-sim-api
- collection_type: open
  name: Soracom Cloud Camera Services API
  slug: open-soracom-soracam-api
- collection_type: open
  name: Soracom Stats and Diagnostics API
  slug: open-soracom-stats-api
- collection_type: open
  name: Soracom Virtual Private Gateway API
  slug: open-soracom-vpg-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/soracom-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soracom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/soracom-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/soracom/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/soracom-audit-sim-session-events-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/soracom-collect-sim-harvest-data-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/soracom-create-traffic-event-handler-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/soracom-deactivate-sim-with-guard-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/soracom-export-monthly-billing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/soracom-provision-group-and-attach-sim-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/soracom-register-and-activate-sim-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/soracom-register-and-verify-coupon-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/soracom-register-device-to-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/soracom-register-subscriber-to-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/soracom-send-sms-to-active-sim-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.soracom.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/
- group: docs
  title: ''
  type: Documentation
  url: https://users.soracom.io/ja-jp/tools/api/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.soracom.io/en/start/
- group: start
  title: ''
  type: Signup
  url: https://console.soracom.io/#/signup
- group: start
  title: ''
  type: Login
  url: https://console.soracom.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.soracom.io/pricing/
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.soracom.io/en/docs/reference/fees/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.soracom.io/
- group: company
  title: ''
  type: Blog
  url: https://soracom.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.soracom.io/
- group: company
  title: ''
  type: Press
  url: https://www.soracom.io/press-releases/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.soracom.io/terms_of_service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.soracom.io/privacy_policy/
- group: operate
  title: ''
  type: Support
  url: https://support.soracom.io
- group: operate
  title: ''
  type: Contact
  url: https://www.soracom.io/contact/
- group: operate
  title: ''
  type: Forums
  url: https://discuss.soracom.io
- group: other
  title: ''
  type: Coverage
  url: https://www.soracom.io/pricing/countries/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/air/sim-types/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/tools/api/endpoints/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/tools/api/key-and-token/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/tools/api/how-to-read-api-reference/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soracom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soracom-labs
- group: build
  title: ''
  type: CLI
  url: https://github.com/soracom/soracom-cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/soracom/soracom-sdk-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/soracom/soracom-sdk-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/soracom/soracom-sdk-swift
- group: build
  title: ''
  type: SDKs
  url: https://github.com/soracom/soracom-inventory-agent-for-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/soracom/krypton-client-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/soracom/endorse-client-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/soracom/soracom-krypton-client-for-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/soracom/soracom-endorse-client-for-java
- group: build
  title: ''
  type: Tools
  url: https://github.com/soracom/soratun
- group: build
  title: ''
  type: Tools
  url: https://github.com/soracom/soraql
- group: build
  title: ''
  type: Tools
  url: https://github.com/soracom/homebrew-soracom-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/soracom/multus-multivpc-cni
- group: build
  title: ''
  type: Tools
  url: https://github.com/soracom/orbit-sdk-rust
- group: build
  title: ''
  type: Tools
  url: https://github.com/soracom/orbit-sdk-tinygo
- group: build
  title: ''
  type: Tools
  url: https://github.com/soracom/orbit-sdk-c
- group: build
  title: ''
  type: Tools
  url: https://github.com/soracom/orbit-sdk-assemblyscript
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/soracom/handson
- group: build
  title: ''
  type: Library
  url: https://github.com/soracom/SORACOM-LoRaWAN
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/start/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/air/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/beam/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/funnel/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/funk/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/harvest/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/lagoon-v3/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/inventory/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/napter/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/orbit/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/vpg/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/sam/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/event-handler/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/query/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.soracom.io/en/docs/credentials-store/
- group: other
  title: ''
  type: Coverage
  url: https://developers.soracom.io/en/docs/air/speed-class/
- group: commercial
  title: ''
  type: Plans
  url: plans/soracom-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/soracom-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/soracom-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/soracom-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/soracom-rules.yml
created: '2026-05-25T00:00:00.000Z'
description: Soracom is a global IoT cellular connectivity and platform provider headquartered in Tokyo, founded in 2014, with regional operations in the US (Soracom Global) and EU. The platform pairs multicarrier SIMs (physical, eSIM, iSIM) across 170+ countries with a deep platform of cloud integration services (Beam, Funnel, Funk), data services (Harvest, Lagoon, Query, Orbit), device management (Inventory, Krypton, Endorse, Napter), and network gateways (VPG / Canal / Direct / Door / Gate / Junction / Peek). Soracom exposes the entire stack through a coverage-aware REST API documented at users.soracom.io and maintained as a public OpenAPI 3.0 specification in the soracom-cli GitHub repo.
examples:
- key_count: 2
  name: Soracom Auth Example
  slug: soracom-auth-example
- key_count: 2
  name: Soracom Bill Latest Example
  slug: soracom-bill-latest-example
- key_count: 2
  name: Soracom Harvest Data Example
  slug: soracom-harvest-data-example
- key_count: 2
  name: Soracom Napter Create Example
  slug: soracom-napter-create-example
- key_count: 2
  name: Soracom Sim List Example
  slug: soracom-sim-list-example
features:
- Global multicarrier cellular IoT connectivity spanning 170+ countries on Air for Cellular (plan01s)
- Region-specific plans — plan-US, plan-D, plan-K, plan-DU (Japan), planP1 (60+ countries eSIM), planX series, plan-NL1 — for tuned coverage and price
- eSIM and iSIM (planP1/planX1/planX2) with multi-IMSI profile management
- Soracom Arc — Wireguard-based virtual SIM that joins non-cellular IP devices via soratun
- Soracom Air for LoRaWAN and Air for Sigfox — managed LPWAN connectivity
- Soracom Beam — cloud proxy for TLS termination and HTTP/MQTT/TCP/UDP/WebSocket protocol conversion
- Soracom Funnel — adapter that forwards device payloads to AWS Kinesis/IoT, Azure Event Hubs, GCP Pub/Sub, and more
- Soracom Funk — serverless invocation of AWS Lambda / Azure Functions / Google Cloud Functions from device payloads
- Soracom Harvest Data — managed time-series store; Harvest Files for binary uploads
- Soracom Orbit — inline WebAssembly Soralets that transform device payloads in flight
- Soracom Lagoon — managed Grafana-style dashboards (Free / Maker $9.80/mo / Pro $49.80/mo)
- Soracom Query — columnar SQL analytics over SIM session, location, and data history
- Soracom Napter — on-demand secure remote TCP port mapping into SIM-attached devices
- Soracom Inventory — LwM2M device registration, object models, observe/notify, and remote execution
- Soracom Endorse — hardware-rooted SIM-based device authentication
- Soracom Krypton — credential and certificate provisioning rooted in SIM identity
- Virtual Private Gateway (VPG) — Canal (AWS VPC peering), Direct (AWS Direct Connect), Door (IPSec VPN), Gate (reverse-NAT to cloud)
- Soracom Junction — Layer-3 packet rule engine (mirror/inspect/redirect) attached to VPG
- Soracom Peek — managed packet capture per SIM or per VPG
- Soracom Flux — visual workflow automation across Soracom data
- Soracom Access Management (SAM) — sub-users, roles, IAM-style policy documents, MFA
- Switch-user (cross-operator delegation) for distributors and managed-service providers
- Coverage-aware API endpoints — api.soracom.io / jp.api.soracom.io (Japan) and g.api.soracom.io (global)
- Soracom Sandbox API at api-sandbox.soracom.io for safe integration testing
- Auto-generated soracom CLI built directly from the OpenAPI spec
- Official SDKs in Go and Ruby; community SDKs and clients in Java, Swift, JavaScript
- Orbit SDKs for Rust, TinyGo, C, and AssemblyScript
- Soracom Cloud Camera Services (SoraCam) — managed cameras with livestream, image exports, motion events
- Reverse-NAT, IMEI lock, IP whitelisting, and TLS-everywhere posture for industrial IoT
- Audit logs for all API calls and all Napter sessions
- Direct billing endpoints (/v1/bills) with daily and monthly granularity and CSV export
finops:
- name: Soracom Finops
  service_category: IoT and Connectivity
  slug: soracom-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soracom.png
json_schemas:
- name: Soracom Harvest Data Entry
  property_count: 6
  slug: soracom-data-entry
- name: Soracom Inventory Device
  property_count: 9
  slug: soracom-device
- name: Soracom Group
  property_count: 7
  slug: soracom-group
- name: Soracom Napter Port Mapping
  property_count: 9
  slug: soracom-port-mapping
- name: Soracom SIM
  property_count: 16
  slug: soracom-sim
json_structures:
- name: Soracom Device Structure
  property_count: 9
  slug: soracom-device-structure
- name: Soracom Sim Structure
  property_count: 13
  slug: soracom-sim-structure
jsonld:
- class_count: 0
  name: Soracom Context
  property_count: 7
  slug: soracom-context
layout: provider
modified: '2026-05-25'
name: Soracom
nav: Providers
network: true
overview: 'Soracom publishes 45 APIs on the [APIs.io](https://apis.io/) network, including SIM Management API, Group Configuration API, Billing API, and 42 more. Tagged areas include IoT, Cellular, LPWAN, SIM, and LoRaWAN.


  The Soracom catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Soracom''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 72 more developer resources.'
plans:
- name: Soracom Plans Pricing
  plan_count: 17
  slug: soracom-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 0
  name: Soracom Rate Limits
  slug: soracom-rate-limits
rules:
- name: Soracom API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: soracom-jsonschema-spectral-rules
- name: Soracom API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: soracom-rules
score:
  band: strong
  composite: 63.9
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 71.8
    developer_ergonomics: 71.7
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 63.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 45
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soracom/refs/heads/main/screenshots/soracom-2026-06-20T194218.png
security:
- kind: authentication
  name: Soracom Authentication
  slug: soracom-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Soracom Domain Security
  slug: soracom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soracom
tags:
- IoT
- Cellular
- LPWAN
- SIM
- LoRaWAN
- Sigfox
- MVNO
- Connectivity
- Edge
- Japan
website: https://www.soracom.io
---
