---
aid: jms
name: JMS
description: Java Message Service (JMS), now known as Jakarta Messaging, is a Java API that allows applications to create, send, receive, and read messages. It defines a common enterprise messaging API for loosely coupled, reliable, and asynchronous communication between distributed application components. Current release is Jakarta Messaging 3.1 (Jakarta EE 10).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise Integration
  - Jakarta EE
  - Java
  - JMS
  - Messaging
  - Standard
url: https://raw.githubusercontent.com/api-evangelist/jms/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jms:jms
    name: Jakarta Messaging
    description: The Jakarta Messaging (formerly Java Message Service) specification for enterprise messaging and asynchronous communication between distributed components. Defines point-to-point queues and publish/subscribe topics with guaranteed delivery semantics.
    humanURL: https://jakarta.ee/specifications/messaging/
    tags:
      - Enterprise Integration
      - Java
      - Messaging
    properties:
      - type: Specification (3.1)
        url: https://jakarta.ee/specifications/messaging/3.1/
      - type: Specification (3.0)
        url: https://jakarta.ee/specifications/messaging/3.0/
      - type: Specification (2.0)
        url: https://jakarta.ee/specifications/messaging/2.0/
      - type: JavaDoc
        url: https://jakarta.ee/specifications/messaging/3.1/apidocs/
      - type: GitHub Repository
        url: https://github.com/jakartaee/messaging
common:
  - type: Website
    url: https://jakarta.ee/specifications/messaging/
  - type: Documentation
    url: https://jakarta.ee/specifications/messaging/3.1/
  - type: GitHub Organization
    url: https://github.com/jakartaee
  - type: Issues
    url: https://github.com/jakartaee/messaging/issues
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
