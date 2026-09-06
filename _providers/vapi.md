---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 48
  human_in_the_loop: 48
  name: Vapi Agentic Access
  operation_count: 79
  slug: vapi-agentic-access
  summary_line: 79 operations · 48 acting · 48 human-in-the-loop
api_count: 1
apis:
- description: Server- and client-side webhook events emitted by Vapi during voice sessions, including end-of-call reports, transcripts, function calls, status updates, and tool invocations.
  name: Vapi Webhooks API
  slug: webhooks
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Analytics API from Vapi — 1 operation(s) for analytics.
  name: Vapi Analytics API
  slug: vapi-analytics-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Assistants API from Vapi — 2 operation(s) for assistants.
  name: Vapi Assistants API
  slug: vapi-assistants-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Calls API from Vapi — 2 operation(s) for calls.
  name: Vapi Calls API
  slug: vapi-calls-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Campaigns API from Vapi — 2 operation(s) for campaigns.
  name: Vapi Campaigns API
  slug: vapi-campaigns-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Chats API from Vapi — 3 operation(s) for chats.
  name: Vapi Chats API
  slug: vapi-chats-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Eval API from Vapi — 4 operation(s) for eval.
  name: Vapi Eval API
  slug: vapi-eval-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Files API from Vapi — 2 operation(s) for files.
  name: Vapi Files API
  slug: vapi-files-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Insight API from Vapi — 4 operation(s) for insight.
  name: Vapi Insight API
  slug: vapi-insight-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Observability/Scorecard API from Vapi — 2 operation(s) for observability/scorecard.
  name: Vapi Observability/Scorecard API
  slug: vapi-observability-scorecard-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Phone Numbers API from Vapi — 3 operation(s) for phone numbers.
  name: Vapi Phone Numbers API
  slug: vapi-phone-numbers-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Provider Resources API from Vapi — 2 operation(s) for provider resources.
  name: Vapi Provider Resources API
  slug: vapi-provider-resources-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Sessions API from Vapi — 2 operation(s) for sessions.
  name: Vapi Sessions API
  slug: vapi-sessions-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Squads API from Vapi — 2 operation(s) for squads.
  name: Vapi Squads API
  slug: vapi-squads-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Structured Outputs API from Vapi — 3 operation(s) for structured outputs.
  name: Vapi Structured Outputs API
  slug: vapi-structured-outputs-api
- baseURL: https://api.vapi.ai
  baseurl_source: declared
  description: The Tools API from Vapi — 2 operation(s) for tools.
  name: Vapi Tools API
  slug: vapi-tools-api
artifact_total: 922
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vapi Analytics API
  slug: open-vapi-analytics-api
- collection_type: open
  name: Vapi Analytics Assistants API
  slug: open-vapi-assistants-api
- collection_type: open
  name: Vapi Analytics Calls API
  slug: open-vapi-calls-api
- collection_type: open
  name: Vapi Analytics Campaigns API
  slug: open-vapi-campaigns-api
- collection_type: open
  name: Vapi Analytics Chats API
  slug: open-vapi-chats-api
- collection_type: open
  name: Vapi Analytics Eval API
  slug: open-vapi-eval-api
- collection_type: open
  name: Vapi Analytics Files API
  slug: open-vapi-files-api
- collection_type: open
  name: Vapi Analytics Insight API
  slug: open-vapi-insight-api
- collection_type: open
  name: Vapi Analytics Observability/Scorecard API
  slug: open-vapi-observability-scorecard-api
- collection_type: open
  name: Vapi Analytics Phone Numbers API
  slug: open-vapi-phone-numbers-api
- collection_type: open
  name: Vapi Analytics Provider Resources API
  slug: open-vapi-provider-resources-api
- collection_type: open
  name: Vapi Analytics Sessions API
  slug: open-vapi-sessions-api
- collection_type: open
  name: Vapi Analytics Squads API
  slug: open-vapi-squads-api
- collection_type: open
  name: Vapi Analytics Structured Outputs API
  slug: open-vapi-structured-outputs-api
- collection_type: open
  name: Vapi Analytics Tools API
  slug: open-vapi-tools-api
- collection_type: open
  name: Vapi API
  slug: open-vapi
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vapi-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vapi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vapi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vapi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VapiAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vapi-ai
- group: company
  title: ''
  type: Website
  url: https://vapi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vapi.ai/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/vapi-openapi.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vapi-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://vapi.ai/llms.txt
created: '2026-05-08'
description: Vapi is a voice AI agents platform for building, testing, and deploying real-time voice agents across phone, web, and SIP. The Vapi REST API exposes assistants, calls, chats, campaigns, phone numbers, tools, files, squads, sessions, structured outputs, and analytics, plus server/client webhook events. A published OpenAPI spec is available at https://api.vapi.ai/api-json.
finops:
- name: Vapi Finops
  service_category: AI
  slug: vapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vapi.png
json_schemas:
- name: AddVoiceToProviderDTO
  property_count: 3
  slug: vapi-addvoicetoproviderdto
- name: AIEdgeCondition
  property_count: 2
  slug: vapi-aiedgecondition
- name: Analysis
  property_count: 4
  slug: vapi-analysis
- name: AnalysisCost
  property_count: 7
  slug: vapi-analysiscost
- name: AnalysisCostBreakdown
  property_count: 16
  slug: vapi-analysiscostbreakdown
- name: AnalysisPlan
  property_count: 6
  slug: vapi-analysisplan
- name: AnalyticsOperation
  property_count: 3
  slug: vapi-analyticsoperation
- name: AnalyticsQuery
  property_count: 6
  slug: vapi-analyticsquery
- name: AnalyticsQueryDTO
  property_count: 1
  slug: vapi-analyticsquerydto
- name: AnalyticsQueryResult
  property_count: 3
  slug: vapi-analyticsqueryresult
- name: AnthropicBedrockCredential
  property_count: 10
  slug: vapi-anthropicbedrockcredential
- name: AnthropicBedrockModel
  property_count: 11
  slug: vapi-anthropicbedrockmodel
- name: AnthropicCredential
  property_count: 7
  slug: vapi-anthropiccredential
- name: AnthropicModel
  property_count: 11
  slug: vapi-anthropicmodel
- name: AnthropicThinkingConfig
  property_count: 2
  slug: vapi-anthropicthinkingconfig
- name: AnyscaleCredential
  property_count: 7
  slug: vapi-anyscalecredential
- name: AnyscaleModel
  property_count: 10
  slug: vapi-anyscalemodel
- name: ApiRequestTool
  property_count: 19
  slug: vapi-apirequesttool
- name: Artifact
  property_count: 18
  slug: vapi-artifact
- name: ArtifactPlan
  property_count: 17
  slug: vapi-artifactplan
- name: AssemblyAICredential
  property_count: 7
  slug: vapi-assemblyaicredential
- name: AssemblyAITranscriber
  property_count: 16
  slug: vapi-assemblyaitranscriber
- name: Assistant
  property_count: 35
  slug: vapi-assistant
- name: AssistantActivation
  property_count: 2
  slug: vapi-assistantactivation
- name: AssistantCustomEndpointingRule
  property_count: 4
  slug: vapi-assistantcustomendpointingrule
- name: AssistantMessage
  property_count: 6
  slug: vapi-assistantmessage
- name: AssistantMessageEvaluationContinuePlan
  property_count: 3
  slug: vapi-assistantmessageevaluationcontinueplan
- name: AssistantMessageJudgePlanAI
  property_count: 3
  slug: vapi-assistantmessagejudgeplanai
- name: AssistantMessageJudgePlanExact
  property_count: 3
  slug: vapi-assistantmessagejudgeplanexact
- name: AssistantMessageJudgePlanRegex
  property_count: 3
  slug: vapi-assistantmessagejudgeplanregex
- name: AssistantOverrides
  property_count: 33
  slug: vapi-assistantoverrides
- name: AssistantPaginatedResponse
  property_count: 2
  slug: vapi-assistantpaginatedresponse
- name: AssistantSpeechWordAlignmentTiming
  property_count: 4
  slug: vapi-assistantspeechwordalignmenttiming
- name: AssistantSpeechWordProgressTiming
  property_count: 6
  slug: vapi-assistantspeechwordprogresstiming
- name: AssistantSpeechWordTimestamp
  property_count: 3
  slug: vapi-assistantspeechwordtimestamp
- name: AssistantVersionPaginatedResponse
  property_count: 3
  slug: vapi-assistantversionpaginatedresponse
- name: AutoReloadPlan
  property_count: 2
  slug: vapi-autoreloadplan
- name: AWSIAMCredentialsAuthenticationPlan
  property_count: 3
  slug: vapi-awsiamcredentialsauthenticationplan
- name: AWSStsAssumeRoleUser
  property_count: 2
  slug: vapi-awsstsassumeroleuser
- name: AWSStsAuthenticationArtifact
  property_count: 1
  slug: vapi-awsstsauthenticationartifact
- name: AWSStsAuthenticationPlan
  property_count: 3
  slug: vapi-awsstsauthenticationplan
- name: AWSStsAuthenticationSession
  property_count: 4
  slug: vapi-awsstsauthenticationsession
- name: AWSStsCredentials
  property_count: 4
  slug: vapi-awsstscredentials
- name: AzureBlobStorageBucketPlan
  property_count: 3
  slug: vapi-azureblobstoragebucketplan
- name: AzureCredential
  property_count: 11
  slug: vapi-azurecredential
- name: AzureOpenAICredential
  property_count: 11
  slug: vapi-azureopenaicredential
- name: AzureSpeechTranscriber
  property_count: 6
  slug: vapi-azurespeechtranscriber
- name: AzureVoice
  property_count: 6
  slug: vapi-azurevoice
- name: BackgroundSpeechDenoisingPlan
  property_count: 2
  slug: vapi-backgroundspeechdenoisingplan
- name: BackoffPlan
  property_count: 4
  slug: vapi-backoffplan
- name: BarInsight
  property_count: 12
  slug: vapi-barinsight
- name: BarInsightFromCallTable
  property_count: 7
  slug: vapi-barinsightfromcalltable
- name: BarInsightMetadata
  property_count: 5
  slug: vapi-barinsightmetadata
- name: BashTool
  property_count: 10
  slug: vapi-bashtool
- name: BashToolWithToolCall
  property_count: 7
  slug: vapi-bashtoolwithtoolcall
- name: BearerAuthenticationPlan
  property_count: 4
  slug: vapi-bearerauthenticationplan
- name: BothCustomEndpointingRule
  property_count: 6
  slug: vapi-bothcustomendpointingrule
- name: BotMessage
  property_count: 7
  slug: vapi-botmessage
- name: BucketPlan
  property_count: 5
  slug: vapi-bucketplan
- name: ByoPhoneNumber
  property_count: 16
  slug: vapi-byophonenumber
- name: ByoSipTrunkCredential
  property_count: 12
  slug: vapi-byosiptrunkcredential
- name: Call
  property_count: 40
  slug: vapi-call
- name: CallBatchError
  property_count: 2
  slug: vapi-callbatcherror
- name: CallBatchResponse
  property_count: 3
  slug: vapi-callbatchresponse
- name: CallHookAssistantSpeechInterrupted
  property_count: 2
  slug: vapi-callhookassistantspeechinterrupted
- name: CallHookCallEnding
  property_count: 3
  slug: vapi-callhookcallending
- name: CallHookCustomerSpeechInterrupted
  property_count: 2
  slug: vapi-callhookcustomerspeechinterrupted
- name: CallHookCustomerSpeechTimeout
  property_count: 4
  slug: vapi-callhookcustomerspeechtimeout
- name: CallHookFilter
  property_count: 3
  slug: vapi-callhookfilter
- name: CallHookModelResponseTimeout
  property_count: 2
  slug: vapi-callhookmodelresponsetimeout
- name: CallHookTranscriberEndpointedSpeechLowConfidence
  property_count: 3
  slug: vapi-callhooktranscriberendpointedspeechlowconfidence
- name: CallPaginatedResponse
  property_count: 2
  slug: vapi-callpaginatedresponse
- name: Campaign
  property_count: 20
  slug: vapi-campaign
- name: CampaignPaginatedResponse
  property_count: 2
  slug: vapi-campaignpaginatedresponse
- name: CartesiaCredential
  property_count: 8
  slug: vapi-cartesiacredential
- name: CartesiaExperimentalControls
  property_count: 2
  slug: vapi-cartesiaexperimentalcontrols
- name: CartesiaGenerationConfig
  property_count: 3
  slug: vapi-cartesiagenerationconfig
- name: CartesiaGenerationConfigExperimental
  property_count: 1
  slug: vapi-cartesiagenerationconfigexperimental
- name: CartesiaPronunciationDictionary
  property_count: 6
  slug: vapi-cartesiapronunciationdictionary
- name: CartesiaPronunciationDictItem
  property_count: 2
  slug: vapi-cartesiapronunciationdictitem
- name: CartesiaTranscriber
  property_count: 4
  slug: vapi-cartesiatranscriber
- name: CartesiaVoice
  property_count: 10
  slug: vapi-cartesiavoice
- name: CerebrasCredential
  property_count: 7
  slug: vapi-cerebrascredential
- name: CerebrasModel
  property_count: 10
  slug: vapi-cerebrasmodel
- name: Chat
  property_count: 18
  slug: vapi-chat
- name: ChatAssistantOverrides
  property_count: 1
  slug: vapi-chatassistantoverrides
- name: ChatCost
  property_count: 2
  slug: vapi-chatcost
- name: ChatEvalAssistantMessageEvaluation
  property_count: 3
  slug: vapi-chatevalassistantmessageevaluation
- name: ChatEvalAssistantMessageMock
  property_count: 3
  slug: vapi-chatevalassistantmessagemock
- name: ChatEvalAssistantMessageMockToolCall
  property_count: 2
  slug: vapi-chatevalassistantmessagemocktoolcall
- name: ChatEvalSystemMessageMock
  property_count: 2
  slug: vapi-chatevalsystemmessagemock
- name: ChatEvalToolResponseMessageEvaluation
  property_count: 2
  slug: vapi-chatevaltoolresponsemessageevaluation
- name: ChatEvalToolResponseMessageMock
  property_count: 2
  slug: vapi-chatevaltoolresponsemessagemock
- name: ChatEvalUserMessageMock
  property_count: 2
  slug: vapi-chatevalusermessagemock
- name: ChatPaginatedResponse
  property_count: 2
  slug: vapi-chatpaginatedresponse
- name: ChunkPlan
  property_count: 4
  slug: vapi-chunkplan
- name: ClientInboundMessage
  property_count: 1
  slug: vapi-clientinboundmessage
- name: ClientInboundMessageAddMessage
  property_count: 3
  slug: vapi-clientinboundmessageaddmessage
- name: ClientInboundMessageControl
  property_count: 2
  slug: vapi-clientinboundmessagecontrol
- name: ClientInboundMessageEndCall
  property_count: 1
  slug: vapi-clientinboundmessageendcall
- name: ClientInboundMessageSay
  property_count: 5
  slug: vapi-clientinboundmessagesay
- name: ClientInboundMessageSendTransportMessage
  property_count: 2
  slug: vapi-clientinboundmessagesendtransportmessage
- name: ClientInboundMessageTransfer
  property_count: 3
  slug: vapi-clientinboundmessagetransfer
- name: ClientMessage
  property_count: 1
  slug: vapi-clientmessage
- name: ClientMessageAssistantSpeech
  property_count: 10
  slug: vapi-clientmessageassistantspeech
- name: ClientMessageAssistantStarted
  property_count: 7
  slug: vapi-clientmessageassistantstarted
- name: ClientMessageCallDeleted
  property_count: 6
  slug: vapi-clientmessagecalldeleted
- name: ClientMessageCallDeleteFailed
  property_count: 6
  slug: vapi-clientmessagecalldeletefailed
- name: ClientMessageChatCreated
  property_count: 7
  slug: vapi-clientmessagechatcreated
- name: ClientMessageChatDeleted
  property_count: 7
  slug: vapi-clientmessagechatdeleted
- name: ClientMessageConversationUpdate
  property_count: 8
  slug: vapi-clientmessageconversationupdate
- name: ClientMessageHang
  property_count: 6
  slug: vapi-clientmessagehang
- name: ClientMessageLanguageChangeDetected
  property_count: 7
  slug: vapi-clientmessagelanguagechangedetected
- name: ClientMessageMetadata
  property_count: 7
  slug: vapi-clientmessagemetadata
- name: ClientMessageModelOutput
  property_count: 8
  slug: vapi-clientmessagemodeloutput
- name: ClientMessageSessionCreated
  property_count: 7
  slug: vapi-clientmessagesessioncreated
- name: ClientMessageSessionDeleted
  property_count: 7
  slug: vapi-clientmessagesessiondeleted
- name: ClientMessageSessionUpdated
  property_count: 7
  slug: vapi-clientmessagesessionupdated
- name: ClientMessageSpeechUpdate
  property_count: 9
  slug: vapi-clientmessagespeechupdate
- name: ClientMessageToolCalls
  property_count: 8
  slug: vapi-clientmessagetoolcalls
- name: ClientMessageToolCallsResult
  property_count: 7
  slug: vapi-clientmessagetoolcallsresult
- name: ClientMessageTranscript
  property_count: 12
  slug: vapi-clientmessagetranscript
- name: ClientMessageTransferUpdate
  property_count: 11
  slug: vapi-clientmessagetransferupdate
- name: ClientMessageUserInterrupted
  property_count: 7
  slug: vapi-clientmessageuserinterrupted
- name: ClientMessageVoiceInput
  property_count: 7
  slug: vapi-clientmessagevoiceinput
- name: ClientMessageWorkflowNodeStarted
  property_count: 7
  slug: vapi-clientmessageworkflownodestarted
- name: CloneVoiceDTO
  property_count: 4
  slug: vapi-clonevoicedto
- name: CloudflareCredential
  property_count: 11
  slug: vapi-cloudflarecredential
- name: CloudflareR2BucketPlan
  property_count: 5
  slug: vapi-cloudflarer2bucketplan
- name: CodeTool
  property_count: 15
  slug: vapi-codetool
- name: CodeToolEnvironmentVariable
  property_count: 2
  slug: vapi-codetoolenvironmentvariable
- name: Compliance
  property_count: 1
  slug: vapi-compliance
- name: ComplianceOverride
  property_count: 1
  slug: vapi-complianceoverride
- name: CompliancePlan
  property_count: 4
  slug: vapi-complianceplan
- name: ComputerTool
  property_count: 13
  slug: vapi-computertool
- name: ComputerToolWithToolCall
  property_count: 10
  slug: vapi-computertoolwithtoolcall
- name: Condition
  property_count: 3
  slug: vapi-condition
- name: ContextEngineeringPlanAll
  property_count: 1
  slug: vapi-contextengineeringplanall
- name: ContextEngineeringPlanLastNMessages
  property_count: 2
  slug: vapi-contextengineeringplanlastnmessages
- name: ContextEngineeringPlanNone
  property_count: 1
  slug: vapi-contextengineeringplannone
- name: ContextEngineeringPlanPreviousAssistantMessages
  property_count: 1
  slug: vapi-contextengineeringplanpreviousassistantmessages
- name: ContextEngineeringPlanUserAndAssistantMessages
  property_count: 1
  slug: vapi-contextengineeringplanuserandassistantmessages
- name: ConversationNode
  property_count: 12
  slug: vapi-conversationnode
- name: CostBreakdown
  property_count: 12
  slug: vapi-costbreakdown
- name: CreateAnthropicBedrockCredentialDTO
  property_count: 4
  slug: vapi-createanthropicbedrockcredentialdto
- name: CreateAnthropicCredentialDTO
  property_count: 3
  slug: vapi-createanthropiccredentialdto
- name: CreateAnyscaleCredentialDTO
  property_count: 3
  slug: vapi-createanyscalecredentialdto
- name: CreateApiRequestToolDTO
  property_count: 15
  slug: vapi-createapirequesttooldto
- name: CreateAssemblyAICredentialDTO
  property_count: 3
  slug: vapi-createassemblyaicredentialdto
- name: CreateAssistantDTO
  property_count: 31
  slug: vapi-createassistantdto
- name: CreateAzureCredentialDTO
  property_count: 7
  slug: vapi-createazurecredentialdto
- name: CreateAzureOpenAICredentialDTO
  property_count: 7
  slug: vapi-createazureopenaicredentialdto
- name: CreateBarInsightFromCallTableDTO
  property_count: 7
  slug: vapi-createbarinsightfromcalltabledto
- name: CreateBashToolDTO
  property_count: 6
  slug: vapi-createbashtooldto
- name: CreateByoPhoneNumberDTO
  property_count: 11
  slug: vapi-createbyophonenumberdto
- name: CreateByoSipTrunkCredentialDTO
  property_count: 8
  slug: vapi-createbyosiptrunkcredentialdto
- name: CreateCallDTO
  property_count: 17
  slug: vapi-createcalldto
- name: CreateCampaignDTO
  property_count: 8
  slug: vapi-createcampaigndto
- name: CreateCartesiaCredentialDTO
  property_count: 4
  slug: vapi-createcartesiacredentialdto
- name: CreateCerebrasCredentialDTO
  property_count: 3
  slug: vapi-createcerebrascredentialdto
- name: CreateChatDTO
  property_count: 11
  slug: vapi-createchatdto
- name: CreateChatStreamResponse
  property_count: 4
  slug: vapi-createchatstreamresponse
- name: CreateCloudflareCredentialDTO
  property_count: 7
  slug: vapi-createcloudflarecredentialdto
- name: CreateCodeToolDTO
  property_count: 11
  slug: vapi-createcodetooldto
- name: CreateComputerToolDTO
  property_count: 9
  slug: vapi-createcomputertooldto
- name: CreateCustomCredentialDTO
  property_count: 4
  slug: vapi-createcustomcredentialdto
- name: CreateCustomerDTO
  property_count: 8
  slug: vapi-createcustomerdto
- name: CreateCustomKnowledgeBaseDTO
  property_count: 2
  slug: vapi-createcustomknowledgebasedto
- name: CreateCustomLLMCredentialDTO
  property_count: 4
  slug: vapi-createcustomllmcredentialdto
- name: CreateDeepgramCredentialDTO
  property_count: 4
  slug: vapi-createdeepgramcredentialdto
- name: CreateDeepInfraCredentialDTO
  property_count: 3
  slug: vapi-createdeepinfracredentialdto
- name: CreateDeepSeekCredentialDTO
  property_count: 3
  slug: vapi-createdeepseekcredentialdto
- name: CreateDtmfToolDTO
  property_count: 4
  slug: vapi-createdtmftooldto
- name: CreateElevenLabsCredentialDTO
  property_count: 3
  slug: vapi-createelevenlabscredentialdto
- name: CreateEmailCredentialDTO
  property_count: 3
  slug: vapi-createemailcredentialdto
- name: CreateEndCallToolDTO
  property_count: 3
  slug: vapi-createendcalltooldto
- name: CreateEvalDTO
  property_count: 4
  slug: vapi-createevaldto
- name: CreateEvalRunDTO
  property_count: 4
  slug: vapi-createevalrundto
- name: CreateFileDTO
  property_count: 1
  slug: vapi-createfiledto
- name: CreateFunctionToolDTO
  property_count: 8
  slug: vapi-createfunctiontooldto
- name: CreateGcpCredentialDTO
  property_count: 6
  slug: vapi-creategcpcredentialdto
- name: CreateGhlToolDTO
  property_count: 4
  slug: vapi-createghltooldto
- name: CreateGladiaCredentialDTO
  property_count: 3
  slug: vapi-creategladiacredentialdto
- name: CreateGoHighLevelCalendarAvailabilityToolDTO
  property_count: 3
  slug: vapi-creategohighlevelcalendaravailabilitytooldto
- name: CreateGoHighLevelCalendarEventCreateToolDTO
  property_count: 3
  slug: vapi-creategohighlevelcalendareventcreatetooldto
- name: CreateGoHighLevelContactCreateToolDTO
  property_count: 3
  slug: vapi-creategohighlevelcontactcreatetooldto
- name: CreateGoHighLevelContactGetToolDTO
  property_count: 3
  slug: vapi-creategohighlevelcontactgettooldto
- name: CreateGoHighLevelCredentialDTO
  property_count: 3
  slug: vapi-creategohighlevelcredentialdto
- name: CreateGoHighLevelMCPCredentialDTO
  property_count: 3
  slug: vapi-creategohighlevelmcpcredentialdto
- name: CreateGoogleCalendarCheckAvailabilityToolDTO
  property_count: 3
  slug: vapi-creategooglecalendarcheckavailabilitytooldto
- name: CreateGoogleCalendarCreateEventToolDTO
  property_count: 3
  slug: vapi-creategooglecalendarcreateeventtooldto
- name: CreateGoogleCalendarOAuth2AuthorizationCredentialDTO
  property_count: 3
  slug: vapi-creategooglecalendaroauth2authorizationcredentialdto
- name: CreateGoogleCalendarOAuth2ClientCredentialDTO
  property_count: 2
  slug: vapi-creategooglecalendaroauth2clientcredentialdto
- name: CreateGoogleCredentialDTO
  property_count: 3
  slug: vapi-creategooglecredentialdto
- name: CreateGoogleSheetsOAuth2AuthorizationCredentialDTO
  property_count: 3
  slug: vapi-creategooglesheetsoauth2authorizationcredentialdto
- name: CreateGoogleSheetsRowAppendToolDTO
  property_count: 3
  slug: vapi-creategooglesheetsrowappendtooldto
- name: CreateGroqCredentialDTO
  property_count: 3
  slug: vapi-creategroqcredentialdto
- name: CreateHandoffToolDTO
  property_count: 6
  slug: vapi-createhandofftooldto
- name: CreateHumeCredentialDTO
  property_count: 3
  slug: vapi-createhumecredentialdto
- name: CreateInflectionAICredentialDTO
  property_count: 3
  slug: vapi-createinflectionaicredentialdto
- name: CreateInworldCredentialDTO
  property_count: 3
  slug: vapi-createinworldcredentialdto
- name: CreateLangfuseCredentialDTO
  property_count: 5
  slug: vapi-createlangfusecredentialdto
- name: CreateLineInsightFromCallTableDTO
  property_count: 7
  slug: vapi-createlineinsightfromcalltabledto
- name: CreateLmntCredentialDTO
  property_count: 3
  slug: vapi-createlmntcredentialdto
- name: CreateMakeCredentialDTO
  property_count: 5
  slug: vapi-createmakecredentialdto
- name: CreateMakeToolDTO
  property_count: 4
  slug: vapi-createmaketooldto
- name: CreateMcpToolDTO
  property_count: 6
  slug: vapi-createmcptooldto
- name: CreateMinimaxCredentialDTO
  property_count: 4
  slug: vapi-createminimaxcredentialdto
- name: CreateMistralCredentialDTO
  property_count: 3
  slug: vapi-createmistralcredentialdto
- name: CreateNeuphonicCredentialDTO
  property_count: 3
  slug: vapi-createneuphoniccredentialdto
- name: CreateOpenAICredentialDTO
  property_count: 3
  slug: vapi-createopenaicredentialdto
- name: CreateOpenRouterCredentialDTO
  property_count: 3
  slug: vapi-createopenroutercredentialdto
- name: CreateOrgDTO
  property_count: 8
  slug: vapi-createorgdto
- name: CreateOutboundCallDTO
  property_count: 17
  slug: vapi-createoutboundcalldto
- name: CreateOutputToolDTO
  property_count: 3
  slug: vapi-createoutputtooldto
- name: CreatePerplexityAICredentialDTO
  property_count: 3
  slug: vapi-createperplexityaicredentialdto
- name: CreatePersonalityDTO
  property_count: 3
  slug: vapi-createpersonalitydto
- name: CreatePieInsightFromCallTableDTO
  property_count: 6
  slug: vapi-createpieinsightfromcalltabledto
- name: CreatePlayHTCredentialDTO
  property_count: 4
  slug: vapi-createplayhtcredentialdto
- name: CreateQueryToolDTO
  property_count: 4
  slug: vapi-createquerytooldto
- name: CreateRimeAICredentialDTO
  property_count: 3
  slug: vapi-createrimeaicredentialdto
- name: CreateRunpodCredentialDTO
  property_count: 3
  slug: vapi-createrunpodcredentialdto
- name: CreateS3CredentialDTO
  property_count: 8
  slug: vapi-creates3credentialdto
- name: CreateScenarioDTO
  property_count: 7
  slug: vapi-createscenariodto
- name: CreateScorecardDTO
  property_count: 4
  slug: vapi-createscorecarddto
- name: CreateSesameVoiceDTO
  property_count: 2
  slug: vapi-createsesamevoicedto
- name: CreateSessionDTO
  property_count: 13
  slug: vapi-createsessiondto
- name: CreateSimulationDTO
  property_count: 4
  slug: vapi-createsimulationdto
- name: CreateSimulationRunDTO
  property_count: 4
  slug: vapi-createsimulationrundto
- name: CreateSimulationSuiteDTO
  property_count: 4
  slug: vapi-createsimulationsuitedto
- name: CreateSipRequestToolDTO
  property_count: 6
  slug: vapi-createsiprequesttooldto
- name: CreateSlackOAuth2AuthorizationCredentialDTO
  property_count: 3
  slug: vapi-createslackoauth2authorizationcredentialdto
- name: CreateSlackSendMessageToolDTO
  property_count: 3
  slug: vapi-createslacksendmessagetooldto
- name: CreateSlackWebhookCredentialDTO
  property_count: 3
  slug: vapi-createslackwebhookcredentialdto
- name: CreateSmallestAICredentialDTO
  property_count: 3
  slug: vapi-createsmallestaicredentialdto
- name: CreateSmsToolDTO
  property_count: 3
  slug: vapi-createsmstooldto
- name: CreateSonioxCredentialDTO
  property_count: 4
  slug: vapi-createsonioxcredentialdto
- name: CreateSpeechmaticsCredentialDTO
  property_count: 3
  slug: vapi-createspeechmaticscredentialdto
- name: CreateSquadDTO
  property_count: 3
  slug: vapi-createsquaddto
- name: CreateStructuredOutputDTO
  property_count: 9
  slug: vapi-createstructuredoutputdto
- name: CreateSupabaseCredentialDTO
  property_count: 4
  slug: vapi-createsupabasecredentialdto
- name: CreateTavusCredentialDTO
  property_count: 3
  slug: vapi-createtavuscredentialdto
- name: CreateTelnyxPhoneNumberDTO
  property_count: 10
  slug: vapi-createtelnyxphonenumberdto
- name: CreateTestSuiteDto
  property_count: 4
  slug: vapi-createtestsuitedto
- name: CreateTestSuiteRunDto
  property_count: 1
  slug: vapi-createtestsuiterundto
- name: CreateTestSuiteTestChatDto
  property_count: 5
  slug: vapi-createtestsuitetestchatdto
- name: CreateTestSuiteTestVoiceDto
  property_count: 5
  slug: vapi-createtestsuitetestvoicedto
- name: CreateTextEditorToolDTO
  property_count: 6
  slug: vapi-createtexteditortooldto
- name: CreateTextInsightFromCallTableDTO
  property_count: 5
  slug: vapi-createtextinsightfromcalltabledto
- name: CreateTogetherAICredentialDTO
  property_count: 3
  slug: vapi-createtogetheraicredentialdto
- name: CreateTokenDTO
  property_count: 3
  slug: vapi-createtokendto
- name: CreateToolTemplateDTO
  property_count: 7
  slug: vapi-createtooltemplatedto
- name: CreateTransferCallToolDTO
  property_count: 4
  slug: vapi-createtransfercalltooldto
- name: CreateTwilioCredentialDTO
  property_count: 6
  slug: vapi-createtwiliocredentialdto
- name: CreateTwilioPhoneNumberDTO
  property_count: 14
  slug: vapi-createtwiliophonenumberdto
- name: CreateVapiPhoneNumberDTO
  property_count: 11
  slug: vapi-createvapiphonenumberdto
- name: CreateVoicemailToolDTO
  property_count: 4
  slug: vapi-createvoicemailtooldto
- name: CreateVonageCredentialDTO
  property_count: 4
  slug: vapi-createvonagecredentialdto
- name: CreateVonagePhoneNumberDTO
  property_count: 10
  slug: vapi-createvonagephonenumberdto
- name: CreateWebCallDTO
  property_count: 10
  slug: vapi-createwebcalldto
- name: CreateWebChatDTO
  property_count: 9
  slug: vapi-createwebchatdto
- name: CreateWebCustomerDTO
  property_count: 8
  slug: vapi-createwebcustomerdto
- name: CreateWebhookCredentialDTO
  property_count: 3
  slug: vapi-createwebhookcredentialdto
- name: CreateWellSaidCredentialDTO
  property_count: 3
  slug: vapi-createwellsaidcredentialdto
- name: CreateWorkflowDTO
  property_count: 24
  slug: vapi-createworkflowdto
- name: CreateXAiCredentialDTO
  property_count: 3
  slug: vapi-createxaicredentialdto
- name: CredentialActionRequest
  property_count: 2
  slug: vapi-credentialactionrequest
- name: CredentialEndUser
  property_count: 4
  slug: vapi-credentialenduser
- name: CredentialSessionError
  property_count: 2
  slug: vapi-credentialsessionerror
- name: CredentialSessionResponse
  property_count: 1
  slug: vapi-credentialsessionresponse
- name: CredentialWebhookDTO
  property_count: 12
  slug: vapi-credentialwebhookdto
- name: CustomCredential
  property_count: 9
  slug: vapi-customcredential
- name: CustomEndpointingModelSmartEndpointingPlan
  property_count: 2
  slug: vapi-customendpointingmodelsmartendpointingplan
- name: CustomerCustomEndpointingRule
  property_count: 4
  slug: vapi-customercustomendpointingrule
- name: CustomerSpeechTimeoutOptions
  property_count: 3
  slug: vapi-customerspeechtimeoutoptions
- name: CustomKnowledgeBase
  property_count: 4
  slug: vapi-customknowledgebase
- name: CustomLLMCredential
  property_count: 9
  slug: vapi-customllmcredential
- name: CustomLLMModel
  property_count: 15
  slug: vapi-customllmmodel
- name: CustomMessage
  property_count: 3
  slug: vapi-custommessage
- name: CustomTranscriber
  property_count: 3
  slug: vapi-customtranscriber
- name: CustomVoice
  property_count: 6
  slug: vapi-customvoice
- name: DeepgramCredential
  property_count: 8
  slug: vapi-deepgramcredential
- name: DeepgramTranscriber
  property_count: 16
  slug: vapi-deepgramtranscriber
- name: DeepgramVoice
  property_count: 7
  slug: vapi-deepgramvoice
- name: DeepInfraCredential
  property_count: 7
  slug: vapi-deepinfracredential
- name: DeepInfraModel
  property_count: 10
  slug: vapi-deepinframodel
- name: DeepSeekCredential
  property_count: 7
  slug: vapi-deepseekcredential
- name: DeepSeekModel
  property_count: 10
  slug: vapi-deepseekmodel
- name: DeleteCallDTO
  property_count: 1
  slug: vapi-deletecalldto
- name: DeveloperMessage
  property_count: 4
  slug: vapi-developermessage
- name: DialPlanEntry
  property_count: 2
  slug: vapi-dialplanentry
- name: DtmfTool
  property_count: 8
  slug: vapi-dtmftool
- name: Edge
  property_count: 4
  slug: vapi-edge
- name: ElevenLabsCredential
  property_count: 7
  slug: vapi-elevenlabscredential
- name: ElevenLabsPronunciationDictionary
  property_count: 8
  slug: vapi-elevenlabspronunciationdictionary
- name: ElevenLabsPronunciationDictionaryLocator
  property_count: 2
  slug: vapi-elevenlabspronunciationdictionarylocator
- name: ElevenLabsTranscriber
  property_count: 8
  slug: vapi-elevenlabstranscriber
- name: ElevenLabsVoice
  property_count: 16
  slug: vapi-elevenlabsvoice
- name: EmailCredential
  property_count: 7
  slug: vapi-emailcredential
- name: EndCallTool
  property_count: 7
  slug: vapi-endcalltool
- name: EndpointedSpeechLowConfidenceOptions
  property_count: 2
  slug: vapi-endpointedspeechlowconfidenceoptions
- name: Eval
  property_count: 8
  slug: vapi-eval
- name: EvalAnthropicModel
  property_count: 6
  slug: vapi-evalanthropicmodel
- name: EvalCustomModel
  property_count: 8
  slug: vapi-evalcustommodel
- name: EvalGoogleModel
  property_count: 5
  slug: vapi-evalgooglemodel
- name: EvalGroqModel
  property_count: 5
  slug: vapi-evalgroqmodel
- name: EvalModelListOptions
  property_count: 1
  slug: vapi-evalmodellistoptions
- name: EvalOpenAIModel
  property_count: 5
  slug: vapi-evalopenaimodel
- name: EvalPaginatedResponse
  property_count: 2
  slug: vapi-evalpaginatedresponse
- name: EvalRun
  property_count: 15
  slug: vapi-evalrun
- name: EvalRunPaginatedResponse
  property_count: 2
  slug: vapi-evalrunpaginatedresponse
- name: EvalRunResult
  property_count: 4
  slug: vapi-evalrunresult
- name: EvalRunTargetAssistant
  property_count: 4
  slug: vapi-evalruntargetassistant
- name: EvalRunTargetSquad
  property_count: 4
  slug: vapi-evalruntargetsquad
- name: EvaluationPlanItem
  property_count: 5
  slug: vapi-evaluationplanitem
- name: EvalUserEditable
  property_count: 4
  slug: vapi-evalusereditable
- name: EventsTableBooleanCondition
  property_count: 3
  slug: vapi-eventstablebooleancondition
- name: EventsTableNumberCondition
  property_count: 3
  slug: vapi-eventstablenumbercondition
- name: EventsTableStringCondition
  property_count: 3
  slug: vapi-eventstablestringcondition
- name: ExactReplacement
  property_count: 4
  slug: vapi-exactreplacement
- name: ExportChatDTO
  property_count: 21
  slug: vapi-exportchatdto
- name: ExportSessionDTO
  property_count: 25
  slug: vapi-exportsessiondto
- name: FallbackAssemblyAITranscriber
  property_count: 15
  slug: vapi-fallbackassemblyaitranscriber
- name: FallbackAzureSpeechTranscriber
  property_count: 5
  slug: vapi-fallbackazurespeechtranscriber
- name: FallbackAzureVoice
  property_count: 5
  slug: vapi-fallbackazurevoice
- name: FallbackCartesiaTranscriber
  property_count: 3
  slug: vapi-fallbackcartesiatranscriber
- name: FallbackCartesiaVoice
  property_count: 9
  slug: vapi-fallbackcartesiavoice
- name: FallbackCustomTranscriber
  property_count: 2
  slug: vapi-fallbackcustomtranscriber
- name: FallbackCustomVoice
  property_count: 5
  slug: vapi-fallbackcustomvoice
- name: FallbackDeepgramTranscriber
  property_count: 15
  slug: vapi-fallbackdeepgramtranscriber
- name: FallbackDeepgramVoice
  property_count: 6
  slug: vapi-fallbackdeepgramvoice
- name: FallbackElevenLabsTranscriber
  property_count: 7
  slug: vapi-fallbackelevenlabstranscriber
- name: FallbackElevenLabsVoice
  property_count: 15
  slug: vapi-fallbackelevenlabsvoice
- name: FallbackGladiaTranscriber
  property_count: 15
  slug: vapi-fallbackgladiatranscriber
- name: FallbackGoogleTranscriber
  property_count: 3
  slug: vapi-fallbackgoogletranscriber
- name: FallbackHumeVoice
  property_count: 7
  slug: vapi-fallbackhumevoice
- name: FallbackInworldVoice
  property_count: 8
  slug: vapi-fallbackinworldvoice
- name: FallbackLMNTVoice
  property_count: 6
  slug: vapi-fallbacklmntvoice
- name: FallbackMinimaxVoice
  property_count: 13
  slug: vapi-fallbackminimaxvoice
- name: FallbackNeuphonicVoice
  property_count: 7
  slug: vapi-fallbackneuphonicvoice
- name: FallbackOpenAITranscriber
  property_count: 3
  slug: vapi-fallbackopenaitranscriber
- name: FallbackOpenAIVoice
  property_count: 7
  slug: vapi-fallbackopenaivoice
- name: FallbackPlan
  property_count: 1
  slug: vapi-fallbackplan
- name: FallbackPlayHTVoice
  property_count: 12
  slug: vapi-fallbackplayhtvoice
- name: FallbackRimeAIVoice
  property_count: 11
  slug: vapi-fallbackrimeaivoice
- name: FallbackSesameVoice
  property_count: 5
  slug: vapi-fallbacksesamevoice
- name: FallbackSmallestAIVoice
  property_count: 6
  slug: vapi-fallbacksmallestaivoice
- name: FallbackSonioxTranscriber
  property_count: 8
  slug: vapi-fallbacksonioxtranscriber
- name: FallbackSpeechmaticsTranscriber
  property_count: 12
  slug: vapi-fallbackspeechmaticstranscriber
- name: FallbackTalkscriberTranscriber
  property_count: 3
  slug: vapi-fallbacktalkscribertranscriber
- name: FallbackTavusVoice
  property_count: 10
  slug: vapi-fallbacktavusvoice
- name: FallbackTranscriberPlan
  property_count: 1
  slug: vapi-fallbacktranscriberplan
- name: FallbackVapiVoice
  property_count: 6
  slug: vapi-fallbackvapivoice
- name: FallbackWellSaidVoice
  property_count: 7
  slug: vapi-fallbackwellsaidvoice
- name: File
  property_count: 18
  slug: vapi-file
- name: FilterDateTypeColumnOnCallTable
  property_count: 3
  slug: vapi-filterdatetypecolumnoncalltable
- name: FilterNumberArrayTypeColumnOnCallTable
  property_count: 3
  slug: vapi-filternumberarraytypecolumnoncalltable
- name: FilterNumberTypeColumnOnCallTable
  property_count: 3
  slug: vapi-filternumbertypecolumnoncalltable
- name: FilterStringArrayTypeColumnOnCallTable
  property_count: 3
  slug: vapi-filterstringarraytypecolumnoncalltable
- name: FilterStringTypeColumnOnCallTable
  property_count: 3
  slug: vapi-filterstringtypecolumnoncalltable
- name: FilterStructuredOutputColumnOnCallTable
  property_count: 3
  slug: vapi-filterstructuredoutputcolumnoncalltable
- name: FormatPlan
  property_count: 4
  slug: vapi-formatplan
- name: FourierDenoisingPlan
  property_count: 6
  slug: vapi-fourierdenoisingplan
- name: FunctionCall
  property_count: 2
  slug: vapi-functioncall
- name: FunctionCallHookAction
  property_count: 8
  slug: vapi-functioncallhookaction
- name: FunctionTool
  property_count: 12
  slug: vapi-functiontool
- name: FunctionToolProviderDetails
  property_count: 3
  slug: vapi-functiontoolproviderdetails
- name: FunctionToolWithToolCall
  property_count: 9
  slug: vapi-functiontoolwithtoolcall
- name: GcpCredential
  property_count: 10
  slug: vapi-gcpcredential
- name: GcpKey
  property_count: 11
  slug: vapi-gcpkey
- name: GeminiMultimodalLivePrebuiltVoiceConfig
  property_count: 1
  slug: vapi-geminimultimodalliveprebuiltvoiceconfig
- name: GeminiMultimodalLiveSpeechConfig
  property_count: 1
  slug: vapi-geminimultimodallivespeechconfig
- name: GeminiMultimodalLiveVoiceConfig
  property_count: 1
  slug: vapi-geminimultimodallivevoiceconfig
- name: GeneratedScenario
  property_count: 4
  slug: vapi-generatedscenario
- name: GenerateScenariosDTO
  property_count: 2
  slug: vapi-generatescenariosdto
- name: GenerateScenariosResponse
  property_count: 2
  slug: vapi-generatescenariosresponse
- name: GetChatPaginatedDTO
  property_count: 18
  slug: vapi-getchatpaginateddto
- name: GetEvalPaginatedDTO
  property_count: 13
  slug: vapi-getevalpaginateddto
- name: GetEvalRunPaginatedDTO
  property_count: 13
  slug: vapi-getevalrunpaginateddto
- name: GetSessionPaginatedDTO
  property_count: 22
  slug: vapi-getsessionpaginateddto
- name: GhlTool
  property_count: 8
  slug: vapi-ghltool
- name: GhlToolMetadata
  property_count: 2
  slug: vapi-ghltoolmetadata
- name: GhlToolProviderDetails
  property_count: 8
  slug: vapi-ghltoolproviderdetails
- name: GhlToolWithToolCall
  property_count: 5
  slug: vapi-ghltoolwithtoolcall
- name: GladiaCredential
  property_count: 7
  slug: vapi-gladiacredential
- name: GladiaCustomVocabularyConfigDTO
  property_count: 2
  slug: vapi-gladiacustomvocabularyconfigdto
- name: GladiaTranscriber
  property_count: 16
  slug: vapi-gladiatranscriber
- name: GladiaVocabularyItemDTO
  property_count: 4
  slug: vapi-gladiavocabularyitemdto
- name: GlobalNodePlan
  property_count: 2
  slug: vapi-globalnodeplan
- name: GoHighLevelCalendarAvailabilityTool
  property_count: 7
  slug: vapi-gohighlevelcalendaravailabilitytool
- name: GoHighLevelCalendarAvailabilityToolProviderDetails
  property_count: 3
  slug: vapi-gohighlevelcalendaravailabilitytoolproviderdetails
- name: GoHighLevelCalendarAvailabilityToolWithToolCall
  property_count: 4
  slug: vapi-gohighlevelcalendaravailabilitytoolwithtoolcall
- name: GoHighLevelCalendarEventCreateTool
  property_count: 7
  slug: vapi-gohighlevelcalendareventcreatetool
- name: GoHighLevelCalendarEventCreateToolProviderDetails
  property_count: 3
  slug: vapi-gohighlevelcalendareventcreatetoolproviderdetails
- name: GoHighLevelCalendarEventCreateToolWithToolCall
  property_count: 4
  slug: vapi-gohighlevelcalendareventcreatetoolwithtoolcall
- name: GoHighLevelContactCreateTool
  property_count: 7
  slug: vapi-gohighlevelcontactcreatetool
- name: GoHighLevelContactCreateToolProviderDetails
  property_count: 3
  slug: vapi-gohighlevelcontactcreatetoolproviderdetails
- name: GoHighLevelContactCreateToolWithToolCall
  property_count: 4
  slug: vapi-gohighlevelcontactcreatetoolwithtoolcall
- name: GoHighLevelContactGetTool
  property_count: 7
  slug: vapi-gohighlevelcontactgettool
- name: GoHighLevelContactGetToolProviderDetails
  property_count: 3
  slug: vapi-gohighlevelcontactgettoolproviderdetails
- name: GoHighLevelContactGetToolWithToolCall
  property_count: 4
  slug: vapi-gohighlevelcontactgettoolwithtoolcall
- name: GoHighLevelCredential
  property_count: 7
  slug: vapi-gohighlevelcredential
- name: GoHighLevelMCPCredential
  property_count: 7
  slug: vapi-gohighlevelmcpcredential
- name: GoogleCalendarCheckAvailabilityTool
  property_count: 7
  slug: vapi-googlecalendarcheckavailabilitytool
- name: GoogleCalendarCreateEventTool
  property_count: 7
  slug: vapi-googlecalendarcreateeventtool
- name: GoogleCalendarCreateEventToolProviderDetails
  property_count: 3
  slug: vapi-googlecalendarcreateeventtoolproviderdetails
- name: GoogleCalendarCreateEventToolWithToolCall
  property_count: 4
  slug: vapi-googlecalendarcreateeventtoolwithtoolcall
- name: GoogleCalendarOAuth2AuthorizationCredential
  property_count: 7
  slug: vapi-googlecalendaroauth2authorizationcredential
- name: GoogleCalendarOAuth2ClientCredential
  property_count: 6
  slug: vapi-googlecalendaroauth2clientcredential
- name: GoogleCredential
  property_count: 7
  slug: vapi-googlecredential
- name: GoogleModel
  property_count: 11
  slug: vapi-googlemodel
- name: GoogleRealtimeConfig
  property_count: 5
  slug: vapi-googlerealtimeconfig
- name: GoogleSheetsOAuth2AuthorizationCredential
  property_count: 7
  slug: vapi-googlesheetsoauth2authorizationcredential
- name: GoogleSheetsRowAppendTool
  property_count: 7
  slug: vapi-googlesheetsrowappendtool
- name: GoogleSheetsRowAppendToolProviderDetails
  property_count: 3
  slug: vapi-googlesheetsrowappendtoolproviderdetails
- name: GoogleSheetsRowAppendToolWithToolCall
  property_count: 4
  slug: vapi-googlesheetsrowappendtoolwithtoolcall
- name: GoogleTranscriber
  property_count: 4
  slug: vapi-googletranscriber
- name: GoogleVoicemailDetectionPlan
  property_count: 4
  slug: vapi-googlevoicemaildetectionplan
- name: GroqCredential
  property_count: 7
  slug: vapi-groqcredential
- name: GroqModel
  property_count: 10
  slug: vapi-groqmodel
- name: GroupCondition
  property_count: 3
  slug: vapi-groupcondition
- name: HandoffDestinationAssistant
  property_count: 8
  slug: vapi-handoffdestinationassistant
- name: HandoffDestinationDynamic
  property_count: 3
  slug: vapi-handoffdestinationdynamic
- name: HandoffDestinationSquad
  property_count: 8
  slug: vapi-handoffdestinationsquad
- name: HandoffTool
  property_count: 10
  slug: vapi-handofftool
- name: HangupNode
  property_count: 4
  slug: vapi-hangupnode
- name: HMACAuthenticationPlan
  property_count: 11
  slug: vapi-hmacauthenticationplan
- name: HumeCredential
  property_count: 7
  slug: vapi-humecredential
- name: HumeVoice
  property_count: 8
  slug: vapi-humevoice
- name: ImportTwilioPhoneNumberDTO
  property_count: 13
  slug: vapi-importtwiliophonenumberdto
- name: ImportVonagePhoneNumberDTO
  property_count: 9
  slug: vapi-importvonagephonenumberdto
- name: InflectionAICredential
  property_count: 7
  slug: vapi-inflectionaicredential
- name: InflectionAIModel
  property_count: 10
  slug: vapi-inflectionaimodel
- name: Insight
  property_count: 7
  slug: vapi-insight
- name: InsightFormula
  property_count: 2
  slug: vapi-insightformula
- name: InsightPaginatedResponse
  property_count: 2
  slug: vapi-insightpaginatedresponse
- name: InsightRunDTO
  property_count: 3
  slug: vapi-insightrundto
- name: InsightRunFormatPlan
  property_count: 1
  slug: vapi-insightrunformatplan
- name: InsightRunResponse
  property_count: 5
  slug: vapi-insightrunresponse
- name: InsightTimeRange
  property_count: 3
  slug: vapi-insighttimerange
- name: InsightTimeRangeWithStep
  property_count: 4
  slug: vapi-insighttimerangewithstep
- name: InviteUserDTO
  property_count: 3
  slug: vapi-inviteuserdto
- name: InvoicePlan
  property_count: 4
  slug: vapi-invoiceplan
- name: InworldCredential
  property_count: 7
  slug: vapi-inworldcredential
- name: InworldVoice
  property_count: 9
  slug: vapi-inworldvoice
- name: JSONQueryOnCallTableWithNumberTypeColumn
  property_count: 6
  slug: vapi-jsonqueryoncalltablewithnumbertypecolumn
- name: JSONQueryOnCallTableWithStringTypeColumn
  property_count: 6
  slug: vapi-jsonqueryoncalltablewithstringtypecolumn
- name: JSONQueryOnCallTableWithStructuredOutputColumn
  property_count: 6
  slug: vapi-jsonqueryoncalltablewithstructuredoutputcolumn
- name: JSONQueryOnEventsTable
  property_count: 6
  slug: vapi-jsonqueryoneventstable
- name: JsonSchema
  property_count: 9
  slug: vapi-jsonschema
- name: JwtResponse
  property_count: 2
  slug: vapi-jwtresponse
- name: KeypadInputPlan
  property_count: 3
  slug: vapi-keypadinputplan
- name: KnowledgeBase
  property_count: 5
  slug: vapi-knowledgebase
- name: KnowledgeBaseCost
  property_count: 5
  slug: vapi-knowledgebasecost
- name: KnowledgeBaseResponseDocument
  property_count: 3
  slug: vapi-knowledgebaseresponsedocument
- name: LangfuseCredential
  property_count: 9
  slug: vapi-langfusecredential
- name: LangfuseObservabilityPlan
  property_count: 6
  slug: vapi-langfuseobservabilityplan
- name: LatencyMetrics
  property_count: 6
  slug: vapi-latencymetrics
- name: LineInsight
  property_count: 12
  slug: vapi-lineinsight
- name: LineInsightFromCallTable
  property_count: 7
  slug: vapi-lineinsightfromcalltable
- name: LineInsightMetadata
  property_count: 5
  slug: vapi-lineinsightmetadata
- name: LiquidCondition
  property_count: 2
  slug: vapi-liquidcondition
- name: LivekitSmartEndpointingPlan
  property_count: 2
  slug: vapi-livekitsmartendpointingplan
- name: LmntCredential
  property_count: 7
  slug: vapi-lmntcredential
- name: LMNTVoice
  property_count: 7
  slug: vapi-lmntvoice
- name: MakeCredential
  property_count: 9
  slug: vapi-makecredential
- name: MakeTool
  property_count: 8
  slug: vapi-maketool
- name: MakeToolMetadata
  property_count: 2
  slug: vapi-maketoolmetadata
- name: MakeToolProviderDetails
  property_count: 7
  slug: vapi-maketoolproviderdetails
- name: MakeToolWithToolCall
  property_count: 5
  slug: vapi-maketoolwithtoolcall
- name: McpTool
  property_count: 10
  slug: vapi-mcptool
- name: McpToolMessages
  property_count: 2
  slug: vapi-mcptoolmessages
- name: McpToolMetadata
  property_count: 1
  slug: vapi-mcptoolmetadata
- name: MessageAddHookAction
  property_count: 3
  slug: vapi-messageaddhookaction
- name: MessageTarget
  property_count: 2
  slug: vapi-messagetarget
- name: MinimaxLLMModel
  property_count: 10
  slug: vapi-minimaxllmmodel
- name: MinimaxVoice
  property_count: 14
  slug: vapi-minimaxvoice
- name: MistralCredential
  property_count: 7
  slug: vapi-mistralcredential
- name: ModelCost
  property_count: 6
  slug: vapi-modelcost
- name: Monitor
  property_count: 3
  slug: vapi-monitor
- name: MonitorPlan
  property_count: 5
  slug: vapi-monitorplan
- name: MonitorResult
  property_count: 2
  slug: vapi-monitorresult
- name: Mono
  property_count: 3
  slug: vapi-mono
- name: NeuphonicCredential
  property_count: 7
  slug: vapi-neuphoniccredential
- name: NeuphonicVoice
  property_count: 8
  slug: vapi-neuphonicvoice
- name: NodeArtifact
  property_count: 3
  slug: vapi-nodeartifact
- name: OAuth2AuthenticationPlan
  property_count: 5
  slug: vapi-oauth2authenticationplan
- name: Oauth2AuthenticationSession
  property_count: 3
  slug: vapi-oauth2authenticationsession
- name: OpenAICredential
  property_count: 7
  slug: vapi-openaicredential
- name: OpenAIFunction
  property_count: 4
  slug: vapi-openaifunction
- name: OpenAIFunctionParameters
  property_count: 3
  slug: vapi-openaifunctionparameters
- name: OpenAIMessage
  property_count: 2
  slug: vapi-openaimessage
- name: OpenAIModel
  property_count: 14
  slug: vapi-openaimodel
- name: OpenAIResponsesRequest
  property_count: 11
  slug: vapi-openairesponsesrequest
- name: OpenAITranscriber
  property_count: 4
  slug: vapi-openaitranscriber
- name: OpenAIVoice
  property_count: 8
  slug: vapi-openaivoice
- name: OpenAIVoicemailDetectionPlan
  property_count: 4
  slug: vapi-openaivoicemaildetectionplan
- name: OpenAIWebChatRequest
  property_count: 9
  slug: vapi-openaiwebchatrequest
- name: OpenRouterCredential
  property_count: 7
  slug: vapi-openroutercredential
- name: OpenRouterModel
  property_count: 10
  slug: vapi-openroutermodel
- name: Org
  property_count: 18
  slug: vapi-org
- name: OutputTool
  property_count: 7
  slug: vapi-outputtool
- name: PaginationMeta
  property_count: 9
  slug: vapi-paginationmeta
- name: PerformanceMetrics
  property_count: 10
  slug: vapi-performancemetrics
- name: PerplexityAICredential
  property_count: 7
  slug: vapi-perplexityaicredential
- name: PerplexityAIModel
  property_count: 10
  slug: vapi-perplexityaimodel
- name: Personality
  property_count: 7
  slug: vapi-personality
- name: PhoneNumberCallEndingHookFilter
  property_count: 3
  slug: vapi-phonenumbercallendinghookfilter
- name: PhoneNumberCallRingingHookFilter
  property_count: 3
  slug: vapi-phonenumbercallringinghookfilter
- name: PhoneNumberHookCallEnding
  property_count: 3
  slug: vapi-phonenumberhookcallending
- name: PhoneNumberHookCallRinging
  property_count: 3
  slug: vapi-phonenumberhookcallringing
- name: PhoneNumberPaginatedResponse
  property_count: 2
  slug: vapi-phonenumberpaginatedresponse
- name: PieInsight
  property_count: 11
  slug: vapi-pieinsight
- name: PieInsightFromCallTable
  property_count: 6
  slug: vapi-pieinsightfromcalltable
- name: PlayHTCredential
  property_count: 8
  slug: vapi-playhtcredential
- name: PlayHTVoice
  property_count: 13
  slug: vapi-playhtvoice
- name: PromptInjectionSecurityFilter
  property_count: 1
  slug: vapi-promptinjectionsecurityfilter
- name: ProviderResource
  property_count: 8
  slug: vapi-providerresource
- name: ProviderResourcePaginatedResponse
  property_count: 2
  slug: vapi-providerresourcepaginatedresponse
- name: PublicKeyEncryptionPlan
  property_count: 3
  slug: vapi-publickeyencryptionplan
- name: QueryTool
  property_count: 8
  slug: vapi-querytool
- name: RCESecurityFilter
  property_count: 1
  slug: vapi-rcesecurityfilter
- name: Recording
  property_count: 4
  slug: vapi-recording
- name: RecordingConsent
  property_count: 2
  slug: vapi-recordingconsent
- name: RecordingConsentPlanStayOnLine
  property_count: 5
  slug: vapi-recordingconsentplanstayonline
- name: RecordingConsentPlanVerbal
  property_count: 6
  slug: vapi-recordingconsentplanverbal
- name: RegexCondition
  property_count: 4
  slug: vapi-regexcondition
- name: RegexOption
  property_count: 2
  slug: vapi-regexoption
- name: RegexReplacement
  property_count: 4
  slug: vapi-regexreplacement
- name: RegexSecurityFilter
  property_count: 2
  slug: vapi-regexsecurityfilter
- name: RelayCommandNote
  property_count: 2
  slug: vapi-relaycommandnote
- name: RelayCommandOptions
  property_count: 1
  slug: vapi-relaycommandoptions
- name: RelayCommandSay
  property_count: 2
  slug: vapi-relaycommandsay
- name: RelayRequest
  property_count: 4
  slug: vapi-relayrequest
- name: RelayResponse
  property_count: 4
  slug: vapi-relayresponse
- name: RelayTargetAssistant
  property_count: 3
  slug: vapi-relaytargetassistant
- name: RelayTargetOptions
  property_count: 1
  slug: vapi-relaytargetoptions
- name: RelayTargetSquad
  property_count: 3
  slug: vapi-relaytargetsquad
- name: ResponseCompletedEvent
  property_count: 2
  slug: vapi-responsecompletedevent
- name: ResponseErrorEvent
  property_count: 5
  slug: vapi-responseerrorevent
- name: ResponseObject
  property_count: 6
  slug: vapi-responseobject
- name: ResponseOutputMessage
  property_count: 5
  slug: vapi-responseoutputmessage
- name: ResponseOutputText
  property_count: 3
  slug: vapi-responseoutputtext
- name: ResponseTextDeltaEvent
  property_count: 5
  slug: vapi-responsetextdeltaevent
- name: ResponseTextDoneEvent
  property_count: 5
  slug: vapi-responsetextdoneevent
- name: RimeAICredential
  property_count: 7
  slug: vapi-rimeaicredential
- name: RimeAIVoice
  property_count: 12
  slug: vapi-rimeaivoice
- name: RunpodCredential
  property_count: 7
  slug: vapi-runpodcredential
- name: S3Credential
  property_count: 12
  slug: vapi-s3credential
- name: SayHookAction
  property_count: 3
  slug: vapi-sayhookaction
- name: SayPhoneNumberHookAction
  property_count: 2
  slug: vapi-sayphonenumberhookaction
- name: SbcConfiguration
  property_count: 0
  slug: vapi-sbcconfiguration
- name: Scenario
  property_count: 11
  slug: vapi-scenario
- name: ScenarioToolMock
  property_count: 3
  slug: vapi-scenariotoolmock
- name: SchedulePlan
  property_count: 2
  slug: vapi-scheduleplan
- name: Scorecard
  property_count: 8
  slug: vapi-scorecard
- name: ScorecardMetric
  property_count: 2
  slug: vapi-scorecardmetric
- name: ScorecardPaginatedResponse
  property_count: 2
  slug: vapi-scorecardpaginatedresponse
- name: SecurityFilterBase
  property_count: 0
  slug: vapi-securityfilterbase
- name: SecurityFilterPlan
  property_count: 4
  slug: vapi-securityfilterplan
- name: Server
  property_count: 7
  slug: vapi-server
- name: ServerMessage
  property_count: 1
  slug: vapi-servermessage
- name: ServerMessageAssistantRequest
  property_count: 8
  slug: vapi-servermessageassistantrequest
- name: ServerMessageAssistantSpeech
  property_count: 12
  slug: vapi-servermessageassistantspeech
- name: ServerMessageCallDeleted
  property_count: 8
  slug: vapi-servermessagecalldeleted
- name: ServerMessageCallDeleteFailed
  property_count: 8
  slug: vapi-servermessagecalldeletefailed
- name: ServerMessageCallEndpointingRequest
  property_count: 10
  slug: vapi-servermessagecallendpointingrequest
- name: ServerMessageChatCreated
  property_count: 8
  slug: vapi-servermessagechatcreated
- name: ServerMessageChatDeleted
  property_count: 8
  slug: vapi-servermessagechatdeleted
- name: ServerMessageConversationUpdate
  property_count: 10
  slug: vapi-servermessageconversationupdate
- name: ServerMessageEndOfCallReport
  property_count: 16
  slug: vapi-servermessageendofcallreport
- name: ServerMessageHandoffDestinationRequest
  property_count: 9
  slug: vapi-servermessagehandoffdestinationrequest
- name: ServerMessageHang
  property_count: 8
  slug: vapi-servermessagehang
- name: ServerMessageKnowledgeBaseRequest
  property_count: 10
  slug: vapi-servermessageknowledgebaserequest
- name: ServerMessageLanguageChangeDetected
  property_count: 9
  slug: vapi-servermessagelanguagechangedetected
- name: ServerMessageModelOutput
  property_count: 10
  slug: vapi-servermessagemodeloutput
- name: ServerMessagePhoneCallControl
  property_count: 10
  slug: vapi-servermessagephonecallcontrol
- name: ServerMessageResponse
  property_count: 1
  slug: vapi-servermessageresponse
- name: ServerMessageResponseAssistantRequest
  property_count: 11
  slug: vapi-servermessageresponseassistantrequest
- name: ServerMessageResponseCallEndpointingRequest
  property_count: 1
  slug: vapi-servermessageresponsecallendpointingrequest
- name: ServerMessageResponseHandoffDestinationRequest
  property_count: 3
  slug: vapi-servermessageresponsehandoffdestinationrequest
- name: ServerMessageResponseKnowledgeBaseRequest
  property_count: 2
  slug: vapi-servermessageresponseknowledgebaserequest
- name: ServerMessageResponseToolCalls
  property_count: 2
  slug: vapi-servermessageresponsetoolcalls
- name: ServerMessageResponseTransferDestinationRequest
  property_count: 3
  slug: vapi-servermessageresponsetransferdestinationrequest
- name: ServerMessageResponseVoiceRequest
  property_count: 1
  slug: vapi-servermessageresponsevoicerequest
- name: ServerMessageSessionCreated
  property_count: 9
  slug: vapi-servermessagesessioncreated
- name: ServerMessageSessionDeleted
  property_count: 9
  slug: vapi-servermessagesessiondeleted
- name: ServerMessageSessionUpdated
  property_count: 9
  slug: vapi-servermessagesessionupdated
- name: ServerMessageSpeechUpdate
  property_count: 11
  slug: vapi-servermessagespeechupdate
- name: ServerMessageStatusUpdate
  property_count: 16
  slug: vapi-servermessagestatusupdate
- name: ServerMessageToolCalls
  property_count: 10
  slug: vapi-servermessagetoolcalls
- name: ServerMessageTranscript
  property_count: 14
  slug: vapi-servermessagetranscript
- name: ServerMessageTransferDestinationRequest
  property_count: 8
  slug: vapi-servermessagetransferdestinationrequest
- name: ServerMessageTransferUpdate
  property_count: 13
  slug: vapi-servermessagetransferupdate
- name: ServerMessageUserInterrupted
  property_count: 9
  slug: vapi-servermessageuserinterrupted
- name: ServerMessageVoiceInput
  property_count: 9
  slug: vapi-servermessagevoiceinput
- name: ServerMessageVoiceRequest
  property_count: 10
  slug: vapi-servermessagevoicerequest
- name: SesameVoice
  property_count: 6
  slug: vapi-sesamevoice
- name: Session
  property_count: 20
  slug: vapi-session
- name: SessionCost
  property_count: 2
  slug: vapi-sessioncost
- name: SessionCreatedHook
  property_count: 3
  slug: vapi-sessioncreatedhook
- name: SessionPaginatedResponse
  property_count: 2
  slug: vapi-sessionpaginatedresponse
- name: Simulation
  property_count: 8
  slug: vapi-simulation
- name: SimulationConcurrencyResponse
  property_count: 7
  slug: vapi-simulationconcurrencyresponse
- name: SimulationHookCallEnded
  property_count: 2
  slug: vapi-simulationhookcallended
- name: SimulationHookCallStarted
  property_count: 2
  slug: vapi-simulationhookcallstarted
- name: SimulationHookInclude
  property_count: 3
  slug: vapi-simulationhookinclude
- name: SimulationHookWebhookAction
  property_count: 3
  slug: vapi-simulationhookwebhookaction
- name: SimulationRun
  property_count: 14
  slug: vapi-simulationrun
- name: SimulationRunConfiguration
  property_count: 1
  slug: vapi-simulationrunconfiguration
- name: SimulationRunItem
  property_count: 23
  slug: vapi-simulationrunitem
- name: SimulationRunItemCallMetadata
  property_count: 4
  slug: vapi-simulationrunitemcallmetadata
- name: SimulationRunItemCallMonitor
  property_count: 1
  slug: vapi-simulationrunitemcallmonitor
- name: SimulationRunItemCounts
  property_count: 6
  slug: vapi-simulationrunitemcounts
- name: SimulationRunItemImprovements
  property_count: 5
  slug: vapi-simulationrunitemimprovements
- name: SimulationRunItemImprovementSuggestion
  property_count: 2
  slug: vapi-simulationrunitemimprovementsuggestion
- name: SimulationRunItemMetadata
  property_count: 7
  slug: vapi-simulationrunitemmetadata
- name: SimulationRunItemResults
  property_count: 3
  slug: vapi-simulationrunitemresults
- name: SimulationRunSimulationEntry
  property_count: 7
  slug: vapi-simulationrunsimulationentry
- name: SimulationRunSuiteEntry
  property_count: 3
  slug: vapi-simulationrunsuiteentry
- name: SimulationRunTargetAssistant
  property_count: 3
  slug: vapi-simulationruntargetassistant
- name: SimulationRunTargetSquad
  property_count: 3
  slug: vapi-simulationruntargetsquad
- name: SimulationRunTransportConfiguration
  property_count: 1
  slug: vapi-simulationruntransportconfiguration
- name: SimulationSuite
  property_count: 8
  slug: vapi-simulationsuite
- name: SipAuthentication
  property_count: 3
  slug: vapi-sipauthentication
- name: SipRequestTool
  property_count: 10
  slug: vapi-siprequesttool
- name: SipTrunkGateway
  property_count: 7
  slug: vapi-siptrunkgateway
- name: SipTrunkOutboundAuthenticationPlan
  property_count: 3
  slug: vapi-siptrunkoutboundauthenticationplan
- name: SipTrunkOutboundSipRegisterPlan
  property_count: 3
  slug: vapi-siptrunkoutboundsipregisterplan
- name: SlackOAuth2AuthorizationCredential
  property_count: 7
  slug: vapi-slackoauth2authorizationcredential
- name: SlackSendMessageTool
  property_count: 7
  slug: vapi-slacksendmessagetool
- name: SlackWebhookCredential
  property_count: 7
  slug: vapi-slackwebhookcredential
- name: SmallestAICredential
  property_count: 7
  slug: vapi-smallestaicredential
- name: SmallestAIVoice
  property_count: 7
  slug: vapi-smallestaivoice
- name: SmartDenoisingPlan
  property_count: 1
  slug: vapi-smartdenoisingplan
- name: SmsTool
  property_count: 7
  slug: vapi-smstool
- name: SonioxContextGeneralItem
  property_count: 2
  slug: vapi-sonioxcontextgeneralitem
- name: SonioxCredential
  property_count: 8
  slug: vapi-sonioxcredential
- name: SonioxTranscriber
  property_count: 9
  slug: vapi-sonioxtranscriber
- name: SpeechmaticsCredential
  property_count: 7
  slug: vapi-speechmaticscredential
- name: SpeechmaticsCustomVocabularyItem
  property_count: 2
  slug: vapi-speechmaticscustomvocabularyitem
- name: SpeechmaticsTranscriber
  property_count: 13
  slug: vapi-speechmaticstranscriber
- name: SpkiPemPublicKeyConfig
  property_count: 3
  slug: vapi-spkipempublickeyconfig
- name: SQLInjectionSecurityFilter
  property_count: 1
  slug: vapi-sqlinjectionsecurityfilter
- name: Squad
  property_count: 7
  slug: vapi-squad
- name: SquadMemberDTO
  property_count: 4
  slug: vapi-squadmemberdto
- name: SSRFSecurityFilter
  property_count: 1
  slug: vapi-ssrfsecurityfilter
- name: StartSpeakingPlan
  property_count: 5
  slug: vapi-startspeakingplan
- name: StopSpeakingPlan
  property_count: 5
  slug: vapi-stopspeakingplan
- name: StructuredDataMultiPlan
  property_count: 2
  slug: vapi-structureddatamultiplan
- name: StructuredDataPlan
  property_count: 4
  slug: vapi-structureddataplan
- name: StructuredOutput
  property_count: 13
  slug: vapi-structuredoutput
- name: StructuredOutputEvaluationResult
  property_count: 10
  slug: vapi-structuredoutputevaluationresult
- name: StructuredOutputFilterDTO
  property_count: 8
  slug: vapi-structuredoutputfilterdto
- name: StructuredOutputPaginatedResponse
  property_count: 2
  slug: vapi-structuredoutputpaginatedresponse
- name: StructuredOutputRunDTO
  property_count: 4
  slug: vapi-structuredoutputrundto
- name: Subscription
  property_count: 43
  slug: vapi-subscription
- name: SubscriptionLimits
  property_count: 3
  slug: vapi-subscriptionlimits
- name: SuccessEvaluationPlan
  property_count: 4
  slug: vapi-successevaluationplan
- name: SummaryPlan
  property_count: 3
  slug: vapi-summaryplan
- name: SupabaseBucketPlan
  property_count: 6
  slug: vapi-supabasebucketplan
- name: SupabaseCredential
  property_count: 8
  slug: vapi-supabasecredential
- name: SyncVoiceLibraryDTO
  property_count: 1
  slug: vapi-syncvoicelibrarydto
- name: SystemMessage
  property_count: 4
  slug: vapi-systemmessage
- name: TalkscriberTranscriber
  property_count: 4
  slug: vapi-talkscribertranscriber
- name: TargetPlan
  property_count: 4
  slug: vapi-targetplan
- name: TavusConversationProperties
  property_count: 10
  slug: vapi-tavusconversationproperties
- name: TavusCredential
  property_count: 7
  slug: vapi-tavuscredential
- name: TavusVoice
  property_count: 11
  slug: vapi-tavusvoice
- name: TelnyxPhoneNumber
  property_count: 15
  slug: vapi-telnyxphonenumber
- name: Template
  property_count: 11
  slug: vapi-template
- name: TesterPlan
  property_count: 3
  slug: vapi-testerplan
- name: TestSuite
  property_count: 8
  slug: vapi-testsuite
- name: TestSuitePhoneNumber
  property_count: 2
  slug: vapi-testsuitephonenumber
- name: TestSuiteRun
  property_count: 8
  slug: vapi-testsuiterun
- name: TestSuiteRunScorerAI
  property_count: 4
  slug: vapi-testsuiterunscorerai
- name: TestSuiteRunsPaginatedResponse
  property_count: 2
  slug: vapi-testsuiterunspaginatedresponse
- name: TestSuiteRunTestAttempt
  property_count: 4
  slug: vapi-testsuiteruntestattempt
- name: TestSuiteRunTestAttemptCall
  property_count: 1
  slug: vapi-testsuiteruntestattemptcall
- name: TestSuiteRunTestAttemptMetadata
  property_count: 1
  slug: vapi-testsuiteruntestattemptmetadata
- name: TestSuiteRunTestResult
  property_count: 2
  slug: vapi-testsuiteruntestresult
- name: TestSuitesPaginatedResponse
  property_count: 2
  slug: vapi-testsuitespaginatedresponse
- name: TestSuiteTestChat
  property_count: 10
  slug: vapi-testsuitetestchat
- name: TestSuiteTestScorerAI
  property_count: 2
  slug: vapi-testsuitetestscorerai
- name: TestSuiteTestsPaginatedResponse
  property_count: 2
  slug: vapi-testsuitetestspaginatedresponse
- name: TestSuiteTestVoice
  property_count: 10
  slug: vapi-testsuitetestvoice
- name: TextContent
  property_count: 3
  slug: vapi-textcontent
- name: TextEditorTool
  property_count: 10
  slug: vapi-texteditortool
- name: TextEditorToolWithToolCall
  property_count: 7
  slug: vapi-texteditortoolwithtoolcall
- name: TextInsight
  property_count: 10
  slug: vapi-textinsight
- name: TextInsightFromCallTable
  property_count: 5
  slug: vapi-textinsightfromcalltable
- name: TimeRange
  property_count: 4
  slug: vapi-timerange
- name: TogetherAICredential
  property_count: 7
  slug: vapi-togetheraicredential
- name: TogetherAIModel
  property_count: 10
  slug: vapi-togetheraimodel
- name: Token
  property_count: 8
  slug: vapi-token
- name: TokenRestrictions
  property_count: 4
  slug: vapi-tokenrestrictions
- name: ToolCall
  property_count: 3
  slug: vapi-toolcall
- name: ToolCallFunction
  property_count: 2
  slug: vapi-toolcallfunction
- name: ToolCallHookAction
  property_count: 3
  slug: vapi-toolcallhookaction
- name: ToolCallMessage
  property_count: 5
  slug: vapi-toolcallmessage
- name: ToolCallResult
  property_count: 6
  slug: vapi-toolcallresult
- name: ToolCallResultMessage
  property_count: 8
  slug: vapi-toolcallresultmessage
- name: ToolCallResultMessageWarning
  property_count: 3
  slug: vapi-toolcallresultmessagewarning
- name: ToolMessage
  property_count: 5
  slug: vapi-toolmessage
- name: ToolMessageComplete
  property_count: 6
  slug: vapi-toolmessagecomplete
- name: ToolMessageDelayed
  property_count: 5
  slug: vapi-toolmessagedelayed
- name: ToolMessageFailed
  property_count: 5
  slug: vapi-toolmessagefailed
- name: ToolMessageStart
  property_count: 5
  slug: vapi-toolmessagestart
- name: ToolNode
  property_count: 6
  slug: vapi-toolnode
- name: ToolParameter
  property_count: 2
  slug: vapi-toolparameter
- name: ToolRejectionPlan
  property_count: 1
  slug: vapi-toolrejectionplan
- name: ToolTemplateMetadata
  property_count: 3
  slug: vapi-tooltemplatemetadata
- name: ToolTemplateSetup
  property_count: 4
  slug: vapi-tooltemplatesetup
- name: TranscriberCost
  property_count: 4
  slug: vapi-transcribercost
- name: TranscriptionEndpointingPlan
  property_count: 3
  slug: vapi-transcriptionendpointingplan
- name: TranscriptPlan
  property_count: 3
  slug: vapi-transcriptplan
- name: TransferAssistant
  property_count: 11
  slug: vapi-transferassistant
- name: TransferAssistantModel
  property_count: 4
  slug: vapi-transferassistantmodel
- name: TransferCallTool
  property_count: 8
  slug: vapi-transfercalltool
- name: TransferCancelToolUserEditable
  property_count: 3
  slug: vapi-transfercanceltoolusereditable
- name: TransferDestinationAssistant
  property_count: 5
  slug: vapi-transferdestinationassistant
- name: TransferDestinationNumber
  property_count: 8
  slug: vapi-transferdestinationnumber
- name: TransferDestinationSip
  property_count: 7
  slug: vapi-transferdestinationsip
- name: TransferFallbackPlan
  property_count: 2
  slug: vapi-transferfallbackplan
- name: TransferHookAction
  property_count: 2
  slug: vapi-transferhookaction
- name: TransferPhoneNumberHookAction
  property_count: 2
  slug: vapi-transferphonenumberhookaction
- name: TransferPlan
  property_count: 12
  slug: vapi-transferplan
- name: TransferSuccessfulToolUserEditable
  property_count: 3
  slug: vapi-transfersuccessfultoolusereditable
- name: TransportConfigurationTwilio
  property_count: 4
  slug: vapi-transportconfigurationtwilio
- name: TransportCost
  property_count: 4
  slug: vapi-transportcost
- name: TurnLatency
  property_count: 5
  slug: vapi-turnlatency
- name: TwilioCredential
  property_count: 10
  slug: vapi-twiliocredential
- name: TwilioPhoneNumber
  property_count: 19
  slug: vapi-twiliophonenumber
- name: TwilioSMSChatTransport
  property_count: 6
  slug: vapi-twiliosmschattransport
- name: TwilioTransportMessage
  property_count: 2
  slug: vapi-twiliotransportmessage
- name: TwilioVoicemailDetectionPlan
  property_count: 7
  slug: vapi-twiliovoicemaildetectionplan
- name: UpdateAnthropicBedrockCredentialDTO
  property_count: 3
  slug: vapi-updateanthropicbedrockcredentialdto
- name: UpdateAnthropicCredentialDTO
  property_count: 2
  slug: vapi-updateanthropiccredentialdto
- name: UpdateAnyscaleCredentialDTO
  property_count: 2
  slug: vapi-updateanyscalecredentialdto
- name: UpdateApiRequestToolDTO
  property_count: 14
  slug: vapi-updateapirequesttooldto
- name: UpdateAssemblyAICredentialDTO
  property_count: 2
  slug: vapi-updateassemblyaicredentialdto
- name: UpdateAssistantDTO
  property_count: 31
  slug: vapi-updateassistantdto
- name: UpdateAzureCredentialDTO
  property_count: 6
  slug: vapi-updateazurecredentialdto
- name: UpdateAzureOpenAICredentialDTO
  property_count: 6
  slug: vapi-updateazureopenaicredentialdto
- name: UpdateBarInsightFromCallTableDTO
  property_count: 7
  slug: vapi-updatebarinsightfromcalltabledto
- name: UpdateBashToolDTO
  property_count: 5
  slug: vapi-updatebashtooldto
- name: UpdateByoPhoneNumberDTO
  property_count: 10
  slug: vapi-updatebyophonenumberdto
- name: UpdateByoSipTrunkCredentialDTO
  property_count: 7
  slug: vapi-updatebyosiptrunkcredentialdto
- name: UpdateCallDTO
  property_count: 1
  slug: vapi-updatecalldto
- name: UpdateCampaignDTO
  property_count: 8
  slug: vapi-updatecampaigndto
- name: UpdateCartesiaCredentialDTO
  property_count: 3
  slug: vapi-updatecartesiacredentialdto
- name: UpdateCerebrasCredentialDTO
  property_count: 2
  slug: vapi-updatecerebrascredentialdto
- name: UpdateCloudflareCredentialDTO
  property_count: 6
  slug: vapi-updatecloudflarecredentialdto
- name: UpdateCodeToolDTO
  property_count: 10
  slug: vapi-updatecodetooldto
- name: UpdateComputerToolDTO
  property_count: 8
  slug: vapi-updatecomputertooldto
- name: UpdateCustomCredentialDTO
  property_count: 3
  slug: vapi-updatecustomcredentialdto
- name: UpdateCustomKnowledgeBaseDTO
  property_count: 1
  slug: vapi-updatecustomknowledgebasedto
- name: UpdateCustomLLMCredentialDTO
  property_count: 3
  slug: vapi-updatecustomllmcredentialdto
- name: UpdateDeepgramCredentialDTO
  property_count: 3
  slug: vapi-updatedeepgramcredentialdto
- name: UpdateDeepInfraCredentialDTO
  property_count: 2
  slug: vapi-updatedeepinfracredentialdto
- name: UpdateDeepSeekCredentialDTO
  property_count: 2
  slug: vapi-updatedeepseekcredentialdto
- name: UpdateDtmfToolDTO
  property_count: 3
  slug: vapi-updatedtmftooldto
- name: UpdateElevenLabsCredentialDTO
  property_count: 2
  slug: vapi-updateelevenlabscredentialdto
- name: UpdateEmailCredentialDTO
  property_count: 2
  slug: vapi-updateemailcredentialdto
- name: UpdateEndCallToolDTO
  property_count: 2
  slug: vapi-updateendcalltooldto
- name: UpdateEvalDTO
  property_count: 4
  slug: vapi-updateevaldto
- name: UpdateFileDTO
  property_count: 1
  slug: vapi-updatefiledto
- name: UpdateFunctionToolDTO
  property_count: 7
  slug: vapi-updatefunctiontooldto
- name: UpdateGcpCredentialDTO
  property_count: 5
  slug: vapi-updategcpcredentialdto
- name: UpdateGhlToolDTO
  property_count: 3
  slug: vapi-updateghltooldto
- name: UpdateGladiaCredentialDTO
  property_count: 2
  slug: vapi-updategladiacredentialdto
- name: UpdateGoHighLevelCalendarAvailabilityToolDTO
  property_count: 2
  slug: vapi-updategohighlevelcalendaravailabilitytooldto
- name: UpdateGoHighLevelCalendarEventCreateToolDTO
  property_count: 2
  slug: vapi-updategohighlevelcalendareventcreatetooldto
- name: UpdateGoHighLevelContactCreateToolDTO
  property_count: 2
  slug: vapi-updategohighlevelcontactcreatetooldto
- name: UpdateGoHighLevelContactGetToolDTO
  property_count: 2
  slug: vapi-updategohighlevelcontactgettooldto
- name: UpdateGoHighLevelCredentialDTO
  property_count: 2
  slug: vapi-updategohighlevelcredentialdto
- name: UpdateGoHighLevelMCPCredentialDTO
  property_count: 2
  slug: vapi-updategohighlevelmcpcredentialdto
- name: UpdateGoogleCalendarCheckAvailabilityToolDTO
  property_count: 2
  slug: vapi-updategooglecalendarcheckavailabilitytooldto
- name: UpdateGoogleCalendarCreateEventToolDTO
  property_count: 2
  slug: vapi-updategooglecalendarcreateeventtooldto
- name: UpdateGoogleCalendarOAuth2AuthorizationCredentialDTO
  property_count: 2
  slug: vapi-updategooglecalendaroauth2authorizationcredentialdto
- name: UpdateGoogleCalendarOAuth2ClientCredentialDTO
  property_count: 1
  slug: vapi-updategooglecalendaroauth2clientcredentialdto
- name: UpdateGoogleCredentialDTO
  property_count: 2
  slug: vapi-updategooglecredentialdto
- name: UpdateGoogleSheetsOAuth2AuthorizationCredentialDTO
  property_count: 2
  slug: vapi-updategooglesheetsoauth2authorizationcredentialdto
- name: UpdateGoogleSheetsRowAppendToolDTO
  property_count: 2
  slug: vapi-updategooglesheetsrowappendtooldto
- name: UpdateGroqCredentialDTO
  property_count: 2
  slug: vapi-updategroqcredentialdto
- name: UpdateHandoffToolDTO
  property_count: 5
  slug: vapi-updatehandofftooldto
- name: UpdateHumeCredentialDTO
  property_count: 2
  slug: vapi-updatehumecredentialdto
- name: UpdateInflectionAICredentialDTO
  property_count: 2
  slug: vapi-updateinflectionaicredentialdto
- name: UpdateInworldCredentialDTO
  property_count: 2
  slug: vapi-updateinworldcredentialdto
- name: UpdateLangfuseCredentialDTO
  property_count: 4
  slug: vapi-updatelangfusecredentialdto
- name: UpdateLineInsightFromCallTableDTO
  property_count: 7
  slug: vapi-updatelineinsightfromcalltabledto
- name: UpdateLmntCredentialDTO
  property_count: 2
  slug: vapi-updatelmntcredentialdto
- name: UpdateMakeCredentialDTO
  property_count: 4
  slug: vapi-updatemakecredentialdto
- name: UpdateMakeToolDTO
  property_count: 3
  slug: vapi-updatemaketooldto
- name: UpdateMcpToolDTO
  property_count: 5
  slug: vapi-updatemcptooldto
- name: UpdateMistralCredentialDTO
  property_count: 2
  slug: vapi-updatemistralcredentialdto
- name: UpdateNeuphonicCredentialDTO
  property_count: 2
  slug: vapi-updateneuphoniccredentialdto
- name: UpdateOpenAICredentialDTO
  property_count: 2
  slug: vapi-updateopenaicredentialdto
- name: UpdateOpenRouterCredentialDTO
  property_count: 2
  slug: vapi-updateopenroutercredentialdto
- name: UpdateOrgDTO
  property_count: 8
  slug: vapi-updateorgdto
- name: UpdateOutputToolDTO
  property_count: 2
  slug: vapi-updateoutputtooldto
- name: UpdatePerplexityAICredentialDTO
  property_count: 2
  slug: vapi-updateperplexityaicredentialdto
- name: UpdatePersonalityDTO
  property_count: 3
  slug: vapi-updatepersonalitydto
- name: UpdatePieInsightFromCallTableDTO
  property_count: 6
  slug: vapi-updatepieinsightfromcalltabledto
- name: UpdatePlayHTCredentialDTO
  property_count: 3
  slug: vapi-updateplayhtcredentialdto
- name: UpdateQueryToolDTO
  property_count: 3
  slug: vapi-updatequerytooldto
- name: UpdateRimeAICredentialDTO
  property_count: 2
  slug: vapi-updaterimeaicredentialdto
- name: UpdateRunpodCredentialDTO
  property_count: 2
  slug: vapi-updaterunpodcredentialdto
- name: UpdateS3CredentialDTO
  property_count: 7
  slug: vapi-updates3credentialdto
- name: UpdateScenarioDTO
  property_count: 7
  slug: vapi-updatescenariodto
- name: UpdateScorecardDTO
  property_count: 4
  slug: vapi-updatescorecarddto
- name: UpdateSessionDTO
  property_count: 4
  slug: vapi-updatesessiondto
- name: UpdateSimulationDTO
  property_count: 4
  slug: vapi-updatesimulationdto
- name: UpdateSimulationSuiteDTO
  property_count: 4
  slug: vapi-updatesimulationsuitedto
- name: UpdateSipRequestToolDTO
  property_count: 5
  slug: vapi-updatesiprequesttooldto
- name: UpdateSlackOAuth2AuthorizationCredentialDTO
  property_count: 2
  slug: vapi-updateslackoauth2authorizationcredentialdto
- name: UpdateSlackSendMessageToolDTO
  property_count: 2
  slug: vapi-updateslacksendmessagetooldto
- name: UpdateSlackWebhookCredentialDTO
  property_count: 2
  slug: vapi-updateslackwebhookcredentialdto
- name: UpdateSmsToolDTO
  property_count: 2
  slug: vapi-updatesmstooldto
- name: UpdateSonioxCredentialDTO
  property_count: 3
  slug: vapi-updatesonioxcredentialdto
- name: UpdateSquadDTO
  property_count: 3
  slug: vapi-updatesquaddto
- name: UpdateStructuredOutputDTO
  property_count: 9
  slug: vapi-updatestructuredoutputdto
- name: UpdateTelnyxPhoneNumberDTO
  property_count: 9
  slug: vapi-updatetelnyxphonenumberdto
- name: UpdateTestSuiteDto
  property_count: 4
  slug: vapi-updatetestsuitedto
- name: UpdateTestSuiteRunDto
  property_count: 1
  slug: vapi-updatetestsuiterundto
- name: UpdateTestSuiteTestChatDto
  property_count: 5
  slug: vapi-updatetestsuitetestchatdto
- name: UpdateTestSuiteTestVoiceDto
  property_count: 5
  slug: vapi-updatetestsuitetestvoicedto
- name: UpdateTextEditorToolDTO
  property_count: 5
  slug: vapi-updatetexteditortooldto
- name: UpdateTextInsightFromCallTableDTO
  property_count: 5
  slug: vapi-updatetextinsightfromcalltabledto
- name: UpdateTogetherAICredentialDTO
  property_count: 2
  slug: vapi-updatetogetheraicredentialdto
- name: UpdateTokenDTO
  property_count: 3
  slug: vapi-updatetokendto
- name: UpdateToolTemplateDTO
  property_count: 7
  slug: vapi-updatetooltemplatedto
- name: UpdateTransferCallToolDTO
  property_count: 3
  slug: vapi-updatetransfercalltooldto
- name: UpdateTwilioCredentialDTO
  property_count: 5
  slug: vapi-updatetwiliocredentialdto
- name: UpdateTwilioPhoneNumberDTO
  property_count: 13
  slug: vapi-updatetwiliophonenumberdto
- name: UpdateUserRoleDTO
  property_count: 2
  slug: vapi-updateuserroledto
- name: UpdateVapiPhoneNumberDTO
  property_count: 9
  slug: vapi-updatevapiphonenumberdto
- name: UpdateVoicemailToolDTO
  property_count: 3
  slug: vapi-updatevoicemailtooldto
- name: UpdateVonageCredentialDTO
  property_count: 3
  slug: vapi-updatevonagecredentialdto
- name: UpdateVonagePhoneNumberDTO
  property_count: 9
  slug: vapi-updatevonagephonenumberdto
- name: UpdateWebhookCredentialDTO
  property_count: 2
  slug: vapi-updatewebhookcredentialdto
- name: UpdateWellSaidCredentialDTO
  property_count: 2
  slug: vapi-updatewellsaidcredentialdto
- name: UpdateWorkflowDTO
  property_count: 24
  slug: vapi-updateworkflowdto
- name: UpdateXAiCredentialDTO
  property_count: 2
  slug: vapi-updatexaicredentialdto
- name: User
  property_count: 5
  slug: vapi-user
- name: UserMessage
  property_count: 11
  slug: vapi-usermessage
- name: VapiCost
  property_count: 4
  slug: vapi-vapicost
- name: VapiModel
  property_count: 12
  slug: vapi-vapimodel
- name: VapiPhoneNumber
  property_count: 17
  slug: vapi-vapiphonenumber
- name: VapiPronunciationDictionaryLocator
  property_count: 2
  slug: vapi-vapipronunciationdictionarylocator
- name: VapiSipTransportMessage
  property_count: 4
  slug: vapi-vapisiptransportmessage
- name: VapiSmartEndpointingPlan
  property_count: 1
  slug: vapi-vapismartendpointingplan
- name: VapiVoice
  property_count: 7
  slug: vapi-vapivoice
- name: VapiVoicemailDetectionPlan
  property_count: 4
  slug: vapi-vapivoicemaildetectionplan
- name: VariableExtractionAlias
  property_count: 2
  slug: vapi-variableextractionalias
- name: VariableExtractionPlan
  property_count: 2
  slug: vapi-variableextractionplan
- name: VariableValueGroupBy
  property_count: 1
  slug: vapi-variablevaluegroupby
- name: VoiceCost
  property_count: 4
  slug: vapi-voicecost
- name: VoiceLibrary
  property_count: 20
  slug: vapi-voicelibrary
- name: VoiceLibraryVoiceResponse
  property_count: 7
  slug: vapi-voicelibraryvoiceresponse
- name: VoicemailDetectionBackoffPlan
  property_count: 3
  slug: vapi-voicemaildetectionbackoffplan
- name: VoicemailDetectionCost
  property_count: 8
  slug: vapi-voicemaildetectioncost
- name: VoicemailTool
  property_count: 8
  slug: vapi-voicemailtool
- name: VonageCredential
  property_count: 10
  slug: vapi-vonagecredential
- name: VonagePhoneNumber
  property_count: 15
  slug: vapi-vonagephonenumber
- name: WebChat
  property_count: 3
  slug: vapi-webchat
- name: WebhookCredential
  property_count: 8
  slug: vapi-webhookcredential
- name: WellSaidCredential
  property_count: 7
  slug: vapi-wellsaidcredential
- name: WellSaidVoice
  property_count: 8
  slug: vapi-wellsaidvoice
- name: Workflow
  property_count: 28
  slug: vapi-workflow
- name: WorkflowAnthropicBedrockModel
  property_count: 5
  slug: vapi-workflowanthropicbedrockmodel
- name: WorkflowAnthropicModel
  property_count: 5
  slug: vapi-workflowanthropicmodel
- name: WorkflowCustomModel
  property_count: 8
  slug: vapi-workflowcustommodel
- name: WorkflowGoogleModel
  property_count: 4
  slug: vapi-workflowgooglemodel
- name: WorkflowOpenAIModel
  property_count: 4
  slug: vapi-workflowopenaimodel
- name: WorkflowOverrides
  property_count: 1
  slug: vapi-workflowoverrides
- name: WorkflowUserEditable
  property_count: 24
  slug: vapi-workflowusereditable
- name: XAiCredential
  property_count: 7
  slug: vapi-xaicredential
- name: XaiModel
  property_count: 10
  slug: vapi-xaimodel
- name: XSSSecurityFilter
  property_count: 1
  slug: vapi-xsssecurityfilter
json_structures:
- name: Vapi Structure
  property_count: 0
  slug: vapi-structure
layout: provider
modified: '2026-05-19'
name: Vapi
nav: Providers
network: true
overview: 'Vapi publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Assistants API, Calls API, and 12 more. Tagged areas include Artificial Intelligence, Voice, Agents, Real-Time, and CPaaS.


  The Vapi catalog on APIs.io includes 1 Spectral governance ruleset.


  Vapi''s developer surface includes authentication, documentation, and 12 more developer resources.'
plans:
- name: Vapi Plans Pricing
  plan_count: 2
  slug: vapi-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Vapi Rate Limits
  slug: vapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Vapi API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vapi-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.3
    catalog_earned_first_party: 0.0
    catalog_gap: 67.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 9.8
    contract_quality: 51.6
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vapi/refs/heads/main/screenshots/vapi-2026-06-20T200920.png
security:
- kind: authentication
  name: Vapi Authentication
  slug: vapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vapi Domain Security
  slug: vapi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Vapi Trust Center
  slug: vapi-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: vapi
tags:
- Artificial Intelligence
- Voice
- Agents
- Real-Time
- CPaaS
website: https://vapi.ai/
---
