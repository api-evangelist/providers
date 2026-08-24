---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
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
  score: 48.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 117
  human_in_the_loop: 0
  name: Syniverse Agentic Access
  operation_count: 187
  slug: syniverse-agentic-access
  summary_line: 187 operations · 117 acting
api_count: 12
apis:
- description: 'The Syniverse Communication Gateway (SCG) API — the core of the Syniverse Developer Community platform. 72 documented paths and 148 operations covering message requests, messages, scheduled messages, '
  name: Syniverse Omni-Channel Messaging API (SCG)
  slug: syniverse-omni-channel-messaging-api
- description: Generates and validates one-time passwords and delivers customized tokens over SMS, voice or push to verify an end user. Documented as part of the SCG API surface with application, user, associate, va
  name: Syniverse Multi-Factor Authentication API
  slug: syniverse-multi-factor-authentication-api
- description: Single-number lookup service that returns the current carrier, line type and status of a phone number so an enterprise can detect ported, deactivated, disconnected or reassigned numbers. Batch file lo
  name: Syniverse Phone Number Verification API
  slug: syniverse-phone-number-verification-api
- description: A single POST /v2/match operation that returns match scores comparing an end user's asserted identity against Syniverse-sourced mobile data. This is Syniverse's own identity-matching API, not the CAMA
  name: Syniverse Right Party Verification API
  slug: syniverse-right-party-verification-api
- description: 'A single POST /v1/simCheck operation that reports whether an end user''s mobile channel has had recent SIM changes or call forwarding enabled, as an account-takeover risk signal. Functionally adjacent '
  name: Syniverse Account Takeover Detection API
  slug: syniverse-account-takeover-detection-api
- description: Resolves inbound text and MMS traffic to a disposition — the spam and messaging-abuse classification service sold to messaging operators and enterprises. Two operations, /v1/txt/resolve and /v1/mms/re
  name: Syniverse Messaging Trust Resolve API
  slug: syniverse-messaging-trust-resolve-api
- description: Submits spam reports into the Messaging Trust datafeed via a single POST /spam/report operation, secured with OAuth2 client credentials against the Messaging Trust token endpoint.
  name: Syniverse Messaging Trust Spam Datafeed API
  slug: syniverse-messaging-trust-spam-datafeed-api
- description: US 10DLC (10-digit long code) campaign provisioning — create, retrieve, suspend and resume campaigns, attach and detach long codes and number pools, and manage AT&T DCA campaigns and application addre
  name: Syniverse 10DLC API
  slug: syniverse-10dlc-api
- description: 'The deprecated version 1 of the 10DLC provisioning API, still published in the SDC documentation under an explicitly deprecated section. Adds and removes 10DLC long codes and number pool associations '
  name: Syniverse 10DLC Number Pool API (v1, deprecated)
  slug: syniverse-10dlc-number-pool-api
- description: 'Developer Community gateway service for managing whitelists of entities and transactions, used to allow trial-account destination numbers and similar platform-level allow lists. Six operations across '
  name: Syniverse Whitelisting Service API
  slug: syniverse-whitelisting-service-api
- description: Regenerates the access token associated with an SDC application via GET /saop-rest-data/v1/apptoken-refresh. This is the token-lifecycle piece of the Syniverse Developer Community bearer-token auth mo
  name: Syniverse SDC Application Access Token Management API
  slug: syniverse-access-token-management-api
- description: 'The webhook and event layer of the Syniverse Developer Community. The Event Subscription Service (ESS) API manages topics, topic-subscriptions, delivery-configurations, event-types, event-deliveries, '
  name: Syniverse Event Subscription Service API (Event Manager)
  slug: syniverse-event-subscription-service-api
artifact_total: 29
asyncapis:
- description: ''
  name: Syniverse Event Manager Webhooks
  slug: syniverse-event-manager-webhooks
collections:
- collection_type: open
  name: Syniverse 10DLC Provissioning API
  slug: open-syniverse-10dlc-number-pool
- collection_type: open
  name: 10DLC
  slug: open-syniverse-10dlc
- collection_type: open
  name: Syniverse Account Takeover Detection API
  slug: open-syniverse-account-takeover-detection
- collection_type: open
  name: MT Spam Datafeed
  slug: open-syniverse-messaging-trust-datafeed
- collection_type: open
  name: SCG API
  slug: open-syniverse-multi-factor-authentication
- collection_type: open
  name: SCG API
  slug: open-syniverse-omni-channel-messaging
- collection_type: open
  name: PNV
  slug: open-syniverse-phone-number-verification
- collection_type: open
  name: Syniverse Right Party Verification API
  slug: open-syniverse-right-party-verification
- collection_type: open
  name: SDC Application Access Token Management
  slug: open-syniverse-token-management
- collection_type: open
  name: Whitelisting_Service
  slug: open-syniverse-whitelisting-service
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/syniverse-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/syniverse-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syniverse-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/syniverse-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/syniverse-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/syniverse-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/syniverse-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/syniverse-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/syniverse-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/syniverse-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/syniverse-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/syniverse-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/syniverse-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/syniverse-event-manager-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/syniverse-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/syniverse-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/syniverse-llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://sdcdocumentation.syniverse.com/index.php/omni-channel/getting-started/sms-mms-quickstart
- group: company
  title: ''
  type: Website
  url: https://www.syniverse.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.syniverse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sdcdocumentation.syniverse.com/
- group: start
  title: ''
  type: SignUp
  url: https://developer.syniverse.com/home.html#apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Syniverse
- group: operate
  title: ''
  type: Support
  url: https://sdcsupport.syniverse.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.syniverse.com/blog
- group: company
  title: ''
  type: News
  url: https://www.syniverse.com/news-and-events
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/syniverse
- group: operate
  title: ''
  type: Contact
  url: https://www.syniverse.com/contact/general-inquiries
- group: commercial
  title: ''
  type: Legal
  url: https://www.syniverse.com/legal/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.syniverse.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.syniverse.com/privacy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.syniverse.com/privacy/
created: '2026-07-25'
description: 'Syniverse is a United States headquartered wholesale telecommunications company that sits between mobile network operators rather than in front of consumers. Its mobility business runs inter-carrier roaming, IPX network and signaling, 5G SEPP, clearing and settlement, global SIM and satellite roaming for carriers, and none of that carrier-side estate is exposed as a public API. Its messaging business is the opposite: an A2P/CPaaS aggregator selling SMS, MMS, RCS, WhatsApp, push, voice, 10DLC campaign registration, messaging trust/anti-spam and mobile identity services to enterprises, and it is published through a genuine self-serve developer portal, the Syniverse Developer Community (SDC), where anyone can sign up for a free API key, read the docs, and download eleven Redoc-rendered OpenAPI/Swagger definitions. On network APIs Syniverse is a channel, not a source — it joined GSMA Open Gateway in April 2025 as a channel partner and announced an integration with Aduna in June
  2025, but no CAMARA-defined API is documented or callable on its developer portal today.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Syniverse MCP Server
  slug: syniverse-mcp-server
modified: '2026-07-25'
name: Syniverse
nav: Providers
network: true
overview: 'Syniverse publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Omni-Channel Messaging API (SCG), Multi-Factor Authentication API, Phone Number Verification API, and 8 more. Tagged areas include Telecommunications, United States, CPaaS, Messaging, and SMS.


  The Syniverse catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Syniverse''s developer surface includes authentication, sandbox, getting-started guide, documentation, signup flow, support, engineering blog, and 26 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 4
  name: Syniverse Rate Limits
  slug: syniverse-rate-limits
scopes:
- name: Syniverse Scopes
  scope_count: 0
  slug: syniverse-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.4
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 56.4
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 81.8
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 66.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/syniverse/refs/heads/main/screenshots/syniverse-2026-08-17T082233.png
security:
- kind: authentication
  name: Syniverse Authentication
  slug: syniverse-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Syniverse Domain Security
  slug: syniverse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: syniverse
tags:
- Telecommunications
- United States
- CPaaS
- Messaging
- SMS
- Roaming
- IPX
- Wholesale
- Identity Verification
- SIM Swap
- 10DLC
- Open Gateway
- Network APIs
- Aggregator
website: https://www.syniverse.com/
---
