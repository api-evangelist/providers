---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 62
  human_in_the_loop: 6
  name: Kombo Agentic Access
  operation_count: 121
  slug: kombo-agentic-access
  summary_line: 121 operations · 62 acting · 6 human-in-the-loop
api_count: 8
apis:
- description: Endpoints for AI-powered job application features.
  name: Kombo AI Apply API
  slug: kombo-ai-apply-api
- description: Custom integration-specific endpoints.
  name: Kombo Custom Endpoints API
  slug: kombo-custom-endpoints-api
- description: The General API from Kombo — 12 operation(s) for general.
  name: Kombo General API
  slug: kombo-general-api
- description: Endpoints for Kombo Connect, our end-user-facing flow for setting up new integrations.
  name: Kombo Kombo Connect API
  slug: kombo-kombo-connect-api
- description: Unified endpoints to access all the ATS concepts you might need.
  name: Kombo Unified ATS API API
  slug: kombo-unified-ats-api-api
- description: Unified endpoints to operate Assessments and Background Checks for many applicant tracking systems.
  name: Kombo Unified ATS (Assessment & Background Check) API API
  slug: kombo-unified-ats-assessment-background-check-api-api
- description: Unified endpoints to access all the HR concepts you might need.
  name: Kombo Unified HRIS API API
  slug: kombo-unified-hris-api-api
- description: Unified endpoints to access all the LMS concepts you might need.
  name: Kombo Unified LMS API API
  slug: kombo-unified-lms-api-api
artifact_total: 670
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kombo AI Apply API
  slug: open-kombo-ai-apply-api
- collection_type: open
  name: Kombo AI Apply Custom Endpoints API
  slug: open-kombo-custom-endpoints-api
- collection_type: open
  name: Kombo AI Apply General API
  slug: open-kombo-general-api
- collection_type: open
  name: Kombo AI Apply Kombo Connect API
  slug: open-kombo-kombo-connect-api
- collection_type: open
  name: Kombo AI Apply Unified ATS API API
  slug: open-kombo-unified-ats-api-api
- collection_type: open
  name: Kombo AI Apply Unified ATS (Assessment & Background Check) API API
  slug: open-kombo-unified-ats-assessment-background-check-api-api
- collection_type: open
  name: Kombo AI Apply Unified HRIS API API
  slug: open-kombo-unified-hris-api-api
- collection_type: open
  name: Kombo AI Apply Unified LMS API API
  slug: open-kombo-unified-lms-api-api
- collection_type: open
  name: Kombo API
  slug: open-kombo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kombo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kombo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kombo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kombo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kombo-api
- group: company
  title: ''
  type: Website
  url: https://www.kombo.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kombo.dev
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.kombo.dev/openapi.json
- group: build
  title: ''
  type: SDKs
  url: https://kombo.dev/libraries-and-sdks
- group: auth
  title: ''
  type: Security
  url: https://security.kombo.dev
- group: operate
  title: ''
  type: Support
  url: mailto:support@kombo.dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kombo-api
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.kombo.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.kombo.dev/blog
created: '2026-03-16'
description: Kombo is a unified API for HR and ATS integrations, enabling B2B SaaS companies to connect with HRIS, payroll, recruiting, and learning systems through a single integration.
examples:
- key_count: 6
  name: Kombo Deleteatscandidatescandidateidtags Example
  slug: kombo-deleteatscandidatescandidateidtags-example
- key_count: 6
  name: Kombo Deleteatscustomaviontesyncedjobsjobremoteid Example
  slug: kombo-deleteatscustomaviontesyncedjobsjobremoteid-example
- key_count: 6
  name: Kombo Deletehrisabsencesabsenceid Example
  slug: kombo-deletehrisabsencesabsenceid-example
- key_count: 6
  name: Kombo Deletehrisemployeeskillassignmentsemployeeskillassignmentid Example
  slug: kombo-deletehrisemployeeskillassignmentsemployeeskillassignmentid-example
- key_count: 6
  name: Kombo Deletehrisskillsskillid Example
  slug: kombo-deletehrisskillsskillid-example
- key_count: 6
  name: Kombo Getaiapplyapplications Example
  slug: kombo-getaiapplyapplications-example
- key_count: 6
  name: Kombo Getaiapplycareersites Example
  slug: kombo-getaiapplycareersites-example
- key_count: 6
  name: Kombo Getaiapplyjobfeeds Example
  slug: kombo-getaiapplyjobfeeds-example
- key_count: 6
  name: Kombo Getaiapplypostings Example
  slug: kombo-getaiapplypostings-example
- key_count: 6
  name: Kombo Getassessmentpackages Example
  slug: kombo-getassessmentpackages-example
- key_count: 6
  name: Kombo Getatsactionsatsaddapplicationattachment Example
  slug: kombo-getatsactionsatsaddapplicationattachment-example
- key_count: 6
  name: Kombo Getatsactionsatsaddcandidateattachment Example
  slug: kombo-getatsactionsatsaddcandidateattachment-example
- key_count: 6
  name: Kombo Getatsactionsatscreateapplication Example
  slug: kombo-getatsactionsatscreateapplication-example
- key_count: 6
  name: Kombo Getatsactionsatscreatecandidate Example
  slug: kombo-getatsactionsatscreatecandidate-example
- key_count: 6
  name: Kombo Getatsapplications Example
  slug: kombo-getatsapplications-example
- key_count: 6
  name: Kombo Getatsapplicationsapplicationidattachments Example
  slug: kombo-getatsapplicationsapplicationidattachments-example
- key_count: 6
  name: Kombo Getatsapplicationstages Example
  slug: kombo-getatsapplicationstages-example
- key_count: 6
  name: Kombo Getatscandidates Example
  slug: kombo-getatscandidates-example
- key_count: 6
  name: Kombo Getatscandidatescandidateidattachments Example
  slug: kombo-getatscandidatescandidateidattachments-example
- key_count: 6
  name: Kombo Getatsinterviews Example
  slug: kombo-getatsinterviews-example
- key_count: 6
  name: Kombo Getatsjobs Example
  slug: kombo-getatsjobs-example
- key_count: 6
  name: Kombo Getatsoffers Example
  slug: kombo-getatsoffers-example
- key_count: 6
  name: Kombo Getatsrejectionreasons Example
  slug: kombo-getatsrejectionreasons-example
- key_count: 6
  name: Kombo Getatsroles Example
  slug: kombo-getatsroles-example
- key_count: 6
  name: Kombo Getatstags Example
  slug: kombo-getatstags-example
- key_count: 6
  name: Kombo Getatsusers Example
  slug: kombo-getatsusers-example
- key_count: 6
  name: Kombo Getcheckapikey Example
  slug: kombo-getcheckapikey-example
- key_count: 6
  name: Kombo Getconnectintegrationbytokentoken Example
  slug: kombo-getconnectintegrationbytokentoken-example
- key_count: 6
  name: Kombo Getcustomdatevavailabledocuments Example
  slug: kombo-getcustomdatevavailabledocuments-example
- key_count: 6
  name: Kombo Getcustomdatevsysteminformation Example
  slug: kombo-getcustomdatevsysteminformation-example
- key_count: 6
  name: Kombo Gethrisabsences Example
  slug: kombo-gethrisabsences-example
- key_count: 6
  name: Kombo Gethrisabsencetypes Example
  slug: kombo-gethrisabsencetypes-example
- key_count: 6
  name: Kombo Gethrisemployeedocumentcategories Example
  slug: kombo-gethrisemployeedocumentcategories-example
- key_count: 6
  name: Kombo Gethrisemployees Example
  slug: kombo-gethrisemployees-example
- key_count: 6
  name: Kombo Gethrisemployeesform Example
  slug: kombo-gethrisemployeesform-example
- key_count: 6
  name: Kombo Gethrisemployeeskillassignments Example
  slug: kombo-gethrisemployeeskillassignments-example
- key_count: 6
  name: Kombo Gethrisemployments Example
  slug: kombo-gethrisemployments-example
- key_count: 6
  name: Kombo Gethrisgroups Example
  slug: kombo-gethrisgroups-example
- key_count: 6
  name: Kombo Gethrislegalentities Example
  slug: kombo-gethrislegalentities-example
- key_count: 6
  name: Kombo Gethrislocations Example
  slug: kombo-gethrislocations-example
- key_count: 6
  name: Kombo Gethrisperformancereviewcycles Example
  slug: kombo-gethrisperformancereviewcycles-example
- key_count: 6
  name: Kombo Gethrisperformancereviews Example
  slug: kombo-gethrisperformancereviews-example
- key_count: 6
  name: Kombo Gethrisskills Example
  slug: kombo-gethrisskills-example
- key_count: 6
  name: Kombo Gethrisstaffingentities Example
  slug: kombo-gethrisstaffingentities-example
- key_count: 6
  name: Kombo Gethristeams Example
  slug: kombo-gethristeams-example
- key_count: 6
  name: Kombo Gethristimeoffbalances Example
  slug: kombo-gethristimeoffbalances-example
- key_count: 6
  name: Kombo Gethristimesheets Example
  slug: kombo-gethristimesheets-example
- key_count: 6
  name: Kombo Getintegrationsintegrationid Example
  slug: kombo-getintegrationsintegrationid-example
- key_count: 6
  name: Kombo Getintegrationsintegrationidcustomfields Example
  slug: kombo-getintegrationsintegrationidcustomfields-example
- key_count: 6
  name: Kombo Getintegrationsintegrationidintegrationfields Example
  slug: kombo-getintegrationsintegrationidintegrationfields-example
- key_count: 6
  name: Kombo Getlmscourseprogressions Example
  slug: kombo-getlmscourseprogressions-example
- key_count: 6
  name: Kombo Getlmscourses Example
  slug: kombo-getlmscourses-example
- key_count: 6
  name: Kombo Getlmsskills Example
  slug: kombo-getlmsskills-example
- key_count: 6
  name: Kombo Getlmsusers Example
  slug: kombo-getlmsusers-example
- key_count: 6
  name: Kombo Gettoolscategory Example
  slug: kombo-gettoolscategory-example
- key_count: 6
  name: Kombo Patchhrisemployeesemployeeid Example
  slug: kombo-patchhrisemployeesemployeeid-example
- key_count: 6
  name: Kombo Patchhrisemployeeskillassignmentsemployeeskillassignmentid Example
  slug: kombo-patchhrisemployeeskillassignmentsemployeeskillassignmentid-example
- key_count: 6
  name: Kombo Patchhrisskillsskillid Example
  slug: kombo-patchhrisskillsskillid-example
- key_count: 6
  name: Kombo Patchintegrationsintegrationidintegrationfieldsintegrationfi Example
  slug: kombo-patchintegrationsintegrationidintegrationfieldsintegrationfi-example
- key_count: 6
  name: Kombo Postaiapplyapply Example
  slug: kombo-postaiapplyapply-example
- key_count: 6
  name: Kombo Postaiapplycareersites Example
  slug: kombo-postaiapplycareersites-example
- key_count: 6
  name: Kombo Postaiapplyjobfeeds Example
  slug: kombo-postaiapplyjobfeeds-example
- key_count: 6
  name: Kombo Postaiapplyjobfeedsbulkimport Example
  slug: kombo-postaiapplyjobfeedsbulkimport-example
- key_count: 6
  name: Kombo Postaiapplypostings Example
  slug: kombo-postaiapplypostings-example
- key_count: 6
  name: Kombo Postaiapplypostingspostingidinquire Example
  slug: kombo-postaiapplypostingspostingidinquire-example
- key_count: 6
  name: Kombo Postaiapplyunifiedapijobsjobidapplications Example
  slug: kombo-postaiapplyunifiedapijobsjobidapplications-example
- key_count: 6
  name: Kombo Postatsapplicationsapplicationidattachments Example
  slug: kombo-postatsapplicationsapplicationidattachments-example
- key_count: 6
  name: Kombo Postatsapplicationsapplicationidnotes Example
  slug: kombo-postatsapplicationsapplicationidnotes-example
- key_count: 6
  name: Kombo Postatsapplicationsapplicationidreject Example
  slug: kombo-postatsapplicationsapplicationidreject-example
- key_count: 6
  name: Kombo Postatsapplicationsapplicationidresultlinks Example
  slug: kombo-postatsapplicationsapplicationidresultlinks-example
- key_count: 6
  name: Kombo Postatscandidates Example
  slug: kombo-postatscandidates-example
- key_count: 6
  name: Kombo Postatscandidatescandidateidattachments Example
  slug: kombo-postatscandidatescandidateidattachments-example
- key_count: 6
  name: Kombo Postatscandidatescandidateidresultlinks Example
  slug: kombo-postatscandidatescandidateidresultlinks-example
- key_count: 6
  name: Kombo Postatscandidatescandidateidtags Example
  slug: kombo-postatscandidatescandidateidtags-example
- key_count: 6
  name: Kombo Postatscustomaviontesyncedjobs Example
  slug: kombo-postatscustomaviontesyncedjobs-example
- key_count: 6
  name: Kombo Postatsimporttrackedapplication Example
  slug: kombo-postatsimporttrackedapplication-example
- key_count: 6
  name: Kombo Postatsjobsjobidapplications Example
  slug: kombo-postatsjobsjobidapplications-example
- key_count: 6
  name: Kombo Postconnectactivateintegration Example
  slug: kombo-postconnectactivateintegration-example
- key_count: 6
  name: Kombo Postconnectcreatelink Example
  slug: kombo-postconnectcreatelink-example
- key_count: 6
  name: Kombo Postcustomdatevdownloaddocument Example
  slug: kombo-postcustomdatevdownloaddocument-example
- key_count: 6
  name: Kombo Postcustomdatevemployeesemployeeiddownloaddocument Example
  slug: kombo-postcustomdatevemployeesemployeeiddownloaddocument-example
- key_count: 6
  name: Kombo Postcustomdatevemployeesemployeeideaurequests Example
  slug: kombo-postcustomdatevemployeesemployeeideaurequests-example
- key_count: 6
  name: Kombo Postcustomdatevpassthrough Example
  slug: kombo-postcustomdatevpassthrough-example
- key_count: 6
  name: Kombo Postcustomdatevpushdatageneral Example
  slug: kombo-postcustomdatevpushdatageneral-example
- key_count: 6
  name: Kombo Postcustomdatevpushdatapayroll Example
  slug: kombo-postcustomdatevpushdatapayroll-example
- key_count: 6
  name: Kombo Postcustomsilaeemployeesemployeeidpayrollsupplements Example
  slug: kombo-postcustomsilaeemployeesemployeeidpayrollsupplements-example
- key_count: 6
  name: Kombo Postforcesync Example
  slug: kombo-postforcesync-example
- key_count: 6
  name: Kombo Posthrisabsences Example
  slug: kombo-posthrisabsences-example
- key_count: 6
  name: Kombo Posthrisemployees Example
  slug: kombo-posthrisemployees-example
- key_count: 6
  name: Kombo Posthrisemployeesemployeeiddocuments Example
  slug: kombo-posthrisemployeesemployeeiddocuments-example
- key_count: 6
  name: Kombo Posthrisemployeesform Example
  slug: kombo-posthrisemployeesform-example
- key_count: 6
  name: Kombo Posthrisemployeeskillassignments Example
  slug: kombo-posthrisemployeeskillassignments-example
- key_count: 6
  name: Kombo Posthrisprovisioninggroupsgroupiddiff Example
  slug: kombo-posthrisprovisioninggroupsgroupiddiff-example
- key_count: 6
  name: Kombo Posthrisprovisioninggroupsgroupidsetuplinks Example
  slug: kombo-posthrisprovisioninggroupsgroupidsetuplinks-example
- key_count: 6
  name: Kombo Posthrisskills Example
  slug: kombo-posthrisskills-example
- key_count: 6
  name: Kombo Postintegrationsintegrationidrelink Example
  slug: kombo-postintegrationsintegrationidrelink-example
- key_count: 6
  name: Kombo Postintegrationsintegrationidsetuplink Example
  slug: kombo-postintegrationsintegrationidsetuplink-example
- key_count: 6
  name: Kombo Postlmscourseprogressions Example
  slug: kombo-postlmscourseprogressions-example
- key_count: 6
  name: Kombo Postlmscourseprogressionscourseprogressionidcomplete Example
  slug: kombo-postlmscourseprogressionscourseprogressionidcomplete-example
- key_count: 6
  name: Kombo Postlmscoursesbulk Example
  slug: kombo-postlmscoursesbulk-example
- key_count: 6
  name: Kombo Postlmscoursescourseiddeactivate Example
  slug: kombo-postlmscoursescourseiddeactivate-example
- key_count: 6
  name: Kombo Postpassthroughtoolapi Example
  slug: kombo-postpassthroughtoolapi-example
- key_count: 6
  name: Kombo Putassessmentordersassessmentorderidresult Example
  slug: kombo-putassessmentordersassessmentorderidresult-example
- key_count: 6
  name: Kombo Putassessmentpackages Example
  slug: kombo-putassessmentpackages-example
- key_count: 6
  name: Kombo Putatsapplicationsapplicationidstage Example
  slug: kombo-putatsapplicationsapplicationidstage-example
- key_count: 6
  name: Kombo Putcustomdatevemployeesemployeeidcompensations Example
  slug: kombo-putcustomdatevemployeesemployeeidcompensations-example
- key_count: 6
  name: Kombo Putcustomdatevemployeesemployeeidpreparepayroll Example
  slug: kombo-putcustomdatevemployeesemployeeidpreparepayroll-example
- key_count: 6
  name: Kombo Putintegrationsintegrationidcustomfieldscustomfieldid Example
  slug: kombo-putintegrationsintegrationidcustomfieldscustomfieldid-example
finops:
- name: Kombo Finops
  service_category: HR Tech / Unified API
  slug: kombo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kombo.png
json_schemas:
- name: AiApplyApplicationStatusUpdatedWebhookPayload
  property_count: 3
  slug: kombo-aiapplyapplicationstatusupdatedwebhookpayload
- name: AiApplyJobPostingStatusUpdatedWebhookPayload
  property_count: 3
  slug: kombo-aiapplyjobpostingstatusupdatedwebhookpayload
- name: AssessmentOrderReceivedWebhookPayload
  property_count: 3
  slug: kombo-assessmentorderreceivedwebhookpayload
- name: BulkImportJobPostingInput
  property_count: 4
  slug: kombo-bulkimportjobpostinginput
- name: BulkImportJobPostingLocation
  property_count: 2
  slug: kombo-bulkimportjobpostinglocation
- name: BulkImportResponse
  property_count: 2
  slug: kombo-bulkimportresponse
- name: ConnectionFlowFailedWebhookPayload
  property_count: 3
  slug: kombo-connectionflowfailedwebhookpayload
- name: DataChangedWebhookPayload
  property_count: 3
  slug: kombo-datachangedwebhookpayload
- name: DeleteAtsCandidatesCandidateIdTagsParameterCandidateId
  property_count: 0
  slug: kombo-deleteatscandidatescandidateidtagsparametercandidateid
- name: DeleteAtsCandidatesCandidateIdTagsPositiveResponse
  property_count: 3
  slug: kombo-deleteatscandidatescandidateidtagspositiveresponse
- name: DeleteAtsCandidatesCandidateIdTagsRequestBody
  property_count: 2
  slug: kombo-deleteatscandidatescandidateidtagsrequestbody
- name: DeleteAtsCustomAvionteSyncedJobsJobRemoteIdParameterJobRemoteId
  property_count: 0
  slug: kombo-deleteatscustomaviontesyncedjobsjobremoteidparameterjobremot
- name: DeleteAtsCustomAvionteSyncedJobsJobRemoteIdPositiveResponse
  property_count: 2
  slug: kombo-deleteatscustomaviontesyncedjobsjobremoteidpositiveresponse
- name: DeleteAtsCustomAvionteSyncedJobsJobRemoteIdRequestBody
  property_count: 0
  slug: kombo-deleteatscustomaviontesyncedjobsjobremoteidrequestbody
- name: DeleteHrisAbsencesAbsenceIdParameterAbsenceId
  property_count: 0
  slug: kombo-deletehrisabsencesabsenceidparameterabsenceid
- name: DeleteHrisAbsencesAbsenceIdPositiveResponse
  property_count: 3
  slug: kombo-deletehrisabsencesabsenceidpositiveresponse
- name: DeleteHrisAbsencesAbsenceIdRequestBody
  property_count: 1
  slug: kombo-deletehrisabsencesabsenceidrequestbody
- name: DeleteHrisEmployeeSkillAssignmentsEmployeeSkillAssignmentIdParameterEmployeeSkillAssignmentId
  property_count: 0
  slug: kombo-deletehrisemployeeskillassignmentsemployeeskillassignmentidp
- name: DeleteHrisEmployeeSkillAssignmentsEmployeeSkillAssignmentIdRequestBody
  property_count: 0
  slug: kombo-deletehrisemployeeskillassignmentsemployeeskillassignmentidr
- name: DeleteHrisSkillsSkillIdParameterSkillId
  property_count: 0
  slug: kombo-deletehrisskillsskillidparameterskillid
- name: DeleteHrisSkillsSkillIdPositiveResponse
  property_count: 2
  slug: kombo-deletehrisskillsskillidpositiveresponse
- name: DeleteHrisSkillsSkillIdRequestBody
  property_count: 0
  slug: kombo-deletehrisskillsskillidrequestbody
- name: DeleteIntegrationsIntegrationIdParameterIntegrationId
  property_count: 0
  slug: kombo-deleteintegrationsintegrationidparameterintegrationid
- name: DeleteIntegrationsIntegrationIdPositiveResponse
  property_count: 2
  slug: kombo-deleteintegrationsintegrationidpositiveresponse
- name: DeleteIntegrationsIntegrationIdRequestBody
  property_count: 0
  slug: kombo-deleteintegrationsintegrationidrequestbody
- name: GetAiApplyApplicationsParameterCursor
  property_count: 0
  slug: kombo-getaiapplyapplicationsparametercursor
- name: GetAiApplyApplicationsParameterIds
  property_count: 0
  slug: kombo-getaiapplyapplicationsparameterids
- name: GetAiApplyApplicationsParameterJobPostingIds
  property_count: 0
  slug: kombo-getaiapplyapplicationsparameterjobpostingids
- name: GetAiApplyApplicationsParameterPageSize
  property_count: 0
  slug: kombo-getaiapplyapplicationsparameterpagesize
- name: GetAiApplyApplicationsPositiveResponse
  property_count: 2
  slug: kombo-getaiapplyapplicationspositiveresponse
- name: GetAiApplyCareerSitesParameterCursor
  property_count: 0
  slug: kombo-getaiapplycareersitesparametercursor
- name: GetAiApplyCareerSitesParameterIds
  property_count: 0
  slug: kombo-getaiapplycareersitesparameterids
- name: GetAiApplyCareerSitesParameterPageSize
  property_count: 0
  slug: kombo-getaiapplycareersitesparameterpagesize
- name: GetAiApplyCareerSitesPositiveResponse
  property_count: 2
  slug: kombo-getaiapplycareersitespositiveresponse
- name: GetAiApplyJobFeedsParameterCursor
  property_count: 0
  slug: kombo-getaiapplyjobfeedsparametercursor
- name: GetAiApplyJobFeedsParameterIds
  property_count: 0
  slug: kombo-getaiapplyjobfeedsparameterids
- name: GetAiApplyJobFeedsParameterPageSize
  property_count: 0
  slug: kombo-getaiapplyjobfeedsparameterpagesize
- name: GetAiApplyJobFeedsPositiveResponse
  property_count: 2
  slug: kombo-getaiapplyjobfeedspositiveresponse
- name: GetAiApplyPostingsParameterCareerSiteIds
  property_count: 0
  slug: kombo-getaiapplypostingsparametercareersiteids
- name: GetAiApplyPostingsParameterCursor
  property_count: 0
  slug: kombo-getaiapplypostingsparametercursor
- name: GetAiApplyPostingsParameterIds
  property_count: 0
  slug: kombo-getaiapplypostingsparameterids
- name: GetAiApplyPostingsParameterJobCodes
  property_count: 0
  slug: kombo-getaiapplypostingsparameterjobcodes
- name: GetAiApplyPostingsParameterPageSize
  property_count: 0
  slug: kombo-getaiapplypostingsparameterpagesize
- name: GetAiApplyPostingsPositiveResponse
  property_count: 2
  slug: kombo-getaiapplypostingspositiveresponse
- name: GetAiApplyUnifiedApiJobsParameterCareerSiteIds
  property_count: 0
  slug: kombo-getaiapplyunifiedapijobsparametercareersiteids
- name: GetAiApplyUnifiedApiJobsParameterCursor
  property_count: 0
  slug: kombo-getaiapplyunifiedapijobsparametercursor
- name: GetAiApplyUnifiedApiJobsParameterIds
  property_count: 0
  slug: kombo-getaiapplyunifiedapijobsparameterids
- name: GetAiApplyUnifiedApiJobsParameterJobCodes
  property_count: 0
  slug: kombo-getaiapplyunifiedapijobsparameterjobcodes
- name: GetAiApplyUnifiedApiJobsParameterPageSize
  property_count: 0
  slug: kombo-getaiapplyunifiedapijobsparameterpagesize
- name: GetAiApplyUnifiedApiJobsParameterRemoteIds
  property_count: 0
  slug: kombo-getaiapplyunifiedapijobsparameterremoteids
- name: GetAiApplyUnifiedApiJobsPositiveResponse
  property_count: 2
  slug: kombo-getaiapplyunifiedapijobspositiveresponse
- name: GetAssessmentOrdersOpenParameterCursor
  property_count: 0
  slug: kombo-getassessmentordersopenparametercursor
- name: GetAssessmentOrdersOpenParameterPageSize
  property_count: 0
  slug: kombo-getassessmentordersopenparameterpagesize
- name: GetAssessmentOrdersOpenPositiveResponse
  property_count: 2
  slug: kombo-getassessmentordersopenpositiveresponse
- name: GetAssessmentOrdersParameterCreatedAfter
  property_count: 0
  slug: kombo-getassessmentordersparametercreatedafter
- name: GetAssessmentOrdersParameterCursor
  property_count: 0
  slug: kombo-getassessmentordersparametercursor
- name: GetAssessmentOrdersParameterIds
  property_count: 0
  slug: kombo-getassessmentordersparameterids
- name: GetAssessmentOrdersParameterPageSize
  property_count: 0
  slug: kombo-getassessmentordersparameterpagesize
- name: GetAssessmentOrdersParameterStatuses
  property_count: 0
  slug: kombo-getassessmentordersparameterstatuses
- name: GetAssessmentOrdersPositiveResponse
  property_count: 2
  slug: kombo-getassessmentorderspositiveresponse
- name: GetAssessmentPackagesPositiveResponse
  property_count: 2
  slug: kombo-getassessmentpackagespositiveresponse
- name: GetAtsActionsAtsAddApplicationAttachmentPositiveResponse
  property_count: 2
  slug: kombo-getatsactionsatsaddapplicationattachmentpositiveresponse
- name: GetAtsActionsAtsAddCandidateAttachmentPositiveResponse
  property_count: 2
  slug: kombo-getatsactionsatsaddcandidateattachmentpositiveresponse
- name: GetAtsActionsAtsCreateApplicationPositiveResponse
  property_count: 2
  slug: kombo-getatsactionsatscreateapplicationpositiveresponse
- name: GetAtsActionsAtsCreateCandidatePositiveResponse
  property_count: 2
  slug: kombo-getatsactionsatscreatecandidatepositiveresponse
- name: GetAtsApplicationsApplicationIdAttachmentsParameterApplicationId
  property_count: 0
  slug: kombo-getatsapplicationsapplicationidattachmentsparameterapplicati
- name: GetAtsApplicationsApplicationIdAttachmentsPositiveResponse
  property_count: 3
  slug: kombo-getatsapplicationsapplicationidattachmentspositiveresponse
- name: GetAtsApplicationsParameterCurrentStageIds
  property_count: 0
  slug: kombo-getatsapplicationsparametercurrentstageids
- name: GetAtsApplicationsParameterCursor
  property_count: 0
  slug: kombo-getatsapplicationsparametercursor
- name: GetAtsApplicationsParameterIds
  property_count: 0
  slug: kombo-getatsapplicationsparameterids
- name: GetAtsApplicationsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getatsapplicationsparameterignoreunsupportedfilters
- name: GetAtsApplicationsParameterIncludeDeleted
  property_count: 0
  slug: kombo-getatsapplicationsparameterincludedeleted
- name: GetAtsApplicationsParameterJobIds
  property_count: 0
  slug: kombo-getatsapplicationsparameterjobids
- name: GetAtsApplicationsParameterJobRemoteIds
  property_count: 0
  slug: kombo-getatsapplicationsparameterjobremoteids
- name: GetAtsApplicationsParameterOutcome
  property_count: 0
  slug: kombo-getatsapplicationsparameteroutcome
- name: GetAtsApplicationsParameterOutcomes
  property_count: 0
  slug: kombo-getatsapplicationsparameteroutcomes
- name: GetAtsApplicationsParameterPageSize
  property_count: 0
  slug: kombo-getatsapplicationsparameterpagesize
- name: GetAtsApplicationsParameterRemoteCreatedAfter
  property_count: 0
  slug: kombo-getatsapplicationsparameterremotecreatedafter
- name: GetAtsApplicationsParameterRemoteIds
  property_count: 0
  slug: kombo-getatsapplicationsparameterremoteids
- name: GetAtsApplicationsParameterUpdatedAfter
  property_count: 0
  slug: kombo-getatsapplicationsparameterupdatedafter
- name: GetAtsApplicationsPositiveResponse
  property_count: 2
  slug: kombo-getatsapplicationspositiveresponse
- name: GetAtsApplicationStagesParameterCursor
  property_count: 0
  slug: kombo-getatsapplicationstagesparametercursor
- name: GetAtsApplicationStagesParameterIds
  property_count: 0
  slug: kombo-getatsapplicationstagesparameterids
- name: GetAtsApplicationStagesParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getatsapplicationstagesparameterignoreunsupportedfilters
- name: GetAtsApplicationStagesParameterIncludeDeleted
  property_count: 0
  slug: kombo-getatsapplicationstagesparameterincludedeleted
- name: GetAtsApplicationStagesParameterPageSize
  property_count: 0
  slug: kombo-getatsapplicationstagesparameterpagesize
- name: GetAtsApplicationStagesParameterRemoteIds
  property_count: 0
  slug: kombo-getatsapplicationstagesparameterremoteids
- name: GetAtsApplicationStagesParameterUpdatedAfter
  property_count: 0
  slug: kombo-getatsapplicationstagesparameterupdatedafter
- name: GetAtsApplicationStagesPositiveResponse
  property_count: 2
  slug: kombo-getatsapplicationstagespositiveresponse
- name: GetAtsCandidatesCandidateIdAttachmentsParameterCandidateId
  property_count: 0
  slug: kombo-getatscandidatescandidateidattachmentsparametercandidateid
- name: GetAtsCandidatesCandidateIdAttachmentsPositiveResponse
  property_count: 3
  slug: kombo-getatscandidatescandidateidattachmentspositiveresponse
- name: GetAtsCandidatesParameterCursor
  property_count: 0
  slug: kombo-getatscandidatesparametercursor
- name: GetAtsCandidatesParameterEmail
  property_count: 0
  slug: kombo-getatscandidatesparameteremail
- name: GetAtsCandidatesParameterFirstName
  property_count: 0
  slug: kombo-getatscandidatesparameterfirstname
- name: GetAtsCandidatesParameterIds
  property_count: 0
  slug: kombo-getatscandidatesparameterids
- name: GetAtsCandidatesParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getatscandidatesparameterignoreunsupportedfilters
- name: GetAtsCandidatesParameterIncludeDeleted
  property_count: 0
  slug: kombo-getatscandidatesparameterincludedeleted
- name: GetAtsCandidatesParameterJobIds
  property_count: 0
  slug: kombo-getatscandidatesparameterjobids
- name: GetAtsCandidatesParameterLastName
  property_count: 0
  slug: kombo-getatscandidatesparameterlastname
- name: GetAtsCandidatesParameterPageSize
  property_count: 0
  slug: kombo-getatscandidatesparameterpagesize
- name: GetAtsCandidatesParameterRemoteIds
  property_count: 0
  slug: kombo-getatscandidatesparameterremoteids
- name: GetAtsCandidatesParameterUpdatedAfter
  property_count: 0
  slug: kombo-getatscandidatesparameterupdatedafter
- name: GetAtsCandidatesPositiveResponse
  property_count: 2
  slug: kombo-getatscandidatespositiveresponse
- name: GetAtsInterviewsParameterCursor
  property_count: 0
  slug: kombo-getatsinterviewsparametercursor
- name: GetAtsInterviewsParameterIds
  property_count: 0
  slug: kombo-getatsinterviewsparameterids
- name: GetAtsInterviewsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getatsinterviewsparameterignoreunsupportedfilters
- name: GetAtsInterviewsParameterIncludeDeleted
  property_count: 0
  slug: kombo-getatsinterviewsparameterincludedeleted
- name: GetAtsInterviewsParameterJobIds
  property_count: 0
  slug: kombo-getatsinterviewsparameterjobids
- name: GetAtsInterviewsParameterPageSize
  property_count: 0
  slug: kombo-getatsinterviewsparameterpagesize
- name: GetAtsInterviewsParameterRemoteIds
  property_count: 0
  slug: kombo-getatsinterviewsparameterremoteids
- name: GetAtsInterviewsParameterUpdatedAfter
  property_count: 0
  slug: kombo-getatsinterviewsparameterupdatedafter
- name: GetAtsInterviewsPositiveResponse
  property_count: 2
  slug: kombo-getatsinterviewspositiveresponse
- name: GetAtsJobsParameterCursor
  property_count: 0
  slug: kombo-getatsjobsparametercursor
- name: GetAtsJobsParameterEmploymentTypes
  property_count: 0
  slug: kombo-getatsjobsparameteremploymenttypes
- name: GetAtsJobsParameterIds
  property_count: 0
  slug: kombo-getatsjobsparameterids
- name: GetAtsJobsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getatsjobsparameterignoreunsupportedfilters
- name: GetAtsJobsParameterIncludeDeleted
  property_count: 0
  slug: kombo-getatsjobsparameterincludedeleted
- name: GetAtsJobsParameterJobCodes
  property_count: 0
  slug: kombo-getatsjobsparameterjobcodes
- name: GetAtsJobsParameterNameContains
  property_count: 0
  slug: kombo-getatsjobsparameternamecontains
- name: GetAtsJobsParameterPageSize
  property_count: 0
  slug: kombo-getatsjobsparameterpagesize
- name: GetAtsJobsParameterPostUrl
  property_count: 0
  slug: kombo-getatsjobsparameterposturl
- name: GetAtsJobsParameterRemoteCreatedAfter
  property_count: 0
  slug: kombo-getatsjobsparameterremotecreatedafter
- name: GetAtsJobsParameterRemoteIds
  property_count: 0
  slug: kombo-getatsjobsparameterremoteids
- name: GetAtsJobsParameterStatus
  property_count: 0
  slug: kombo-getatsjobsparameterstatus
- name: GetAtsJobsParameterStatuses
  property_count: 0
  slug: kombo-getatsjobsparameterstatuses
- name: GetAtsJobsParameterUpdatedAfter
  property_count: 0
  slug: kombo-getatsjobsparameterupdatedafter
- name: GetAtsJobsParameterVisibilities
  property_count: 0
  slug: kombo-getatsjobsparametervisibilities
- name: GetAtsJobsPositiveResponse
  property_count: 2
  slug: kombo-getatsjobspositiveresponse
- name: GetAtsOffersParameterCursor
  property_count: 0
  slug: kombo-getatsoffersparametercursor
- name: GetAtsOffersParameterIds
  property_count: 0
  slug: kombo-getatsoffersparameterids
- name: GetAtsOffersParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getatsoffersparameterignoreunsupportedfilters
- name: GetAtsOffersParameterIncludeDeleted
  property_count: 0
  slug: kombo-getatsoffersparameterincludedeleted
- name: GetAtsOffersParameterPageSize
  property_count: 0
  slug: kombo-getatsoffersparameterpagesize
- name: GetAtsOffersParameterRemoteIds
  property_count: 0
  slug: kombo-getatsoffersparameterremoteids
- name: GetAtsOffersParameterUpdatedAfter
  property_count: 0
  slug: kombo-getatsoffersparameterupdatedafter
- name: GetAtsOffersPositiveResponse
  property_count: 2
  slug: kombo-getatsofferspositiveresponse
- name: GetAtsRejectionReasonsParameterCursor
  property_count: 0
  slug: kombo-getatsrejectionreasonsparametercursor
- name: GetAtsRejectionReasonsParameterIds
  property_count: 0
  slug: kombo-getatsrejectionreasonsparameterids
- name: GetAtsRejectionReasonsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getatsrejectionreasonsparameterignoreunsupportedfilters
- name: GetAtsRejectionReasonsParameterIncludeDeleted
  property_count: 0
  slug: kombo-getatsrejectionreasonsparameterincludedeleted
- name: GetAtsRejectionReasonsParameterPageSize
  property_count: 0
  slug: kombo-getatsrejectionreasonsparameterpagesize
- name: GetAtsRejectionReasonsParameterRemoteIds
  property_count: 0
  slug: kombo-getatsrejectionreasonsparameterremoteids
- name: GetAtsRejectionReasonsParameterUpdatedAfter
  property_count: 0
  slug: kombo-getatsrejectionreasonsparameterupdatedafter
- name: GetAtsRejectionReasonsPositiveResponse
  property_count: 2
  slug: kombo-getatsrejectionreasonspositiveresponse
- name: GetAtsRolesParameterCursor
  property_count: 0
  slug: kombo-getatsrolesparametercursor
- name: GetAtsRolesParameterIds
  property_count: 0
  slug: kombo-getatsrolesparameterids
- name: GetAtsRolesParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getatsrolesparameterignoreunsupportedfilters
- name: GetAtsRolesParameterIncludeDeleted
  property_count: 0
  slug: kombo-getatsrolesparameterincludedeleted
- name: GetAtsRolesParameterPageSize
  property_count: 0
  slug: kombo-getatsrolesparameterpagesize
- name: GetAtsRolesParameterRemoteIds
  property_count: 0
  slug: kombo-getatsrolesparameterremoteids
- name: GetAtsRolesParameterScopes
  property_count: 0
  slug: kombo-getatsrolesparameterscopes
- name: GetAtsRolesParameterUpdatedAfter
  property_count: 0
  slug: kombo-getatsrolesparameterupdatedafter
- name: GetAtsRolesPositiveResponse
  property_count: 2
  slug: kombo-getatsrolespositiveresponse
- name: GetAtsTagsParameterCursor
  property_count: 0
  slug: kombo-getatstagsparametercursor
- name: GetAtsTagsParameterIds
  property_count: 0
  slug: kombo-getatstagsparameterids
- name: GetAtsTagsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getatstagsparameterignoreunsupportedfilters
- name: GetAtsTagsParameterIncludeDeleted
  property_count: 0
  slug: kombo-getatstagsparameterincludedeleted
- name: GetAtsTagsParameterPageSize
  property_count: 0
  slug: kombo-getatstagsparameterpagesize
- name: GetAtsTagsParameterRemoteIds
  property_count: 0
  slug: kombo-getatstagsparameterremoteids
- name: GetAtsTagsParameterUpdatedAfter
  property_count: 0
  slug: kombo-getatstagsparameterupdatedafter
- name: GetAtsTagsPositiveResponse
  property_count: 2
  slug: kombo-getatstagspositiveresponse
- name: GetAtsUsersParameterCursor
  property_count: 0
  slug: kombo-getatsusersparametercursor
- name: GetAtsUsersParameterEmails
  property_count: 0
  slug: kombo-getatsusersparameteremails
- name: GetAtsUsersParameterIds
  property_count: 0
  slug: kombo-getatsusersparameterids
- name: GetAtsUsersParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getatsusersparameterignoreunsupportedfilters
- name: GetAtsUsersParameterIncludeDeleted
  property_count: 0
  slug: kombo-getatsusersparameterincludedeleted
- name: GetAtsUsersParameterPageSize
  property_count: 0
  slug: kombo-getatsusersparameterpagesize
- name: GetAtsUsersParameterRemoteIds
  property_count: 0
  slug: kombo-getatsusersparameterremoteids
- name: GetAtsUsersParameterUpdatedAfter
  property_count: 0
  slug: kombo-getatsusersparameterupdatedafter
- name: GetAtsUsersPositiveResponse
  property_count: 2
  slug: kombo-getatsuserspositiveresponse
- name: GetCheckApiKeyPositiveResponse
  property_count: 2
  slug: kombo-getcheckapikeypositiveresponse
- name: GetConnectIntegrationByTokenTokenParameterToken
  property_count: 0
  slug: kombo-getconnectintegrationbytokentokenparametertoken
- name: GetConnectIntegrationByTokenTokenPositiveResponse
  property_count: 2
  slug: kombo-getconnectintegrationbytokentokenpositiveresponse
- name: GetCustomDatevAvailableDocumentsParameterPeriod
  property_count: 0
  slug: kombo-getcustomdatevavailabledocumentsparameterperiod
- name: GetCustomDatevAvailableDocumentsPositiveResponse
  property_count: 3
  slug: kombo-getcustomdatevavailabledocumentspositiveresponse
- name: GetCustomDatevCheckDocumentPermissionPositiveResponse
  property_count: 3
  slug: kombo-getcustomdatevcheckdocumentpermissionpositiveresponse
- name: GetCustomDatevCheckEauPermissionPositiveResponse
  property_count: 3
  slug: kombo-getcustomdatevcheckeaupermissionpositiveresponse
- name: GetCustomDatevCheckWritePermissionPositiveResponse
  property_count: 3
  slug: kombo-getcustomdatevcheckwritepermissionpositiveresponse
- name: GetCustomDatevDataPushesPositiveResponse
  property_count: 2
  slug: kombo-getcustomdatevdatapushespositiveresponse
- name: GetCustomDatevEauRequestsEauIdParameterEauId
  property_count: 0
  slug: kombo-getcustomdateveaurequestseauidparametereauid
- name: GetCustomDatevEauRequestsEauIdPositiveResponse
  property_count: 3
  slug: kombo-getcustomdateveaurequestseauidpositiveresponse
- name: GetCustomDatevSystemInformationPositiveResponse
  property_count: 2
  slug: kombo-getcustomdatevsysteminformationpositiveresponse
- name: GetHrisAbsencesParameterCursor
  property_count: 0
  slug: kombo-gethrisabsencesparametercursor
- name: GetHrisAbsencesParameterDateFrom
  property_count: 0
  slug: kombo-gethrisabsencesparameterdatefrom
- name: GetHrisAbsencesParameterDateUntil
  property_count: 0
  slug: kombo-gethrisabsencesparameterdateuntil
- name: GetHrisAbsencesParameterEmployeeId
  property_count: 0
  slug: kombo-gethrisabsencesparameteremployeeid
- name: GetHrisAbsencesParameterIds
  property_count: 0
  slug: kombo-gethrisabsencesparameterids
- name: GetHrisAbsencesParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethrisabsencesparameterignoreunsupportedfilters
- name: GetHrisAbsencesParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethrisabsencesparameterincludedeleted
- name: GetHrisAbsencesParameterPageSize
  property_count: 0
  slug: kombo-gethrisabsencesparameterpagesize
- name: GetHrisAbsencesParameterRemoteIds
  property_count: 0
  slug: kombo-gethrisabsencesparameterremoteids
- name: GetHrisAbsencesParameterTimeFrom
  property_count: 0
  slug: kombo-gethrisabsencesparametertimefrom
- name: GetHrisAbsencesParameterTimeUntil
  property_count: 0
  slug: kombo-gethrisabsencesparametertimeuntil
- name: GetHrisAbsencesParameterTypeIds
  property_count: 0
  slug: kombo-gethrisabsencesparametertypeids
- name: GetHrisAbsencesParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethrisabsencesparameterupdatedafter
- name: GetHrisAbsencesPositiveResponse
  property_count: 2
  slug: kombo-gethrisabsencespositiveresponse
- name: GetHrisAbsenceTypesParameterCursor
  property_count: 0
  slug: kombo-gethrisabsencetypesparametercursor
- name: GetHrisAbsenceTypesParameterIds
  property_count: 0
  slug: kombo-gethrisabsencetypesparameterids
- name: GetHrisAbsenceTypesParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethrisabsencetypesparameterignoreunsupportedfilters
- name: GetHrisAbsenceTypesParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethrisabsencetypesparameterincludedeleted
- name: GetHrisAbsenceTypesParameterPageSize
  property_count: 0
  slug: kombo-gethrisabsencetypesparameterpagesize
- name: GetHrisAbsenceTypesParameterRemoteIds
  property_count: 0
  slug: kombo-gethrisabsencetypesparameterremoteids
- name: GetHrisAbsenceTypesParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethrisabsencetypesparameterupdatedafter
- name: GetHrisAbsenceTypesPositiveResponse
  property_count: 2
  slug: kombo-gethrisabsencetypespositiveresponse
- name: GetHrisEmployeeDocumentCategoriesParameterCursor
  property_count: 0
  slug: kombo-gethrisemployeedocumentcategoriesparametercursor
- name: GetHrisEmployeeDocumentCategoriesParameterIds
  property_count: 0
  slug: kombo-gethrisemployeedocumentcategoriesparameterids
- name: GetHrisEmployeeDocumentCategoriesParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethrisemployeedocumentcategoriesparameterignoreunsupportedf
- name: GetHrisEmployeeDocumentCategoriesParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethrisemployeedocumentcategoriesparameterincludedeleted
- name: GetHrisEmployeeDocumentCategoriesParameterPageSize
  property_count: 0
  slug: kombo-gethrisemployeedocumentcategoriesparameterpagesize
- name: GetHrisEmployeeDocumentCategoriesParameterRemoteIds
  property_count: 0
  slug: kombo-gethrisemployeedocumentcategoriesparameterremoteids
- name: GetHrisEmployeeDocumentCategoriesParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethrisemployeedocumentcategoriesparameterupdatedafter
- name: GetHrisEmployeeDocumentCategoriesPositiveResponse
  property_count: 2
  slug: kombo-gethrisemployeedocumentcategoriespositiveresponse
- name: GetHrisEmployeesFormPositiveResponse
  property_count: 3
  slug: kombo-gethrisemployeesformpositiveresponse
- name: GetHrisEmployeeSkillAssignmentsParameterEmployeeIds
  property_count: 0
  slug: kombo-gethrisemployeeskillassignmentsparameteremployeeids
- name: GetHrisEmployeeSkillAssignmentsParameterIds
  property_count: 0
  slug: kombo-gethrisemployeeskillassignmentsparameterids
- name: GetHrisEmployeeSkillAssignmentsParameterRemoteIds
  property_count: 0
  slug: kombo-gethrisemployeeskillassignmentsparameterremoteids
- name: GetHrisEmployeeSkillAssignmentsParameterSkillIds
  property_count: 0
  slug: kombo-gethrisemployeeskillassignmentsparameterskillids
- name: GetHrisEmployeeSkillAssignmentsPositiveResponse
  property_count: 2
  slug: kombo-gethrisemployeeskillassignmentspositiveresponse
- name: GetHrisEmployeesParameterCursor
  property_count: 0
  slug: kombo-gethrisemployeesparametercursor
- name: GetHrisEmployeesParameterCustomFields
  property_count: 0
  slug: kombo-gethrisemployeesparametercustomfields
- name: GetHrisEmployeesParameterEmploymentStatus
  property_count: 0
  slug: kombo-gethrisemployeesparameteremploymentstatus
- name: GetHrisEmployeesParameterEmploymentStatuses
  property_count: 0
  slug: kombo-gethrisemployeesparameteremploymentstatuses
- name: GetHrisEmployeesParameterGroupIds
  property_count: 0
  slug: kombo-gethrisemployeesparametergroupids
- name: GetHrisEmployeesParameterIds
  property_count: 0
  slug: kombo-gethrisemployeesparameterids
- name: GetHrisEmployeesParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethrisemployeesparameterignoreunsupportedfilters
- name: GetHrisEmployeesParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethrisemployeesparameterincludedeleted
- name: GetHrisEmployeesParameterLegalEntityIds
  property_count: 0
  slug: kombo-gethrisemployeesparameterlegalentityids
- name: GetHrisEmployeesParameterPageSize
  property_count: 0
  slug: kombo-gethrisemployeesparameterpagesize
- name: GetHrisEmployeesParameterPersonalEmails
  property_count: 0
  slug: kombo-gethrisemployeesparameterpersonalemails
- name: GetHrisEmployeesParameterRemoteIds
  property_count: 0
  slug: kombo-gethrisemployeesparameterremoteids
- name: GetHrisEmployeesParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethrisemployeesparameterupdatedafter
- name: GetHrisEmployeesParameterWorkEmails
  property_count: 0
  slug: kombo-gethrisemployeesparameterworkemails
- name: GetHrisEmployeesParameterWorkLocationIds
  property_count: 0
  slug: kombo-gethrisemployeesparameterworklocationids
- name: GetHrisEmployeesPositiveResponse
  property_count: 2
  slug: kombo-gethrisemployeespositiveresponse
- name: GetHrisEmploymentsParameterCursor
  property_count: 0
  slug: kombo-gethrisemploymentsparametercursor
- name: GetHrisEmploymentsParameterIds
  property_count: 0
  slug: kombo-gethrisemploymentsparameterids
- name: GetHrisEmploymentsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethrisemploymentsparameterignoreunsupportedfilters
- name: GetHrisEmploymentsParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethrisemploymentsparameterincludedeleted
- name: GetHrisEmploymentsParameterPageSize
  property_count: 0
  slug: kombo-gethrisemploymentsparameterpagesize
- name: GetHrisEmploymentsParameterRemoteIds
  property_count: 0
  slug: kombo-gethrisemploymentsparameterremoteids
- name: GetHrisEmploymentsParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethrisemploymentsparameterupdatedafter
- name: GetHrisEmploymentsPositiveResponse
  property_count: 2
  slug: kombo-gethrisemploymentspositiveresponse
- name: GetHrisGroupsParameterCursor
  property_count: 0
  slug: kombo-gethrisgroupsparametercursor
- name: GetHrisGroupsParameterIds
  property_count: 0
  slug: kombo-gethrisgroupsparameterids
- name: GetHrisGroupsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethrisgroupsparameterignoreunsupportedfilters
- name: GetHrisGroupsParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethrisgroupsparameterincludedeleted
- name: GetHrisGroupsParameterNameContains
  property_count: 0
  slug: kombo-gethrisgroupsparameternamecontains
- name: GetHrisGroupsParameterPageSize
  property_count: 0
  slug: kombo-gethrisgroupsparameterpagesize
- name: GetHrisGroupsParameterRemoteIds
  property_count: 0
  slug: kombo-gethrisgroupsparameterremoteids
- name: GetHrisGroupsParameterTypes
  property_count: 0
  slug: kombo-gethrisgroupsparametertypes
- name: GetHrisGroupsParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethrisgroupsparameterupdatedafter
- name: GetHrisGroupsPositiveResponse
  property_count: 2
  slug: kombo-gethrisgroupspositiveresponse
- name: GetHrisLegalEntitiesParameterCursor
  property_count: 0
  slug: kombo-gethrislegalentitiesparametercursor
- name: GetHrisLegalEntitiesParameterIds
  property_count: 0
  slug: kombo-gethrislegalentitiesparameterids
- name: GetHrisLegalEntitiesParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethrislegalentitiesparameterignoreunsupportedfilters
- name: GetHrisLegalEntitiesParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethrislegalentitiesparameterincludedeleted
- name: GetHrisLegalEntitiesParameterNameContains
  property_count: 0
  slug: kombo-gethrislegalentitiesparameternamecontains
- name: GetHrisLegalEntitiesParameterPageSize
  property_count: 0
  slug: kombo-gethrislegalentitiesparameterpagesize
- name: GetHrisLegalEntitiesParameterRemoteIds
  property_count: 0
  slug: kombo-gethrislegalentitiesparameterremoteids
- name: GetHrisLegalEntitiesParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethrislegalentitiesparameterupdatedafter
- name: GetHrisLegalEntitiesPositiveResponse
  property_count: 2
  slug: kombo-gethrislegalentitiespositiveresponse
- name: GetHrisLocationsParameterCursor
  property_count: 0
  slug: kombo-gethrislocationsparametercursor
- name: GetHrisLocationsParameterIds
  property_count: 0
  slug: kombo-gethrislocationsparameterids
- name: GetHrisLocationsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethrislocationsparameterignoreunsupportedfilters
- name: GetHrisLocationsParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethrislocationsparameterincludedeleted
- name: GetHrisLocationsParameterNameContains
  property_count: 0
  slug: kombo-gethrislocationsparameternamecontains
- name: GetHrisLocationsParameterPageSize
  property_count: 0
  slug: kombo-gethrislocationsparameterpagesize
- name: GetHrisLocationsParameterRemoteIds
  property_count: 0
  slug: kombo-gethrislocationsparameterremoteids
- name: GetHrisLocationsParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethrislocationsparameterupdatedafter
- name: GetHrisLocationsPositiveResponse
  property_count: 2
  slug: kombo-gethrislocationspositiveresponse
- name: GetHrisPerformanceReviewCyclesParameterCursor
  property_count: 0
  slug: kombo-gethrisperformancereviewcyclesparametercursor
- name: GetHrisPerformanceReviewCyclesParameterIds
  property_count: 0
  slug: kombo-gethrisperformancereviewcyclesparameterids
- name: GetHrisPerformanceReviewCyclesParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethrisperformancereviewcyclesparameterignoreunsupportedfilt
- name: GetHrisPerformanceReviewCyclesParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethrisperformancereviewcyclesparameterincludedeleted
- name: GetHrisPerformanceReviewCyclesParameterPageSize
  property_count: 0
  slug: kombo-gethrisperformancereviewcyclesparameterpagesize
- name: GetHrisPerformanceReviewCyclesParameterRemoteIds
  property_count: 0
  slug: kombo-gethrisperformancereviewcyclesparameterremoteids
- name: GetHrisPerformanceReviewCyclesParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethrisperformancereviewcyclesparameterupdatedafter
- name: GetHrisPerformanceReviewCyclesPositiveResponse
  property_count: 2
  slug: kombo-gethrisperformancereviewcyclespositiveresponse
- name: GetHrisPerformanceReviewsParameterCursor
  property_count: 0
  slug: kombo-gethrisperformancereviewsparametercursor
- name: GetHrisPerformanceReviewsParameterIds
  property_count: 0
  slug: kombo-gethrisperformancereviewsparameterids
- name: GetHrisPerformanceReviewsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethrisperformancereviewsparameterignoreunsupportedfilters
- name: GetHrisPerformanceReviewsParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethrisperformancereviewsparameterincludedeleted
- name: GetHrisPerformanceReviewsParameterPageSize
  property_count: 0
  slug: kombo-gethrisperformancereviewsparameterpagesize
- name: GetHrisPerformanceReviewsParameterRemoteIds
  property_count: 0
  slug: kombo-gethrisperformancereviewsparameterremoteids
- name: GetHrisPerformanceReviewsParameterReviewCycleIds
  property_count: 0
  slug: kombo-gethrisperformancereviewsparameterreviewcycleids
- name: GetHrisPerformanceReviewsParameterRevieweeIds
  property_count: 0
  slug: kombo-gethrisperformancereviewsparameterrevieweeids
- name: GetHrisPerformanceReviewsParameterTypes
  property_count: 0
  slug: kombo-gethrisperformancereviewsparametertypes
- name: GetHrisPerformanceReviewsParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethrisperformancereviewsparameterupdatedafter
- name: GetHrisPerformanceReviewsPositiveResponse
  property_count: 2
  slug: kombo-gethrisperformancereviewspositiveresponse
- name: GetHrisSkillsParameterIds
  property_count: 0
  slug: kombo-gethrisskillsparameterids
- name: GetHrisSkillsParameterNameContains
  property_count: 0
  slug: kombo-gethrisskillsparameternamecontains
- name: GetHrisSkillsParameterRemoteIds
  property_count: 0
  slug: kombo-gethrisskillsparameterremoteids
- name: GetHrisSkillsPositiveResponse
  property_count: 2
  slug: kombo-gethrisskillspositiveresponse
- name: GetHrisStaffingEntitiesParameterCursor
  property_count: 0
  slug: kombo-gethrisstaffingentitiesparametercursor
- name: GetHrisStaffingEntitiesParameterIds
  property_count: 0
  slug: kombo-gethrisstaffingentitiesparameterids
- name: GetHrisStaffingEntitiesParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethrisstaffingentitiesparameterignoreunsupportedfilters
- name: GetHrisStaffingEntitiesParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethrisstaffingentitiesparameterincludedeleted
- name: GetHrisStaffingEntitiesParameterModelTypes
  property_count: 0
  slug: kombo-gethrisstaffingentitiesparametermodeltypes
- name: GetHrisStaffingEntitiesParameterPageSize
  property_count: 0
  slug: kombo-gethrisstaffingentitiesparameterpagesize
- name: GetHrisStaffingEntitiesParameterRemoteIds
  property_count: 0
  slug: kombo-gethrisstaffingentitiesparameterremoteids
- name: GetHrisStaffingEntitiesParameterStatuses
  property_count: 0
  slug: kombo-gethrisstaffingentitiesparameterstatuses
- name: GetHrisStaffingEntitiesParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethrisstaffingentitiesparameterupdatedafter
- name: GetHrisStaffingEntitiesPositiveResponse
  property_count: 2
  slug: kombo-gethrisstaffingentitiespositiveresponse
- name: GetHrisTeamsParameterCursor
  property_count: 0
  slug: kombo-gethristeamsparametercursor
- name: GetHrisTeamsParameterIds
  property_count: 0
  slug: kombo-gethristeamsparameterids
- name: GetHrisTeamsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethristeamsparameterignoreunsupportedfilters
- name: GetHrisTeamsParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethristeamsparameterincludedeleted
- name: GetHrisTeamsParameterPageSize
  property_count: 0
  slug: kombo-gethristeamsparameterpagesize
- name: GetHrisTeamsParameterRemoteIds
  property_count: 0
  slug: kombo-gethristeamsparameterremoteids
- name: GetHrisTeamsParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethristeamsparameterupdatedafter
- name: GetHrisTeamsPositiveResponse
  property_count: 2
  slug: kombo-gethristeamspositiveresponse
- name: GetHrisTimeOffBalancesParameterCursor
  property_count: 0
  slug: kombo-gethristimeoffbalancesparametercursor
- name: GetHrisTimeOffBalancesParameterEmployeeId
  property_count: 0
  slug: kombo-gethristimeoffbalancesparameteremployeeid
- name: GetHrisTimeOffBalancesParameterIds
  property_count: 0
  slug: kombo-gethristimeoffbalancesparameterids
- name: GetHrisTimeOffBalancesParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethristimeoffbalancesparameterignoreunsupportedfilters
- name: GetHrisTimeOffBalancesParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethristimeoffbalancesparameterincludedeleted
- name: GetHrisTimeOffBalancesParameterPageSize
  property_count: 0
  slug: kombo-gethristimeoffbalancesparameterpagesize
- name: GetHrisTimeOffBalancesParameterRemoteIds
  property_count: 0
  slug: kombo-gethristimeoffbalancesparameterremoteids
- name: GetHrisTimeOffBalancesParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethristimeoffbalancesparameterupdatedafter
- name: GetHrisTimeOffBalancesPositiveResponse
  property_count: 2
  slug: kombo-gethristimeoffbalancespositiveresponse
- name: GetHrisTimesheetsParameterCursor
  property_count: 0
  slug: kombo-gethristimesheetsparametercursor
- name: GetHrisTimesheetsParameterEmployeeId
  property_count: 0
  slug: kombo-gethristimesheetsparameteremployeeid
- name: GetHrisTimesheetsParameterEndedAfter
  property_count: 0
  slug: kombo-gethristimesheetsparameterendedafter
- name: GetHrisTimesheetsParameterEndedBefore
  property_count: 0
  slug: kombo-gethristimesheetsparameterendedbefore
- name: GetHrisTimesheetsParameterIds
  property_count: 0
  slug: kombo-gethristimesheetsparameterids
- name: GetHrisTimesheetsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-gethristimesheetsparameterignoreunsupportedfilters
- name: GetHrisTimesheetsParameterIncludeDeleted
  property_count: 0
  slug: kombo-gethristimesheetsparameterincludedeleted
- name: GetHrisTimesheetsParameterPageSize
  property_count: 0
  slug: kombo-gethristimesheetsparameterpagesize
- name: GetHrisTimesheetsParameterRemoteIds
  property_count: 0
  slug: kombo-gethristimesheetsparameterremoteids
- name: GetHrisTimesheetsParameterStartedAfter
  property_count: 0
  slug: kombo-gethristimesheetsparameterstartedafter
- name: GetHrisTimesheetsParameterStartedBefore
  property_count: 0
  slug: kombo-gethristimesheetsparameterstartedbefore
- name: GetHrisTimesheetsParameterUpdatedAfter
  property_count: 0
  slug: kombo-gethristimesheetsparameterupdatedafter
- name: GetHrisTimesheetsPositiveResponse
  property_count: 2
  slug: kombo-gethristimesheetspositiveresponse
- name: GetIntegrationsIntegrationIdCustomFieldsParameterCursor
  property_count: 0
  slug: kombo-getintegrationsintegrationidcustomfieldsparametercursor
- name: GetIntegrationsIntegrationIdCustomFieldsParameterIntegrationId
  property_count: 0
  slug: kombo-getintegrationsintegrationidcustomfieldsparameterintegration
- name: GetIntegrationsIntegrationIdCustomFieldsParameterPageSize
  property_count: 0
  slug: kombo-getintegrationsintegrationidcustomfieldsparameterpagesize
- name: GetIntegrationsIntegrationIdCustomFieldsPositiveResponse
  property_count: 2
  slug: kombo-getintegrationsintegrationidcustomfieldspositiveresponse
- name: GetIntegrationsIntegrationIdIntegrationFieldsParameterCursor
  property_count: 0
  slug: kombo-getintegrationsintegrationidintegrationfieldsparametercursor
- name: GetIntegrationsIntegrationIdIntegrationFieldsParameterIntegrationId
  property_count: 0
  slug: kombo-getintegrationsintegrationidintegrationfieldsparameterintegr
- name: GetIntegrationsIntegrationIdIntegrationFieldsParameterPageSize
  property_count: 0
  slug: kombo-getintegrationsintegrationidintegrationfieldsparameterpagesi
- name: GetIntegrationsIntegrationIdIntegrationFieldsPositiveResponse
  property_count: 2
  slug: kombo-getintegrationsintegrationidintegrationfieldspositiverespons
- name: GetIntegrationsIntegrationIdParameterIntegrationId
  property_count: 0
  slug: kombo-getintegrationsintegrationidparameterintegrationid
- name: GetIntegrationsIntegrationIdPositiveResponse
  property_count: 2
  slug: kombo-getintegrationsintegrationidpositiveresponse
- name: GetLmsCourseProgressionsParameterCourseIds
  property_count: 0
  slug: kombo-getlmscourseprogressionsparametercourseids
- name: GetLmsCourseProgressionsParameterCursor
  property_count: 0
  slug: kombo-getlmscourseprogressionsparametercursor
- name: GetLmsCourseProgressionsParameterIds
  property_count: 0
  slug: kombo-getlmscourseprogressionsparameterids
- name: GetLmsCourseProgressionsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getlmscourseprogressionsparameterignoreunsupportedfilters
- name: GetLmsCourseProgressionsParameterIncludeDeleted
  property_count: 0
  slug: kombo-getlmscourseprogressionsparameterincludedeleted
- name: GetLmsCourseProgressionsParameterPageSize
  property_count: 0
  slug: kombo-getlmscourseprogressionsparameterpagesize
- name: GetLmsCourseProgressionsParameterRemoteIds
  property_count: 0
  slug: kombo-getlmscourseprogressionsparameterremoteids
- name: GetLmsCourseProgressionsParameterUpdatedAfter
  property_count: 0
  slug: kombo-getlmscourseprogressionsparameterupdatedafter
- name: GetLmsCourseProgressionsParameterUserIds
  property_count: 0
  slug: kombo-getlmscourseprogressionsparameteruserids
- name: GetLmsCourseProgressionsPositiveResponse
  property_count: 2
  slug: kombo-getlmscourseprogressionspositiveresponse
- name: GetLmsCoursesBulkTaskIdParameterTaskId
  property_count: 0
  slug: kombo-getlmscoursesbulktaskidparametertaskid
- name: GetLmsCoursesBulkTaskIdPositiveResponse
  property_count: 2
  slug: kombo-getlmscoursesbulktaskidpositiveresponse
- name: GetLmsCoursesParameterCursor
  property_count: 0
  slug: kombo-getlmscoursesparametercursor
- name: GetLmsCoursesParameterIds
  property_count: 0
  slug: kombo-getlmscoursesparameterids
- name: GetLmsCoursesParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getlmscoursesparameterignoreunsupportedfilters
- name: GetLmsCoursesParameterIncludeDeleted
  property_count: 0
  slug: kombo-getlmscoursesparameterincludedeleted
- name: GetLmsCoursesParameterPageSize
  property_count: 0
  slug: kombo-getlmscoursesparameterpagesize
- name: GetLmsCoursesParameterRemoteIds
  property_count: 0
  slug: kombo-getlmscoursesparameterremoteids
- name: GetLmsCoursesParameterUpdatedAfter
  property_count: 0
  slug: kombo-getlmscoursesparameterupdatedafter
- name: GetLmsCoursesPositiveResponse
  property_count: 2
  slug: kombo-getlmscoursespositiveresponse
- name: GetLmsSkillsParameterCursor
  property_count: 0
  slug: kombo-getlmsskillsparametercursor
- name: GetLmsSkillsParameterIds
  property_count: 0
  slug: kombo-getlmsskillsparameterids
- name: GetLmsSkillsParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getlmsskillsparameterignoreunsupportedfilters
- name: GetLmsSkillsParameterIncludeDeleted
  property_count: 0
  slug: kombo-getlmsskillsparameterincludedeleted
- name: GetLmsSkillsParameterPageSize
  property_count: 0
  slug: kombo-getlmsskillsparameterpagesize
- name: GetLmsSkillsParameterRemoteIds
  property_count: 0
  slug: kombo-getlmsskillsparameterremoteids
- name: GetLmsSkillsParameterUpdatedAfter
  property_count: 0
  slug: kombo-getlmsskillsparameterupdatedafter
- name: GetLmsSkillsPositiveResponse
  property_count: 2
  slug: kombo-getlmsskillspositiveresponse
- name: GetLmsUsersParameterCursor
  property_count: 0
  slug: kombo-getlmsusersparametercursor
- name: GetLmsUsersParameterIds
  property_count: 0
  slug: kombo-getlmsusersparameterids
- name: GetLmsUsersParameterIgnoreUnsupportedFilters
  property_count: 0
  slug: kombo-getlmsusersparameterignoreunsupportedfilters
- name: GetLmsUsersParameterIncludeDeleted
  property_count: 0
  slug: kombo-getlmsusersparameterincludedeleted
- name: GetLmsUsersParameterPageSize
  property_count: 0
  slug: kombo-getlmsusersparameterpagesize
- name: GetLmsUsersParameterRemoteIds
  property_count: 0
  slug: kombo-getlmsusersparameterremoteids
- name: GetLmsUsersParameterUpdatedAfter
  property_count: 0
  slug: kombo-getlmsusersparameterupdatedafter
- name: GetLmsUsersParameterWorkEmails
  property_count: 0
  slug: kombo-getlmsusersparameterworkemails
- name: GetLmsUsersPositiveResponse
  property_count: 2
  slug: kombo-getlmsuserspositiveresponse
- name: GetToolsCategoryParameterCategory
  property_count: 0
  slug: kombo-gettoolscategoryparametercategory
- name: GetToolsCategoryPositiveResponse
  property_count: 2
  slug: kombo-gettoolscategorypositiveresponse
- name: InlineAssessmentOrderReceivedWebhookPayload
  property_count: 3
  slug: kombo-inlineassessmentorderreceivedwebhookpayload
- name: IntegrationCreatedWebhookPayload
  property_count: 3
  slug: kombo-integrationcreatedwebhookpayload
- name: IntegrationDeletedWebhookPayload
  property_count: 3
  slug: kombo-integrationdeletedwebhookpayload
- name: IntegrationStateChangedWebhookPayload
  property_count: 3
  slug: kombo-integrationstatechangedwebhookpayload
- name: PatchAtsApplicationsApplicationIdInterviewsParameterApplicationId
  property_count: 0
  slug: kombo-patchatsapplicationsapplicationidinterviewsparameterapplicat
- name: PatchAtsApplicationsApplicationIdInterviewsPositiveResponse
  property_count: 2
  slug: kombo-patchatsapplicationsapplicationidinterviewspositiveresponse
- name: PatchAtsApplicationsApplicationIdInterviewsRequestBody
  property_count: 7
  slug: kombo-patchatsapplicationsapplicationidinterviewsrequestbody
- name: PatchHrisEmployeesEmployeeIdParameterEmployeeId
  property_count: 0
  slug: kombo-patchhrisemployeesemployeeidparameteremployeeid
- name: PatchHrisEmployeesEmployeeIdPositiveResponse
  property_count: 3
  slug: kombo-patchhrisemployeesemployeeidpositiveresponse
- name: PatchHrisEmployeesEmployeeIdRequestBody
  property_count: 18
  slug: kombo-patchhrisemployeesemployeeidrequestbody
- name: PatchHrisEmployeeSkillAssignmentsEmployeeSkillAssignmentIdParameterEmployeeSkillAssignmentId
  property_count: 0
  slug: kombo-patchhrisemployeeskillassignmentsemployeeskillassignmentidpa
- name: PatchHrisEmployeeSkillAssignmentsEmployeeSkillAssignmentIdPositiveResponse
  property_count: 2
  slug: kombo-patchhrisemployeeskillassignmentsemployeeskillassignmentidpo
- name: PatchHrisEmployeeSkillAssignmentsEmployeeSkillAssignmentIdRequestBody
  property_count: 1
  slug: kombo-patchhrisemployeeskillassignmentsemployeeskillassignmentidre
- name: PatchHrisSkillsSkillIdParameterSkillId
  property_count: 0
  slug: kombo-patchhrisskillsskillidparameterskillid
- name: PatchHrisSkillsSkillIdPositiveResponse
  property_count: 2
  slug: kombo-patchhrisskillsskillidpositiveresponse
- name: PatchHrisSkillsSkillIdRequestBody
  property_count: 2
  slug: kombo-patchhrisskillsskillidrequestbody
- name: PatchIntegrationsIntegrationIdIntegrationFieldsIntegrationFieldIdParameterIntegrationId
  property_count: 0
  slug: kombo-patchintegrationsintegrationidintegrationfieldsintegrationfi
- name: PostAiApplyApplyPositiveResponse
  property_count: 2
  slug: kombo-postaiapplyapplypositiveresponse
- name: PostAiApplyApplyRequestBody
  property_count: 6
  slug: kombo-postaiapplyapplyrequestbody
- name: PostAiApplyCareerSitesPositiveResponse
  property_count: 2
  slug: kombo-postaiapplycareersitespositiveresponse
- name: PostAiApplyCareerSitesRequestBody
  property_count: 1
  slug: kombo-postaiapplycareersitesrequestbody
- name: PostAiApplyJobFeedsPositiveResponse
  property_count: 2
  slug: kombo-postaiapplyjobfeedspositiveresponse
- name: PostAiApplyJobFeedsRequestBody
  property_count: 1
  slug: kombo-postaiapplyjobfeedsrequestbody
- name: PostAiApplyPostingsPositiveResponse
  property_count: 2
  slug: kombo-postaiapplypostingspositiveresponse
- name: PostAiApplyPostingsPostingIdInquireParameterPostingId
  property_count: 0
  slug: kombo-postaiapplypostingspostingidinquireparameterpostingid
- name: PostAiApplyPostingsPostingIdInquirePositiveResponse
  property_count: 2
  slug: kombo-postaiapplypostingspostingidinquirepositiveresponse
- name: PostAiApplyPostingsPostingIdInquireRequestBody
  property_count: 0
  slug: kombo-postaiapplypostingspostingidinquirerequestbody
- name: PostAiApplyPostingsRequestBody
  property_count: 4
  slug: kombo-postaiapplypostingsrequestbody
- name: PostAiApplyUnifiedApiJobsJobIdApplicationsParameterJobId
  property_count: 0
  slug: kombo-postaiapplyunifiedapijobsjobidapplicationsparameterjobid
- name: PostAiApplyUnifiedApiJobsJobIdApplicationsPositiveResponse
  property_count: 2
  slug: kombo-postaiapplyunifiedapijobsjobidapplicationspositiveresponse
- name: PostAiApplyUnifiedApiJobsJobIdApplicationsRequestBody
  property_count: 9
  slug: kombo-postaiapplyunifiedapijobsjobidapplicationsrequestbody
- name: PostAtsApplicationsApplicationIdAttachmentsParameterApplicationId
  property_count: 0
  slug: kombo-postatsapplicationsapplicationidattachmentsparameterapplicat
- name: PostAtsApplicationsApplicationIdAttachmentsPositiveResponse
  property_count: 3
  slug: kombo-postatsapplicationsapplicationidattachmentspositiveresponse
- name: PostAtsApplicationsApplicationIdAttachmentsRequestBody
  property_count: 2
  slug: kombo-postatsapplicationsapplicationidattachmentsrequestbody
- name: PostAtsApplicationsApplicationIdInterviewsParameterApplicationId
  property_count: 0
  slug: kombo-postatsapplicationsapplicationidinterviewsparameterapplicati
- name: PostAtsApplicationsApplicationIdInterviewsPositiveResponse
  property_count: 2
  slug: kombo-postatsapplicationsapplicationidinterviewspositiveresponse
- name: PostAtsApplicationsApplicationIdInterviewsRequestBody
  property_count: 6
  slug: kombo-postatsapplicationsapplicationidinterviewsrequestbody
- name: PostAtsApplicationsApplicationIdNotesParameterApplicationId
  property_count: 0
  slug: kombo-postatsapplicationsapplicationidnotesparameterapplicationid
- name: PostAtsApplicationsApplicationIdNotesPositiveResponse
  property_count: 3
  slug: kombo-postatsapplicationsapplicationidnotespositiveresponse
- name: PostAtsApplicationsApplicationIdNotesRequestBody
  property_count: 3
  slug: kombo-postatsapplicationsapplicationidnotesrequestbody
- name: PostAtsApplicationsApplicationIdRejectParameterApplicationId
  property_count: 0
  slug: kombo-postatsapplicationsapplicationidrejectparameterapplicationid
- name: PostAtsApplicationsApplicationIdRejectPositiveResponse
  property_count: 3
  slug: kombo-postatsapplicationsapplicationidrejectpositiveresponse
- name: PostAtsApplicationsApplicationIdRejectRequestBody
  property_count: 3
  slug: kombo-postatsapplicationsapplicationidrejectrequestbody
- name: PostAtsApplicationsApplicationIdResultLinksParameterApplicationId
  property_count: 0
  slug: kombo-postatsapplicationsapplicationidresultlinksparameterapplicat
- name: PostAtsApplicationsApplicationIdResultLinksPositiveResponse
  property_count: 3
  slug: kombo-postatsapplicationsapplicationidresultlinkspositiveresponse
- name: PostAtsApplicationsApplicationIdResultLinksRequestBody
  property_count: 4
  slug: kombo-postatsapplicationsapplicationidresultlinksrequestbody
- name: PostAtsCandidatesCandidateIdAttachmentsParameterCandidateId
  property_count: 0
  slug: kombo-postatscandidatescandidateidattachmentsparametercandidateid
- name: PostAtsCandidatesCandidateIdAttachmentsPositiveResponse
  property_count: 3
  slug: kombo-postatscandidatescandidateidattachmentspositiveresponse
- name: PostAtsCandidatesCandidateIdAttachmentsRequestBody
  property_count: 2
  slug: kombo-postatscandidatescandidateidattachmentsrequestbody
- name: PostAtsCandidatesCandidateIdResultLinksParameterCandidateId
  property_count: 0
  slug: kombo-postatscandidatescandidateidresultlinksparametercandidateid
- name: PostAtsCandidatesCandidateIdResultLinksPositiveResponse
  property_count: 3
  slug: kombo-postatscandidatescandidateidresultlinkspositiveresponse
- name: PostAtsCandidatesCandidateIdResultLinksRequestBody
  property_count: 4
  slug: kombo-postatscandidatescandidateidresultlinksrequestbody
- name: PostAtsCandidatesCandidateIdTagsParameterCandidateId
  property_count: 0
  slug: kombo-postatscandidatescandidateidtagsparametercandidateid
- name: PostAtsCandidatesCandidateIdTagsPositiveResponse
  property_count: 3
  slug: kombo-postatscandidatescandidateidtagspositiveresponse
- name: PostAtsCandidatesCandidateIdTagsRequestBody
  property_count: 2
  slug: kombo-postatscandidatescandidateidtagsrequestbody
- name: PostAtsCandidatesPositiveResponse
  property_count: 3
  slug: kombo-postatscandidatespositiveresponse
- name: PostAtsCandidatesRequestBody
  property_count: 8
  slug: kombo-postatscandidatesrequestbody
- name: PostAtsCustomAvionteSyncedJobsPositiveResponse
  property_count: 2
  slug: kombo-postatscustomaviontesyncedjobspositiveresponse
- name: PostAtsCustomAvionteSyncedJobsRequestBody
  property_count: 1
  slug: kombo-postatscustomaviontesyncedjobsrequestbody
- name: PostAtsImportTrackedApplicationPositiveResponse
  property_count: 3
  slug: kombo-postatsimporttrackedapplicationpositiveresponse
- name: PostAtsImportTrackedApplicationRequestBody
  property_count: 7
  slug: kombo-postatsimporttrackedapplicationrequestbody
- name: PostAtsJobsJobIdApplicationsParameterJobId
  property_count: 0
  slug: kombo-postatsjobsjobidapplicationsparameterjobid
- name: PostAtsJobsJobIdApplicationsPositiveResponse
  property_count: 3
  slug: kombo-postatsjobsjobidapplicationspositiveresponse
- name: PostAtsJobsJobIdApplicationsRequestBody
  property_count: 8
  slug: kombo-postatsjobsjobidapplicationsrequestbody
- name: PostConnectActivateIntegrationPositiveResponse
  property_count: 2
  slug: kombo-postconnectactivateintegrationpositiveresponse
- name: PostConnectActivateIntegrationRequestBody
  property_count: 1
  slug: kombo-postconnectactivateintegrationrequestbody
- name: PostConnectCreateLinkPositiveResponse
  property_count: 2
  slug: kombo-postconnectcreatelinkpositiveresponse
- name: PostConnectCreateLinkRequestBody
  property_count: 11
  slug: kombo-postconnectcreatelinkrequestbody
- name: PostCustomDatevDownloadDocumentPositiveResponse
  property_count: 3
  slug: kombo-postcustomdatevdownloaddocumentpositiveresponse
- name: PostCustomDatevDownloadDocumentRequestBody
  property_count: 3
  slug: kombo-postcustomdatevdownloaddocumentrequestbody
- name: PostCustomDatevEmployeesEmployeeIdDownloadDocumentParameterEmployeeId
  property_count: 0
  slug: kombo-postcustomdatevemployeesemployeeiddownloaddocumentparametere
- name: PostCustomDatevEmployeesEmployeeIdDownloadDocumentPositiveResponse
  property_count: 3
  slug: kombo-postcustomdatevemployeesemployeeiddownloaddocumentpositivere
- name: PostCustomDatevEmployeesEmployeeIdDownloadDocumentRequestBody
  property_count: 2
  slug: kombo-postcustomdatevemployeesemployeeiddownloaddocumentrequestbod
- name: PostCustomDatevEmployeesEmployeeIdEauRequestsParameterEmployeeId
  property_count: 0
  slug: kombo-postcustomdatevemployeesemployeeideaurequestsparameteremploy
- name: PostCustomDatevEmployeesEmployeeIdEauRequestsPositiveResponse
  property_count: 3
  slug: kombo-postcustomdatevemployeesemployeeideaurequestspositiverespons
- name: PostCustomDatevEmployeesEmployeeIdEauRequestsRequestBody
  property_count: 3
  slug: kombo-postcustomdatevemployeesemployeeideaurequestsrequestbody
- name: PostCustomDatevPassthroughPositiveResponse
  property_count: 3
  slug: kombo-postcustomdatevpassthroughpositiveresponse
- name: PostCustomDatevPassthroughRequestBody
  property_count: 5
  slug: kombo-postcustomdatevpassthroughrequestbody
- name: PostCustomDatevPushDataGeneralPositiveResponse
  property_count: 3
  slug: kombo-postcustomdatevpushdatageneralpositiveresponse
- name: PostCustomDatevPushDataGeneralRequestBody
  property_count: 0
  slug: kombo-postcustomdatevpushdatageneralrequestbody
- name: PostCustomDatevPushDataPayrollPositiveResponse
  property_count: 3
  slug: kombo-postcustomdatevpushdatapayrollpositiveresponse
- name: PostCustomDatevPushDataPayrollRequestBody
  property_count: 1
  slug: kombo-postcustomdatevpushdatapayrollrequestbody
- name: PostCustomSilaeEmployeesEmployeeIdPayrollSupplementsParameterEmployeeId
  property_count: 0
  slug: kombo-postcustomsilaeemployeesemployeeidpayrollsupplementsparamete
- name: PostCustomSilaeEmployeesEmployeeIdPayrollSupplementsPositiveResponse
  property_count: 3
  slug: kombo-postcustomsilaeemployeesemployeeidpayrollsupplementspositive
- name: PostCustomSilaeEmployeesEmployeeIdPayrollSupplementsRequestBody
  property_count: 4
  slug: kombo-postcustomsilaeemployeesemployeeidpayrollsupplementsrequestb
- name: PostForceSyncPositiveResponse
  property_count: 2
  slug: kombo-postforcesyncpositiveresponse
- name: PostForceSyncRequestBody
  property_count: 1
  slug: kombo-postforcesyncrequestbody
- name: PostHrisAbsencesPositiveResponse
  property_count: 3
  slug: kombo-posthrisabsencespositiveresponse
- name: PostHrisAbsencesRequestBody
  property_count: 13
  slug: kombo-posthrisabsencesrequestbody
- name: PostHrisEmployeesEmployeeIdDocumentsParameterEmployeeId
  property_count: 0
  slug: kombo-posthrisemployeesemployeeiddocumentsparameteremployeeid
- name: PostHrisEmployeesEmployeeIdDocumentsPositiveResponse
  property_count: 3
  slug: kombo-posthrisemployeesemployeeiddocumentspositiveresponse
- name: PostHrisEmployeesEmployeeIdDocumentsRequestBody
  property_count: 2
  slug: kombo-posthrisemployeesemployeeiddocumentsrequestbody
- name: PostHrisEmployeesFormPositiveResponse
  property_count: 3
  slug: kombo-posthrisemployeesformpositiveresponse
- name: PostHrisEmployeesFormRequestBody
  property_count: 1
  slug: kombo-posthrisemployeesformrequestbody
- name: PostHrisEmployeeSkillAssignmentsPositiveResponse
  property_count: 2
  slug: kombo-posthrisemployeeskillassignmentspositiveresponse
- name: PostHrisEmployeeSkillAssignmentsRequestBody
  property_count: 3
  slug: kombo-posthrisemployeeskillassignmentsrequestbody
- name: PostHrisEmployeesPositiveResponse
  property_count: 3
  slug: kombo-posthrisemployeespositiveresponse
- name: PostHrisEmployeesRequestBody
  property_count: 14
  slug: kombo-posthrisemployeesrequestbody
- name: PostHrisProvisioningGroupsGroupIdDiffParameterGroupId
  property_count: 0
  slug: kombo-posthrisprovisioninggroupsgroupiddiffparametergroupid
- name: PostHrisProvisioningGroupsGroupIdDiffPositiveResponse
  property_count: 2
  slug: kombo-posthrisprovisioninggroupsgroupiddiffpositiveresponse
- name: PostHrisProvisioningGroupsGroupIdDiffRequestBody
  property_count: 2
  slug: kombo-posthrisprovisioninggroupsgroupiddiffrequestbody
- name: PostHrisProvisioningGroupsGroupIdSetupLinksParameterGroupId
  property_count: 0
  slug: kombo-posthrisprovisioninggroupsgroupidsetuplinksparametergroupid
- name: PostHrisProvisioningGroupsGroupIdSetupLinksPositiveResponse
  property_count: 2
  slug: kombo-posthrisprovisioninggroupsgroupidsetuplinkspositiveresponse
- name: PostHrisProvisioningGroupsGroupIdSetupLinksRequestBody
  property_count: 1
  slug: kombo-posthrisprovisioninggroupsgroupidsetuplinksrequestbody
- name: PostHrisSkillsPositiveResponse
  property_count: 2
  slug: kombo-posthrisskillspositiveresponse
- name: PostHrisSkillsRequestBody
  property_count: 2
  slug: kombo-posthrisskillsrequestbody
- name: PostIntegrationsIntegrationIdRelinkParameterIntegrationId
  property_count: 0
  slug: kombo-postintegrationsintegrationidrelinkparameterintegrationid
- name: PostIntegrationsIntegrationIdRelinkPositiveResponse
  property_count: 2
  slug: kombo-postintegrationsintegrationidrelinkpositiveresponse
- name: PostIntegrationsIntegrationIdRelinkRequestBody
  property_count: 3
  slug: kombo-postintegrationsintegrationidrelinkrequestbody
- name: PostIntegrationsIntegrationIdSetupLinkParameterIntegrationId
  property_count: 0
  slug: kombo-postintegrationsintegrationidsetuplinkparameterintegrationid
- name: PostIntegrationsIntegrationIdSetupLinkPositiveResponse
  property_count: 2
  slug: kombo-postintegrationsintegrationidsetuplinkpositiveresponse
- name: PostIntegrationsIntegrationIdSetupLinkRequestBody
  property_count: 2
  slug: kombo-postintegrationsintegrationidsetuplinkrequestbody
- name: PostLmsCourseProgressionsCourseProgressionIdCompleteParameterCourseProgressionId
  property_count: 0
  slug: kombo-postlmscourseprogressionscourseprogressionidcompleteparamete
- name: PostLmsCourseProgressionsCourseProgressionIdCompletePositiveResponse
  property_count: 3
  slug: kombo-postlmscourseprogressionscourseprogressionidcompletepositive
- name: PostLmsCourseProgressionsCourseProgressionIdCompleteRequestBody
  property_count: 2
  slug: kombo-postlmscourseprogressionscourseprogressionidcompleterequestb
- name: PostLmsCourseProgressionsPositiveResponse
  property_count: 3
  slug: kombo-postlmscourseprogressionspositiveresponse
- name: PostLmsCourseProgressionsRequestBody
  property_count: 2
  slug: kombo-postlmscourseprogressionsrequestbody
- name: PostLmsCoursesBulkPositiveResponse
  property_count: 3
  slug: kombo-postlmscoursesbulkpositiveresponse
- name: PostLmsCoursesBulkRequestBody
  property_count: 1
  slug: kombo-postlmscoursesbulkrequestbody
- name: PostLmsCoursesCourseIdDeactivateParameterCourseId
  property_count: 0
  slug: kombo-postlmscoursescourseiddeactivateparametercourseid
- name: PostLmsCoursesCourseIdDeactivatePositiveResponse
  property_count: 3
  slug: kombo-postlmscoursescourseiddeactivatepositiveresponse
- name: PostLmsCoursesCourseIdDeactivateRequestBody
  property_count: 0
  slug: kombo-postlmscoursescourseiddeactivaterequestbody
- name: PostPassthroughToolApiParameterApi
  property_count: 0
  slug: kombo-postpassthroughtoolapiparameterapi
- name: PostPassthroughToolApiParameterTool
  property_count: 0
  slug: kombo-postpassthroughtoolapiparametertool
- name: PostPassthroughToolApiPositiveResponse
  property_count: 3
  slug: kombo-postpassthroughtoolapipositiveresponse
- name: PostPassthroughToolApiRequestBody
  property_count: 8
  slug: kombo-postpassthroughtoolapirequestbody
- name: PutAssessmentOrdersAssessmentOrderIdResultParameterAssessmentOrderId
  property_count: 0
  slug: kombo-putassessmentordersassessmentorderidresultparameterassessmen
- name: PutAssessmentOrdersAssessmentOrderIdResultPositiveResponse
  property_count: 3
  slug: kombo-putassessmentordersassessmentorderidresultpositiveresponse
- name: PutAssessmentOrdersAssessmentOrderIdResultRequestBody
  property_count: 8
  slug: kombo-putassessmentordersassessmentorderidresultrequestbody
- name: PutAssessmentPackagesPositiveResponse
  property_count: 3
  slug: kombo-putassessmentpackagespositiveresponse
- name: PutAssessmentPackagesRequestBody
  property_count: 1
  slug: kombo-putassessmentpackagesrequestbody
- name: PutAtsApplicationsApplicationIdStageParameterApplicationId
  property_count: 0
  slug: kombo-putatsapplicationsapplicationidstageparameterapplicationid
- name: PutAtsApplicationsApplicationIdStagePositiveResponse
  property_count: 3
  slug: kombo-putatsapplicationsapplicationidstagepositiveresponse
- name: PutAtsApplicationsApplicationIdStageRequestBody
  property_count: 2
  slug: kombo-putatsapplicationsapplicationidstagerequestbody
- name: PutCustomDatevEmployeesEmployeeIdCompensationsParameterEmployeeId
  property_count: 0
  slug: kombo-putcustomdatevemployeesemployeeidcompensationsparameteremplo
- name: PutCustomDatevEmployeesEmployeeIdCompensationsPositiveResponse
  property_count: 3
  slug: kombo-putcustomdatevemployeesemployeeidcompensationspositiverespon
- name: PutCustomDatevEmployeesEmployeeIdCompensationsRequestBody
  property_count: 2
  slug: kombo-putcustomdatevemployeesemployeeidcompensationsrequestbody
- name: PutCustomDatevEmployeesEmployeeIdPreparePayrollParameterEmployeeId
  property_count: 0
  slug: kombo-putcustomdatevemployeesemployeeidpreparepayrollparameterempl
- name: PutCustomDatevEmployeesEmployeeIdPreparePayrollPositiveResponse
  property_count: 3
  slug: kombo-putcustomdatevemployeesemployeeidpreparepayrollpositiverespo
- name: PutCustomDatevEmployeesEmployeeIdPreparePayrollRequestBody
  property_count: 4
  slug: kombo-putcustomdatevemployeesemployeeidpreparepayrollrequestbody
- name: PutIntegrationsIntegrationIdCustomFieldsCustomFieldIdParameterIntegrationId
  property_count: 0
  slug: kombo-putintegrationsintegrationidcustomfieldscustomfieldidparamet
- name: PutIntegrationsIntegrationIdCustomFieldsCustomFieldIdPositiveResponse
  property_count: 2
  slug: kombo-putintegrationsintegrationidcustomfieldscustomfieldidpositiv
- name: PutIntegrationsIntegrationIdCustomFieldsCustomFieldIdRequestBody
  property_count: 1
  slug: kombo-putintegrationsintegrationidcustomfieldscustomfieldidrequest
- name: PutIntegrationsIntegrationIdEnabledParameterIntegrationId
  property_count: 0
  slug: kombo-putintegrationsintegrationidenabledparameterintegrationid
- name: PutIntegrationsIntegrationIdEnabledPositiveResponse
  property_count: 2
  slug: kombo-putintegrationsintegrationidenabledpositiveresponse
- name: PutIntegrationsIntegrationIdEnabledRequestBody
  property_count: 1
  slug: kombo-putintegrationsintegrationidenabledrequestbody
- name: Schema1
  property_count: 0
  slug: kombo-schema1
- name: Schema2
  property_count: 0
  slug: kombo-schema2
- name: Schema3
  property_count: 0
  slug: kombo-schema3
- name: Schema4
  property_count: 0
  slug: kombo-schema4
- name: Schema5
  property_count: 0
  slug: kombo-schema5
- name: Schema6
  property_count: 0
  slug: kombo-schema6
- name: SyncFinishedWebhookPayload
  property_count: 3
  slug: kombo-syncfinishedwebhookpayload
json_structures:
- name: Kombo Structure
  property_count: 0
  slug: kombo-structure
layout: provider
modified: '2026-05-19'
name: Kombo
nav: Providers
network: true
overview: 'Kombo publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AI Apply API, Custom Endpoints API, General API, and 5 more. Tagged areas include ATS, Embedded iPaaS, HRIS, LMS, and Payroll.


  The Kombo catalog on APIs.io includes 1 Spectral governance ruleset.


  Kombo''s developer surface includes authentication, documentation, support, engineering blog, and 10 more developer resources.'
plans:
- name: Kombo Plans Pricing
  plan_count: 3
  slug: kombo-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Kombo Rate Limits
  slug: kombo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Kombo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: kombo-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.0
  delta: 2.4
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 9.8
    contract_quality: 57.4
    developer_ergonomics: 47.6
    discoverability: 72.2
    governance: 9.8
    operational_transparency: 18.4
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kombo/refs/heads/main/screenshots/kombo-2026-06-20T184122.png
security:
- kind: authentication
  name: Kombo Authentication
  slug: kombo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kombo Domain Security
  slug: kombo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kombo Trust Center
  slug: kombo-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: kombo
tags:
- ATS
- Embedded iPaaS
- HRIS
- LMS
- Payroll
- Unified-API
website: https://www.kombo.dev
---
