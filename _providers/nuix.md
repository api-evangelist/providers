---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Nuix Agentic Access
  operation_count: 34
  slug: nuix-agentic-access
  summary_line: 34 operations · 17 acting
api_count: 2
apis:
- description: GraphQL-based API for querying and managing discovery data within Nuix Discover, supporting queries and mutations for document review, production sets, and legal analytics workflows.
  name: Nuix Discover Connect API
  slug: nuix-discover-connect-api
- baseURL: '{protocol}://{address}:{port}/api/ecc'
  baseurl_source: declared
  description: The Case API from Nuix — 3 operation(s) for case.
  name: Nuix Case API
  slug: nuix-case-api
- baseURL: '{protocol}://{address}:{port}/api/ecc'
  baseurl_source: declared
  description: The Collection and Survey API from Nuix — 4 operation(s) for collection and survey.
  name: Nuix Collection and Survey API
  slug: nuix-collection-and-survey-api
- baseURL: '{protocol}://{address}:{port}/api/ecc'
  baseurl_source: declared
  description: The Collection Configuration API from Nuix — 2 operation(s) for collection configuration.
  name: Nuix Collection Configuration API
  slug: nuix-collection-configuration-api
- baseURL: '{protocol}://{address}:{port}/api/ecc'
  baseurl_source: declared
  description: The Computer API from Nuix — 1 operation(s) for computer.
  name: Nuix Computer API
  slug: nuix-computer-api
- baseURL: '{protocol}://{address}:{port}/api/ecc'
  baseurl_source: declared
  description: The Computer Configuration API from Nuix — 2 operation(s) for computer configuration.
  name: Nuix Computer Configuration API
  slug: nuix-computer-configuration-api
- baseURL: '{protocol}://{address}:{port}/api/ecc'
  baseurl_source: declared
  description: The Custodian API from Nuix — 1 operation(s) for custodian.
  name: Nuix Custodian API
  slug: nuix-custodian-api
- baseURL: '{protocol}://{address}:{port}/api/ecc'
  baseurl_source: declared
  description: The Group API from Nuix — 2 operation(s) for group.
  name: Nuix Group API
  slug: nuix-group-api
- baseURL: '{protocol}://{address}:{port}/api/ecc'
  baseurl_source: declared
  description: The Job API from Nuix — 3 operation(s) for job.
  name: Nuix Job API
  slug: nuix-job-api
- baseURL: '{protocol}://{address}:{port}/api/ecc'
  baseurl_source: declared
  description: The Log API from Nuix — 1 operation(s) for log.
  name: Nuix Log API
  slug: nuix-log-api
- baseURL: '{protocol}://{address}:{port}/api/ecc'
  baseurl_source: declared
  description: The Target API from Nuix — 3 operation(s) for target.
  name: Nuix Target API
  slug: nuix-target-api
- baseURL: '{protocol}://{address}:{port}/api/ecc'
  baseurl_source: declared
  description: The Utility API from Nuix — 3 operation(s) for utility.
  name: Nuix Utility API
  slug: nuix-utility-api
- baseURL: https://discover.nuix.com/api
  baseurl_source: declared
  description: The Access API from Nuix — 2 operation(s) for access.
  name: Nuix Access API
  slug: nuix-access-api
- baseURL: https://discover.nuix.com/api
  baseurl_source: declared
  description: The Analysis API from Nuix — 35 operation(s) for analysis.
  name: Nuix Analysis API
  slug: nuix-analysis-api
- baseURL: https://discover.nuix.com/api
  baseurl_source: declared
  description: The Culling API from Nuix — 21 operation(s) for culling.
  name: Nuix Culling API
  slug: nuix-culling-api
- baseURL: https://discover.nuix.com/api
  baseurl_source: declared
  description: The Export API from Nuix — 15 operation(s) for export.
  name: Nuix Export API
  slug: nuix-export-api
- baseURL: https://discover.nuix.com/api
  baseurl_source: declared
  description: The Inventory API from Nuix — 13 operation(s) for inventory.
  name: Nuix Inventory API
  slug: nuix-inventory-api
- baseURL: https://discover.nuix.com/api
  baseurl_source: declared
  description: The Licensing API from Nuix — 6 operation(s) for licensing.
  name: Nuix Licensing API
  slug: nuix-licensing-api
- baseURL: https://discover.nuix.com/api
  baseurl_source: declared
  description: The Monitoring API from Nuix — 6 operation(s) for monitoring.
  name: Nuix Monitoring API
  slug: nuix-monitoring-api
- baseURL: https://discover.nuix.com/api
  baseurl_source: declared
  description: The Processing API from Nuix — 22 operation(s) for processing.
  name: Nuix Processing API
  slug: nuix-processing-api
- baseURL: https://discover.nuix.com/api
  baseurl_source: declared
  description: The Resources API from Nuix — 18 operation(s) for resources.
  name: Nuix Resources API
  slug: nuix-resources-api
- baseURL: https://discover.nuix.com/api
  baseurl_source: declared
  description: The Scripting API from Nuix — 2 operation(s) for scripting.
  name: Nuix Scripting API
  slug: nuix-scripting-api
- baseURL: https://discover.nuix.com/api
  baseurl_source: declared
  description: The Search API from Nuix — 4 operation(s) for search.
  name: Nuix Search API
  slug: nuix-search-api
- baseURL: https://discover.nuix.com/api
  baseurl_source: declared
  description: The System API from Nuix — 10 operation(s) for system.
  name: Nuix System API
  slug: nuix-system-api
artifact_total: 419
collections:
- collection_type: open
  name: NUIX ECC REST API Command Reference Case API
  slug: open-nuix-case-api
- collection_type: open
  name: NUIX ECC REST API Command Reference Case Collection and Survey API
  slug: open-nuix-collection-and-survey-api
- collection_type: open
  name: NUIX ECC REST API Command Reference Case Collection Configuration API
  slug: open-nuix-collection-configuration-api
- collection_type: open
  name: NUIX ECC REST API Command Reference Case Computer API
  slug: open-nuix-computer-api
- collection_type: open
  name: NUIX ECC REST API Command Reference Case Computer Configuration API
  slug: open-nuix-computer-configuration-api
- collection_type: open
  name: NUIX ECC REST API Command Reference Case Custodian API
  slug: open-nuix-custodian-api
- collection_type: open
  name: NUIX ECC REST API Command Reference Case Group API
  slug: open-nuix-group-api
- collection_type: open
  name: NUIX ECC REST API Command Reference Case Job API
  slug: open-nuix-job-api
- collection_type: open
  name: NUIX ECC REST API Command Reference Case Log API
  slug: open-nuix-log-api
- collection_type: open
  name: NUIX ECC REST API Command Reference Case Target API
  slug: open-nuix-target-api
- collection_type: open
  name: NUIX ECC REST API Command Reference Case Utility API
  slug: open-nuix-utility-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/nuix/overview
- group: commercial
  href: https://artifacts.apis.io/nuix/finops/nuix-finops.yml
  title: ''
  type: FinOps
  url: finops/nuix-finops.yml
- group: operate
  href: https://artifacts.apis.io/nuix/rate-limits/nuix-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nuix-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nuix/plans/nuix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nuix-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/nuix/rules/nuix-rules.yml
  title: ''
  type: Spectral
  url: rules/nuix-rules.yml
- group: design
  href: https://artifacts.apis.io/nuix/rules/nuix-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/nuix-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/nuix/json-ld/nuix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nuix-context.jsonld
- group: design
  href: https://artifacts.apis.io/nuix/vocabulary/nuix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nuix-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/nuix/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/nuix/data-model/nuix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nuix-data-model.yml
- group: operate
  href: https://artifacts.apis.io/nuix/changelog/nuix-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nuix-changelog.yml
- group: design
  href: https://artifacts.apis.io/nuix/conventions/nuix-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nuix-conventions.yml
- group: auth
  href: https://artifacts.apis.io/nuix/security/nuix-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/nuix-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nuix/scopes/nuix-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/nuix-scopes.yml
- group: design
  href: https://artifacts.apis.io/nuix/lifecycle/nuix-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nuix-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/nuix/errors/nuix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nuix-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nuix/conformance/nuix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nuix-conformance.yml
- group: other
  href: https://artifacts.apis.io/nuix/overlays/nuix-case-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nuix-case-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/nuix/llms/nuix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nuix-llms.txt
- group: auth
  href: https://artifacts.apis.io/nuix/well-known/nuix-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nuix-status-security.txt
- group: auth
  href: https://artifacts.apis.io/nuix/well-known/nuix-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nuix-security.txt
- group: auth
  href: https://artifacts.apis.io/nuix/well-known/nuix-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nuix-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/nuix/well-known/nuix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nuix-well-known.yml
- group: other
  href: https://artifacts.apis.io/nuix/hosts/nuix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nuix-hosts.yml
- group: build
  href: https://artifacts.apis.io/nuix/integrations/nuix-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/nuix-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/nuix/vendors/nuix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nuix-vendors.yml
- group: build
  href: https://artifacts.apis.io/nuix/packages/nuix-packages.yml
  title: ''
  type: SDKs
  url: packages/nuix-packages.yml
- group: build
  href: https://artifacts.apis.io/nuix/packages/nuix-packages.yml
  title: ''
  type: Packages
  url: packages/nuix-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.nuix.com/latest/engine/rest/quick-start/home.html
- group: company
  title: ''
  type: BlogRSS
  url: https://www.nuix.com/rss.xml
- group: company
  title: ''
  type: Website
  url: https://www.nuix.com/
- group: agent
  href: https://artifacts.apis.io/nuix/agentic-access/nuix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nuix-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/nuix/security/nuix-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nuix-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nuix/security/nuix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nuix-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/nuix/authentication/nuix-authentication.yml
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
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.nuix.com/en/content/server/DL/projects_frameless/Nuix%20Discover%2010.20%20Online%20Help/Project_Source_Files/Developer_Resources/Connect_API/API_Reference_documentation.htm
- group: other
  title: ''
  type: DeveloperProgram
  url: https://www.nuix.com/nuix-developer-program
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nuix
- group: company
  title: ''
  type: Blog
  url: https://www.nuix.com/resources?resource_type=18
- group: company
  title: ''
  type: Newsroom
  url: https://www.nuix.com/news
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nuix.com/
- group: operate
  title: ''
  type: Support
  url: https://nuix.service-now.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.nuix.com/customer-support-portal
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nuix.com/pricing
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustcenter.nuix.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.nuix.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nuix.com/nuix-website-terms-service
- group: commercial
  title: ''
  type: Legal
  url: https://www.nuix.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nuix.com/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://careers.nuix.com/
- group: company
  title: ''
  type: Investors
  url: https://www.nuix.com/investors
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/nuix
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nuix
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
description: Nuix is a provider of investigative analytics and intelligence software that delivers data privacy, fraud and investigations, and legal eDiscovery solutions (Nuix Neo, Nuix Workstation, Nuix Discover, Nuix Adaptive Security). Developers integrate through the Nuix Engine SDK documented at developer.nuix.com, the GraphQL-based Nuix Discover Connect API, and the self-hosted Nuix Adaptive Security REST API for endpoint collection, cases, jobs and targets.
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
- has_sources: false
  method: generated
  name: Nuix Finops
  primary_unit: ''
  service_category: ''
  slug: nuix-finops
  template: true
graphqls:
- description: Nuix Discover provides a GraphQL-based Connect API (also called the Connect Graph API) for querying and managing eDiscovery data within the Nuix Discover platform. The API supports queries and mutatio
  name: Nuix GraphQL API
  slug: nuix-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuix.png
json_schemas:
- name: AsyncFunctionStatusObject
  property_count: 26
  slug: nuix-async-function-status-object
- name: AsyncFunctionStatus
  property_count: 26
  slug: nuix-async-function-status
- name: BulkApplyItemTagListRequest
  property_count: 13
  slug: nuix-bulk-apply-item-tag-list-request
- name: BulkProductionSetWithProfilesRequest
  property_count: 16
  slug: nuix-bulk-production-set-with-profiles-request
- name: BulkSearcherRequest
  property_count: 20
  slug: nuix-bulk-searcher-request
- name: Computer
  property_count: 13
  slug: nuix-computer
- name: createCaseRequest
  property_count: 2
  slug: nuix-create-case-request
- name: createConfigurationRequest
  property_count: 5
  slug: nuix-create-configuration-request
- name: createConfigurationResponse
  property_count: 8
  slug: nuix-create-configuration-response
- name: createCustodianRequest
  property_count: 3
  slug: nuix-create-custodian-request
- name: createGroupRequest
  property_count: 2
  slug: nuix-create-group-request
- name: createTargetRequest
  property_count: 7
  slug: nuix-create-target-request
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
- name: jobActionRequest
  property_count: 1
  slug: nuix-job-action-request
- name: jobDetail
  property_count: 18
  slug: nuix-job-detail
- name: jobListDetail
  property_count: 22
  slug: nuix-job-list-detail
- name: launchCaseCollectionByConfigurationRequest
  property_count: 5
  slug: nuix-launch-case-collection-by-configuration-request
- name: launchCaseCollectionByConfigurationResponse
  property_count: 2
  slug: nuix-launch-case-collection-by-configuration-response
- name: launchCaseCollectionByPathRequest
  property_count: 10
  slug: nuix-launch-case-collection-by-path-request
- name: launchCaseCollectionByTargetRequest
  property_count: 5
  slug: nuix-launch-case-collection-by-target-request
- name: launchCaseCollectionRequest
  property_count: 5
  slug: nuix-launch-case-collection-request
- name: launchCaseCollectionResponse
  property_count: 2
  slug: nuix-launch-case-collection-response
- name: licenseResponse
  property_count: 3
  slug: nuix-license-response
- name: listCasesResponse
  property_count: 1
  slug: nuix-list-cases-response
- name: listComputerConfResponse
  property_count: 1
  slug: nuix-list-computer-conf-response
- name: listComputerRequest
  property_count: 6
  slug: nuix-list-computer-request
- name: listConfigurationsResponse
  property_count: 1
  slug: nuix-list-configurations-response
- name: listCustodianResponse
  property_count: 1
  slug: nuix-list-custodian-response
- name: listGroupsResponse
  property_count: 1
  slug: nuix-list-groups-response
- name: listJobRequest
  property_count: 6
  slug: nuix-list-job-request
- name: listTargetsResponse
  property_count: 1
  slug: nuix-list-targets-response
- name: LogEntry
  property_count: 9
  slug: nuix-log-entry
- name: modifyCaseRequest
  property_count: 2
  slug: nuix-modify-case-request
- name: modifyGroupRequest
  property_count: 5
  slug: nuix-modify-group-request
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
- name: SearchNativeRequest
  property_count: 25
  slug: nuix-search-native-request
- name: standardResponse
  property_count: 3
  slug: nuix-standard-response
- name: systemInfoResponse
  property_count: 7
  slug: nuix-system-info-response
jsonld:
- class_count: 26
  name: Nuix Context
  property_count: 7
  slug: nuix-context
layout: provider
modified: '2026-10-21'
name: Nuix
nav: Providers
network: true
overview: 'Nuix publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Case API, Collection and Survey API, Collection Configuration API, and 21 more. Tagged areas include Forensics, eDiscovery, Investigations, Compliance, and Data Processing.


  The Nuix catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Nuix''s developer surface includes changelog, getting-started guide, authentication, developer portal, documentation, API reference, engineering blog, and 51 more developer resources.'
plans:
- name: Nuix Plans Pricing
  plan_count: 1
  slug: nuix-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Nuix Rate Limits
  slug: nuix-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Nuix — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nuix-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Nuix API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 4
  slug: nuix-rules
scopes:
- name: Nuix Scopes
  scope_count: 5
  slug: nuix-scopes
  summary_line: 5 scopes
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 36
    catalog_earned: 75.8
    catalog_earned_first_party: 16.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 46.1
    contract_governance: 35.6
    contract_quality: 59.8
    developer_ergonomics: 60.1
    discoverability: 74.1
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 66.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/nuix/nuix-2026-06-20T190513.png
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
skill_count: 3
skills:
- name: nuix-ecc-collect-from-a-custodian
  slug: nuix-ecc-collect-from-a-custodian
- name: nuix-ingest-and-search-a-case
  slug: nuix-ingest-and-search-a-case
- name: nuix-tag-and-export-items
  slug: nuix-tag-and-export-items
slug: nuix
tags:
- Forensics
- eDiscovery
- Investigations
- Compliance
- Data Processing
- Legal Tech
- Intelligence
website: https://www.nuix.com/
---
