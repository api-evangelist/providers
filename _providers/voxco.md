---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 35
  human_in_the_loop: 0
  name: Voxco Agentic Access
  operation_count: 53
  slug: voxco-agentic-access
  summary_line: 53 operations · 35 acting
api_count: 11
apis:
- description: The AICoder API from Voxco — 15 operation(s) for aicoder.
  name: Voxco AICoder API
  slug: voxco-aicoder-api
- description: The Codebooks API from Voxco — 5 operation(s) for codebooks.
  name: Voxco Codebooks API
  slug: voxco-codebooks-api
- description: The Companies API from Voxco — 1 operation(s) for companies.
  name: Voxco Companies API
  slug: voxco-companies-api
- description: The Exports API from Voxco — 2 operation(s) for exports.
  name: Voxco Exports API
  slug: voxco-exports-api
- description: The Languages API from Voxco — 1 operation(s) for languages.
  name: Voxco Languages API
  slug: voxco-languages-api
- description: The Questions API from Voxco — 7 operation(s) for questions.
  name: Voxco Questions API
  slug: voxco-questions-api
- description: The Responses API from Voxco — 4 operation(s) for responses.
  name: Voxco Responses API
  slug: voxco-responses-api
- description: The Sessions API from Voxco — 1 operation(s) for sessions.
  name: Voxco Sessions API
  slug: voxco-sessions-api
- description: The Studies API from Voxco — 3 operation(s) for studies.
  name: Voxco Studies API
  slug: voxco-studies-api
- description: The StudyRespondents API from Voxco — 1 operation(s) for studyrespondents.
  name: Voxco StudyRespondents API
  slug: voxco-studyrespondents-api
- description: The Users API from Voxco — 1 operation(s) for users.
  name: Voxco Users API
  slug: voxco-users-api
artifact_total: 243
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/voxco-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voxco-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/voxco-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.voxco.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.voxco.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.voxco.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.voxco.com/pricing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voxco
- group: other
  title: ''
  type: X
  url: https://x.com/voxco
- group: commercial
  title: ''
  type: Plans
  url: plans/voxco-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/voxco-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/voxco-finops.yml
created: '2026-06-13'
description: Voxco is an omnichannel survey platform serving market research firms and corporate research teams across 40+ countries. It provides a REST API for managing surveys, distributing questionnaires via multiple channels (online, CATI, mobile, IVR), collecting responses, and accessing survey analytics. The Ascribe text analytics API further enables AI-powered coding and analysis of open-ended survey responses.
examples:
- key_count: 2
  name: Delete Codebooks_{Codebookkey}_Codes Request
  slug: delete-Codebooks_{codebookKey}_Codes-request
- key_count: 4
  name: Delete Codebooks_{Codebookkey}_Codes Response 200
  slug: delete-Codebooks_{codebookKey}_Codes-response-200
- key_count: 2
  name: Delete Questions_Batch Request
  slug: delete-Questions_Batch-request
- key_count: 4
  name: Delete Questions_Batch Response 200
  slug: delete-Questions_Batch-response-200
- key_count: 3
  name: Delete Questions_{Questionkey}_{Entitytype} Response 200
  slug: delete-Questions_{questionKey}_{entityType}-response-200
- key_count: 1
  name: Delete Responses_Batch Request
  slug: delete-Responses_Batch-request
- key_count: 2
  name: Delete Responses_Batch Response 200
  slug: delete-Responses_Batch-response-200
- key_count: 1
  name: Delete Responses_{Questionkey}_{Respondentid} Response 200
  slug: delete-Responses_{QuestionKey}_{RespondentID}-response-200
- key_count: 1
  name: Delete Studies Request
  slug: delete-Studies-request
- key_count: 1
  name: Delete Studies Response 200
  slug: delete-Studies-response-200
- key_count: 1
  name: Delete Studies_{Studykey}_Respondents Request
  slug: delete-Studies_{studyKey}_Respondents-request
- key_count: 3
  name: Delete Studies_{Studykey}_Respondents Response 200
  slug: delete-Studies_{studyKey}_Respondents-response-200
- key_count: 2
  name: Get Aicoder_Analyze_Codebooks Response 200
  slug: get-AICoder_Analyze_Codebooks-response-200
- key_count: 3
  name: Get Aicoder_Analyze_{Taskstatuskey} Response 200
  slug: get-AICoder_Analyze_{taskStatusKey}-response-200
- key_count: 2
  name: Get Aicoder_Export_Codebook_{Taskstatuskey} Response 200
  slug: get-AICoder_Export_Codebook_{taskStatusKey}-response-200
- key_count: 3
  name: Get Aicoder_Export_Dichotomous_{Taskstatuskey} Response 200
  slug: get-AICoder_Export_Dichotomous_{taskStatusKey}-response-200
- key_count: 3
  name: Get Aicoder_Export_Excel_{Taskstatuskey} Response 200
  slug: get-AICoder_Export_Excel_{taskStatusKey}-response-200
- key_count: 2
  name: Get Aicoder_Netcodes_{Taskstatuskey} Response 200
  slug: get-AICoder_NetCodes_{taskStatusKey}-response-200
- key_count: 2
  name: Get Aicoder_Projects Response 200
  slug: get-AICoder_Projects-response-200
- key_count: 3
  name: Get Codebooks_Question_{Questionkey} Response 200
  slug: get-Codebooks_Question_{questionKey}-response-200
- key_count: 3
  name: Get Codebooks_{Codebookkey} Response 200
  slug: get-Codebooks_{codebookKey}-response-200
- key_count: 2
  name: Get Companies Response 200
  slug: get-Companies-response-200
- key_count: 2
  name: Get Exports Response 200
  slug: get-Exports-response-200
- key_count: 11
  name: Get Exports_{Jobkey} Response 200
  slug: get-Exports_{jobKey}-response-200
- key_count: 2
  name: Get Languages_Translate Response 200
  slug: get-Languages_Translate-response-200
- key_count: 2
  name: Get Questions_{Studykey} Response 200
  slug: get-Questions_{studyKey}-response-200
- key_count: 2
  name: Get Responses_{Questionkey} Response 200
  slug: get-Responses_{questionKey}-response-200
- key_count: 2
  name: Get Studies Response 200
  slug: get-Studies-response-200
- key_count: 20
  name: Get Studies_{Studykey} Response 200
  slug: get-Studies_{studyKey}-response-200
- key_count: 2
  name: Get Users Response 200
  slug: get-Users-response-200
- key_count: 12
  name: Post Aicoder_Analyze Request
  slug: post-AICoder_Analyze-request
- key_count: 2
  name: Post Aicoder_Analyze Response 200
  slug: post-AICoder_Analyze-response-200
- key_count: 2
  name: Post Aicoder_Analyze_Incremental Request
  slug: post-AICoder_Analyze_Incremental-request
- key_count: 2
  name: Post Aicoder_Analyze_Incremental Response 200
  slug: post-AICoder_Analyze_Incremental-response-200
- key_count: 7
  name: Post Aicoder_Analyze_V3 Request
  slug: post-AICoder_Analyze_v3-request
- key_count: 2
  name: Post Aicoder_Analyze_V3 Response 200
  slug: post-AICoder_Analyze_v3-response-200
- key_count: 4
  name: Post Aicoder_Export_Codebook Request
  slug: post-AICoder_Export_Codebook-request
- key_count: 2
  name: Post Aicoder_Export_Codebook Response 200
  slug: post-AICoder_Export_Codebook-response-200
- key_count: 3
  name: Post Aicoder_Export_Dichotomous Request
  slug: post-AICoder_Export_Dichotomous-request
- key_count: 2
  name: Post Aicoder_Export_Dichotomous Response 200
  slug: post-AICoder_Export_Dichotomous-response-200
- key_count: 1
  name: Post Aicoder_Export_Excel Request
  slug: post-AICoder_Export_Excel-request
- key_count: 2
  name: Post Aicoder_Export_Excel Response 200
  slug: post-AICoder_Export_Excel-response-200
- key_count: 3
  name: Post Aicoder_Links Request
  slug: post-AICoder_Links-request
- key_count: 2
  name: Post Aicoder_Links Response 200
  slug: post-AICoder_Links-response-200
- key_count: 3
  name: Post Aicoder_Netcodes Request
  slug: post-AICoder_NetCodes-request
- key_count: 2
  name: Post Aicoder_Netcodes Response 200
  slug: post-AICoder_NetCodes-response-200
- key_count: 2
  name: Post Codebooks_Codes_Batch Request
  slug: post-Codebooks_Codes_Batch-request
- key_count: 2
  name: Post Codebooks_Codes_Batch Response 200
  slug: post-Codebooks_Codes_Batch-response-200
- key_count: 2
  name: Post Codebooks_{Codebookkey}_Codes Request
  slug: post-Codebooks_{codebookKey}_Codes-request
- key_count: 3
  name: Post Codebooks_{Codebookkey}_Codes Response 200
  slug: post-Codebooks_{codebookKey}_Codes-response-200
- key_count: 1
  name: Post Codebooks_{Questionkey} Request
  slug: post-Codebooks_{questionKey}-request
- key_count: 3
  name: Post Codebooks_{Questionkey} Response 200
  slug: post-Codebooks_{questionKey}-response-200
- key_count: 1
  name: Post Companies Request
  slug: post-Companies-request
- key_count: 3
  name: Post Companies Response 200
  slug: post-Companies-response-200
- key_count: 5
  name: Post Exports Request
  slug: post-Exports-request
- key_count: 2
  name: Post Exports Response 200
  slug: post-Exports-response-200
- key_count: 2
  name: Post Questions_Translate Request
  slug: post-Questions_Translate-request
- key_count: 6
  name: Post Questions_Translate Response 200
  slug: post-Questions_Translate-response-200
- key_count: 11
  name: Post Questions_{Studykey} Request
  slug: post-Questions_{studyKey}-request
- key_count: 13
  name: Post Questions_{Studykey} Response 200
  slug: post-Questions_{studyKey}-response-200
- key_count: 1
  name: Post Questions_{Studykey}_Batch Request
  slug: post-Questions_{studyKey}_Batch-request
- key_count: 4
  name: Post Questions_{Studykey}_Batch Response 200
  slug: post-Questions_{studyKey}_Batch-response-200
- key_count: 4
  name: Post Responses_{Questionkey} Request
  slug: post-Responses_{questionKey}-request
- key_count: 9
  name: Post Responses_{Questionkey} Response 200
  slug: post-Responses_{questionKey}-response-200
- key_count: 1
  name: Post Responses_{Studykey}_Batch Request
  slug: post-Responses_{studyKey}_Batch-request
- key_count: 2
  name: Post Responses_{Studykey}_Batch Response 200
  slug: post-Responses_{studyKey}_Batch-response-200
- key_count: 3
  name: Post Session_New Request
  slug: post-Session_New-request
- key_count: 3
  name: Post Session_New Response 200
  slug: post-Session_New-response-200
- key_count: 12
  name: Post Studies Request
  slug: post-Studies-request
- key_count: 20
  name: Post Studies Response 200
  slug: post-Studies-response-200
- key_count: 2
  name: Post Studies_Translate Request
  slug: post-Studies_Translate-request
- key_count: 2
  name: Post Studies_Translate Response 200
  slug: post-Studies_Translate-response-200
- key_count: 2
  name: Put Codebooks_{Codebookkey}_Codes Request
  slug: put-Codebooks_{codebookKey}_Codes-request
- key_count: 4
  name: Put Codebooks_{Codebookkey}_Codes Response 200
  slug: put-Codebooks_{codebookKey}_Codes-response-200
- key_count: 1
  name: Put Questions_{Studykey}_Batch Request
  slug: put-Questions_{studyKey}_Batch-request
- key_count: 3
  name: Put Questions_{Studykey}_Batch Response 200
  slug: put-Questions_{studyKey}_Batch-response-200
- key_count: 3
  name: Put Responses_{Questionkey} Request
  slug: put-Responses_{questionKey}-request
- key_count: 5
  name: Put Responses_{Questionkey} Response 200
  slug: put-Responses_{questionKey}-response-200
- key_count: 2
  name: Put Responses_{Studykey}_Batch Request
  slug: put-Responses_{studyKey}_Batch-request
- key_count: 2
  name: Put Responses_{Studykey}_Batch Response 200
  slug: put-Responses_{studyKey}_Batch-response-200
- key_count: 13
  name: Put Studies Request
  slug: put-Studies-request
- key_count: 20
  name: Put Studies Response 200
  slug: put-Studies-response-200
finops:
- name: Voxco Finops
  service_category: ''
  slug: voxco-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/voxco.png
json_schemas:
- name: AICoderAnalyzeGetCodebooksResponse
  property_count: 2
  slug: AICoderAnalyzeGetCodebooksResponse
- name: AICoderCodeStudyIncrementallyRequest
  property_count: 2
  slug: AICoderCodeStudyIncrementallyRequest
- name: AICoderCodeStudyIncrementallyResponse
  property_count: 2
  slug: AICoderCodeStudyIncrementallyResponse
- name: AICoderCodeStudyRequest
  property_count: 12
  slug: AICoderCodeStudyRequest
- name: AICoderCodeStudyResponse
  property_count: 2
  slug: AICoderCodeStudyResponse
- name: AICoderCodeStudyStatusOfTaskResponse
  property_count: 3
  slug: AICoderCodeStudyStatusOfTaskResponse
- name: AICoderCodeStudyV3Request
  property_count: 7
  slug: AICoderCodeStudyV3Request
- name: AICoderCodebookExportGetStatusOfTaskResponse
  property_count: 2
  slug: AICoderCodebookExportGetStatusOfTaskResponse
- name: AICoderCodebookExportRequest
  property_count: 4
  slug: AICoderCodebookExportRequest
- name: AICoderCodebookExportResponse
  property_count: 2
  slug: AICoderCodebookExportResponse
- name: AICoderCreateLinkRequest
  property_count: 3
  slug: AICoderCreateLinkRequest
- name: AICoderCreateLinkResponse
  property_count: 2
  slug: AICoderCreateLinkResponse
- name: AICoderDichotomousExportGetStatusOfTaskResponse
  property_count: 3
  slug: AICoderDichotomousExportGetStatusOfTaskResponse
- name: AICoderDichotomousExportRequest
  property_count: 3
  slug: AICoderDichotomousExportRequest
- name: AICoderDichotomousExportResponse
  property_count: 2
  slug: AICoderDichotomousExportResponse
- name: AICoderExcelExportGetStatusOfTaskResponse
  property_count: 3
  slug: AICoderExcelExportGetStatusOfTaskResponse
- name: AICoderExcelExportRequest
  property_count: 1
  slug: AICoderExcelExportRequest
- name: AICoderExcelExportResponse
  property_count: 2
  slug: AICoderExcelExportResponse
- name: AICoderGetProjectsTaskResponse
  property_count: 2
  slug: AICoderGetProjectsTaskResponse
- name: AICoderGroupCodesRequest
  property_count: 3
  slug: AICoderGroupCodesRequest
- name: AICoderGroupCodesResponse
  property_count: 2
  slug: AICoderGroupCodesResponse
- name: AICoderGroupCodesStatusOfTaskResponse
  property_count: 2
  slug: AICoderGroupCodesStatusOfTaskResponse
- name: AICoderLink
  property_count: 3
  slug: AICoderLink
- name: AICoderProjectAPI
  property_count: 11
  slug: AICoderProjectAPI
- name: AddCodesIntoCodebookRequest
  property_count: 2
  slug: AddCodesIntoCodebookRequest
- name: AddCodesIntoCodebookResponse
  property_count: 3
  slug: AddCodesIntoCodebookResponse
- name: AddCodesIntoCodebooksBatchRequest
  property_count: 2
  slug: AddCodesIntoCodebooksBatchRequest
- name: AddCodesIntoCodebooksBatchResponse
  property_count: 2
  slug: AddCodesIntoCodebooksBatchResponse
- name: AddCodesIntoCodebooksBatchResultItem
  property_count: 3
  slug: AddCodesIntoCodebooksBatchResultItem
- name: AddedCode
  property_count: 2
  slug: AddedCode
- name: AddedResponseBatchResult
  property_count: 3
  slug: AddedResponseBatchResult
- name: AddedResponseWithCodingInfo
  property_count: 6
  slug: AddedResponseWithCodingInfo
- name: AnalyzeByClosedEndCodesOption
  property_count: 2
  slug: AnalyzeByClosedEndCodesOption
- name: AnalyzeByClosedEndOption
  property_count: 2
  slug: AnalyzeByClosedEndOption
- name: AssignSegmentSiblingsOptions
  property_count: 3
  slug: AssignSegmentSiblingsOptions
- name: AssignTopSegmentsOptions
  property_count: 3
  slug: AssignTopSegmentsOptions
- name: AutoCodeQuestionRequest
  property_count: 3
  slug: AutoCodeQuestionRequest
- name: AutoCodeQuestionResponse
  property_count: 2
  slug: AutoCodeQuestionResponse
- name: CodeOrNet
  property_count: 7
  slug: CodeOrNet
- name: CodebookAIOptions
  property_count: 4
  slug: CodebookAIOptions
- name: CodebookBuilderCreationMethod
  property_count: 0
  slug: CodebookBuilderCreationMethod
- name: CodebookBuilderV3Options
  property_count: 7
  slug: CodebookBuilderV3Options
- name: CodebookGranularityOption
  property_count: 0
  slug: CodebookGranularityOption
- name: CodebookInitialOptions
  property_count: 3
  slug: CodebookInitialOptions
- name: CodebookItem
  property_count: 2
  slug: CodebookItem
- name: CodebookNewCodes
  property_count: 2
  slug: CodebookNewCodes
- name: Company
  property_count: 2
  slug: Company
- name: CreateCodebookForQuestionRequest
  property_count: 1
  slug: CreateCodebookForQuestionRequest
- name: CreateCodebookForQuestionResponse
  property_count: 3
  slug: CreateCodebookForQuestionResponse
- name: CreateNewCompanyRequest
  property_count: 1
  slug: CreateNewCompanyRequest
- name: CreateNewCompanyResponse
  property_count: 3
  slug: CreateNewCompanyResponse
- name: CreateQuestionRequest
  property_count: 11
  slug: CreateQuestionRequest
- name: CreateQuestionResponse
  property_count: 13
  slug: CreateQuestionResponse
- name: CreateQuestionsBatchRequest
  property_count: 1
  slug: CreateQuestionsBatchRequest
- name: CreateQuestionsBatchResponse
  property_count: 4
  slug: CreateQuestionsBatchResponse
- name: DBJobStatus
  property_count: 0
  slug: DBJobStatus
- name: DBJobType
  property_count: 0
  slug: DBJobType
- name: DBQuestionCodingSource
  property_count: 0
  slug: DBQuestionCodingSource
- name: DBQuestionTypes
  property_count: 0
  slug: DBQuestionTypes
- name: DBScriptParameterType
  property_count: 0
  slug: DBScriptParameterType
- name: DBScriptPurpose
  property_count: 0
  slug: DBScriptPurpose
- name: DeleteCodebookCodesRequest
  property_count: 2
  slug: DeleteCodebookCodesRequest
- name: DeleteCodebookCodesResponse
  property_count: 4
  slug: DeleteCodebookCodesResponse
- name: DeleteQuestionResponse
  property_count: 3
  slug: DeleteQuestionResponse
- name: DeleteQuestionResponseResultItem
  property_count: 3
  slug: DeleteQuestionResponseResultItem
- name: DeleteQuestionResponses
  property_count: 2
  slug: DeleteQuestionResponses
- name: DeleteQuestionsBatchRequest
  property_count: 2
  slug: DeleteQuestionsBatchRequest
- name: DeleteQuestionsBatchResponse
  property_count: 4
  slug: DeleteQuestionsBatchResponse
- name: DeleteQuestionsBatchResult
  property_count: 2
  slug: DeleteQuestionsBatchResult
- name: DeleteResponseResponse
  property_count: 1
  slug: DeleteResponseResponse
- name: DeleteResponsesBatchRequest
  property_count: 1
  slug: DeleteResponsesBatchRequest
- name: DeleteResponsesBatchResponse
  property_count: 2
  slug: DeleteResponsesBatchResponse
- name: DeleteStudyRequest
  property_count: 1
  slug: DeleteStudyRequest
- name: DeleteStudyRespondentFailure
  property_count: 2
  slug: DeleteStudyRespondentFailure
- name: DeleteStudyRespondentsRequest
  property_count: 1
  slug: DeleteStudyRespondentsRequest
- name: DeleteStudyRespondentsResponse
  property_count: 3
  slug: DeleteStudyRespondentsResponse
- name: DeleteStudyResponse
  property_count: 1
  slug: DeleteStudyResponse
- name: EnhancedThemeExtractorOptions
  property_count: 5
  slug: EnhancedThemeExtractorOptions
- name: ExistingCodebookOptions
  property_count: 3
  slug: ExistingCodebookOptions
- name: ExistingResponse
  property_count: 6
  slug: ExistingResponse
- name: ExportToCoderType
  property_count: 0
  slug: ExportToCoderType
- name: ExportsJobStatusResponse
  property_count: 11
  slug: ExportsJobStatusResponse
- name: ExportsRequest
  property_count: 5
  slug: ExportsRequest
- name: ExportsResponse
  property_count: 2
  slug: ExportsResponse
- name: FailedCode
  property_count: 2
  slug: FailedCode
- name: FailedQuestionIdBatch
  property_count: 2
  slug: FailedQuestionIdBatch
- name: FailedQuestionKeyBatch
  property_count: 2
  slug: FailedQuestionKeyBatch
- name: GenerativeAIOptions
  property_count: 2
  slug: GenerativeAIOptions
- name: GetCodebookResponse
  property_count: 3
  slug: GetCodebookResponse
- name: GetCompaniesResponse
  property_count: 2
  slug: GetCompaniesResponse
- name: GetLanguagesToTranslateResponse
  property_count: 2
  slug: GetLanguagesToTranslateResponse
- name: GetQuestionCodebookResponse
  property_count: 3
  slug: GetQuestionCodebookResponse
- name: GetQuestionsResponse
  property_count: 2
  slug: GetQuestionsResponse
- name: GetResponsesResponse
  property_count: 2
  slug: GetResponsesResponse
- name: GetScriptsResponse
  property_count: 2
  slug: GetScriptsResponse
- name: GetStudiesResponse
  property_count: 2
  slug: GetStudiesResponse
- name: GetStudyResponse
  property_count: 20
  slug: GetStudyResponse
- name: GetUsersResponse
  property_count: 2
  slug: GetUsersResponse
- name: MergeSimilarOptions
  property_count: 2
  slug: MergeSimilarOptions
- name: NaturalLanguage
  property_count: 2
  slug: NaturalLanguage
- name: NewCodeOrNet
  property_count: 6
  slug: NewCodeOrNet
- name: NewSessionRequest
  property_count: 3
  slug: NewSessionRequest
- name: NewSessionResponse
  property_count: 3
  slug: NewSessionResponse
- name: NewStudyRequest
  property_count: 12
  slug: NewStudyRequest
- name: NewStudyResponse
  property_count: 20
  slug: NewStudyResponse
- name: NonGenerativeAIOptions
  property_count: 3
  slug: NonGenerativeAIOptions
- name: PostQuestionResponses
  property_count: 2
  slug: PostQuestionResponses
- name: PostResponse
  property_count: 7
  slug: PostResponse
- name: PostResponseBatch
  property_count: 5
  slug: PostResponseBatch
- name: PostResponsesBatchRequest
  property_count: 1
  slug: PostResponsesBatchRequest
- name: PostResponsesBatchResponse
  property_count: 2
  slug: PostResponsesBatchResponse
- name: PostResponsesRequest
  property_count: 4
  slug: PostResponsesRequest
- name: PostResponsesResponse
  property_count: 9
  slug: PostResponsesResponse
- name: PutQuestionResponses
  property_count: 2
  slug: PutQuestionResponses
- name: PutResponse
  property_count: 7
  slug: PutResponse
- name: PutResponseBatch
  property_count: 5
  slug: PutResponseBatch
- name: PutResponsesBatchRequest
  property_count: 2
  slug: PutResponsesBatchRequest
- name: PutResponsesBatchResponse
  property_count: 2
  slug: PutResponsesBatchResponse
- name: PutResponsesBatchResult
  property_count: 6
  slug: PutResponsesBatchResult
- name: PutResponsesRequest
  property_count: 3
  slug: PutResponsesRequest
- name: PutResponsesResponse
  property_count: 5
  slug: PutResponsesResponse
- name: Question
  property_count: 17
  slug: Question
- name: ResponseCodeRemoved
  property_count: 5
  slug: ResponseCodeRemoved
- name: ScriptDefinition
  property_count: 9
  slug: ScriptDefinition
- name: ScriptParameter
  property_count: 7
  slug: ScriptParameter
- name: SegmentCode
  property_count: 3
  slug: SegmentCode
- name: SetQuestionCodebookResponse
  property_count: 1
  slug: SetQuestionCodebookResponse
- name: Study
  property_count: 14
  slug: Study
- name: TaskTypes
  property_count: 0
  slug: TaskTypes
- name: TranslateQuestionRequest
  property_count: 2
  slug: TranslateQuestionRequest
- name: TranslateQuestionResponse
  property_count: 6
  slug: TranslateQuestionResponse
- name: TranslateStudyRequest
  property_count: 2
  slug: TranslateStudyRequest
- name: TranslateStudyResponse
  property_count: 5
  slug: TranslateStudyResponse
- name: UpdateCode
  property_count: 6
  slug: UpdateCode
- name: UpdateCodesInCodebookRequest
  property_count: 2
  slug: UpdateCodesInCodebookRequest
- name: UpdateCodesInCodebookResponse
  property_count: 4
  slug: UpdateCodesInCodebookResponse
- name: UpdateQuestionBatch
  property_count: 11
  slug: UpdateQuestionBatch
- name: UpdateQuestionsBatchRequest
  property_count: 1
  slug: UpdateQuestionsBatchRequest
- name: UpdateQuestionsBatchResponse
  property_count: 3
  slug: UpdateQuestionsBatchResponse
- name: UpdateStudyRequest
  property_count: 13
  slug: UpdateStudyRequest
- name: UpdateStudyResponse
  property_count: 20
  slug: UpdateStudyResponse
- name: User
  property_count: 2
  slug: User
jsonld:
- class_count: 1
  name: Voxco Context
  property_count: 80
  slug: voxco-context
layout: provider
modified: '2026-06-13'
name: Voxco
nav: Providers
network: true
overview: 'Voxco publishes 11 APIs on the [APIs.io](https://apis.io/) network, including AICoder API, Codebooks API, Companies API, and 8 more. Tagged areas include Survey Software, Market Research, CATI, Omnichannel, and Text Analytics.


  The Voxco catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Voxco''s developer surface includes authentication, documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Voxco Plans Pricing
  plan_count: 5
  slug: voxco-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Voxco Rate Limits
  slug: voxco-rate-limits
rules:
- name: Voxco API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: voxco-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.3
  delta: -4.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voxco/refs/heads/main/screenshots/voxco-2026-06-20T201139.png
security:
- kind: authentication
  name: Voxco Authentication
  slug: voxco-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Voxco Domain Security
  slug: voxco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voxco
tags:
- Survey Software
- Market Research
- CATI
- Omnichannel
- Text Analytics
- Data Collection
- Panel Management
website: https://www.voxco.com
---
