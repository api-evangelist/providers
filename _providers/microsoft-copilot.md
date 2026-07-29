---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Microsoft Copilot Agentic Access
  operation_count: 6
  slug: microsoft-copilot-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 7
apis:
- description: API for building custom connectors that bring external data into Microsoft Graph to enhance Microsoft 365 Copilot experiences including search and retrieval augmented generation.
  name: Microsoft 365 Copilot Connectors API
  slug: microsoft-365-copilot-connectors-api
- description: APIs for building, publishing, and integrating custom agents and copilots using Microsoft Copilot Studio, including Direct Line API for connecting web and custom applications.
  name: Microsoft Copilot Studio API
  slug: microsoft-copilot-studio-api
- description: Subscribe to change notifications for Copilot interactions across Microsoft 365.
  name: Microsoft Copilot Change Notifications API
  slug: microsoft-copilot-change-notifications-api
- description: Programmatically start and continue conversations with Microsoft 365 Copilot using enterprise search and web search grounding. Preview API.
  name: Microsoft Copilot Chat API
  slug: microsoft-copilot-chat-api
- description: Export and archive user interactions with Copilot across Microsoft 365 applications for compliance and auditing.
  name: Microsoft Copilot Interaction Export API
  slug: microsoft-copilot-interaction-export-api
- description: Retrieve relevant text chunks from SharePoint, OneDrive, and Copilot connectors content for Retrieval Augmented Generation (RAG) scenarios.
  name: Microsoft Copilot Retrieval API
  slug: microsoft-copilot-retrieval-api
- description: Perform hybrid search (semantic and lexical) across OneDrive for work or school content using natural language queries. Preview API.
  name: Microsoft Copilot Search API
  slug: microsoft-copilot-search-api
artifact_total: 151
collections:
- collection_type: postman
  name: Microsoft Copilot Microsoft 365 Copilot APIs Change Notifications API
  slug: postman-microsoft-copilot-change-notifications-api
- collection_type: postman
  name: Microsoft Copilot Microsoft 365 Copilot APIs Change Notifications Chat API
  slug: postman-microsoft-copilot-chat-api
- collection_type: postman
  name: Microsoft Copilot Microsoft 365 Copilot APIs Change Notifications Interaction Export API
  slug: postman-microsoft-copilot-interaction-export-api
- collection_type: postman
  name: Microsoft Copilot Microsoft 365 Copilot APIs Change Notifications Retrieval API
  slug: postman-microsoft-copilot-retrieval-api
- collection_type: postman
  name: Microsoft Copilot Microsoft 365 Copilot APIs Change Notifications Search API
  slug: postman-microsoft-copilot-search-api
- collection_type: open
  name: Microsoft Copilot Microsoft 365 Copilot APIs
  slug: open-microsoft-copilot
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-copilot/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-copilot-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-copilot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-copilot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-copilot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-copilot-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoftcopilot
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/copilot/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-copilot/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/copilot
- group: company
  title: ''
  type: Blog
  url: https://blogs.microsoft.com/blog/tag/copilot/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.microsoft.com
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/microsoft-365/copilot
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/sdks/api-libraries
- group: build
  title: ''
  type: CodeExamples
  url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/samples
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/whats-new
- group: auth
  title: ''
  type: Security
  url: https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/CopilotStudioSamples
created: '2024-01-15'
description: Microsoft Copilot is an AI-powered assistant that helps users with productivity tasks, content generation, and information retrieval across Microsoft 365 applications and services.
examples:
- key_count: 5
  name: Microsoft Copilot Ai Interaction Attachment Example
  slug: microsoft-copilot-ai-interaction-attachment-example
- key_count: 3
  name: Microsoft Copilot Ai Interaction Collection Response Example
  slug: microsoft-copilot-ai-interaction-collection-response-example
- key_count: 3
  name: Microsoft Copilot Ai Interaction Context Example
  slug: microsoft-copilot-ai-interaction-context-example
- key_count: 13
  name: Microsoft Copilot Ai Interaction Example
  slug: microsoft-copilot-ai-interaction-example
- key_count: 3
  name: Microsoft Copilot Ai Interaction Link Example
  slug: microsoft-copilot-ai-interaction-link-example
- key_count: 3
  name: Microsoft Copilot Ai Interaction Mention Example
  slug: microsoft-copilot-ai-interaction-mention-example
- key_count: 3
  name: Microsoft Copilot Chat Conversation Request Example
  slug: microsoft-copilot-chat-conversation-request-example
- key_count: 1
  name: Microsoft Copilot Chat Conversation Response Example
  slug: microsoft-copilot-chat-conversation-response-example
- key_count: 4
  name: Microsoft Copilot Chat Message Example
  slug: microsoft-copilot-chat-message-example
- key_count: 2
  name: Microsoft Copilot Chat Message Request Example
  slug: microsoft-copilot-chat-message-request-example
- key_count: 0
  name: Microsoft Copilot Chat Message Response Example
  slug: microsoft-copilot-chat-message-response-example
- key_count: 1
  name: Microsoft Copilot Copilot Search Data Sources Configuration Example
  slug: microsoft-copilot-copilot-search-data-sources-configuration-example
- key_count: 6
  name: Microsoft Copilot Copilotchangenotificationscreatesubscription Example
  slug: microsoft-copilot-copilotchangenotificationscreatesubscription-example
- key_count: 6
  name: Microsoft Copilot Copilotchatcontinueconversation Example
  slug: microsoft-copilot-copilotchatcontinueconversation-example
- key_count: 6
  name: Microsoft Copilot Copilotchatstartconversation Example
  slug: microsoft-copilot-copilotchatstartconversation-example
- key_count: 6
  name: Microsoft Copilot Copilotinteractionhistorygetallenterpriseinteractions Example
  slug: microsoft-copilot-copilotinteractionhistorygetallenterpriseinteractions-example
- key_count: 6
  name: Microsoft Copilot Copilotretrieval Example
  slug: microsoft-copilot-copilotretrieval-example
- key_count: 6
  name: Microsoft Copilot Copilotsearch Example
  slug: microsoft-copilot-copilotsearch-example
- key_count: 1
  name: Microsoft Copilot Data Source Configuration Example
  slug: microsoft-copilot-data-source-configuration-example
- key_count: 3
  name: Microsoft Copilot Identity Set Example
  slug: microsoft-copilot-identity-set-example
- key_count: 2
  name: Microsoft Copilot Item Body Example
  slug: microsoft-copilot-item-body-example
- key_count: 1
  name: Microsoft Copilot O Data Error Example
  slug: microsoft-copilot-o-data-error-example
- key_count: 2
  name: Microsoft Copilot Retrieval Extract Example
  slug: microsoft-copilot-retrieval-extract-example
- key_count: 4
  name: Microsoft Copilot Retrieval Hit Example
  slug: microsoft-copilot-retrieval-hit-example
- key_count: 5
  name: Microsoft Copilot Retrieval Request Example
  slug: microsoft-copilot-retrieval-request-example
- key_count: 1
  name: Microsoft Copilot Retrieval Response Example
  slug: microsoft-copilot-retrieval-response-example
- key_count: 4
  name: Microsoft Copilot Search Hit Example
  slug: microsoft-copilot-search-hit-example
- key_count: 2
  name: Microsoft Copilot Search Request Example
  slug: microsoft-copilot-search-request-example
- key_count: 3
  name: Microsoft Copilot Search Response Example
  slug: microsoft-copilot-search-response-example
- key_count: 5
  name: Microsoft Copilot Sensitivity Label Example
  slug: microsoft-copilot-sensitivity-label-example
- key_count: 6
  name: Microsoft Copilot Subscription Example
  slug: microsoft-copilot-subscription-example
- key_count: 5
  name: Microsoft Copilot Subscription Request Example
  slug: microsoft-copilot-subscription-request-example
features:
- description: Retrieve relevant enterprise content from Microsoft 365 using AI-powered retrieval augmented generation with permissions and sensitivity label awareness.
  name: Retrieval API
- description: Perform semantic search across Microsoft 365 content including SharePoint, OneDrive, and Exchange with AI-enhanced ranking.
  name: Search API
- description: Programmatically start and continue conversations with Microsoft 365 Copilot grounded in enterprise and web search data.
  name: Chat API
- description: Export and audit Copilot interaction history across the organization for compliance and governance purposes.
  name: Interaction Export
- description: Subscribe to real-time notifications for Copilot interactions and events across Microsoft 365.
  name: Change Notifications
- description: Low-code platform for building custom agents, copilots, and conversational AI experiences.
  name: Copilot Studio
- description: Bring external data into Microsoft Graph to enhance Copilot search and retrieval capabilities.
  name: Connectors
- description: Extend Copilot with custom plugins, agents, and API integrations using declarative or code-first approaches.
  name: Extensibility
finops:
- name: Microsoft Copilot Finops
  service_category: AI / Productivity
  slug: microsoft-copilot-finops
image: https://www.microsoft.com/en-us/microsoft-copilot/assets/images/copilot-icon.png
integrations:
- description: Deep integration with Word, Excel, PowerPoint, Outlook, Teams, and other Microsoft 365 applications.
  name: Microsoft 365
- description: Access organizational data through the Microsoft Graph API for retrieval, search, and chat capabilities.
  name: Microsoft Graph
- description: Enterprise authentication and authorization using Azure AD with OAuth 2.0 and OIDC.
  name: Azure Active Directory
- description: Connect Copilot with Power Automate, Power Apps, and Power BI for end-to-end workflow automation.
  name: Power Platform
json_schemas:
- name: AiInteractionAttachment
  property_count: 5
  slug: microsoft-copilot-ai-interaction-attachment
- name: AiInteractionCollectionResponse
  property_count: 3
  slug: microsoft-copilot-ai-interaction-collection-response
- name: AiInteractionContext
  property_count: 3
  slug: microsoft-copilot-ai-interaction-context
- name: AiInteractionLink
  property_count: 3
  slug: microsoft-copilot-ai-interaction-link
- name: AiInteractionMention
  property_count: 3
  slug: microsoft-copilot-ai-interaction-mention
- name: AiInteraction
  property_count: 13
  slug: microsoft-copilot-ai-interaction
- name: AiInteraction
  property_count: 15
  slug: microsoft-copilot-aiinteraction
- name: AiInteractionAttachment
  property_count: 5
  slug: microsoft-copilot-aiinteractionattachment
- name: AiInteractionCollectionResponse
  property_count: 3
  slug: microsoft-copilot-aiinteractioncollectionresponse
- name: AiInteractionContext
  property_count: 3
  slug: microsoft-copilot-aiinteractioncontext
- name: AiInteractionLink
  property_count: 3
  slug: microsoft-copilot-aiinteractionlink
- name: AiInteractionMention
  property_count: 3
  slug: microsoft-copilot-aiinteractionmention
- name: ChatConversationRequest
  property_count: 3
  slug: microsoft-copilot-chat-conversation-request
- name: ChatConversationResponse
  property_count: 1
  slug: microsoft-copilot-chat-conversation-response
- name: ChatMessageRequest
  property_count: 2
  slug: microsoft-copilot-chat-message-request
- name: ChatMessageResponse
  property_count: 0
  slug: microsoft-copilot-chat-message-response
- name: ChatMessage
  property_count: 4
  slug: microsoft-copilot-chat-message
- name: ChatConversationRequest
  property_count: 3
  slug: microsoft-copilot-chatconversationrequest
- name: ChatConversationResponse
  property_count: 2
  slug: microsoft-copilot-chatconversationresponse
- name: ChatMessage
  property_count: 4
  slug: microsoft-copilot-chatmessage
- name: ChatMessageRequest
  property_count: 2
  slug: microsoft-copilot-chatmessagerequest
- name: ChatMessageResponse
  property_count: 1
  slug: microsoft-copilot-chatmessageresponse
- name: CopilotSearchDataSourcesConfiguration
  property_count: 1
  slug: microsoft-copilot-copilot-search-data-sources-configuration
- name: CopilotSearchDataSourcesConfiguration
  property_count: 1
  slug: microsoft-copilot-copilotsearchdatasourcesconfiguration
- name: DataSourceConfiguration
  property_count: 1
  slug: microsoft-copilot-data-source-configuration
- name: DataSourceConfiguration
  property_count: 1
  slug: microsoft-copilot-datasourceconfiguration
- name: IdentitySet
  property_count: 3
  slug: microsoft-copilot-identity-set
- name: IdentitySet
  property_count: 3
  slug: microsoft-copilot-identityset
- name: Microsoft 365 Copilot Interaction
  property_count: 15
  slug: microsoft-copilot-interaction
- name: ItemBody
  property_count: 2
  slug: microsoft-copilot-item-body
- name: ItemBody
  property_count: 2
  slug: microsoft-copilot-itembody
- name: ODataError
  property_count: 1
  slug: microsoft-copilot-o-data-error
- name: ODataError
  property_count: 1
  slug: microsoft-copilot-odataerror
- name: RetrievalExtract
  property_count: 2
  slug: microsoft-copilot-retrieval-extract
- name: RetrievalHit
  property_count: 4
  slug: microsoft-copilot-retrieval-hit
- name: RetrievalRequest
  property_count: 5
  slug: microsoft-copilot-retrieval-request
- name: RetrievalResponse
  property_count: 1
  slug: microsoft-copilot-retrieval-response
- name: RetrievalExtract
  property_count: 2
  slug: microsoft-copilot-retrievalextract
- name: RetrievalHit
  property_count: 5
  slug: microsoft-copilot-retrievalhit
- name: RetrievalRequest
  property_count: 6
  slug: microsoft-copilot-retrievalrequest
- name: RetrievalResponse
  property_count: 1
  slug: microsoft-copilot-retrievalresponse
- name: SearchHit
  property_count: 4
  slug: microsoft-copilot-search-hit
- name: SearchRequest
  property_count: 2
  slug: microsoft-copilot-search-request
- name: SearchResponse
  property_count: 3
  slug: microsoft-copilot-search-response
- name: SearchHit
  property_count: 4
  slug: microsoft-copilot-searchhit
- name: SearchRequest
  property_count: 3
  slug: microsoft-copilot-searchrequest
- name: SearchResponse
  property_count: 3
  slug: microsoft-copilot-searchresponse
- name: SensitivityLabel
  property_count: 5
  slug: microsoft-copilot-sensitivity-label
- name: SensitivityLabel
  property_count: 5
  slug: microsoft-copilot-sensitivitylabel
- name: SubscriptionRequest
  property_count: 5
  slug: microsoft-copilot-subscription-request
- name: Subscription
  property_count: 6
  slug: microsoft-copilot-subscription
- name: SubscriptionRequest
  property_count: 5
  slug: microsoft-copilot-subscriptionrequest
json_structures:
- name: Microsoft Copilot Ai Interaction Attachment Structure
  property_count: 5
  slug: microsoft-copilot-ai-interaction-attachment-structure
- name: Microsoft Copilot Ai Interaction Collection Response Structure
  property_count: 3
  slug: microsoft-copilot-ai-interaction-collection-response-structure
- name: Microsoft Copilot Ai Interaction Context Structure
  property_count: 3
  slug: microsoft-copilot-ai-interaction-context-structure
- name: Microsoft Copilot Ai Interaction Link Structure
  property_count: 3
  slug: microsoft-copilot-ai-interaction-link-structure
- name: Microsoft Copilot Ai Interaction Mention Structure
  property_count: 3
  slug: microsoft-copilot-ai-interaction-mention-structure
- name: Microsoft Copilot Ai Interaction Structure
  property_count: 13
  slug: microsoft-copilot-ai-interaction-structure
- name: Microsoft Copilot Chat Conversation Request Structure
  property_count: 3
  slug: microsoft-copilot-chat-conversation-request-structure
- name: Microsoft Copilot Chat Conversation Response Structure
  property_count: 1
  slug: microsoft-copilot-chat-conversation-response-structure
- name: Microsoft Copilot Chat Message Request Structure
  property_count: 2
  slug: microsoft-copilot-chat-message-request-structure
- name: Microsoft Copilot Chat Message Response Structure
  property_count: 0
  slug: microsoft-copilot-chat-message-response-structure
- name: Microsoft Copilot Chat Message Structure
  property_count: 4
  slug: microsoft-copilot-chat-message-structure
- name: Microsoft Copilot Copilot Search Data Sources Configuration Structure
  property_count: 1
  slug: microsoft-copilot-copilot-search-data-sources-configuration-structure
- name: Microsoft Copilot Data Source Configuration Structure
  property_count: 1
  slug: microsoft-copilot-data-source-configuration-structure
- name: Microsoft Copilot Identity Set Structure
  property_count: 3
  slug: microsoft-copilot-identity-set-structure
- name: Microsoft Copilot Item Body Structure
  property_count: 2
  slug: microsoft-copilot-item-body-structure
- name: Microsoft Copilot O Data Error Structure
  property_count: 1
  slug: microsoft-copilot-o-data-error-structure
- name: Microsoft Copilot Retrieval Extract Structure
  property_count: 2
  slug: microsoft-copilot-retrieval-extract-structure
- name: Microsoft Copilot Retrieval Hit Structure
  property_count: 4
  slug: microsoft-copilot-retrieval-hit-structure
- name: Microsoft Copilot Retrieval Request Structure
  property_count: 5
  slug: microsoft-copilot-retrieval-request-structure
- name: Microsoft Copilot Retrieval Response Structure
  property_count: 1
  slug: microsoft-copilot-retrieval-response-structure
- name: Microsoft Copilot Search Hit Structure
  property_count: 4
  slug: microsoft-copilot-search-hit-structure
- name: Microsoft Copilot Search Request Structure
  property_count: 2
  slug: microsoft-copilot-search-request-structure
- name: Microsoft Copilot Search Response Structure
  property_count: 3
  slug: microsoft-copilot-search-response-structure
- name: Microsoft Copilot Sensitivity Label Structure
  property_count: 5
  slug: microsoft-copilot-sensitivity-label-structure
- name: Microsoft Copilot Structure
  property_count: 0
  slug: microsoft-copilot-structure
- name: Microsoft Copilot Subscription Request Structure
  property_count: 5
  slug: microsoft-copilot-subscription-request-structure
- name: Microsoft Copilot Subscription Structure
  property_count: 6
  slug: microsoft-copilot-subscription-structure
jsonld:
- class_count: 0
  name: Microsoft Copilot Context
  property_count: 0
  slug: microsoft-copilot-context
layout: provider
modified: '2026-05-19'
name: Microsoft Copilot
nav: Providers
network: true
overview: 'Microsoft Copilot publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Change Notifications API, Chat API, Interaction Export API, and 2 more. Tagged areas include Agents, AI Assistant, Artificial Intelligence, Chatbot, and Copilot.


  The Microsoft Copilot catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft Copilot''s developer surface includes authentication, getting-started guide, pricing, support, engineering blog, developer portal, code examples, and 15 more developer resources.'
plans:
- name: Microsoft Copilot Plans Pricing
  plan_count: 7
  slug: microsoft-copilot-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Microsoft Copilot Rate Limits
  slug: microsoft-copilot-rate-limits
rules:
- name: Microsoft Copilot API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-copilot-jsonschema-spectral-rules
- name: Microsoft Copilot API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 8
  slug: microsoft-copilot-spectral-rules
scopes:
- name: Microsoft Copilot Scopes
  scope_count: 5
  slug: microsoft-copilot-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: exemplar
  composite: 66.2
  delta: -2.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 74.6
    developer_ergonomics: 47.8
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 73.7
  previous_composite: 68.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-copilot/refs/heads/main/screenshots/microsoft-copilot-2026-06-20T185448.png
security:
- kind: authentication
  name: Microsoft Copilot Authentication
  slug: microsoft-copilot-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Copilot Domain Security
  slug: microsoft-copilot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Copilot Vulnerability Disclosure
  slug: microsoft-copilot-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-copilot
tags:
- Agents
- AI Assistant
- Artificial Intelligence
- Chatbot
- Copilot
- Extensibility
- Generative AI
- Microsoft 365
- Productivity
use_cases:
- description: Build applications that retrieve relevant enterprise content from Microsoft 365 while respecting permissions and compliance controls.
  name: Enterprise Knowledge Retrieval
- description: Integrate Copilot capabilities into line-of-business applications for document summarization, drafting, and data analysis.
  name: AI-Assisted Productivity
- description: Create domain-specific AI agents using Copilot Studio that automate workflows and answer questions from custom data sources.
  name: Custom Agent Development
- description: Monitor and audit Copilot usage across the organization with interaction history export and change notifications.
  name: Compliance and Governance
website: https://developer.microsoft.com/en-us/microsoft-365/copilot
---
