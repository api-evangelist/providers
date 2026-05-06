---
aid: signal
url: https://raw.githubusercontent.com/api-evangelist/signal/refs/heads/main/apis.yml
apis:
  - aid: signal:signal-protocol-specifications
    name: Signal Protocol Specifications
    tags:
      - Encryption
      - Messaging
      - Cryptography
      - Security
      - Protocols
    humanURL: https://signal.org/docs/
    properties:
      - url: https://signal.org/docs/
        type: Documentation
    description: The Signal Protocol Specifications define the core cryptographic protocols that underpin Signal's end-to-end encrypted messaging. These include the X3DH (Extended Triple Diffie-Hellman) key agreement protocol for establishing shared secrets between parties, the Double Ratchet Algorithm for deriving new encryption keys per message, the PQXDH (Post-Quantum Extended Diffie-Hellman) protocol for quantum-resistant key agreement, and XEdDSA for EdDSA-compatible signature schemes. These specifications are published independently so they can be adopted by other projects beyond Signal itself.
  - aid: signal:signal-libsignal-sdk
    name: Signal libsignal SDK
    tags:
      - SDK
      - Encryption
      - Cryptography
      - Java
      - Swift
      - TypeScript
      - Rust
    humanURL: https://github.com/signalapp/libsignal
    properties:
      - url: https://github.com/signalapp/libsignal
        type: GitHub
      - url: https://github.com/signalapp/libsignal
        type: Documentation
    description: The libsignal SDK provides platform-agnostic APIs used by the official Signal clients and server. It implements the Signal Protocol including the Double Ratchet algorithm, as well as other cryptographic primitives such as AES-GCM encryption and zero-knowledge group functionality. The core implementations are written in Rust, with bindings exposed as Java, Swift, and TypeScript libraries.
  - aid: signal:signal-server
    name: Signal Server
    tags:
      - Messaging
      - Server
      - Backend
      - Encryption
      - Open Source
    humanURL: https://github.com/signalapp/Signal-Server
    baseURL: https://chat.signal.org
    properties:
      - url: https://github.com/signalapp/Signal-Server
        type: GitHub
      - url: https://github.com/signalapp/Signal-Server
        type: Documentation
      - url: openapi/signal-server-openapi.yml
        type: OpenAPI
      - url: asyncapi/signal-server-asyncapi.yml
        type: AsyncAPI
      - url: rules/signal-rules.yml
        type: SpectralRules
      - url: capabilities/secure-messaging.yaml
        type: Capabilities
      - url: json-schema/signal-protocol-entities-schema.json
        type: JSONSchema
      - url: json-ld/signal-context.jsonld
        type: JSONLD
      - url: vocabulary/signal-vocabulary.yml
        type: Vocabulary
    description: Signal-Server is the open-source server backend that supports the Signal Private Messenger applications on Android, Desktop, and iOS. Built as a Dropwizard application, it provides REST controllers for account management, message delivery, key distribution, and device provisioning, along with gRPC services and WebSocket endpoints for real-time communication. The server handles user registration, encrypted message routing, push notification delivery, and pre-key bundle management.
  - aid: signal:signal-android-sdk
    name: Signal Android SDK
    tags:
      - Android
      - Mobile
      - Messaging
      - Encryption
      - Open Source
    humanURL: https://github.com/signalapp/Signal-Android
    properties:
      - url: https://github.com/signalapp/Signal-Android
        type: GitHub
      - url: https://github.com/signalapp/Signal-Android
        type: Documentation
    description: Signal-Android is the open-source Android client for the Signal encrypted messaging platform. It provides the full messaging experience including end-to-end encrypted text messages, voice calls, video calls, group chats, and media sharing. The application integrates the libsignal protocol library for cryptographic operations and communicates with the Signal Server for message routing and delivery.
  - aid: signal:signal-ios-sdk
    name: Signal iOS SDK
    tags:
      - iOS
      - Mobile
      - Messaging
      - Encryption
      - Open Source
    humanURL: https://github.com/signalapp/Signal-iOS
    properties:
      - url: https://github.com/signalapp/Signal-iOS
        type: GitHub
      - url: https://github.com/signalapp/Signal-iOS
        type: Documentation
    description: Signal-iOS is the open-source iOS client for the Signal encrypted messaging platform. It delivers end-to-end encrypted messaging, voice calls, video calls, and group communications on iPhone and iPad devices. The application uses the libsignal protocol library for all cryptographic operations and connects to the Signal Server infrastructure for message delivery and synchronization.
  - aid: signal:signal-desktop-sdk
    name: Signal Desktop SDK
    tags:
      - Desktop
      - Electron
      - Messaging
      - Encryption
      - Open Source
    humanURL: https://github.com/signalapp/Signal-Desktop
    properties:
      - url: https://github.com/signalapp/Signal-Desktop
        type: GitHub
      - url: https://github.com/signalapp/Signal-Desktop
        type: Documentation
    description: Signal-Desktop is the open-source desktop client for the Signal encrypted messaging platform, built with Electron and TypeScript. It provides end-to-end encrypted messaging, voice calls, video calls, and group communications on Windows, macOS, and Linux. The desktop client links to an existing Signal mobile account and synchronizes messages across devices.
name: Signal
tags:
  - Encryption
  - Messaging
  - Security
  - Cryptography
  - Open Source
  - Privacy
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-20'
modified: '2026-05-02'
position: Consuming
segments:
  - Messaging
  - Security
  - Cryptography
description: Signal is a privacy-focused messaging platform that provides end-to-end encrypted communication through open-source applications on mobile and desktop. Their developer ecosystem centers around the open-source Signal Protocol, client SDKs, and server infrastructure, enabling developers to study, audit, and integrate secure messaging capabilities. The Signal Protocol is the most widely deployed end-to-end encryption protocol in the world, used by Signal, WhatsApp, Google Messages, and other platforms.
common:
  - type: Website
    url: https://signal.org/
  - type: Documentation
    url: https://signal.org/docs/
  - type: Blog
    url: https://signal.org/blog/
  - type: Support
    url: https://support.signal.org/
  - type: TermsOfService
    url: https://signal.org/legal/
  - type: PrivacyPolicy
    url: https://signal.org/legal/#privacy-policy
  - type: GitHub
    url: https://github.com/signalapp
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
