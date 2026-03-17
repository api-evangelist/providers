---
name: Amazon Q
description: >-
  Amazon Q is a generative AI-powered assistant that helps with various tasks
  including answering questions, generating content, and taking actions based on
  your enterprise data and systems. It is available in multiple product variants
  including Amazon Q Business for enterprise knowledge, Amazon Q Developer for
  software development, and Amazon Q in Connect for customer service agents.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://example.com/apis/amazon-q/apis.yml
created: 2024-01-15 00:00:00+00:00
modified: '2026-03-16'
specificationVersion: '0.18'
tags:
- Artificial Intelligence
- Generative AI
- Assistant
- Enterprise
- AWS
apis:
- name: Amazon Q Business API
  description: >-
    API for Amazon Q Business, a fully managed generative AI-powered enterprise
    chat assistant that you can deploy within your organization. It enables
    employees to ask questions, get summaries, generate content, and complete
    tasks using enterprise data from connected data sources with
    permissions-aware responses.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://aws.amazon.com/q/business/
  baseURL: https://qbusiness.{region}.amazonaws.com
  tags:
  - Enterprise
  - Business Intelligence
  - Q&A
  - Knowledge Management
  - Generative AI
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/
  - type: OpenAPI
    url: https://example.com/openapi/amazon-q-business.json
  - type: Authentication
    url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security-iam.html
  - type: Pricing
    url: https://aws.amazon.com/q/business/pricing/
  - type: API Reference
    url: https://docs.aws.amazon.com/amazonq/latest/api-reference/Welcome.html
  - type: Getting Started
    url: https://aws.amazon.com/q/business/getting-started/
  - type: Features
    url: https://aws.amazon.com/q/business/features/
  - type: Developer Guide
    url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/qbusiness/
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: Quotas
    url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/quotas-regions.html
  - type: Change Log
    url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-history.html
- name: Amazon Q Business QApps API
  description: >-
    API for Amazon Q Apps, a feature within Amazon Q Business that allows web
    experience users to create lightweight, purpose-built AI apps to fulfill
    specific tasks using their enterprise data. It supports creating, managing,
    sharing, and running custom Q Apps through a library system.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Operations_QApps.html
  baseURL: https://qbusiness.{region}.amazonaws.com
  tags:
  - Applications
  - Low Code
  - Generative AI
  - Enterprise
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/
  - type: API Reference
    url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Operations_QApps.html
- name: Amazon Q Developer API
  description: >-
    API for Amazon Q Developer, the most capable generative AI-powered assistant
    for software development. It provides inline code suggestions, chat-based
    coding assistance, security scanning, code transformations, and agentic
    feature development across IDEs, the CLI, and the AWS Management Console.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://aws.amazon.com/q/developer/
  baseURL: https://q.{region}.amazonaws.com
  tags:
  - Developer Tools
  - Code Generation
  - IDE Integration
  - Security Scanning
  - AI Assistant
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/
  - type: OpenAPI
    url: https://example.com/openapi/amazon-q-developer.json
  - type: Authentication
    url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam.html
  - type: Pricing
    url: https://aws.amazon.com/q/developer/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/q/developer/getting-started/
  - type: Features
    url: https://aws.amazon.com/q/developer/features/
  - type: Developer Guide
    url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html
  - type: Quotas
    url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/quotas.html
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: Change Log
    url: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/doc-history.html
  - type: GitHubRepository
    url: https://github.com/aws/amazon-q-developer-cli
- name: Amazon Q Connect API
  description: >-
    API for Amazon Q in Connect, a generative AI-powered customer service
    assistant integrated with Amazon Connect. It automatically detects customer
    intent during calls and chats using conversational analytics and natural
    language understanding, then provides contact center agents with real-time
    generative responses, suggested actions, and links to relevant documents.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://aws.amazon.com/connect/q/
  baseURL: https://wisdom.{region}.amazonaws.com
  tags:
  - Customer Service
  - Contact Center
  - Agent Assistance
  - Real-Time
  - Generative AI
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/connect/latest/adminguide/amazon-q-connect.html
  - type: API Reference
    url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Q_Connect.html
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/qconnect/
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: GitHubRepository
    url: https://github.com/aws/amazon-q-connectjs
- name: Amazon Q Developer in Chat Applications API
  description: >-
    API for Amazon Q Developer in chat applications, which enables integration
    of Amazon Q Developer capabilities into messaging platforms. It provides
    descriptions, request parameters, and response formats for interacting with
    Amazon Q Developer through chat-based interfaces.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://docs.aws.amazon.com/chatbot/latest/APIReference/Welcome.html
  baseURL: https://chatbot.{region}.amazonaws.com
  tags:
  - Chat
  - Messaging
  - Developer Tools
  - Integration
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/chatbot/latest/APIReference/Welcome.html
  - type: API Reference
    url: https://docs.aws.amazon.com/chatbot/latest/APIReference/Welcome.html
common:
- type: Portal
  url: https://aws.amazon.com/q/
- type: Getting Started
  url: https://aws.amazon.com/q/getting-started/
- type: Documentation
  url: https://docs.aws.amazon.com/amazonq/
- type: Blog
  url: https://aws.amazon.com/blogs/aws/tag/amazon-q/
- type: FAQ
  url: https://aws.amazon.com/q/faqs/
- type: Support
  url: https://aws.amazon.com/contact-us/
- type: Terms of Service
  url: https://aws.amazon.com/service-terms/
- type: Privacy Policy
  url: https://aws.amazon.com/privacy/
- type: Pricing
  url: https://aws.amazon.com/q/pricing/
- type: Status
  url: https://health.aws.amazon.com/health/status
- type: SDKs
  url: https://aws.amazon.com/tools/
- type: Console
  url: https://console.aws.amazon.com/
- type: Sign Up
  url: https://portal.aws.amazon.com/billing/signup
- type: Community
  url: https://repost.aws/tags/TALmcXzmfeRaKOzrBowJ9cJQ/amazon-q
- type: GitHub Organization
  url: https://github.com/aws
maintainers:
- FN: Kin Lane
  email: kin@apievangelist.com
  x-twitter: apievangelist
---