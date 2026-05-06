---
aid: bloomberg-instant-messaging
name: Bloomberg Instant Messaging
description: Bloomberg Instant Messaging (IB) is a secure, compliant messaging platform embedded in the Bloomberg Terminal and accessible via Bloomberg Anywhere. It enables real-time communication between financial professionals globally, with message archiving, compliance monitoring, and integration capabilities. Bloomberg also provides B-Chat for broader enterprise messaging connectivity.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-instant-messaging/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Messaging
  - Instant Messaging
  - Compliance
  - Financial Communication
  - Bloomberg IB
  - Bloomberg
apis:
  - aid: bloomberg-instant-messaging:bloomberg-ib-api
    name: Bloomberg IB Messaging API
    description: Programmatic access to Bloomberg's secure IB messaging network for sending and receiving messages within the Bloomberg Terminal ecosystem. Supports integration with trading and compliance systems for automated messaging workflows.
    humanURL: https://www.bloomberg.com/professional/product/bloomberg-messaging/
    baseURL: blpapi://localhost:8194
    tags:
      - IB Messaging
      - Secure Messaging
      - Terminal Messaging
      - Compliance
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/product/bloomberg-messaging/
  - aid: bloomberg-instant-messaging:bloomberg-bchat
    name: Bloomberg B-Chat
    description: Bloomberg's enterprise communication platform extending the Bloomberg messaging network to broader enterprise connectivity, enabling compliant communication with financial counterparties outside the Bloomberg Terminal.
    humanURL: https://www.bloomberg.com/professional/product/bloomberg-messaging/
    baseURL: https://messaging.bloomberg.com
    tags:
      - B-Chat
      - Enterprise Messaging
      - Counterparty Communication
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
        description: End-to-end secure messaging between financial professionals on the Bloomberg network.
      - name: Message Archiving
        description: Automatic message archiving for compliance and regulatory requirements.
      - name: Compliance Controls
        description: Supervision tools for monitoring and reviewing communications.
      - name: Group Chats
        description: Multi-participant group chats and chat rooms for financial discussions.
      - name: File Sharing
        description: Secure file and document sharing within the messaging platform.
      - name: Bloomberg Anywhere Access
        description: Access Bloomberg messaging from mobile and remote devices via Bloomberg Anywhere.
  - type: UseCases
    data:
      - name: Trade Negotiation
        description: Negotiate trades and discuss pricing in real time with counterparties.
      - name: Research Distribution
        description: Share research reports and market insights with clients and colleagues.
      - name: Compliance Surveillance
        description: Archive and monitor communications for regulatory compliance.
      - name: Client Communication
        description: Maintain compliant communication records with institutional clients.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
