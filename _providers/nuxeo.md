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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 58
  human_in_the_loop: 0
  name: Nuxeo Agentic Access
  operation_count: 139
  slug: nuxeo-agentic-access
  summary_line: 139 operations · 58 acting
api_count: 22
apis:
- description: The ACL API from Nuxeo — 2 operation(s) for acl.
  name: Nuxeo ACL API
  slug: nuxeo-acl-api
- description: Adaptation Endpoints
  name: Nuxeo Adapter API
  slug: nuxeo-adapter-api
- description: The Annotation API from Nuxeo — 2 operation(s) for annotation.
  name: Nuxeo Annotation API
  slug: nuxeo-annotation-api
- description: The Audit API from Nuxeo — 2 operation(s) for audit.
  name: Nuxeo Audit API
  slug: nuxeo-audit-api
- description: Automation Operations
  name: Nuxeo Automation API
  slug: nuxeo-automation-api
- description: The Blob API from Nuxeo — 2 operation(s) for blob.
  name: Nuxeo Blob API
  slug: nuxeo-blob-api
- description: Business Object Operations
  name: Nuxeo Business Object API
  slug: nuxeo-business-object-api
- description: The Children API from Nuxeo — 2 operation(s) for children.
  name: Nuxeo Children API
  slug: nuxeo-children-api
- description: Configuration Information
  name: Nuxeo Configuration API
  slug: nuxeo-configuration-api
- description: The Conversion API from Nuxeo — 4 operation(s) for conversion.
  name: Nuxeo Conversion API
  slug: nuxeo-conversion-api
- description: Directory Operations
  name: Nuxeo Directory API
  slug: nuxeo-directory-api
- description: Document Operations
  name: Nuxeo Document API
  slug: nuxeo-document-api
- description: The Empty Document API from Nuxeo — 3 operation(s) for empty document.
  name: Nuxeo Empty Document API
  slug: nuxeo-empty-document-api
- description: Group Operations
  name: Nuxeo Group API
  slug: nuxeo-group-api
- description: OAuth2 Operations
  name: Nuxeo OAuth2 API
  slug: nuxeo-oauth2-api
- description: The Rendition API from Nuxeo — 2 operation(s) for rendition.
  name: Nuxeo Rendition API
  slug: nuxeo-rendition-api
- description: Search Operations
  name: Nuxeo Search API
  slug: nuxeo-search-api
- description: The Task API from Nuxeo — 5 operation(s) for task.
  name: Nuxeo Task API
  slug: nuxeo-task-api
- description: Authentication Token Operations
  name: Nuxeo Token API
  slug: nuxeo-token-api
- description: User Operations
  name: Nuxeo User API
  slug: nuxeo-user-api
- description: Workflow Operations
  name: Nuxeo Workflow API
  slug: nuxeo-workflow-api
- description: Workflow Model Information
  name: Nuxeo Workflow Model API
  slug: nuxeo-workflow-model-api
artifact_total: 77
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nuxeo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuxeo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nuxeo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hyland.com/en/solutions/products/nuxeo-platform
- group: docs
  title: ''
  type: Documentation
  url: https://doc.nuxeo.com/nxdoc/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nuxeo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nuxeo
- group: company
  title: ''
  type: Blog
  url: https://connect.hyland.com/t5/nuxeo-blog/bg-p/nuxeo1blog-board
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hyland.com/en/resources/nuxeo-download
- group: operate
  title: ''
  type: StatusPage
  url: https://doc.nuxeo.com/nxdoc/health-check/
- group: other
  title: ''
  type: X
  url: https://x.com/nuxeo
- group: commercial
  title: ''
  type: Plans
  url: plans/nuxeo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nuxeo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nuxeo-finops.yml
created: '2026-06-13'
description: Nuxeo is an open-source, cloud-native enterprise content management platform owned by Hyland Software. It provides a comprehensive REST API for managing documents, digital assets, workflows, metadata, search, batch uploads, and cloud file storage in large-scale enterprise environments. The API supports OAuth2, token-based, and basic authentication, and exposes automation chains, content enrichers, and web adapters for flexible integration.
finops:
- name: Nuxeo Finops
  service_category: ''
  slug: nuxeo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuxeo.png
json_schemas:
- name: Ace
  property_count: 3
  slug: Ace
- name: Acl
  property_count: 2
  slug: Acl
- name: Acp
  property_count: 2
  slug: Acp
- name: AuthenticationTokenList
  property_count: 3
  slug: AuthenticationTokenList
- name: BusinessObject
  property_count: 2
  slug: BusinessObject
- name: BusinessObjectList
  property_count: 19
  slug: BusinessObjectList
- name: document
  property_count: 13
  slug: Document
- name: GroupRef
  property_count: 3
  slug: GroupRef
- name: LogEntries
  property_count: 19
  slug: LogEntries
- name: LogEntry
  property_count: 12
  slug: LogEntry
- name: OperationDescription
  property_count: 8
  slug: OperationDescription
- name: OperationDescriptionList
  property_count: 3
  slug: OperationDescriptionList
- name: OperationParamDescription
  property_count: 7
  slug: OperationParamDescription
- name: OperationParams
  property_count: 2
  slug: OperationParams
- name: Property
  property_count: 2
  slug: Property
- name: annotation
  property_count: 15
  slug: annotation
- name: annotationList
  property_count: 2
  slug: annotationList
- name: changePassword
  property_count: 2
  slug: changePassword
- name: directoryEntries
  property_count: 19
  slug: directoryEntries
- name: directoryEntry
  property_count: 3
  slug: directoryEntry
- name: docType
  property_count: 5
  slug: docType
- name: docTypes
  property_count: 2
  slug: docTypes
- name: documents
  property_count: 19
  slug: documents
- name: facet
  property_count: 2
  slug: facet
- name: group
  property_count: 3
  slug: group
- name: oauth2ClientData
  property_count: 7
  slug: oauth2ClientData
- name: oauth2ClientDataList
  property_count: 19
  slug: oauth2ClientDataList
- name: oauth2ProviderData
  property_count: 14
  slug: oauth2ProviderData
- name: oauth2ProviderDataList
  property_count: 19
  slug: oauth2ProviderDataList
- name: oauth2ProviderTokenData
  property_count: 1
  slug: oauth2ProviderTokenData
- name: oauth2TokenData
  property_count: 8
  slug: oauth2TokenData
- name: oauth2TokenDataList
  property_count: 19
  slug: oauth2TokenDataList
- name: savedsearch
  property_count: 13
  slug: savedsearch
- name: savedsearches
  property_count: 19
  slug: savedsearches
- name: schema
  property_count: 3
  slug: schema
- name: task
  property_count: 15
  slug: task
- name: taskAction
  property_count: 3
  slug: taskAction
- name: taskComments
  property_count: 2
  slug: taskComments
- name: taskCompletionRequest
  property_count: 4
  slug: taskCompletionRequest
- name: taskInfo
  property_count: 2
  slug: taskInfo
- name: tasks
  property_count: 2
  slug: tasks
- name: user
  property_count: 6
  slug: user
- name: userList
  property_count: 19
  slug: userList
- name: workflow
  property_count: 6
  slug: workflow
- name: workflowGraph
  property_count: 0
  slug: workflowGraph
- name: workflowRequest
  property_count: 4
  slug: workflowRequest
- name: workflows
  property_count: 2
  slug: workflows
jsonld:
- class_count: 0
  name: Nuxeo Rest Api Context
  property_count: 0
  slug: nuxeo-rest-api
layout: provider
modified: '2026-06-13'
name: Nuxeo
nav: Providers
network: true
overview: 'Nuxeo publishes 22 APIs on the [APIs.io](https://apis.io/) network, including ACL API, Adapter API, Annotation API, and 19 more. Tagged areas include Content Management, Digital Asset Management, Enterprise, Documents, and Workflows.


  The Nuxeo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nuxeo''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Nuxeo Plans Pricing
  plan_count: 2
  slug: nuxeo-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Nuxeo Rate Limits
  slug: nuxeo-rate-limits
rules:
- name: Nuxeo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nuxeo-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.0
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 47.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuxeo/refs/heads/main/screenshots/nuxeo-2026-06-20T190538.png
security:
- kind: authentication
  name: Nuxeo Authentication
  slug: nuxeo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Nuxeo Domain Security
  slug: nuxeo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: nuxeo
tags:
- Content Management
- Digital Asset Management
- Enterprise
- Documents
- Workflows
- Search
- Open Source
website: https://www.hyland.com/en/solutions/products/nuxeo-platform
---
