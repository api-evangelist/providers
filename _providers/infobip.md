---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 62.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1172
  human_in_the_loop: 30
  name: Infobip Agentic Access
  operation_count: 1886
  slug: infobip-agentic-access
  summary_line: 1886 operations · 1172 acting · 30 human-in-the-loop
api_count: 47
apis:
- description: Infobip's Two Factor Authentication API for OTP (One Time Passcode) delivery and verification. OTPs can be delivered over SMS, Voice or Email. Learn more about the workflow and setup. You can use SDKs
  name: Infobip 2FA API
  slug: infobip-2fa
- description: Manage your Infobip account details, such as individual users and api keys. — 13 operation path(s) and 0 webhook(s) in Infobip's published OpenAPI.
  name: Infobip Account management API
  slug: infobip-account-management
- description: Infobip AI assistant is a retrieval-augmented generation (RAG) solution that performs tasks based on documents and instructions you specify. This means the AI draws answers directly from your document
  name: Infobip AI Assistants API
  slug: infobip-ai-assistants
- description: Answers is the Infobip fully-encompassed chatbot building platform that enables you to build, test, and deploy highly customized chatbots of different types. Multiple channels are supported on Answers
  name: Infobip Answers API
  slug: infobip-answers
- description: Use Apple Messages for Business to contact customers in real time. Through the Messages app on iOS, macOS, watchOS, and iPadOS, Apple Messages for Business makes it easy for customers to communicate w
  name: Infobip Apple Messages for Business API
  slug: infobip-apple-mfb
- description: Applications and Entities are designed to be flexible and modular to give you the opportunity to define your business environment, use cases, applications, customers, assets, etc. on the Infobip platf
  name: Infobip Application and Entity Management API
  slug: infobip-application-entity
- description: The Billing Usage API gives you programmatic access to the same billing data behind your monthly invoices. Query costs on demand, integrate results into your own systems, and build automated reporting
  name: Infobip Billing Usage API
  slug: infobip-billing-usage-api
- description: Represents a set of services used for biometric authentication and identity proofing of the end user. — 5 operation path(s) and 4 webhook(s) in Infobip's published OpenAPI.
  name: Infobip Biometrics API
  slug: infobip-biometrics
- description: Phone numbers and email addresses (referred to as destinations) that no longer want to be contacted are stored inside a Blocklist (also known as Do Not Contact List) This platform feature is used to m
  name: Infobip Blocklist API
  slug: infobip-blocklist
- description: Contact us and get started with CAMARA. Please fill out the form, and our experts will contact you shortly. CAMARA represents a set of services that we offer in cooperation with the mobile network ope
  name: Infobip CAMARA API
  slug: infobip-camara
- description: Create and manage your catalogs to use with other Infobip solutions. Catalogs are similar to databases, you can store and retrieve data sets. Concepts explained Catalog - a set of records. Each record
  name: Infobip Catalogs API
  slug: infobip-catalogs-api
- description: Reuse assets created on Infobip SaaS products in order to recreate configuration more easily on a single or across multiple accounts. Export or share Moments flows, Answers chatbots or other SaaS asse
  name: Infobip Common Assets API
  slug: infobip-common-assets
- description: Conversations is a solution that allows Enterprises to engage in conversations with their customers over multiple channels. The solution is available either as a web-based cloud platform web interface
  name: Infobip Conversations API
  slug: infobip-conversations
- description: Infobip Email is a cloud-based, all-in-one communication solution suited for both transactional and marketing email message delivery. It allows users to create rich, personalized, and responsive email
  name: Infobip Email API
  slug: infobip-email
- description: 'Instagram DMs are an in-app messaging feature that enables your business to be reachable by your customers over one of the most popular social media platforms. To utilize Instagram DMs in combination '
  name: Infobip Instagram Direct Messages API
  slug: infobip-instagram
- description: Kakao Talk holds immense value in the Korean market due to its widespread adoption, versatile features, and seamless integration into various aspects of daily life. In South Korea, Kakao Talk has beco
  name: Infobip Kakao Talk API
  slug: infobip-kakao
- description: Knowledge Base is a centralized content management system for creating, organizing, and retrieving articles, attachments, and structured content. Content is organized into categories, folders, and a h
  name: Infobip Knowledge Base API
  slug: infobip-knowledge-base
- description: 'Disrupt the Southeast Asian market with LINE messaging. Send timely notifications and reminders to your customers, through pre-approved templates, so they can take prompt action and never miss out on '
  name: Infobip LINE API
  slug: infobip-line
- description: Infobip Live Chat product offers real-time chat communication with customer on your website or in through your mobile app. More information about the product you can find at Live Chat product document
  name: Infobip Live Chat API
  slug: infobip-live-chat
- description: The Messages API integrates multiple messaging channels into one interface. Instead of using a separate API for each messaging channel, use only one API for multiple channels and message types. — 5 op
  name: Infobip Messages API API
  slug: infobip-messages-api
- description: Grow your business with conversations on Messenger. To utilize Messenger in combination with other channels, check out Messages API. — 11 operation path(s) and 5 webhook(s) in Infobip's published Open
  name: Infobip Messenger API
  slug: infobip-messenger
- description: Metrics API is a way to access aggregated traffic information. By integrating this API, you can retrieve analytics related to your communications and build your own reporting facilities. — 2 operation
  name: Infobip Metrics API
  slug: infobip-metrics-api
- description: Infobip MMS API allows you to send and receive MMS messages and receive delivery reports on your endpoint in real time. You can send messages up to 1600 characters in length together with multimedia c
  name: Infobip MMS API
  slug: infobip-mms
- description: Mobile push and in-app messaging is a set of API requests to send mobile push and in-app messages, receive data about an application with a mobile SDK​, and receive statistics and reports about push m
  name: Infobip Mobile push and in-app messaging API
  slug: infobip-mobile-app-messaging
- description: Contact us and get started with Mobile Identity. Please fill out the form, and our experts will contact you shortly. — 8 operation path(s) and 3 webhook(s) in Infobip's published OpenAPI.
  name: Infobip Mobile Identity API
  slug: infobip-mobile-identity
- description: Use Moments to set up and manage automated messaging campaigns with your customers by building conversation workflows. — 7 operation path(s) and 0 webhook(s) in Infobip's published OpenAPI.
  name: Infobip Moments API
  slug: infobip-moments
- description: Number Activation State are reports with end user numbers that had a change in their activation status. Those would be usually numbers that become deactivated, however sometimes they would also have i
  name: Infobip Number Activation State API
  slug: infobip-number-activation-state
- description: Number Lookup is a product that draws information from Home Location Register which is a database that contains important information about every mobile subscriber of a specific mobile network. — 3 op
  name: Infobip Number lookup API
  slug: infobip-number-lookup
- description: Numbers are essential for two way communication and your branding. Buy and manage your numbers to send and receive messages and voice calls. — 47 operation path(s) and 7 webhook(s) in Infobip's publis
  name: Infobip Numbers API
  slug: infobip-numbers
- description: 'Send messages over WhatsApp, Viber, Voice, VKontakte, Line and other channels with a failover to SMS or any other channel of your choice. — 5 operation path(s) and 3 webhook(s) in Infobip''s published '
  name: Infobip OMNI Failover API
  slug: infobip-omni-failover
- description: 'Open Channel enables your system to exchange messages with Infobip SaaS products through the Infobip public API. Inbound messages are sent through the Infobip API to the Open Channel destination that '
  name: Infobip Open Channel API
  slug: infobip-open-channel
- description: OpenAPI is an industry-standard specification for defining REST APIs. It allows you to generate client libraries, automate API testing, and streamline integration workflows. Infobip OpenAPI specificat
  name: Infobip OpenAPI Specification API
  slug: infobip-openapi
- description: 'Build rich profiles for each person to create audience segments for more precise targeting. Manage duplicates and import your data over API. Events reflect actions that end users take on your website '
  name: Infobip People API
  slug: infobip-people
- description: Rich Communication Services (RCS) is a new, visually appealing messaging channel that offers rich functionalities to enable more engaging customer journeys. RCS is sometimes referred to as the “SMS 2.
  name: Infobip RCS API
  slug: infobip-rcs
- description: The Resources API is a set of endpoints designed to manage and request communication resources, such as alphanumeric senders and numbers. Automate resource registration, validation, and provisioning t
  name: Infobip Resources API
  slug: infobip-resources
- description: Sending Strategy represents one type of configuration for your sending resources. This configuration in its simplest form allows you to set manipulation for your senders on a country level for a speci
  name: Infobip Sending Strategy Management API
  slug: infobip-sending-strategy
- description: Signals is a solution for detecting and blocking artificially generated traffic. Each mobile device has a unique identifier assigned to it. It's called a Mobile Station International Subscriber Direct
  name: Infobip Signals API
  slug: infobip-signals
- description: SMS (Short Message Service) is the most extensive messaging service available in terms of reach and coverage. A SMS can be sent to and from any mobile device in the world and does not necessarily requ
  name: Infobip SMS API
  slug: infobip-sms
- description: Subscriptions are a way to manage notifications sent to your webhooks by Infobip. It is a useful feature if you want to narrow down the list of events to be notified about or specify different webhook
  name: Infobip Subscriptions Management API
  slug: infobip-subscriptions-api
- description: 'TikTok Business Messaging enables one-to-one conversations between TikTok users and your TikTok Business Account. With Infobip, you can receive inbound messages through webhooks, reply to users using '
  name: Infobip TikTok API
  slug: infobip-tiktok
- description: Viber offers businesses a dynamic duo of tools - Viber Business Messages and Viber Bots. These solutions are designed to revolutionize customer engagement and communication strategies, providing busin
  name: Infobip Viber API
  slug: infobip-viber
- description: Infobip Vocalize API allows you to integrate AI Gamification features into your application. — 9 operation path(s) and 0 webhook(s) in Infobip's published OpenAPI.
  name: Infobip Vocalize API
  slug: infobip-vocalize
- description: Infobip Voice API allows you to engage into voice communication with your customer using the Voice API features. With Calls API, you can use our granular APIs to create any inbound or outbound voice a
  name: Infobip Voice API
  slug: infobip-voice
- description: Infobip WebRTC provide a simplified and secure way of real-time audio and video communication over the web and inside mobile applications. It's powered by Web Real-Time Communication (WebRTC) technolo
  name: Infobip WebRTC API
  slug: infobip-webrtc-calls
- description: With 2 billion users, WhatsApp is the most used application worldwide. It enables you to reach more customers, sharing important and timely notifications, as well as provide real-time customer support
  name: Infobip WhatsApp API
  slug: infobip-whatsapp
- description: Zalo offers businesses a dynamic tool - Zalo Notification Service. This solution is designed to revolutionize customer engagement and communication strategies, providing businesses with a direct and e
  name: Infobip Zalo API
  slug: infobip-zalo
- description: Infobip OpenAPI Specification from Infobip — 652 path(s) described in OpenAPI.
  name: Infobip OpenAPI Specification
  slug: infobip-platform-full-openapi
artifact_total: 150
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
  name: infobip-mcp.yml
  slug: infobip-mcpyml
modified: '2026-07-25'
name: Infobip
nav: Providers
network: true
overview: 'Infobip publishes 47 APIs on the [APIs.io](https://apis.io/) network, including 2FA API, Account management API, AI Assistants API, and 44 more. Tagged areas include Telecommunications, Croatia, CPaaS, Messaging, and SMS.


  The Infobip catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Infobip''s developer surface includes authentication, documentation, API reference, SDKs, signup flow, pricing, changelog, and 57 more developer resources.'
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
  composite: 71.5
  delta: 6.1
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 66.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 68.4
  previous_composite: 65.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 47
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 93.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
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
