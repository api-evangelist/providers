---
aid: messagebird
url: https://raw.githubusercontent.com/api-evangelist/messagebird/refs/heads/main/apis.yml
apis:
- aid: messagebird:sms-messaging-api
  name: MessageBird SMS Messaging API
  tags:
  - Communications
  - Messaging
  - SMS
  - Text Messages
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://rest.messagebird.com
  humanURL: https://developers.messagebird.com/api/sms-messaging/
  properties:
  - url: https://developers.messagebird.com/api/sms-messaging/
    type: Documentation
  - url: openapi/messagebird-sms-messaging-openapi.yml
    type: OpenAPI
  description: The MessageBird SMS Messaging API allows developers to send and receive SMS messages to and from any country in the world through a REST interface. It supports features such as message scheduling, delivery reports, Unicode messages, and concatenated messages for longer content. The API provides both HTTP and SMPP connectivity options for high-volume messaging use cases.
- aid: messagebird:voice-calling-api
  name: MessageBird Voice Calling API
  tags:
  - Calling
  - Communications
  - Telephony
  - Voice
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://voice.messagebird.com
  humanURL: https://developers.messagebird.com/api/voice-calling/
  properties:
  - url: https://developers.messagebird.com/api/voice-calling/
    type: Documentation
  - url: openapi/messagebird-voice-calling-openapi.yml
    type: OpenAPI
  description: The MessageBird Voice Calling API enables developers to make, receive, and control phone calls programmatically. It supports call flows for building interactive voice response systems, call recording, call transfers, and real-time webhooks for call events. The API provides global coverage and can be used to build contact center solutions, automated calling systems, and voice-enabled applications.
- aid: messagebird:voice-messaging-api
  name: MessageBird Voice Messaging API
  tags:
  - Communications
  - Messaging
  - Text-To-Speech
  - Voice
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://rest.messagebird.com
  humanURL: https://developers.messagebird.com/api/voice-messaging/
  properties:
  - url: https://developers.messagebird.com/api/voice-messaging/
    type: Documentation
  - url: openapi/messagebird-voice-messaging-openapi.yml
    type: OpenAPI
  description: The MessageBird Voice Messaging API enables developers to transform text messages into voice messages delivered to any country. It supports 26 languages with configurable attributes such as male or female voice, speaking rate, repeat options, and scheduling. The API is useful for sending voice notifications, alerts, and one-time passwords to users who may not have access to SMS.
- aid: messagebird:conversations-api
  name: MessageBird Conversations API
  tags:
  - Chat
  - Communications
  - Messaging
  - Omnichannel
  - WhatsApp
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://conversations.messagebird.com
  humanURL: https://developers.messagebird.com/api/conversations/
  properties:
  - url: https://developers.messagebird.com/api/conversations/
    type: Documentation
  - url: openapi/messagebird-conversations-openapi.yml
    type: OpenAPI
  - url: asyncapi/messagebird-conversations-asyncapi.yml
    type: AsyncAPI
  description: The MessageBird Conversations API provides a unified interface for managing omnichannel messaging across platforms such as SMS, WhatsApp, Facebook Messenger, Telegram, and more. It consolidates messages from multiple channels into a single conversation thread per contact, enabling consistent customer communication. The API supports sending and receiving messages, managing conversation state, and handling webhooks for real-time event processing.
- aid: messagebird:whatsapp-api
  name: MessageBird WhatsApp API
  tags:
  - Communications
  - Messaging
  - Notifications
  - WhatsApp
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://conversations.messagebird.com
  humanURL: https://developers.messagebird.com/api/whatsapp
  properties:
  - url: https://developers.messagebird.com/api/whatsapp
    type: Documentation
  - url: openapi/messagebird-whatsapp-openapi.yml
    type: OpenAPI
  description: The MessageBird WhatsApp API allows developers to send and receive WhatsApp messages for alerts, notifications, customer support, and two-factor authentication. It provides access to all WhatsApp Business features through a single API, including template messages, media messages, and interactive message types. The API supports rich media content and provides delivery and read receipts for message tracking.
- aid: messagebird:verify-api
  name: MessageBird Verify API
  tags:
  - OTP
  - Security
  - Two-Factor Authentication
  - Verification
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://rest.messagebird.com
  humanURL: https://developers.messagebird.com/api/verify/
  properties:
  - url: https://developers.messagebird.com/api/verify/
    type: Documentation
  - url: openapi/messagebird-verify-openapi.yml
    type: OpenAPI
  description: The MessageBird Verify API provides a simple way to implement two-factor authentication and phone number verification. It generates and validates one-time passwords delivered via SMS or voice call, handling token generation, delivery, and verification in a single workflow. The API supports configurable token length, expiration time, and delivery channel selection for flexible integration into sign-up and login flows.
- aid: messagebird:lookup-api
  name: MessageBird Lookup API
  tags:
  - HLR
  - Number Intelligence
  - Phone Numbers
  - Validation
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://rest.messagebird.com
  humanURL: https://developers.messagebird.com/api/lookup/
  properties:
  - url: https://developers.messagebird.com/api/lookup/
    type: Documentation
  - url: openapi/messagebird-lookup-openapi.yml
    type: OpenAPI
  description: The MessageBird Lookup API enables developers to validate and look up mobile phone numbers. It performs HLR lookups on the mobile network to identify number format, country, operator, and availability in real-time. The API is useful for cleaning contact lists, validating user-provided phone numbers, and determining the correct format before sending messages.
- aid: messagebird:hlr-api
  name: MessageBird HLR API
  tags:
  - HLR
  - Mobile Network
  - Network Query
  - Phone Numbers
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://rest.messagebird.com
  humanURL: https://developers.messagebird.com/api/hlr/
  properties:
  - url: https://developers.messagebird.com/api/hlr/
    type: Documentation
  - url: openapi/messagebird-hlr-openapi.yml
    type: OpenAPI
  description: The MessageBird HLR API provides a way to send Home Location Register network queries to any mobile number globally. It allows developers to determine which operator a mobile number belongs to in real-time and check whether the number is currently active on the network. This API is commonly used for number portability checks, fraud prevention, and optimizing message routing.
- aid: messagebird:contacts-api
  name: MessageBird Contacts API
  tags:
  - Address Book
  - Contacts
  - Customer Data
  - Groups
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://rest.messagebird.com
  humanURL: https://developers.messagebird.com/api/contacts/
  properties:
  - url: https://developers.messagebird.com/api/contacts/
    type: Documentation
  - url: openapi/messagebird-contacts-openapi.yml
    type: OpenAPI
  description: The MessageBird Contacts API allows developers to manage contact information for end-users and customers across messaging platforms. It supports creating, reading, updating, and deleting contacts, as well as organizing them into groups for targeted messaging campaigns. A single contact can be associated with multiple communication channels such as SMS, WhatsApp, and Telegram.
- aid: messagebird:numbers-api
  name: MessageBird Numbers API
  tags:
  - Number Management
  - Phone Numbers
  - Provisioning
  - Telecommunications
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://numbers.messagebird.com
  humanURL: https://developers.messagebird.com/api/numbers/
  properties:
  - url: https://developers.messagebird.com/api/numbers/
    type: Documentation
  - url: openapi/messagebird-numbers-openapi.yml
    type: OpenAPI
  description: The MessageBird Numbers API enables developers to search for, purchase, and manage phone numbers programmatically. It supports local, toll-free, and mobile number types across multiple countries, with the ability to filter by pattern, type, and region. Purchased numbers can be configured for SMS and voice capabilities and assigned to specific messaging or calling workflows.
- aid: messagebird:balance-api
  name: MessageBird Balance API
  tags:
  - Account
  - Balance
  - Billing
  - Credits
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://rest.messagebird.com
  humanURL: https://developers.messagebird.com/api/balance/
  properties:
  - url: https://developers.messagebird.com/api/balance/
    type: Documentation
  - url: openapi/messagebird-balance-openapi.yml
    type: OpenAPI
  description: The MessageBird Balance API provides developers with access to their account balance information. It returns the current payment type, available amount, and currency for the account associated with the API key. This API is useful for monitoring credit usage, building billing dashboards, and setting up automated alerts when account balances fall below a threshold.
- aid: messagebird:integrations-api
  name: MessageBird Integrations API
  tags:
  - Integrations
  - Message Templates
  - Templates
  - WhatsApp
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://integrations.messagebird.com
  humanURL: https://developers.messagebird.com/api/integrations/
  properties:
  - url: https://developers.messagebird.com/api/integrations/
    type: Documentation
  - url: openapi/messagebird-integrations-openapi.yml
    type: OpenAPI
  description: The MessageBird Integrations API allows developers to create, fetch, and delete message templates for supported platforms. It currently supports template management for the WhatsApp platform, enabling developers to programmatically manage the templates required for sending WhatsApp Business notifications and messages. The API handles template submission, approval status tracking, and lifecycle management.
name: Messagebird
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Build powerful apps using the fastest and most reliable cloud communications APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

