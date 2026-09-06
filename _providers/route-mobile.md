---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 69
  human_in_the_loop: 3
  name: Route Mobile Agentic Access
  operation_count: 108
  slug: route-mobile-agentic-access
  summary_line: 108 operations · 69 acting · 3 human-in-the-loop
api_count: 5
apis:
- description: 'Route Mobile''s enterprise voice and cloud telephony surface, documented as narrative guides on the developer portal (send message and template management calls) and published as a first-party Postman '
  name: Route Mobile Enterprise Voice 2.0 API
  slug: route-mobile-enterprise-voice-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: APIs for account management, credit queries, and authentication tokens.
  name: Route Mobile Account API
  slug: route-mobile-account-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Manage your WhatsApp Business profile settings, account details, and profile photo.
  name: Route Mobile Account Management API
  slug: route-mobile-account-management-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Retrieve account/user details
  name: Route Mobile Accounts API
  slug: route-mobile-accounts-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Authenticate with the Route Mobile WhatsApp Business API to obtain a JWT token for subsequent API calls.
  name: Route Mobile Authentication API
  slug: route-mobile-authentication-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Upload files, create, start, pause, and resume bulk messaging campaigns to reach large audiences.
  name: Route Mobile Bulk Campaigns API
  slug: route-mobile-bulk-campaigns-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Upload campaign files and manage bulk RCS messaging campaigns at scale.
  name: Route Mobile Bulk Upload Campaign API
  slug: route-mobile-bulk-upload-campaign-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Webhook receiver endpoints for real-time RCS message delivery and event notifications.
  name: Route Mobile Callback API
  slug: route-mobile-callback-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Check and retrieve RCS capability details for phone numbers in bulk.
  name: Route Mobile Capability Check API
  slug: route-mobile-capability-check-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Create, update, delete, and fetch product feeds and catalog details for WhatsApp Commerce.
  name: Route Mobile Catalog Management API
  slug: route-mobile-catalog-management-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Upload media files (images, videos, PDFs) to the RCS file server for use in messages.
  name: Route Mobile File Server API
  slug: route-mobile-file-server-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: APIs for third-party platform integrations.
  name: Route Mobile Integrations API
  slug: route-mobile-integrations-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Authenticate users and obtain JWT tokens for RCS API access.
  name: Route Mobile Login API
  slug: route-mobile-login-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: APIs for managing RCS bot testers, templates, and account configuration.
  name: Route Mobile Management API
  slug: route-mobile-management-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: APIs for submitting SMS messages.
  name: Route Mobile Message Sending API
  slug: route-mobile-message-sending-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Send transactional emails and retrieve message info
  name: Route Mobile Messages API
  slug: route-mobile-messages-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Send template messages (marketing, utility, authentication) and session messages (text, media, interactive, payments, flows) to individual recipients.
  name: Route Mobile Messaging API
  slug: route-mobile-messaging-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Store and verify user opt-in and opt-out consent for WhatsApp messaging compliance.
  name: Route Mobile Opt-in Management API
  slug: route-mobile-opt-in-management-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: APIs for OTP generation and verification.
  name: Route Mobile OTP API
  slug: route-mobile-otp-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Send RCS payment request messages to customers.
  name: Route Mobile Payment API
  slug: route-mobile-payment-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Send RCS notification, session, and India template messages including text, media, rich cards, carousels, and interactive suggestions.
  name: Route Mobile RCS Messages API
  slug: route-mobile-rcs-messages-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: APIs for managing RCS message requests and retrieving request status.
  name: Route Mobile RCS Messages Request API
  slug: route-mobile-rcs-messages-request-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: The RCS Optin API API from Route Mobile — 1 operation(s) for rcs optin api.
  name: Route Mobile RCS Optin API
  slug: route-mobile-rcs-optin-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: The RCS Template API API from Route Mobile — 3 operation(s) for rcs template api.
  name: Route Mobile RCS Template API
  slug: route-mobile-rcs-template-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Generate, download, and query messaging reports including delivery stats, campaign metrics, opt-in data, and template usage counts.
  name: Route Mobile Reports API
  slug: route-mobile-reports-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Add, verify, list, and delete sending domains
  name: Route Mobile Sending Domains API
  slug: route-mobile-sending-domains-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Manage SMTP sub-users (create, edit, reset password, list)
  name: Route Mobile SMTP Users API
  slug: route-mobile-smtp-users-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Add, check, list, and delete tracking domains
  name: Route Mobile Tracking Domains API
  slug: route-mobile-tracking-domains-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Send bulk campaign messages to multiple Viber recipients at once using a file_code from the Campaign File Upload API. Supports all message types including fallback delivery to SMS or WhatsApp, and sch
  name: Route Mobile Viber Bulk Messaging API
  slug: route-mobile-viber-bulk-messaging-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Send single messages to individual Viber users including text, images, videos, files, OTP verification, and interactive buttons. Also manage campaign file uploads and legacy campaign send operations.
  name: Route Mobile Viber Business Messaging API
  slug: route-mobile-viber-business-messaging-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Receive real-time webhook notifications for incoming messages and delivery reports from the Viber platform. Configure your callback URL in the webhook settings.
  name: Route Mobile Viber Client Callback API
  slug: route-mobile-viber-client-callback-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Authenticate and obtain a JWT token to access the Viber Business Messaging APIs. Tokens are valid for one hour by default.
  name: Route Mobile Viber Login API
  slug: route-mobile-viber-login-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Access delivery reports, campaign performance metrics, summary dashboards, and message-level tabular data. Create and download detailed CSV reports. Manage approved Viber message templates.
  name: Route Mobile Viber Reports API
  slug: route-mobile-viber-reports-api-api
- baseURL: https://api.rmlconnect.net
  baseurl_source: declared
  description: Configure event webhooks for email delivery events
  name: Route Mobile Webhooks API
  slug: route-mobile-webhooks-api
artifact_total: 44
asyncapis:
- description: ''
  name: Route Mobile Webhooks
  slug: route-mobile-webhooks
collections:
- collection_type: open
  name: Route Mobile Rich Communication Services (RCS) API Documentation
  slug: open-route-mobile-rcs
- collection_type: open
  name: SendClean Email API
  slug: open-route-mobile-sendclean-email
- collection_type: open
  name: Route Mobile SMS APIs
  slug: open-route-mobile-sms
- collection_type: open
  name: Route Mobile Viber OpenAPI Specification
  slug: open-route-mobile-viber
- collection_type: open
  name: Route Mobile WhatsApp Business API
  slug: open-route-mobile-whatsapp-business
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/route-mobile-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/routemobile/WhatsApp-Business-API/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/route-mobile-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/route-mobile-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/route-mobile-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/route-mobile-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/route-mobile-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/route-mobile-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/route-mobile-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/route-mobile-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/route-mobile-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://routemobile.com/company-profile/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/route-mobile-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/route-mobile-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/route-mobile-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/route-mobile-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/route-mobile-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/route-mobile-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/route-mobile-sms-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/route-mobile-whatsapp-business-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/route-mobile-rcs-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/route-mobile-viber-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/route-mobile-sendclean-email-overlay.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.rmlconnect.net/route-mobile-project/docs/getting-started-on-route-mobile-panel
- group: operate
  title: ''
  type: Support
  url: https://routemobile.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://routemobile.com/terms-condition/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://routemobile.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://routemobile.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.rmlconnect.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.rmlconnect.net/
- group: other
  title: ''
  type: APIDocuments
  url: https://routemobile.com/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/routemobile
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/routemobile/route-mobile-s-public-workspace
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developer.rmlconnect.net/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://routemobile.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/routemobilelimited/
- group: start
  title: ''
  type: SignUp
  url: https://routemobile.com/contact-us/
created: '2026-07-25'
description: 'Route Mobile Limited is a Mumbai-headquartered cloud communications platform (CPaaS) provider and one of India''s largest A2P messaging aggregators, listed on the BSE and NSE and now majority-owned by Belgium''s Proximus Group, where it sits alongside BICS and Telesign inside Proximus Global. It sells enterprise messaging (SMS, WhatsApp Business Platform, RCS, Viber, Google Business Messages, Telegram, Instagram), OTP and identity verification, voice and cloud telephony, transactional email through SendClean, URL shortening through Acculync, and a telecom-operator product line (SMSC-as-a-service, the Route Shield SMS firewall, Route Hub, and Instant Virtual Numbers) that puts it on both sides of the carrier relationship — reselling operator connectivity to enterprises while also selling infrastructure back to operators. Its API posture is genuinely self-serve and public: a ReadMe-hosted developer portal at developer.rmlconnect.net documents roughly 108 REST operations across
  SMS, WhatsApp, RCS, Viber and email, backed by five downloadable OpenAPI 3.0 definitions that are also mirrored in first-party GitHub repositories with Postman collections and Redoc pages. That places Route Mobile firmly in the CPaaS-aggregator half of telecom rather than the partner-gated operator half. On the sector''s defining standards question it is thinner than its marketing suggests: nothing in its public documentation references CAMARA, GSMA Open Gateway, Number Verification, SIM Swap, Device Location or CIBA, and its network-API story lives entirely at the parent level, in Proximus Global''s Konera aggregation platform announced as "aligned with GSMA''s CAMARA standardization initiative" — a press release, not a callable Route Mobile endpoint. Authentication across its live APIs is legacy-CPaaS rather than telco-standard: username and password query parameters for SMS, JWT bearer tokens minted by product-level login endpoints for WhatsApp, RCS and Viber, and owner_id plus token
  in the request body for email.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Route Mobile
nav: Providers
network: true
overview: 'Route Mobile publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Enterprise Voice 2.0 API, Account API, Account Management API, and 31 more. Tagged areas include Telecommunications, India, CPaaS, Messaging, and SMS.


  The Route Mobile catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Route Mobile''s developer surface includes authentication, sandbox, getting-started guide, support, documentation, engineering blog, signup flow, and 31 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 6
  name: Route Mobile Rate Limits
  slug: route-mobile-rate-limits
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 65.5
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
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
    score: 56.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/route-mobile/refs/heads/main/screenshots/route-mobile-2026-08-17T081637.png
security:
- kind: authentication
  name: Route Mobile Authentication
  slug: route-mobile-authentication
  summary_line: apiKey/http/query-credentials/body-credentials · 5 schemes
- kind: domain-security
  name: Route Mobile Domain Security
  slug: route-mobile-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: route-mobile
tags:
- Telecommunications
- India
- CPaaS
- Messaging
- SMS
- A2P Messaging
- WhatsApp Business
- RCS
- Voice
- Email
- Identity Verification
- OTP
- Aggregator
website: https://routemobile.com/
---
