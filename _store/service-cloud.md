---
name: Salesforce Service Cloud APIs
description: A collection of APIs for Salesforce Service Cloud, enabling customer service and support operations.
image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
created: '2024-01-15'
modified: '2024-01-15'
specificationVersion: '0.18'
url: https://api.salesforce.com/apis.json
apis:
  - name: Service Cloud REST API
    description: Core REST API for Service Cloud operations including cases, knowledge articles, and customer interactions.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/rest-api-icon.png
    humanUrl: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
    baseUrl: https://yourInstance.salesforce.com/services/data/v59.0
    tags:
      - Cases
      - CRM
      - Customers
      - REST
      - Support
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.htm
      - type: OpenAPI
        url: https://api.salesforce.com/service-cloud/openapi.json
      - type: Authentication
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_authentication.htm
      - type: Swagger
        url: https://api.salesforce.com/service-cloud/swagger.json
  - name: Service Cloud Case Management API
    description: Specialized API for managing support cases, case routing, and escalations.
    humanUrl: https://developer.salesforce.com/docs/service/case-management
    baseUrl: https://yourInstance.salesforce.com/services/data/v59.0/sobjects/Case
    tags:
      - Cases
      - Escalation
      - Routing
      - Tickets
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_case.htm
      - type: Examples
        url: https://developer.salesforce.com/docs/service/case-examples
  - name: Service Cloud Knowledge API
    description: API for managing knowledge articles, categories, and knowledge base operations.
    humanUrl: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/
    baseUrl: https://yourInstance.salesforce.com/services/data/v59.0/knowledgeManagement
    tags:
      - Articles
      - Documentation
      - Knowledge
      - Self-Service
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/knowledge_development.htm
      - type: API Reference
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_knowledge.htm
  - name: Service Cloud Omni-Channel API
    description: API for managing omni-channel routing, presence, and work assignments.
    humanUrl: https://developer.salesforce.com/docs/service/omnichannel
    baseUrl: https://yourInstance.salesforce.com/services/data/v59.0/omnichannel
    tags:
      - Omnichannel
      - Presence
      - Routing
      - Workforce
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_omnichannel.htm
      - type: Guide
        url: https://help.salesforce.com/s/articleView?id=sf.omnichannel_intro.htm
  - name: Service Cloud Live Agent API
    description: API for real-time chat and messaging with customers.
    humanUrl: https://developer.salesforce.com/docs/atlas.en-us.live_agent_rest.meta/live_agent_rest/
    baseUrl: https://yourInstance.salesforce.com/chat/rest
    tags:
      - Chat
      - Live-Agent
      - Messaging
      - Real-Time
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.live_agent_rest.meta/live_agent_rest/live_agent_rest_API_intro.htm
      - type: API Reference
        url: https://developer.salesforce.com/docs/atlas.en-us.live_agent_rest.meta/live_agent_rest/live_agent_rest_API_calls.htm
  - name: Service Cloud Einstein Bots API
    description: API for building and managing AI-powered chatbots for customer service.
    humanUrl: https://developer.salesforce.com/docs/service/einstein-bots
    baseUrl: https://yourInstance.salesforce.com/services/data/v59.0/einstein/bots
    tags:
      - AI
      - Automation
      - Bots
      - Chatbots
      - Einstein
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.bot_cookbook.meta/bot_cookbook/
      - type: API Reference
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_bot.htm
  - name: Service Cloud Streaming API
    description: API for receiving near real-time notifications of changes to Service Cloud data.
    humanUrl: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/
    baseUrl: https://yourInstance.salesforce.com/cometd/59.0
    tags:
      - Events
      - Push-Notifications
      - Real-Time
      - Streaming
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/intro_stream.htm
      - type: Guide
        url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/quick_start.htm
  - name: Service Cloud CTI API
    description: Computer Telephony Integration API for connecting phone systems with Service Cloud.
    humanUrl: https://developer.salesforce.com/docs/atlas.en-us.api_cti.meta/api_cti/
    baseUrl: https://yourInstance.salesforce.com/support/api/59.0/cti
    tags:
      - Call-Center
      - CTI
      - Phone
      - Telephony
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_cti.meta/api_cti/sforce_api_cti_intro.htm
      - type: Integration Guide
        url: https://developer.salesforce.com/docs/atlas.en-us.api_cti.meta/api_cti/sforce_api_cti_integration.htm
maintainers:
  - name: Salesforce
    email: developer@salesforce.com
    url: https://developer.salesforce.com
tags:
  - Cloud
  - CRM
  - Customer-Service
  - Enterprise
  - Salesforce
  - Support
include: []
common:
  - type: Portal
    url: https://developer.salesforce.com/
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart.htm
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_authentication.htm
  - type: Rate Limits
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm
  - type: SDKs
    url: https://developer.salesforce.com/tools/sdks
  - type: Status Page
    url: https://status.salesforce.com/
  - type: Support
    url: https://help.salesforce.com/
  - type: Terms of Service
    url: https://www.salesforce.com/company/legal/agreements/
  - type: Privacy Policy
    url: https://www.salesforce.com/company/privacy/
---
