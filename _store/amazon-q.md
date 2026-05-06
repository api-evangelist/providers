---
name: Amazon Q
description: Amazon Q is a generative AI-powered assistant that helps with various tasks including answering questions, generating content, and taking actions based on your enterprise data and systems. It is available in multiple product variants including Amazon Q Business for enterprise knowledge, Amazon Q Developer for software development, and Amazon Q in Connect for customer service agents.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/amazon-q/refs/heads/main/apis.yml
created: 2024-01-15T00:00:00.000Z
modified: '2026-04-19'
specificationVersion: '0.18'
tags:
  - Artificial Intelligence
  - Assistant
  - AWS
  - Enterprise
  - Generative AI
apis:
  - name: Amazon Q Business API
    description: API for Amazon Q Business, a fully managed generative AI-powered enterprise chat assistant that you can deploy within your organization. It enables employees to ask questions, get summaries, generate content, and complete tasks using enterprise data from connected data sources with permissions-aware responses.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://aws.amazon.com/q/business/
    baseURL: https://qbusiness.{region}.amazonaws.com
    tags:
      - Business Intelligence
      - Enterprise
      - Generative AI
      - Knowledge Management
      - Q&A
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/
      - type: OpenAPI
        url: https://example.com/openapi/amazon-q-business.json
      - type: Authentication
        url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security-iam.html
      - type: Pricing
        url: https://aws.amazon.com/q/business/pricing/
      - type: APIReference
        url: https://docs.aws.amazon.com/amazonq/latest/api-reference/Welcome.html
      - type: GettingStarted
        url: https://aws.amazon.com/q/business/getting-started/
      - type: Features
        url: https://aws.amazon.com/q/business/features/
      - type: Documentation
        url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html
      - type: CLI
        url: https://docs.aws.amazon.com/cli/latest/reference/qbusiness/
      - type: SDK
        url: https://aws.amazon.com/tools/
      - type: Quotas
        url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quotas-regions.html
      - type: ChangeLog
        url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-history.html
  - name: Amazon Q Business QApps API
    description: API for Amazon Q Apps, a feature within Amazon Q Business that allows web experience users to create lightweight, purpose-built AI apps to fulfill specific tasks using their enterprise data. It supports creating, managing, sharing, and running custom Q Apps through a library system.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Operations_QApps.html
    baseURL: https://qbusiness.{region}.amazonaws.com
    tags:
      - Applications
      - Enterprise
      - Generative AI
      - Low Code
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/
      - type: APIReference
        url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Operations_QApps.html
  - name: Amazon Q Developer API
    description: API for Amazon Q Developer, the most capable generative AI-powered assistant for software development. It provides inline code suggestions, chat-based coding assistance, security scanning, code transformations, and agentic feature development across IDEs, the CLI, and the AWS Management Console.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://aws.amazon.com/q/developer/
    baseURL: https://q.{region}.amazonaws.com
    tags:
      - AI Assistant
      - Code Generation
      - Developer Tools
      - IDE Integration
      - Security Scanning
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/
      - type: OpenAPI
        url: https://example.com/openapi/amazon-q-developer.json
      - type: Authentication
        url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam.html
      - type: Pricing
        url: https://aws.amazon.com/q/developer/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/q/developer/getting-started/
      - type: Features
        url: https://aws.amazon.com/q/developer/features/
      - type: Documentation
        url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html
      - type: Quotas
        url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/quotas.html
      - type: SDK
        url: https://aws.amazon.com/tools/
      - type: ChangeLog
        url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/doc-history.html
      - type: GitHubRepository
        url: https://github.com/aws/amazon-q-developer-cli
  - name: Amazon Q Connect API
    description: API for Amazon Q in Connect, a generative AI-powered customer service assistant integrated with Amazon Connect. It automatically detects customer intent during calls and chats using conversational analytics and natural language understanding, then provides contact center agents with real-time generative responses, suggested actions, and links to relevant documents.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://aws.amazon.com/connect/q/
    baseURL: https://wisdom.{region}.amazonaws.com
    tags:
      - Agent Assistance
      - Contact Center
      - Customer Service
      - Generative AI
      - Real-Time
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/connect/latest/adminguide/amazon-q-connect.html
      - type: APIReference
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Q_Connect.html
      - type: CLI
        url: https://docs.aws.amazon.com/cli/latest/reference/qconnect/
      - type: SDK
        url: https://aws.amazon.com/tools/
      - type: GitHubRepository
        url: https://github.com/aws/amazon-q-connectjs
  - name: Amazon Q Developer in Chat Applications API
    description: API for Amazon Q Developer in chat applications, which enables integration of Amazon Q Developer capabilities into messaging platforms. It provides descriptions, request parameters, and response formats for interacting with Amazon Q Developer through chat-based interfaces.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.aws.amazon.com/chatbot/latest/APIReference/Welcome.html
    baseURL: https://chatbot.{region}.amazonaws.com
    tags:
      - Chat
      - Developer Tools
      - Integration
      - Messaging
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/chatbot/latest/APIReference/Welcome.html
      - type: APIReference
        url: https://docs.aws.amazon.com/chatbot/latest/APIReference/Welcome.html
common:
  - type: Portal
    url: https://aws.amazon.com/q/
  - type: GettingStarted
    url: https://aws.amazon.com/q/getting-started/
  - type: Documentation
    url: https://docs.aws.amazon.com/amazonq/
  - type: Blog
    url: https://aws.amazon.com/blogs/aws/tag/amazon-q/
  - type: FAQ
    url: https://aws.amazon.com/q/faqs/
  - type: Support
    url: https://aws.amazon.com/contact-us/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Pricing
    url: https://aws.amazon.com/q/pricing/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: SDK
    url: https://aws.amazon.com/tools/
  - type: Portal
    url: https://console.aws.amazon.com/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Community
    url: https://repost.aws/tags/TALmcXzmfeRaKOzrBowJ9cJQ/amazon-q
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: JSON-LD
    url: json-ld/amazon-q-openapi-application-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-q-openapi-conversation-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-q-openapi-data-source-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-q-openapi-index-context.jsonld
  - type: JSON-LD
    url: json-ld/amazon-q-openapi-message-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-q-openapi-application-schema.json
  - type: JSONSchema
    url: json-schema/amazon-q-openapi-conversation-schema.json
  - type: JSONSchema
    url: json-schema/amazon-q-openapi-data-source-schema.json
  - type: JSONSchema
    url: json-schema/amazon-q-openapi-index-schema.json
  - type: JSONSchema
    url: json-schema/amazon-q-openapi-message-schema.json
  - type: JSONStructure
    url: json-structure/amazon-q-openapi-application-structure.json
  - type: JSONStructure
    url: json-structure/amazon-q-openapi-conversation-structure.json
  - type: JSONStructure
    url: json-structure/amazon-q-openapi-data-source-structure.json
  - type: JSONStructure
    url: json-structure/amazon-q-openapi-index-structure.json
  - type: JSONStructure
    url: json-structure/amazon-q-openapi-message-structure.json
  - type: Example
    url: examples/amazon-q-openapi-application-example.json
  - type: Example
    url: examples/amazon-q-openapi-conversation-example.json
  - type: Example
    url: examples/amazon-q-openapi-data-source-example.json
  - type: Example
    url: examples/amazon-q-openapi-index-example.json
  - type: Example
    url: examples/amazon-q-openapi-message-example.json
  - type: NaftikoCapability
    url: capabilities/amazon-q.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-q.yaml
  - type: SpectralRules
    url: rules/amazon-q-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-q-vocabulary.yaml
  - type: OpenAPI
    url: openapi/amazon-q-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    x-twitter: apievangelist
---
