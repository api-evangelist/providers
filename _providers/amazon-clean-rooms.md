---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Clean Rooms Agentic Access
  operation_count: 10
  slug: amazon-clean-rooms-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 4
apis:
- baseURL: https://cleanrooms.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing Clean Rooms collaborations
  name: Amazon Clean Rooms Collaborations API
  slug: amazon-clean-rooms-collaborations-api
- baseURL: https://cleanrooms.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing configured tables
  name: Amazon Clean Rooms Configured Tables API
  slug: amazon-clean-rooms-configured-tables-api
- baseURL: https://cleanrooms.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing collaboration memberships
  name: Amazon Clean Rooms Memberships API
  slug: amazon-clean-rooms-memberships-api
- baseURL: https://cleanrooms.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for executing and managing protected queries
  name: Amazon Clean Rooms Protected Queries API
  slug: amazon-clean-rooms-protected-queries-api
artifact_total: 93
asyncapis:
- description: ''
  name: Amazon Clean Rooms Events
  slug: amazon-clean-rooms-events
collections:
- collection_type: postman
  name: Amazon Clean Rooms Collaborations API
  slug: postman-amazon-clean-rooms-collaborations-api
- collection_type: postman
  name: Amazon Clean Rooms Collaborations Configured Tables API
  slug: postman-amazon-clean-rooms-configured-tables-api
- collection_type: postman
  name: Amazon Clean Rooms Collaborations Memberships API
  slug: postman-amazon-clean-rooms-memberships-api
- collection_type: postman
  name: Amazon Clean Rooms Collaborations Protected Queries API
  slug: postman-amazon-clean-rooms-protected-queries-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Clean Rooms Collaborations API
  slug: open-amazon-clean-rooms-collaborations-api
- collection_type: open
  name: Amazon Clean Rooms Collaborations Configured Tables API
  slug: open-amazon-clean-rooms-configured-tables-api
- collection_type: open
  name: Amazon Clean Rooms Collaborations Memberships API
  slug: open-amazon-clean-rooms-memberships-api
- collection_type: open
  name: Amazon Clean Rooms Collaborations Protected Queries API
  slug: open-amazon-clean-rooms-protected-queries-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/amazon-clean-rooms-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-clean-rooms-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-clean-rooms/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-clean-rooms-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-clean-rooms-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-clean-rooms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-clean-rooms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-clean-rooms-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/clean-rooms/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/clean-rooms/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/big-data/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/cleanrooms/
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-clean-rooms
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-clean-rooms-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-clean-rooms-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-clean-rooms-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-clean-rooms-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-clean-rooms-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-clean-rooms-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-clean-rooms-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/amazon-clean-rooms-lifecycle.yml
- group: build
  title: ''
  type: SDKs
  url: packages/amazon-clean-rooms-packages.yml
- group: auth
  title: ''
  type: Security
  url: security/amazon-clean-rooms-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/amazon-clean-rooms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amazon-clean-rooms-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amazon-clean-rooms-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/amazon-clean-rooms-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amazon-clean-rooms-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amazon-clean-rooms-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-clean-rooms-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/amazon-clean-rooms-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/amazon-clean-rooms-tool-crosswalk.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-clean-rooms-conformance.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/clean-rooms/pricing/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/getting-started.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aws.amazon.com/clean-rooms/
created: '2026-03-16'
description: Amazon Clean Rooms enables organizations to collaborate and analyze shared datasets without exposing underlying raw data to partners. Create secure data clean rooms in minutes and collaborate with any company while maintaining data privacy through differential privacy, cryptographic computing, and flexible analytics.
examples:
- key_count: 9
  name: Clean Rooms Collaboration Example
  slug: clean-rooms-collaboration-example
- key_count: 7
  name: Clean Rooms Configured Table Example
  slug: clean-rooms-configured-table-example
- key_count: 6
  name: Clean Rooms Create Collaboration Request Example
  slug: clean-rooms-create-collaboration-request-example
- key_count: 1
  name: Clean Rooms Create Collaboration Response Example
  slug: clean-rooms-create-collaboration-response-example
- key_count: 5
  name: Clean Rooms Create Configured Table Request Example
  slug: clean-rooms-create-configured-table-request-example
- key_count: 1
  name: Clean Rooms Create Configured Table Response Example
  slug: clean-rooms-create-configured-table-response-example
- key_count: 2
  name: Clean Rooms Create Membership Request Example
  slug: clean-rooms-create-membership-request-example
- key_count: 1
  name: Clean Rooms Create Membership Response Example
  slug: clean-rooms-create-membership-response-example
- key_count: 1
  name: Clean Rooms Get Collaboration Response Example
  slug: clean-rooms-get-collaboration-response-example
- key_count: 2
  name: Clean Rooms List Collaborations Response Example
  slug: clean-rooms-list-collaborations-response-example
- key_count: 2
  name: Clean Rooms List Configured Tables Response Example
  slug: clean-rooms-list-configured-tables-response-example
- key_count: 2
  name: Clean Rooms List Memberships Response Example
  slug: clean-rooms-list-memberships-response-example
- key_count: 2
  name: Clean Rooms List Protected Queries Response Example
  slug: clean-rooms-list-protected-queries-response-example
- key_count: 7
  name: Clean Rooms Membership Example
  slug: clean-rooms-membership-example
- key_count: 5
  name: Clean Rooms Protected Query Example
  slug: clean-rooms-protected-query-example
- key_count: 3
  name: Clean Rooms Start Protected Query Request Example
  slug: clean-rooms-start-protected-query-request-example
- key_count: 1
  name: Clean Rooms Start Protected Query Response Example
  slug: clean-rooms-start-protected-query-response-example
features:
- description: Analyze shared datasets without exposing underlying raw data using differential privacy and cryptographic computing.
  name: Privacy-Preserving Analytics
- description: Collaborate with Snowflake and AWS datasets without data movement or ETL pipelines.
  name: Zero-ETL Integration
- description: Execute SQL, PySpark, or ML model queries on partner data with configurable privacy controls.
  name: Protected Queries
- description: Run analytics using SQL, PySpark, or custom ML models with granular access controls.
  name: Flexible Analysis Methods
- description: Audit data usage with analysis logging to track all queries run within a collaboration.
  name: Analysis Logging
- description: Match customer records across applications and channels without sharing PII.
  name: Customer Record Matching
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-clean-rooms.png
integrations:
- description: Store and retrieve collaboration data and query results in S3.
  name: Amazon S3
- description: Zero-ETL integration with Snowflake datasets for cross-platform collaboration.
  name: Snowflake
- description: Configure Glue tables as the underlying data source for Clean Rooms configured tables.
  name: AWS Glue
- description: Run analytics on collaboration results stored in S3 using Athena.
  name: Amazon Athena
- description: Apply ML models within protected Clean Rooms jobs.
  name: Amazon SageMaker
- description: Control access to Clean Rooms resources with IAM policies.
  name: AWS IAM
- description: Audit all Clean Rooms API calls via CloudTrail.
  name: AWS CloudTrail
json_schemas:
- name: Collaboration
  property_count: 9
  slug: clean-rooms-collaboration
- name: ConfiguredTable
  property_count: 7
  slug: clean-rooms-configured-table
- name: CreateCollaborationRequest
  property_count: 6
  slug: clean-rooms-create-collaboration-request
- name: CreateCollaborationResponse
  property_count: 1
  slug: clean-rooms-create-collaboration-response
- name: CreateConfiguredTableRequest
  property_count: 5
  slug: clean-rooms-create-configured-table-request
- name: CreateConfiguredTableResponse
  property_count: 1
  slug: clean-rooms-create-configured-table-response
- name: CreateMembershipRequest
  property_count: 2
  slug: clean-rooms-create-membership-request
- name: CreateMembershipResponse
  property_count: 1
  slug: clean-rooms-create-membership-response
- name: GetCollaborationResponse
  property_count: 1
  slug: clean-rooms-get-collaboration-response
- name: ListCollaborationsResponse
  property_count: 2
  slug: clean-rooms-list-collaborations-response
- name: ListConfiguredTablesResponse
  property_count: 2
  slug: clean-rooms-list-configured-tables-response
- name: ListMembershipsResponse
  property_count: 2
  slug: clean-rooms-list-memberships-response
- name: ListProtectedQueriesResponse
  property_count: 2
  slug: clean-rooms-list-protected-queries-response
- name: Membership
  property_count: 7
  slug: clean-rooms-membership
- name: ProtectedQuery
  property_count: 5
  slug: clean-rooms-protected-query
- name: StartProtectedQueryRequest
  property_count: 3
  slug: clean-rooms-start-protected-query-request
- name: StartProtectedQueryResponse
  property_count: 1
  slug: clean-rooms-start-protected-query-response
json_structures:
- name: Clean Rooms Collaboration Structure
  property_count: 9
  slug: clean-rooms-collaboration-structure
- name: Clean Rooms Configured Table Structure
  property_count: 7
  slug: clean-rooms-configured-table-structure
- name: Clean Rooms Create Collaboration Request Structure
  property_count: 6
  slug: clean-rooms-create-collaboration-request-structure
- name: Clean Rooms Create Collaboration Response Structure
  property_count: 1
  slug: clean-rooms-create-collaboration-response-structure
- name: Clean Rooms Create Configured Table Request Structure
  property_count: 5
  slug: clean-rooms-create-configured-table-request-structure
- name: Clean Rooms Create Configured Table Response Structure
  property_count: 1
  slug: clean-rooms-create-configured-table-response-structure
- name: Clean Rooms Create Membership Request Structure
  property_count: 2
  slug: clean-rooms-create-membership-request-structure
- name: Clean Rooms Create Membership Response Structure
  property_count: 1
  slug: clean-rooms-create-membership-response-structure
- name: Clean Rooms Get Collaboration Response Structure
  property_count: 1
  slug: clean-rooms-get-collaboration-response-structure
- name: Clean Rooms List Collaborations Response Structure
  property_count: 2
  slug: clean-rooms-list-collaborations-response-structure
- name: Clean Rooms List Configured Tables Response Structure
  property_count: 2
  slug: clean-rooms-list-configured-tables-response-structure
- name: Clean Rooms List Memberships Response Structure
  property_count: 2
  slug: clean-rooms-list-memberships-response-structure
- name: Clean Rooms List Protected Queries Response Structure
  property_count: 2
  slug: clean-rooms-list-protected-queries-response-structure
- name: Clean Rooms Membership Structure
  property_count: 7
  slug: clean-rooms-membership-structure
- name: Clean Rooms Protected Query Structure
  property_count: 5
  slug: clean-rooms-protected-query-structure
- name: Clean Rooms Start Protected Query Request Structure
  property_count: 3
  slug: clean-rooms-start-protected-query-request-structure
- name: Clean Rooms Start Protected Query Response Structure
  property_count: 1
  slug: clean-rooms-start-protected-query-response-structure
jsonld:
- class_count: 19
  name: Amazon Clean Rooms Context
  property_count: 32
  slug: amazon-clean-rooms-context
layout: provider
modified: '2026-08-13'
name: Amazon Clean Rooms
nav: Providers
network: true
overview: 'Amazon Clean Rooms publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Collaborations API, Configured Tables API, Memberships API, and 1 more. Tagged areas include Cleanrooms, Data Collaboration, Privacy, Analytics, and Marketing.


  The Amazon Clean Rooms catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Amazon Clean Rooms'' developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 41 more developer resources.'
plans:
- name: Amazon Clean Rooms Plans Pricing
  plan_count: 0
  slug: amazon-clean-rooms-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 6
  name: Amazon Clean Rooms Rate Limits
  slug: amazon-clean-rooms-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Clean Rooms API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-clean-rooms-jsonschema-spectral-rules
- effective_rule_count: 75
  extends:
  - spectral:oas
  name: Amazon Clean Rooms API Rules
  rule_count: 34
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 17
  slug: amazon-clean-rooms-spectral-rules
score:
  band: strong
  composite: 64.3
  coverage:
    artifact_dirs: 30
    catalog_gap: 32.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 33.3
    contract_quality: 40.1
    developer_ergonomics: 90.5
    discoverability: 81.5
    governance: 33.3
    operational_transparency: 92.1
  previous_composite: 64.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-clean-rooms/refs/heads/main/screenshots/amazon-clean-rooms-2026-07-25T195939.png
security:
- kind: authentication
  name: Amazon Clean Rooms Authentication
  slug: amazon-clean-rooms-authentication
  summary_line: aws-sigv4 · 1 scheme
- kind: domain-security
  name: Amazon Clean Rooms Domain Security
  slug: amazon-clean-rooms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Clean Rooms Vulnerability Disclosure
  slug: amazon-clean-rooms-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Clean Rooms Trust Center
  slug: amazon-clean-rooms-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-clean-rooms
tags:
- Cleanrooms
- Data Collaboration
- Privacy
- Analytics
- Marketing
use_cases:
- description: Measure campaign effectiveness by combining advertiser and publisher data in a privacy-safe environment.
  name: Marketing Measurement
- description: Build comprehensive customer views by combining data from multiple channels and partners.
  name: Customer Insights
- description: Enable multi-company research and product development with secure data sharing.
  name: Collaborative Research
- description: Analyze sensitive financial or health data across organizations for risk prediction without data exposure.
  name: Risk Assessment
- description: Create and activate privacy-safe audience segments across advertising platforms.
  name: Audience Activation
website: https://aws.amazon.com/clean-rooms/
---
