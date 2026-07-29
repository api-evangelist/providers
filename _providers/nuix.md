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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 135
  human_in_the_loop: 1
  name: Nuix Agentic Access
  operation_count: 241
  slug: nuix-agentic-access
  summary_line: 241 operations · 135 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Primary RESTful service for processing unstructured data, managing forensic cases, ingesting evidence, running search queries, performing OCR and entity extraction, and orchestrating asynchronous proc
  name: Nuix Core Engine REST API
  slug: nuix-core-engine-rest-api
- description: GraphQL-based API for querying and managing discovery data within Nuix Discover, supporting queries and mutations for document review, production sets, and legal analytics workflows.
  name: Nuix Discover Connect API
  slug: nuix-discover-connect-api
- description: The Case API from Nuix — 3 operation(s) for case.
  name: Nuix Case API
  slug: nuix-case-api
- description: The Collection and Survey API from Nuix — 4 operation(s) for collection and survey.
  name: Nuix Collection and Survey API
  slug: nuix-collection-and-survey-api
- description: The Collection Configuration API from Nuix — 2 operation(s) for collection configuration.
  name: Nuix Collection Configuration API
  slug: nuix-collection-configuration-api
- description: The Computer API from Nuix — 1 operation(s) for computer.
  name: Nuix Computer API
  slug: nuix-computer-api
- description: The Computer Configuration API from Nuix — 2 operation(s) for computer configuration.
  name: Nuix Computer Configuration API
  slug: nuix-computer-configuration-api
- description: The Custodian API from Nuix — 1 operation(s) for custodian.
  name: Nuix Custodian API
  slug: nuix-custodian-api
- description: The Group API from Nuix — 2 operation(s) for group.
  name: Nuix Group API
  slug: nuix-group-api
- description: The Job API from Nuix — 3 operation(s) for job.
  name: Nuix Job API
  slug: nuix-job-api
- description: The Log API from Nuix — 1 operation(s) for log.
  name: Nuix Log API
  slug: nuix-log-api
- description: The Target API from Nuix — 3 operation(s) for target.
  name: Nuix Target API
  slug: nuix-target-api
- description: The Utility API from Nuix — 3 operation(s) for utility.
  name: Nuix Utility API
  slug: nuix-utility-api
artifact_total: 356
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nuix-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nuix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nuix-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.nuix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nuix.com/latest/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nuix
- group: company
  title: ''
  type: Blog
  url: https://www.nuix.com/blog
- group: operate
  title: ''
  type: Status
  url: https://status.nuix.com/
- group: operate
  title: ''
  type: Support
  url: https://nuix.service-now.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nuix.com/legal/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nuix.com/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/nuix/refs/heads/main/plans/nuix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/nuix/refs/heads/main/rate-limits/nuix-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/nuix/refs/heads/main/finops/nuix-finops.yml
created: '2026-06-13'
description: Nuix is an investigative analytics and intelligence platform providing REST APIs for processing unstructured data, managing forensic cases, running entity extraction, conducting digital investigations, and supporting eDiscovery and compliance workflows across legal, security, and law enforcement domains.
examples:
- key_count: 1
  name: Nuix Rest Asyncfunctions Key Status Put Cancel A Function
  slug: nuix-rest-asyncFunctions-key-status-put-Cancel-a-Function
- key_count: 1
  name: Nuix Rest Asyncfunctions Key Status Put Cancel A Function.Json
  slug: nuix-rest-asyncFunctions-key-status-put-Cancel-a-Function.json
- key_count: 1
  name: Nuix Rest Asyncfunctions Key Status Put Pause A Function
  slug: nuix-rest-asyncFunctions-key-status-put-Pause-a-Function
- key_count: 1
  name: Nuix Rest Asyncfunctions Key Status Put Pause A Function.Json
  slug: nuix-rest-asyncFunctions-key-status-put-Pause-a-Function.json
- key_count: 1
  name: Nuix Rest Asyncfunctions Key Status Put Resume A Function
  slug: nuix-rest-asyncFunctions-key-status-put-Resume-a-Function
- key_count: 1
  name: Nuix Rest Asyncfunctions Key Status Put Resume A Function.Json
  slug: nuix-rest-asyncFunctions-key-status-put-Resume-a-Function.json
- key_count: 1
  name: Nuix Rest Asyncfunctions Key Status Put Stop A Function
  slug: nuix-rest-asyncFunctions-key-status-put-Stop-a-Function
- key_count: 1
  name: Nuix Rest Asyncfunctions Key Status Put Stop A Function.Json
  slug: nuix-rest-asyncFunctions-key-status-put-Stop-a-Function.json
- key_count: 1
  name: Nuix Rest Authenticatedusers Login Put Username, Password, License, And Requested Workers.Json
  slug: nuix-rest-authenticatedUsers-login-put-Username,-Password,-License,-and-Requested-Workers.json
- key_count: 1
  name: Nuix Rest Authenticatedusers Login Put Username, Password, And License.Json
  slug: nuix-rest-authenticatedUsers-login-put-Username,-Password,-and-License.json
- key_count: 1
  name: Nuix Rest Authenticatedusers Login Put Username And Password Only
  slug: nuix-rest-authenticatedUsers-login-put-Username-And-Password-Only
- key_count: 1
  name: Nuix Rest Authenticatedusers Login Put Username And Password Only.Json
  slug: nuix-rest-authenticatedUsers-login-put-Username-And-Password-Only.json
- key_count: 1
  name: Nuix Rest Authenticatedusers Login Put Username Password License A
  slug: nuix-rest-authenticatedUsers-login-put-Username-Password-License-a
- key_count: 1
  name: Nuix Rest Authenticatedusers Login Put Username Password And Licens
  slug: nuix-rest-authenticatedUsers-login-put-Username-Password-and-Licens
- key_count: 1
  name: Nuix Rest Cases Caseid Asyncfunctions Search Post Asynchronous Search
  slug: nuix-rest-cases-caseId-asyncFunctions-search-post-Asynchronous-Search
- key_count: 1
  name: Nuix Rest Cases Caseid Custodians Post Create Custodian
  slug: nuix-rest-cases-caseId-custodians-post-Create-Custodian
- key_count: 1
  name: Nuix Rest Cases Caseid Custodians Post Create Custodian.Json
  slug: nuix-rest-cases-caseId-custodians-post-Create-Custodian.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Centera Post Simple Centera Cluster Ingesti
  slug: nuix-rest-cases-caseId-evidence-centera-post-Simple-Centera-Cluster-Ingesti
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Centera Post Simple Centera Cluster Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-centera-post-Simple-Centera-Cluster-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Documentum Post Simple Documentum Ingestion
  slug: nuix-rest-cases-caseId-evidence-documentum-post-Simple-Documentum-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Dropbox Post Simple Dropbox Ingestion
  slug: nuix-rest-cases-caseId-evidence-dropbox-post-Simple-Dropbox-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Dropbox Post Simple Dropbox Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-dropbox-post-Simple-Dropbox-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Ev Post Simple Enterprise Vault Ingest
  slug: nuix-rest-cases-caseId-evidence-ev-post-Simple-Enterprise-Vault-Ingest
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Ev Post Simple Enterprise Vault Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-ev-post-Simple-Enterprise-Vault-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Exchange Post Simple Exchange Ingestion
  slug: nuix-rest-cases-caseId-evidence-exchange-post-Simple-Exchange-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Exchange Post Simple Exchange Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-exchange-post-Simple-Exchange-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence File Post Simple File Ingestion
  slug: nuix-rest-cases-caseId-evidence-file-post-Simple-File-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence File Post Simple File Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-file-post-Simple-File-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Loadfile Post Simple Loadfile Ingestion
  slug: nuix-rest-cases-caseId-evidence-loadFile-post-Simple-Loadfile-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Loadfile Post Simple Loadfile Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-loadFile-post-Simple-Loadfile-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Mail Post Gmail Imap Ingestion
  slug: nuix-rest-cases-caseId-evidence-mail-post-GMail-IMAP-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Mail Post Gmail Imap Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-mail-post-GMail-IMAP-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Ms365 Post Simple Microsoft 365 Ingestion
  slug: nuix-rest-cases-caseId-evidence-ms365-post-Simple-Microsoft-365-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Oracle Post Simple Oracle Server Ingestion
  slug: nuix-rest-cases-caseId-evidence-oracle-post-Simple-Oracle-Server-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Oracle Post Simple Oracle Server Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-oracle-post-Simple-Oracle-Server-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Post File And S3 Bucket Ingestion
  slug: nuix-rest-cases-caseId-evidence-post-File-and-S3-Bucket-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Post File And S3 Bucket Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-post-File-and-S3-Bucket-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Repository Post Simple Evidence Repository Ing
  slug: nuix-rest-cases-caseId-evidence-repository-post-Simple-Evidence-Repository-Ing
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Repository Post Simple Evidence Repository Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-repository-post-Simple-Evidence-Repository-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence S3 Post Sample S3 Bucket Ingestion
  slug: nuix-rest-cases-caseId-evidence-s3-post-Sample-S3-Bucket-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence S3 Post Sample S3 Bucket Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-s3-post-Sample-S3-Bucket-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Sharepoint Post Simple Sharepoint Ingestion
  slug: nuix-rest-cases-caseId-evidence-sharepoint-post-Simple-Sharepoint-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Sharepoint Post Simple Sharepoint Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-sharepoint-post-Simple-Sharepoint-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Slack Post Simple Slack Ingestion
  slug: nuix-rest-cases-caseId-evidence-slack-post-Simple-Slack-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Splitfiles Post Simple Split Files Ingestion
  slug: nuix-rest-cases-caseId-evidence-splitFiles-post-Simple-Split-Files-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Splitfiles Post Simple Split Files Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-splitFiles-post-Simple-Split-Files-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Sql Post Simple Sql Server Ingestion
  slug: nuix-rest-cases-caseId-evidence-sql-post-Simple-SQL-Server-Ingestion
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Sql Post Simple Sql Server Ingestion.Json
  slug: nuix-rest-cases-caseId-evidence-sql-post-Simple-SQL-Server-Ingestion.json
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Ssh Post Ssh Ingestion Authentication K
  slug: nuix-rest-cases-caseId-evidence-ssh-post-SSH-Ingestion-Authentication-K
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Ssh Post Ssh Ingestion Username Passwor
  slug: nuix-rest-cases-caseId-evidence-ssh-post-SSH-Ingestion-Username-Passwor
- key_count: 1
  name: Nuix Rest Cases Caseid Evidence Twitter Post Simple Historical Twitter Inge
  slug: nuix-rest-cases-caseId-evidence-twitter-post-Simple-Historical-Twitter-Inge
- key_count: 1
  name: Nuix Rest Cases Caseid Itemsets Itemsetnameorguid Items Patch Bulk Add Items To Itemset
  slug: nuix-rest-cases-caseId-itemSets-itemSetNameOrGuid-items-patch-Bulk-Add-Items-to-ItemSet
- key_count: 1
  name: Nuix Rest Cases Caseid Itemsets Itemsetnameorguid Items Patch Bulk Remove Items From Itemset
  slug: nuix-rest-cases-caseId-itemSets-itemSetNameOrGuid-items-patch-Bulk-Remove-Items-From-ItemSet
- key_count: 1
  name: Nuix Rest Cases Caseid Itemsets Itemsetnameorguid Items Post Add Items To An Item Set
  slug: nuix-rest-cases-caseId-itemSets-itemSetNameOrGuid-items-post-Add-Items-to-an-Item-Set
- key_count: 1
  name: Nuix Rest Cases Caseid Itemsets Itemsetnameorguid Put Rename An Item Set
  slug: nuix-rest-cases-caseId-itemSets-itemSetNameOrGuid-put-Rename-an-Item-Set
- key_count: 1
  name: Nuix Rest Cases Caseid Itemsets Post Simple Item Set Create Request
  slug: nuix-rest-cases-caseId-itemSets-post-Simple-Item-Set-Create-Request
- key_count: 1
  name: Nuix Rest Cases Caseid Items Ocr Put Simple Ocr Request
  slug: nuix-rest-cases-caseId-items-ocr-put-Simple-OCR-Request
- key_count: 1
  name: Nuix Rest Cases Caseid Items Put Reload All Items
  slug: nuix-rest-cases-caseId-items-put-Reload-All-Items
- key_count: 1
  name: Nuix Rest Cases Caseid Stores Put Populate Binary Store And Prin
  slug: nuix-rest-cases-caseId-stores-put-Populate-binary-store-and-prin
- key_count: 1
  name: Nuix Rest Cases Caseid Stores Put Populate Binary Store And Printed Image Store.Json
  slug: nuix-rest-cases-caseId-stores-put-Populate-binary-store-and-printed-image-store.json
- key_count: 1
  name: Nuix Rest Cases Caseid Subset Post Elasticsearch Case Subset
  slug: nuix-rest-cases-caseId-subset-post-Elasticsearch-Case-Subset
- key_count: 1
  name: Nuix Rest Cases Caseid Subset Post Elasticsearch Case Subset.Json
  slug: nuix-rest-cases-caseId-subset-post-Elasticsearch-Case-Subset.json
- key_count: 1
  name: Nuix Rest Cases Caseid Subset Post Simple Case Subset
  slug: nuix-rest-cases-caseId-subset-post-Simple-Case-Subset
- key_count: 1
  name: Nuix Rest Cases Caseid Subset Post Simple Case Subset.Json
  slug: nuix-rest-cases-caseId-subset-post-Simple-Case-Subset.json
- key_count: 1
  name: Nuix Rest Cases Caseid Tags Patch Create Tags
  slug: nuix-rest-cases-caseId-tags-patch-Create-Tags
- key_count: 1
  name: Nuix Rest Cases Caseid Tags Patch Create Tags.Json
  slug: nuix-rest-cases-caseId-tags-patch-Create-Tags.json
- key_count: 1
  name: Nuix Rest Cases Caseid Tags Patch Delete Tags
  slug: nuix-rest-cases-caseId-tags-patch-Delete-Tags
- key_count: 1
  name: Nuix Rest Cases Caseid Tags Patch Delete Tags.Json
  slug: nuix-rest-cases-caseId-tags-patch-Delete-Tags.json
- key_count: 1
  name: Nuix Rest Cases Caseid Tags Patch Rename Tags
  slug: nuix-rest-cases-caseId-tags-patch-Rename-Tags
- key_count: 1
  name: Nuix Rest Cases Caseid Tags Patch Rename Tags.Json
  slug: nuix-rest-cases-caseId-tags-patch-Rename-Tags.json
- key_count: 1
  name: Nuix Rest Cases Caseid Tags Tagname Put Simple Rename Tag Request
  slug: nuix-rest-cases-caseId-tags-tagName-put-Simple-Rename-Tag-Request
- key_count: 1
  name: Nuix Rest Cases Caseid Tags Tagname Put Simple Rename Tag Request.Json
  slug: nuix-rest-cases-caseId-tags-tagName-put-Simple-Rename-Tag-Request.json
- key_count: 1
  name: Nuix Rest Cases Caseid Userscripts Put Javascript
  slug: nuix-rest-cases-caseId-userScripts-put-Javascript
- key_count: 1
  name: Nuix Rest Cases Caseid Userscripts Put Python
  slug: nuix-rest-cases-caseId-userScripts-put-Python
- key_count: 1
  name: Nuix Rest Cases Caseid Userscripts Put Ruby
  slug: nuix-rest-cases-caseId-userScripts-put-Ruby
- key_count: 1
  name: Nuix Rest Cases Post Compoundcasecreation
  slug: nuix-rest-cases-post-CompoundCaseCreation
- key_count: 1
  name: Nuix Rest Cases Post Compoundcasecreation.Json
  slug: nuix-rest-cases-post-CompoundCaseCreation.json
- key_count: 1
  name: Nuix Rest Cases Post Elasticsearchcasecreation
  slug: nuix-rest-cases-post-ElasticsearchCaseCreation
- key_count: 1
  name: Nuix Rest Cases Post Elasticsearchcasecreation.Json
  slug: nuix-rest-cases-post-ElasticsearchCaseCreation.json
- key_count: 1
  name: Nuix Rest Cases Post Simplecasecreation
  slug: nuix-rest-cases-post-SimpleCaseCreation
- key_count: 1
  name: Nuix Rest Cases Post Simplecasecreation.Json
  slug: nuix-rest-cases-post-SimpleCaseCreation.json
- key_count: 1
  name: Nuix Rest System Properties Propertyname Put Update Property Example
  slug: nuix-rest-system-properties-propertyName-put-Update-Property-Example
- key_count: 1
  name: Nuix Rest Userscripts Put Javascript
  slug: nuix-rest-userScripts-put-Javascript
- key_count: 1
  name: Nuix Rest Userscripts Put Python
  slug: nuix-rest-userScripts-put-Python
- key_count: 1
  name: Nuix Rest Userscripts Put Ruby
  slug: nuix-rest-userScripts-put-Ruby
- key_count: 1
  name: Nuix Rest V1 Cases Caseid Productionsets Post Simple Production Set
  slug: nuix-rest-v1-cases-caseId-productionSets-post-Simple-Production-Set
finops:
- name: Nuix Finops
  service_category: ''
  slug: nuix-finops
graphqls:
- description: Nuix Discover provides a GraphQL-based Connect API (also called the Connect Graph API) for querying and managing eDiscovery data within the Nuix Discover platform. The API supports queries and mutatio
  name: Nuix GraphQL API
  slug: nuix-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuix.png
json_schemas:
- name: Case
  property_count: 3
  slug: nuix-ecc-case
- name: CollectionDetail
  property_count: 4
  slug: nuix-ecc-collectiondetail
- name: Computer
  property_count: 13
  slug: nuix-ecc-computer
- name: ComputerConf
  property_count: 17
  slug: nuix-ecc-computerconf
- name: ComputerJobs
  property_count: 3
  slug: nuix-ecc-computerjobs
- name: Configuration
  property_count: 9
  slug: nuix-ecc-configuration
- name: createCaseRequest
  property_count: 2
  slug: nuix-ecc-createcaserequest
- name: createConfigurationRequest
  property_count: 5
  slug: nuix-ecc-createconfigurationrequest
- name: createConfigurationResponse
  property_count: 8
  slug: nuix-ecc-createconfigurationresponse
- name: createCustodianRequest
  property_count: 3
  slug: nuix-ecc-createcustodianrequest
- name: createGroupRequest
  property_count: 2
  slug: nuix-ecc-creategrouprequest
- name: createTargetRequest
  property_count: 7
  slug: nuix-ecc-createtargetrequest
- name: Custodian
  property_count: 2
  slug: nuix-ecc-custodian
- name: DateCriteria
  property_count: 8
  slug: nuix-ecc-datecriteria
- name: Evidence
  property_count: 9
  slug: nuix-ecc-evidence
- name: Extension
  property_count: 2
  slug: nuix-ecc-extension
- name: FileType
  property_count: 3
  slug: nuix-ecc-filetype
- name: FolderSpec
  property_count: 4
  slug: nuix-ecc-folderspec
- name: Group
  property_count: 4
  slug: nuix-ecc-group
- name: Hash
  property_count: 3
  slug: nuix-ecc-hash
- name: jobActionRequest
  property_count: 1
  slug: nuix-ecc-jobactionrequest
- name: JobCreated
  property_count: 4
  slug: nuix-ecc-jobcreated
- name: jobDetail
  property_count: 18
  slug: nuix-ecc-jobdetail
- name: jobListDetail
  property_count: 22
  slug: nuix-ecc-joblistdetail
- name: Keyword
  property_count: 4
  slug: nuix-ecc-keyword
- name: launchCaseCollectionByConfigurationRequest
  property_count: 5
  slug: nuix-ecc-launchcasecollectionbyconfigurationrequest
- name: launchCaseCollectionByConfigurationResponse
  property_count: 2
  slug: nuix-ecc-launchcasecollectionbyconfigurationresponse
- name: launchCaseCollectionByPathRequest
  property_count: 10
  slug: nuix-ecc-launchcasecollectionbypathrequest
- name: launchCaseCollectionByTargetRequest
  property_count: 5
  slug: nuix-ecc-launchcasecollectionbytargetrequest
- name: launchCaseCollectionRequest
  property_count: 5
  slug: nuix-ecc-launchcasecollectionrequest
- name: launchCaseCollectionResponse
  property_count: 2
  slug: nuix-ecc-launchcasecollectionresponse
- name: licenseResponse
  property_count: 3
  slug: nuix-ecc-licenseresponse
- name: listCaseCollectionResponse
  property_count: 1
  slug: nuix-ecc-listcasecollectionresponse
- name: listCasesResponse
  property_count: 1
  slug: nuix-ecc-listcasesresponse
- name: listComputerConfResponse
  property_count: 1
  slug: nuix-ecc-listcomputerconfresponse
- name: listComputerRequest
  property_count: 6
  slug: nuix-ecc-listcomputerrequest
- name: listConfigurationsResponse
  property_count: 1
  slug: nuix-ecc-listconfigurationsresponse
- name: listCustodianResponse
  property_count: 1
  slug: nuix-ecc-listcustodianresponse
- name: listGroupsResponse
  property_count: 1
  slug: nuix-ecc-listgroupsresponse
- name: listJobRequest
  property_count: 6
  slug: nuix-ecc-listjobrequest
- name: listTargetsResponse
  property_count: 1
  slug: nuix-ecc-listtargetsresponse
- name: LogEntry
  property_count: 9
  slug: nuix-ecc-logentry
- name: modifyCaseRequest
  property_count: 2
  slug: nuix-ecc-modifycaserequest
- name: modifyGroupRequest
  property_count: 5
  slug: nuix-ecc-modifygrouprequest
- name: standardResponse
  property_count: 3
  slug: nuix-ecc-standardresponse
- name: systemInfoResponse
  property_count: 7
  slug: nuix-ecc-systeminforesponse
- name: Target
  property_count: 7
  slug: nuix-ecc-target
- name: TargetInputs
  property_count: 3
  slug: nuix-ecc-targetinputs
- name: Task
  property_count: 12
  slug: nuix-ecc-task
- name: TaskCreated
  property_count: 4
  slug: nuix-ecc-taskcreated
- name: TaskToCreate
  property_count: 13
  slug: nuix-ecc-tasktocreate
- name: AboutResponse
  property_count: 5
  slug: nuix-rest-aboutresponse
- name: AboutResponseV1
  property_count: 12
  slug: nuix-rest-aboutresponsev1
- name: ApplicationHealth
  property_count: 2
  slug: nuix-rest-applicationhealth
- name: ApplyCustomMetadataResponse
  property_count: 2
  slug: nuix-rest-applycustommetadataresponse
- name: ApplyTagListRequest
  property_count: 12
  slug: nuix-rest-applytaglistrequest
- name: ApplyTagListResponse
  property_count: 3
  slug: nuix-rest-applytaglistresponse
- name: AsyncFunctionResponse
  property_count: 2
  slug: nuix-rest-asyncfunctionresponse
- name: AsyncFunctionStatus
  property_count: 26
  slug: nuix-rest-asyncfunctionstatus
- name: AsyncFunctionStatusesResponse
  property_count: 7
  slug: nuix-rest-asyncfunctionstatusesresponse
- name: AsyncFunctionStatusObject
  property_count: 26
  slug: nuix-rest-asyncfunctionstatusobject
- name: AuditStatus
  property_count: 4
  slug: nuix-rest-auditstatus
- name: AuthenticationRequest
  property_count: 4
  slug: nuix-rest-authenticationrequest
- name: AuthenticationResponse
  property_count: 6
  slug: nuix-rest-authenticationresponse
- name: BatchLoadDetailsResponse
  property_count: 10
  slug: nuix-rest-batchloaddetailsresponse
- name: BulkApplyCaseTagListRequest
  property_count: 3
  slug: nuix-rest-bulkapplycasetaglistrequest
- name: BulkApplyCustomMetadataResponse
  property_count: 4
  slug: nuix-rest-bulkapplycustommetadataresponse
- name: BulkApplyItemCustomMetadataRequest
  property_count: 2
  slug: nuix-rest-bulkapplyitemcustommetadatarequest
- name: BulkApplyItemSetChangeResponse
  property_count: 1
  slug: nuix-rest-bulkapplyitemsetchangeresponse
- name: BulkApplyItemTagListRequest
  property_count: 13
  slug: nuix-rest-bulkapplyitemtaglistrequest
- name: BulkExclusionRequest
  property_count: 13
  slug: nuix-rest-bulkexclusionrequest
- name: BulkInclusionRequest
  property_count: 11
  slug: nuix-rest-bulkinclusionrequest
- name: BulkIngestionRequest
  property_count: 11
  slug: nuix-rest-bulkingestionrequest
- name: BulkItemCustomMetadataDeleteRequest
  property_count: 4
  slug: nuix-rest-bulkitemcustommetadatadeleterequest
- name: BulkItemCustomMetadataRequest
  property_count: 6
  slug: nuix-rest-bulkitemcustommetadatarequest
- name: BulkItemSetItemsRequest
  property_count: 2
  slug: nuix-rest-bulkitemsetitemsrequest
- name: BulkProductionSetWithProfilesRequest
  property_count: 16
  slug: nuix-rest-bulkproductionsetwithprofilesrequest
- name: BulkSearcherRequest
  property_count: 20
  slug: nuix-rest-bulksearcherrequest
- name: CaseDeleteResponse
  property_count: 4
  slug: nuix-rest-casedeleteresponse
- name: CaseDigest
  property_count: 16
  slug: nuix-rest-casedigest
- name: CaseFunctionQueue
  property_count: 2
  slug: nuix-rest-casefunctionqueue
- name: CaseHistoryEventResponse
  property_count: 9
  slug: nuix-rest-casehistoryeventresponse
- name: CaseMetadataField
  property_count: 2
  slug: nuix-rest-casemetadatafield
- name: CaseModification
  property_count: 1
  slug: nuix-rest-casemodification
- name: CaseResponse
  property_count: 22
  slug: nuix-rest-caseresponse
- name: CaseSubsetMetadata
  property_count: 5
  slug: nuix-rest-casesubsetmetadata
- name: CaseSubsetProcessingSettings
  property_count: 4
  slug: nuix-rest-casesubsetprocessingsettings
- name: CharsetResponse
  property_count: 2
  slug: nuix-rest-charsetresponse
- name: Cluster
  property_count: 1
  slug: nuix-rest-cluster
- name: ClusteredRestErrorResponse
  property_count: 5
  slug: nuix-rest-clusteredresterrorresponse
- name: ClusterHealth
  property_count: 4
  slug: nuix-rest-clusterhealth
- name: ClusterNode
  property_count: 4
  slug: nuix-rest-clusternode
- name: ClusterNodeDetails
  property_count: 13
  slug: nuix-rest-clusternodedetails
- name: ClusterRunRequest
  property_count: 6
  slug: nuix-rest-clusterrunrequest
- name: ClusterRunResponse
  property_count: 6
  slug: nuix-rest-clusterrunresponse
- name: ClusterThirdPartyDependency
  property_count: 2
  slug: nuix-rest-clusterthirdpartydependency
- name: ConfigurationChangeResponse
  property_count: 2
  slug: nuix-rest-configurationchangeresponse
- name: CountRequest
  property_count: 1
  slug: nuix-rest-countrequest
- name: CountResponse
  property_count: 4
  slug: nuix-rest-countresponse
- name: CreateCaseRequest
  property_count: 7
  slug: nuix-rest-createcaserequest
- name: CreateCaseSubsetRequest
  property_count: 15
  slug: nuix-rest-createcasesubsetrequest
- name: CreateReviewJobOptions
  property_count: 5
  slug: nuix-rest-createreviewjoboptions
- name: CreateReviewJobRequest
  property_count: 2
  slug: nuix-rest-createreviewjobrequest
- name: CreateTagListResponse
  property_count: 3
  slug: nuix-rest-createtaglistresponse
- name: CustodianRequest
  property_count: 2
  slug: nuix-rest-custodianrequest
- name: CustodianResponse
  property_count: 2
  slug: nuix-rest-custodianresponse
- name: CustomMetadataFieldResponse
  property_count: 6
  slug: nuix-rest-custommetadatafieldresponse
- name: CustomMetadataRequest
  property_count: 5
  slug: nuix-rest-custommetadatarequest
- name: CustomMetadataResponse
  property_count: 6
  slug: nuix-rest-custommetadataresponse
- name: DeduplicationQueryListRequest
  property_count: 2
  slug: nuix-rest-deduplicationquerylistrequest
- name: DeleteTagListResponse
  property_count: 3
  slug: nuix-rest-deletetaglistresponse
- name: DirectoryAccess
  property_count: 8
  slug: nuix-rest-directoryaccess
- name: ElasticSearchSettings
  property_count: 33
  slug: nuix-rest-elasticsearchsettings
- name: EntityType
  property_count: 2
  slug: nuix-rest-entitytype
- name: EntityTypesResponse
  property_count: 1
  slug: nuix-rest-entitytypesresponse
- name: EvidenceContainer
  property_count: 7
  slug: nuix-rest-evidencecontainer
- name: EvidenceContainerWithTargets
  property_count: 24
  slug: nuix-rest-evidencecontainerwithtargets
- name: EvidenceRepository
  property_count: 8
  slug: nuix-rest-evidencerepository
- name: ExportOptions
  property_count: 9
  slug: nuix-rest-exportoptions
- name: ExportRequest
  property_count: 9
  slug: nuix-rest-exportrequest
- name: FamilyStatisticsResponse
  property_count: 4
  slug: nuix-rest-familystatisticsresponse
- name: FileUpload
  property_count: 3
  slug: nuix-rest-fileupload
- name: FileUploadResponse
  property_count: 1
  slug: nuix-rest-fileuploadresponse
- name: GenericItemGuidResponse
  property_count: 3
  slug: nuix-rest-genericitemguidresponse
- name: GenericResponse
  property_count: 1
  slug: nuix-rest-genericresponse
- name: ImagingOptions
  property_count: 23
  slug: nuix-rest-imagingoptions
- name: IngestibleCenteraCluster
  property_count: 2
  slug: nuix-rest-ingestiblecenteracluster
- name: IngestibleDocumentum
  property_count: 8
  slug: nuix-rest-ingestibledocumentum
- name: IngestibleDropbox
  property_count: 3
  slug: nuix-rest-ingestibledropbox
- name: IngestibleEnterpriseVault
  property_count: 8
  slug: nuix-rest-ingestibleenterprisevault
- name: IngestibleExchangeMailbox
  property_count: 9
  slug: nuix-rest-ingestibleexchangemailbox
- name: IngestibleFile
  property_count: 1
  slug: nuix-rest-ingestiblefile
- name: IngestibleLoadFile
  property_count: 2
  slug: nuix-rest-ingestibleloadfile
- name: IngestibleMailStore
  property_count: 5
  slug: nuix-rest-ingestiblemailstore
- name: IngestibleMicrosoft365
  property_count: 16
  slug: nuix-rest-ingestiblemicrosoft365
- name: IngestibleOracleServer
  property_count: 7
  slug: nuix-rest-ingestibleoracleserver
- name: IngestibleS3Bucket
  property_count: 5
  slug: nuix-rest-ingestibles3bucket
- name: IngestibleSharepoint
  property_count: 4
  slug: nuix-rest-ingestiblesharepoint
- name: IngestibleSlack
  property_count: 5
  slug: nuix-rest-ingestibleslack
- name: IngestibleSplitFileList
  property_count: 1
  slug: nuix-rest-ingestiblesplitfilelist
- name: IngestibleSQLServer
  property_count: 7
  slug: nuix-rest-ingestiblesqlserver
- name: IngestibleSSH
  property_count: 10
  slug: nuix-rest-ingestiblessh
- name: IngestibleTwitter
  property_count: 4
  slug: nuix-rest-ingestibletwitter
- name: InvestigatorTimeZoneResponse
  property_count: 1
  slug: nuix-rest-investigatortimezoneresponse
- name: ItemCommentRequest
  property_count: 1
  slug: nuix-rest-itemcommentrequest
- name: ItemCommentResponse
  property_count: 2
  slug: nuix-rest-itemcommentresponse
- name: ItemCustodianRequest
  property_count: 1
  slug: nuix-rest-itemcustodianrequest
- name: ItemCustodianResponse
  property_count: 2
  slug: nuix-rest-itemcustodianresponse
- name: ItemGuids
  property_count: 1
  slug: nuix-rest-itemguids
- name: ItemMarshallingOptions
  property_count: 14
  slug: nuix-rest-itemmarshallingoptions
- name: ItemPropertiesRequest
  property_count: 2
  slug: nuix-rest-itempropertiesrequest
- name: ItemSetAddItemsRequest
  property_count: 2
  slug: nuix-rest-itemsetadditemsrequest
- name: ItemSetBatchResponse
  property_count: 2
  slug: nuix-rest-itemsetbatchresponse
- name: ItemSetCreateRequest
  property_count: 7
  slug: nuix-rest-itemsetcreaterequest
- name: ItemSetDuplicatesResponse
  property_count: 1
  slug: nuix-rest-itemsetduplicatesresponse
- name: ItemSetItemsResponse
  property_count: 5
  slug: nuix-rest-itemsetitemsresponse
- name: ItemSetNameChangeRequest
  property_count: 1
  slug: nuix-rest-itemsetnamechangerequest
- name: ItemSetRemoveItemsRequest
  property_count: 4
  slug: nuix-rest-itemsetremoveitemsrequest
- name: ItemSetRequest
  property_count: 7
  slug: nuix-rest-itemsetrequest
- name: ItemSetResponse
  property_count: 4
  slug: nuix-rest-itemsetresponse
- name: ItemSizeResponse
  property_count: 2
  slug: nuix-rest-itemsizeresponse
- name: ItemSizesRequest
  property_count: 3
  slug: nuix-rest-itemsizesrequest
- name: ItemsShinglesRequest
  property_count: 4
  slug: nuix-rest-itemsshinglesrequest
- name: ItemTextResponse
  property_count: 5
  slug: nuix-rest-itemtextresponse
- name: KeyStoreKeyParameters
  property_count: 4
  slug: nuix-rest-keystorekeyparameters
- name: KindTypeResponse
  property_count: 3
  slug: nuix-rest-kindtyperesponse
- name: LanguageResponse
  property_count: 3
  slug: nuix-rest-languageresponse
- name: Languages
  property_count: 0
  slug: nuix-rest-languages
- name: LicenseDescription
  property_count: 16
  slug: nuix-rest-licensedescription
- name: MarkupSet
  property_count: 4
  slug: nuix-rest-markupset
- name: MarkupSetDeleteResponse
  property_count: 2
  slug: nuix-rest-markupsetdeleteresponse
- name: MarkupSetRequest
  property_count: 3
  slug: nuix-rest-markupsetrequest
- name: MarshalledItems
  property_count: 7
  slug: nuix-rest-marshalleditems
- name: MetadataItemDetails
  property_count: 3
  slug: nuix-rest-metadataitemdetails
- name: Microsoft365VersionFilterOptions
  property_count: 2
  slug: nuix-rest-microsoft365versionfilteroptions
- name: MimeTypeProcessingSetting
  property_count: 2
  slug: nuix-rest-mimetypeprocessingsetting
- name: MimeTypeSpecificProcessingSettings
  property_count: 7
  slug: nuix-rest-mimetypespecificprocessingsettings
- name: NamedEntity
  property_count: 2
  slug: nuix-rest-namedentity
- name: NmsUser
  property_count: 2
  slug: nuix-rest-nmsuser
- name: NodeHealth
  property_count: 4
  slug: nuix-rest-nodehealth
- name: NuixItemKindResponse
  property_count: 2
  slug: nuix-rest-nuixitemkindresponse
- name: NuixItemType
  property_count: 5
  slug: nuix-rest-nuixitemtype
- name: NuixItemTypeResponse
  property_count: 5
  slug: nuix-rest-nuixitemtyperesponse
- name: NuixReviewJobItem
  property_count: 2
  slug: nuix-rest-nuixreviewjobitem
- name: NuixTaskRequest
  property_count: 8
  slug: nuix-rest-nuixtaskrequest
- name: OcrOptions
  property_count: 12
  slug: nuix-rest-ocroptions
- name: OcrOptionsV2
  property_count: 13
  slug: nuix-rest-ocroptionsv2
- name: OcrRequest
  property_count: 5
  slug: nuix-rest-ocrrequest
- name: OcrRequestV2
  property_count: 7
  slug: nuix-rest-ocrrequestv2
- name: OcrTemplateDetails
  property_count: 21
  slug: nuix-rest-ocrtemplatedetails
- name: OperatingSystemDigest
  property_count: 8
  slug: nuix-rest-operatingsystemdigest
- name: ParallelProcessingSettings
  property_count: 7
  slug: nuix-rest-parallelprocessingsettings
- name: PasswordDiscoverySettings
  property_count: 2
  slug: nuix-rest-passworddiscoverysettings
- name: PopulateStoresRequest
  property_count: 6
  slug: nuix-rest-populatestoresrequest
- name: ProcessorSettings
  property_count: 51
  slug: nuix-rest-processorsettings
- name: ProductionSetRequest
  property_count: 12
  slug: nuix-rest-productionsetrequest
- name: ProductionSetResponse
  property_count: 9
  slug: nuix-rest-productionsetresponse
- name: PromoteToDiscoverRequest
  property_count: 5
  slug: nuix-rest-promotetodiscoverrequest
- name: QueryValidationResponse
  property_count: 3
  slug: nuix-rest-queryvalidationresponse
- name: QueueStateNuixTaskRequest
  property_count: 5
  slug: nuix-rest-queuestatenuixtaskrequest
- name: ReloadItemsIngestionRequest
  property_count: 10
  slug: nuix-rest-reloaditemsingestionrequest
- name: RescanEvidenceRepositoriesSettings
  property_count: 1
  slug: nuix-rest-rescanevidencerepositoriessettings
- name: ReviewJobAddItemsOptions
  property_count: 1
  slug: nuix-rest-reviewjobadditemsoptions
- name: ReviewJobAddItemsRequest
  property_count: 2
  slug: nuix-rest-reviewjobadditemsrequest
- name: ReviewJobResponse
  property_count: 2
  slug: nuix-rest-reviewjobresponse
- name: SearchHit
  property_count: 2
  slug: nuix-rest-searchhit
- name: SearchHitRequest
  property_count: 1
  slug: nuix-rest-searchhitrequest
- name: SearchHitResponse
  property_count: 3
  slug: nuix-rest-searchhitresponse
- name: SearchMacroResponse
  property_count: 2
  slug: nuix-rest-searchmacroresponse
- name: SearchMacroStructuredResponse
  property_count: 2
  slug: nuix-rest-searchmacrostructuredresponse
- name: SearchNativeRequest
  property_count: 25
  slug: nuix-rest-searchnativerequest
- name: SearchNativeResult
  property_count: 14
  slug: nuix-rest-searchnativeresult
- name: Sequence
  property_count: 0
  slug: nuix-rest-sequence
- name: SingleContainerIngestionRequestIngestibleCenteraCluster
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestiblecenteracluster
- name: SingleContainerIngestionRequestIngestibleDocumentum
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestibledocumentum
- name: SingleContainerIngestionRequestIngestibleDropbox
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestibledropbox
- name: SingleContainerIngestionRequestIngestibleEnterpriseVault
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestibleenterprisevault
- name: SingleContainerIngestionRequestIngestibleExchangeMailbox
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestibleexchangemailbox
- name: SingleContainerIngestionRequestIngestibleFile
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestiblefile
- name: SingleContainerIngestionRequestIngestibleLoadFile
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestibleloadfile
- name: SingleContainerIngestionRequestIngestibleMailStore
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestiblemailstore
- name: SingleContainerIngestionRequestIngestibleMicrosoft365
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestiblemicrosoft365
- name: SingleContainerIngestionRequestIngestibleOracleServer
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestibleoracleserver
- name: SingleContainerIngestionRequestIngestibleS3Bucket
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestibles3bucket
- name: SingleContainerIngestionRequestIngestibleSharepoint
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestiblesharepoint
- name: SingleContainerIngestionRequestIngestibleSlack
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestibleslack
- name: SingleContainerIngestionRequestIngestibleSplitFileList
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestiblesplitfilelist
- name: SingleContainerIngestionRequestIngestibleSQLServer
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestiblesqlserver
- name: SingleContainerIngestionRequestIngestibleSSH
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestiblessh
- name: SingleContainerIngestionRequestIngestibleTwitter
  property_count: 11
  slug: nuix-rest-singlecontaineringestionrequestingestibletwitter
- name: SingleRepositoryIngestionRequest
  property_count: 10
  slug: nuix-rest-singlerepositoryingestionrequest
- name: SlipsheetsRequest
  property_count: 2
  slug: nuix-rest-slipsheetsrequest
- name: Success
  property_count: 1
  slug: nuix-rest-success
- name: SystemPropertyRequest
  property_count: 1
  slug: nuix-rest-systempropertyrequest
- name: SystemPropertyResponse
  property_count: 3
  slug: nuix-rest-systempropertyresponse
- name: TagExpansion
  property_count: 12
  slug: nuix-rest-tagexpansion
- name: TagList
  property_count: 1
  slug: nuix-rest-taglist
- name: TagRequest
  property_count: 2
  slug: nuix-rest-tagrequest
- name: TaskStatusRequest
  property_count: 1
  slug: nuix-rest-taskstatusrequest
- name: ThirdPartyDependencyResponse
  property_count: 5
  slug: nuix-rest-thirdpartydependencyresponse
- name: ThumbnailUtilityRequest
  property_count: 2
  slug: nuix-rest-thumbnailutilityrequest
- name: ThumbnailUtilityRequestDimension
  property_count: 2
  slug: nuix-rest-thumbnailutilityrequestdimension
- name: TimezoneRequest
  property_count: 1
  slug: nuix-rest-timezonerequest
- name: UserScriptRequest
  property_count: 9
  slug: nuix-rest-userscriptrequest
- name: UserScriptRequestV2
  property_count: 8
  slug: nuix-rest-userscriptrequestv2
- name: WordCountsRequest
  property_count: 10
  slug: nuix-rest-wordcountsrequest
- name: WordCountsResponse
  property_count: 2
  slug: nuix-rest-wordcountsresponse
jsonld:
- class_count: 26
  name: Nuix Context
  property_count: 7
  slug: nuix-context
layout: provider
modified: '2026-06-13'
name: Nuix
nav: Providers
network: true
overview: 'Nuix publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Core Engine REST API, Case API, Collection and Survey API, and 9 more. Tagged areas include Forensics, eDiscovery, Investigations, Compliance, and Data Processing.


  The Nuix catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nuix''s developer surface includes authentication, developer portal, documentation, GitHub presence, engineering blog, status page, support, and 8 more developer resources.'
plans:
- name: Nuix Plans Pricing
  plan_count: 4
  slug: nuix-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 4
  name: Nuix Rate Limits
  slug: nuix-rate-limits
rules:
- name: Nuix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nuix-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.2
  delta: -4.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 67.4
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 58.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuix/refs/heads/main/screenshots/nuix-2026-06-20T190513.png
security:
- kind: authentication
  name: Nuix Authentication
  slug: nuix-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Nuix Domain Security
  slug: nuix-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nuix Vulnerability Disclosure
  slug: nuix-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nuix
tags:
- Forensics
- eDiscovery
- Investigations
- Compliance
- Data Processing
- Legal Technology
- Intelligence
website: https://developer.nuix.com/
---
