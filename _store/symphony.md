---
aid: symphony
url: >-
  https://raw.githubusercontent.com/api-search/financial/main/_apis/symphony/apis.md
apis:
  - aid: symphony:symphony-pod-api
    name: Symphony Pod API
    humanURL: https://developers.symphony.com/
    tags: []
    properties:
      - url: https://developers.symphony.com/
        type: Documentation
      - url: openapi/pod-openapi-original.yml
        type: OpenAPI
    description: >-
      The Symphony Pod API is used to build tools in order to manage and
      administer Symphony for your organization. 
  - aid: symphony:symphony-agent-api
    name: Symphony Agent API
    tags:
      - Extended
      - Message
      - Search
      - Attachment
      - Stream
      - Share
      - Echo
      - Delete
      - Subscribe
      - Unsubscribe
      - Subscribers
      - Policies
      - Enable
      - Disable
      - Dictionaries
      - Data
      - Violations
      - Privileged User
      - Datafeed
      - Read
    properties:
      - url: https://developers.symphony.com/
        type: Documentation
      - url: properties/symphony-agent-api-openapi.yml
        type: OpenAPI
    description: >-
      The Symphony Agent is responsible for encryption and decryption of
      messages and content sent to and from a bot.
  - aid: symphony:symphony-authenticator-api
    name: Symphony Authenticator API
    tags:
      - Pod
      - Authentication
    properties:
      - url: https://developers.symphony.com/
        type: Documentation
      - url: properties/symphony-authenticator-api-openapi.yml
        type: OpenAPI
    description: >-
      Tailor your portfolio exposures and risks using our hedging and
      optimization tools. Dynamically manage objectives and constraints while
      controlling for cost and tradability to meet your investment goals.
  - aid: symphony:symphony-community-connect-api
    name: Symphony Community Connect API
    tags:
      - Tenant
      - ' Users'
      - ' Company'
    properties:
      - url: https://developers.symphony.com/
        type: Documentation
      - url: properties/symphony-community-connect-api-openapi.yml
        type: OpenAPI
    description: >-
      Access the full range of Goldman Sachs indices and basket products, or
      create bespoke solutions to tailor your own investment strategies. Design,
      create, and rebalance fully-customized, ready-to-trade basket solutions to
      express thematic and risk views.
  - aid: symphony:symphony-login-api
    name: Symphony Login API
    tags:
      - Authenticate
      - Applications
      - User Names
      - Users
    properties:
      - url: https://developers.symphony.com/
        type: Documentation
      - url: properties/symphony-login-api-openapi.yml
        type: OpenAPI
    description: >-
      Programmatically manage your portfolio lifecycle from creation and update
      to scheduling reports with full control over visibility and sharing.
      Automate your portfolio workflow using our APIs - leaving you to focus on
      the alpha driving decisions.
  - aid: symphony:symphony-profile-manager-api
    name: Symphony Profile Manager API
    tags:
      - Groups
      - ' Types'
      - ' All'
      - Profiles
    properties:
      - url: https://developers.symphony.com/
        type: Documentation
      - url: properties/symphony-profile-manager-api-openapi.yml
        type: OpenAPI
    description: Profile Manager is a microservice to manage users profile and groups.
name: Symphony
tags:
  - Financial
  - Messaging
type: Contract
access: 3rd-Party
created: 2024/04/14
modified: '2025-01-03'
position: Consuming
description: >-
  Symphony is a communication platform designed specifically for professional
  teams. It provides an innovative solution for secure collaboration, allowing
  users to communicate in real-time through messaging, voice, and video calls.
  Symphony also offers integrations with various tools and applications commonly
  used in the workplace, making it easy for teams to streamline their workflow
  and increase productivity. With robust security features and compliance
  standards, Symphony ensures that sensitive information is protected and
  communication remains confidential. Overall, Symphony is a powerful tool that
  empowers teams to work together efficiently and effectively, no matter where
  they are located.
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
specificationVersion: '0.18'
---