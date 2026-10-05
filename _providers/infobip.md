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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.0
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 1172
  human_in_the_loop: 30
  name: Infobip Agentic Access
  operation_count: 1886
  slug: infobip-agentic-access
  summary_line: 1886 operations · 1172 acting · 30 human-in-the-loop
api_count: 48
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
artifact_total: 142
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
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/rules/infobip-rules.yml
  title: ''
  type: Spectral
  url: rules/infobip-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/json-ld/infobip-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/infobip-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/vocabulary/infobip-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/infobip-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/asyncapi/infobip-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/infobip-webhooks-asyncapi.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/llms/infobip-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/infobip-docs-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/vendors/infobip-vendors.yml
  title: ''
  type: Vendors
  url: vendors/infobip-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.infobip.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.infobip.com/leadership
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/plans/infobip-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/infobip-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/capabilities/infobip-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/infobip-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-2fa-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-2fa-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-account-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-account-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-ai-assistants-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-ai-assistants-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-answers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-answers-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-apple-mfb-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-apple-mfb-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-application-entity-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-application-entity-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-billing-usage-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-billing-usage-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-biometrics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-biometrics-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-blocklist-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-blocklist-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-camara-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-camara-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-catalogs-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-catalogs-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-common-assets-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-common-assets-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-conversations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-conversations-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-email-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-email-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-instagram-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-instagram-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-kakao-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-kakao-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-knowledge-base-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-knowledge-base-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-line-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-line-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-live-chat-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-live-chat-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-messages-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-messages-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-messenger-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-messenger-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-metrics-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-metrics-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-mms-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-mms-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-mobile-app-messaging-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-mobile-app-messaging-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-mobile-identity-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-mobile-identity-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-moments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-moments-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-number-activation-state-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-number-activation-state-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-number-lookup-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-number-lookup-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-numbers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-numbers-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-omni-failover-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-omni-failover-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-open-channel-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-open-channel-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-openapi-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-people-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-people-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-rcs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-rcs-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-resources-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-resources-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-sending-strategy-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-sending-strategy-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-signals-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-signals-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-sms-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-sms-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-subscriptions-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-subscriptions-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-tiktok-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-tiktok-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-viber-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-viber-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-vocalize-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-vocalize-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-voice-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-voice-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-webrtc-calls-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-webrtc-calls-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-whatsapp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-whatsapp-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-zalo-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-zalo-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/infobip/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/agentic-access/infobip-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/infobip-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/security/infobip-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/infobip-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/security/infobip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infobip-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/scopes/infobip-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/infobip-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/authentication/infobip-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/openapi/_original/infobip-platform-full-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/infobip-platform-full-openapi.json
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
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/packages/infobip-packages.yml
  title: ''
  type: Packages
  url: packages/infobip-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/packages/infobip-packages.yml
  title: ''
  type: SDKs
  url: packages/infobip-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/well-known/infobip-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/infobip-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/well-known/infobip-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/infobip-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/well-known/infobip-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/infobip-api-catalog.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/well-known/infobip-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/infobip-openid-configuration.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/mcp/infobip-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/infobip-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/mcp/infobip-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/infobip-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/llms/infobip-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/infobip-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/conventions/infobip-conventions.yml
  title: ''
  type: Conventions
  url: conventions/infobip-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/errors/infobip-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/infobip-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/errors/infobip-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/infobip-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/lifecycle/infobip-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/infobip-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/lifecycle/infobip-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/infobip-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/rate-limits/infobip-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/infobip-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/conformance/infobip-conformance.yml
  title: ''
  type: Conformance
  url: conformance/infobip-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.infobip.com/certificates
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/security/infobip-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/infobip-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.infobip.com/security-trust-center/cvd-policy
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/asyncapi/infobip-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/infobip-webhooks-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/asyncapi/infobip-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/infobip-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/data-model/infobip-data-model.yml
  title: ''
  type: DataModel
  url: data-model/infobip-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/sandbox/infobip-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/infobip-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/components/infobip-components.yml
  title: ''
  type: Components
  url: components/infobip-components.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/changelog/infobip-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/infobip-changelog.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/overlays/infobip-platform-full-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/infobip-platform-full-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/skills/infobip-send-sms-and-confirm-delivery.md
  title: ''
  type: AgentSkill
  url: skills/infobip-send-sms-and-confirm-delivery.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/skills/infobip-send-whatsapp-template-message.md
  title: ''
  type: AgentSkill
  url: skills/infobip-send-whatsapp-template-message.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/skills/infobip-two-factor-authentication.md
  title: ''
  type: AgentSkill
  url: skills/infobip-two-factor-authentication.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/skills/infobip-verify-identity-with-network-apis.md
  title: ''
  type: AgentSkill
  url: skills/infobip-verify-identity-with-network-apis.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/skills/infobip-send-email-and-manage-deliverability.md
  title: ''
  type: AgentSkill
  url: skills/infobip-send-email-and-manage-deliverability.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/skills/infobip-manage-people-profiles.md
  title: ''
  type: AgentSkill
  url: skills/infobip-manage-people-profiles.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/skills/infobip-provision-numbers-and-webhooks.md
  title: ''
  type: AgentSkill
  url: skills/infobip-provision-numbers-and-webhooks.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/infobip/refs/heads/main/skills/infobip-omnichannel-send-with-failover.md
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
json_schemas:
- name: OmniAdvancedRequest
  property_count: 19
  slug: infobip-04790a6ae08cb63186016b6e4b8eb1c003a31d6a3227220686470a5721dc2d02-omni-advanced-request
- name: ArticleDetailResponse
  property_count: 24
  slug: infobip-09ef6171198229ad9a73a413d2271afa3ba31b9abbd6cd8a0cc9563fd721f1ed-article-detail-response
- name: TollFreeUnifiedNumberCampaignApiModel
  property_count: 40
  slug: infobip-2700ea5ecfd0574f21019319e90eb63416ede8263eab67e466c718c51cd1a77a-toll-free-unified-number-campaign-api-model
- name: QueryAiAssistantApiResponse
  property_count: 2
  slug: infobip-2a53d681c9399f766b0cfff54e0469d04419b36fc1603e6db03e69cc8ad55f34-query-ai-assistant-api-response
- name: RetrieveContextApiResponse
  property_count: 1
  slug: infobip-2a53d681c9399f766b0cfff54e0469d04419b36fc1603e6db03e69cc8ad55f34-retrieve-context-api-response
- name: RetrieveContextRequest
  property_count: 5
  slug: infobip-2a53d681c9399f766b0cfff54e0469d04419b36fc1603e6db03e69cc8ad55f34-retrieve-context-request
- name: SimpleAiAssistantQuery
  property_count: 4
  slug: infobip-2a53d681c9399f766b0cfff54e0469d04419b36fc1603e6db03e69cc8ad55f34-simple-ai-assistant-query
- name: SendMimeRequestSchema
  property_count: 13
  slug: infobip-34438aa163eb13a2a06ad96ae98170e41cc2ee8902e8b7655aba73ceb0bb23f1-send-mime-request-schema
- name: SendRequestSchema
  property_count: 37
  slug: infobip-34438aa163eb13a2a06ad96ae98170e41cc2ee8902e8b7655aba73ceb0bb23f1-send-request-schema
- name: CallLog
  property_count: 24
  slug: infobip-431fb79b0e816230968e14ba1e1c6fadb75cfde9cb3c381f4217b2777f48153f-call-log
- name: MoConfigurationRequest
  property_count: 4
  slug: infobip-7c77a2c703ce12a601f120565936de62cf48d1baf9232d5411f82fc339353553-mo-configuration-request
- name: EnrollmentSessionRequest
  property_count: 7
  slug: infobip-8a19359d3a412667abbd2d38733e247b91417d2a845ae41758328736ea0ecce9-enrollment-session-request
- name: ExtractionSessionRequest
  property_count: 7
  slug: infobip-8a19359d3a412667abbd2d38733e247b91417d2a845ae41758328736ea0ecce9-extraction-session-request
- name: VerificationSessionRequest
  property_count: 8
  slug: infobip-8a19359d3a412667abbd2d38733e247b91417d2a845ae41758328736ea0ecce9-verification-session-request
- name: IamPersonV2
  property_count: 22
  slug: infobip-a8ed60f1ed4abc0dfe4d5460edd3205f89585f2cd4b436e4d83a1231d28c264c-iam-person-v2
- name: RecordingMetadataApiModel
  property_count: 22
  slug: infobip-b979cda441a7c661201042835d7dc18eaec3fa68a2905164912469051f8b8866-recording-metadata-api-model
- name: CreateApiKeyRequest
  property_count: 8
  slug: infobip-bb8af9c2d2d4d677e25555100e31662e23d86ede8b5d73bbf4974b4decdd08d7-create-api-key-request
- name: UpdateApiKeyRequest
  property_count: 9
  slug: infobip-bb8af9c2d2d4d677e25555100e31662e23d86ede8b5d73bbf4974b4decdd08d7-update-api-key-request
- name: Message
  property_count: 15
  slug: infobip-c3b21d2ffef2552e10577daa67c904ac80618665b001ef386a4faefc515e78f3-message
- name: SmsOrVoiceMessage
  property_count: 12
  slug: infobip-c3b21d2ffef2552e10577daa67c904ac80618665b001ef386a4faefc515e78f3-sms-or-voice-message
- name: CreateRcsSenderApiRequest
  property_count: 16
  slug: infobip-c4d4776b979fea48176211c392051aca0dae21d75b7a9ca349c8f2eb95a84913-create-rcs-sender-api-request
- name: RcsSender
  property_count: 19
  slug: infobip-c4d4776b979fea48176211c392051aca0dae21d75b7a9ca349c8f2eb95a84913-rcs-sender
- name: CamaraKycMatchRequestDto
  property_count: 20
  slug: infobip-c4fb96364cd87b1d1d15720880c5153ef26f58342e4ec03b9d5896f2251f17ae-camara-kyc-match-request-dto
- name: CamaraKycMatchResponseDto
  property_count: 32
  slug: infobip-c4fb96364cd87b1d1d15720880c5153ef26f58342e4ec03b9d5896f2251f17ae-camara-kyc-match-response-dto
- name: SmvVerifyAdvancedRequestDto
  property_count: 8
  slug: infobip-c4fb96364cd87b1d1d15720880c5153ef26f58342e4ec03b9d5896f2251f17ae-smv-verify-advanced-request-dto
- name: AvailableProducts
  property_count: 1
  slug: infobip-d2eeca5070e19d116b5e48cb8dbc21132490d09f32a707af8c36324fa50d906d-available-products
- name: OpenAPI
  property_count: 0
  slug: infobip-d2eeca5070e19d116b5e48cb8dbc21132490d09f32a707af8c36324fa50d906d-open-api
- name: SegmentCreateDto
  property_count: 4
  slug: infobip-d76a8e2b7d80b5cb0751e11a31b96eabeaf6b2ec1de2932507f7f2749e61e91c-segment-create-dto
- name: SegmentResponseDto
  property_count: 7
  slug: infobip-d76a8e2b7d80b5cb0751e11a31b96eabeaf6b2ec1de2932507f7f2749e61e91c-segment-response-dto
- name: SegmentUpdateDto
  property_count: 4
  slug: infobip-d76a8e2b7d80b5cb0751e11a31b96eabeaf6b2ec1de2932507f7f2749e61e91c-segment-update-dto
jsonld:
- class_count: 120
  name: Infobip Context
  property_count: 193
  slug: infobip-context
layout: provider
mcp_servers:
- description: 'Infobip runs a FLEET of remote MCP servers rather than a single endpoint: one server

    per API product, all on https://mcp.infobip.com/{product}. Streamable HTTP is the

    default transport, SSE is availab'
  name: Infobip MCP Server
  slug: infobip-mcp-yml
modified: '2026-09-16'
name: Infobip
nav: Providers
network: true
overview: 'Infobip publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AI Hub API, Channels API, Connectivity API, and 3 more. Tagged areas include Telecommunications, Croatia, CPaaS, Messaging, and SMS.


  The Infobip catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Infobip''s developer surface includes authentication, documentation, API reference, SDKs, signup flow, pricing, changelog, and 113 more developer resources.'
plans:
- name: Infobip Plans Pricing
  plan_count: 4
  slug: infobip-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 44
  name: Infobip Rate Limits
  slug: infobip-rate-limits
rules:
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Infobip API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 4
  slug: infobip-rules
scopes:
- name: Infobip Scopes
  scope_count: 159
  slug: infobip-scopes
  summary_line: 159 scopes · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 82.4
  coverage:
    artifact_dirs: 34
    catalog_earned: 80.8
    catalog_earned_first_party: 12.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 72.1
    developer_ergonomics: 68.5
    discoverability: 83.3
    operational_transparency: 68.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 81.8
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
    score: 55.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 61.1
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
- Communications
website: https://www.infobip.com/
---
