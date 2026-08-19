---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Allegion Agentic Access
  operation_count: 20
  slug: allegion-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 5
apis:
- description: Create, schedule, update, and delete numeric access codes per device
  name: Allegion Access Codes API
  slug: allegion-access-codes-api
- description: Track the asynchronous status of lock / unlock and configuration commands
  name: Allegion Commands API
  slug: allegion-commands-api
- description: ENGAGE hardware discovery and commissioning (Allegion Device Communication SDK)
  name: Allegion Devices API
  slug: allegion-devices-api
- description: Upload, delete, and list BLE Mobile Credentials for end users
  name: Allegion Mobile Credentials API
  slug: allegion-mobile-credentials-api
- description: Subscribe partner endpoints to device, command, access code, and account events
  name: Allegion Webhook Subscriptions API
  slug: allegion-webhook-subscriptions-api
artifact_total: 56
collections:
- collection_type: postman
  name: ENGAGE Cloud Credentialing Access Codes API
  slug: postman-allegion-access-codes-api
- collection_type: postman
  name: ENGAGE Cloud Credentialing Access Codes Commands API
  slug: postman-allegion-commands-api
- collection_type: postman
  name: ENGAGE Cloud Credentialing Access Codes Devices API
  slug: postman-allegion-devices-api
- collection_type: postman
  name: ENGAGE Cloud Credentialing Access Codes Mobile Credentials API
  slug: postman-allegion-mobile-credentials-api
- collection_type: postman
  name: ENGAGE Cloud Credentialing Access Codes Webhook Subscriptions API
  slug: postman-allegion-webhook-subscriptions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ENGAGE Cloud Credentialing Access Codes API
  slug: open-allegion-access-codes-api
- collection_type: open
  name: ENGAGE Cloud Credentialing Access Codes Commands API
  slug: open-allegion-commands-api
- collection_type: open
  name: ENGAGE Cloud Credentialing Access Codes Devices API
  slug: open-allegion-devices-api
- collection_type: open
  name: ENGAGE Cloud Credentialing Access Codes Mobile Credentials API
  slug: open-allegion-mobile-credentials-api
- collection_type: open
  name: ENGAGE Cloud Credentialing Access Codes Webhook Subscriptions API
  slug: open-allegion-webhook-subscriptions-api
- collection_type: open
  name: ENGAGE Cloud Credentialing API
  slug: open-engage-credentialing
- collection_type: open
  name: Schlage Home API
  slug: open-schlage-home
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/allegion/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/allegion-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/allegion-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/allegion-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allegion-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/allegion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/allegion-scopes.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.allegion.com
- group: start
  title: ''
  type: Portal
  url: https://developerapi.allegion.com
- group: start
  title: ''
  type: Login
  url: https://developerapi.allegion.com/signin/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.allegion.com/en/documentation.html
- group: other
  title: ''
  type: Overview
  url: https://developer.allegion.com/en/index.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.allegion.com/en/release-notes.html
- group: operate
  title: ''
  type: Support
  url: https://developersupport.allegion.com/hc/en-us
- group: auth
  title: ''
  type: Authentication
  url: https://developer.allegion.com/en/products/schlage-home/getting-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Allegion
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Allegion-Public
- group: build
  title: ''
  type: SDKs
  url: https://developer.allegion.com/en/products/schlage-mobile-credentials/mobile-sdk.html
- group: build
  title: ''
  type: SDKs
  url: https://developer.allegion.com/en/products/schlage-mobile-credentials/how-to-integrate-schlage-ble-mobile-credentials-with-an-access-control-system.html
- group: company
  title: ''
  type: Blog
  url: https://developer.allegion.com/en/products/schlage-home/schlage-home-api-blog.html
- group: other
  title: ''
  type: CorporateSite
  url: https://www.allegion.com
- group: company
  title: ''
  type: About
  url: https://www.allegion.com/corp/en/about.html
- group: other
  title: ''
  type: ConsumerBrand
  url: https://www.schlage.com
- group: other
  title: ''
  type: ConsumerBrand
  url: https://commercial.schlage.com
- group: other
  title: ''
  type: ConsumerBrand
  url: https://www.vonduprin.com
- group: other
  title: ''
  type: ConsumerBrand
  url: https://www.lcnclosers.com
- group: other
  title: ''
  type: ConsumerBrand
  url: https://www.yonomi.com
- group: company
  title: ''
  type: Partners
  url: https://www.allegion.com/corp/en/partners.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/allegion
- group: other
  title: ''
  type: X
  url: https://x.com/AllegionPlc
- group: company
  title: ''
  type: Investors
  url: https://investor.allegion.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.allegion.com/en/products/schlage-mobile-credentials/how-to-integrate-schlage-ble-mobile-credentials-with-an-access-control-system.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.allegion.com/corp/en/privacy-policy.html
- group: other
  title: ''
  type: Scale
  url: ''
- group: operate
  title: ''
  type: SupportedHardware
  url: ''
- group: design
  title: ''
  type: JSONLD
  url: json-ld/allegion-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/allegion-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/allegion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/allegion-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/allegion-finops.yml
created: '2026-05-23'
description: Allegion plc is a global security products company with $3.8B in 2024 revenue, 13,000+ employees, and 30+ brands across 120 countries (Schlage, Von Duprin, LCN, CISA, Steelcraft, Interflex, SimonsVoss, Yonomi). The Allegion Developer Portal exposes two documented integration surfaces - the Schlage Home API V2 (residential WiFi smart locks) and the ENGAGE Cloud Credentialing API (commercial BLE mobile credentials), plus iOS and Android Device Communication and BLE Mobile Access SDKs gated behind an Allegion Security Token Agreement.
examples:
- key_count: 2
  name: Engage List Credentials Example
  slug: engage-list-credentials-example
- key_count: 2
  name: Engage Upload Credential Example
  slug: engage-upload-credential-example
- key_count: 2
  name: Schlage Home Create Access Code Example
  slug: schlage-home-create-access-code-example
- key_count: 2
  name: Schlage Home List Devices Example
  slug: schlage-home-list-devices-example
- key_count: 2
  name: Schlage Home Webhook Subscription Example
  slug: schlage-home-webhook-subscription-example
features:
- Schlage Home API V2 OAuth 2.0 Authorization Code flow against https://account.schlage.com
- WebHooks subscription API for device state, access code, command, and account events (HTTPS only, 30s validation window)
- 202 ACCEPTED asynchronous command pattern for POST / PUT / DELETE device operations
- DST-offset-aware Access Code Webhooks (April 2026)
- Access Code Synchronization to reconcile lock-stored codes with cloud (July 2025)
- WiFi signal strength surfaced in GET Device endpoint (March 2025)
- ENGAGE Cloud Credentialing API for BLE Mobile Credential upload, delete, list using alle-subscription-key header + Basic Auth
- Allegion Device Communication SDK (iOS, Android) for ENGAGE device commissioning and door file distribution
- Allegion BLE Mobile Access SDK (iOS, Android) for credential download, BLE discovery, pre-connection unlock
- Supports Schlage Encode Deadbolt, Encode Plus, Encode Levers (WiFi residential)
- Supports Gen 2 ENGAGE hardware (Control BE467B / FE410B, NDEB, LEBMS / LEBMD, MTKB readers)
- Webhook signature verification via public key
- HTTPS-only callback URLs, 200-299 success range
- Onboarding requires Schlage Home Representative approval (residential) or Allegion Security Token Agreement (mobile credentials)
finops:
- name: Allegion Finops
  service_category: Identity, Security, and Access
  slug: allegion-finops
image: https://www.allegion.com/content/dam/allegion-corporate/logos/allegion-logo.svg
json_schemas:
- name: ENGAGE Mobile Credential
  property_count: 10
  slug: engage-credential
- name: Schlage Home Access Code
  property_count: 5
  slug: schlage-home-access-code
- name: Schlage Home Device
  property_count: 9
  slug: schlage-home-device
- name: Schlage Home Webhook Subscription
  property_count: 5
  slug: schlage-home-webhook-subscription
json_structures:
- name: Engage Credential Structure
  property_count: 0
  slug: engage-credential-structure
- name: Schlage Home Device Structure
  property_count: 0
  slug: schlage-home-device-structure
jsonld:
- class_count: 10
  name: Allegion Context
  property_count: 36
  slug: allegion-context
layout: provider
modified: '2026-05-23'
name: Allegion
nav: Providers
network: true
overview: 'Allegion publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Access Codes API, Commands API, Devices API, and 2 more. Tagged areas include Access Control, Smart Lock, Smart Home, Mobile Credentials, and Bluetooth.


  The Allegion catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Allegion''s developer surface includes authentication, developer portal, documentation, release notes, support, engineering blog, and 32 more developer resources.'
plans:
- name: Allegion Plans Pricing
  plan_count: 3
  slug: allegion-plans-pricing
random_paper: 98
rate_limits:
- limit_count: 7
  name: Allegion Rate Limits
  slug: allegion-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Allegion API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: allegion-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Allegion API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: engage-credentialing-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Allegion API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: schlage-home-rules
scopes:
- name: Allegion Scopes
  scope_count: 5
  slug: allegion-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 56.8
  delta: -9.1
  facets:
    access_clarity: 64.5
    commercial_clarity: 64.5
    contract_governance: 25.0
    contract_quality: 68.1
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 65.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/allegion/refs/heads/main/screenshots/allegion-2026-06-20T171528.png
security:
- kind: authentication
  name: Allegion Authentication
  slug: allegion-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Allegion Domain Security
  slug: allegion-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Allegion Vulnerability Disclosure
  slug: allegion-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Allegion Trust Center
  slug: allegion-trust-center
  summary_line: SOC 2
slug: allegion
tags:
- Access Control
- Smart Lock
- Smart Home
- Mobile Credentials
- Bluetooth
- BLE
- IoT
- Security
- Webhooks
- OAuth
- Schlage
- Von Duprin
- ENGAGE
website: https://developer.allegion.com
---
