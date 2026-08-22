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
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 69
  human_in_the_loop: 3
  name: Route Mobile Agentic Access
  operation_count: 108
  slug: route-mobile-agentic-access
  summary_line: 108 operations · 69 acting · 3 human-in-the-loop
api_count: 6
apis:
- description: Route Mobile's core A2P SMS platform — single, bulk, scheduled and personalised SMS submission over HTTPS, credit checks, account details, OTP generation and verification, DND/whitelist management, co
  name: Route Mobile SMS API
  slug: route-mobile-sms-api
- description: Route Mobile is a Meta Business Solution Provider for the WhatsApp Business Platform. The API covers JWT login, account management, template and session messaging, bulk campaign upload and management,
  name: Route Mobile WhatsApp Business API
  slug: route-mobile-whatsapp-business-api
- description: Rich Communication Services business messaging — verified sender messaging with rich cards, carousels and suggested replies, single and bulk message submission, an RCS payment/bill-send endpoint, typi
  name: Route Mobile RCS Business Messaging API
  slug: route-mobile-rcs-api
- description: 'Viber Business Messages — login, single and bulk message submission (text, image, video, file and template messages), campaign management, media upload, summary and graph reporting, report generation '
  name: Route Mobile Viber Business Messages API
  slug: route-mobile-viber-api
- description: SendClean is Route Mobile's transactional and bulk email product, exposed as a JSON-over-HTTP-POST REST API. 24 documented operations covering SMTP user creation and password reset, sending-domain and
  name: SendClean Email API
  slug: sendclean-email-api
- description: 'Route Mobile''s enterprise voice and cloud telephony surface, documented as narrative guides on the developer portal (send message and template management calls) and published as a first-party Postman '
  name: Route Mobile Enterprise Voice 2.0 API
  slug: route-mobile-enterprise-voice-api
artifact_total: 17
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: route-mobile-mcp.yml
  slug: route-mobile-mcpyml
modified: '2026-07-25'
name: Route Mobile
nav: Providers
network: true
overview: 'Route Mobile publishes 6 APIs on the [APIs.io](https://apis.io/) network, including SMS API, WhatsApp Business API, RCS Business Messaging API, and 3 more. Tagged areas include Telecommunications, India, CPaaS, Messaging, and SMS.


  The Route Mobile catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Route Mobile''s developer surface includes authentication, sandbox, getting-started guide, support, documentation, engineering blog, signup flow, and 29 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 6
  name: Route Mobile Rate Limits
  slug: route-mobile-rate-limits
score:
  band: strong
  composite: 57.7
  delta: 4.9
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 30.3
    contract_quality: 69.2
    developer_ergonomics: 53.0
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 42.1
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 56.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
