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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 26
  human_in_the_loop: 13
  name: Gcp Cloud Storage Agentic Access
  operation_count: 38
  slug: gcp-cloud-storage-agentic-access
  summary_line: 38 operations · 26 acting · 13 human-in-the-loop
api_count: 6
apis:
- description: Amazon S3-compatible XML API for Google Cloud Storage.
  name: Google Cloud Storage XML API
  slug: google-cloud-storage-xml-api
- description: Operations for managing bucket-level access control lists
  name: Google Cloud Storage BucketAccessControls API
  slug: gcp-cloud-storage-bucketaccesscontrols-api
- description: Operations for managing Cloud Storage buckets
  name: Google Cloud Storage Buckets API
  slug: gcp-cloud-storage-buckets-api
- description: Operations for managing default object access controls on buckets
  name: Google Cloud Storage DefaultObjectAccessControls API
  slug: gcp-cloud-storage-defaultobjectaccesscontrols-api
- description: Operations for managing object-level access control lists
  name: Google Cloud Storage ObjectAccessControls API
  slug: gcp-cloud-storage-objectaccesscontrols-api
- description: Operations for managing objects within Cloud Storage buckets
  name: Google Cloud Storage Objects API
  slug: gcp-cloud-storage-objects-api
artifact_total: 75
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
  name: API Collection
  slug: open-.refine-report
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-storage/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gcp-cloud-storage-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gcp-cloud-storage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gcp-cloud-storage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gcp-cloud-storage-authentication.yml
- group: auth
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
  type: Security
  url: https://cloud.google.com/storage/docs/security
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
  title: ''
  type: SpectralRules
  url: rules/gcp-cloud-storage-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/gcp-cloud-storage-vocabulary.yaml
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
- name: Gcp Cloud Storage Finops
  service_category: API
  slug: gcp-cloud-storage-finops
image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
json_schemas:
- name: Google Cloud Storage Bucket
  property_count: 30
  slug: gcp-cloud-storage-bucket
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
modified: '2026-05-19'
name: Google Cloud Storage
nav: Providers
network: true
overview: 'Google Cloud Storage publishes 5 APIs on the [APIs.io](https://apis.io/) network, including BucketAccessControls API, Buckets API, DefaultObjectAccessControls API, and 2 more. Tagged areas include Archival, Backup, Blob Storage, Cloud Storage, and Data.


  The Google Cloud Storage catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Google Cloud Storage''s developer surface includes authentication, getting-started guide, developer console, engineering blog, changelog, API reference, CLI, and 12 more developer resources.'
plans:
- name: Gcp Cloud Storage Plans Pricing
  plan_count: 3
  slug: gcp-cloud-storage-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Gcp Cloud Storage Rate Limits
  slug: gcp-cloud-storage-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Cloud Storage API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: gcp-cloud-storage-jsonschema-spectral-rules
- effective_rule_count: 60
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
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 28.8
    contract_quality: 73.8
    developer_ergonomics: 52.4
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gcp-cloud-storage/refs/heads/main/screenshots/gcp-cloud-storage-2026-06-20T181701.png
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
website: https://cloud.google.com/storage
---
