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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Amazon Datazone Agentic Access
  operation_count: 19
  slug: amazon-datazone-agentic-access
  summary_line: 19 operations · 10 acting
api_count: 6
apis:
- description: Operations for managing data assets in the catalog
  name: Amazon DataZone Assets API
  slug: amazon-datazone-assets-api
- description: Operations for managing DataZone domains
  name: Amazon DataZone Domains API
  slug: amazon-datazone-domains-api
- description: Operations for managing data environments
  name: Amazon DataZone Environments API
  slug: amazon-datazone-environments-api
- description: Operations for managing asset listings in the catalog
  name: Amazon DataZone Listings API
  slug: amazon-datazone-listings-api
- description: Operations for managing projects within a domain
  name: Amazon DataZone Projects API
  slug: amazon-datazone-projects-api
- description: Operations for managing data subscriptions
  name: Amazon DataZone Subscriptions API
  slug: amazon-datazone-subscriptions-api
arazzos:
- description: List pending subscription requests and active subscriptions to audit data access.
  name: Amazon DataZone Audit Domain Subscriptions
  slug: amazon-datazone-audit-domain-subscriptions-workflow
- description: Create a domain, wait for it to be AVAILABLE, then create a project inside it.
  name: Amazon DataZone Bootstrap Domain and Project
  slug: amazon-datazone-bootstrap-domain-and-project-workflow
- description: Create a data asset in a project and read it back to confirm cataloging.
  name: Amazon DataZone Catalog a Data Asset
  slug: amazon-datazone-catalog-asset-workflow
- description: Search catalog listings, then raise a subscription request for the first match.
  name: Amazon DataZone Discover and Subscribe
  slug: amazon-datazone-discover-and-subscribe-workflow
- description: Create a project, catalog an asset, and provision an environment in one workspace flow.
  name: Amazon DataZone Onboard Data Workspace
  slug: amazon-datazone-onboard-data-workspace-workflow
- description: Create a DataZone domain and poll until it becomes AVAILABLE.
  name: Amazon DataZone Provision Domain
  slug: amazon-datazone-provision-domain-workflow
- description: Create a project environment and poll the environment list until it is ACTIVE.
  name: Amazon DataZone Provision Environment
  slug: amazon-datazone-provision-environment-workflow
- description: Create a project, catalog an asset in it, then search the catalog for the listing.
  name: Amazon DataZone Publish Data Product
  slug: amazon-datazone-publish-data-product-workflow
- description: Read a project, update its description, then read it back to confirm the change.
  name: Amazon DataZone Rename Project
  slug: amazon-datazone-rename-project-workflow
- description: Create a subscription request, then poll the request list until it leaves PENDING.
  name: Amazon DataZone Request and Track Subscription
  slug: amazon-datazone-request-and-track-subscription-workflow
- description: List projects in a domain and branch to delete the domain only when it is empty.
  name: Amazon DataZone Teardown Domain
  slug: amazon-datazone-teardown-domain-workflow
- description: Confirm a project exists, delete it, then verify the delete via a 404 read-back.
  name: Amazon DataZone Teardown Project
  slug: amazon-datazone-teardown-project-workflow
artifact_total: 79
collections:
- collection_type: postman
  name: Amazon DataZone API
  slug: postman-amazon-datazone
- collection_type: open
  name: Amazon DataZone API
  slug: open-amazon-datazone
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-datazone-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-datazone-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-datazone-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-datazone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-datazone-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-datazone/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-datazone-audit-domain-subscriptions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-datazone-bootstrap-domain-and-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-datazone-catalog-asset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-datazone-discover-and-subscribe-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-datazone-onboard-data-workspace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-datazone-provision-domain-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-datazone-provision-environment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-datazone-publish-data-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-datazone-rename-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-datazone-request-and-track-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-datazone-teardown-domain-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-datazone-teardown-project-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/datazone/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/datazone/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/datazone/
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
  url: https://console.aws.amazon.com/datazone/
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
  url: rules/amazon-datazone-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-datazone-vocabulary.yaml
created: '2026-03-16'
description: Amazon DataZone is a data management service that helps you catalog, discover, govern, share, and analyze your data across your organization and beyond. It enables data producers and consumers to collaborate, with built-in governance, data catalog capabilities, and a business data catalog to organize and share data across your AWS environment. DataZone provides domain-based governance, project workspaces, subscription-based access control, and integration with AWS analytics services.
examples:
- key_count: 6
  name: Asset Example
  slug: asset-example
- key_count: 5
  name: Create Asset Request Example
  slug: create-asset-request-example
- key_count: 3
  name: Create Domain Request Example
  slug: create-domain-request-example
- key_count: 4
  name: Create Environment Request Example
  slug: create-environment-request-example
- key_count: 2
  name: Create Project Request Example
  slug: create-project-request-example
- key_count: 6
  name: Domain Example
  slug: domain-example
- key_count: 6
  name: Environment Example
  slug: environment-example
- key_count: 2
  name: Error Example
  slug: error-example
- key_count: 1
  name: List Domains Response Example
  slug: list-domains-response-example
- key_count: 1
  name: List Projects Response Example
  slug: list-projects-response-example
- key_count: 5
  name: Project Example
  slug: project-example
- key_count: 5
  name: Subscription Request Example
  slug: subscription-request-example
features:
- description: Central catalog where data producers publish assets and data consumers can discover, understand, and request access to data products.
  name: Business Data Catalog
- description: Organize data assets, users, and governance policies within domains that reflect your organizational structure and data ownership.
  name: Domain-Based Governance
- description: Built-in request/approval workflow for data consumers to request access to data assets with business justification and audit trail.
  name: Subscription Workflow
- description: Isolated project containers within domains where teams organize their data assets, environments, and members.
  name: Project Workspaces
- description: Automatically provision data access environments with Athena, Glue, Redshift, or other tools when subscriptions are approved.
  name: Analytics Environment Provisioning
- description: Automatically discover and import tables from AWS Glue Data Catalog into DataZone for cataloging and governance.
  name: Glue Data Catalog Integration
- description: Track data lineage across assets to understand data origins, transformations, and dependencies for trust and compliance.
  name: Data Lineage
finops:
- name: Amazon Datazone Finops
  service_category: API
  slug: amazon-datazone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-datazone.png
json_schemas:
- name: Asset
  property_count: 7
  slug: asset
- name: Create Asset Request
  property_count: 5
  slug: create-asset-request
- name: Create Domain Request
  property_count: 4
  slug: create-domain-request
- name: Create Environment Request
  property_count: 5
  slug: create-environment-request
- name: Create Project Request
  property_count: 2
  slug: create-project-request
- name: Domain
  property_count: 7
  slug: domain
- name: Environment
  property_count: 6
  slug: environment
- name: Error
  property_count: 2
  slug: error
- name: List Domains Response
  property_count: 2
  slug: list-domains-response
- name: List Projects Response
  property_count: 2
  slug: list-projects-response
- name: Project
  property_count: 5
  slug: project
- name: Subscription Request
  property_count: 5
  slug: subscription-request
json_structures:
- name: Asset Structure
  property_count: 0
  slug: asset-structure
- name: Create Asset Request Structure
  property_count: 0
  slug: create-asset-request-structure
- name: Create Domain Request Structure
  property_count: 0
  slug: create-domain-request-structure
- name: Create Environment Request Structure
  property_count: 0
  slug: create-environment-request-structure
- name: Create Project Request Structure
  property_count: 0
  slug: create-project-request-structure
- name: Domain Structure
  property_count: 0
  slug: domain-structure
- name: Environment Structure
  property_count: 0
  slug: environment-structure
- name: Error Structure
  property_count: 0
  slug: error-structure
- name: List Domains Response Structure
  property_count: 0
  slug: list-domains-response-structure
- name: List Projects Response Structure
  property_count: 0
  slug: list-projects-response-structure
- name: Project Structure
  property_count: 0
  slug: project-structure
- name: Subscription Request Structure
  property_count: 0
  slug: subscription-request-structure
jsonld:
- class_count: 0
  name: Amazon Datazone Context
  property_count: 26
  slug: amazon-datazone-context
layout: provider
modified: '2026-05-19'
name: Amazon DataZone
nav: Providers
network: true
overview: 'Amazon DataZone publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Domains API, Environments API, and 3 more. Tagged areas include Data Catalog, Data Governance, Data Management, Data Sharing, and Analytics.


  The Amazon DataZone catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon DataZone''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 26 more developer resources.'
plans:
- name: Amazon Datazone Plans Pricing
  plan_count: 3
  slug: amazon-datazone-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Amazon Datazone Rate Limits
  slug: amazon-datazone-rate-limits
rules:
- name: Amazon DataZone API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-datazone-jsonschema-spectral-rules
- name: Amazon DataZone API Rules
  rule_count: 26
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 10
  slug: amazon-datazone-spectral-rules
score:
  band: exemplar
  composite: 67.7
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 78.8
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 67.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-datazone/refs/heads/main/screenshots/amazon-datazone-2026-06-20T171616.png
security:
- kind: authentication
  name: Amazon Datazone Authentication
  slug: amazon-datazone-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Datazone Domain Security
  slug: amazon-datazone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Datazone Vulnerability Disclosure
  slug: amazon-datazone-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Datazone Trust Center
  slug: amazon-datazone-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-datazone
tags:
- Data Catalog
- Data Governance
- Data Management
- Data Sharing
- Analytics
use_cases:
- description: Build an internal data marketplace where business units publish their data products for discovery and consumption by other teams.
  name: Enterprise Data Marketplace
- description: Implement governed data access with approval workflows ensuring data consumers have proper authorization and business justification.
  name: Data Access Governance
- description: Share data assets across AWS accounts within an organization using DataZone's subscription and access management capabilities.
  name: Cross-Account Data Sharing
- description: Enable analysts to discover and access data independently through the DataZone catalog with automatic environment provisioning.
  name: Self-Service Analytics
- description: Maintain audit trails of data access, govern sensitive data assets, and enforce data residency policies through domain governance.
  name: Regulatory Data Compliance
website: https://aws.amazon.com/datazone/
---
