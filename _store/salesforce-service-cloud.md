---
aid: salesforce-service-cloud
url: https://raw.githubusercontent.com/api-evangelist/salesforce-service-cloud/refs/heads/main/apis.yml
apis:
- name: Salesforce Service Cloud REST API
  description: RESTful API for managing customer service operations including cases, contacts, accounts, and knowledge articles.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  tags:
  - Accounts
  - Cases
  - Contacts
  - REST
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
  - type: OpenAPI
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_list.htm
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_list.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart.htm
  - type: OpenAPI
    url: openapi/salesforce-service-cloud-rest-openapi.yml
- name: Salesforce Service Cloud SOAP API
  description: SOAP-based API for enterprise integration and complex service cloud operations.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/
  baseURL: https://yourInstance.salesforce.com/services/Soap/c/59.0/
  tags:
  - Enterprise
  - Integration
  - SOAP
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/
  - type: WSDL
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_quickstart_intro.htm
- name: Service Cloud Streaming API
  description: Real-time streaming API for push notifications and event-driven architecture.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/
  baseURL: https://yourInstance.salesforce.com/cometd/59.0/
  tags:
  - Events
  - Push Notifications
  - Real-Time
  - Streaming
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/
  - type: Protocol
    url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/using_streaming_api.htm
  - type: AsyncAPI
    url: asyncapi/salesforce-streaming-api-asyncapi.yml
- name: Live Agent REST API
  description: API for managing live chat sessions and agent interactions.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.live_agent_rest.meta/live_agent_rest/
  baseURL: https://yourInstance.salesforce.com/chat/rest/
  tags:
  - Agent
  - Live Chat
  - Real-Time Support
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.live_agent_rest.meta/live_agent_rest/
  - type: API Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.live_agent_rest.meta/live_agent_rest/live_agent_rest_API_requests.htm
  - type: OpenAPI
    url: openapi/salesforce-live-agent-openapi.yml
- name: Knowledge API
  description: API for managing knowledge base articles and content.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/knowledge/
  tags:
  - Articles
  - Content Management
  - Knowledge Base
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/
  - type: API Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/knowledge_development.htm
- name: Einstein Bot API
  description: API for building and managing AI-powered chatbots for customer service.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.bot_cookbook.meta/bot_cookbook/
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/einstein/bots/
  tags:
  - AI
  - Automation
  - Chatbot
  - Einstein
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.bot_cookbook.meta/bot_cookbook/
  - type: Developer Guide
    url: https://developer.salesforce.com/docs/atlas.en-us.bot_cookbook.meta/bot_cookbook/bot_cookbook_before.htm
- name: Omni-Channel API
  description: API for managing omni-channel routing, agent presence, and work distribution across multiple service channels including chat, messaging, email, and voice.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.omni_channel_dev.meta/omni_channel_dev/omnichannel_developer_guide_intro.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  tags:
  - Agent Presence
  - Omni-Channel
  - Routing
  - Work Distribution
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.omni_channel_dev.meta/omni_channel_dev/omnichannel_developer_guide_intro.htm
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.omni_channel_dev.meta/omni_channel_dev/service_presence_soap_api_intro.htm
- name: Service Cloud Voice Telephony Integration API
  description: REST API for integrating telephony systems with Service Cloud Voice, enabling programmatic management of voice calls, call recording, and real-time transcription within the service console.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_intro.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  tags:
  - Call Center
  - Real-Time
  - Telephony
  - Voice
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_intro.htm
  - type: Reference
    url: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_rest_overview.htm
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_rest_authorization.htm
- name: Service Cloud Voice for Partner Telephony API
  description: Developer API for connecting third-party telephony systems to Service Cloud Voice, including the Connector API for passing information between contact center platforms and Salesforce.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
  humanURL: https://developer.salesforce.com/docs/atlas.en-us.voice_pt_developer_guide.meta/voice_pt_developer_guide/voice_pt_dev_guide.htm
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  tags:
  - Connector
  - Integration
  - Partner Telephony
  - Voice
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.voice_pt_developer_guide.meta/voice_pt_developer_guide/voice_pt_dev_guide.htm
  - type: Getting Started
    url: https://developer.salesforce.com/docs/atlas.en-us.voice_pt_developer_guide.meta/voice_pt_developer_guide/voice_pt_connector_api_get_started.htm
- name: Agentforce Service Agent API
  description: REST API for building and deploying AI-powered service agents using Agentforce, enabling headless agent interactions, session management, and seamless escalation from AI agents to human service representatives.
  image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
  humanURL: https://developer.salesforce.com/docs/einstein/genai/guide/get-started-agents.html
  baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  tags:
  - Agentforce
  - AI
  - Automation
  - Service Agent
  properties:
  - type: Documentation
    url: https://developer.salesforce.com/docs/einstein/genai/guide/get-started-agents.html
  - type: Reference
    url: https://developer.salesforce.com/docs/einstein/genai/guide/agent-api.html
  - type: Getting Started
    url: https://developer.salesforce.com/docs/einstein/genai/guide/agent-api-get-started.html
name: Salesforce Service Cloud
tags:
- Case Management
- CRM
- Customer Service
- Help Desk
- Support
- Ticketing
type: Contract
image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Salesforce Service Cloud is a customer service and support platform that helps businesses deliver smarter, faster, and more personalized customer service across all channels.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

