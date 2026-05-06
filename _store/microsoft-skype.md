---
aid: microsoft-skype
name: Microsoft Skype
description: Microsoft Skype provides communication APIs for voice, video, and messaging. For new development, Azure Communication Services is the recommended successor, providing cloud-based communication capabilities including calling, SMS, chat, and email.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Communication
  - Messaging
  - Microsoft
  - Video
  - Voice
url: https://raw.githubusercontent.com/api-evangelist/microsoft-skype/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-skype:skype-uris
    name: Skype URIs API
    tags:
      - Communication
      - Messaging
      - Video
      - Voice
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/skype-sdk/skypeuris/skypeuris
    properties:
      - url: https://learn.microsoft.com/en-us/skype-sdk/skypeuris/skypeuris
        type: Documentation
    description: Skype URIs provide a mechanism for launching Skype actions from web pages and applications. Developers can create links that initiate calls, video calls, and chat conversations with specified Skype users, enabling communication integration without complex API integration.
  - aid: microsoft-skype:communication-api
    name: Azure Communication Services
    tags:
      - Chat
      - Communication
      - SMS
      - Video
      - Voice
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{resource}.communication.azure.com/
    humanURL: https://learn.microsoft.com/en-us/azure/communication-services/
    properties:
      - url: https://learn.microsoft.com/en-us/azure/communication-services/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/
        type: Getting Started
    description: Azure Communication Services (successor to Skype developer APIs) provides cloud-based communication APIs for voice calling, video calling, SMS messaging, email, and chat. It powers Microsoft Teams interoperability and enables developers to build rich communication experiences in custom applications.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Website
    url: https://www.skype.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/communication-services/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/communication-services/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
