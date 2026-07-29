---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 46
  human_in_the_loop: 1
  name: Kore Wireless Agentic Access
  operation_count: 117
  slug: kore-wireless-agentic-access
  summary_line: 117 operations · 46 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The KORE ConnectivityPro API is the largest of KORE's published surfaces — 49 paths and 55 operations covering SIM and eSIM provisioning, eSIM profile management, activation profiles, subscriptions, a
  name: KORE Connectivity Pro API
  slug: kore-connectivity-pro-api
- description: Super SIM is the multi-IMSI global cellular connectivity platform KORE acquired from Twilio IoT. The API exposes 20 paths and 31 operations across Sim, Fleet, NetworkAccessProfile, Network, eSimProfil
  name: KORE Super SIM API
  slug: kore-super-sim-api
- description: Programmable Wireless is the legacy Twilio IoT cellular product now operated by KORE. The API publishes 9 paths and 16 operations covering the Wireless Sim resource, RatePlan, Command, DataSession, an
  name: KORE Programmable Wireless API
  slug: kore-programmable-wireless-api
- description: The KORE SMS API programmatically exchanges short messages with IoT devices on KORE connectivity. Three operations — send a message, list messages, and retrieve SMS message history — form the messagin
  name: KORE SMS API
  slug: kore-sms-api
- description: The public KORE Webhook API creates, retrieves, and modifies the signing secrets used to verify callbacks KORE sends to customer endpoints. KORE webhooks are signature-verified and idempotent, and the
  name: KORE Webhook API
  slug: kore-webhook-api
- description: The KORE IAM API manages customer accounts and their relationships — creating accounts, retrieving account hierarchies, and managing platform-specific mappings between parent and child accounts across
  name: KORE Identity and Access Management API
  slug: kore-iam-api
- description: The Client Management API creates, retrieves, and lists the API Clients that hold the credentials and settings for an integration with KORE. An API Client is the required gateway to every other KORE A
  name: KORE API Clients API
  slug: kore-api-clients-api
- description: The KORE Token API is the OAuth 2.0 authorization endpoint for the whole platform. A single POST to /v1/auth/token exchanges Client Credentials for a bearer access token per RFC 6749 section 4.4, with
  name: KORE Token API
  slug: kore-token-api
artifact_total: 15
asyncapis:
- description: ''
  name: Kore Wireless Event Streams Webhooks
  slug: kore-wireless-event-streams-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kore-wireless-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kore-wireless-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kore-wireless-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kore-wireless-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kore-wireless-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.korewireless.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.korewireless.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.korewireless.com/api/api-reference
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.korewireless.com/
- group: start
  title: ''
  type: Console
  url: https://console.korewireless.com/
- group: start
  title: ''
  type: SignUp
  url: https://console.korewireless.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/korewireless
- group: docs
  title: ''
  type: OpenAPIRepository
  url: https://github.com/korewireless/kore-openapi
- group: auth
  title: ''
  type: Authentication
  url: https://docs.korewireless.com/developers/api-management/auth
- group: design
  title: ''
  type: Webhooks
  url: https://docs.korewireless.com/developers/webhooks
- group: other
  title: ''
  type: EventStreams
  url: https://docs.korewireless.com/developers/event-streams
- group: operate
  title: ''
  type: StatusPage
  url: https://korewireless.service-now.com/csm?id=services_status
- group: company
  title: ''
  type: Blog
  url: https://www.korewireless.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.korewireless.com/news/
- group: docs
  title: ''
  type: TechnicalDocumentation
  url: https://www.korewireless.com/technical-documentation/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kore-wireless
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.korewireless.com/developers/get-started/apis
- group: operate
  title: ''
  type: Support
  url: https://docs.korewireless.com/troubleshooting/
- group: operate
  title: ''
  type: Contact
  url: https://www.korewireless.com/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.korewireless.com/programmable-wireless/help-and-support/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.korewireless.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.korewireless.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.korewireless.com/responsible-disclosure-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kore-wireless-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/kore-wireless-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kore-wireless-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kore-wireless-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kore-wireless-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kore-wireless-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kore-wireless-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kore-wireless-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kore-wireless-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kore-wireless-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kore-wireless-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kore-wireless-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kore-wireless-event-streams-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kore-wireless-data-model.yml
created: '2026-07-25'
description: 'KORE Wireless (KORE Group Holdings) is an Atlanta, Georgia headquartered global IoT connectivity provider operating as a mobile virtual network operator (MVNO) across more than 190 countries, with over 20 million IoT connections under management. KORE sits in the aggregator half of the telecom value chain: it does not own spectrum or radio access network, it resells and orchestrates multi-carrier cellular connectivity, eSIM/iSIM provisioning, device management, and IoT security as a service to enterprises in healthcare, fleet, logistics, utilities, and industrial automation. In 2024 KORE acquired the Twilio IoT business — Super SIM, Programmable Wireless, and Microvisor — inheriting a genuinely developer-first API surface, and it has kept that posture: KORE publishes eight OpenAPI 3.0 specifications in a public GitHub repository (github.com/korewireless/kore-openapi) with a make-based SDK generation workflow, an open GitBook documentation site at docs.korewireless.com requiring
  no login, self-serve account registration at console.korewireless.com, OAuth 2.0 client-credentials authorization, signed webhooks, and CloudEvents-formatted event streams. KORE publishes no CAMARA network APIs and is not a GSMA Open Gateway operator participant — as an MVNO it consumes carrier network capability rather than exposing it, and no CAMARA, Open Gateway, TM Forum, or NEF/SCEF reference appears anywhere in its documentation. In 2026 KORE was taken private by Searchlight Capital Partners and Abry Partners and delisted from the NYSE.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface derived from KORE OpenAPI
  slug: candidate-mcp-tool-surface-derived-from-kore-openapi
modified: '2026-07-25'
name: KORE Wireless
nav: Providers
network: true
overview: 'KORE Wireless publishes 8 APIs on the [APIs.io](https://apis.io/) network, including KORE Connectivity Pro API, KORE Super SIM API, KORE Programmable Wireless API, and 5 more. Tagged areas include Telecommunications, United States, IoT, eSIM, and Connectivity.


  The KORE Wireless catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  KORE Wireless'' developer surface includes authentication, documentation, API reference, developer console, signup flow, engineering blog, product news, and 36 more developer resources.'
random_paper: 13
scopes:
- name: Kore Wireless Scopes
  scope_count: 0
  slug: kore-wireless-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.6
  delta: 1.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.7
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 87.5
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 75.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Kore Wireless Authentication
  slug: kore-wireless-authentication
  summary_line: oauth2/apiKey/http · 3 schemes
- kind: domain-security
  name: Kore Wireless Domain Security
  slug: kore-wireless-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kore Wireless Vulnerability Disclosure
  slug: kore-wireless-vulnerability-disclosure
  summary_line: disclosure policy published
slug: kore-wireless
tags:
- Telecommunications
- United States
- IoT
- eSIM
- Connectivity
- MVNO
- SIM Management
- Roaming
- Messaging
- SMS
- Device Management
- Network APIs
website: https://www.korewireless.com/
---
