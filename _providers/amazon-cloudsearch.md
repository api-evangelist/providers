---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Amazon Cloudsearch Agentic Access
  operation_count: 6
  slug: amazon-cloudsearch-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 2
apis:
- description: Operations for creating and managing search domains
  name: Amazon CloudSearch Domains API
  slug: amazon-cloudsearch-domains-api
- description: Operations for defining and managing index fields
  name: Amazon CloudSearch Index Fields API
  slug: amazon-cloudsearch-index-fields-api
artifact_total: 51
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-cloudsearch-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-cloudsearch-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-cloudsearch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-cloudsearch-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/cloudsearch/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/what-is-cloudsearch.html
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
  url: https://aws.amazon.com/blogs/compute/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudsearch/
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
  url: https://stackoverflow.com/questions/tagged/amazon-cloudsearch
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: build
  title: ''
  type: Packages
  url: packages/amazon-cloudsearch-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-cloudsearch-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-cloudsearch-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-cloudsearch-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-cloudsearch-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-cloudsearch-lifecycle.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-cloudsearch-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudsearch-vocabulary.yaml
created: '2024-01-15'
description: Amazon CloudSearch is a managed search service that makes it easy to set up, manage, and scale a search solution for your website or application. Supports full-text search, Boolean search, faceted search, autocomplete, geospatial search, and 34 languages.
examples:
- key_count: 1
  name: Cloudsearch Create Domain Request Example
  slug: cloudsearch-create-domain-request-example
- key_count: 1
  name: Cloudsearch Create Domain Response Example
  slug: cloudsearch-create-domain-response-example
- key_count: 1
  name: Cloudsearch Define Index Field Request Example
  slug: cloudsearch-define-index-field-request-example
- key_count: 1
  name: Cloudsearch Define Index Field Response Example
  slug: cloudsearch-define-index-field-response-example
- key_count: 1
  name: Cloudsearch Delete Domain Response Example
  slug: cloudsearch-delete-domain-response-example
- key_count: 1
  name: Cloudsearch Describe Domains Response Example
  slug: cloudsearch-describe-domains-response-example
- key_count: 1
  name: Cloudsearch Describe Index Fields Response Example
  slug: cloudsearch-describe-index-fields-response-example
- key_count: 11
  name: Cloudsearch Domain Status Example
  slug: cloudsearch-domain-status-example
- key_count: 1
  name: Cloudsearch Index Documents Response Example
  slug: cloudsearch-index-documents-response-example
features:
- description: Set up, manage, and scale search without becoming a search expert.
  name: Managed Search Infrastructure
- description: Full-text search across 34 languages with language-specific analyzers.
  name: Multi-Language Support
- description: Narrow search results by category with faceted navigation.
  name: Faceted Search
- description: Real-time search suggestions as users type.
  name: Autocomplete Suggestions
- description: Automatically scale resources as data volume and query traffic change.
  name: Automatic Scaling
- description: Distribute search traffic across multiple availability zones with Multi-AZ.
  name: High Availability
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Index documents stored in S3 buckets.
  name: Amazon S3
- description: Search DynamoDB data by exporting to CloudSearch.
  name: Amazon DynamoDB
- description: Control access to search domains with IAM policies.
  name: AWS IAM
- description: Cache search results at CloudFront edge for lower latency.
  name: Amazon CloudFront
json_schemas:
- name: Amazon CloudSearch Domain
  property_count: 11
  slug: amazon-cloudsearch-domain
- name: CreateDomainRequest
  property_count: 1
  slug: cloudsearch-create-domain-request
- name: CreateDomainResponse
  property_count: 1
  slug: cloudsearch-create-domain-response
- name: DefineIndexFieldRequest
  property_count: 1
  slug: cloudsearch-define-index-field-request
- name: DefineIndexFieldResponse
  property_count: 1
  slug: cloudsearch-define-index-field-response
- name: DeleteDomainResponse
  property_count: 1
  slug: cloudsearch-delete-domain-response
- name: DescribeDomainsResponse
  property_count: 1
  slug: cloudsearch-describe-domains-response
- name: DescribeIndexFieldsResponse
  property_count: 1
  slug: cloudsearch-describe-index-fields-response
- name: DomainStatus
  property_count: 11
  slug: cloudsearch-domain-status
- name: IndexDocumentsResponse
  property_count: 1
  slug: cloudsearch-index-documents-response
json_structures:
- name: Cloudsearch Create Domain Request Structure
  property_count: 1
  slug: cloudsearch-create-domain-request-structure
- name: Cloudsearch Create Domain Response Structure
  property_count: 1
  slug: cloudsearch-create-domain-response-structure
- name: Cloudsearch Define Index Field Request Structure
  property_count: 1
  slug: cloudsearch-define-index-field-request-structure
- name: Cloudsearch Define Index Field Response Structure
  property_count: 1
  slug: cloudsearch-define-index-field-response-structure
- name: Cloudsearch Delete Domain Response Structure
  property_count: 1
  slug: cloudsearch-delete-domain-response-structure
- name: Cloudsearch Describe Domains Response Structure
  property_count: 1
  slug: cloudsearch-describe-domains-response-structure
- name: Cloudsearch Describe Index Fields Response Structure
  property_count: 1
  slug: cloudsearch-describe-index-fields-response-structure
- name: Cloudsearch Domain Status Structure
  property_count: 11
  slug: cloudsearch-domain-status-structure
- name: Cloudsearch Index Documents Response Structure
  property_count: 1
  slug: cloudsearch-index-documents-response-structure
jsonld:
- class_count: 9
  name: Amazon Cloudsearch Context
  property_count: 16
  slug: amazon-cloudsearch-context
layout: provider
modified: '2026-06-20'
name: Amazon CloudSearch
nav: Providers
network: true
overview: 'Amazon CloudSearch publishes 2 APIs on the [APIs.io](https://apis.io/) network: Domains API and Index Fields API. Tagged areas include CloudSearch, Search, Full-Text Search, and Managed.


  The Amazon CloudSearch catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon CloudSearch''s developer surface includes developer portal, documentation, support, engineering blog, developer console, signup flow, YouTube channel, and 20 more developer resources.'
random_paper: 20
rules:
- name: Amazon CloudSearch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-cloudsearch-jsonschema-spectral-rules
- name: Amazon CloudSearch API Rules
  rule_count: 24
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 10
  slug: amazon-cloudsearch-spectral-rules
score:
  band: developing
  composite: 55.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 72.6
    developer_ergonomics: 30.4
    discoverability: 80.0
    governance: 86.8
    operational_transparency: 21.1
  previous_composite: 55.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-cloudsearch/refs/heads/main/screenshots/amazon-cloudsearch-2026-07-25T195949.png
security:
- kind: domain-security
  name: Amazon Cloudsearch Domain Security
  slug: amazon-cloudsearch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Cloudsearch Vulnerability Disclosure
  slug: amazon-cloudsearch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Cloudsearch Trust Center
  slug: amazon-cloudsearch-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-cloudsearch
tags:
- CloudSearch
- Search
- Full-Text Search
- Managed
use_cases:
- description: Add powerful full-text search capabilities to websites and web applications.
  name: Website Search
- description: Enable customers to find products with faceted filtering and relevance ranking.
  name: E-Commerce Product Search
- description: Search across large document repositories with Boolean and proximity search.
  name: Document Search
- description: Find resources by location with geospatial search queries.
  name: Geospatial Search
website: https://aws.amazon.com/cloudsearch/
---
