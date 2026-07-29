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
- acting_count: 1
  human_in_the_loop: 0
  name: Ariba Sourcing Agentic Access
  operation_count: 7
  slug: ariba-sourcing-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 3
apis:
- description: External approval task retrieval and action operations
  name: Ariba Sourcing Approval Tasks API
  slug: ariba-sourcing-approval-tasks-api
- description: Sourcing document and workspace retrieval
  name: Ariba Sourcing Documents API
  slug: ariba-sourcing-documents-api
- description: Approval group membership retrieval
  name: Ariba Sourcing Groups API
  slug: ariba-sourcing-groups-api
artifact_total: 67
collections:
- collection_type: postman
  name: Ariba Sourcing - External Approval Approval Tasks API
  slug: postman-ariba-sourcing-approval-tasks-api
- collection_type: postman
  name: Ariba Sourcing - External Approval Approval Tasks Documents API
  slug: postman-ariba-sourcing-documents-api
- collection_type: postman
  name: Ariba Sourcing - External Approval Approval Tasks Groups API
  slug: postman-ariba-sourcing-groups-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ariba-sourcing/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ariba-sourcing-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ariba-sourcing-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ariba-sourcing-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ariba-sourcing-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ariba-sourcing-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.ariba.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/ariba-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/sap-ariba-developer-portal-quick-start-guide-for-developers
- group: operate
  title: ''
  type: Support
  url: https://help.sap.com/ariba
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sap.com/corporate/en/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SAP-samples
- group: build
  title: SAP Ariba Extensibility Samples
  type: CodeExamples
  url: https://github.com/SAP-samples/ariba-extensibility-samples
- group: design
  title: ''
  type: SpectralRules
  url: rules/ariba-sourcing-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ariba-sourcing-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.ariba.com/llms.txt
created: '2024-01-01'
description: SAP Ariba Sourcing provides cloud-based strategic sourcing capabilities for procurement organizations. It enables supplier collaboration, RFx management, electronic auctions, and contract management through APIs that integrate sourcing processes with enterprise systems.
examples:
- key_count: 5
  name: External Approval Api Approvable Document Example
  slug: external-approval-api-approvable-document-example
- key_count: 4
  name: External Approval Api Approval Action Request Example
  slug: external-approval-api-approval-action-request-example
- key_count: 3
  name: External Approval Api Approval Action Response Example
  slug: external-approval-api-approval-action-response-example
- key_count: 6
  name: External Approval Api Approval Change Example
  slug: external-approval-api-approval-change-example
- key_count: 1
  name: External Approval Api Approval Changes Response Example
  slug: external-approval-api-approval-changes-response-example
- key_count: 1
  name: External Approval Api Approval Request Example
  slug: external-approval-api-approval-request-example
- key_count: 5
  name: External Approval Api Approval Task Example
  slug: external-approval-api-approval-task-example
- key_count: 2
  name: External Approval Api Approver Example
  slug: external-approval-api-approver-example
- key_count: 2
  name: External Approval Api Group Member Example
  slug: external-approval-api-group-member-example
- key_count: 2
  name: External Approval Api Group Members Response Example
  slug: external-approval-api-group-members-response-example
- key_count: 1
  name: External Approval Api Pending Approvables Response Example
  slug: external-approval-api-pending-approvables-response-example
- key_count: 6
  name: External Approval Api Pending Approval Task Example
  slug: external-approval-api-pending-approval-task-example
features:
- description: Enables external systems to retrieve, review, and approve or deny SAP Ariba sourcing approval tasks programmatically.
  name: External Approval Workflow
- description: Supports approval tasks for sourcing projects, RFX documents, contract workspaces, contract content, and supplier management projects.
  name: Multi-Document Type Support
- description: Well-defined rate limits of 20 req/sec, 400 req/min, 12000 req/hour, and 40000 req/day for production stability.
  name: Rate-Limited API Access
- description: Results pagination with offset and limit parameters plus X-Total-Count headers for efficient data retrieval.
  name: Pagination Support
- description: Supports approval flows with groups, enabling retrieval of group membership to identify eligible approvers.
  name: Group-Based Approval
- description: Enables downloading attachments associated with approvable documents for review prior to approval decisions.
  name: Attachment Downloads
finops:
- name: Ariba Sourcing Finops
  service_category: API
  slug: ariba-sourcing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ariba-sourcing.png
integrations:
- description: Route sourcing approval tasks to SAP ERP workflows and approval hierarchies.
  name: SAP ERP
- description: Orchestrate approval workflows across SAP Ariba and connected systems using SAP Integration Suite.
  name: SAP Integration Suite
- description: Approve contract workspaces and contract content documents through the external approval API.
  name: SAP Ariba Contracts
- description: Approve supplier lifecycle and performance management projects and supplier registration requests.
  name: SAP Ariba Supplier Management
json_schemas:
- name: ApprovableDocument
  property_count: 5
  slug: external-approval-api-approvable-document
- name: ApprovalActionRequest
  property_count: 4
  slug: external-approval-api-approval-action-request
- name: ApprovalActionResponse
  property_count: 3
  slug: external-approval-api-approval-action-response
- name: ApprovalChange
  property_count: 6
  slug: external-approval-api-approval-change
- name: ApprovalChangesResponse
  property_count: 1
  slug: external-approval-api-approval-changes-response
- name: ApprovalRequest
  property_count: 1
  slug: external-approval-api-approval-request
- name: ApprovalTask
  property_count: 5
  slug: external-approval-api-approval-task
- name: Approver
  property_count: 2
  slug: external-approval-api-approver
- name: GroupMember
  property_count: 2
  slug: external-approval-api-group-member
- name: GroupMembersResponse
  property_count: 2
  slug: external-approval-api-group-members-response
- name: PendingApprovablesResponse
  property_count: 1
  slug: external-approval-api-pending-approvables-response
- name: PendingApprovalTask
  property_count: 6
  slug: external-approval-api-pending-approval-task
json_structures:
- name: External Approval Api Approvable Document Structure
  property_count: 5
  slug: external-approval-api-approvable-document-structure
- name: External Approval Api Approval Action Request Structure
  property_count: 4
  slug: external-approval-api-approval-action-request-structure
- name: External Approval Api Approval Action Response Structure
  property_count: 3
  slug: external-approval-api-approval-action-response-structure
- name: External Approval Api Approval Change Structure
  property_count: 6
  slug: external-approval-api-approval-change-structure
- name: External Approval Api Approval Changes Response Structure
  property_count: 1
  slug: external-approval-api-approval-changes-response-structure
- name: External Approval Api Approval Request Structure
  property_count: 1
  slug: external-approval-api-approval-request-structure
- name: External Approval Api Approval Task Structure
  property_count: 5
  slug: external-approval-api-approval-task-structure
- name: External Approval Api Approver Structure
  property_count: 2
  slug: external-approval-api-approver-structure
- name: External Approval Api Group Member Structure
  property_count: 2
  slug: external-approval-api-group-member-structure
- name: External Approval Api Group Members Response Structure
  property_count: 2
  slug: external-approval-api-group-members-response-structure
- name: External Approval Api Pending Approvables Response Structure
  property_count: 1
  slug: external-approval-api-pending-approvables-response-structure
- name: External Approval Api Pending Approval Task Structure
  property_count: 6
  slug: external-approval-api-pending-approval-task-structure
jsonld:
- class_count: 13
  name: Ariba Sourcing External Approval Api Context
  property_count: 20
  slug: ariba-sourcing-external-approval-api-context
layout: provider
modified: '2026-05-19'
name: Ariba Sourcing
nav: Providers
network: true
overview: 'Ariba Sourcing publishes 3 APIs on the [APIs.io](https://apis.io/) network: Approval Tasks API, Documents API, and Groups API. Tagged areas include Approvals, Auctions, B2B, Contracts, and Procurement.


  The Ariba Sourcing catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ariba Sourcing''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, code examples, and 11 more developer resources.'
plans:
- name: Ariba Sourcing Plans Pricing
  plan_count: 3
  slug: ariba-sourcing-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Ariba Sourcing Rate Limits
  slug: ariba-sourcing-rate-limits
rules:
- name: Ariba Sourcing API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ariba-sourcing-jsonschema-spectral-rules
- name: Ariba Sourcing API Rules
  rule_count: 34
  severity_counts:
    error: 15
    hint: 0
    info: 5
    warn: 14
  slug: ariba-sourcing-spectral-rules
scopes:
- name: Ariba Sourcing Scopes
  scope_count: 0
  slug: ariba-sourcing-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.3
  delta: -6.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.6
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 66.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ariba-sourcing/refs/heads/main/screenshots/ariba-sourcing-2026-06-20T172427.png
security:
- kind: authentication
  name: Ariba Sourcing Authentication
  slug: ariba-sourcing-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ariba Sourcing Domain Security
  slug: ariba-sourcing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ariba Sourcing Vulnerability Disclosure
  slug: ariba-sourcing-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ariba-sourcing
tags:
- Approvals
- Auctions
- B2B
- Contracts
- Procurement
- RFx
- SAP
- Sourcing
- Supplier Management
- Supply Chain
use_cases:
- description: Automate the approval workflow for sourcing events and contracts by polling for pending tasks and submitting programmatic approval actions.
  name: Automated Sourcing Approvals
- description: Route SAP Ariba sourcing approval tasks to external ERP or workflow systems for approval by authorized personnel.
  name: ERP-Integrated Approvals
- description: Manage external approval of supplier registration and onboarding projects through the supplier management approval workflow.
  name: Supplier Onboarding Approval
- description: Integrate contract workspace approvals with enterprise contract management systems for streamlined legal and commercial review.
  name: Contract Approval Automation
website: https://developer.ariba.com
---
