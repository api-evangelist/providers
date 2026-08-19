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
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Amazon Data Exchange Agentic Access
  operation_count: 27
  slug: amazon-data-exchange-agentic-access
  summary_line: 27 operations · 16 acting
api_count: 6
apis:
- description: Operations for managing data assets within revisions
  name: Amazon Data Exchange Assets API
  slug: amazon-data-exchange-assets-api
- description: Operations for managing data sets
  name: Amazon Data Exchange Data Sets API
  slug: amazon-data-exchange-data-sets-api
- description: Operations for managing event-driven actions
  name: Amazon Data Exchange Event Actions API
  slug: amazon-data-exchange-event-actions-api
- description: Operations for import/export jobs
  name: Amazon Data Exchange Jobs API
  slug: amazon-data-exchange-jobs-api
- description: Operations for managing data set revisions
  name: Amazon Data Exchange Revisions API
  slug: amazon-data-exchange-revisions-api
- description: Operations for managing resource tags
  name: Amazon Data Exchange Tags API
  slug: amazon-data-exchange-tags-api
arazzos:
- description: Register a RevisionPublished event action, then create and finalize a revision to trigger it.
  name: Amazon Data Exchange Auto Export On Publish
  slug: amazon-data-exchange-auto-export-on-publish-workflow
- description: List owned data sets, inspect the first one, and list its revisions.
  name: Amazon Data Exchange Browse Data Set Revisions
  slug: amazon-data-exchange-browse-data-set-revisions-workflow
- description: Find an in-flight job for a data set and cancel it if it is still running.
  name: Amazon Data Exchange Cancel Running Job
  slug: amazon-data-exchange-cancel-running-job-workflow
- description: Find a revision, confirm it is not finalized, and delete it as a draft.
  name: Amazon Data Exchange Delete Draft Revision
  slug: amazon-data-exchange-delete-draft-revision-workflow
- description: Discover an entitled data set, pick its latest revision, and export it to S3.
  name: Amazon Data Exchange Export Entitled Data
  slug: amazon-data-exchange-export-entitled-data-workflow
- description: Export all assets of a revision to an S3 bucket by creating, starting, and polling a job.
  name: Amazon Data Exchange Export Revision To S3
  slug: amazon-data-exchange-export-revision-to-s3-workflow
- description: Open a revision, import a single asset from a signed URL, wait, and list the result.
  name: Amazon Data Exchange Import Asset From Signed URL
  slug: amazon-data-exchange-import-asset-from-signed-url-workflow
- description: List the assets in a revision and fetch the details of the first asset.
  name: Amazon Data Exchange Inspect Revision Assets
  slug: amazon-data-exchange-inspect-revision-assets-workflow
- description: Create a data set, add a revision, import assets from S3, and finalize it for publishing.
  name: Amazon Data Exchange Publish Data Set
  slug: amazon-data-exchange-publish-data-set-workflow
- description: Locate an asset in a revision and rename it to a new asset name.
  name: Amazon Data Exchange Rename Revision Asset
  slug: amazon-data-exchange-rename-revision-asset-workflow
- description: Create a data set, apply governance tags to it, and read the tags back.
  name: Amazon Data Exchange Tag New Data Set
  slug: amazon-data-exchange-tag-new-data-set-workflow
- description: Read a resource's tags and remove a chosen set of tag keys from it.
  name: Amazon Data Exchange Untag Resource
  slug: amazon-data-exchange-untag-resource-workflow
- description: Read a data set, update its name and description, and verify the change.
  name: Amazon Data Exchange Update Data Set Metadata
  slug: amazon-data-exchange-update-data-set-metadata-workflow
- description: Find an existing event action, repoint its export destination, and verify the change.
  name: Amazon Data Exchange Update Event Action Destination
  slug: amazon-data-exchange-update-event-action-destination-workflow
artifact_total: 118
collections:
- collection_type: postman
  name: AWS Data Exchange API
  slug: postman-amazon-data-exchange
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Data Exchange Assets API
  slug: open-amazon-data-exchange-assets-api
- collection_type: open
  name: AWS Data Exchange Assets Data Sets API
  slug: open-amazon-data-exchange-data-sets-api
- collection_type: open
  name: AWS Data Exchange Assets Event Actions API
  slug: open-amazon-data-exchange-event-actions-api
- collection_type: open
  name: AWS Data Exchange Assets Jobs API
  slug: open-amazon-data-exchange-jobs-api
- collection_type: open
  name: AWS Data Exchange Assets Revisions API
  slug: open-amazon-data-exchange-revisions-api
- collection_type: open
  name: AWS Data Exchange Assets Tags API
  slug: open-amazon-data-exchange-tags-api
- collection_type: open
  name: AWS Data Exchange API
  slug: open-amazon-data-exchange
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-data-exchange-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-data-exchange-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-data-exchange-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-data-exchange-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-data-exchange-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-data-exchange/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-auto-export-on-publish-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-browse-data-set-revisions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-cancel-running-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-delete-draft-revision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-export-entitled-data-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-export-revision-to-s3-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-import-asset-from-signed-url-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-inspect-revision-assets-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-publish-data-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-rename-revision-asset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-tag-new-data-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-untag-resource-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-update-data-set-metadata-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-data-exchange-update-event-action-destination-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/data-exchange/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/data-exchange/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/data-exchange/
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
  url: https://aws.amazon.com/blogs/big-data/category/analytics/aws-data-exchange/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/dataexchange/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-data-exchange-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-data-exchange-vocabulary.yaml
created: '2026-03-16'
description: AWS Data Exchange makes it easy to find, subscribe to, and use third-party data in the cloud. Qualified data providers can publish data products consisting of data sets with versioned revisions and assets including S3 snapshots, Redshift data shares, API Gateway APIs, and Lake Formation permissions. Subscribers can find and subscribe to data products directly in the AWS Management Console and use the Data Exchange API to load data into Amazon S3 for analysis with AWS analytics and machine learning services.
examples:
- key_count: 6
  name: Asset Example
  slug: asset-example
- key_count: 4
  name: Create Data Set Request Example
  slug: create-data-set-request-example
- key_count: 2
  name: Create Event Action Request Example
  slug: create-event-action-request-example
- key_count: 2
  name: Create Job Request Example
  slug: create-job-request-example
- key_count: 2
  name: Create Revision Request Example
  slug: create-revision-request-example
- key_count: 8
  name: Data Set Example
  slug: data-set-example
- key_count: 3
  name: Error Example
  slug: error-example
- key_count: 4
  name: Event Action Example
  slug: event-action-example
- key_count: 6
  name: Job Example
  slug: job-example
- key_count: 1
  name: List Data Set Revisions Response Example
  slug: list-data-set-revisions-response-example
- key_count: 1
  name: List Data Sets Response Example
  slug: list-data-sets-response-example
- key_count: 1
  name: List Event Actions Response Example
  slug: list-event-actions-response-example
- key_count: 1
  name: List Jobs Response Example
  slug: list-jobs-response-example
- key_count: 1
  name: List Revision Assets Response Example
  slug: list-revision-assets-response-example
- key_count: 1
  name: List Tags Response Example
  slug: list-tags-response-example
- key_count: 7
  name: Revision Example
  slug: revision-example
- key_count: 2
  name: Start Job Response Example
  slug: start-job-response-example
- key_count: 1
  name: Tag Resource Request Example
  slug: tag-resource-request-example
- key_count: 1
  name: Update Asset Request Example
  slug: update-asset-request-example
- key_count: 2
  name: Update Data Set Request Example
  slug: update-data-set-request-example
- key_count: 1
  name: Update Event Action Request Example
  slug: update-event-action-request-example
- key_count: 2
  name: Update Revision Request Example
  slug: update-revision-request-example
features:
- description: Create, update, and manage data sets containing versioned collections of data available for subscription and distribution in the marketplace.
  name: Data Set Management
- description: Organize data into versioned revisions with comments, then finalize and publish them to make data available to subscribers automatically.
  name: Revision Publishing
- description: Support for S3 snapshots, Redshift data shares, API Gateway APIs, Lake Formation permissions, and S3 data access as asset types.
  name: Multi-Format Asset Support
- description: Asynchronous import/export jobs for transferring data between external sources (S3, Redshift) and Data Exchange revisions at scale.
  name: Import and Export Jobs
- description: Configurable event actions that automatically export revision data to S3 when a new revision is published, eliminating manual downloads.
  name: Event-Driven Delivery
- description: Seamlessly list and sell data products in AWS Marketplace with built-in billing, subscription management, and entitlement enforcement.
  name: AWS Marketplace Integration
- description: Control access to data products using AWS IAM policies and resource- level permissions with ARN-based resource identification.
  name: Fine-Grained Access Control
finops:
- name: Amazon Data Exchange Finops
  service_category: API
  slug: amazon-data-exchange-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-data-exchange.png
json_schemas:
- name: Asset
  property_count: 9
  slug: asset
- name: Create Data Set Request
  property_count: 4
  slug: create-data-set-request
- name: Create Event Action Request
  property_count: 2
  slug: create-event-action-request
- name: Create Job Request
  property_count: 2
  slug: create-job-request
- name: Create Revision Request
  property_count: 2
  slug: create-revision-request
- name: Data Set
  property_count: 9
  slug: data-set
- name: Error
  property_count: 3
  slug: error
- name: Event Action
  property_count: 6
  slug: event-action
- name: Job
  property_count: 8
  slug: job
- name: List Data Set Revisions Response
  property_count: 2
  slug: list-data-set-revisions-response
- name: List Data Sets Response
  property_count: 2
  slug: list-data-sets-response
- name: List Event Actions Response
  property_count: 2
  slug: list-event-actions-response
- name: List Jobs Response
  property_count: 2
  slug: list-jobs-response
- name: List Revision Assets Response
  property_count: 2
  slug: list-revision-assets-response
- name: List Tags Response
  property_count: 1
  slug: list-tags-response
- name: Revision
  property_count: 8
  slug: revision
- name: Start Job Response
  property_count: 2
  slug: start-job-response
- name: Tag Resource Request
  property_count: 1
  slug: tag-resource-request
- name: Update Asset Request
  property_count: 1
  slug: update-asset-request
- name: Update Data Set Request
  property_count: 2
  slug: update-data-set-request
- name: Update Event Action Request
  property_count: 1
  slug: update-event-action-request
- name: Update Revision Request
  property_count: 2
  slug: update-revision-request
json_structures:
- name: Asset Structure
  property_count: 0
  slug: asset-structure
- name: Create Data Set Request Structure
  property_count: 0
  slug: create-data-set-request-structure
- name: Create Event Action Request Structure
  property_count: 0
  slug: create-event-action-request-structure
- name: Create Job Request Structure
  property_count: 0
  slug: create-job-request-structure
- name: Create Revision Request Structure
  property_count: 0
  slug: create-revision-request-structure
- name: Data Set Structure
  property_count: 0
  slug: data-set-structure
- name: Error Structure
  property_count: 0
  slug: error-structure
- name: Event Action Structure
  property_count: 0
  slug: event-action-structure
- name: Job Structure
  property_count: 0
  slug: job-structure
- name: List Data Set Revisions Response Structure
  property_count: 0
  slug: list-data-set-revisions-response-structure
- name: List Data Sets Response Structure
  property_count: 0
  slug: list-data-sets-response-structure
- name: List Event Actions Response Structure
  property_count: 0
  slug: list-event-actions-response-structure
- name: List Jobs Response Structure
  property_count: 0
  slug: list-jobs-response-structure
- name: List Revision Assets Response Structure
  property_count: 0
  slug: list-revision-assets-response-structure
- name: List Tags Response Structure
  property_count: 0
  slug: list-tags-response-structure
- name: Revision Structure
  property_count: 0
  slug: revision-structure
- name: Start Job Response Structure
  property_count: 0
  slug: start-job-response-structure
- name: Tag Resource Request Structure
  property_count: 0
  slug: tag-resource-request-structure
- name: Update Asset Request Structure
  property_count: 0
  slug: update-asset-request-structure
- name: Update Data Set Request Structure
  property_count: 0
  slug: update-data-set-request-structure
- name: Update Event Action Request Structure
  property_count: 0
  slug: update-event-action-request-structure
- name: Update Revision Request Structure
  property_count: 0
  slug: update-revision-request-structure
jsonld:
- class_count: 0
  name: Amazon Data Exchange Context
  property_count: 49
  slug: amazon-data-exchange-context
layout: provider
modified: '2026-05-19'
name: Amazon Data Exchange
nav: Providers
network: true
overview: 'Amazon Data Exchange publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Data Sets API, Event Actions API, and 3 more. Tagged areas include Data Exchange, Data Marketplace, Third-Party Data, Analytics, and Subscriptions.


  The Amazon Data Exchange catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Data Exchange''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 28 more developer resources.'
plans:
- name: Amazon Data Exchange Plans Pricing
  plan_count: 3
  slug: amazon-data-exchange-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Amazon Data Exchange Rate Limits
  slug: amazon-data-exchange-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Data Exchange API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-data-exchange-jsonschema-spectral-rules
- effective_rule_count: 77
  extends:
  - spectral:oas
  name: Amazon Data Exchange API Rules
  rule_count: 36
  severity_counts:
    error: 13
    hint: 0
    info: 7
    warn: 16
  slug: amazon-data-exchange-spectral-rules
score:
  band: developing
  composite: 53.6
  delta: -6.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 25.0
    contract_quality: 77.9
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-data-exchange/refs/heads/main/screenshots/amazon-data-exchange-2026-06-20T171621.png
security:
- kind: authentication
  name: Amazon Data Exchange Authentication
  slug: amazon-data-exchange-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Data Exchange Domain Security
  slug: amazon-data-exchange-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Data Exchange Vulnerability Disclosure
  slug: amazon-data-exchange-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Data Exchange Trust Center
  slug: amazon-data-exchange-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-data-exchange
tags:
- Data Exchange
- Data Marketplace
- Third-Party Data
- Analytics
- Subscriptions
use_cases:
- description: Subscribe to curated third-party datasets from financial data providers, healthcare data aggregators, weather services, and market research firms.
  name: Third-Party Data Acquisition
- description: Publish and sell proprietary datasets to other AWS customers via the marketplace with automated billing and subscription management.
  name: Data Product Monetization
- description: Configure event actions to automatically deliver new data revisions to S3, enabling downstream analytics pipelines to process fresh data.
  name: Automated Data Pipelines
- description: Access high-quality labeled datasets and specialized data products from Data Exchange to train and improve machine learning models.
  name: ML Training Data
- description: Subscribe to compliance reference data including sanctions lists, legal entity identifiers, and regulatory taxonomies via Data Exchange.
  name: Regulatory Compliance Data
website: https://aws.amazon.com/data-exchange/
---
