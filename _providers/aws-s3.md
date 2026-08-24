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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 54
  human_in_the_loop: 2
  name: Aws S3 Agentic Access
  operation_count: 97
  slug: aws-s3-agentic-access
  summary_line: 97 operations · 54 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: The Amazon Simple Storage Service API from Amazon S3 API — 48 operation(s) for amazon simple storage service.
  name: Amazon S3 API Amazon Simple Storage Service API
  slug: aws-s3-amazon-simple-storage-service-api
- description: The WriteGetObjectResponse#x Amz Request Route&x Amz Request Token API from Amazon S3 API — 1 operation(s) for writegetobjectresponse#x amz request route&x amz request token.
  name: Amazon S3 API WriteGetObjectResponse#x Amz Request Route&x Amz Request Token API
  slug: aws-s3-writegetobjectresponse-x-amz-request-route-x-amz-request-token-api
artifact_total: 1755
collections:
- collection_type: postman
  name: Amazon Simple Storage Service API
  slug: postman-aws-s3-amazon-simple-storage-service-api
- collection_type: postman
  name: Amazon Simple Storage Service WriteGetObjectResponse#x Amz Request Route&x Amz Request Token API
  slug: postman-aws-s3-writegetobjectresponse-x-amz-request-route-x-amz-request-token-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Simple Storage Service API
  slug: open-aws-s3-amazon-simple-storage-service-api
- collection_type: open
  name: Amazon Simple Storage Service WriteGetObjectResponse#x Amz Request Route&x Amz Request Token API
  slug: open-aws-s3-writegetobjectresponse-x-amz-request-route-x-amz-request-token-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-s3-api/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-s3-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-s3-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-s3-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-s3-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-s3-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/s3/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/storage/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/s3/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/s3/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://aws.amazon.com/releasenotes/Amazon-S3/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/s3/
- group: design
  title: ''
  type: SpectralRules
  url: rules/aws-s3-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aws-s3-vocabulary.yaml
created: '2024-01-15'
description: Amazon Simple Storage Service (S3) is an object storage service offering industry-leading scalability, data availability, security, and performance for storing and retrieving any amount of data.
examples:
- key_count: 3
  name: S3 Abortdate Example
  slug: s3-abortdate-example
- key_count: 3
  name: S3 Abortincompletemultipartupload Example
  slug: s3-abortincompletemultipartupload-example
- key_count: 3
  name: S3 Abortmultipartuploadoutput Example
  slug: s3-abortmultipartuploadoutput-example
- key_count: 3
  name: S3 Abortmultipartuploadrequest Example
  slug: s3-abortmultipartuploadrequest-example
- key_count: 3
  name: S3 Abortruleid Example
  slug: s3-abortruleid-example
- key_count: 3
  name: S3 Accelerateconfiguration Example
  slug: s3-accelerateconfiguration-example
- key_count: 3
  name: S3 Acceptranges Example
  slug: s3-acceptranges-example
- key_count: 3
  name: S3 Accesscontrolpolicy Example
  slug: s3-accesscontrolpolicy-example
- key_count: 3
  name: S3 Accesscontroltranslation Example
  slug: s3-accesscontroltranslation-example
- key_count: 3
  name: S3 Accesspointarn Example
  slug: s3-accesspointarn-example
- key_count: 3
  name: S3 Accountid Example
  slug: s3-accountid-example
- key_count: 3
  name: S3 Allowedheader Example
  slug: s3-allowedheader-example
- key_count: 3
  name: S3 Allowedheaders Example
  slug: s3-allowedheaders-example
- key_count: 3
  name: S3 Allowedmethod Example
  slug: s3-allowedmethod-example
- key_count: 3
  name: S3 Allowedmethods Example
  slug: s3-allowedmethods-example
- key_count: 3
  name: S3 Allowedorigin Example
  slug: s3-allowedorigin-example
- key_count: 3
  name: S3 Allowedorigins Example
  slug: s3-allowedorigins-example
- key_count: 3
  name: S3 Allowquotedrecorddelimiter Example
  slug: s3-allowquotedrecorddelimiter-example
- key_count: 3
  name: S3 Analyticsandoperator Example
  slug: s3-analyticsandoperator-example
- key_count: 3
  name: S3 Analyticsconfiguration Example
  slug: s3-analyticsconfiguration-example
- key_count: 3
  name: S3 Analyticsconfigurationlist Example
  slug: s3-analyticsconfigurationlist-example
- key_count: 3
  name: S3 Analyticsexportdestination Example
  slug: s3-analyticsexportdestination-example
- key_count: 3
  name: S3 Analyticsfilter Example
  slug: s3-analyticsfilter-example
- key_count: 3
  name: S3 Analyticsid Example
  slug: s3-analyticsid-example
- key_count: 3
  name: S3 Analyticss3Bucketdestination Example
  slug: s3-analyticss3bucketdestination-example
- key_count: 3
  name: S3 Analyticss3Exportfileformat Example
  slug: s3-analyticss3exportfileformat-example
- key_count: 3
  name: S3 Archivestatus Example
  slug: s3-archivestatus-example
- key_count: 3
  name: S3 Body Example
  slug: s3-body-example
- key_count: 3
  name: S3 Bucket Example
  slug: s3-bucket-example
- key_count: 3
  name: S3 Bucketacceleratestatus Example
  slug: s3-bucketacceleratestatus-example
- key_count: 3
  name: S3 Bucketalreadyexists Example
  slug: s3-bucketalreadyexists-example
- key_count: 3
  name: S3 Bucketalreadyownedbyyou Example
  slug: s3-bucketalreadyownedbyyou-example
- key_count: 3
  name: S3 Bucketcannedacl Example
  slug: s3-bucketcannedacl-example
- key_count: 3
  name: S3 Bucketkeyenabled Example
  slug: s3-bucketkeyenabled-example
- key_count: 3
  name: S3 Bucketlifecycleconfiguration Example
  slug: s3-bucketlifecycleconfiguration-example
- key_count: 3
  name: S3 Bucketlocationconstraint Example
  slug: s3-bucketlocationconstraint-example
- key_count: 3
  name: S3 Bucketloggingstatus Example
  slug: s3-bucketloggingstatus-example
- key_count: 3
  name: S3 Bucketlogspermission Example
  slug: s3-bucketlogspermission-example
- key_count: 3
  name: S3 Bucketname Example
  slug: s3-bucketname-example
- key_count: 3
  name: S3 Buckets Example
  slug: s3-buckets-example
- key_count: 3
  name: S3 Bucketversioningstatus Example
  slug: s3-bucketversioningstatus-example
- key_count: 3
  name: S3 Bypassgovernanceretention Example
  slug: s3-bypassgovernanceretention-example
- key_count: 3
  name: S3 Bytesprocessed Example
  slug: s3-bytesprocessed-example
- key_count: 3
  name: S3 Bytesreturned Example
  slug: s3-bytesreturned-example
- key_count: 3
  name: S3 Bytesscanned Example
  slug: s3-bytesscanned-example
- key_count: 3
  name: S3 Cachecontrol Example
  slug: s3-cachecontrol-example
- key_count: 3
  name: S3 Checksum Example
  slug: s3-checksum-example
- key_count: 3
  name: S3 Checksumalgorithm Example
  slug: s3-checksumalgorithm-example
- key_count: 3
  name: S3 Checksumalgorithmlist Example
  slug: s3-checksumalgorithmlist-example
- key_count: 3
  name: S3 Checksumcrc32 Example
  slug: s3-checksumcrc32-example
- key_count: 3
  name: S3 Checksumcrc32C Example
  slug: s3-checksumcrc32c-example
- key_count: 3
  name: S3 Checksummode Example
  slug: s3-checksummode-example
- key_count: 3
  name: S3 Checksumsha1 Example
  slug: s3-checksumsha1-example
- key_count: 3
  name: S3 Checksumsha256 Example
  slug: s3-checksumsha256-example
- key_count: 3
  name: S3 Cloudfunction Example
  slug: s3-cloudfunction-example
- key_count: 3
  name: S3 Cloudfunctionconfiguration Example
  slug: s3-cloudfunctionconfiguration-example
- key_count: 3
  name: S3 Cloudfunctioninvocationrole Example
  slug: s3-cloudfunctioninvocationrole-example
- key_count: 3
  name: S3 Code Example
  slug: s3-code-example
- key_count: 3
  name: S3 Comments Example
  slug: s3-comments-example
- key_count: 3
  name: S3 Commonprefix Example
  slug: s3-commonprefix-example
- key_count: 3
  name: S3 Commonprefixlist Example
  slug: s3-commonprefixlist-example
- key_count: 3
  name: S3 Completedmultipartupload Example
  slug: s3-completedmultipartupload-example
- key_count: 3
  name: S3 Completedpart Example
  slug: s3-completedpart-example
- key_count: 3
  name: S3 Completedpartlist Example
  slug: s3-completedpartlist-example
- key_count: 3
  name: S3 Completemultipartuploadoutput Example
  slug: s3-completemultipartuploadoutput-example
- key_count: 3
  name: S3 Completemultipartuploadrequest Example
  slug: s3-completemultipartuploadrequest-example
- key_count: 3
  name: S3 Compressiontype Example
  slug: s3-compressiontype-example
- key_count: 3
  name: S3 Condition Example
  slug: s3-condition-example
- key_count: 3
  name: S3 Confirmremoveselfbucketaccess Example
  slug: s3-confirmremoveselfbucketaccess-example
- key_count: 3
  name: S3 Contentdisposition Example
  slug: s3-contentdisposition-example
- key_count: 3
  name: S3 Contentencoding Example
  slug: s3-contentencoding-example
- key_count: 3
  name: S3 Contentlanguage Example
  slug: s3-contentlanguage-example
- key_count: 3
  name: S3 Contentlength Example
  slug: s3-contentlength-example
- key_count: 3
  name: S3 Contentmd5 Example
  slug: s3-contentmd5-example
- key_count: 3
  name: S3 Contentrange Example
  slug: s3-contentrange-example
- key_count: 3
  name: S3 Contenttype Example
  slug: s3-contenttype-example
- key_count: 3
  name: S3 Continuationevent Example
  slug: s3-continuationevent-example
- key_count: 3
  name: S3 Copyobjectoutput Example
  slug: s3-copyobjectoutput-example
- key_count: 3
  name: S3 Copyobjectrequest Example
  slug: s3-copyobjectrequest-example
- key_count: 3
  name: S3 Copyobjectresult Example
  slug: s3-copyobjectresult-example
- key_count: 3
  name: S3 Copypartresult Example
  slug: s3-copypartresult-example
- key_count: 3
  name: S3 Copysource Example
  slug: s3-copysource-example
- key_count: 3
  name: S3 Copysourceifmatch Example
  slug: s3-copysourceifmatch-example
- key_count: 3
  name: S3 Copysourceifmodifiedsince Example
  slug: s3-copysourceifmodifiedsince-example
- key_count: 3
  name: S3 Copysourceifnonematch Example
  slug: s3-copysourceifnonematch-example
- key_count: 3
  name: S3 Copysourceifunmodifiedsince Example
  slug: s3-copysourceifunmodifiedsince-example
- key_count: 3
  name: S3 Copysourcerange Example
  slug: s3-copysourcerange-example
- key_count: 3
  name: S3 Copysourcessecustomeralgorithm Example
  slug: s3-copysourcessecustomeralgorithm-example
- key_count: 3
  name: S3 Copysourcessecustomerkey Example
  slug: s3-copysourcessecustomerkey-example
- key_count: 3
  name: S3 Copysourcessecustomerkeymd5 Example
  slug: s3-copysourcessecustomerkeymd5-example
- key_count: 3
  name: S3 Copysourceversionid Example
  slug: s3-copysourceversionid-example
- key_count: 3
  name: S3 Corsconfiguration Example
  slug: s3-corsconfiguration-example
- key_count: 3
  name: S3 Corsrule Example
  slug: s3-corsrule-example
- key_count: 3
  name: S3 Corsrules Example
  slug: s3-corsrules-example
- key_count: 3
  name: S3 Createbucketconfiguration Example
  slug: s3-createbucketconfiguration-example
- key_count: 3
  name: S3 Createbucketoutput Example
  slug: s3-createbucketoutput-example
- key_count: 3
  name: S3 Createbucketrequest Example
  slug: s3-createbucketrequest-example
- key_count: 3
  name: S3 Createmultipartuploadoutput Example
  slug: s3-createmultipartuploadoutput-example
- key_count: 3
  name: S3 Createmultipartuploadrequest Example
  slug: s3-createmultipartuploadrequest-example
- key_count: 3
  name: S3 Creationdate Example
  slug: s3-creationdate-example
- key_count: 3
  name: S3 Csvinput Example
  slug: s3-csvinput-example
- key_count: 3
  name: S3 Csvoutput Example
  slug: s3-csvoutput-example
- key_count: 3
  name: S3 Date Example
  slug: s3-date-example
- key_count: 3
  name: S3 Days Example
  slug: s3-days-example
- key_count: 3
  name: S3 Daysafterinitiation Example
  slug: s3-daysafterinitiation-example
- key_count: 3
  name: S3 Defaultretention Example
  slug: s3-defaultretention-example
- key_count: 3
  name: S3 Delete Example
  slug: s3-delete-example
- key_count: 3
  name: S3 Deletebucketanalyticsconfigurationrequest Example
  slug: s3-deletebucketanalyticsconfigurationrequest-example
- key_count: 3
  name: S3 Deletebucketcorsrequest Example
  slug: s3-deletebucketcorsrequest-example
- key_count: 3
  name: S3 Deletebucketencryptionrequest Example
  slug: s3-deletebucketencryptionrequest-example
- key_count: 3
  name: S3 Deletebucketintelligenttieringconfigurationrequest Example
  slug: s3-deletebucketintelligenttieringconfigurationrequest-example
- key_count: 3
  name: S3 Deletebucketinventoryconfigurationrequest Example
  slug: s3-deletebucketinventoryconfigurationrequest-example
- key_count: 3
  name: S3 Deletebucketlifecyclerequest Example
  slug: s3-deletebucketlifecyclerequest-example
- key_count: 3
  name: S3 Deletebucketmetricsconfigurationrequest Example
  slug: s3-deletebucketmetricsconfigurationrequest-example
- key_count: 3
  name: S3 Deletebucketownershipcontrolsrequest Example
  slug: s3-deletebucketownershipcontrolsrequest-example
- key_count: 3
  name: S3 Deletebucketpolicyrequest Example
  slug: s3-deletebucketpolicyrequest-example
- key_count: 3
  name: S3 Deletebucketreplicationrequest Example
  slug: s3-deletebucketreplicationrequest-example
- key_count: 3
  name: S3 Deletebucketrequest Example
  slug: s3-deletebucketrequest-example
- key_count: 3
  name: S3 Deletebuckettaggingrequest Example
  slug: s3-deletebuckettaggingrequest-example
- key_count: 3
  name: S3 Deletebucketwebsiterequest Example
  slug: s3-deletebucketwebsiterequest-example
- key_count: 3
  name: S3 Deletedobject Example
  slug: s3-deletedobject-example
- key_count: 3
  name: S3 Deletedobjects Example
  slug: s3-deletedobjects-example
- key_count: 3
  name: S3 Deletemarker Example
  slug: s3-deletemarker-example
- key_count: 3
  name: S3 Deletemarkerentry Example
  slug: s3-deletemarkerentry-example
- key_count: 3
  name: S3 Deletemarkerreplication Example
  slug: s3-deletemarkerreplication-example
- key_count: 3
  name: S3 Deletemarkerreplicationstatus Example
  slug: s3-deletemarkerreplicationstatus-example
- key_count: 3
  name: S3 Deletemarkers Example
  slug: s3-deletemarkers-example
- key_count: 3
  name: S3 Deletemarkerversionid Example
  slug: s3-deletemarkerversionid-example
- key_count: 3
  name: S3 Deleteobjectoutput Example
  slug: s3-deleteobjectoutput-example
- key_count: 3
  name: S3 Deleteobjectrequest Example
  slug: s3-deleteobjectrequest-example
- key_count: 3
  name: S3 Deleteobjectsoutput Example
  slug: s3-deleteobjectsoutput-example
- key_count: 3
  name: S3 Deleteobjectsrequest Example
  slug: s3-deleteobjectsrequest-example
- key_count: 3
  name: S3 Deleteobjecttaggingoutput Example
  slug: s3-deleteobjecttaggingoutput-example
- key_count: 3
  name: S3 Deleteobjecttaggingrequest Example
  slug: s3-deleteobjecttaggingrequest-example
- key_count: 3
  name: S3 Deletepublicaccessblockrequest Example
  slug: s3-deletepublicaccessblockrequest-example
- key_count: 3
  name: S3 Delimiter Example
  slug: s3-delimiter-example
- key_count: 3
  name: S3 Description Example
  slug: s3-description-example
- key_count: 3
  name: S3 Destination Example
  slug: s3-destination-example
- key_count: 3
  name: S3 Displayname Example
  slug: s3-displayname-example
- key_count: 3
  name: S3 Emailaddress Example
  slug: s3-emailaddress-example
- key_count: 3
  name: S3 Enablerequestprogress Example
  slug: s3-enablerequestprogress-example
- key_count: 3
  name: S3 Encodingtype Example
  slug: s3-encodingtype-example
- key_count: 3
  name: S3 Encryption Example
  slug: s3-encryption-example
- key_count: 3
  name: S3 Encryptionconfiguration Example
  slug: s3-encryptionconfiguration-example
- key_count: 3
  name: S3 End Example
  slug: s3-end-example
- key_count: 3
  name: S3 Endevent Example
  slug: s3-endevent-example
- key_count: 3
  name: S3 Error Example
  slug: s3-error-example
- key_count: 3
  name: S3 Errorcode Example
  slug: s3-errorcode-example
- key_count: 3
  name: S3 Errordocument Example
  slug: s3-errordocument-example
- key_count: 3
  name: S3 Errormessage Example
  slug: s3-errormessage-example
- key_count: 3
  name: S3 Errors Example
  slug: s3-errors-example
- key_count: 3
  name: S3 Etag Example
  slug: s3-etag-example
- key_count: 3
  name: S3 Event Example
  slug: s3-event-example
- key_count: 3
  name: S3 Eventbridgeconfiguration Example
  slug: s3-eventbridgeconfiguration-example
- key_count: 3
  name: S3 Eventlist Example
  slug: s3-eventlist-example
- key_count: 3
  name: S3 Existingobjectreplication Example
  slug: s3-existingobjectreplication-example
- key_count: 3
  name: S3 Existingobjectreplicationstatus Example
  slug: s3-existingobjectreplicationstatus-example
- key_count: 3
  name: S3 Expiration Example
  slug: s3-expiration-example
- key_count: 3
  name: S3 Expirationstatus Example
  slug: s3-expirationstatus-example
- key_count: 3
  name: S3 Expiredobjectdeletemarker Example
  slug: s3-expiredobjectdeletemarker-example
- key_count: 3
  name: S3 Expires Example
  slug: s3-expires-example
- key_count: 3
  name: S3 Exposeheader Example
  slug: s3-exposeheader-example
- key_count: 3
  name: S3 Exposeheaders Example
  slug: s3-exposeheaders-example
- key_count: 3
  name: S3 Expression Example
  slug: s3-expression-example
- key_count: 3
  name: S3 Expressiontype Example
  slug: s3-expressiontype-example
- key_count: 3
  name: S3 Fetchowner Example
  slug: s3-fetchowner-example
- key_count: 3
  name: S3 Fielddelimiter Example
  slug: s3-fielddelimiter-example
- key_count: 3
  name: S3 Fileheaderinfo Example
  slug: s3-fileheaderinfo-example
- key_count: 3
  name: S3 Filterrule Example
  slug: s3-filterrule-example
- key_count: 3
  name: S3 Filterrulelist Example
  slug: s3-filterrulelist-example
- key_count: 3
  name: S3 Filterrulename Example
  slug: s3-filterrulename-example
- key_count: 3
  name: S3 Filterrulevalue Example
  slug: s3-filterrulevalue-example
- key_count: 3
  name: S3 Getbucketaccelerateconfigurationoutput Example
  slug: s3-getbucketaccelerateconfigurationoutput-example
- key_count: 3
  name: S3 Getbucketaccelerateconfigurationrequest Example
  slug: s3-getbucketaccelerateconfigurationrequest-example
- key_count: 3
  name: S3 Getbucketacloutput Example
  slug: s3-getbucketacloutput-example
- key_count: 3
  name: S3 Getbucketaclrequest Example
  slug: s3-getbucketaclrequest-example
- key_count: 3
  name: S3 Getbucketanalyticsconfigurationoutput Example
  slug: s3-getbucketanalyticsconfigurationoutput-example
- key_count: 3
  name: S3 Getbucketanalyticsconfigurationrequest Example
  slug: s3-getbucketanalyticsconfigurationrequest-example
- key_count: 3
  name: S3 Getbucketcorsoutput Example
  slug: s3-getbucketcorsoutput-example
- key_count: 3
  name: S3 Getbucketcorsrequest Example
  slug: s3-getbucketcorsrequest-example
- key_count: 3
  name: S3 Getbucketencryptionoutput Example
  slug: s3-getbucketencryptionoutput-example
- key_count: 3
  name: S3 Getbucketencryptionrequest Example
  slug: s3-getbucketencryptionrequest-example
- key_count: 3
  name: S3 Getbucketintelligenttieringconfigurationoutput Example
  slug: s3-getbucketintelligenttieringconfigurationoutput-example
- key_count: 3
  name: S3 Getbucketintelligenttieringconfigurationrequest Example
  slug: s3-getbucketintelligenttieringconfigurationrequest-example
- key_count: 3
  name: S3 Getbucketinventoryconfigurationoutput Example
  slug: s3-getbucketinventoryconfigurationoutput-example
- key_count: 3
  name: S3 Getbucketinventoryconfigurationrequest Example
  slug: s3-getbucketinventoryconfigurationrequest-example
- key_count: 3
  name: S3 Getbucketlifecycleconfigurationoutput Example
  slug: s3-getbucketlifecycleconfigurationoutput-example
- key_count: 3
  name: S3 Getbucketlifecycleconfigurationrequest Example
  slug: s3-getbucketlifecycleconfigurationrequest-example
- key_count: 3
  name: S3 Getbucketlifecycleoutput Example
  slug: s3-getbucketlifecycleoutput-example
- key_count: 3
  name: S3 Getbucketlifecyclerequest Example
  slug: s3-getbucketlifecyclerequest-example
- key_count: 3
  name: S3 Getbucketlocationoutput Example
  slug: s3-getbucketlocationoutput-example
- key_count: 3
  name: S3 Getbucketlocationrequest Example
  slug: s3-getbucketlocationrequest-example
- key_count: 3
  name: S3 Getbucketloggingoutput Example
  slug: s3-getbucketloggingoutput-example
- key_count: 3
  name: S3 Getbucketloggingrequest Example
  slug: s3-getbucketloggingrequest-example
- key_count: 3
  name: S3 Getbucketmetricsconfigurationoutput Example
  slug: s3-getbucketmetricsconfigurationoutput-example
- key_count: 3
  name: S3 Getbucketmetricsconfigurationrequest Example
  slug: s3-getbucketmetricsconfigurationrequest-example
- key_count: 3
  name: S3 Getbucketnotificationconfigurationrequest Example
  slug: s3-getbucketnotificationconfigurationrequest-example
- key_count: 3
  name: S3 Getbucketownershipcontrolsoutput Example
  slug: s3-getbucketownershipcontrolsoutput-example
- key_count: 3
  name: S3 Getbucketownershipcontrolsrequest Example
  slug: s3-getbucketownershipcontrolsrequest-example
- key_count: 3
  name: S3 Getbucketpolicyoutput Example
  slug: s3-getbucketpolicyoutput-example
- key_count: 3
  name: S3 Getbucketpolicyrequest Example
  slug: s3-getbucketpolicyrequest-example
- key_count: 3
  name: S3 Getbucketpolicystatusoutput Example
  slug: s3-getbucketpolicystatusoutput-example
- key_count: 3
  name: S3 Getbucketpolicystatusrequest Example
  slug: s3-getbucketpolicystatusrequest-example
- key_count: 3
  name: S3 Getbucketreplicationoutput Example
  slug: s3-getbucketreplicationoutput-example
- key_count: 3
  name: S3 Getbucketreplicationrequest Example
  slug: s3-getbucketreplicationrequest-example
- key_count: 3
  name: S3 Getbucketrequestpaymentoutput Example
  slug: s3-getbucketrequestpaymentoutput-example
- key_count: 3
  name: S3 Getbucketrequestpaymentrequest Example
  slug: s3-getbucketrequestpaymentrequest-example
- key_count: 3
  name: S3 Getbuckettaggingoutput Example
  slug: s3-getbuckettaggingoutput-example
- key_count: 3
  name: S3 Getbuckettaggingrequest Example
  slug: s3-getbuckettaggingrequest-example
- key_count: 3
  name: S3 Getbucketversioningoutput Example
  slug: s3-getbucketversioningoutput-example
- key_count: 3
  name: S3 Getbucketversioningrequest Example
  slug: s3-getbucketversioningrequest-example
- key_count: 3
  name: S3 Getbucketwebsiteoutput Example
  slug: s3-getbucketwebsiteoutput-example
- key_count: 3
  name: S3 Getbucketwebsiterequest Example
  slug: s3-getbucketwebsiterequest-example
- key_count: 3
  name: S3 Getobjectacloutput Example
  slug: s3-getobjectacloutput-example
- key_count: 3
  name: S3 Getobjectaclrequest Example
  slug: s3-getobjectaclrequest-example
- key_count: 3
  name: S3 Getobjectattributesoutput Example
  slug: s3-getobjectattributesoutput-example
- key_count: 3
  name: S3 Getobjectattributesparts Example
  slug: s3-getobjectattributesparts-example
- key_count: 3
  name: S3 Getobjectattributesrequest Example
  slug: s3-getobjectattributesrequest-example
- key_count: 3
  name: S3 Getobjectlegalholdoutput Example
  slug: s3-getobjectlegalholdoutput-example
- key_count: 3
  name: S3 Getobjectlegalholdrequest Example
  slug: s3-getobjectlegalholdrequest-example
- key_count: 3
  name: S3 Getobjectlockconfigurationoutput Example
  slug: s3-getobjectlockconfigurationoutput-example
- key_count: 3
  name: S3 Getobjectlockconfigurationrequest Example
  slug: s3-getobjectlockconfigurationrequest-example
- key_count: 3
  name: S3 Getobjectoutput Example
  slug: s3-getobjectoutput-example
- key_count: 3
  name: S3 Getobjectrequest Example
  slug: s3-getobjectrequest-example
- key_count: 3
  name: S3 Getobjectresponsestatuscode Example
  slug: s3-getobjectresponsestatuscode-example
- key_count: 3
  name: S3 Getobjectretentionoutput Example
  slug: s3-getobjectretentionoutput-example
- key_count: 3
  name: S3 Getobjectretentionrequest Example
  slug: s3-getobjectretentionrequest-example
- key_count: 3
  name: S3 Getobjecttaggingoutput Example
  slug: s3-getobjecttaggingoutput-example
- key_count: 3
  name: S3 Getobjecttaggingrequest Example
  slug: s3-getobjecttaggingrequest-example
- key_count: 3
  name: S3 Getobjecttorrentoutput Example
  slug: s3-getobjecttorrentoutput-example
- key_count: 3
  name: S3 Getobjecttorrentrequest Example
  slug: s3-getobjecttorrentrequest-example
- key_count: 3
  name: S3 Getpublicaccessblockoutput Example
  slug: s3-getpublicaccessblockoutput-example
- key_count: 3
  name: S3 Getpublicaccessblockrequest Example
  slug: s3-getpublicaccessblockrequest-example
- key_count: 3
  name: S3 Glacierjobparameters Example
  slug: s3-glacierjobparameters-example
- key_count: 3
  name: S3 Grant Example
  slug: s3-grant-example
- key_count: 3
  name: S3 Grantee Example
  slug: s3-grantee-example
- key_count: 3
  name: S3 Grantfullcontrol Example
  slug: s3-grantfullcontrol-example
- key_count: 3
  name: S3 Grantread Example
  slug: s3-grantread-example
- key_count: 3
  name: S3 Grantreadacp Example
  slug: s3-grantreadacp-example
- key_count: 3
  name: S3 Grants Example
  slug: s3-grants-example
- key_count: 3
  name: S3 Grantwrite Example
  slug: s3-grantwrite-example
- key_count: 3
  name: S3 Grantwriteacp Example
  slug: s3-grantwriteacp-example
- key_count: 3
  name: S3 Headbucketrequest Example
  slug: s3-headbucketrequest-example
- key_count: 3
  name: S3 Headobjectoutput Example
  slug: s3-headobjectoutput-example
- key_count: 3
  name: S3 Headobjectrequest Example
  slug: s3-headobjectrequest-example
- key_count: 3
  name: S3 Hostname Example
  slug: s3-hostname-example
- key_count: 3
  name: S3 Httperrorcodereturnedequals Example
  slug: s3-httperrorcodereturnedequals-example
- key_count: 3
  name: S3 Httpredirectcode Example
  slug: s3-httpredirectcode-example
- key_count: 3
  name: S3 Id Example
  slug: s3-id-example
- key_count: 3
  name: S3 Ifmatch Example
  slug: s3-ifmatch-example
- key_count: 3
  name: S3 Ifmodifiedsince Example
  slug: s3-ifmodifiedsince-example
- key_count: 3
  name: S3 Ifnonematch Example
  slug: s3-ifnonematch-example
- key_count: 3
  name: S3 Ifunmodifiedsince Example
  slug: s3-ifunmodifiedsince-example
- key_count: 3
  name: S3 Indexdocument Example
  slug: s3-indexdocument-example
- key_count: 3
  name: S3 Initiated Example
  slug: s3-initiated-example
- key_count: 3
  name: S3 Initiator Example
  slug: s3-initiator-example
- key_count: 3
  name: S3 Inputserialization Example
  slug: s3-inputserialization-example
- key_count: 3
  name: S3 Intelligenttieringaccesstier Example
  slug: s3-intelligenttieringaccesstier-example
- key_count: 3
  name: S3 Intelligenttieringandoperator Example
  slug: s3-intelligenttieringandoperator-example
- key_count: 3
  name: S3 Intelligenttieringconfiguration Example
  slug: s3-intelligenttieringconfiguration-example
- key_count: 3
  name: S3 Intelligenttieringconfigurationlist Example
  slug: s3-intelligenttieringconfigurationlist-example
- key_count: 3
  name: S3 Intelligenttieringdays Example
  slug: s3-intelligenttieringdays-example
- key_count: 3
  name: S3 Intelligenttieringfilter Example
  slug: s3-intelligenttieringfilter-example
- key_count: 3
  name: S3 Intelligenttieringid Example
  slug: s3-intelligenttieringid-example
- key_count: 3
  name: S3 Intelligenttieringstatus Example
  slug: s3-intelligenttieringstatus-example
- key_count: 3
  name: S3 Invalidobjectstate Example
  slug: s3-invalidobjectstate-example
- key_count: 3
  name: S3 Inventoryconfiguration Example
  slug: s3-inventoryconfiguration-example
- key_count: 3
  name: S3 Inventoryconfigurationlist Example
  slug: s3-inventoryconfigurationlist-example
- key_count: 3
  name: S3 Inventorydestination Example
  slug: s3-inventorydestination-example
- key_count: 3
  name: S3 Inventoryencryption Example
  slug: s3-inventoryencryption-example
- key_count: 3
  name: S3 Inventoryfilter Example
  slug: s3-inventoryfilter-example
- key_count: 3
  name: S3 Inventoryformat Example
  slug: s3-inventoryformat-example
- key_count: 3
  name: S3 Inventoryfrequency Example
  slug: s3-inventoryfrequency-example
- key_count: 3
  name: S3 Inventoryid Example
  slug: s3-inventoryid-example
- key_count: 3
  name: S3 Inventoryincludedobjectversions Example
  slug: s3-inventoryincludedobjectversions-example
- key_count: 3
  name: S3 Inventoryoptionalfield Example
  slug: s3-inventoryoptionalfield-example
- key_count: 3
  name: S3 Inventoryoptionalfields Example
  slug: s3-inventoryoptionalfields-example
- key_count: 3
  name: S3 Inventorys3Bucketdestination Example
  slug: s3-inventorys3bucketdestination-example
- key_count: 3
  name: S3 Inventoryschedule Example
  slug: s3-inventoryschedule-example
- key_count: 3
  name: S3 Isenabled Example
  slug: s3-isenabled-example
- key_count: 3
  name: S3 Islatest Example
  slug: s3-islatest-example
- key_count: 3
  name: S3 Ispublic Example
  slug: s3-ispublic-example
- key_count: 3
  name: S3 Istruncated Example
  slug: s3-istruncated-example
- key_count: 3
  name: S3 Jsoninput Example
  slug: s3-jsoninput-example
- key_count: 3
  name: S3 Jsonoutput Example
  slug: s3-jsonoutput-example
- key_count: 3
  name: S3 Jsontype Example
  slug: s3-jsontype-example
- key_count: 3
  name: S3 Keycount Example
  slug: s3-keycount-example
- key_count: 3
  name: S3 Keymarker Example
  slug: s3-keymarker-example
- key_count: 3
  name: S3 Keyprefixequals Example
  slug: s3-keyprefixequals-example
- key_count: 3
  name: S3 Kmscontext Example
  slug: s3-kmscontext-example
- key_count: 3
  name: S3 Lambdafunctionarn Example
  slug: s3-lambdafunctionarn-example
- key_count: 3
  name: S3 Lambdafunctionconfiguration Example
  slug: s3-lambdafunctionconfiguration-example
- key_count: 3
  name: S3 Lambdafunctionconfigurationlist Example
  slug: s3-lambdafunctionconfigurationlist-example
- key_count: 3
  name: S3 Lastmodified Example
  slug: s3-lastmodified-example
- key_count: 3
  name: S3 Lifecycleconfiguration Example
  slug: s3-lifecycleconfiguration-example
- key_count: 3
  name: S3 Lifecycleexpiration Example
  slug: s3-lifecycleexpiration-example
- key_count: 3
  name: S3 Lifecyclerule Example
  slug: s3-lifecyclerule-example
- key_count: 3
  name: S3 Lifecycleruleandoperator Example
  slug: s3-lifecycleruleandoperator-example
- key_count: 3
  name: S3 Lifecyclerulefilter Example
  slug: s3-lifecyclerulefilter-example
- key_count: 3
  name: S3 Lifecyclerules Example
  slug: s3-lifecyclerules-example
- key_count: 3
  name: S3 Listbucketanalyticsconfigurationsoutput Example
  slug: s3-listbucketanalyticsconfigurationsoutput-example
- key_count: 3
  name: S3 Listbucketanalyticsconfigurationsrequest Example
  slug: s3-listbucketanalyticsconfigurationsrequest-example
- key_count: 3
  name: S3 Listbucketintelligenttieringconfigurationsoutput Example
  slug: s3-listbucketintelligenttieringconfigurationsoutput-example
- key_count: 3
  name: S3 Listbucketintelligenttieringconfigurationsrequest Example
  slug: s3-listbucketintelligenttieringconfigurationsrequest-example
- key_count: 3
  name: S3 Listbucketinventoryconfigurationsoutput Example
  slug: s3-listbucketinventoryconfigurationsoutput-example
- key_count: 3
  name: S3 Listbucketinventoryconfigurationsrequest Example
  slug: s3-listbucketinventoryconfigurationsrequest-example
- key_count: 3
  name: S3 Listbucketmetricsconfigurationsoutput Example
  slug: s3-listbucketmetricsconfigurationsoutput-example
- key_count: 3
  name: S3 Listbucketmetricsconfigurationsrequest Example
  slug: s3-listbucketmetricsconfigurationsrequest-example
- key_count: 3
  name: S3 Listbucketsoutput Example
  slug: s3-listbucketsoutput-example
- key_count: 3
  name: S3 Listmultipartuploadsoutput Example
  slug: s3-listmultipartuploadsoutput-example
- key_count: 3
  name: S3 Listmultipartuploadsrequest Example
  slug: s3-listmultipartuploadsrequest-example
- key_count: 3
  name: S3 Listobjectsoutput Example
  slug: s3-listobjectsoutput-example
- key_count: 3
  name: S3 Listobjectsrequest Example
  slug: s3-listobjectsrequest-example
- key_count: 3
  name: S3 Listobjectsv2Output Example
  slug: s3-listobjectsv2output-example
- key_count: 3
  name: S3 Listobjectsv2Request Example
  slug: s3-listobjectsv2request-example
- key_count: 3
  name: S3 Listobjectversionsoutput Example
  slug: s3-listobjectversionsoutput-example
- key_count: 3
  name: S3 Listobjectversionsrequest Example
  slug: s3-listobjectversionsrequest-example
- key_count: 3
  name: S3 Listpartsoutput Example
  slug: s3-listpartsoutput-example
- key_count: 3
  name: S3 Listpartsrequest Example
  slug: s3-listpartsrequest-example
- key_count: 3
  name: S3 Location Example
  slug: s3-location-example
- key_count: 3
  name: S3 Locationprefix Example
  slug: s3-locationprefix-example
- key_count: 3
  name: S3 Loggingenabled Example
  slug: s3-loggingenabled-example
- key_count: 3
  name: S3 Marker Example
  slug: s3-marker-example
- key_count: 3
  name: S3 Maxageseconds Example
  slug: s3-maxageseconds-example
- key_count: 3
  name: S3 Maxkeys Example
  slug: s3-maxkeys-example
- key_count: 3
  name: S3 Maxparts Example
  slug: s3-maxparts-example
- key_count: 3
  name: S3 Maxuploads Example
  slug: s3-maxuploads-example
- key_count: 3
  name: S3 Message Example
  slug: s3-message-example
- key_count: 3
  name: S3 Metadata Example
  slug: s3-metadata-example
- key_count: 3
  name: S3 Metadatadirective Example
  slug: s3-metadatadirective-example
- key_count: 3
  name: S3 Metadataentry Example
  slug: s3-metadataentry-example
- key_count: 3
  name: S3 Metadatakey Example
  slug: s3-metadatakey-example
- key_count: 3
  name: S3 Metadatavalue Example
  slug: s3-metadatavalue-example
- key_count: 3
  name: S3 Metrics Example
  slug: s3-metrics-example
- key_count: 3
  name: S3 Metricsandoperator Example
  slug: s3-metricsandoperator-example
- key_count: 3
  name: S3 Metricsconfiguration Example
  slug: s3-metricsconfiguration-example
- key_count: 3
  name: S3 Metricsconfigurationlist Example
  slug: s3-metricsconfigurationlist-example
- key_count: 3
  name: S3 Metricsfilter Example
  slug: s3-metricsfilter-example
- key_count: 3
  name: S3 Metricsid Example
  slug: s3-metricsid-example
- key_count: 3
  name: S3 Metricsstatus Example
  slug: s3-metricsstatus-example
- key_count: 3
  name: S3 Mfa Example
  slug: s3-mfa-example
- key_count: 3
  name: S3 Mfadelete Example
  slug: s3-mfadelete-example
- key_count: 3
  name: S3 Mfadeletestatus Example
  slug: s3-mfadeletestatus-example
- key_count: 3
  name: S3 Minutes Example
  slug: s3-minutes-example
- key_count: 3
  name: S3 Missingmeta Example
  slug: s3-missingmeta-example
- key_count: 3
  name: S3 Multipartupload Example
  slug: s3-multipartupload-example
- key_count: 3
  name: S3 Multipartuploadid Example
  slug: s3-multipartuploadid-example
- key_count: 3
  name: S3 Multipartuploadlist Example
  slug: s3-multipartuploadlist-example
- key_count: 3
  name: S3 Nextkeymarker Example
  slug: s3-nextkeymarker-example
- key_count: 3
  name: S3 Nextmarker Example
  slug: s3-nextmarker-example
- key_count: 3
  name: S3 Nextpartnumbermarker Example
  slug: s3-nextpartnumbermarker-example
- key_count: 3
  name: S3 Nexttoken Example
  slug: s3-nexttoken-example
- key_count: 3
  name: S3 Nextuploadidmarker Example
  slug: s3-nextuploadidmarker-example
- key_count: 3
  name: S3 Nextversionidmarker Example
  slug: s3-nextversionidmarker-example
- key_count: 3
  name: S3 Noncurrentversionexpiration Example
  slug: s3-noncurrentversionexpiration-example
- key_count: 3
  name: S3 Noncurrentversiontransition Example
  slug: s3-noncurrentversiontransition-example
- key_count: 3
  name: S3 Noncurrentversiontransitionlist Example
  slug: s3-noncurrentversiontransitionlist-example
- key_count: 3
  name: S3 Nosuchbucket Example
  slug: s3-nosuchbucket-example
- key_count: 3
  name: S3 Nosuchkey Example
  slug: s3-nosuchkey-example
- key_count: 3
  name: S3 Nosuchupload Example
  slug: s3-nosuchupload-example
- key_count: 3
  name: S3 Notificationconfiguration Example
  slug: s3-notificationconfiguration-example
- key_count: 3
  name: S3 Notificationconfigurationdeprecated Example
  slug: s3-notificationconfigurationdeprecated-example
- key_count: 3
  name: S3 Notificationconfigurationfilter Example
  slug: s3-notificationconfigurationfilter-example
- key_count: 3
  name: S3 Notificationid Example
  slug: s3-notificationid-example
- key_count: 3
  name: S3 Object Example
  slug: s3-object-example
- key_count: 3
  name: S3 Objectalreadyinactivetiererror Example
  slug: s3-objectalreadyinactivetiererror-example
- key_count: 3
  name: S3 Objectattributes Example
  slug: s3-objectattributes-example
- key_count: 3
  name: S3 Objectattributeslist Example
  slug: s3-objectattributeslist-example
- key_count: 3
  name: S3 Objectcannedacl Example
  slug: s3-objectcannedacl-example
- key_count: 3
  name: S3 Objectidentifier Example
  slug: s3-objectidentifier-example
- key_count: 3
  name: S3 Objectidentifierlist Example
  slug: s3-objectidentifierlist-example
- key_count: 3
  name: S3 Objectkey Example
  slug: s3-objectkey-example
- key_count: 3
  name: S3 Objectlist Example
  slug: s3-objectlist-example
- key_count: 3
  name: S3 Objectlockconfiguration Example
  slug: s3-objectlockconfiguration-example
- key_count: 3
  name: S3 Objectlockenabled Example
  slug: s3-objectlockenabled-example
- key_count: 3
  name: S3 Objectlockenabledforbucket Example
  slug: s3-objectlockenabledforbucket-example
- key_count: 3
  name: S3 Objectlocklegalhold Example
  slug: s3-objectlocklegalhold-example
- key_count: 3
  name: S3 Objectlocklegalholdstatus Example
  slug: s3-objectlocklegalholdstatus-example
- key_count: 3
  name: S3 Objectlockmode Example
  slug: s3-objectlockmode-example
- key_count: 3
  name: S3 Objectlockretainuntildate Example
  slug: s3-objectlockretainuntildate-example
- key_count: 3
  name: S3 Objectlockretention Example
  slug: s3-objectlockretention-example
- key_count: 3
  name: S3 Objectlockretentionmode Example
  slug: s3-objectlockretentionmode-example
- key_count: 3
  name: S3 Objectlockrule Example
  slug: s3-objectlockrule-example
- key_count: 3
  name: S3 Objectlocktoken Example
  slug: s3-objectlocktoken-example
- key_count: 3
  name: S3 Objectnotinactivetiererror Example
  slug: s3-objectnotinactivetiererror-example
- key_count: 3
  name: S3 Objectownership Example
  slug: s3-objectownership-example
- key_count: 3
  name: S3 Objectpart Example
  slug: s3-objectpart-example
- key_count: 3
  name: S3 Objectsize Example
  slug: s3-objectsize-example
- key_count: 3
  name: S3 Objectsizegreaterthanbytes Example
  slug: s3-objectsizegreaterthanbytes-example
- key_count: 3
  name: S3 Objectsizelessthanbytes Example
  slug: s3-objectsizelessthanbytes-example
- key_count: 3
  name: S3 Objectstorageclass Example
  slug: s3-objectstorageclass-example
- key_count: 3
  name: S3 Objectversion Example
  slug: s3-objectversion-example
- key_count: 3
  name: S3 Objectversionid Example
  slug: s3-objectversionid-example
- key_count: 3
  name: S3 Objectversionlist Example
  slug: s3-objectversionlist-example
- key_count: 3
  name: S3 Objectversionstorageclass Example
  slug: s3-objectversionstorageclass-example
- key_count: 3
  name: S3 Outputlocation Example
  slug: s3-outputlocation-example
- key_count: 3
  name: S3 Outputserialization Example
  slug: s3-outputserialization-example
- key_count: 3
  name: S3 Owner Example
  slug: s3-owner-example
- key_count: 3
  name: S3 Owneroverride Example
  slug: s3-owneroverride-example
- key_count: 3
  name: S3 Ownershipcontrols Example
  slug: s3-ownershipcontrols-example
- key_count: 3
  name: S3 Ownershipcontrolsrule Example
  slug: s3-ownershipcontrolsrule-example
- key_count: 3
  name: S3 Ownershipcontrolsrules Example
  slug: s3-ownershipcontrolsrules-example
- key_count: 3
  name: S3 Parquetinput Example
  slug: s3-parquetinput-example
- key_count: 3
  name: S3 Part Example
  slug: s3-part-example
- key_count: 3
  name: S3 Partnumber Example
  slug: s3-partnumber-example
- key_count: 3
  name: S3 Partnumbermarker Example
  slug: s3-partnumbermarker-example
- key_count: 3
  name: S3 Parts Example
  slug: s3-parts-example
- key_count: 3
  name: S3 Partscount Example
  slug: s3-partscount-example
- key_count: 3
  name: S3 Partslist Example
  slug: s3-partslist-example
- key_count: 3
  name: S3 Payer Example
  slug: s3-payer-example
- key_count: 3
  name: S3 Permission Example
  slug: s3-permission-example
- key_count: 3
  name: S3 Policy Example
  slug: s3-policy-example
- key_count: 3
  name: S3 Policystatus Example
  slug: s3-policystatus-example
- key_count: 3
  name: S3 Prefix Example
  slug: s3-prefix-example
- key_count: 3
  name: S3 Priority Example
  slug: s3-priority-example
- key_count: 3
  name: S3 Progress Example
  slug: s3-progress-example
- key_count: 3
  name: S3 Progressevent Example
  slug: s3-progressevent-example
- key_count: 3
  name: S3 Protocol Example
  slug: s3-protocol-example
- key_count: 3
  name: S3 Publicaccessblockconfiguration Example
  slug: s3-publicaccessblockconfiguration-example
- key_count: 3
  name: S3 Putbucketaccelerateconfigurationrequest Example
  slug: s3-putbucketaccelerateconfigurationrequest-example
- key_count: 3
  name: S3 Putbucketaclrequest Example
  slug: s3-putbucketaclrequest-example
- key_count: 3
  name: S3 Putbucketanalyticsconfigurationrequest Example
  slug: s3-putbucketanalyticsconfigurationrequest-example
- key_count: 3
  name: S3 Putbucketcorsrequest Example
  slug: s3-putbucketcorsrequest-example
- key_count: 3
  name: S3 Putbucketencryptionrequest Example
  slug: s3-putbucketencryptionrequest-example
- key_count: 3
  name: S3 Putbucketintelligenttieringconfigurationrequest Example
  slug: s3-putbucketintelligenttieringconfigurationrequest-example
- key_count: 3
  name: S3 Putbucketinventoryconfigurationrequest Example
  slug: s3-putbucketinventoryconfigurationrequest-example
- key_count: 3
  name: S3 Putbucketlifecycleconfigurationrequest Example
  slug: s3-putbucketlifecycleconfigurationrequest-example
- key_count: 3
  name: S3 Putbucketlifecyclerequest Example
  slug: s3-putbucketlifecyclerequest-example
- key_count: 3
  name: S3 Putbucketloggingrequest Example
  slug: s3-putbucketloggingrequest-example
- key_count: 3
  name: S3 Putbucketmetricsconfigurationrequest Example
  slug: s3-putbucketmetricsconfigurationrequest-example
- key_count: 3
  name: S3 Putbucketnotificationconfigurationrequest Example
  slug: s3-putbucketnotificationconfigurationrequest-example
- key_count: 3
  name: S3 Putbucketnotificationrequest Example
  slug: s3-putbucketnotificationrequest-example
- key_count: 3
  name: S3 Putbucketownershipcontrolsrequest Example
  slug: s3-putbucketownershipcontrolsrequest-example
- key_count: 3
  name: S3 Putbucketpolicyrequest Example
  slug: s3-putbucketpolicyrequest-example
- key_count: 3
  name: S3 Putbucketreplicationrequest Example
  slug: s3-putbucketreplicationrequest-example
- key_count: 3
  name: S3 Putbucketrequestpaymentrequest Example
  slug: s3-putbucketrequestpaymentrequest-example
- key_count: 3
  name: S3 Putbuckettaggingrequest Example
  slug: s3-putbuckettaggingrequest-example
- key_count: 3
  name: S3 Putbucketversioningrequest Example
  slug: s3-putbucketversioningrequest-example
- key_count: 3
  name: S3 Putbucketwebsiterequest Example
  slug: s3-putbucketwebsiterequest-example
- key_count: 3
  name: S3 Putobjectacloutput Example
  slug: s3-putobjectacloutput-example
- key_count: 3
  name: S3 Putobjectaclrequest Example
  slug: s3-putobjectaclrequest-example
- key_count: 3
  name: S3 Putobjectlegalholdoutput Example
  slug: s3-putobjectlegalholdoutput-example
- key_count: 3
  name: S3 Putobjectlegalholdrequest Example
  slug: s3-putobjectlegalholdrequest-example
- key_count: 3
  name: S3 Putobjectlockconfigurationoutput Example
  slug: s3-putobjectlockconfigurationoutput-example
- key_count: 3
  name: S3 Putobjectlockconfigurationrequest Example
  slug: s3-putobjectlockconfigurationrequest-example
- key_count: 3
  name: S3 Putobjectoutput Example
  slug: s3-putobjectoutput-example
- key_count: 3
  name: S3 Putobjectrequest Example
  slug: s3-putobjectrequest-example
- key_count: 3
  name: S3 Putobjectretentionoutput Example
  slug: s3-putobjectretentionoutput-example
- key_count: 3
  name: S3 Putobjectretentionrequest Example
  slug: s3-putobjectretentionrequest-example
- key_count: 3
  name: S3 Putobjecttaggingoutput Example
  slug: s3-putobjecttaggingoutput-example
- key_count: 3
  name: S3 Putobjecttaggingrequest Example
  slug: s3-putobjecttaggingrequest-example
- key_count: 3
  name: S3 Putpublicaccessblockrequest Example
  slug: s3-putpublicaccessblockrequest-example
- key_count: 3
  name: S3 Queuearn Example
  slug: s3-queuearn-example
- key_count: 3
  name: S3 Queueconfiguration Example
  slug: s3-queueconfiguration-example
- key_count: 3
  name: S3 Queueconfigurationdeprecated Example
  slug: s3-queueconfigurationdeprecated-example
- key_count: 3
  name: S3 Queueconfigurationlist Example
  slug: s3-queueconfigurationlist-example
- key_count: 3
  name: S3 Quiet Example
  slug: s3-quiet-example
- key_count: 3
  name: S3 Quotecharacter Example
  slug: s3-quotecharacter-example
- key_count: 3
  name: S3 Quoteescapecharacter Example
  slug: s3-quoteescapecharacter-example
- key_count: 3
  name: S3 Quotefields Example
  slug: s3-quotefields-example
- key_count: 3
  name: S3 Range Example
  slug: s3-range-example
- key_count: 3
  name: S3 Recorddelimiter Example
  slug: s3-recorddelimiter-example
- key_count: 3
  name: S3 Recordsevent Example
  slug: s3-recordsevent-example
- key_count: 3
  name: S3 Redirect Example
  slug: s3-redirect-example
- key_count: 3
  name: S3 Redirectallrequeststo Example
  slug: s3-redirectallrequeststo-example
- key_count: 3
  name: S3 Replacekeyprefixwith Example
  slug: s3-replacekeyprefixwith-example
- key_count: 3
  name: S3 Replacekeywith Example
  slug: s3-replacekeywith-example
- key_count: 3
  name: S3 Replicakmskeyid Example
  slug: s3-replicakmskeyid-example
- key_count: 3
  name: S3 Replicamodifications Example
  slug: s3-replicamodifications-example
- key_count: 3
  name: S3 Replicamodificationsstatus Example
  slug: s3-replicamodificationsstatus-example
- key_count: 3
  name: S3 Replicationconfiguration Example
  slug: s3-replicationconfiguration-example
- key_count: 3
  name: S3 Replicationrule Example
  slug: s3-replicationrule-example
- key_count: 3
  name: S3 Replicationruleandoperator Example
  slug: s3-replicationruleandoperator-example
- key_count: 3
  name: S3 Replicationrulefilter Example
  slug: s3-replicationrulefilter-example
- key_count: 3
  name: S3 Replicationrules Example
  slug: s3-replicationrules-example
- key_count: 3
  name: S3 Replicationrulestatus Example
  slug: s3-replicationrulestatus-example
- key_count: 3
  name: S3 Replicationstatus Example
  slug: s3-replicationstatus-example
- key_count: 3
  name: S3 Replicationtime Example
  slug: s3-replicationtime-example
- key_count: 3
  name: S3 Replicationtimestatus Example
  slug: s3-replicationtimestatus-example
- key_count: 3
  name: S3 Replicationtimevalue Example
  slug: s3-replicationtimevalue-example
- key_count: 3
  name: S3 Requestcharged Example
  slug: s3-requestcharged-example
- key_count: 3
  name: S3 Requestpayer Example
  slug: s3-requestpayer-example
- key_count: 3
  name: S3 Requestpaymentconfiguration Example
  slug: s3-requestpaymentconfiguration-example
- key_count: 3
  name: S3 Requestprogress Example
  slug: s3-requestprogress-example
- key_count: 3
  name: S3 Requestroute Example
  slug: s3-requestroute-example
- key_count: 3
  name: S3 Requesttoken Example
  slug: s3-requesttoken-example
- key_count: 3
  name: S3 Responsecachecontrol Example
  slug: s3-responsecachecontrol-example
- key_count: 3
  name: S3 Responsecontentdisposition Example
  slug: s3-responsecontentdisposition-example
- key_count: 3
  name: S3 Responsecontentencoding Example
  slug: s3-responsecontentencoding-example
- key_count: 3
  name: S3 Responsecontentlanguage Example
  slug: s3-responsecontentlanguage-example
- key_count: 3
  name: S3 Responsecontenttype Example
  slug: s3-responsecontenttype-example
- key_count: 3
  name: S3 Responseexpires Example
  slug: s3-responseexpires-example
- key_count: 3
  name: S3 Restore Example
  slug: s3-restore-example
- key_count: 3
  name: S3 Restoreobjectoutput Example
  slug: s3-restoreobjectoutput-example
- key_count: 3
  name: S3 Restoreobjectrequest Example
  slug: s3-restoreobjectrequest-example
- key_count: 3
  name: S3 Restoreoutputpath Example
  slug: s3-restoreoutputpath-example
- key_count: 3
  name: S3 Restorerequest Example
  slug: s3-restorerequest-example
- key_count: 3
  name: S3 Restorerequesttype Example
  slug: s3-restorerequesttype-example
- key_count: 3
  name: S3 Role Example
  slug: s3-role-example
- key_count: 3
  name: S3 Routingrule Example
  slug: s3-routingrule-example
- key_count: 3
  name: S3 Routingrules Example
  slug: s3-routingrules-example
- key_count: 3
  name: S3 Rule Example
  slug: s3-rule-example
- key_count: 3
  name: S3 Rules Example
  slug: s3-rules-example
- key_count: 3
  name: S3 S3Keyfilter Example
  slug: s3-s3keyfilter-example
- key_count: 3
  name: S3 S3Location Example
  slug: s3-s3location-example
- key_count: 3
  name: S3 Scanrange Example
  slug: s3-scanrange-example
- key_count: 3
  name: S3 Selectobjectcontenteventstream Example
  slug: s3-selectobjectcontenteventstream-example
- key_count: 3
  name: S3 Selectobjectcontentoutput Example
  slug: s3-selectobjectcontentoutput-example
- key_count: 3
  name: S3 Selectobjectcontentrequest Example
  slug: s3-selectobjectcontentrequest-example
- key_count: 3
  name: S3 Selectparameters Example
  slug: s3-selectparameters-example
- key_count: 3
  name: S3 Serversideencryption Example
  slug: s3-serversideencryption-example
- key_count: 3
  name: S3 Serversideencryptionbydefault Example
  slug: s3-serversideencryptionbydefault-example
- key_count: 3
  name: S3 Serversideencryptionconfiguration Example
  slug: s3-serversideencryptionconfiguration-example
- key_count: 3
  name: S3 Serversideencryptionrule Example
  slug: s3-serversideencryptionrule-example
- key_count: 3
  name: S3 Serversideencryptionrules Example
  slug: s3-serversideencryptionrules-example
- key_count: 3
  name: S3 Setting Example
  slug: s3-setting-example
- key_count: 3
  name: S3 Size Example
  slug: s3-size-example
- key_count: 3
  name: S3 Skipvalidation Example
  slug: s3-skipvalidation-example
- key_count: 3
  name: S3 Sourceselectioncriteria Example
  slug: s3-sourceselectioncriteria-example
- key_count: 3
  name: S3 Ssecustomeralgorithm Example
  slug: s3-ssecustomeralgorithm-example
- key_count: 3
  name: S3 Ssecustomerkey Example
  slug: s3-ssecustomerkey-example
- key_count: 3
  name: S3 Ssecustomerkeymd5 Example
  slug: s3-ssecustomerkeymd5-example
- key_count: 3
  name: S3 Ssekms Example
  slug: s3-ssekms-example
- key_count: 3
  name: S3 Ssekmsencryptedobjects Example
  slug: s3-ssekmsencryptedobjects-example
- key_count: 3
  name: S3 Ssekmsencryptedobjectsstatus Example
  slug: s3-ssekmsencryptedobjectsstatus-example
- key_count: 3
  name: S3 Ssekmsencryptioncontext Example
  slug: s3-ssekmsencryptioncontext-example
- key_count: 3
  name: S3 Ssekmskeyid Example
  slug: s3-ssekmskeyid-example
- key_count: 3
  name: S3 Sses3 Example
  slug: s3-sses3-example
- key_count: 3
  name: S3 Start Example
  slug: s3-start-example
- key_count: 3
  name: S3 Startafter Example
  slug: s3-startafter-example
- key_count: 3
  name: S3 Stats Example
  slug: s3-stats-example
- key_count: 3
  name: S3 Statsevent Example
  slug: s3-statsevent-example
- key_count: 3
  name: S3 Storageclass Example
  slug: s3-storageclass-example
- key_count: 3
  name: S3 Storageclassanalysis Example
  slug: s3-storageclassanalysis-example
- key_count: 3
  name: S3 Storageclassanalysisdataexport Example
  slug: s3-storageclassanalysisdataexport-example
- key_count: 3
  name: S3 Storageclassanalysisschemaversion Example
  slug: s3-storageclassanalysisschemaversion-example
- key_count: 3
  name: S3 Suffix Example
  slug: s3-suffix-example
- key_count: 3
  name: S3 Tag Example
  slug: s3-tag-example
- key_count: 3
  name: S3 Tagcount Example
  slug: s3-tagcount-example
- key_count: 3
  name: S3 Tagging Example
  slug: s3-tagging-example
- key_count: 3
  name: S3 Taggingdirective Example
  slug: s3-taggingdirective-example
- key_count: 3
  name: S3 Taggingheader Example
  slug: s3-taggingheader-example
- key_count: 3
  name: S3 Tagset Example
  slug: s3-tagset-example
- key_count: 3
  name: S3 Targetbucket Example
  slug: s3-targetbucket-example
- key_count: 3
  name: S3 Targetgrant Example
  slug: s3-targetgrant-example
- key_count: 3
  name: S3 Targetgrants Example
  slug: s3-targetgrants-example
- key_count: 3
  name: S3 Targetprefix Example
  slug: s3-targetprefix-example
- key_count: 3
  name: S3 Tier Example
  slug: s3-tier-example
- key_count: 3
  name: S3 Tiering Example
  slug: s3-tiering-example
- key_count: 3
  name: S3 Tieringlist Example
  slug: s3-tieringlist-example
- key_count: 3
  name: S3 Token Example
  slug: s3-token-example
- key_count: 3
  name: S3 Topicarn Example
  slug: s3-topicarn-example
- key_count: 3
  name: S3 Topicconfiguration Example
  slug: s3-topicconfiguration-example
- key_count: 3
  name: S3 Topicconfigurationdeprecated Example
  slug: s3-topicconfigurationdeprecated-example
- key_count: 3
  name: S3 Topicconfigurationlist Example
  slug: s3-topicconfigurationlist-example
- key_count: 3
  name: S3 Transition Example
  slug: s3-transition-example
- key_count: 3
  name: S3 Transitionlist Example
  slug: s3-transitionlist-example
- key_count: 3
  name: S3 Transitionstorageclass Example
  slug: s3-transitionstorageclass-example
- key_count: 3
  name: S3 Type Example
  slug: s3-type-example
- key_count: 3
  name: S3 Uploadidmarker Example
  slug: s3-uploadidmarker-example
- key_count: 3
  name: S3 Uploadpartcopyoutput Example
  slug: s3-uploadpartcopyoutput-example
- key_count: 3
  name: S3 Uploadpartcopyrequest Example
  slug: s3-uploadpartcopyrequest-example
- key_count: 3
  name: S3 Uploadpartoutput Example
  slug: s3-uploadpartoutput-example
- key_count: 3
  name: S3 Uploadpartrequest Example
  slug: s3-uploadpartrequest-example
- key_count: 3
  name: S3 Uri Example
  slug: s3-uri-example
- key_count: 3
  name: S3 Usermetadata Example
  slug: s3-usermetadata-example
- key_count: 3
  name: S3 Value Example
  slug: s3-value-example
- key_count: 3
  name: S3 Versioncount Example
  slug: s3-versioncount-example
- key_count: 3
  name: S3 Versionidmarker Example
  slug: s3-versionidmarker-example
- key_count: 3
  name: S3 Versioningconfiguration Example
  slug: s3-versioningconfiguration-example
- key_count: 3
  name: S3 Websiteconfiguration Example
  slug: s3-websiteconfiguration-example
- key_count: 3
  name: S3 Websiteredirectlocation Example
  slug: s3-websiteredirectlocation-example
- key_count: 3
  name: S3 Writegetobjectresponserequest Example
  slug: s3-writegetobjectresponserequest-example
- key_count: 3
  name: S3 Years Example
  slug: s3-years-example
features:
- description: Store and retrieve any amount of data, at any time, from anywhere.
  name: Scalable Object Storage
- description: Keep multiple variants of an object in the same bucket to recover from unintended actions.
  name: Versioning
- description: Automatically transition objects to cheaper storage classes or expire them after a defined period.
  name: Lifecycle Policies
- description: Automatically replicate objects across AWS Regions for compliance and disaster recovery.
  name: Cross-Region Replication
- description: Encrypt objects at rest using SSE-S3, SSE-KMS, or SSE-C managed keys.
  name: Server-Side Encryption
- description: Fine-grained access via bucket policies, ACLs, and IAM policies.
  name: Access Control
- description: Trigger Lambda functions, SQS messages, or SNS topics on bucket events.
  name: Event Notifications
- description: Retrieve a subset of data from an object using SQL expressions.
  name: S3 Select
- description: Speed up uploads using CloudFront's globally distributed edge locations.
  name: Transfer Acceleration
- description: Automatically move objects to the most cost-effective access tier based on usage patterns.
  name: Intelligent-Tiering
finops:
- name: Aws S3 Finops
  service_category: API
  slug: aws-s3-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-s3.png
json_schemas:
- name: AbortDate
  property_count: 0
  slug: s3-abortdate
- name: AbortIncompleteMultipartUpload
  property_count: 1
  slug: s3-abortincompletemultipartupload
- name: AbortMultipartUploadOutput
  property_count: 0
  slug: s3-abortmultipartuploadoutput
- name: AbortMultipartUploadRequest
  property_count: 0
  slug: s3-abortmultipartuploadrequest
- name: AbortRuleId
  property_count: 0
  slug: s3-abortruleid
- name: AccelerateConfiguration
  property_count: 1
  slug: s3-accelerateconfiguration
- name: AcceptRanges
  property_count: 0
  slug: s3-acceptranges
- name: AccessControlPolicy
  property_count: 2
  slug: s3-accesscontrolpolicy
- name: AccessControlTranslation
  property_count: 1
  slug: s3-accesscontroltranslation
- name: AccessPointArn
  property_count: 0
  slug: s3-accesspointarn
- name: AccountId
  property_count: 0
  slug: s3-accountid
- name: AllowedHeader
  property_count: 0
  slug: s3-allowedheader
- name: AllowedHeaders
  property_count: 0
  slug: s3-allowedheaders
- name: AllowedMethod
  property_count: 0
  slug: s3-allowedmethod
- name: AllowedMethods
  property_count: 0
  slug: s3-allowedmethods
- name: AllowedOrigin
  property_count: 0
  slug: s3-allowedorigin
- name: AllowedOrigins
  property_count: 0
  slug: s3-allowedorigins
- name: AllowQuotedRecordDelimiter
  property_count: 0
  slug: s3-allowquotedrecorddelimiter
- name: AnalyticsAndOperator
  property_count: 2
  slug: s3-analyticsandoperator
- name: AnalyticsConfiguration
  property_count: 3
  slug: s3-analyticsconfiguration
- name: AnalyticsConfigurationList
  property_count: 0
  slug: s3-analyticsconfigurationlist
- name: AnalyticsExportDestination
  property_count: 1
  slug: s3-analyticsexportdestination
- name: AnalyticsFilter
  property_count: 3
  slug: s3-analyticsfilter
- name: AnalyticsId
  property_count: 0
  slug: s3-analyticsid
- name: AnalyticsS3BucketDestination
  property_count: 4
  slug: s3-analyticss3bucketdestination
- name: AnalyticsS3ExportFileFormat
  property_count: 0
  slug: s3-analyticss3exportfileformat
- name: ArchiveStatus
  property_count: 0
  slug: s3-archivestatus
- name: Body
  property_count: 0
  slug: s3-body
- name: Bucket
  property_count: 2
  slug: s3-bucket
- name: BucketAccelerateStatus
  property_count: 0
  slug: s3-bucketacceleratestatus
- name: BucketAlreadyExists
  property_count: 0
  slug: s3-bucketalreadyexists
- name: BucketAlreadyOwnedByYou
  property_count: 0
  slug: s3-bucketalreadyownedbyyou
- name: BucketCannedACL
  property_count: 0
  slug: s3-bucketcannedacl
- name: BucketKeyEnabled
  property_count: 0
  slug: s3-bucketkeyenabled
- name: BucketLifecycleConfiguration
  property_count: 1
  slug: s3-bucketlifecycleconfiguration
- name: BucketLocationConstraint
  property_count: 0
  slug: s3-bucketlocationconstraint
- name: BucketLoggingStatus
  property_count: 1
  slug: s3-bucketloggingstatus
- name: BucketLogsPermission
  property_count: 0
  slug: s3-bucketlogspermission
- name: BucketName
  property_count: 0
  slug: s3-bucketname
- name: Buckets
  property_count: 0
  slug: s3-buckets
- name: BucketVersioningStatus
  property_count: 0
  slug: s3-bucketversioningstatus
- name: BypassGovernanceRetention
  property_count: 0
  slug: s3-bypassgovernanceretention
- name: BytesProcessed
  property_count: 0
  slug: s3-bytesprocessed
- name: BytesReturned
  property_count: 0
  slug: s3-bytesreturned
- name: BytesScanned
  property_count: 0
  slug: s3-bytesscanned
- name: CacheControl
  property_count: 0
  slug: s3-cachecontrol
- name: Checksum
  property_count: 4
  slug: s3-checksum
- name: ChecksumAlgorithm
  property_count: 0
  slug: s3-checksumalgorithm
- name: ChecksumAlgorithmList
  property_count: 0
  slug: s3-checksumalgorithmlist
- name: ChecksumCRC32
  property_count: 0
  slug: s3-checksumcrc32
- name: ChecksumCRC32C
  property_count: 0
  slug: s3-checksumcrc32c
- name: ChecksumMode
  property_count: 0
  slug: s3-checksummode
- name: ChecksumSHA1
  property_count: 0
  slug: s3-checksumsha1
- name: ChecksumSHA256
  property_count: 0
  slug: s3-checksumsha256
- name: CloudFunction
  property_count: 0
  slug: s3-cloudfunction
- name: CloudFunctionConfiguration
  property_count: 5
  slug: s3-cloudfunctionconfiguration
- name: CloudFunctionInvocationRole
  property_count: 0
  slug: s3-cloudfunctioninvocationrole
- name: Code
  property_count: 0
  slug: s3-code
- name: Comments
  property_count: 0
  slug: s3-comments
- name: CommonPrefix
  property_count: 1
  slug: s3-commonprefix
- name: CommonPrefixList
  property_count: 0
  slug: s3-commonprefixlist
- name: CompletedMultipartUpload
  property_count: 1
  slug: s3-completedmultipartupload
- name: CompletedPart
  property_count: 6
  slug: s3-completedpart
- name: CompletedPartList
  property_count: 0
  slug: s3-completedpartlist
- name: CompleteMultipartUploadOutput
  property_count: 8
  slug: s3-completemultipartuploadoutput
- name: CompleteMultipartUploadRequest
  property_count: 1
  slug: s3-completemultipartuploadrequest
- name: CompressionType
  property_count: 0
  slug: s3-compressiontype
- name: Condition
  property_count: 2
  slug: s3-condition
- name: ConfirmRemoveSelfBucketAccess
  property_count: 0
  slug: s3-confirmremoveselfbucketaccess
- name: ContentDisposition
  property_count: 0
  slug: s3-contentdisposition
- name: ContentEncoding
  property_count: 0
  slug: s3-contentencoding
- name: ContentLanguage
  property_count: 0
  slug: s3-contentlanguage
- name: ContentLength
  property_count: 0
  slug: s3-contentlength
- name: ContentMD5
  property_count: 0
  slug: s3-contentmd5
- name: ContentRange
  property_count: 0
  slug: s3-contentrange
- name: ContentType
  property_count: 0
  slug: s3-contenttype
- name: ContinuationEvent
  property_count: 0
  slug: s3-continuationevent
- name: CopyObjectOutput
  property_count: 1
  slug: s3-copyobjectoutput
- name: CopyObjectRequest
  property_count: 1
  slug: s3-copyobjectrequest
- name: CopyObjectResult
  property_count: 6
  slug: s3-copyobjectresult
- name: CopyPartResult
  property_count: 6
  slug: s3-copypartresult
- name: CopySource
  property_count: 0
  slug: s3-copysource
- name: CopySourceIfMatch
  property_count: 0
  slug: s3-copysourceifmatch
- name: CopySourceIfModifiedSince
  property_count: 0
  slug: s3-copysourceifmodifiedsince
- name: CopySourceIfNoneMatch
  property_count: 0
  slug: s3-copysourceifnonematch
- name: CopySourceIfUnmodifiedSince
  property_count: 0
  slug: s3-copysourceifunmodifiedsince
- name: CopySourceRange
  property_count: 0
  slug: s3-copysourcerange
- name: CopySourceSSECustomerAlgorithm
  property_count: 0
  slug: s3-copysourcessecustomeralgorithm
- name: CopySourceSSECustomerKey
  property_count: 0
  slug: s3-copysourcessecustomerkey
- name: CopySourceSSECustomerKeyMD5
  property_count: 0
  slug: s3-copysourcessecustomerkeymd5
- name: CopySourceVersionId
  property_count: 0
  slug: s3-copysourceversionid
- name: CORSConfiguration
  property_count: 1
  slug: s3-corsconfiguration
- name: CORSRule
  property_count: 6
  slug: s3-corsrule
- name: CORSRules
  property_count: 0
  slug: s3-corsrules
- name: CreateBucketConfiguration
  property_count: 1
  slug: s3-createbucketconfiguration
- name: CreateBucketOutput
  property_count: 0
  slug: s3-createbucketoutput
- name: CreateBucketRequest
  property_count: 1
  slug: s3-createbucketrequest
- name: CreateMultipartUploadOutput
  property_count: 3
  slug: s3-createmultipartuploadoutput
- name: CreateMultipartUploadRequest
  property_count: 1
  slug: s3-createmultipartuploadrequest
- name: CreationDate
  property_count: 0
  slug: s3-creationdate
- name: CSVInput
  property_count: 7
  slug: s3-csvinput
- name: CSVOutput
  property_count: 5
  slug: s3-csvoutput
- name: Date
  property_count: 0
  slug: s3-date
- name: Days
  property_count: 0
  slug: s3-days
- name: DaysAfterInitiation
  property_count: 0
  slug: s3-daysafterinitiation
- name: DefaultRetention
  property_count: 3
  slug: s3-defaultretention
- name: Delete
  property_count: 2
  slug: s3-delete
- name: DeleteBucketAnalyticsConfigurationRequest
  property_count: 0
  slug: s3-deletebucketanalyticsconfigurationrequest
- name: DeleteBucketCorsRequest
  property_count: 0
  slug: s3-deletebucketcorsrequest
- name: DeleteBucketEncryptionRequest
  property_count: 0
  slug: s3-deletebucketencryptionrequest
- name: DeleteBucketIntelligentTieringConfigurationRequest
  property_count: 0
  slug: s3-deletebucketintelligenttieringconfigurationrequest
- name: DeleteBucketInventoryConfigurationRequest
  property_count: 0
  slug: s3-deletebucketinventoryconfigurationrequest
- name: DeleteBucketLifecycleRequest
  property_count: 0
  slug: s3-deletebucketlifecyclerequest
- name: DeleteBucketMetricsConfigurationRequest
  property_count: 0
  slug: s3-deletebucketmetricsconfigurationrequest
- name: DeleteBucketOwnershipControlsRequest
  property_count: 0
  slug: s3-deletebucketownershipcontrolsrequest
- name: DeleteBucketPolicyRequest
  property_count: 0
  slug: s3-deletebucketpolicyrequest
- name: DeleteBucketReplicationRequest
  property_count: 0
  slug: s3-deletebucketreplicationrequest
- name: DeleteBucketRequest
  property_count: 0
  slug: s3-deletebucketrequest
- name: DeleteBucketTaggingRequest
  property_count: 0
  slug: s3-deletebuckettaggingrequest
- name: DeleteBucketWebsiteRequest
  property_count: 0
  slug: s3-deletebucketwebsiterequest
- name: DeletedObject
  property_count: 4
  slug: s3-deletedobject
- name: DeletedObjects
  property_count: 0
  slug: s3-deletedobjects
- name: DeleteMarker
  property_count: 0
  slug: s3-deletemarker
- name: DeleteMarkerEntry
  property_count: 5
  slug: s3-deletemarkerentry
- name: DeleteMarkerReplication
  property_count: 1
  slug: s3-deletemarkerreplication
- name: DeleteMarkerReplicationStatus
  property_count: 0
  slug: s3-deletemarkerreplicationstatus
- name: DeleteMarkers
  property_count: 0
  slug: s3-deletemarkers
- name: DeleteMarkerVersionId
  property_count: 0
  slug: s3-deletemarkerversionid
- name: DeleteObjectOutput
  property_count: 0
  slug: s3-deleteobjectoutput
- name: DeleteObjectRequest
  property_count: 0
  slug: s3-deleteobjectrequest
- name: DeleteObjectsOutput
  property_count: 2
  slug: s3-deleteobjectsoutput
- name: DeleteObjectsRequest
  property_count: 1
  slug: s3-deleteobjectsrequest
- name: DeleteObjectTaggingOutput
  property_count: 0
  slug: s3-deleteobjecttaggingoutput
- name: DeleteObjectTaggingRequest
  property_count: 0
  slug: s3-deleteobjecttaggingrequest
- name: DeletePublicAccessBlockRequest
  property_count: 0
  slug: s3-deletepublicaccessblockrequest
- name: Delimiter
  property_count: 0
  slug: s3-delimiter
- name: Description
  property_count: 0
  slug: s3-description
- name: Destination
  property_count: 7
  slug: s3-destination
- name: DisplayName
  property_count: 0
  slug: s3-displayname
- name: EmailAddress
  property_count: 0
  slug: s3-emailaddress
- name: EnableRequestProgress
  property_count: 0
  slug: s3-enablerequestprogress
- name: EncodingType
  property_count: 0
  slug: s3-encodingtype
- name: Encryption
  property_count: 3
  slug: s3-encryption
- name: EncryptionConfiguration
  property_count: 1
  slug: s3-encryptionconfiguration
- name: End
  property_count: 0
  slug: s3-end
- name: EndEvent
  property_count: 0
  slug: s3-endevent
- name: Error
  property_count: 4
  slug: s3-error
- name: ErrorCode
  property_count: 0
  slug: s3-errorcode
- name: ErrorDocument
  property_count: 1
  slug: s3-errordocument
- name: ErrorMessage
  property_count: 0
  slug: s3-errormessage
- name: Errors
  property_count: 0
  slug: s3-errors
- name: ETag
  property_count: 0
  slug: s3-etag
- name: Event
  property_count: 0
  slug: s3-event
- name: EventBridgeConfiguration
  property_count: 0
  slug: s3-eventbridgeconfiguration
- name: EventList
  property_count: 0
  slug: s3-eventlist
- name: ExistingObjectReplication
  property_count: 1
  slug: s3-existingobjectreplication
- name: ExistingObjectReplicationStatus
  property_count: 0
  slug: s3-existingobjectreplicationstatus
- name: Expiration
  property_count: 0
  slug: s3-expiration
- name: ExpirationStatus
  property_count: 0
  slug: s3-expirationstatus
- name: ExpiredObjectDeleteMarker
  property_count: 0
  slug: s3-expiredobjectdeletemarker
- name: Expires
  property_count: 0
  slug: s3-expires
- name: ExposeHeader
  property_count: 0
  slug: s3-exposeheader
- name: ExposeHeaders
  property_count: 0
  slug: s3-exposeheaders
- name: Expression
  property_count: 0
  slug: s3-expression
- name: ExpressionType
  property_count: 0
  slug: s3-expressiontype
- name: FetchOwner
  property_count: 0
  slug: s3-fetchowner
- name: FieldDelimiter
  property_count: 0
  slug: s3-fielddelimiter
- name: FileHeaderInfo
  property_count: 0
  slug: s3-fileheaderinfo
- name: FilterRule
  property_count: 2
  slug: s3-filterrule
- name: FilterRuleList
  property_count: 0
  slug: s3-filterrulelist
- name: FilterRuleName
  property_count: 0
  slug: s3-filterrulename
- name: FilterRuleValue
  property_count: 0
  slug: s3-filterrulevalue
- name: GetBucketAccelerateConfigurationOutput
  property_count: 1
  slug: s3-getbucketaccelerateconfigurationoutput
- name: GetBucketAccelerateConfigurationRequest
  property_count: 0
  slug: s3-getbucketaccelerateconfigurationrequest
- name: GetBucketAclOutput
  property_count: 2
  slug: s3-getbucketacloutput
- name: GetBucketAclRequest
  property_count: 0
  slug: s3-getbucketaclrequest
- name: GetBucketAnalyticsConfigurationOutput
  property_count: 1
  slug: s3-getbucketanalyticsconfigurationoutput
- name: GetBucketAnalyticsConfigurationRequest
  property_count: 0
  slug: s3-getbucketanalyticsconfigurationrequest
- name: GetBucketCorsOutput
  property_count: 1
  slug: s3-getbucketcorsoutput
- name: GetBucketCorsRequest
  property_count: 0
  slug: s3-getbucketcorsrequest
- name: GetBucketEncryptionOutput
  property_count: 1
  slug: s3-getbucketencryptionoutput
- name: GetBucketEncryptionRequest
  property_count: 0
  slug: s3-getbucketencryptionrequest
- name: GetBucketIntelligentTieringConfigurationOutput
  property_count: 1
  slug: s3-getbucketintelligenttieringconfigurationoutput
- name: GetBucketIntelligentTieringConfigurationRequest
  property_count: 0
  slug: s3-getbucketintelligenttieringconfigurationrequest
- name: GetBucketInventoryConfigurationOutput
  property_count: 1
  slug: s3-getbucketinventoryconfigurationoutput
- name: GetBucketInventoryConfigurationRequest
  property_count: 0
  slug: s3-getbucketinventoryconfigurationrequest
- name: GetBucketLifecycleConfigurationOutput
  property_count: 1
  slug: s3-getbucketlifecycleconfigurationoutput
- name: GetBucketLifecycleConfigurationRequest
  property_count: 0
  slug: s3-getbucketlifecycleconfigurationrequest
- name: GetBucketLifecycleOutput
  property_count: 1
  slug: s3-getbucketlifecycleoutput
- name: GetBucketLifecycleRequest
  property_count: 0
  slug: s3-getbucketlifecyclerequest
- name: GetBucketLocationOutput
  property_count: 1
  slug: s3-getbucketlocationoutput
- name: GetBucketLocationRequest
  property_count: 0
  slug: s3-getbucketlocationrequest
- name: GetBucketLoggingOutput
  property_count: 1
  slug: s3-getbucketloggingoutput
- name: GetBucketLoggingRequest
  property_count: 0
  slug: s3-getbucketloggingrequest
- name: GetBucketMetricsConfigurationOutput
  property_count: 1
  slug: s3-getbucketmetricsconfigurationoutput
- name: GetBucketMetricsConfigurationRequest
  property_count: 0
  slug: s3-getbucketmetricsconfigurationrequest
- name: GetBucketNotificationConfigurationRequest
  property_count: 0
  slug: s3-getbucketnotificationconfigurationrequest
- name: GetBucketOwnershipControlsOutput
  property_count: 1
  slug: s3-getbucketownershipcontrolsoutput
- name: GetBucketOwnershipControlsRequest
  property_count: 0
  slug: s3-getbucketownershipcontrolsrequest
- name: GetBucketPolicyOutput
  property_count: 1
  slug: s3-getbucketpolicyoutput
- name: GetBucketPolicyRequest
  property_count: 0
  slug: s3-getbucketpolicyrequest
- name: GetBucketPolicyStatusOutput
  property_count: 1
  slug: s3-getbucketpolicystatusoutput
- name: GetBucketPolicyStatusRequest
  property_count: 0
  slug: s3-getbucketpolicystatusrequest
- name: GetBucketReplicationOutput
  property_count: 1
  slug: s3-getbucketreplicationoutput
- name: GetBucketReplicationRequest
  property_count: 0
  slug: s3-getbucketreplicationrequest
- name: GetBucketRequestPaymentOutput
  property_count: 1
  slug: s3-getbucketrequestpaymentoutput
- name: GetBucketRequestPaymentRequest
  property_count: 0
  slug: s3-getbucketrequestpaymentrequest
- name: GetBucketTaggingOutput
  property_count: 1
  slug: s3-getbuckettaggingoutput
- name: GetBucketTaggingRequest
  property_count: 0
  slug: s3-getbuckettaggingrequest
- name: GetBucketVersioningOutput
  property_count: 2
  slug: s3-getbucketversioningoutput
- name: GetBucketVersioningRequest
  property_count: 0
  slug: s3-getbucketversioningrequest
- name: GetBucketWebsiteOutput
  property_count: 4
  slug: s3-getbucketwebsiteoutput
- name: GetBucketWebsiteRequest
  property_count: 0
  slug: s3-getbucketwebsiterequest
- name: GetObjectAclOutput
  property_count: 2
  slug: s3-getobjectacloutput
- name: GetObjectAclRequest
  property_count: 0
  slug: s3-getobjectaclrequest
- name: GetObjectAttributesOutput
  property_count: 5
  slug: s3-getobjectattributesoutput
- name: GetObjectAttributesParts
  property_count: 6
  slug: s3-getobjectattributesparts
- name: GetObjectAttributesRequest
  property_count: 0
  slug: s3-getobjectattributesrequest
- name: GetObjectLegalHoldOutput
  property_count: 1
  slug: s3-getobjectlegalholdoutput
- name: GetObjectLegalHoldRequest
  property_count: 0
  slug: s3-getobjectlegalholdrequest
- name: GetObjectLockConfigurationOutput
  property_count: 1
  slug: s3-getobjectlockconfigurationoutput
- name: GetObjectLockConfigurationRequest
  property_count: 0
  slug: s3-getobjectlockconfigurationrequest
- name: GetObjectOutput
  property_count: 2
  slug: s3-getobjectoutput
- name: GetObjectRequest
  property_count: 0
  slug: s3-getobjectrequest
- name: GetObjectResponseStatusCode
  property_count: 0
  slug: s3-getobjectresponsestatuscode
- name: GetObjectRetentionOutput
  property_count: 1
  slug: s3-getobjectretentionoutput
- name: GetObjectRetentionRequest
  property_count: 0
  slug: s3-getobjectretentionrequest
- name: GetObjectTaggingOutput
  property_count: 1
  slug: s3-getobjecttaggingoutput
- name: GetObjectTaggingRequest
  property_count: 0
  slug: s3-getobjecttaggingrequest
- name: GetObjectTorrentOutput
  property_count: 1
  slug: s3-getobjecttorrentoutput
- name: GetObjectTorrentRequest
  property_count: 0
  slug: s3-getobjecttorrentrequest
- name: GetPublicAccessBlockOutput
  property_count: 1
  slug: s3-getpublicaccessblockoutput
- name: GetPublicAccessBlockRequest
  property_count: 0
  slug: s3-getpublicaccessblockrequest
- name: GlacierJobParameters
  property_count: 1
  slug: s3-glacierjobparameters
- name: Grant
  property_count: 2
  slug: s3-grant
- name: Grantee
  property_count: 5
  slug: s3-grantee
- name: GrantFullControl
  property_count: 0
  slug: s3-grantfullcontrol
- name: GrantRead
  property_count: 0
  slug: s3-grantread
- name: GrantReadACP
  property_count: 0
  slug: s3-grantreadacp
- name: Grants
  property_count: 0
  slug: s3-grants
- name: GrantWrite
  property_count: 0
  slug: s3-grantwrite
- name: GrantWriteACP
  property_count: 0
  slug: s3-grantwriteacp
- name: HeadBucketRequest
  property_count: 0
  slug: s3-headbucketrequest
- name: HeadObjectOutput
  property_count: 1
  slug: s3-headobjectoutput
- name: HeadObjectRequest
  property_count: 0
  slug: s3-headobjectrequest
- name: HostName
  property_count: 0
  slug: s3-hostname
- name: HttpErrorCodeReturnedEquals
  property_count: 0
  slug: s3-httperrorcodereturnedequals
- name: HttpRedirectCode
  property_count: 0
  slug: s3-httpredirectcode
- name: ID
  property_count: 0
  slug: s3-id
- name: IfMatch
  property_count: 0
  slug: s3-ifmatch
- name: IfModifiedSince
  property_count: 0
  slug: s3-ifmodifiedsince
- name: IfNoneMatch
  property_count: 0
  slug: s3-ifnonematch
- name: IfUnmodifiedSince
  property_count: 0
  slug: s3-ifunmodifiedsince
- name: IndexDocument
  property_count: 1
  slug: s3-indexdocument
- name: Initiated
  property_count: 0
  slug: s3-initiated
- name: Initiator
  property_count: 2
  slug: s3-initiator
- name: InputSerialization
  property_count: 4
  slug: s3-inputserialization
- name: IntelligentTieringAccessTier
  property_count: 0
  slug: s3-intelligenttieringaccesstier
- name: IntelligentTieringAndOperator
  property_count: 2
  slug: s3-intelligenttieringandoperator
- name: IntelligentTieringConfiguration
  property_count: 4
  slug: s3-intelligenttieringconfiguration
- name: IntelligentTieringConfigurationList
  property_count: 0
  slug: s3-intelligenttieringconfigurationlist
- name: IntelligentTieringDays
  property_count: 0
  slug: s3-intelligenttieringdays
- name: IntelligentTieringFilter
  property_count: 3
  slug: s3-intelligenttieringfilter
- name: IntelligentTieringId
  property_count: 0
  slug: s3-intelligenttieringid
- name: IntelligentTieringStatus
  property_count: 0
  slug: s3-intelligenttieringstatus
- name: InvalidObjectState
  property_count: 0
  slug: s3-invalidobjectstate
- name: InventoryConfiguration
  property_count: 7
  slug: s3-inventoryconfiguration
- name: InventoryConfigurationList
  property_count: 0
  slug: s3-inventoryconfigurationlist
- name: InventoryDestination
  property_count: 1
  slug: s3-inventorydestination
- name: InventoryEncryption
  property_count: 2
  slug: s3-inventoryencryption
- name: InventoryFilter
  property_count: 1
  slug: s3-inventoryfilter
- name: InventoryFormat
  property_count: 0
  slug: s3-inventoryformat
- name: InventoryFrequency
  property_count: 0
  slug: s3-inventoryfrequency
- name: InventoryId
  property_count: 0
  slug: s3-inventoryid
- name: InventoryIncludedObjectVersions
  property_count: 0
  slug: s3-inventoryincludedobjectversions
- name: InventoryOptionalField
  property_count: 0
  slug: s3-inventoryoptionalfield
- name: InventoryOptionalFields
  property_count: 0
  slug: s3-inventoryoptionalfields
- name: InventoryS3BucketDestination
  property_count: 5
  slug: s3-inventorys3bucketdestination
- name: InventorySchedule
  property_count: 1
  slug: s3-inventoryschedule
- name: IsEnabled
  property_count: 0
  slug: s3-isenabled
- name: IsLatest
  property_count: 0
  slug: s3-islatest
- name: IsPublic
  property_count: 0
  slug: s3-ispublic
- name: IsTruncated
  property_count: 0
  slug: s3-istruncated
- name: JSONInput
  property_count: 1
  slug: s3-jsoninput
- name: JSONOutput
  property_count: 1
  slug: s3-jsonoutput
- name: JSONType
  property_count: 0
  slug: s3-jsontype
- name: KeyCount
  property_count: 0
  slug: s3-keycount
- name: KeyMarker
  property_count: 0
  slug: s3-keymarker
- name: KeyPrefixEquals
  property_count: 0
  slug: s3-keyprefixequals
- name: KMSContext
  property_count: 0
  slug: s3-kmscontext
- name: LambdaFunctionArn
  property_count: 0
  slug: s3-lambdafunctionarn
- name: LambdaFunctionConfiguration
  property_count: 4
  slug: s3-lambdafunctionconfiguration
- name: LambdaFunctionConfigurationList
  property_count: 0
  slug: s3-lambdafunctionconfigurationlist
- name: LastModified
  property_count: 0
  slug: s3-lastmodified
- name: LifecycleConfiguration
  property_count: 1
  slug: s3-lifecycleconfiguration
- name: LifecycleExpiration
  property_count: 3
  slug: s3-lifecycleexpiration
- name: LifecycleRule
  property_count: 9
  slug: s3-lifecyclerule
- name: LifecycleRuleAndOperator
  property_count: 4
  slug: s3-lifecycleruleandoperator
- name: LifecycleRuleFilter
  property_count: 5
  slug: s3-lifecyclerulefilter
- name: LifecycleRules
  property_count: 0
  slug: s3-lifecyclerules
- name: ListBucketAnalyticsConfigurationsOutput
  property_count: 4
  slug: s3-listbucketanalyticsconfigurationsoutput
- name: ListBucketAnalyticsConfigurationsRequest
  property_count: 0
  slug: s3-listbucketanalyticsconfigurationsrequest
- name: ListBucketIntelligentTieringConfigurationsOutput
  property_count: 4
  slug: s3-listbucketintelligenttieringconfigurationsoutput
- name: ListBucketIntelligentTieringConfigurationsRequest
  property_count: 0
  slug: s3-listbucketintelligenttieringconfigurationsrequest
- name: ListBucketInventoryConfigurationsOutput
  property_count: 4
  slug: s3-listbucketinventoryconfigurationsoutput
- name: ListBucketInventoryConfigurationsRequest
  property_count: 0
  slug: s3-listbucketinventoryconfigurationsrequest
- name: ListBucketMetricsConfigurationsOutput
  property_count: 4
  slug: s3-listbucketmetricsconfigurationsoutput
- name: ListBucketMetricsConfigurationsRequest
  property_count: 0
  slug: s3-listbucketmetricsconfigurationsrequest
- name: ListBucketsOutput
  property_count: 2
  slug: s3-listbucketsoutput
- name: ListMultipartUploadsOutput
  property_count: 12
  slug: s3-listmultipartuploadsoutput
- name: ListMultipartUploadsRequest
  property_count: 0
  slug: s3-listmultipartuploadsrequest
- name: ListObjectsOutput
  property_count: 10
  slug: s3-listobjectsoutput
- name: ListObjectsRequest
  property_count: 0
  slug: s3-listobjectsrequest
- name: ListObjectsV2Output
  property_count: 12
  slug: s3-listobjectsv2output
- name: ListObjectsV2Request
  property_count: 0
  slug: s3-listobjectsv2request
- name: ListObjectVersionsOutput
  property_count: 13
  slug: s3-listobjectversionsoutput
- name: ListObjectVersionsRequest
  property_count: 0
  slug: s3-listobjectversionsrequest
- name: ListPartsOutput
  property_count: 12
  slug: s3-listpartsoutput
- name: ListPartsRequest
  property_count: 0
  slug: s3-listpartsrequest
- name: Location
  property_count: 0
  slug: s3-location
- name: LocationPrefix
  property_count: 0
  slug: s3-locationprefix
- name: LoggingEnabled
  property_count: 3
  slug: s3-loggingenabled
- name: Marker
  property_count: 0
  slug: s3-marker
- name: MaxAgeSeconds
  property_count: 0
  slug: s3-maxageseconds
- name: MaxKeys
  property_count: 0
  slug: s3-maxkeys
- name: MaxParts
  property_count: 0
  slug: s3-maxparts
- name: MaxUploads
  property_count: 0
  slug: s3-maxuploads
- name: Message
  property_count: 0
  slug: s3-message
- name: Metadata
  property_count: 0
  slug: s3-metadata
- name: MetadataDirective
  property_count: 0
  slug: s3-metadatadirective
- name: MetadataEntry
  property_count: 2
  slug: s3-metadataentry
- name: MetadataKey
  property_count: 0
  slug: s3-metadatakey
- name: MetadataValue
  property_count: 0
  slug: s3-metadatavalue
- name: Metrics
  property_count: 2
  slug: s3-metrics
- name: MetricsAndOperator
  property_count: 3
  slug: s3-metricsandoperator
- name: MetricsConfiguration
  property_count: 2
  slug: s3-metricsconfiguration
- name: MetricsConfigurationList
  property_count: 0
  slug: s3-metricsconfigurationlist
- name: MetricsFilter
  property_count: 4
  slug: s3-metricsfilter
- name: MetricsId
  property_count: 0
  slug: s3-metricsid
- name: MetricsStatus
  property_count: 0
  slug: s3-metricsstatus
- name: MFA
  property_count: 0
  slug: s3-mfa
- name: MFADelete
  property_count: 0
  slug: s3-mfadelete
- name: MFADeleteStatus
  property_count: 0
  slug: s3-mfadeletestatus
- name: Minutes
  property_count: 0
  slug: s3-minutes
- name: MissingMeta
  property_count: 0
  slug: s3-missingmeta
- name: MultipartUpload
  property_count: 7
  slug: s3-multipartupload
- name: MultipartUploadId
  property_count: 0
  slug: s3-multipartuploadid
- name: MultipartUploadList
  property_count: 0
  slug: s3-multipartuploadlist
- name: NextKeyMarker
  property_count: 0
  slug: s3-nextkeymarker
- name: NextMarker
  property_count: 0
  slug: s3-nextmarker
- name: NextPartNumberMarker
  property_count: 0
  slug: s3-nextpartnumbermarker
- name: NextToken
  property_count: 0
  slug: s3-nexttoken
- name: NextUploadIdMarker
  property_count: 0
  slug: s3-nextuploadidmarker
- name: NextVersionIdMarker
  property_count: 0
  slug: s3-nextversionidmarker
- name: NoncurrentVersionExpiration
  property_count: 2
  slug: s3-noncurrentversionexpiration
- name: NoncurrentVersionTransition
  property_count: 3
  slug: s3-noncurrentversiontransition
- name: NoncurrentVersionTransitionList
  property_count: 0
  slug: s3-noncurrentversiontransitionlist
- name: NoSuchBucket
  property_count: 0
  slug: s3-nosuchbucket
- name: NoSuchKey
  property_count: 0
  slug: s3-nosuchkey
- name: NoSuchUpload
  property_count: 0
  slug: s3-nosuchupload
- name: NotificationConfiguration
  property_count: 4
  slug: s3-notificationconfiguration
- name: NotificationConfigurationDeprecated
  property_count: 3
  slug: s3-notificationconfigurationdeprecated
- name: NotificationConfigurationFilter
  property_count: 1
  slug: s3-notificationconfigurationfilter
- name: NotificationId
  property_count: 0
  slug: s3-notificationid
- name: Object
  property_count: 7
  slug: s3-object
- name: ObjectAlreadyInActiveTierError
  property_count: 0
  slug: s3-objectalreadyinactivetiererror
- name: ObjectAttributes
  property_count: 0
  slug: s3-objectattributes
- name: ObjectAttributesList
  property_count: 0
  slug: s3-objectattributeslist
- name: ObjectCannedACL
  property_count: 0
  slug: s3-objectcannedacl
- name: ObjectIdentifier
  property_count: 2
  slug: s3-objectidentifier
- name: ObjectIdentifierList
  property_count: 0
  slug: s3-objectidentifierlist
- name: ObjectKey
  property_count: 0
  slug: s3-objectkey
- name: ObjectList
  property_count: 0
  slug: s3-objectlist
- name: ObjectLockConfiguration
  property_count: 2
  slug: s3-objectlockconfiguration
- name: ObjectLockEnabled
  property_count: 0
  slug: s3-objectlockenabled
- name: ObjectLockEnabledForBucket
  property_count: 0
  slug: s3-objectlockenabledforbucket
- name: ObjectLockLegalHold
  property_count: 1
  slug: s3-objectlocklegalhold
- name: ObjectLockLegalHoldStatus
  property_count: 0
  slug: s3-objectlocklegalholdstatus
- name: ObjectLockMode
  property_count: 0
  slug: s3-objectlockmode
- name: ObjectLockRetainUntilDate
  property_count: 0
  slug: s3-objectlockretainuntildate
- name: ObjectLockRetention
  property_count: 2
  slug: s3-objectlockretention
- name: ObjectLockRetentionMode
  property_count: 0
  slug: s3-objectlockretentionmode
- name: ObjectLockRule
  property_count: 1
  slug: s3-objectlockrule
- name: ObjectLockToken
  property_count: 0
  slug: s3-objectlocktoken
- name: ObjectNotInActiveTierError
  property_count: 0
  slug: s3-objectnotinactivetiererror
- name: ObjectOwnership
  property_count: 0
  slug: s3-objectownership
- name: ObjectPart
  property_count: 6
  slug: s3-objectpart
- name: ObjectSize
  property_count: 0
  slug: s3-objectsize
- name: ObjectSizeGreaterThanBytes
  property_count: 0
  slug: s3-objectsizegreaterthanbytes
- name: ObjectSizeLessThanBytes
  property_count: 0
  slug: s3-objectsizelessthanbytes
- name: ObjectStorageClass
  property_count: 0
  slug: s3-objectstorageclass
- name: ObjectVersion
  property_count: 9
  slug: s3-objectversion
- name: ObjectVersionId
  property_count: 0
  slug: s3-objectversionid
- name: ObjectVersionList
  property_count: 0
  slug: s3-objectversionlist
- name: ObjectVersionStorageClass
  property_count: 0
  slug: s3-objectversionstorageclass
- name: OutputLocation
  property_count: 1
  slug: s3-outputlocation
- name: OutputSerialization
  property_count: 2
  slug: s3-outputserialization
- name: Owner
  property_count: 2
  slug: s3-owner
- name: OwnerOverride
  property_count: 0
  slug: s3-owneroverride
- name: OwnershipControls
  property_count: 1
  slug: s3-ownershipcontrols
- name: OwnershipControlsRule
  property_count: 1
  slug: s3-ownershipcontrolsrule
- name: OwnershipControlsRules
  property_count: 0
  slug: s3-ownershipcontrolsrules
- name: ParquetInput
  property_count: 0
  slug: s3-parquetinput
- name: Part
  property_count: 8
  slug: s3-part
- name: PartNumber
  property_count: 0
  slug: s3-partnumber
- name: PartNumberMarker
  property_count: 0
  slug: s3-partnumbermarker
- name: Parts
  property_count: 0
  slug: s3-parts
- name: PartsCount
  property_count: 0
  slug: s3-partscount
- name: PartsList
  property_count: 0
  slug: s3-partslist
- name: Payer
  property_count: 0
  slug: s3-payer
- name: Permission
  property_count: 0
  slug: s3-permission
- name: Policy
  property_count: 0
  slug: s3-policy
- name: PolicyStatus
  property_count: 1
  slug: s3-policystatus
- name: Prefix
  property_count: 0
  slug: s3-prefix
- name: Priority
  property_count: 0
  slug: s3-priority
- name: Progress
  property_count: 3
  slug: s3-progress
- name: ProgressEvent
  property_count: 1
  slug: s3-progressevent
- name: Protocol
  property_count: 0
  slug: s3-protocol
- name: PublicAccessBlockConfiguration
  property_count: 4
  slug: s3-publicaccessblockconfiguration
- name: PutBucketAccelerateConfigurationRequest
  property_count: 1
  slug: s3-putbucketaccelerateconfigurationrequest
- name: PutBucketAclRequest
  property_count: 1
  slug: s3-putbucketaclrequest
- name: PutBucketAnalyticsConfigurationRequest
  property_count: 1
  slug: s3-putbucketanalyticsconfigurationrequest
- name: PutBucketCorsRequest
  property_count: 1
  slug: s3-putbucketcorsrequest
- name: PutBucketEncryptionRequest
  property_count: 1
  slug: s3-putbucketencryptionrequest
- name: PutBucketIntelligentTieringConfigurationRequest
  property_count: 1
  slug: s3-putbucketintelligenttieringconfigurationrequest
- name: PutBucketInventoryConfigurationRequest
  property_count: 1
  slug: s3-putbucketinventoryconfigurationrequest
- name: PutBucketLifecycleConfigurationRequest
  property_count: 1
  slug: s3-putbucketlifecycleconfigurationrequest
- name: PutBucketLifecycleRequest
  property_count: 1
  slug: s3-putbucketlifecyclerequest
- name: PutBucketLoggingRequest
  property_count: 1
  slug: s3-putbucketloggingrequest
- name: PutBucketMetricsConfigurationRequest
  property_count: 1
  slug: s3-putbucketmetricsconfigurationrequest
- name: PutBucketNotificationConfigurationRequest
  property_count: 1
  slug: s3-putbucketnotificationconfigurationrequest
- name: PutBucketNotificationRequest
  property_count: 1
  slug: s3-putbucketnotificationrequest
- name: PutBucketOwnershipControlsRequest
  property_count: 1
  slug: s3-putbucketownershipcontrolsrequest
- name: PutBucketPolicyRequest
  property_count: 1
  slug: s3-putbucketpolicyrequest
- name: PutBucketReplicationRequest
  property_count: 1
  slug: s3-putbucketreplicationrequest
- name: PutBucketRequestPaymentRequest
  property_count: 1
  slug: s3-putbucketrequestpaymentrequest
- name: PutBucketTaggingRequest
  property_count: 1
  slug: s3-putbuckettaggingrequest
- name: PutBucketVersioningRequest
  property_count: 1
  slug: s3-putbucketversioningrequest
- name: PutBucketWebsiteRequest
  property_count: 1
  slug: s3-putbucketwebsiterequest
- name: PutObjectAclOutput
  property_count: 0
  slug: s3-putobjectacloutput
- name: PutObjectAclRequest
  property_count: 1
  slug: s3-putobjectaclrequest
- name: PutObjectLegalHoldOutput
  property_count: 0
  slug: s3-putobjectlegalholdoutput
- name: PutObjectLegalHoldRequest
  property_count: 1
  slug: s3-putobjectlegalholdrequest
- name: PutObjectLockConfigurationOutput
  property_count: 0
  slug: s3-putobjectlockconfigurationoutput
- name: PutObjectLockConfigurationRequest
  property_count: 1
  slug: s3-putobjectlockconfigurationrequest
- name: PutObjectOutput
  property_count: 0
  slug: s3-putobjectoutput
- name: PutObjectRequest
  property_count: 2
  slug: s3-putobjectrequest
- name: PutObjectRetentionOutput
  property_count: 0
  slug: s3-putobjectretentionoutput
- name: PutObjectRetentionRequest
  property_count: 1
  slug: s3-putobjectretentionrequest
- name: PutObjectTaggingOutput
  property_count: 0
  slug: s3-putobjecttaggingoutput
- name: PutObjectTaggingRequest
  property_count: 1
  slug: s3-putobjecttaggingrequest
- name: PutPublicAccessBlockRequest
  property_count: 1
  slug: s3-putpublicaccessblockrequest
- name: QueueArn
  property_count: 0
  slug: s3-queuearn
- name: QueueConfiguration
  property_count: 4
  slug: s3-queueconfiguration
- name: QueueConfigurationDeprecated
  property_count: 4
  slug: s3-queueconfigurationdeprecated
- name: QueueConfigurationList
  property_count: 0
  slug: s3-queueconfigurationlist
- name: Quiet
  property_count: 0
  slug: s3-quiet
- name: QuoteCharacter
  property_count: 0
  slug: s3-quotecharacter
- name: QuoteEscapeCharacter
  property_count: 0
  slug: s3-quoteescapecharacter
- name: QuoteFields
  property_count: 0
  slug: s3-quotefields
- name: Range
  property_count: 0
  slug: s3-range
- name: RecordDelimiter
  property_count: 0
  slug: s3-recorddelimiter
- name: RecordsEvent
  property_count: 1
  slug: s3-recordsevent
- name: Redirect
  property_count: 5
  slug: s3-redirect
- name: RedirectAllRequestsTo
  property_count: 2
  slug: s3-redirectallrequeststo
- name: ReplaceKeyPrefixWith
  property_count: 0
  slug: s3-replacekeyprefixwith
- name: ReplaceKeyWith
  property_count: 0
  slug: s3-replacekeywith
- name: ReplicaKmsKeyID
  property_count: 0
  slug: s3-replicakmskeyid
- name: ReplicaModifications
  property_count: 1
  slug: s3-replicamodifications
- name: ReplicaModificationsStatus
  property_count: 0
  slug: s3-replicamodificationsstatus
- name: ReplicationConfiguration
  property_count: 2
  slug: s3-replicationconfiguration
- name: ReplicationRule
  property_count: 9
  slug: s3-replicationrule
- name: ReplicationRuleAndOperator
  property_count: 2
  slug: s3-replicationruleandoperator
- name: ReplicationRuleFilter
  property_count: 3
  slug: s3-replicationrulefilter
- name: ReplicationRules
  property_count: 0
  slug: s3-replicationrules
- name: ReplicationRuleStatus
  property_count: 0
  slug: s3-replicationrulestatus
- name: ReplicationStatus
  property_count: 0
  slug: s3-replicationstatus
- name: ReplicationTime
  property_count: 2
  slug: s3-replicationtime
- name: ReplicationTimeStatus
  property_count: 0
  slug: s3-replicationtimestatus
- name: ReplicationTimeValue
  property_count: 1
  slug: s3-replicationtimevalue
- name: RequestCharged
  property_count: 0
  slug: s3-requestcharged
- name: RequestPayer
  property_count: 0
  slug: s3-requestpayer
- name: RequestPaymentConfiguration
  property_count: 1
  slug: s3-requestpaymentconfiguration
- name: RequestProgress
  property_count: 1
  slug: s3-requestprogress
- name: RequestRoute
  property_count: 0
  slug: s3-requestroute
- name: RequestToken
  property_count: 0
  slug: s3-requesttoken
- name: ResponseCacheControl
  property_count: 0
  slug: s3-responsecachecontrol
- name: ResponseContentDisposition
  property_count: 0
  slug: s3-responsecontentdisposition
- name: ResponseContentEncoding
  property_count: 0
  slug: s3-responsecontentencoding
- name: ResponseContentLanguage
  property_count: 0
  slug: s3-responsecontentlanguage
- name: ResponseContentType
  property_count: 0
  slug: s3-responsecontenttype
- name: ResponseExpires
  property_count: 0
  slug: s3-responseexpires
- name: Restore
  property_count: 0
  slug: s3-restore
- name: RestoreObjectOutput
  property_count: 0
  slug: s3-restoreobjectoutput
- name: RestoreObjectRequest
  property_count: 1
  slug: s3-restoreobjectrequest
- name: RestoreOutputPath
  property_count: 0
  slug: s3-restoreoutputpath
- name: RestoreRequest
  property_count: 7
  slug: s3-restorerequest
- name: RestoreRequestType
  property_count: 0
  slug: s3-restorerequesttype
- name: Role
  property_count: 0
  slug: s3-role
- name: RoutingRule
  property_count: 2
  slug: s3-routingrule
- name: RoutingRules
  property_count: 0
  slug: s3-routingrules
- name: Rule
  property_count: 8
  slug: s3-rule
- name: Rules
  property_count: 0
  slug: s3-rules
- name: S3KeyFilter
  property_count: 1
  slug: s3-s3keyfilter
- name: S3Location
  property_count: 8
  slug: s3-s3location
- name: ScanRange
  property_count: 2
  slug: s3-scanrange
- name: SelectObjectContentEventStream
  property_count: 5
  slug: s3-selectobjectcontenteventstream
- name: SelectObjectContentOutput
  property_count: 1
  slug: s3-selectobjectcontentoutput
- name: SelectObjectContentRequest
  property_count: 6
  slug: s3-selectobjectcontentrequest
- name: SelectParameters
  property_count: 4
  slug: s3-selectparameters
- name: ServerSideEncryption
  property_count: 0
  slug: s3-serversideencryption
- name: ServerSideEncryptionByDefault
  property_count: 2
  slug: s3-serversideencryptionbydefault
- name: ServerSideEncryptionConfiguration
  property_count: 1
  slug: s3-serversideencryptionconfiguration
- name: ServerSideEncryptionRule
  property_count: 2
  slug: s3-serversideencryptionrule
- name: ServerSideEncryptionRules
  property_count: 0
  slug: s3-serversideencryptionrules
- name: Setting
  property_count: 0
  slug: s3-setting
- name: Size
  property_count: 0
  slug: s3-size
- name: SkipValidation
  property_count: 0
  slug: s3-skipvalidation
- name: SourceSelectionCriteria
  property_count: 2
  slug: s3-sourceselectioncriteria
- name: SSECustomerAlgorithm
  property_count: 0
  slug: s3-ssecustomeralgorithm
- name: SSECustomerKey
  property_count: 0
  slug: s3-ssecustomerkey
- name: SSECustomerKeyMD5
  property_count: 0
  slug: s3-ssecustomerkeymd5
- name: SSEKMS
  property_count: 1
  slug: s3-ssekms
- name: SseKmsEncryptedObjects
  property_count: 1
  slug: s3-ssekmsencryptedobjects
- name: SseKmsEncryptedObjectsStatus
  property_count: 0
  slug: s3-ssekmsencryptedobjectsstatus
- name: SSEKMSEncryptionContext
  property_count: 0
  slug: s3-ssekmsencryptioncontext
- name: SSEKMSKeyId
  property_count: 0
  slug: s3-ssekmskeyid
- name: SSES3
  property_count: 0
  slug: s3-sses3
- name: Start
  property_count: 0
  slug: s3-start
- name: StartAfter
  property_count: 0
  slug: s3-startafter
- name: Stats
  property_count: 3
  slug: s3-stats
- name: StatsEvent
  property_count: 1
  slug: s3-statsevent
- name: StorageClass
  property_count: 0
  slug: s3-storageclass
- name: StorageClassAnalysis
  property_count: 1
  slug: s3-storageclassanalysis
- name: StorageClassAnalysisDataExport
  property_count: 2
  slug: s3-storageclassanalysisdataexport
- name: StorageClassAnalysisSchemaVersion
  property_count: 0
  slug: s3-storageclassanalysisschemaversion
- name: Suffix
  property_count: 0
  slug: s3-suffix
- name: Tag
  property_count: 2
  slug: s3-tag
- name: TagCount
  property_count: 0
  slug: s3-tagcount
- name: Tagging
  property_count: 1
  slug: s3-tagging
- name: TaggingDirective
  property_count: 0
  slug: s3-taggingdirective
- name: TaggingHeader
  property_count: 0
  slug: s3-taggingheader
- name: TagSet
  property_count: 0
  slug: s3-tagset
- name: TargetBucket
  property_count: 0
  slug: s3-targetbucket
- name: TargetGrant
  property_count: 2
  slug: s3-targetgrant
- name: TargetGrants
  property_count: 0
  slug: s3-targetgrants
- name: TargetPrefix
  property_count: 0
  slug: s3-targetprefix
- name: Tier
  property_count: 0
  slug: s3-tier
- name: Tiering
  property_count: 2
  slug: s3-tiering
- name: TieringList
  property_count: 0
  slug: s3-tieringlist
- name: Token
  property_count: 0
  slug: s3-token
- name: TopicArn
  property_count: 0
  slug: s3-topicarn
- name: TopicConfiguration
  property_count: 4
  slug: s3-topicconfiguration
- name: TopicConfigurationDeprecated
  property_count: 4
  slug: s3-topicconfigurationdeprecated
- name: TopicConfigurationList
  property_count: 0
  slug: s3-topicconfigurationlist
- name: Transition
  property_count: 3
  slug: s3-transition
- name: TransitionList
  property_count: 0
  slug: s3-transitionlist
- name: TransitionStorageClass
  property_count: 0
  slug: s3-transitionstorageclass
- name: Type
  property_count: 0
  slug: s3-type
- name: UploadIdMarker
  property_count: 0
  slug: s3-uploadidmarker
- name: UploadPartCopyOutput
  property_count: 1
  slug: s3-uploadpartcopyoutput
- name: UploadPartCopyRequest
  property_count: 0
  slug: s3-uploadpartcopyrequest
- name: UploadPartOutput
  property_count: 0
  slug: s3-uploadpartoutput
- name: UploadPartRequest
  property_count: 1
  slug: s3-uploadpartrequest
- name: URI
  property_count: 0
  slug: s3-uri
- name: UserMetadata
  property_count: 0
  slug: s3-usermetadata
- name: Value
  property_count: 0
  slug: s3-value
- name: VersionCount
  property_count: 0
  slug: s3-versioncount
- name: VersionIdMarker
  property_count: 0
  slug: s3-versionidmarker
- name: VersioningConfiguration
  property_count: 2
  slug: s3-versioningconfiguration
- name: WebsiteConfiguration
  property_count: 4
  slug: s3-websiteconfiguration
- name: WebsiteRedirectLocation
  property_count: 0
  slug: s3-websiteredirectlocation
- name: WriteGetObjectResponseRequest
  property_count: 2
  slug: s3-writegetobjectresponserequest
- name: Years
  property_count: 0
  slug: s3-years
json_structures:
- name: S3 Abortdate Structure
  property_count: 0
  slug: s3-abortdate-structure
- name: S3 Abortincompletemultipartupload Structure
  property_count: 0
  slug: s3-abortincompletemultipartupload-structure
- name: S3 Abortmultipartuploadoutput Structure
  property_count: 0
  slug: s3-abortmultipartuploadoutput-structure
- name: S3 Abortmultipartuploadrequest Structure
  property_count: 0
  slug: s3-abortmultipartuploadrequest-structure
- name: S3 Abortruleid Structure
  property_count: 0
  slug: s3-abortruleid-structure
- name: S3 Accelerateconfiguration Structure
  property_count: 0
  slug: s3-accelerateconfiguration-structure
- name: S3 Acceptranges Structure
  property_count: 0
  slug: s3-acceptranges-structure
- name: S3 Accesscontrolpolicy Structure
  property_count: 0
  slug: s3-accesscontrolpolicy-structure
- name: S3 Accesscontroltranslation Structure
  property_count: 0
  slug: s3-accesscontroltranslation-structure
- name: S3 Accesspointarn Structure
  property_count: 0
  slug: s3-accesspointarn-structure
- name: S3 Accountid Structure
  property_count: 0
  slug: s3-accountid-structure
- name: S3 Allowedheader Structure
  property_count: 0
  slug: s3-allowedheader-structure
- name: S3 Allowedheaders Structure
  property_count: 0
  slug: s3-allowedheaders-structure
- name: S3 Allowedmethod Structure
  property_count: 0
  slug: s3-allowedmethod-structure
- name: S3 Allowedmethods Structure
  property_count: 0
  slug: s3-allowedmethods-structure
- name: S3 Allowedorigin Structure
  property_count: 0
  slug: s3-allowedorigin-structure
- name: S3 Allowedorigins Structure
  property_count: 0
  slug: s3-allowedorigins-structure
- name: S3 Allowquotedrecorddelimiter Structure
  property_count: 0
  slug: s3-allowquotedrecorddelimiter-structure
- name: S3 Analyticsandoperator Structure
  property_count: 0
  slug: s3-analyticsandoperator-structure
- name: S3 Analyticsconfiguration Structure
  property_count: 0
  slug: s3-analyticsconfiguration-structure
- name: S3 Analyticsconfigurationlist Structure
  property_count: 0
  slug: s3-analyticsconfigurationlist-structure
- name: S3 Analyticsexportdestination Structure
  property_count: 0
  slug: s3-analyticsexportdestination-structure
- name: S3 Analyticsfilter Structure
  property_count: 0
  slug: s3-analyticsfilter-structure
- name: S3 Analyticsid Structure
  property_count: 0
  slug: s3-analyticsid-structure
- name: S3 Analyticss3Bucketdestination Structure
  property_count: 0
  slug: s3-analyticss3bucketdestination-structure
- name: S3 Analyticss3Exportfileformat Structure
  property_count: 0
  slug: s3-analyticss3exportfileformat-structure
- name: S3 Archivestatus Structure
  property_count: 0
  slug: s3-archivestatus-structure
- name: S3 Body Structure
  property_count: 0
  slug: s3-body-structure
- name: S3 Bucket Structure
  property_count: 0
  slug: s3-bucket-structure
- name: S3 Bucketacceleratestatus Structure
  property_count: 0
  slug: s3-bucketacceleratestatus-structure
- name: S3 Bucketalreadyexists Structure
  property_count: 0
  slug: s3-bucketalreadyexists-structure
- name: S3 Bucketalreadyownedbyyou Structure
  property_count: 0
  slug: s3-bucketalreadyownedbyyou-structure
- name: S3 Bucketcannedacl Structure
  property_count: 0
  slug: s3-bucketcannedacl-structure
- name: S3 Bucketkeyenabled Structure
  property_count: 0
  slug: s3-bucketkeyenabled-structure
- name: S3 Bucketlifecycleconfiguration Structure
  property_count: 0
  slug: s3-bucketlifecycleconfiguration-structure
- name: S3 Bucketlocationconstraint Structure
  property_count: 0
  slug: s3-bucketlocationconstraint-structure
- name: S3 Bucketloggingstatus Structure
  property_count: 0
  slug: s3-bucketloggingstatus-structure
- name: S3 Bucketlogspermission Structure
  property_count: 0
  slug: s3-bucketlogspermission-structure
- name: S3 Bucketname Structure
  property_count: 0
  slug: s3-bucketname-structure
- name: S3 Buckets Structure
  property_count: 0
  slug: s3-buckets-structure
- name: S3 Bucketversioningstatus Structure
  property_count: 0
  slug: s3-bucketversioningstatus-structure
- name: S3 Bypassgovernanceretention Structure
  property_count: 0
  slug: s3-bypassgovernanceretention-structure
- name: S3 Bytesprocessed Structure
  property_count: 0
  slug: s3-bytesprocessed-structure
- name: S3 Bytesreturned Structure
  property_count: 0
  slug: s3-bytesreturned-structure
- name: S3 Bytesscanned Structure
  property_count: 0
  slug: s3-bytesscanned-structure
- name: S3 Cachecontrol Structure
  property_count: 0
  slug: s3-cachecontrol-structure
- name: S3 Checksum Structure
  property_count: 0
  slug: s3-checksum-structure
- name: S3 Checksumalgorithm Structure
  property_count: 0
  slug: s3-checksumalgorithm-structure
- name: S3 Checksumalgorithmlist Structure
  property_count: 0
  slug: s3-checksumalgorithmlist-structure
- name: S3 Checksumcrc32 Structure
  property_count: 0
  slug: s3-checksumcrc32-structure
- name: S3 Checksumcrc32C Structure
  property_count: 0
  slug: s3-checksumcrc32c-structure
- name: S3 Checksummode Structure
  property_count: 0
  slug: s3-checksummode-structure
- name: S3 Checksumsha1 Structure
  property_count: 0
  slug: s3-checksumsha1-structure
- name: S3 Checksumsha256 Structure
  property_count: 0
  slug: s3-checksumsha256-structure
- name: S3 Cloudfunction Structure
  property_count: 0
  slug: s3-cloudfunction-structure
- name: S3 Cloudfunctionconfiguration Structure
  property_count: 0
  slug: s3-cloudfunctionconfiguration-structure
- name: S3 Cloudfunctioninvocationrole Structure
  property_count: 0
  slug: s3-cloudfunctioninvocationrole-structure
- name: S3 Code Structure
  property_count: 0
  slug: s3-code-structure
- name: S3 Comments Structure
  property_count: 0
  slug: s3-comments-structure
- name: S3 Commonprefix Structure
  property_count: 0
  slug: s3-commonprefix-structure
- name: S3 Commonprefixlist Structure
  property_count: 0
  slug: s3-commonprefixlist-structure
- name: S3 Completedmultipartupload Structure
  property_count: 0
  slug: s3-completedmultipartupload-structure
- name: S3 Completedpart Structure
  property_count: 0
  slug: s3-completedpart-structure
- name: S3 Completedpartlist Structure
  property_count: 0
  slug: s3-completedpartlist-structure
- name: S3 Completemultipartuploadoutput Structure
  property_count: 0
  slug: s3-completemultipartuploadoutput-structure
- name: S3 Completemultipartuploadrequest Structure
  property_count: 0
  slug: s3-completemultipartuploadrequest-structure
- name: S3 Compressiontype Structure
  property_count: 0
  slug: s3-compressiontype-structure
- name: S3 Condition Structure
  property_count: 0
  slug: s3-condition-structure
- name: S3 Confirmremoveselfbucketaccess Structure
  property_count: 0
  slug: s3-confirmremoveselfbucketaccess-structure
- name: S3 Contentdisposition Structure
  property_count: 0
  slug: s3-contentdisposition-structure
- name: S3 Contentencoding Structure
  property_count: 0
  slug: s3-contentencoding-structure
- name: S3 Contentlanguage Structure
  property_count: 0
  slug: s3-contentlanguage-structure
- name: S3 Contentlength Structure
  property_count: 0
  slug: s3-contentlength-structure
- name: S3 Contentmd5 Structure
  property_count: 0
  slug: s3-contentmd5-structure
- name: S3 Contentrange Structure
  property_count: 0
  slug: s3-contentrange-structure
- name: S3 Contenttype Structure
  property_count: 0
  slug: s3-contenttype-structure
- name: S3 Continuationevent Structure
  property_count: 0
  slug: s3-continuationevent-structure
- name: S3 Copyobjectoutput Structure
  property_count: 0
  slug: s3-copyobjectoutput-structure
- name: S3 Copyobjectrequest Structure
  property_count: 0
  slug: s3-copyobjectrequest-structure
- name: S3 Copyobjectresult Structure
  property_count: 0
  slug: s3-copyobjectresult-structure
- name: S3 Copypartresult Structure
  property_count: 0
  slug: s3-copypartresult-structure
- name: S3 Copysource Structure
  property_count: 0
  slug: s3-copysource-structure
- name: S3 Copysourceifmatch Structure
  property_count: 0
  slug: s3-copysourceifmatch-structure
- name: S3 Copysourceifmodifiedsince Structure
  property_count: 0
  slug: s3-copysourceifmodifiedsince-structure
- name: S3 Copysourceifnonematch Structure
  property_count: 0
  slug: s3-copysourceifnonematch-structure
- name: S3 Copysourceifunmodifiedsince Structure
  property_count: 0
  slug: s3-copysourceifunmodifiedsince-structure
- name: S3 Copysourcerange Structure
  property_count: 0
  slug: s3-copysourcerange-structure
- name: S3 Copysourcessecustomeralgorithm Structure
  property_count: 0
  slug: s3-copysourcessecustomeralgorithm-structure
- name: S3 Copysourcessecustomerkey Structure
  property_count: 0
  slug: s3-copysourcessecustomerkey-structure
- name: S3 Copysourcessecustomerkeymd5 Structure
  property_count: 0
  slug: s3-copysourcessecustomerkeymd5-structure
- name: S3 Copysourceversionid Structure
  property_count: 0
  slug: s3-copysourceversionid-structure
- name: S3 Corsconfiguration Structure
  property_count: 0
  slug: s3-corsconfiguration-structure
- name: S3 Corsrule Structure
  property_count: 0
  slug: s3-corsrule-structure
- name: S3 Corsrules Structure
  property_count: 0
  slug: s3-corsrules-structure
- name: S3 Createbucketconfiguration Structure
  property_count: 0
  slug: s3-createbucketconfiguration-structure
- name: S3 Createbucketoutput Structure
  property_count: 0
  slug: s3-createbucketoutput-structure
- name: S3 Createbucketrequest Structure
  property_count: 0
  slug: s3-createbucketrequest-structure
- name: S3 Createmultipartuploadoutput Structure
  property_count: 0
  slug: s3-createmultipartuploadoutput-structure
- name: S3 Createmultipartuploadrequest Structure
  property_count: 0
  slug: s3-createmultipartuploadrequest-structure
- name: S3 Creationdate Structure
  property_count: 0
  slug: s3-creationdate-structure
- name: S3 Csvinput Structure
  property_count: 0
  slug: s3-csvinput-structure
- name: S3 Csvoutput Structure
  property_count: 0
  slug: s3-csvoutput-structure
- name: S3 Date Structure
  property_count: 0
  slug: s3-date-structure
- name: S3 Days Structure
  property_count: 0
  slug: s3-days-structure
- name: S3 Daysafterinitiation Structure
  property_count: 0
  slug: s3-daysafterinitiation-structure
- name: S3 Defaultretention Structure
  property_count: 0
  slug: s3-defaultretention-structure
- name: S3 Delete Structure
  property_count: 0
  slug: s3-delete-structure
- name: S3 Deletebucketanalyticsconfigurationrequest Structure
  property_count: 0
  slug: s3-deletebucketanalyticsconfigurationrequest-structure
- name: S3 Deletebucketcorsrequest Structure
  property_count: 0
  slug: s3-deletebucketcorsrequest-structure
- name: S3 Deletebucketencryptionrequest Structure
  property_count: 0
  slug: s3-deletebucketencryptionrequest-structure
- name: S3 Deletebucketintelligenttieringconfigurationrequest Structure
  property_count: 0
  slug: s3-deletebucketintelligenttieringconfigurationrequest-structure
- name: S3 Deletebucketinventoryconfigurationrequest Structure
  property_count: 0
  slug: s3-deletebucketinventoryconfigurationrequest-structure
- name: S3 Deletebucketlifecyclerequest Structure
  property_count: 0
  slug: s3-deletebucketlifecyclerequest-structure
- name: S3 Deletebucketmetricsconfigurationrequest Structure
  property_count: 0
  slug: s3-deletebucketmetricsconfigurationrequest-structure
- name: S3 Deletebucketownershipcontrolsrequest Structure
  property_count: 0
  slug: s3-deletebucketownershipcontrolsrequest-structure
- name: S3 Deletebucketpolicyrequest Structure
  property_count: 0
  slug: s3-deletebucketpolicyrequest-structure
- name: S3 Deletebucketreplicationrequest Structure
  property_count: 0
  slug: s3-deletebucketreplicationrequest-structure
- name: S3 Deletebucketrequest Structure
  property_count: 0
  slug: s3-deletebucketrequest-structure
- name: S3 Deletebuckettaggingrequest Structure
  property_count: 0
  slug: s3-deletebuckettaggingrequest-structure
- name: S3 Deletebucketwebsiterequest Structure
  property_count: 0
  slug: s3-deletebucketwebsiterequest-structure
- name: S3 Deletedobject Structure
  property_count: 0
  slug: s3-deletedobject-structure
- name: S3 Deletedobjects Structure
  property_count: 0
  slug: s3-deletedobjects-structure
- name: S3 Deletemarker Structure
  property_count: 0
  slug: s3-deletemarker-structure
- name: S3 Deletemarkerentry Structure
  property_count: 0
  slug: s3-deletemarkerentry-structure
- name: S3 Deletemarkerreplication Structure
  property_count: 0
  slug: s3-deletemarkerreplication-structure
- name: S3 Deletemarkerreplicationstatus Structure
  property_count: 0
  slug: s3-deletemarkerreplicationstatus-structure
- name: S3 Deletemarkers Structure
  property_count: 0
  slug: s3-deletemarkers-structure
- name: S3 Deletemarkerversionid Structure
  property_count: 0
  slug: s3-deletemarkerversionid-structure
- name: S3 Deleteobjectoutput Structure
  property_count: 0
  slug: s3-deleteobjectoutput-structure
- name: S3 Deleteobjectrequest Structure
  property_count: 0
  slug: s3-deleteobjectrequest-structure
- name: S3 Deleteobjectsoutput Structure
  property_count: 0
  slug: s3-deleteobjectsoutput-structure
- name: S3 Deleteobjectsrequest Structure
  property_count: 0
  slug: s3-deleteobjectsrequest-structure
- name: S3 Deleteobjecttaggingoutput Structure
  property_count: 0
  slug: s3-deleteobjecttaggingoutput-structure
- name: S3 Deleteobjecttaggingrequest Structure
  property_count: 0
  slug: s3-deleteobjecttaggingrequest-structure
- name: S3 Deletepublicaccessblockrequest Structure
  property_count: 0
  slug: s3-deletepublicaccessblockrequest-structure
- name: S3 Delimiter Structure
  property_count: 0
  slug: s3-delimiter-structure
- name: S3 Description Structure
  property_count: 0
  slug: s3-description-structure
- name: S3 Destination Structure
  property_count: 0
  slug: s3-destination-structure
- name: S3 Displayname Structure
  property_count: 0
  slug: s3-displayname-structure
- name: S3 Emailaddress Structure
  property_count: 0
  slug: s3-emailaddress-structure
- name: S3 Enablerequestprogress Structure
  property_count: 0
  slug: s3-enablerequestprogress-structure
- name: S3 Encodingtype Structure
  property_count: 0
  slug: s3-encodingtype-structure
- name: S3 Encryption Structure
  property_count: 0
  slug: s3-encryption-structure
- name: S3 Encryptionconfiguration Structure
  property_count: 0
  slug: s3-encryptionconfiguration-structure
- name: S3 End Structure
  property_count: 0
  slug: s3-end-structure
- name: S3 Endevent Structure
  property_count: 0
  slug: s3-endevent-structure
- name: S3 Error Structure
  property_count: 0
  slug: s3-error-structure
- name: S3 Errorcode Structure
  property_count: 0
  slug: s3-errorcode-structure
- name: S3 Errordocument Structure
  property_count: 0
  slug: s3-errordocument-structure
- name: S3 Errormessage Structure
  property_count: 0
  slug: s3-errormessage-structure
- name: S3 Errors Structure
  property_count: 0
  slug: s3-errors-structure
- name: S3 Etag Structure
  property_count: 0
  slug: s3-etag-structure
- name: S3 Event Structure
  property_count: 0
  slug: s3-event-structure
- name: S3 Eventbridgeconfiguration Structure
  property_count: 0
  slug: s3-eventbridgeconfiguration-structure
- name: S3 Eventlist Structure
  property_count: 0
  slug: s3-eventlist-structure
- name: S3 Existingobjectreplication Structure
  property_count: 0
  slug: s3-existingobjectreplication-structure
- name: S3 Existingobjectreplicationstatus Structure
  property_count: 0
  slug: s3-existingobjectreplicationstatus-structure
- name: S3 Expiration Structure
  property_count: 0
  slug: s3-expiration-structure
- name: S3 Expirationstatus Structure
  property_count: 0
  slug: s3-expirationstatus-structure
- name: S3 Expiredobjectdeletemarker Structure
  property_count: 0
  slug: s3-expiredobjectdeletemarker-structure
- name: S3 Expires Structure
  property_count: 0
  slug: s3-expires-structure
- name: S3 Exposeheader Structure
  property_count: 0
  slug: s3-exposeheader-structure
- name: S3 Exposeheaders Structure
  property_count: 0
  slug: s3-exposeheaders-structure
- name: S3 Expression Structure
  property_count: 0
  slug: s3-expression-structure
- name: S3 Expressiontype Structure
  property_count: 0
  slug: s3-expressiontype-structure
- name: S3 Fetchowner Structure
  property_count: 0
  slug: s3-fetchowner-structure
- name: S3 Fielddelimiter Structure
  property_count: 0
  slug: s3-fielddelimiter-structure
- name: S3 Fileheaderinfo Structure
  property_count: 0
  slug: s3-fileheaderinfo-structure
- name: S3 Filterrule Structure
  property_count: 0
  slug: s3-filterrule-structure
- name: S3 Filterrulelist Structure
  property_count: 0
  slug: s3-filterrulelist-structure
- name: S3 Filterrulename Structure
  property_count: 0
  slug: s3-filterrulename-structure
- name: S3 Filterrulevalue Structure
  property_count: 0
  slug: s3-filterrulevalue-structure
- name: S3 Getbucketaccelerateconfigurationoutput Structure
  property_count: 0
  slug: s3-getbucketaccelerateconfigurationoutput-structure
- name: S3 Getbucketaccelerateconfigurationrequest Structure
  property_count: 0
  slug: s3-getbucketaccelerateconfigurationrequest-structure
- name: S3 Getbucketacloutput Structure
  property_count: 0
  slug: s3-getbucketacloutput-structure
- name: S3 Getbucketaclrequest Structure
  property_count: 0
  slug: s3-getbucketaclrequest-structure
- name: S3 Getbucketanalyticsconfigurationoutput Structure
  property_count: 0
  slug: s3-getbucketanalyticsconfigurationoutput-structure
- name: S3 Getbucketanalyticsconfigurationrequest Structure
  property_count: 0
  slug: s3-getbucketanalyticsconfigurationrequest-structure
- name: S3 Getbucketcorsoutput Structure
  property_count: 0
  slug: s3-getbucketcorsoutput-structure
- name: S3 Getbucketcorsrequest Structure
  property_count: 0
  slug: s3-getbucketcorsrequest-structure
- name: S3 Getbucketencryptionoutput Structure
  property_count: 0
  slug: s3-getbucketencryptionoutput-structure
- name: S3 Getbucketencryptionrequest Structure
  property_count: 0
  slug: s3-getbucketencryptionrequest-structure
- name: S3 Getbucketintelligenttieringconfigurationoutput Structure
  property_count: 0
  slug: s3-getbucketintelligenttieringconfigurationoutput-structure
- name: S3 Getbucketintelligenttieringconfigurationrequest Structure
  property_count: 0
  slug: s3-getbucketintelligenttieringconfigurationrequest-structure
- name: S3 Getbucketinventoryconfigurationoutput Structure
  property_count: 0
  slug: s3-getbucketinventoryconfigurationoutput-structure
- name: S3 Getbucketinventoryconfigurationrequest Structure
  property_count: 0
  slug: s3-getbucketinventoryconfigurationrequest-structure
- name: S3 Getbucketlifecycleconfigurationoutput Structure
  property_count: 0
  slug: s3-getbucketlifecycleconfigurationoutput-structure
- name: S3 Getbucketlifecycleconfigurationrequest Structure
  property_count: 0
  slug: s3-getbucketlifecycleconfigurationrequest-structure
- name: S3 Getbucketlifecycleoutput Structure
  property_count: 0
  slug: s3-getbucketlifecycleoutput-structure
- name: S3 Getbucketlifecyclerequest Structure
  property_count: 0
  slug: s3-getbucketlifecyclerequest-structure
- name: S3 Getbucketlocationoutput Structure
  property_count: 0
  slug: s3-getbucketlocationoutput-structure
- name: S3 Getbucketlocationrequest Structure
  property_count: 0
  slug: s3-getbucketlocationrequest-structure
- name: S3 Getbucketloggingoutput Structure
  property_count: 0
  slug: s3-getbucketloggingoutput-structure
- name: S3 Getbucketloggingrequest Structure
  property_count: 0
  slug: s3-getbucketloggingrequest-structure
- name: S3 Getbucketmetricsconfigurationoutput Structure
  property_count: 0
  slug: s3-getbucketmetricsconfigurationoutput-structure
- name: S3 Getbucketmetricsconfigurationrequest Structure
  property_count: 0
  slug: s3-getbucketmetricsconfigurationrequest-structure
- name: S3 Getbucketnotificationconfigurationrequest Structure
  property_count: 0
  slug: s3-getbucketnotificationconfigurationrequest-structure
- name: S3 Getbucketownershipcontrolsoutput Structure
  property_count: 0
  slug: s3-getbucketownershipcontrolsoutput-structure
- name: S3 Getbucketownershipcontrolsrequest Structure
  property_count: 0
  slug: s3-getbucketownershipcontrolsrequest-structure
- name: S3 Getbucketpolicyoutput Structure
  property_count: 0
  slug: s3-getbucketpolicyoutput-structure
- name: S3 Getbucketpolicyrequest Structure
  property_count: 0
  slug: s3-getbucketpolicyrequest-structure
- name: S3 Getbucketpolicystatusoutput Structure
  property_count: 0
  slug: s3-getbucketpolicystatusoutput-structure
- name: S3 Getbucketpolicystatusrequest Structure
  property_count: 0
  slug: s3-getbucketpolicystatusrequest-structure
- name: S3 Getbucketreplicationoutput Structure
  property_count: 0
  slug: s3-getbucketreplicationoutput-structure
- name: S3 Getbucketreplicationrequest Structure
  property_count: 0
  slug: s3-getbucketreplicationrequest-structure
- name: S3 Getbucketrequestpaymentoutput Structure
  property_count: 0
  slug: s3-getbucketrequestpaymentoutput-structure
- name: S3 Getbucketrequestpaymentrequest Structure
  property_count: 0
  slug: s3-getbucketrequestpaymentrequest-structure
- name: S3 Getbuckettaggingoutput Structure
  property_count: 0
  slug: s3-getbuckettaggingoutput-structure
- name: S3 Getbuckettaggingrequest Structure
  property_count: 0
  slug: s3-getbuckettaggingrequest-structure
- name: S3 Getbucketversioningoutput Structure
  property_count: 0
  slug: s3-getbucketversioningoutput-structure
- name: S3 Getbucketversioningrequest Structure
  property_count: 0
  slug: s3-getbucketversioningrequest-structure
- name: S3 Getbucketwebsiteoutput Structure
  property_count: 0
  slug: s3-getbucketwebsiteoutput-structure
- name: S3 Getbucketwebsiterequest Structure
  property_count: 0
  slug: s3-getbucketwebsiterequest-structure
- name: S3 Getobjectacloutput Structure
  property_count: 0
  slug: s3-getobjectacloutput-structure
- name: S3 Getobjectaclrequest Structure
  property_count: 0
  slug: s3-getobjectaclrequest-structure
- name: S3 Getobjectattributesoutput Structure
  property_count: 0
  slug: s3-getobjectattributesoutput-structure
- name: S3 Getobjectattributesparts Structure
  property_count: 0
  slug: s3-getobjectattributesparts-structure
- name: S3 Getobjectattributesrequest Structure
  property_count: 0
  slug: s3-getobjectattributesrequest-structure
- name: S3 Getobjectlegalholdoutput Structure
  property_count: 0
  slug: s3-getobjectlegalholdoutput-structure
- name: S3 Getobjectlegalholdrequest Structure
  property_count: 0
  slug: s3-getobjectlegalholdrequest-structure
- name: S3 Getobjectlockconfigurationoutput Structure
  property_count: 0
  slug: s3-getobjectlockconfigurationoutput-structure
- name: S3 Getobjectlockconfigurationrequest Structure
  property_count: 0
  slug: s3-getobjectlockconfigurationrequest-structure
- name: S3 Getobjectoutput Structure
  property_count: 0
  slug: s3-getobjectoutput-structure
- name: S3 Getobjectrequest Structure
  property_count: 0
  slug: s3-getobjectrequest-structure
- name: S3 Getobjectresponsestatuscode Structure
  property_count: 0
  slug: s3-getobjectresponsestatuscode-structure
- name: S3 Getobjectretentionoutput Structure
  property_count: 0
  slug: s3-getobjectretentionoutput-structure
- name: S3 Getobjectretentionrequest Structure
  property_count: 0
  slug: s3-getobjectretentionrequest-structure
- name: S3 Getobjecttaggingoutput Structure
  property_count: 0
  slug: s3-getobjecttaggingoutput-structure
- name: S3 Getobjecttaggingrequest Structure
  property_count: 0
  slug: s3-getobjecttaggingrequest-structure
- name: S3 Getobjecttorrentoutput Structure
  property_count: 0
  slug: s3-getobjecttorrentoutput-structure
- name: S3 Getobjecttorrentrequest Structure
  property_count: 0
  slug: s3-getobjecttorrentrequest-structure
- name: S3 Getpublicaccessblockoutput Structure
  property_count: 0
  slug: s3-getpublicaccessblockoutput-structure
- name: S3 Getpublicaccessblockrequest Structure
  property_count: 0
  slug: s3-getpublicaccessblockrequest-structure
- name: S3 Glacierjobparameters Structure
  property_count: 0
  slug: s3-glacierjobparameters-structure
- name: S3 Grant Structure
  property_count: 0
  slug: s3-grant-structure
- name: S3 Grantee Structure
  property_count: 0
  slug: s3-grantee-structure
- name: S3 Grantfullcontrol Structure
  property_count: 0
  slug: s3-grantfullcontrol-structure
- name: S3 Grantread Structure
  property_count: 0
  slug: s3-grantread-structure
- name: S3 Grantreadacp Structure
  property_count: 0
  slug: s3-grantreadacp-structure
- name: S3 Grants Structure
  property_count: 0
  slug: s3-grants-structure
- name: S3 Grantwrite Structure
  property_count: 0
  slug: s3-grantwrite-structure
- name: S3 Grantwriteacp Structure
  property_count: 0
  slug: s3-grantwriteacp-structure
- name: S3 Headbucketrequest Structure
  property_count: 0
  slug: s3-headbucketrequest-structure
- name: S3 Headobjectoutput Structure
  property_count: 0
  slug: s3-headobjectoutput-structure
- name: S3 Headobjectrequest Structure
  property_count: 0
  slug: s3-headobjectrequest-structure
- name: S3 Hostname Structure
  property_count: 0
  slug: s3-hostname-structure
- name: S3 Httperrorcodereturnedequals Structure
  property_count: 0
  slug: s3-httperrorcodereturnedequals-structure
- name: S3 Httpredirectcode Structure
  property_count: 0
  slug: s3-httpredirectcode-structure
- name: S3 Id Structure
  property_count: 0
  slug: s3-id-structure
- name: S3 Ifmatch Structure
  property_count: 0
  slug: s3-ifmatch-structure
- name: S3 Ifmodifiedsince Structure
  property_count: 0
  slug: s3-ifmodifiedsince-structure
- name: S3 Ifnonematch Structure
  property_count: 0
  slug: s3-ifnonematch-structure
- name: S3 Ifunmodifiedsince Structure
  property_count: 0
  slug: s3-ifunmodifiedsince-structure
- name: S3 Indexdocument Structure
  property_count: 0
  slug: s3-indexdocument-structure
- name: S3 Initiated Structure
  property_count: 0
  slug: s3-initiated-structure
- name: S3 Initiator Structure
  property_count: 0
  slug: s3-initiator-structure
- name: S3 Inputserialization Structure
  property_count: 0
  slug: s3-inputserialization-structure
- name: S3 Intelligenttieringaccesstier Structure
  property_count: 0
  slug: s3-intelligenttieringaccesstier-structure
- name: S3 Intelligenttieringandoperator Structure
  property_count: 0
  slug: s3-intelligenttieringandoperator-structure
- name: S3 Intelligenttieringconfiguration Structure
  property_count: 0
  slug: s3-intelligenttieringconfiguration-structure
- name: S3 Intelligenttieringconfigurationlist Structure
  property_count: 0
  slug: s3-intelligenttieringconfigurationlist-structure
- name: S3 Intelligenttieringdays Structure
  property_count: 0
  slug: s3-intelligenttieringdays-structure
- name: S3 Intelligenttieringfilter Structure
  property_count: 0
  slug: s3-intelligenttieringfilter-structure
- name: S3 Intelligenttieringid Structure
  property_count: 0
  slug: s3-intelligenttieringid-structure
- name: S3 Intelligenttieringstatus Structure
  property_count: 0
  slug: s3-intelligenttieringstatus-structure
- name: S3 Invalidobjectstate Structure
  property_count: 0
  slug: s3-invalidobjectstate-structure
- name: S3 Inventoryconfiguration Structure
  property_count: 0
  slug: s3-inventoryconfiguration-structure
- name: S3 Inventoryconfigurationlist Structure
  property_count: 0
  slug: s3-inventoryconfigurationlist-structure
- name: S3 Inventorydestination Structure
  property_count: 0
  slug: s3-inventorydestination-structure
- name: S3 Inventoryencryption Structure
  property_count: 0
  slug: s3-inventoryencryption-structure
- name: S3 Inventoryfilter Structure
  property_count: 0
  slug: s3-inventoryfilter-structure
- name: S3 Inventoryformat Structure
  property_count: 0
  slug: s3-inventoryformat-structure
- name: S3 Inventoryfrequency Structure
  property_count: 0
  slug: s3-inventoryfrequency-structure
- name: S3 Inventoryid Structure
  property_count: 0
  slug: s3-inventoryid-structure
- name: S3 Inventoryincludedobjectversions Structure
  property_count: 0
  slug: s3-inventoryincludedobjectversions-structure
- name: S3 Inventoryoptionalfield Structure
  property_count: 0
  slug: s3-inventoryoptionalfield-structure
- name: S3 Inventoryoptionalfields Structure
  property_count: 0
  slug: s3-inventoryoptionalfields-structure
- name: S3 Inventorys3Bucketdestination Structure
  property_count: 0
  slug: s3-inventorys3bucketdestination-structure
- name: S3 Inventoryschedule Structure
  property_count: 0
  slug: s3-inventoryschedule-structure
- name: S3 Isenabled Structure
  property_count: 0
  slug: s3-isenabled-structure
- name: S3 Islatest Structure
  property_count: 0
  slug: s3-islatest-structure
- name: S3 Ispublic Structure
  property_count: 0
  slug: s3-ispublic-structure
- name: S3 Istruncated Structure
  property_count: 0
  slug: s3-istruncated-structure
- name: S3 Jsoninput Structure
  property_count: 0
  slug: s3-jsoninput-structure
- name: S3 Jsonoutput Structure
  property_count: 0
  slug: s3-jsonoutput-structure
- name: S3 Jsontype Structure
  property_count: 0
  slug: s3-jsontype-structure
- name: S3 Keycount Structure
  property_count: 0
  slug: s3-keycount-structure
- name: S3 Keymarker Structure
  property_count: 0
  slug: s3-keymarker-structure
- name: S3 Keyprefixequals Structure
  property_count: 0
  slug: s3-keyprefixequals-structure
- name: S3 Kmscontext Structure
  property_count: 0
  slug: s3-kmscontext-structure
- name: S3 Lambdafunctionarn Structure
  property_count: 0
  slug: s3-lambdafunctionarn-structure
- name: S3 Lambdafunctionconfiguration Structure
  property_count: 0
  slug: s3-lambdafunctionconfiguration-structure
- name: S3 Lambdafunctionconfigurationlist Structure
  property_count: 0
  slug: s3-lambdafunctionconfigurationlist-structure
- name: S3 Lastmodified Structure
  property_count: 0
  slug: s3-lastmodified-structure
- name: S3 Lifecycleconfiguration Structure
  property_count: 0
  slug: s3-lifecycleconfiguration-structure
- name: S3 Lifecycleexpiration Structure
  property_count: 0
  slug: s3-lifecycleexpiration-structure
- name: S3 Lifecyclerule Structure
  property_count: 0
  slug: s3-lifecyclerule-structure
- name: S3 Lifecycleruleandoperator Structure
  property_count: 0
  slug: s3-lifecycleruleandoperator-structure
- name: S3 Lifecyclerulefilter Structure
  property_count: 0
  slug: s3-lifecyclerulefilter-structure
- name: S3 Lifecyclerules Structure
  property_count: 0
  slug: s3-lifecyclerules-structure
- name: S3 Listbucketanalyticsconfigurationsoutput Structure
  property_count: 0
  slug: s3-listbucketanalyticsconfigurationsoutput-structure
- name: S3 Listbucketanalyticsconfigurationsrequest Structure
  property_count: 0
  slug: s3-listbucketanalyticsconfigurationsrequest-structure
- name: S3 Listbucketintelligenttieringconfigurationsoutput Structure
  property_count: 0
  slug: s3-listbucketintelligenttieringconfigurationsoutput-structure
- name: S3 Listbucketintelligenttieringconfigurationsrequest Structure
  property_count: 0
  slug: s3-listbucketintelligenttieringconfigurationsrequest-structure
- name: S3 Listbucketinventoryconfigurationsoutput Structure
  property_count: 0
  slug: s3-listbucketinventoryconfigurationsoutput-structure
- name: S3 Listbucketinventoryconfigurationsrequest Structure
  property_count: 0
  slug: s3-listbucketinventoryconfigurationsrequest-structure
- name: S3 Listbucketmetricsconfigurationsoutput Structure
  property_count: 0
  slug: s3-listbucketmetricsconfigurationsoutput-structure
- name: S3 Listbucketmetricsconfigurationsrequest Structure
  property_count: 0
  slug: s3-listbucketmetricsconfigurationsrequest-structure
- name: S3 Listbucketsoutput Structure
  property_count: 0
  slug: s3-listbucketsoutput-structure
- name: S3 Listmultipartuploadsoutput Structure
  property_count: 0
  slug: s3-listmultipartuploadsoutput-structure
- name: S3 Listmultipartuploadsrequest Structure
  property_count: 0
  slug: s3-listmultipartuploadsrequest-structure
- name: S3 Listobjectsoutput Structure
  property_count: 0
  slug: s3-listobjectsoutput-structure
- name: S3 Listobjectsrequest Structure
  property_count: 0
  slug: s3-listobjectsrequest-structure
- name: S3 Listobjectsv2Output Structure
  property_count: 0
  slug: s3-listobjectsv2output-structure
- name: S3 Listobjectsv2Request Structure
  property_count: 0
  slug: s3-listobjectsv2request-structure
- name: S3 Listobjectversionsoutput Structure
  property_count: 0
  slug: s3-listobjectversionsoutput-structure
- name: S3 Listobjectversionsrequest Structure
  property_count: 0
  slug: s3-listobjectversionsrequest-structure
- name: S3 Listpartsoutput Structure
  property_count: 0
  slug: s3-listpartsoutput-structure
- name: S3 Listpartsrequest Structure
  property_count: 0
  slug: s3-listpartsrequest-structure
- name: S3 Location Structure
  property_count: 0
  slug: s3-location-structure
- name: S3 Locationprefix Structure
  property_count: 0
  slug: s3-locationprefix-structure
- name: S3 Loggingenabled Structure
  property_count: 0
  slug: s3-loggingenabled-structure
- name: S3 Marker Structure
  property_count: 0
  slug: s3-marker-structure
- name: S3 Maxageseconds Structure
  property_count: 0
  slug: s3-maxageseconds-structure
- name: S3 Maxkeys Structure
  property_count: 0
  slug: s3-maxkeys-structure
- name: S3 Maxparts Structure
  property_count: 0
  slug: s3-maxparts-structure
- name: S3 Maxuploads Structure
  property_count: 0
  slug: s3-maxuploads-structure
- name: S3 Message Structure
  property_count: 0
  slug: s3-message-structure
- name: S3 Metadata Structure
  property_count: 0
  slug: s3-metadata-structure
- name: S3 Metadatadirective Structure
  property_count: 0
  slug: s3-metadatadirective-structure
- name: S3 Metadataentry Structure
  property_count: 0
  slug: s3-metadataentry-structure
- name: S3 Metadatakey Structure
  property_count: 0
  slug: s3-metadatakey-structure
- name: S3 Metadatavalue Structure
  property_count: 0
  slug: s3-metadatavalue-structure
- name: S3 Metrics Structure
  property_count: 0
  slug: s3-metrics-structure
- name: S3 Metricsandoperator Structure
  property_count: 0
  slug: s3-metricsandoperator-structure
- name: S3 Metricsconfiguration Structure
  property_count: 0
  slug: s3-metricsconfiguration-structure
- name: S3 Metricsconfigurationlist Structure
  property_count: 0
  slug: s3-metricsconfigurationlist-structure
- name: S3 Metricsfilter Structure
  property_count: 0
  slug: s3-metricsfilter-structure
- name: S3 Metricsid Structure
  property_count: 0
  slug: s3-metricsid-structure
- name: S3 Metricsstatus Structure
  property_count: 0
  slug: s3-metricsstatus-structure
- name: S3 Mfa Structure
  property_count: 0
  slug: s3-mfa-structure
- name: S3 Mfadelete Structure
  property_count: 0
  slug: s3-mfadelete-structure
- name: S3 Mfadeletestatus Structure
  property_count: 0
  slug: s3-mfadeletestatus-structure
- name: S3 Minutes Structure
  property_count: 0
  slug: s3-minutes-structure
- name: S3 Missingmeta Structure
  property_count: 0
  slug: s3-missingmeta-structure
- name: S3 Multipartupload Structure
  property_count: 0
  slug: s3-multipartupload-structure
- name: S3 Multipartuploadid Structure
  property_count: 0
  slug: s3-multipartuploadid-structure
- name: S3 Multipartuploadlist Structure
  property_count: 0
  slug: s3-multipartuploadlist-structure
- name: S3 Nextkeymarker Structure
  property_count: 0
  slug: s3-nextkeymarker-structure
- name: S3 Nextmarker Structure
  property_count: 0
  slug: s3-nextmarker-structure
- name: S3 Nextpartnumbermarker Structure
  property_count: 0
  slug: s3-nextpartnumbermarker-structure
- name: S3 Nexttoken Structure
  property_count: 0
  slug: s3-nexttoken-structure
- name: S3 Nextuploadidmarker Structure
  property_count: 0
  slug: s3-nextuploadidmarker-structure
- name: S3 Nextversionidmarker Structure
  property_count: 0
  slug: s3-nextversionidmarker-structure
- name: S3 Noncurrentversionexpiration Structure
  property_count: 0
  slug: s3-noncurrentversionexpiration-structure
- name: S3 Noncurrentversiontransition Structure
  property_count: 0
  slug: s3-noncurrentversiontransition-structure
- name: S3 Noncurrentversiontransitionlist Structure
  property_count: 0
  slug: s3-noncurrentversiontransitionlist-structure
- name: S3 Nosuchbucket Structure
  property_count: 0
  slug: s3-nosuchbucket-structure
- name: S3 Nosuchkey Structure
  property_count: 0
  slug: s3-nosuchkey-structure
- name: S3 Nosuchupload Structure
  property_count: 0
  slug: s3-nosuchupload-structure
- name: S3 Notificationconfiguration Structure
  property_count: 0
  slug: s3-notificationconfiguration-structure
- name: S3 Notificationconfigurationdeprecated Structure
  property_count: 0
  slug: s3-notificationconfigurationdeprecated-structure
- name: S3 Notificationconfigurationfilter Structure
  property_count: 0
  slug: s3-notificationconfigurationfilter-structure
- name: S3 Notificationid Structure
  property_count: 0
  slug: s3-notificationid-structure
- name: S3 Object Structure
  property_count: 0
  slug: s3-object-structure
- name: S3 Objectalreadyinactivetiererror Structure
  property_count: 0
  slug: s3-objectalreadyinactivetiererror-structure
- name: S3 Objectattributes Structure
  property_count: 0
  slug: s3-objectattributes-structure
- name: S3 Objectattributeslist Structure
  property_count: 0
  slug: s3-objectattributeslist-structure
- name: S3 Objectcannedacl Structure
  property_count: 0
  slug: s3-objectcannedacl-structure
- name: S3 Objectidentifier Structure
  property_count: 0
  slug: s3-objectidentifier-structure
- name: S3 Objectidentifierlist Structure
  property_count: 0
  slug: s3-objectidentifierlist-structure
- name: S3 Objectkey Structure
  property_count: 0
  slug: s3-objectkey-structure
- name: S3 Objectlist Structure
  property_count: 0
  slug: s3-objectlist-structure
- name: S3 Objectlockconfiguration Structure
  property_count: 0
  slug: s3-objectlockconfiguration-structure
- name: S3 Objectlockenabled Structure
  property_count: 0
  slug: s3-objectlockenabled-structure
- name: S3 Objectlockenabledforbucket Structure
  property_count: 0
  slug: s3-objectlockenabledforbucket-structure
- name: S3 Objectlocklegalhold Structure
  property_count: 0
  slug: s3-objectlocklegalhold-structure
- name: S3 Objectlocklegalholdstatus Structure
  property_count: 0
  slug: s3-objectlocklegalholdstatus-structure
- name: S3 Objectlockmode Structure
  property_count: 0
  slug: s3-objectlockmode-structure
- name: S3 Objectlockretainuntildate Structure
  property_count: 0
  slug: s3-objectlockretainuntildate-structure
- name: S3 Objectlockretention Structure
  property_count: 0
  slug: s3-objectlockretention-structure
- name: S3 Objectlockretentionmode Structure
  property_count: 0
  slug: s3-objectlockretentionmode-structure
- name: S3 Objectlockrule Structure
  property_count: 0
  slug: s3-objectlockrule-structure
- name: S3 Objectlocktoken Structure
  property_count: 0
  slug: s3-objectlocktoken-structure
- name: S3 Objectnotinactivetiererror Structure
  property_count: 0
  slug: s3-objectnotinactivetiererror-structure
- name: S3 Objectownership Structure
  property_count: 0
  slug: s3-objectownership-structure
- name: S3 Objectpart Structure
  property_count: 0
  slug: s3-objectpart-structure
- name: S3 Objectsize Structure
  property_count: 0
  slug: s3-objectsize-structure
- name: S3 Objectsizegreaterthanbytes Structure
  property_count: 0
  slug: s3-objectsizegreaterthanbytes-structure
- name: S3 Objectsizelessthanbytes Structure
  property_count: 0
  slug: s3-objectsizelessthanbytes-structure
- name: S3 Objectstorageclass Structure
  property_count: 0
  slug: s3-objectstorageclass-structure
- name: S3 Objectversion Structure
  property_count: 0
  slug: s3-objectversion-structure
- name: S3 Objectversionid Structure
  property_count: 0
  slug: s3-objectversionid-structure
- name: S3 Objectversionlist Structure
  property_count: 0
  slug: s3-objectversionlist-structure
- name: S3 Objectversionstorageclass Structure
  property_count: 0
  slug: s3-objectversionstorageclass-structure
- name: S3 Outputlocation Structure
  property_count: 0
  slug: s3-outputlocation-structure
- name: S3 Outputserialization Structure
  property_count: 0
  slug: s3-outputserialization-structure
- name: S3 Owner Structure
  property_count: 0
  slug: s3-owner-structure
- name: S3 Owneroverride Structure
  property_count: 0
  slug: s3-owneroverride-structure
- name: S3 Ownershipcontrols Structure
  property_count: 0
  slug: s3-ownershipcontrols-structure
- name: S3 Ownershipcontrolsrule Structure
  property_count: 0
  slug: s3-ownershipcontrolsrule-structure
- name: S3 Ownershipcontrolsrules Structure
  property_count: 0
  slug: s3-ownershipcontrolsrules-structure
- name: S3 Parquetinput Structure
  property_count: 0
  slug: s3-parquetinput-structure
- name: S3 Part Structure
  property_count: 0
  slug: s3-part-structure
- name: S3 Partnumber Structure
  property_count: 0
  slug: s3-partnumber-structure
- name: S3 Partnumbermarker Structure
  property_count: 0
  slug: s3-partnumbermarker-structure
- name: S3 Parts Structure
  property_count: 0
  slug: s3-parts-structure
- name: S3 Partscount Structure
  property_count: 0
  slug: s3-partscount-structure
- name: S3 Partslist Structure
  property_count: 0
  slug: s3-partslist-structure
- name: S3 Payer Structure
  property_count: 0
  slug: s3-payer-structure
- name: S3 Permission Structure
  property_count: 0
  slug: s3-permission-structure
- name: S3 Policy Structure
  property_count: 0
  slug: s3-policy-structure
- name: S3 Policystatus Structure
  property_count: 0
  slug: s3-policystatus-structure
- name: S3 Prefix Structure
  property_count: 0
  slug: s3-prefix-structure
- name: S3 Priority Structure
  property_count: 0
  slug: s3-priority-structure
- name: S3 Progress Structure
  property_count: 0
  slug: s3-progress-structure
- name: S3 Progressevent Structure
  property_count: 0
  slug: s3-progressevent-structure
- name: S3 Protocol Structure
  property_count: 0
  slug: s3-protocol-structure
- name: S3 Publicaccessblockconfiguration Structure
  property_count: 0
  slug: s3-publicaccessblockconfiguration-structure
- name: S3 Putbucketaccelerateconfigurationrequest Structure
  property_count: 0
  slug: s3-putbucketaccelerateconfigurationrequest-structure
- name: S3 Putbucketaclrequest Structure
  property_count: 0
  slug: s3-putbucketaclrequest-structure
- name: S3 Putbucketanalyticsconfigurationrequest Structure
  property_count: 0
  slug: s3-putbucketanalyticsconfigurationrequest-structure
- name: S3 Putbucketcorsrequest Structure
  property_count: 0
  slug: s3-putbucketcorsrequest-structure
- name: S3 Putbucketencryptionrequest Structure
  property_count: 0
  slug: s3-putbucketencryptionrequest-structure
- name: S3 Putbucketintelligenttieringconfigurationrequest Structure
  property_count: 0
  slug: s3-putbucketintelligenttieringconfigurationrequest-structure
- name: S3 Putbucketinventoryconfigurationrequest Structure
  property_count: 0
  slug: s3-putbucketinventoryconfigurationrequest-structure
- name: S3 Putbucketlifecycleconfigurationrequest Structure
  property_count: 0
  slug: s3-putbucketlifecycleconfigurationrequest-structure
- name: S3 Putbucketlifecyclerequest Structure
  property_count: 0
  slug: s3-putbucketlifecyclerequest-structure
- name: S3 Putbucketloggingrequest Structure
  property_count: 0
  slug: s3-putbucketloggingrequest-structure
- name: S3 Putbucketmetricsconfigurationrequest Structure
  property_count: 0
  slug: s3-putbucketmetricsconfigurationrequest-structure
- name: S3 Putbucketnotificationconfigurationrequest Structure
  property_count: 0
  slug: s3-putbucketnotificationconfigurationrequest-structure
- name: S3 Putbucketnotificationrequest Structure
  property_count: 0
  slug: s3-putbucketnotificationrequest-structure
- name: S3 Putbucketownershipcontrolsrequest Structure
  property_count: 0
  slug: s3-putbucketownershipcontrolsrequest-structure
- name: S3 Putbucketpolicyrequest Structure
  property_count: 0
  slug: s3-putbucketpolicyrequest-structure
- name: S3 Putbucketreplicationrequest Structure
  property_count: 0
  slug: s3-putbucketreplicationrequest-structure
- name: S3 Putbucketrequestpaymentrequest Structure
  property_count: 0
  slug: s3-putbucketrequestpaymentrequest-structure
- name: S3 Putbuckettaggingrequest Structure
  property_count: 0
  slug: s3-putbuckettaggingrequest-structure
- name: S3 Putbucketversioningrequest Structure
  property_count: 0
  slug: s3-putbucketversioningrequest-structure
- name: S3 Putbucketwebsiterequest Structure
  property_count: 0
  slug: s3-putbucketwebsiterequest-structure
- name: S3 Putobjectacloutput Structure
  property_count: 0
  slug: s3-putobjectacloutput-structure
- name: S3 Putobjectaclrequest Structure
  property_count: 0
  slug: s3-putobjectaclrequest-structure
- name: S3 Putobjectlegalholdoutput Structure
  property_count: 0
  slug: s3-putobjectlegalholdoutput-structure
- name: S3 Putobjectlegalholdrequest Structure
  property_count: 0
  slug: s3-putobjectlegalholdrequest-structure
- name: S3 Putobjectlockconfigurationoutput Structure
  property_count: 0
  slug: s3-putobjectlockconfigurationoutput-structure
- name: S3 Putobjectlockconfigurationrequest Structure
  property_count: 0
  slug: s3-putobjectlockconfigurationrequest-structure
- name: S3 Putobjectoutput Structure
  property_count: 0
  slug: s3-putobjectoutput-structure
- name: S3 Putobjectrequest Structure
  property_count: 0
  slug: s3-putobjectrequest-structure
- name: S3 Putobjectretentionoutput Structure
  property_count: 0
  slug: s3-putobjectretentionoutput-structure
- name: S3 Putobjectretentionrequest Structure
  property_count: 0
  slug: s3-putobjectretentionrequest-structure
- name: S3 Putobjecttaggingoutput Structure
  property_count: 0
  slug: s3-putobjecttaggingoutput-structure
- name: S3 Putobjecttaggingrequest Structure
  property_count: 0
  slug: s3-putobjecttaggingrequest-structure
- name: S3 Putpublicaccessblockrequest Structure
  property_count: 0
  slug: s3-putpublicaccessblockrequest-structure
- name: S3 Queuearn Structure
  property_count: 0
  slug: s3-queuearn-structure
- name: S3 Queueconfiguration Structure
  property_count: 0
  slug: s3-queueconfiguration-structure
- name: S3 Queueconfigurationdeprecated Structure
  property_count: 0
  slug: s3-queueconfigurationdeprecated-structure
- name: S3 Queueconfigurationlist Structure
  property_count: 0
  slug: s3-queueconfigurationlist-structure
- name: S3 Quiet Structure
  property_count: 0
  slug: s3-quiet-structure
- name: S3 Quotecharacter Structure
  property_count: 0
  slug: s3-quotecharacter-structure
- name: S3 Quoteescapecharacter Structure
  property_count: 0
  slug: s3-quoteescapecharacter-structure
- name: S3 Quotefields Structure
  property_count: 0
  slug: s3-quotefields-structure
- name: S3 Range Structure
  property_count: 0
  slug: s3-range-structure
- name: S3 Recorddelimiter Structure
  property_count: 0
  slug: s3-recorddelimiter-structure
- name: S3 Recordsevent Structure
  property_count: 0
  slug: s3-recordsevent-structure
- name: S3 Redirect Structure
  property_count: 0
  slug: s3-redirect-structure
- name: S3 Redirectallrequeststo Structure
  property_count: 0
  slug: s3-redirectallrequeststo-structure
- name: S3 Replacekeyprefixwith Structure
  property_count: 0
  slug: s3-replacekeyprefixwith-structure
- name: S3 Replacekeywith Structure
  property_count: 0
  slug: s3-replacekeywith-structure
- name: S3 Replicakmskeyid Structure
  property_count: 0
  slug: s3-replicakmskeyid-structure
- name: S3 Replicamodifications Structure
  property_count: 0
  slug: s3-replicamodifications-structure
- name: S3 Replicamodificationsstatus Structure
  property_count: 0
  slug: s3-replicamodificationsstatus-structure
- name: S3 Replicationconfiguration Structure
  property_count: 0
  slug: s3-replicationconfiguration-structure
- name: S3 Replicationrule Structure
  property_count: 0
  slug: s3-replicationrule-structure
- name: S3 Replicationruleandoperator Structure
  property_count: 0
  slug: s3-replicationruleandoperator-structure
- name: S3 Replicationrulefilter Structure
  property_count: 0
  slug: s3-replicationrulefilter-structure
- name: S3 Replicationrules Structure
  property_count: 0
  slug: s3-replicationrules-structure
- name: S3 Replicationrulestatus Structure
  property_count: 0
  slug: s3-replicationrulestatus-structure
- name: S3 Replicationstatus Structure
  property_count: 0
  slug: s3-replicationstatus-structure
- name: S3 Replicationtime Structure
  property_count: 0
  slug: s3-replicationtime-structure
- name: S3 Replicationtimestatus Structure
  property_count: 0
  slug: s3-replicationtimestatus-structure
- name: S3 Replicationtimevalue Structure
  property_count: 0
  slug: s3-replicationtimevalue-structure
- name: S3 Requestcharged Structure
  property_count: 0
  slug: s3-requestcharged-structure
- name: S3 Requestpayer Structure
  property_count: 0
  slug: s3-requestpayer-structure
- name: S3 Requestpaymentconfiguration Structure
  property_count: 0
  slug: s3-requestpaymentconfiguration-structure
- name: S3 Requestprogress Structure
  property_count: 0
  slug: s3-requestprogress-structure
- name: S3 Requestroute Structure
  property_count: 0
  slug: s3-requestroute-structure
- name: S3 Requesttoken Structure
  property_count: 0
  slug: s3-requesttoken-structure
- name: S3 Responsecachecontrol Structure
  property_count: 0
  slug: s3-responsecachecontrol-structure
- name: S3 Responsecontentdisposition Structure
  property_count: 0
  slug: s3-responsecontentdisposition-structure
- name: S3 Responsecontentencoding Structure
  property_count: 0
  slug: s3-responsecontentencoding-structure
- name: S3 Responsecontentlanguage Structure
  property_count: 0
  slug: s3-responsecontentlanguage-structure
- name: S3 Responsecontenttype Structure
  property_count: 0
  slug: s3-responsecontenttype-structure
- name: S3 Responseexpires Structure
  property_count: 0
  slug: s3-responseexpires-structure
- name: S3 Restore Structure
  property_count: 0
  slug: s3-restore-structure
- name: S3 Restoreobjectoutput Structure
  property_count: 0
  slug: s3-restoreobjectoutput-structure
- name: S3 Restoreobjectrequest Structure
  property_count: 0
  slug: s3-restoreobjectrequest-structure
- name: S3 Restoreoutputpath Structure
  property_count: 0
  slug: s3-restoreoutputpath-structure
- name: S3 Restorerequest Structure
  property_count: 0
  slug: s3-restorerequest-structure
- name: S3 Restorerequesttype Structure
  property_count: 0
  slug: s3-restorerequesttype-structure
- name: S3 Role Structure
  property_count: 0
  slug: s3-role-structure
- name: S3 Routingrule Structure
  property_count: 0
  slug: s3-routingrule-structure
- name: S3 Routingrules Structure
  property_count: 0
  slug: s3-routingrules-structure
- name: S3 Rule Structure
  property_count: 0
  slug: s3-rule-structure
- name: S3 Rules Structure
  property_count: 0
  slug: s3-rules-structure
- name: S3 S3Keyfilter Structure
  property_count: 0
  slug: s3-s3keyfilter-structure
- name: S3 S3Location Structure
  property_count: 0
  slug: s3-s3location-structure
- name: S3 Scanrange Structure
  property_count: 0
  slug: s3-scanrange-structure
- name: S3 Selectobjectcontenteventstream Structure
  property_count: 0
  slug: s3-selectobjectcontenteventstream-structure
- name: S3 Selectobjectcontentoutput Structure
  property_count: 0
  slug: s3-selectobjectcontentoutput-structure
- name: S3 Selectobjectcontentrequest Structure
  property_count: 0
  slug: s3-selectobjectcontentrequest-structure
- name: S3 Selectparameters Structure
  property_count: 0
  slug: s3-selectparameters-structure
- name: S3 Serversideencryption Structure
  property_count: 0
  slug: s3-serversideencryption-structure
- name: S3 Serversideencryptionbydefault Structure
  property_count: 0
  slug: s3-serversideencryptionbydefault-structure
- name: S3 Serversideencryptionconfiguration Structure
  property_count: 0
  slug: s3-serversideencryptionconfiguration-structure
- name: S3 Serversideencryptionrule Structure
  property_count: 0
  slug: s3-serversideencryptionrule-structure
- name: S3 Serversideencryptionrules Structure
  property_count: 0
  slug: s3-serversideencryptionrules-structure
- name: S3 Setting Structure
  property_count: 0
  slug: s3-setting-structure
- name: S3 Size Structure
  property_count: 0
  slug: s3-size-structure
- name: S3 Skipvalidation Structure
  property_count: 0
  slug: s3-skipvalidation-structure
- name: S3 Sourceselectioncriteria Structure
  property_count: 0
  slug: s3-sourceselectioncriteria-structure
- name: S3 Ssecustomeralgorithm Structure
  property_count: 0
  slug: s3-ssecustomeralgorithm-structure
- name: S3 Ssecustomerkey Structure
  property_count: 0
  slug: s3-ssecustomerkey-structure
- name: S3 Ssecustomerkeymd5 Structure
  property_count: 0
  slug: s3-ssecustomerkeymd5-structure
- name: S3 Ssekms Structure
  property_count: 0
  slug: s3-ssekms-structure
- name: S3 Ssekmsencryptedobjects Structure
  property_count: 0
  slug: s3-ssekmsencryptedobjects-structure
- name: S3 Ssekmsencryptedobjectsstatus Structure
  property_count: 0
  slug: s3-ssekmsencryptedobjectsstatus-structure
- name: S3 Ssekmsencryptioncontext Structure
  property_count: 0
  slug: s3-ssekmsencryptioncontext-structure
- name: S3 Ssekmskeyid Structure
  property_count: 0
  slug: s3-ssekmskeyid-structure
- name: S3 Sses3 Structure
  property_count: 0
  slug: s3-sses3-structure
- name: S3 Start Structure
  property_count: 0
  slug: s3-start-structure
- name: S3 Startafter Structure
  property_count: 0
  slug: s3-startafter-structure
- name: S3 Stats Structure
  property_count: 0
  slug: s3-stats-structure
- name: S3 Statsevent Structure
  property_count: 0
  slug: s3-statsevent-structure
- name: S3 Storageclass Structure
  property_count: 0
  slug: s3-storageclass-structure
- name: S3 Storageclassanalysis Structure
  property_count: 0
  slug: s3-storageclassanalysis-structure
- name: S3 Storageclassanalysisdataexport Structure
  property_count: 0
  slug: s3-storageclassanalysisdataexport-structure
- name: S3 Storageclassanalysisschemaversion Structure
  property_count: 0
  slug: s3-storageclassanalysisschemaversion-structure
- name: S3 Suffix Structure
  property_count: 0
  slug: s3-suffix-structure
- name: S3 Tag Structure
  property_count: 0
  slug: s3-tag-structure
- name: S3 Tagcount Structure
  property_count: 0
  slug: s3-tagcount-structure
- name: S3 Tagging Structure
  property_count: 0
  slug: s3-tagging-structure
- name: S3 Taggingdirective Structure
  property_count: 0
  slug: s3-taggingdirective-structure
- name: S3 Taggingheader Structure
  property_count: 0
  slug: s3-taggingheader-structure
- name: S3 Tagset Structure
  property_count: 0
  slug: s3-tagset-structure
- name: S3 Targetbucket Structure
  property_count: 0
  slug: s3-targetbucket-structure
- name: S3 Targetgrant Structure
  property_count: 0
  slug: s3-targetgrant-structure
- name: S3 Targetgrants Structure
  property_count: 0
  slug: s3-targetgrants-structure
- name: S3 Targetprefix Structure
  property_count: 0
  slug: s3-targetprefix-structure
- name: S3 Tier Structure
  property_count: 0
  slug: s3-tier-structure
- name: S3 Tiering Structure
  property_count: 0
  slug: s3-tiering-structure
- name: S3 Tieringlist Structure
  property_count: 0
  slug: s3-tieringlist-structure
- name: S3 Token Structure
  property_count: 0
  slug: s3-token-structure
- name: S3 Topicarn Structure
  property_count: 0
  slug: s3-topicarn-structure
- name: S3 Topicconfiguration Structure
  property_count: 0
  slug: s3-topicconfiguration-structure
- name: S3 Topicconfigurationdeprecated Structure
  property_count: 0
  slug: s3-topicconfigurationdeprecated-structure
- name: S3 Topicconfigurationlist Structure
  property_count: 0
  slug: s3-topicconfigurationlist-structure
- name: S3 Transition Structure
  property_count: 0
  slug: s3-transition-structure
- name: S3 Transitionlist Structure
  property_count: 0
  slug: s3-transitionlist-structure
- name: S3 Transitionstorageclass Structure
  property_count: 0
  slug: s3-transitionstorageclass-structure
- name: S3 Type Structure
  property_count: 0
  slug: s3-type-structure
- name: S3 Uploadidmarker Structure
  property_count: 0
  slug: s3-uploadidmarker-structure
- name: S3 Uploadpartcopyoutput Structure
  property_count: 0
  slug: s3-uploadpartcopyoutput-structure
- name: S3 Uploadpartcopyrequest Structure
  property_count: 0
  slug: s3-uploadpartcopyrequest-structure
- name: S3 Uploadpartoutput Structure
  property_count: 0
  slug: s3-uploadpartoutput-structure
- name: S3 Uploadpartrequest Structure
  property_count: 0
  slug: s3-uploadpartrequest-structure
- name: S3 Uri Structure
  property_count: 0
  slug: s3-uri-structure
- name: S3 Usermetadata Structure
  property_count: 0
  slug: s3-usermetadata-structure
- name: S3 Value Structure
  property_count: 0
  slug: s3-value-structure
- name: S3 Versioncount Structure
  property_count: 0
  slug: s3-versioncount-structure
- name: S3 Versionidmarker Structure
  property_count: 0
  slug: s3-versionidmarker-structure
- name: S3 Versioningconfiguration Structure
  property_count: 0
  slug: s3-versioningconfiguration-structure
- name: S3 Websiteconfiguration Structure
  property_count: 0
  slug: s3-websiteconfiguration-structure
- name: S3 Websiteredirectlocation Structure
  property_count: 0
  slug: s3-websiteredirectlocation-structure
- name: S3 Writegetobjectresponserequest Structure
  property_count: 0
  slug: s3-writegetobjectresponserequest-structure
- name: S3 Years Structure
  property_count: 0
  slug: s3-years-structure
jsonld:
- class_count: 30
  name: Aws S3 Context
  property_count: 0
  slug: aws-s3-context
layout: provider
modified: '2026-05-19'
name: Amazon S3 API
nav: Providers
network: true
overview: 'Amazon S3 API publishes 2 APIs on the [APIs.io](https://apis.io/) network: Amazon Simple Storage Service API and WriteGetObjectResponse#x Amz Request Route&x Amz Request Token API. Tagged areas include Cloud Storage, Object Storage, and Storage.


  The Amazon S3 API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon S3 API''s developer surface includes authentication, engineering blog, support, developer console, pricing, changelog, documentation, and 11 more developer resources.'
plans:
- name: Aws S3 Plans Pricing
  plan_count: 3
  slug: aws-s3-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Aws S3 Rate Limits
  slug: aws-s3-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon S3 API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aws-s3-jsonschema-spectral-rules
- effective_rule_count: 60
  extends:
  - spectral:oas
  name: Amazon S3 API API Rules
  rule_count: 19
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 13
  slug: aws-s3-spectral-rules
score:
  band: developing
  composite: 45.3
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 28.8
    contract_quality: 58.4
    developer_ergonomics: 40.5
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 23.7
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-s3/refs/heads/main/screenshots/aws-s3-2026-06-20T172817.png
security:
- kind: authentication
  name: Aws S3 Authentication
  slug: aws-s3-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws S3 Domain Security
  slug: aws-s3-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws S3 Vulnerability Disclosure
  slug: aws-s3-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws S3 Trust Center
  slug: aws-s3-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-s3
tags:
- Cloud Storage
- Object Storage
- Storage
use_cases:
- description: Store raw data for analytics pipelines using AWS Glue, Athena, and Redshift Spectrum.
  name: Data Lake Storage
- description: Host static websites and single-page applications directly from S3.
  name: Static Website Hosting
- description: Store backups and archives with lifecycle policies to move data to Glacier for long-term retention.
  name: Backup and Archive
- description: Store and serve images, videos, and documents globally via CloudFront CDN.
  name: Media Storage and Distribution
- description: Store user-generated content, application logs, and configuration files.
  name: Application Data Storage
website: https://aws.amazon.com/s3/
---
