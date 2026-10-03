---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 31
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering Communications Platform as a Service (CPaaS) and messaging-and-voice infrastructure APIs. This network gathers providers offering programmable SMS, MMS, voice, video, transactional and marketing email, chat, push notifications, in-app messaging, and deliverability services. It includes leading CPaaS platforms (Twilio, Vonage, MessageBird/Bird, Sinch, Plivo, Bandwidth, Telnyx, Infobip), transactional email providers (SendGrid, Mailgun, Postmark, Resend, SparkPost, Mailjet, MailerSend, Mailtrap), video and real-time platforms (Agora, Daily.co, LiveKit, Zoom, Dolby), push and in-app messaging (OneSignal, Pusher, Ably, PubNub, Sendbird, Airship, CleverTap), and notification orchestration layers (Courier, Knock, Customer.io, Braze, Iterable). It is distinct from the Bots topic, which covers conversational scripting and chatbot frameworks.
examples:
- key_count: 10
  name: Communications Delivery Receipt Example
  slug: communications-delivery-receipt-example
- key_count: 13
  name: Communications Message Example
  slug: communications-message-example
features:
- description: CPaaS providers expose programmable APIs for sending and receiving SMS and MMS messages, placing and routing voice calls, and managing phone number inventory across the global PSTN.
  name: Programmable SMS, MMS, and Voice
- description: Email APIs handle high-volume transactional sends, marketing campaigns, template rendering, list management, and deliverability monitoring through ESP infrastructure.
  name: Transactional and Marketing Email
- description: Video and real-time platforms expose APIs and SDKs for embedding live video calls, broadcasts, conferences, and low-latency audio rooms into applications.
  name: Real-Time Video and Audio
- description: Push providers deliver native iOS and Android push notifications, web push, and in-app messages at scale across FCM, APNs, and proprietary delivery infrastructure.
  name: Push Notifications and In-App Messaging
- description: Realtime APIs provide WebSocket-based pub/sub channels, chat rooms, presence, and message history for collaborative and social applications.
  name: Realtime Chat and Pub/Sub
- description: Orchestration platforms unify SMS, email, push, chat, and in-app channels behind a single API with templating, preference management, and routing logic.
  name: Notification Orchestration and Multi-Channel Delivery
- description: Deliverability tooling covers IP warmup, SPF/DKIM/DMARC, bounce and spam handling, suppression lists, and engagement-based sender reputation analytics.
  name: Deliverability and Reputation Management
- description: Communications APIs manage phone number purchase, porting, regulatory compliance, and verification flows like one-time passwords and silent network auth.
  name: Number Provisioning and Verification
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Leading CPaaS provider offering programmable SMS, MMS, voice, video, email (via SendGrid), and verification APIs at global scale.
  name: Twilio
- description: CPaaS platform covering SMS, voice, video, verify, and conversation APIs across messaging channels including WhatsApp and Viber.
  name: Vonage
- description: Transactional and marketing email API owned by Twilio, handling high-volume sends, templates, and deliverability.
  name: SendGrid
- description: Omnichannel CPaaS provider (Bird) offering SMS, voice, email, WhatsApp, and conversational messaging APIs across global carriers.
  name: MessageBird
- description: Global CPaaS platform delivering SMS, voice, email (Mailgun, Mailjet), verification, and conversational messaging APIs.
  name: Sinch
- description: Push notification, in-app messaging, email, and SMS platform with a unified messaging API used by mobile and web applications.
  name: OneSignal
- description: In-app chat, messaging, and calls API powering customer support and social experiences inside mobile and web applications.
  name: Sendbird
- description: WebRTC-based video and audio API for embedding live calls, broadcasts, and recording into web and mobile applications.
  name: Daily.co
- description: Transactional email and email validation API focused on deliverability for developers and high-volume senders.
  name: Mailgun
json_schemas:
- name: DeliveryReceipt
  property_count: 12
  slug: communications-delivery-receipt
- name: Message
  property_count: 16
  slug: communications-message
json_structures:
- name: Communications Delivery Receipt Structure
  property_count: 12
  slug: communications-delivery-receipt-structure
- name: Communications Message Structure
  property_count: 16
  slug: communications-message-structure
jsonld:
- class_count: 10
  name: Communications Context
  property_count: 21
  slug: communications-context
layout: provider
modified: '2026-05-19'
name: Communications
nav: Providers
network: true
overview: 'Communications is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CPaaS, SMS, MMS, Voice, and Email.


  The Communications catalog on APIs.io includes 1 JSON-LD context.


  Communications'' developer surface includes developer portal and 1 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 4.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: communications
tags:
- CPaaS
- SMS
- MMS
- Voice
- Email
- Push Notifications
- Video
- Chat
- Messaging
- Deliverability
use_cases:
- description: Applications use SMS, voice, and email APIs to deliver one-time passcodes and verification messages for login, signup, and high-risk action confirmation.
  name: Two-Factor Authentication and OTP Delivery
- description: Platforms send order confirmations, shipping updates, password resets, and account alerts through email, SMS, and push APIs as part of core product workflows.
  name: Transactional Notifications
- description: Marketing teams orchestrate multi-channel email, SMS, and push campaigns using providers like Braze, Iterable, Customer.io, and Klaviyo to drive retention and lifecycle messaging.
  name: Customer Engagement Campaigns
- description: Telehealth, education, and collaboration apps embed branded live video and audio experiences using Daily.co, Agora, LiveKit, Zoom SDKs, and Dolby.
  name: Live Video and Audio Embeds
- description: Support and sales teams build programmable IVRs, click-to-call, call tracking, and conversational voice flows on Twilio, Vonage, Dialpad, and RingCentral.
  name: Contact Center and Programmable Voice
- description: Apps add direct messaging, group chat, presence, and live commenting using Sendbird, Stream, PubNub, Ably, and Pusher.
  name: Realtime Chat and Social Features
- description: Engineering and SRE teams page on-call staff and broadcast incident status via SMS, voice, push, and email through Knock, Courier, and CPaaS providers.
  name: Operational and Incident Alerting
website: https://apievangelist.com
---
