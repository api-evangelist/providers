---
aid: amazon-connect
url: https://raw.githubusercontent.com/api-evangelist/amazon-connect/refs/heads/main/apis.yml
name: Amazon Connect
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
specificationVersion: '0.19'
description: Amazon Connect is a cloud-based contact center service that makes it easy to set up and manage a customer contact center and provide reliable customer engagement at any scale, with omnichannel support for voice, chat, email, and task management. It includes AI-powered features for agent assistance, customer profiles, conversation analytics, and outbound campaign management.
created: '2024-01-15'
modified: '2026-04-19'
tags:
  - AWS
  - Chat
  - Contact Center
  - Customer Service
  - Voice
  - AI
  - Omnichannel
apis:
  - name: Amazon Connect Service API
    description: The Amazon Connect Service API provides programmatic access to manage contact center instances, users, routing profiles, contact flows, queues, hours of operation, security profiles, and real-time and historical metrics for customer engagement operations.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Service.html
    baseURL: https://connect.amazonaws.com
    tags:
      - Contact Center
      - AWS
      - Voice
      - Chat
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Service.html
      - type: OpenAPI
        url: openapi/amazon-connect-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/connect/2017-08-08/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-connect-instance-schema.json
      - type: JSONLD
        url: json-ld/amazon-connect-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/connect/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/connect/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/connect/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/connect/latest/APIReference/
      - type: CLI
        url: https://docs.aws.amazon.com/cli/latest/reference/connect/
      - type: Security
        url: https://docs.aws.amazon.com/connect/latest/adminguide/security.html
      - type: JSONSchema
        url: json-schema/user-schema.json
      - type: JSONSchema
        url: json-schema/queue-schema.json
      - type: JSONSchema
        url: json-schema/contact-schema.json
      - type: JSONSchema
        url: json-schema/routing-profile-schema.json
      - type: JSONSchema
        url: json-schema/contact-flow-schema.json
      - type: JSONSchema
        url: json-schema/instance-schema.json
  - name: Amazon Connect Streams SDK
    description: Amazon Connect Streams is a browser-based integration API and JavaScript SDK that enables embedding and controlling the Amazon Connect Contact Control Panel (CCP) within your web application or CRM system.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://github.com/amazon-connect/amazon-connect-streams
    baseURL: https://github.com/amazon-connect/amazon-connect-streams
    tags:
      - SDK
      - JavaScript
      - Browser
      - Contact Center
    properties:
      - type: SDK
        url: https://github.com/amazon-connect/amazon-connect-streams
        title: JavaScript Streams SDK
      - type: SDK
        url: https://www.npmjs.com/package/amazon-connect-streams
        title: npm Package
      - type: CodeExamples
        url: https://github.com/amazon-connect/amazon-connect-snippets
        title: Code Snippets
      - type: CodeExamples
        url: https://github.com/amazon-connect/amazon-connect-chat-ui-examples
        title: Chat UI Examples
      - type: SDK
        url: https://github.com/amazon-connect/amazon-connect-chatjs
        title: JavaScript Chat SDK
      - type: SDK
        url: https://github.com/amazon-connect/amazon-connect-chat-ios
        title: iOS Chat SDK
      - type: SDK
        url: https://github.com/amazon-connect/amazon-connect-chat-android
        title: Android Chat SDK
      - type: SDK
        url: https://github.com/amazon-connect/AmazonConnectSDK
        title: Amazon Connect SDK
      - type: Tutorials
        url: https://github.com/amazon-connect/amazon-connect-workshops
        title: Amazon Connect Workshops
  - name: Amazon AppIntegrations API
    description: The Amazon AppIntegrations service enables you to configure and reuse connections to external applications, powering third-party integrations in the Amazon Connect agent workspace.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_AppIntegrations_Service.html
    baseURL: https://app-integrations.amazonaws.com
    tags:
      - Integrations
      - AWS
      - Contact Center
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_AppIntegrations_Service.html
      - type: APIReference
        url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/
  - name: Amazon Connect Contact Lens API
    description: Amazon Connect Contact Lens enables you to analyze conversations between customers and agents using speech transcription, natural language processing, and intelligent search capabilities. It performs sentiment analysis, detects issues, and enables automatic categorization of contacts with both real-time and post-call analytics.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Contact_Lens.html
    baseURL: https://contact-lens.amazonaws.com
    tags:
      - Analytics
      - AI
      - Contact Center
      - NLP
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Contact_Lens.html
      - type: APIReference
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Contact_Lens.html
  - name: Amazon Connect Outbound Campaigns API
    description: With the outbound campaigns feature of Amazon Connect, you can create high-volume outbound campaigns for appointment reminders, telemarketing, subscription renewals, or debt collection.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Outbound_Campaigns.html
    baseURL: https://connect-campaigns.amazonaws.com
    tags:
      - Outbound
      - Campaigns
      - Contact Center
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Outbound_Campaigns.html
      - type: APIReference
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Outbound_Campaigns.html
  - name: Amazon Connect Outbound Campaigns V2 API
    description: The outbound campaigns V2 API provides an updated interface for creating high-volume outbound campaigns including multi-channel support and availability in all Amazon Connect regions.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Outbound_Campaigns_V2.html
    baseURL: https://connect-campaigns.amazonaws.com
    tags:
      - Outbound
      - Campaigns
      - Contact Center
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Outbound_Campaigns_V2.html
      - type: APIReference
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Outbound_Campaigns_V2.html
  - name: Amazon Connect Cases API
    description: With Amazon Connect Cases, agents can track and manage customer issues that require multiple interactions, follow-up tasks, and teams in your contact center. A case represents a customer issue including the steps and interactions taken to resolve it.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Cases.html
    baseURL: https://cases.amazonaws.com
    tags:
      - Cases
      - Case Management
      - Contact Center
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Cases.html
      - type: APIReference
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Cases.html
  - name: Amazon Connect Participant Service API
    description: The Amazon Connect Participant Service enables managing chat participants including agents, customers, and managers. Use it to send messages and events, manage connection state, share attachments, and retrieve chat transcripts within a chat contact.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Participant_Service.html
    baseURL: https://participant.connect.amazonaws.com
    tags:
      - Chat
      - Participants
      - Contact Center
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Participant_Service.html
      - type: APIReference
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Participant_Service.html
  - name: Amazon Connect Customer Profiles API
    description: Amazon Connect Customer Profiles provides a unified customer profile for your contact center with pre-built connectors powered by AppFlow that make it easy to combine customer information from third-party applications such as Salesforce (CRM), ServiceNow (ITSM), and ERP systems with contact history from Amazon Connect.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Customer_Profiles.html
    baseURL: https://profile.profile.amazonaws.com
    tags:
      - Customer Profiles
      - CRM
      - Contact Center
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Customer_Profiles.html
      - type: APIReference
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Connect_Customer_Profiles.html
  - name: Amazon Q Connect API
    description: Amazon Q in Connect is a generative AI customer service assistant built on Amazon Bedrock. It provides real-time recommendations to help contact center agents resolve customer issues quickly and accurately by detecting customer intent and providing immediate generative responses, suggested actions, and links to relevant documents.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Q_Connect.html
    baseURL: https://wisdom.amazonaws.com
    tags:
      - AI
      - Generative AI
      - Agent Assist
      - Contact Center
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Q_Connect.html
      - type: APIReference
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Q_Connect.html
  - name: Amazon Voice ID API
    description: Amazon Connect Voice ID provides real-time caller authentication and fraud risk detection to make voice interactions in contact centers more secure and efficient. Note - Voice ID end of support is scheduled for May 20, 2026.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Voice_ID.html
    baseURL: https://voiceid.amazonaws.com
    tags:
      - Voice
      - Authentication
      - Fraud Detection
      - Contact Center
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Voice_ID.html
      - type: APIReference
        url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Operations_Amazon_Voice_ID.html
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/connect/
  - type: Documentation
    url: https://docs.aws.amazon.com/connect/latest/adminguide/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/support/
  - type: Blog
    url: https://aws.amazon.com/blogs/contact-center/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: GitHubOrganization
    url: https://github.com/amazon-connect
  - type: Console
    url: https://console.aws.amazon.com/connect/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-connect
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Pricing
    url: https://aws.amazon.com/connect/pricing/
  - type: Features
    data:
      - name: Omnichannel Routing
        description: Unified routing across voice, chat, email, and tasks through a single platform with skills-based routing and priority queuing.
      - name: AI-Powered Agent Assist
        description: Amazon Q in Connect provides real-time AI-generated recommendations and answers to help agents resolve customer issues faster.
      - name: Contact Flows
        description: Drag-and-drop contact flow designer for building IVR, chatbot, and agent guidance workflows without extensive coding.
      - name: Conversational Analytics
        description: Contact Lens provides speech transcription, sentiment analysis, and NLP-powered insights across all customer interactions.
      - name: Customer Profiles
        description: Unified customer profile combining CRM, ITSM, ERP, and contact history data for context-aware agent interactions.
      - name: Outbound Campaigns
        description: High-volume multi-channel outbound campaigns with predictive dialer, answering machine detection, and multiple dialing modes.
      - name: Cases Management
        description: Structured case tracking for customer issues requiring multiple interactions, follow-up tasks, and cross-team coordination.
      - name: Voice and Video Calling
        description: In-app, web, and video calling with screen share capabilities using 16kHz high-quality audio with packet loss resistance.
      - name: Chat and Messaging
        description: Real-time and asynchronous messaging including SMS, WhatsApp Business, and Apple Messages for Business integration.
      - name: Real-Time and Historical Metrics
        description: Comprehensive dashboards and reporting for contact center performance optimization and workforce planning.
  - type: UseCases
    data:
      - name: Customer Support Contact Center
        description: Deploy an omnichannel contact center handling voice, chat, email, and messaging with intelligent routing to the right agents.
      - name: AI-Powered Self-Service
        description: Build conversational AI flows that handle common customer requests in 30+ languages without agent involvement.
      - name: Agent Productivity Improvement
        description: Reduce average handle time with real-time AI guidance, unified agent workspace, and automated post-contact work.
      - name: Outbound Customer Engagement
        description: Run appointment reminders, subscription renewals, payment notifications, and telemarketing campaigns at scale.
      - name: Fraud Prevention
        description: Use Voice ID for real-time caller authentication and fraud risk detection in voice contact center interactions.
      - name: Compliance and Quality Monitoring
        description: Analyze 100% of customer interactions with Contact Lens for regulatory compliance and quality assurance.
  - type: SpectralRules
    url: rules/amazon-connect-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-connect-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/contact-center-operations.yaml
  - type: NaftikoCapability
    url: capabilities/shared/connect-service.yaml
  - type: Integrations
    data:
      - name: Salesforce CRM
        description: Pre-built AppFlow connector to sync Salesforce customer data into Amazon Connect Customer Profiles.
      - name: ServiceNow
        description: ITSM integration via AppFlow to bring ServiceNow customer and case data into the Amazon Connect agent workspace.
      - name: AWS Lambda
        description: Native integration with AWS Lambda for custom automation within contact flows and agent events.
      - name: Amazon Lex
        description: Built-in integration with Amazon Lex for building conversational AI bots for voice and chat self-service.
      - name: Amazon Bedrock
        description: Foundation for Amazon Q in Connect generative AI features, providing real-time agent recommendations and answers.
      - name: Amazon S3
        description: Storage integration for call recordings, contact transcripts, exported reports, and Contact Lens output data.
      - name: Amazon Kinesis
        description: Real-time streaming of contact trace records (CTRs) and agent events to data lakes and analytics pipelines.
      - name: WhatsApp Business
        description: Native channel integration to handle customer messaging through WhatsApp Business within the Amazon Connect platform.
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
---
