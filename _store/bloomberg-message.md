---
aid: bloomberg-message
name: Bloomberg Message
description: Bloomberg Message is the core messaging service within the Bloomberg Terminal ecosystem, enabling financial professionals to communicate securely through the Bloomberg IB (Instant Bloomberg) messaging system. It provides a compliant, archived communication channel for trading desks, asset managers, and financial institutions to exchange information, research, and trade-related messages.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-message/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Messaging
  - Financial Communication
  - Bloomberg IB
  - Compliance
  - Trading Communication
  - Bloomberg
apis:
  - aid: bloomberg-message:bloomberg-ib-service
    name: Bloomberg IB (Instant Bloomberg)
    description: Bloomberg's primary secure messaging service for financial professionals, providing real-time message delivery, group chats, broadcast lists, and file sharing within the Bloomberg Terminal and Bloomberg Anywhere environments.
    humanURL: https://www.bloomberg.com/professional/product/bloomberg-messaging/
    baseURL: blpapi://localhost:8194
    tags:
      - IB
      - Instant Messaging
      - Terminal Messaging
      - Secure
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/product/bloomberg-messaging/
  - aid: bloomberg-message:bloomberg-email-gateway
    name: Bloomberg Email Gateway
    description: Gateway service enabling Bloomberg IB messages to be sent and received via email for communication with counterparties not on the Bloomberg network.
    humanURL: https://www.bloomberg.com/professional/product/bloomberg-messaging/
    baseURL: https://messaging.bloomberg.com/email
    tags:
      - Email
      - Gateway
      - External Communication
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/product/bloomberg-messaging/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://developer.bloomberg.com/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: Secure Messaging
        description: Encrypted and authenticated messaging for financial professionals.
      - name: Broadcast Lists
        description: Send messages to curated broadcast lists of contacts and clients.
      - name: Group Chats
        description: Multi-participant discussions for teams and trading desks.
      - name: Message Archiving
        description: Automatic archiving of all messages for compliance and eDiscovery.
      - name: File Transfer
        description: Share documents and files securely through the messaging platform.
      - name: Bloomberg Anywhere Integration
        description: Access Bloomberg Message from mobile and non-Terminal devices.
  - type: UseCases
    data:
      - name: Sell-Side Distribution
        description: Distribute research and trade ideas from sell-side to buy-side clients.
      - name: Trade Communication
        description: Communicate trade intentions and confirmations between counterparties.
      - name: Compliance Records
        description: Maintain compliant records of financial communications for regulators.
      - name: Market Commentary
        description: Share market commentary and analysis with clients through broadcast messages.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
