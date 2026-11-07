---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 13
  name: Gcp Cloud Storage Agentic Access
  operation_count: 38
  slug: gcp-cloud-storage-agentic-access
  summary_line: 38 operations · 26 acting · 13 human-in-the-loop
api_count: 1
apis:
- description: Amazon S3-compatible XML API for Google Cloud Storage.
  name: Google Cloud Storage XML API
  slug: google-cloud-storage-xml-api
- baseURL: https://storage.googleapis.com/storage/v1
  baseurl_source: declared
  description: Operations for managing bucket-level access control lists
  name: Google Cloud Storage BucketAccessControls API
  slug: gcp-cloud-storage-bucketaccesscontrols-api
- baseURL: https://storage.googleapis.com/storage/v1
  baseurl_source: declared
  description: Operations for managing Cloud Storage buckets
  name: Google Cloud Storage Buckets API
  slug: gcp-cloud-storage-buckets-api
- baseURL: https://storage.googleapis.com/storage/v1
  baseurl_source: declared
  description: Operations for managing default object access controls on buckets
  name: Google Cloud Storage DefaultObjectAccessControls API
  slug: gcp-cloud-storage-defaultobjectaccesscontrols-api
- baseURL: https://storage.googleapis.com/storage/v1
  baseurl_source: declared
  description: Operations for managing object-level access control lists
  name: Google Cloud Storage ObjectAccessControls API
  slug: gcp-cloud-storage-objectaccesscontrols-api
- baseURL: https://storage.googleapis.com/storage/v1
  baseurl_source: declared
  description: Operations for managing objects within Cloud Storage buckets
  name: Google Cloud Storage Objects API
  slug: gcp-cloud-storage-objects-api
- baseURL: https://storage.googleapis.com
  baseurl_source: declared
  description: The anywhereCaches API from Google Cloud Storage — 5 operation(s) for anywherecaches.
  name: Google Cloud Storage Anywhere Caches API
  slug: gcp-cloud-storage-anywherecaches-api
- baseURL: https://storage.googleapis.com
  baseurl_source: declared
  description: The Folders API from Google Cloud Storage — 4 operation(s) for folders.
  name: Google Cloud Storage Folders API
  slug: gcp-cloud-storage-folders-api
- baseURL: https://storage.googleapis.com
  baseurl_source: declared
  description: The managedFolders API from Google Cloud Storage — 4 operation(s) for managedfolders.
  name: Google Cloud Storage Managed Folders API
  slug: gcp-cloud-storage-managedfolders-api
- baseURL: https://storage.googleapis.com
  baseurl_source: declared
  description: The Notifications API from Google Cloud Storage — 2 operation(s) for notifications.
  name: Google Cloud Storage Notifications API
  slug: gcp-cloud-storage-notifications-api
- baseURL: https://storage.googleapis.com
  baseurl_source: declared
  description: The Operations API from Google Cloud Storage — 4 operation(s) for operations.
  name: Google Cloud Storage Operations API
  slug: gcp-cloud-storage-operations-api
- baseURL: https://storage.googleapis.com
  baseurl_source: declared
  description: The Projects API from Google Cloud Storage — 3 operation(s) for projects.
  name: Google Cloud Storage Projects API
  slug: gcp-cloud-storage-projects-api
- baseURL: https://storage.googleapis.com
  baseurl_source: declared
  description: The rapidCaches API from Google Cloud Storage — 3 operation(s) for rapidcaches.
  name: Google Cloud Storage Rapid Caches API
  slug: gcp-cloud-storage-rapidcaches-api
artifact_total: 107
collections:
- collection_type: postman
  name: Google Cloud Storage JSON BucketAccessControls API
  slug: postman-gcp-cloud-storage-bucketaccesscontrols-api
- collection_type: postman
  name: Google Cloud Storage JSON BucketAccessControls Buckets API
  slug: postman-gcp-cloud-storage-buckets-api
- collection_type: postman
  name: Google Cloud Storage JSON BucketAccessControls DefaultObjectAccessControls API
  slug: postman-gcp-cloud-storage-defaultobjectaccesscontrols-api
- collection_type: postman
  name: Google Cloud Storage JSON BucketAccessControls ObjectAccessControls API
  slug: postman-gcp-cloud-storage-objectaccesscontrols-api
- collection_type: postman
  name: Google Cloud Storage JSON BucketAccessControls Objects API
  slug: postman-gcp-cloud-storage-objects-api
- collection_type: open
  name: Google Cloud Storage JSON BucketAccessControls API
  slug: open-gcp-cloud-storage-bucketaccesscontrols-api
- collection_type: open
  name: Google Cloud Storage JSON BucketAccessControls Buckets API
  slug: open-gcp-cloud-storage-buckets-api
- collection_type: open
  name: Google Cloud Storage JSON BucketAccessControls DefaultObjectAccessControls API
  slug: open-gcp-cloud-storage-defaultobjectaccesscontrols-api
- collection_type: open
  name: Google Cloud Storage JSON API
  slug: open-gcp-cloud-storage-json-api
- collection_type: open
  name: Google Cloud Storage JSON BucketAccessControls ObjectAccessControls API
  slug: open-gcp-cloud-storage-objectaccesscontrols-api
- collection_type: open
  name: Google Cloud Storage JSON BucketAccessControls Objects API
  slug: open-gcp-cloud-storage-objects-api
common:
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/rules/gcp-cloud-storage-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/gcp-cloud-storage-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/rules/gcp-cloud-storage-rules.yml
  title: ''
  type: Spectral
  url: rules/gcp-cloud-storage-rules.yml
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/rules/gcp-cloud-storage-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/gcp-cloud-storage-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/vocabulary/gcp-cloud-storage-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gcp-cloud-storage-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gcp-cloud-storage/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/data-model/gcp-cloud-storage-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gcp-cloud-storage-data-model.yml
- group: build
  href: https://artifacts.apis.io/gcp-cloud-storage/cli/gcp-cloud-storage-cli.yml
  title: ''
  type: CLI
  url: cli/gcp-cloud-storage-cli.yml
- group: operate
  href: https://artifacts.apis.io/gcp-cloud-storage/changelog/gcp-cloud-storage-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gcp-cloud-storage-changelog.yml
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/conventions/gcp-cloud-storage-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/gcp-cloud-storage-conventions.yml
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/conventions/gcp-cloud-storage-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gcp-cloud-storage-conventions.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://cloud.google.com/terms/deprecation
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/lifecycle/gcp-cloud-storage-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gcp-cloud-storage-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/errors/gcp-cloud-storage-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/gcp-cloud-storage-error-codes.yml
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/errors/gcp-cloud-storage-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gcp-cloud-storage-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/conformance/gcp-cloud-storage-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gcp-cloud-storage-conformance.yml
- group: other
  href: https://artifacts.apis.io/gcp-cloud-storage/grpc/gcp-cloud-storage-storage-v2.proto
  title: ''
  type: Protobuf
  url: grpc/gcp-cloud-storage-storage-v2.proto
- group: agent
  href: https://artifacts.apis.io/gcp-cloud-storage/llms/gcp-cloud-storage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gcp-cloud-storage-llms.txt
- group: build
  href: https://artifacts.apis.io/gcp-cloud-storage/mcp/gcp-cloud-storage-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gcp-cloud-storage-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/gcp-cloud-storage/well-known/gcp-cloud-storage-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gcp-cloud-storage-security.txt
- group: agent
  href: https://artifacts.apis.io/gcp-cloud-storage/well-known/gcp-cloud-storage-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gcp-cloud-storage-well-known.yml
- group: other
  href: https://artifacts.apis.io/gcp-cloud-storage/hosts/gcp-cloud-storage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gcp-cloud-storage-hosts.yml
- group: build
  href: https://artifacts.apis.io/gcp-cloud-storage/integrations/gcp-cloud-storage-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/gcp-cloud-storage-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/gcp-cloud-storage/packages/gcp-cloud-storage-packages.yml
  title: ''
  type: Packages
  url: packages/gcp-cloud-storage-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: auth
  title: ''
  type: Security
  url: https://accounts.google.com/ServiceLogin?hl=en-US&continue=https://myaccount.google.com/intro/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy?hl=en&fg=1
- group: start
  title: ''
  type: Login
  url: https://accounts.google.com/v3/signin/identifier?continue=https://docs.google.com/&emr=1&followup=https://docs.google.com/&osid=1&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1862456855:1793821621877504
- group: agent
  href: https://artifacts.apis.io/gcp-cloud-storage/mcp/gcp-cloud-storage-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gcp-cloud-storage-mcp.yml
- group: commercial
  href: https://artifacts.apis.io/gcp-cloud-storage/finops/gcp-cloud-storage-finops.yml
  title: ''
  type: FinOps
  url: finops/gcp-cloud-storage-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/storage/pricing
- group: operate
  href: https://artifacts.apis.io/gcp-cloud-storage/rate-limits/gcp-cloud-storage-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gcp-cloud-storage-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gcp-cloud-storage/plans/gcp-cloud-storage-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gcp-cloud-storage-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: other
  href: https://artifacts.apis.io/gcp-cloud-storage/capabilities/gcp-cloud-storage-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gcp-cloud-storage-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-storage/overview
- group: agent
  href: https://artifacts.apis.io/gcp-cloud-storage/agentic-access/gcp-cloud-storage-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gcp-cloud-storage-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gcp-cloud-storage/security/gcp-cloud-storage-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gcp-cloud-storage-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gcp-cloud-storage/security/gcp-cloud-storage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gcp-cloud-storage-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gcp-cloud-storage/authentication/gcp-cloud-storage-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gcp-cloud-storage-authentication.yml
- group: auth
  href: https://artifacts.apis.io/gcp-cloud-storage/scopes/gcp-cloud-storage-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gcp-cloud-storage-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/storage/docs/quickstarts
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/storage/docs/reference/libraries
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/storage
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/storage-data-transfer
- group: operate
  title: ''
  type: ChangeLog
  url: https://cloud.google.com/storage/docs/release-notes
- group: other
  title: ''
  type: BestPractices
  url: https://cloud.google.com/storage/docs/best-practices
- group: auth
  title: ''
  type: Compliance
  url: https://cloud.google.com/security/compliance
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.google.com/storage/docs/apis
- group: build
  title: ''
  type: CLI
  url: https://cloud.google.com/storage/docs/discover-object-storage-gsutil
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/rules/gcp-cloud-storage-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/gcp-cloud-storage-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/gcp-cloud-storage/vocabulary/gcp-cloud-storage-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/gcp-cloud-storage-vocabulary.yaml
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/storage
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/storage/docs
created: '2024-01-01'
description: Object storage service offering high durability, availability, and scalability for storing and accessing data on Google Cloud Platform.
examples:
- key_count: 11
  name: Gcp Cloud Storage Json Bucket Access Control Example
  slug: gcp-cloud-storage-json-bucket-access-control-example
- key_count: 30
  name: Gcp Cloud Storage Json Bucket Example
  slug: gcp-cloud-storage-json-bucket-example
- key_count: 3
  name: Gcp Cloud Storage Json Bucket List Example
  slug: gcp-cloud-storage-json-bucket-list-example
- key_count: 10
  name: Gcp Cloud Storage Json Channel Example
  slug: gcp-cloud-storage-json-channel-example
- key_count: 2
  name: Gcp Cloud Storage Json Compose Request Example
  slug: gcp-cloud-storage-json-compose-request-example
- key_count: 1
  name: Gcp Cloud Storage Json Error Example
  slug: gcp-cloud-storage-json-error-example
- key_count: 13
  name: Gcp Cloud Storage Json Object Access Control Example
  slug: gcp-cloud-storage-json-object-access-control-example
- key_count: 34
  name: Gcp Cloud Storage Json Object Example
  slug: gcp-cloud-storage-json-object-example
- key_count: 4
  name: Gcp Cloud Storage Json Object List Example
  slug: gcp-cloud-storage-json-object-list-example
- key_count: 5
  name: Gcp Cloud Storage Json Policy Example
  slug: gcp-cloud-storage-json-policy-example
- key_count: 5
  name: Gcp Cloud Storage Json Rewrite Response Example
  slug: gcp-cloud-storage-json-rewrite-response-example
features:
- description: Store data across multiple regions for high availability and low-latency access worldwide.
  name: Multi-Regional Storage
- description: Automatically transition objects between storage classes or delete them based on configurable rules.
  name: Object Lifecycle Management
- description: Maintain multiple versions of objects for data protection and recovery.
  name: Versioning
- description: Control access using IAM policies, ACLs, and signed URLs for secure data sharing.
  name: Fine-Grained Access Control
- description: Compose multiple objects into a single object without downloading and re-uploading data.
  name: Object Composition
- description: Watch for changes to objects in a bucket and receive push notifications.
  name: Change Notifications
- description: Lock retention policies to prevent object deletion for regulatory compliance.
  name: Retention Policies
finops:
- has_sources: true
  method: derived
  name: Gcp Cloud Storage Finops
  primary_unit: gibibyte hour
  service_category: ''
  slug: gcp-cloud-storage-finops
  template: false
image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
json_schemas:
- name: AdvanceRelocateBucketOperationRequest
  property_count: 2
  slug: gcp-cloud-storage-advance-relocate-bucket-operation-request
- name: AnywhereCache
  property_count: 13
  slug: gcp-cloud-storage-anywhere-cache
- name: AnywhereCaches
  property_count: 3
  slug: gcp-cloud-storage-anywhere-caches
- name: Google Cloud Storage Bucket
  property_count: 30
  slug: gcp-cloud-storage-bucket
- name: Folder
  property_count: 9
  slug: gcp-cloud-storage-folder
- name: Folders
  property_count: 3
  slug: gcp-cloud-storage-folders
- name: GoogleLongrunningListOperationsResponse
  property_count: 3
  slug: gcp-cloud-storage-google-longrunning-list-operations-response
- name: GoogleLongrunningOperation
  property_count: 7
  slug: gcp-cloud-storage-google-longrunning-operation
- name: HmacKeyMetadata
  property_count: 10
  slug: gcp-cloud-storage-hmac-key-metadata
- name: HmacKey
  property_count: 3
  slug: gcp-cloud-storage-hmac-key
- name: HmacKeysMetadata
  property_count: 3
  slug: gcp-cloud-storage-hmac-keys-metadata
- name: BucketAccessControl
  property_count: 11
  slug: gcp-cloud-storage-json-bucket-access-control
- name: BucketList
  property_count: 3
  slug: gcp-cloud-storage-json-bucket-list
- name: Bucket
  property_count: 30
  slug: gcp-cloud-storage-json-bucket
- name: Channel
  property_count: 10
  slug: gcp-cloud-storage-json-channel
- name: ComposeRequest
  property_count: 2
  slug: gcp-cloud-storage-json-compose-request
- name: Error
  property_count: 1
  slug: gcp-cloud-storage-json-error
- name: ObjectAccessControl
  property_count: 13
  slug: gcp-cloud-storage-json-object-access-control
- name: ObjectList
  property_count: 4
  slug: gcp-cloud-storage-json-object-list
- name: Object
  property_count: 34
  slug: gcp-cloud-storage-json-object
- name: Policy
  property_count: 5
  slug: gcp-cloud-storage-json-policy
- name: RewriteResponse
  property_count: 5
  slug: gcp-cloud-storage-json-rewrite-response
- name: ManagedFolder
  property_count: 9
  slug: gcp-cloud-storage-managed-folder
- name: ManagedFolders
  property_count: 3
  slug: gcp-cloud-storage-managed-folders
- name: Notification
  property_count: 9
  slug: gcp-cloud-storage-notification
- name: Notifications
  property_count: 2
  slug: gcp-cloud-storage-notifications
- name: ObjectAccessControl
  property_count: 13
  slug: gcp-cloud-storage-object-access-control
- name: Object
  property_count: 38
  slug: gcp-cloud-storage-object
- name: Policy
  property_count: 5
  slug: gcp-cloud-storage-policy
- name: RapidCache
  property_count: 14
  slug: gcp-cloud-storage-rapid-cache
- name: RapidCaches
  property_count: 3
  slug: gcp-cloud-storage-rapid-caches
- name: ServiceAccount
  property_count: 2
  slug: gcp-cloud-storage-service-account
- name: TestIamPermissionsResponse
  property_count: 2
  slug: gcp-cloud-storage-test-iam-permissions-response
json_structures:
- name: Gcp Cloud Storage Json Bucket Access Control Structure
  property_count: 11
  slug: gcp-cloud-storage-json-bucket-access-control-structure
- name: Gcp Cloud Storage Json Bucket List Structure
  property_count: 3
  slug: gcp-cloud-storage-json-bucket-list-structure
- name: Gcp Cloud Storage Json Bucket Structure
  property_count: 30
  slug: gcp-cloud-storage-json-bucket-structure
- name: Gcp Cloud Storage Json Channel Structure
  property_count: 10
  slug: gcp-cloud-storage-json-channel-structure
- name: Gcp Cloud Storage Json Compose Request Structure
  property_count: 2
  slug: gcp-cloud-storage-json-compose-request-structure
- name: Gcp Cloud Storage Json Error Structure
  property_count: 1
  slug: gcp-cloud-storage-json-error-structure
- name: Gcp Cloud Storage Json Object Access Control Structure
  property_count: 13
  slug: gcp-cloud-storage-json-object-access-control-structure
- name: Gcp Cloud Storage Json Object List Structure
  property_count: 4
  slug: gcp-cloud-storage-json-object-list-structure
- name: Gcp Cloud Storage Json Object Structure
  property_count: 34
  slug: gcp-cloud-storage-json-object-structure
- name: Gcp Cloud Storage Json Policy Structure
  property_count: 5
  slug: gcp-cloud-storage-json-policy-structure
- name: Gcp Cloud Storage Json Rewrite Response Structure
  property_count: 5
  slug: gcp-cloud-storage-json-rewrite-response-structure
jsonld:
- class_count: 0
  name: Gcp Cloud Storage Context
  property_count: 6
  slug: gcp-cloud-storage-context
- class_count: 0
  name: Gcp Cloud Storage Json Context
  property_count: 0
  slug: gcp-cloud-storage-json-context
layout: provider
mcp_servers:
- description: Remote MCP server at storage.googleapis.com requiring OAuth; 10 tools listed.
  name: Cloud Storage MCP server
  slug: cloud-storage-mcp-server
modified: '2026-05-19'
name: Google Cloud Storage
nav: Providers
network: true
overview: 'Google Cloud Storage publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including BucketAccessControls API, Buckets API, DefaultObjectAccessControls API, and 10 more. Tagged areas include Archival, Backup, Blob Storage, Cloud Storage, and Data.


  The Google Cloud Storage catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  Google Cloud Storage''s developer surface includes CLI, changelog, pricing, authentication, getting-started guide, developer console, engineering blog, and 47 more developer resources.'
plans:
- name: Gcp Cloud Storage Plans Pricing
  plan_count: 23
  slug: gcp-cloud-storage-plans-pricing
- name: Gcp Cloud Storage Price Estimates
  plan_count: 0
  slug: gcp-cloud-storage-price-estimates
random_paper: 16
rate_limits:
- limit_count: 16
  name: Gcp Cloud Storage Rate Limits
  slug: gcp-cloud-storage-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Google Cloud Storage — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: gcp-cloud-storage-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: Google Cloud Storage API Rules
  rule_count: 69
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 7
  slug: gcp-cloud-storage-rules
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: Google Cloud Storage API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 10
  slug: gcp-cloud-storage-spectral-rules
scopes:
- name: Gcp Cloud Storage Scopes
  scope_count: 5
  slug: gcp-cloud-storage-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: exemplar
  composite: 71.7
  coverage:
    artifact_dirs: 41
    catalog_earned: 82.0
    catalog_earned_first_party: 24.0
    catalog_gap: 33.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.6
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 63.5
    developer_ergonomics: 69.6
    discoverability: 63.3
    operational_transparency: 73.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gcp-cloud-storage/gcp-cloud-storage-2026-06-20T181701.png
security:
- kind: authentication
  name: Gcp Cloud Storage Authentication
  slug: gcp-cloud-storage-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Gcp Cloud Storage Domain Security
  slug: gcp-cloud-storage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gcp Cloud Storage Vulnerability Disclosure
  slug: gcp-cloud-storage-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: recover-deleted-object
  slug: gcp-cloud-storage-recover-deleted-object
- name: upload-and-share-object
  slug: gcp-cloud-storage-upload-and-share-object
slug: gcp-cloud-storage
tags:
- Archival
- Backup
- Blob Storage
- Cloud Storage
- Data
- File Storage
- Google Cloud
- Object Storage
- Storage
use_cases:
- description: Store structured and unstructured data at scale for analytics and machine learning pipelines.
  name: Data Lake Storage
- description: Store backups with configurable retention and cross-region replication for business continuity.
  name: Backup and Disaster Recovery
- description: Serve static web content directly from Cloud Storage buckets with custom domains.
  name: Static Website Hosting
- description: Store and serve media assets with CDN integration for low-latency content delivery.
  name: Media Content Delivery
website: https://www.google.com/
---
