---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1172
  human_in_the_loop: 30
  name: Infobip Agentic Access
  operation_count: 1886
  slug: infobip-agentic-access
  summary_line: 1886 operations · 1172 acting · 30 human-in-the-loop
api_count: 47
apis:
- baseURL: https://api.infobip.com
  baseurl_source: declared
  description: AI-powered tools and services to help you create smarter and more personalized customer experiences.
  name: Infobip AI Hub API
  slug: infobip-ai-hub-api
- baseURL: https://api.infobip.com
  baseurl_source: declared
  description: Create a perfect customer experience by using the channels your customer already use and love.
  name: Infobip Channels API
  slug: infobip-channels-api
- baseURL: https://api.infobip.com
  baseurl_source: declared
  description: Powerful infrastructure and tools that connect you to the world.
  name: Infobip Connectivity API
  slug: infobip-connectivity-api
- baseURL: https://api.infobip.com
  baseurl_source: declared
  description: Complete solutions that will help you drive better outcomes for your customers and business across the entire customer journey.
  name: Infobip Customer Engagement API
  slug: infobip-customer-engagement-api
- baseURL: https://api.infobip.com
  baseurl_source: declared
  description: Modular tools to scale and automate your business.
  name: Infobip Platform API
  slug: infobip-platform-api
- baseURL: https://api.infobip.com
  baseurl_source: declared
  description: Developer utilities to help you integrate and work with Infobip APIs more efficiently.
  name: Infobip Tools API
  slug: infobip-tools-api
artifact_total: 109
asyncapis:
- description: AsyncAPI projection of the 102 webhooks published in the Infobip platform OpenAPI 3.1 document (the "webhooks" object). Each channel is an Infobip-originated HTTP callback delivered to a customer-conf
  name: Infobip platform webhooks
  slug: infobip-webhooks-asyncapi
- description: ''
  name: Infobip Webhooks
  slug: infobip-webhooks
collections:
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-2fa-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-account-management-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-ai-assistants-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-answers-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-apple-mfb-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-application-entity-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-billing-usage-api-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-biometrics-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-blocklist-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-camara-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-catalogs-api-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-common-assets-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-conversations-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-email-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-instagram-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-kakao-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-knowledge-base-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-line-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-live-chat-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-messages-api-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-messenger-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-metrics-api-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-mms-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-mobile-app-messaging-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-mobile-identity-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-moments-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-number-activation-state-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-number-lookup-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-numbers-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-omni-failover-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-open-channel-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-openapi-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-people-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-rcs-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-resources-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-sending-strategy-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-signals-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-sms-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-subscriptions-api-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-tiktok-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-viber-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-vocalize-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-voice-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-webrtc-calls-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-whatsapp-openapi
- collection_type: postman
  name: Infobip OpenAPI Specification
  slug: postman-infobip-zalo-openapi
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-2fa
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-account-management
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-ai-assistants
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-answers
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-apple-mfb
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-application-entity
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-billing-usage-api
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-biometrics
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-blocklist
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-camara
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-catalogs-api
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-common-assets
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-conversations
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-email
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-instagram
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-kakao
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-knowledge-base
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-line
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-live-chat
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-messages-api
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-messenger
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-metrics-api
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-mms
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-mobile-app-messaging
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-mobile-identity
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-moments
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-number-activation-state
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-number-lookup
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-numbers
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-omni-failover
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-open-channel
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-openapi
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-people
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-platform-full
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-rcs
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-resources
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-sending-strategy
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-signals
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-sms
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-subscriptions-api
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-tiktok
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-viber
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-vocalize
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-voice
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-webrtc-calls
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-whatsapp
- collection_type: open
  name: Infobip OpenAPI Specification
  slug: open-infobip-zalo
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/infobip-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-2fa-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-account-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-ai-assistants-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-answers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-apple-mfb-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-application-entity-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-billing-usage-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-biometrics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-blocklist-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-camara-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-catalogs-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-common-assets-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-conversations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-email-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-instagram-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-kakao-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-knowledge-base-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-line-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-live-chat-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-messages-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-messenger-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-metrics-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-mms-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-mobile-app-messaging-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-mobile-identity-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-moments-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-number-activation-state-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-number-lookup-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-numbers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-omni-failover-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-open-channel-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-openapi-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-people-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-rcs-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-resources-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-sending-strategy-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-signals-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-sms-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-subscriptions-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-tiktok-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-viber-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-vocalize-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-voice-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-webrtc-calls-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-whatsapp-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-zalo-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/infobip/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/infobip-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/infobip-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infobip-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/infobip-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infobip-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.infobip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.infobip.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.infobip.com/docs/api
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/infobip-platform-full-openapi.json
- group: docs
  title: ''
  type: OpenAPIEndpoint
  url: https://api.infobip.com/platform/1/openapi
- group: auth
  title: ''
  type: Authentication
  url: https://www.infobip.com/docs/essentials/api-essentials/api-authorization
- group: build
  title: ''
  type: SDK
  url: https://www.infobip.com/docs/sdk
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/infobip/infobip-api
- group: docs
  title: ''
  type: Documentation
  url: https://www.infobip.com/docs/mcp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infobip
- group: start
  title: ''
  type: SignUp
  url: https://www.infobip.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.infobip.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.infobip.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.infobip.com/docs/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.infobip.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.infobip.com/blog/feed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/infobip
- group: operate
  title: ''
  type: Support
  url: https://www.infobip.com/contact
- group: build
  title: ''
  type: Packages
  url: packages/infobip-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/infobip-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/infobip-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/infobip-security.txt
- group: other
  title: ''
  type: APICatalog
  url: well-known/infobip-api-catalog.json
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/infobip-openid-configuration.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/infobip-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/infobip-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infobip-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/infobip-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/infobip-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/infobip-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infobip-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/infobip-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/infobip-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/infobip-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.infobip.com/certificates
- group: auth
  title: ''
  type: TrustCenter
  url: security/infobip-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.infobip.com/security-trust-center/cvd-policy
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/infobip-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/infobip-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/infobip-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/infobip-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/infobip-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/infobip-changelog.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/infobip-platform-full-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/infobip-send-sms-and-confirm-delivery.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/infobip-send-whatsapp-template-message.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/infobip-two-factor-authentication.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/infobip-verify-identity-with-network-apis.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/infobip-send-email-and-manage-deliverability.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/infobip-manage-people-profiles.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/infobip-provision-numbers-and-webhooks.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/infobip-omnichannel-send-with-failover.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.infobip.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.infobip.com/docs/essentials/getting-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.infobip.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.infobip.com/policies/privacy-notice
- group: start
  title: ''
  type: Console
  url: https://portal.infobip.com
created: '2026-07-25'
description: 'Infobip is a global communications platform as a service (CPaaS) provider headquartered in Vodnjan, Croatia, and is Croatia''s largest technology company. It sells programmable messaging, voice, video, email and customer engagement APIs on top of direct connections into mobile network operators worldwide, sitting in the aggregator layer of the telecom value chain: it buys and resells carrier connectivity, and it is the developer-facing surface that most businesses actually integrate with rather than the carriers themselves. Its API posture is openly self-serve — a free-trial account, a documentation hub at infobip.com/docs/api, first-party SDKs in six languages, a public Postman workspace, remote MCP servers, and an unauthenticated OpenAPI 3.1 endpoint at https://api.infobip.com/platform/1/openapi that returns the complete specification for all public endpoints and webhooks, plus per-product specifications for 46 products. On the network-API side Infobip is a GSMA Open Gateway
  participant certified for SIM Swap and Number Verification (September 2025) and an Aduna channel partner, and it publishes callable CAMARA endpoints — Number Verification, SIM Swap, Device Location Verification and KYC Match — though CAMARA access itself is sales-gated behind a contact form even while the specification is public.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Infobip MCP Server
  slug: infobip-mcp-server
modified: '2026-07-25'
name: Infobip
nav: Providers
network: true
overview: 'Infobip publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AI Hub API, Channels API, Connectivity API, and 3 more. Tagged areas include Telecommunications, Croatia, CPaaS, Messaging, and SMS.


  The Infobip catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Infobip''s developer surface includes authentication, documentation, API reference, SDKs, signup flow, pricing, changelog, and 104 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 44
  name: Infobip Rate Limits
  slug: infobip-rate-limits
scopes:
- name: Infobip Scopes
  scope_count: 159
  slug: infobip-scopes
  summary_line: 159 scopes · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 69.6
  coverage:
    artifact_dirs: 26
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 64.1
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 69.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
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
    score: 93.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/screenshots/infobip-2026-08-07T170702.png
security:
- kind: authentication
  name: Infobip Authentication
  slug: infobip-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Infobip Domain Security
  slug: infobip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Infobip Vulnerability Disclosure
  slug: infobip-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Infobip Trust Center
  slug: infobip-trust-center
  summary_line: ISO 9001, ISO 22301, ISO 27001, ISO 27017, ISO 27018, SOC 2 Type 2, PCI DSS, CSA STAR Level 1, ENS Category Basic, GSMA Open Connectivity Certified, GSMA Mobile Connect Certified, Mobile Ecosystem Forum Certified, Philippines National Privacy Commission Seal of Registration
slug: infobip
tags:
- Telecommunications
- Croatia
- CPaaS
- Messaging
- SMS
- Voice
- RCS
- WhatsApp
- Email
- Network APIs
- CAMARA
- Open Gateway
- Identity Verification
- SIM Swap
- Number Verification
- Omnichannel
- Aggregator
- Customer Engagement
website: https://www.infobip.com/
---
