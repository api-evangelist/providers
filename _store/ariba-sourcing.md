---
aid: ariba-sourcing
name: Ariba Sourcing
description: SAP Ariba Sourcing provides cloud-based strategic sourcing capabilities for procurement organizations. It enables supplier collaboration, RFx management, electronic auctions, and contract management through APIs that integrate sourcing processes with enterprise systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
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
url: https://raw.githubusercontent.com/api-evangelist/ariba-sourcing/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: ariba-sourcing:ariba-sourcing-external-approval-api
    name: Ariba Sourcing - External Approval API
    description: The External Approval API for Sourcing and Supplier Management enables client applications to approve or deny SAP Ariba strategic sourcing approval tasks. It supports external approval tasks in sourcing projects, contract workspaces, engagement risk assessment, and all types of supplier management projects.
    humanURL: https://help.sap.com/docs/ariba-apis
    baseURL: https://openapi.ariba.com/api/sourcing-approval/v2/prod
    tags:
      - Approvals
      - Contracts
      - RFx
      - Sourcing
      - Supplier Management
    properties:
      - type: Documentation
        url: https://help.sap.com/doc/69824194c55e4393870c5d3587aaf821/cloud/en-US/abdf297f281243ed9f8f3ead706a74d3.pdf
      - type: OpenAPI
        url: openapi/ariba-sourcing-external-approval-api.yaml
      - type: JSONSchema
        url: json-schema/external-approval-api-approval-task-schema.json
      - type: JSONSchema
        url: json-schema/external-approval-api-approvable-document-schema.json
      - type: JSONSchema
        url: json-schema/external-approval-api-approval-changes-response-schema.json
      - type: JSONStructure
        url: json-structure/external-approval-api-approval-task-structure.json
      - type: JSONStructure
        url: json-structure/external-approval-api-approvable-document-structure.json
      - type: JSON-LD
        url: json-ld/ariba-sourcing-external-approval-api-context.jsonld
common:
  - type: Portal
    url: https://developer.ariba.com
  - type: Documentation
    url: https://help.sap.com/docs/ariba-apis
  - type: GettingStarted
    url: https://help.sap.com/docs/ariba-apis/help-for-sap-ariba-developer-portal/sap-ariba-developer-portal-quick-start-guide-for-developers
  - type: Support
    url: https://help.sap.com/ariba
  - type: TermsOfService
    url: https://www.sap.com/corporate/en/legal/terms-of-use.html
  - type: PrivacyPolicy
    url: https://www.sap.com/about/legal/privacy.html
  - type: GitHubOrganization
    url: https://github.com/SAP-samples
  - type: CodeExamples
    url: https://github.com/SAP-samples/ariba-extensibility-samples
    title: SAP Ariba Extensibility Samples
  - type: SpectralRules
    url: rules/ariba-sourcing-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/sourcing-approvals.yaml
  - type: Vocabulary
    url: vocabulary/ariba-sourcing-vocabulary.yaml
  - type: Features
    data:
      - name: External Approval Workflow
        description: Enables external systems to retrieve, review, and approve or deny SAP Ariba sourcing approval tasks programmatically.
      - name: Multi-Document Type Support
        description: Supports approval tasks for sourcing projects, RFX documents, contract workspaces, contract content, and supplier management projects.
      - name: Rate-Limited API Access
        description: Well-defined rate limits of 20 req/sec, 400 req/min, 12000 req/hour, and 40000 req/day for production stability.
      - name: Pagination Support
        description: Results pagination with offset and limit parameters plus X-Total-Count headers for efficient data retrieval.
      - name: Group-Based Approval
        description: Supports approval flows with groups, enabling retrieval of group membership to identify eligible approvers.
      - name: Attachment Downloads
        description: Enables downloading attachments associated with approvable documents for review prior to approval decisions.
  - type: UseCases
    data:
      - name: Automated Sourcing Approvals
        description: Automate the approval workflow for sourcing events and contracts by polling for pending tasks and submitting programmatic approval actions.
      - name: ERP-Integrated Approvals
        description: Route SAP Ariba sourcing approval tasks to external ERP or workflow systems for approval by authorized personnel.
      - name: Supplier Onboarding Approval
        description: Manage external approval of supplier registration and onboarding projects through the supplier management approval workflow.
      - name: Contract Approval Automation
        description: Integrate contract workspace approvals with enterprise contract management systems for streamlined legal and commercial review.
  - type: Integrations
    data:
      - name: SAP ERP
        description: Route sourcing approval tasks to SAP ERP workflows and approval hierarchies.
      - name: SAP Integration Suite
        description: Orchestrate approval workflows across SAP Ariba and connected systems using SAP Integration Suite.
      - name: SAP Ariba Contracts
        description: Approve contract workspaces and contract content documents through the external approval API.
      - name: SAP Ariba Supplier Management
        description: Approve supplier lifecycle and performance management projects and supplier registration requests.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
