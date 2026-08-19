---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 106
  human_in_the_loop: 1
  name: Spotdraft Agentic Access
  operation_count: 182
  slug: spotdraft-agentic-access
  summary_line: 182 operations · 106 acting · 1 human-in-the-loop
api_count: 48
apis:
- description: Contract creation, retrieval, updates, previews, downloads, uploads, and lifecycle actions across public API versions.
  name: SpotDraft V1 Contract APIs API
  slug: spotdraft-v1-contract-apis-api
- description: Render stored public email audit HTML for preview and troubleshooting.
  name: SpotDraft V1 Emails API
  slug: spotdraft-v1-emails-api
- description: Public legal intake endpoints for intake submission, detail, attachments, and tasks.
  name: SpotDraft V1 Legal Intake API
  slug: spotdraft-v1-legal-intake-api
- description: Native integration helpers for embedded SpotDraft workflows.
  name: SpotDraft V1 Native Integrations API
  slug: spotdraft-v1-native-integrations-api
- description: Legacy obligation-type reference endpoints.
  name: SpotDraft V1 Obligation Types API
  slug: spotdraft-v1-obligation-types-api
- description: List templates, inspect template fields, and read template details across public API versions.
  name: SpotDraft V1 Templates API
  slug: spotdraft-v1-templates-api
- description: List users, list roles, manage role membership, invite users, and update user access across public API versions.
  name: SpotDraft V1 Users API
  slug: spotdraft-v1-users-api
- description: Create webhook subscriptions, inspect sample payloads, validate deliveries, and manage webhook secrets across public API versions.
  name: SpotDraft V1 Webhooks API
  slug: spotdraft-v1-webhooks-api
- description: Read-only analytics SQL execution and related analytics catalog guidance.
  name: SpotDraft V2.1 Analytics Query API
  slug: spotdraft-v2-1-analytics-query-api
- description: Clickwrap agreement preview, consent status, and contract creation endpoints.
  name: SpotDraft V2.1 Clickwrap API
  slug: spotdraft-v2-1-clickwrap-api
- description: Read contract comments and activity history across public API versions.
  name: SpotDraft V2.1 Contract Activity API
  slug: spotdraft-v2-1-contract-activity-api
- description: Contract creation, retrieval, updates, previews, downloads, uploads, and lifecycle actions across public API versions.
  name: SpotDraft V2.1 Contract APIs API
  slug: spotdraft-v2-1-contract-apis-api
- description: Review contract approvals, approvers, and approval actions across public API versions.
  name: SpotDraft V2.1 Contract Approvals API
  slug: spotdraft-v2-1-contract-approvals-api
- description: Read and update integration-owned external metadata attached to a contract.
  name: SpotDraft V2.1 Contract External Metadata API
  slug: spotdraft-v2-1-contract-external-metadata-api
- description: Discover available contract search filters and facet values.
  name: SpotDraft V2.1 Contract Facets API
  slug: spotdraft-v2-1-contract-facets-api
- description: Invite, uninvite, and manage contract participants and invited roles across public API versions.
  name: SpotDraft V2.1 Contract Invitations API
  slug: spotdraft-v2-1-contract-invitations-api
- description: List workspace-level or contract-type-level contract metadata definitions. Legacy API paths may still use key-pointer naming.
  name: SpotDraft V2.1 Contract Metadata Definitions API
  slug: spotdraft-v2-1-contract-metadata-definitions-api
- description: Read and update contract metadata values for a specific contract. Legacy API paths may still use key-pointer naming.
  name: SpotDraft V2.1 Contract Metadata Values API
  slug: spotdraft-v2-1-contract-metadata-values-api
- description: Read and update contract notes across public API versions.
  name: SpotDraft V2.1 Contract Notes API
  slug: spotdraft-v2-1-contract-notes-api
- description: List and inspect obligations generated from a contract.
  name: SpotDraft V2.1 Contract Obligations API
  slug: spotdraft-v2-1-contract-obligations-api
- description: Browse contract types, questionnaire definitions, and contract-type metadata.
  name: SpotDraft V2.1 Contract Types API
  slug: spotdraft-v2-1-contract-types-api
- description: Retrieve contract version history and generated artifacts such as PDF and DOCX.
  name: SpotDraft V2.1 Contract Versions API
  slug: spotdraft-v2-1-contract-versions-api
- description: Create, search, and manage counterparties across public API versions.
  name: SpotDraft V2.1 Counterparties API
  slug: spotdraft-v2-1-counterparties-api
- description: Organization and organization-type lookups across public API versions.
  name: SpotDraft V2.1 Organizations API
  slug: spotdraft-v2-1-organizations-api
- description: Recipient lookups and participant-facing contract resources across public API versions.
  name: SpotDraft V2.1 Recipients API
  slug: spotdraft-v2-1-recipients-api
- description: Sidebar APIs for legal questions, contract query workflows, and related AI-assisted experiences.
  name: SpotDraft V2.1 Sidebar API
  slug: spotdraft-v2-1-sidebar-api
- description: Task and reminder workflows across public API versions.
  name: SpotDraft V2.1 Tasks and Reminders API
  slug: spotdraft-v2-1-tasks-and-reminders-api
- description: List templates, inspect template fields, and read template details across public API versions.
  name: SpotDraft V2.1 Templates API
  slug: spotdraft-v2-1-templates-api
- description: List users, list roles, manage role membership, invite users, and update user access across public API versions.
  name: SpotDraft V2.1 Users API
  slug: spotdraft-v2-1-users-api
- description: Create webhook subscriptions, inspect sample payloads, validate deliveries, and manage webhook secrets across public API versions.
  name: SpotDraft V2.1 Webhooks API
  slug: spotdraft-v2-1-webhooks-api
- description: Download workspace files through signed URLs.
  name: SpotDraft V2.1 Workspace Files API
  slug: spotdraft-v2-1-workspace-files-api
- description: Create and manage workspace tags used to categorize and filter contracts.
  name: SpotDraft V2.1 Workspace Tags API
  slug: spotdraft-v2-1-workspace-tags-api
- description: Workspace-scoped helper endpoints exposed publicly.
  name: SpotDraft V2.1 Workspaces API
  slug: spotdraft-v2-1-workspaces-api
- description: Read contract comments and activity history across public API versions.
  name: SpotDraft V2 Contract Activity API
  slug: spotdraft-v2-contract-activity-api
- description: Contract creation, retrieval, updates, previews, downloads, uploads, and lifecycle actions across public API versions.
  name: SpotDraft V2 Contract APIs API
  slug: spotdraft-v2-contract-apis-api
- description: Review contract approvals, approvers, and approval actions across public API versions.
  name: SpotDraft V2 Contract Approvals API
  slug: spotdraft-v2-contract-approvals-api
- description: Invite, uninvite, and manage contract participants and invited roles across public API versions.
  name: SpotDraft V2 Contract Invitations API
  slug: spotdraft-v2-contract-invitations-api
- description: List workspace-level or contract-type-level contract metadata definitions. Legacy API paths may still use key-pointer naming.
  name: SpotDraft V2 Contract Metadata Definitions API
  slug: spotdraft-v2-contract-metadata-definitions-api
- description: Read and update contract metadata values for a specific contract. Legacy API paths may still use key-pointer naming.
  name: SpotDraft V2 Contract Metadata Values API
  slug: spotdraft-v2-contract-metadata-values-api
- description: Read and update contract notes across public API versions.
  name: SpotDraft V2 Contract Notes API
  slug: spotdraft-v2-contract-notes-api
- description: Browse contract types, questionnaire definitions, and contract-type metadata.
  name: SpotDraft V2 Contract Types API
  slug: spotdraft-v2-contract-types-api
- description: Retrieve contract version history and generated artifacts such as PDF and DOCX.
  name: SpotDraft V2 Contract Versions API
  slug: spotdraft-v2-contract-versions-api
- description: Create, search, and manage counterparties across public API versions.
  name: SpotDraft V2 Counterparties API
  slug: spotdraft-v2-counterparties-api
- description: Organization and organization-type lookups across public API versions.
  name: SpotDraft V2 Organizations API
  slug: spotdraft-v2-organizations-api
- description: Recipient lookups and participant-facing contract resources across public API versions.
  name: SpotDraft V2 Recipients API
  slug: spotdraft-v2-recipients-api
- description: Task and reminder workflows across public API versions.
  name: SpotDraft V2 Tasks and Reminders API
  slug: spotdraft-v2-tasks-and-reminders-api
- description: List templates, inspect template fields, and read template details across public API versions.
  name: SpotDraft V2 Templates API
  slug: spotdraft-v2-templates-api
- description: List users, list roles, manage role membership, invite users, and update user access across public API versions.
  name: SpotDraft V2 Users API
  slug: spotdraft-v2-users-api
artifact_total: 165
collections:
- collection_type: postman
  name: SpotDraft V1 Contract APIs API
  slug: postman-spotdraft-v1-contract-apis-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V1 Emails API
  slug: postman-spotdraft-v1-emails-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V1 Legal Intake API
  slug: postman-spotdraft-v1-legal-intake-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V1 Native Integrations API
  slug: postman-spotdraft-v1-native-integrations-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V1 Obligation Types API
  slug: postman-spotdraft-v1-obligation-types-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V1 Templates API
  slug: postman-spotdraft-v1-templates-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V1 Users API
  slug: postman-spotdraft-v1-users-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V1 Webhooks API
  slug: postman-spotdraft-v1-webhooks-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Analytics Query API
  slug: postman-spotdraft-v2-1-analytics-query-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Clickwrap API
  slug: postman-spotdraft-v2-1-clickwrap-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Contract Activity API
  slug: postman-spotdraft-v2-1-contract-activity-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Contract APIs API
  slug: postman-spotdraft-v2-1-contract-apis-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Contract Approvals API
  slug: postman-spotdraft-v2-1-contract-approvals-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Contract External Metadata API
  slug: postman-spotdraft-v2-1-contract-external-metadata-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Contract Facets API
  slug: postman-spotdraft-v2-1-contract-facets-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Contract Invitations API
  slug: postman-spotdraft-v2-1-contract-invitations-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Contract Metadata Definitions API
  slug: postman-spotdraft-v2-1-contract-metadata-definitions-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Contract Metadata Values API
  slug: postman-spotdraft-v2-1-contract-metadata-values-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Contract Notes API
  slug: postman-spotdraft-v2-1-contract-notes-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Contract Obligations API
  slug: postman-spotdraft-v2-1-contract-obligations-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Contract Types API
  slug: postman-spotdraft-v2-1-contract-types-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Contract Versions API
  slug: postman-spotdraft-v2-1-contract-versions-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Counterparties API
  slug: postman-spotdraft-v2-1-counterparties-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Organizations API
  slug: postman-spotdraft-v2-1-organizations-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Recipients API
  slug: postman-spotdraft-v2-1-recipients-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Sidebar API
  slug: postman-spotdraft-v2-1-sidebar-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Tasks and Reminders API
  slug: postman-spotdraft-v2-1-tasks-and-reminders-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Templates API
  slug: postman-spotdraft-v2-1-templates-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Users API
  slug: postman-spotdraft-v2-1-users-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Webhooks API
  slug: postman-spotdraft-v2-1-webhooks-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Workspace Files API
  slug: postman-spotdraft-v2-1-workspace-files-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Workspace Tags API
  slug: postman-spotdraft-v2-1-workspace-tags-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2.1 Workspaces API
  slug: postman-spotdraft-v2-1-workspaces-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Contract Activity API
  slug: postman-spotdraft-v2-contract-activity-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Contract APIs API
  slug: postman-spotdraft-v2-contract-apis-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Contract Approvals API
  slug: postman-spotdraft-v2-contract-approvals-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Contract Invitations API
  slug: postman-spotdraft-v2-contract-invitations-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Contract Metadata Definitions API
  slug: postman-spotdraft-v2-contract-metadata-definitions-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Contract Metadata Values API
  slug: postman-spotdraft-v2-contract-metadata-values-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Contract Notes API
  slug: postman-spotdraft-v2-contract-notes-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Contract Types API
  slug: postman-spotdraft-v2-contract-types-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Contract Versions API
  slug: postman-spotdraft-v2-contract-versions-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Counterparties API
  slug: postman-spotdraft-v2-counterparties-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Organizations API
  slug: postman-spotdraft-v2-organizations-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Recipients API
  slug: postman-spotdraft-v2-recipients-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Tasks and Reminders API
  slug: postman-spotdraft-v2-tasks-and-reminders-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Templates API
  slug: postman-spotdraft-v2-templates-api
- collection_type: postman
  name: SpotDraft V1 Contract APIs V2 Users API
  slug: postman-spotdraft-v2-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SpotDraft V1 Contract APIs API
  slug: open-spotdraft-v1-contract-apis-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V1 Emails API
  slug: open-spotdraft-v1-emails-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V1 Legal Intake API
  slug: open-spotdraft-v1-legal-intake-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V1 Native Integrations API
  slug: open-spotdraft-v1-native-integrations-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V1 Obligation Types API
  slug: open-spotdraft-v1-obligation-types-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V1 Templates API
  slug: open-spotdraft-v1-templates-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V1 Users API
  slug: open-spotdraft-v1-users-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V1 Webhooks API
  slug: open-spotdraft-v1-webhooks-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Analytics Query API
  slug: open-spotdraft-v2-1-analytics-query-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Clickwrap API
  slug: open-spotdraft-v2-1-clickwrap-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Contract Activity API
  slug: open-spotdraft-v2-1-contract-activity-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Contract APIs API
  slug: open-spotdraft-v2-1-contract-apis-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Contract Approvals API
  slug: open-spotdraft-v2-1-contract-approvals-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Contract External Metadata API
  slug: open-spotdraft-v2-1-contract-external-metadata-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Contract Facets API
  slug: open-spotdraft-v2-1-contract-facets-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Contract Invitations API
  slug: open-spotdraft-v2-1-contract-invitations-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Contract Metadata Definitions API
  slug: open-spotdraft-v2-1-contract-metadata-definitions-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Contract Metadata Values API
  slug: open-spotdraft-v2-1-contract-metadata-values-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Contract Notes API
  slug: open-spotdraft-v2-1-contract-notes-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Contract Obligations API
  slug: open-spotdraft-v2-1-contract-obligations-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Contract Types API
  slug: open-spotdraft-v2-1-contract-types-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Contract Versions API
  slug: open-spotdraft-v2-1-contract-versions-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Counterparties API
  slug: open-spotdraft-v2-1-counterparties-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Organizations API
  slug: open-spotdraft-v2-1-organizations-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Recipients API
  slug: open-spotdraft-v2-1-recipients-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Sidebar API
  slug: open-spotdraft-v2-1-sidebar-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Tasks and Reminders API
  slug: open-spotdraft-v2-1-tasks-and-reminders-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Templates API
  slug: open-spotdraft-v2-1-templates-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Users API
  slug: open-spotdraft-v2-1-users-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Webhooks API
  slug: open-spotdraft-v2-1-webhooks-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Workspace Files API
  slug: open-spotdraft-v2-1-workspace-files-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Workspace Tags API
  slug: open-spotdraft-v2-1-workspace-tags-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2.1 Workspaces API
  slug: open-spotdraft-v2-1-workspaces-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Contract Activity API
  slug: open-spotdraft-v2-contract-activity-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Contract APIs API
  slug: open-spotdraft-v2-contract-apis-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Contract Approvals API
  slug: open-spotdraft-v2-contract-approvals-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Contract Invitations API
  slug: open-spotdraft-v2-contract-invitations-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Contract Metadata Definitions API
  slug: open-spotdraft-v2-contract-metadata-definitions-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Contract Metadata Values API
  slug: open-spotdraft-v2-contract-metadata-values-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Contract Notes API
  slug: open-spotdraft-v2-contract-notes-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Contract Types API
  slug: open-spotdraft-v2-contract-types-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Contract Versions API
  slug: open-spotdraft-v2-contract-versions-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Counterparties API
  slug: open-spotdraft-v2-counterparties-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Organizations API
  slug: open-spotdraft-v2-organizations-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Recipients API
  slug: open-spotdraft-v2-recipients-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Tasks and Reminders API
  slug: open-spotdraft-v2-tasks-and-reminders-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Templates API
  slug: open-spotdraft-v2-templates-api
- collection_type: open
  name: SpotDraft V1 Contract APIs V2 Users API
  slug: open-spotdraft-v2-users-api
- collection_type: open
  name: SpotDraft API
  slug: open-spotdraft
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/spotdraft/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spotdraft-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/spotdraft-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spotdraft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spotdraft-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.spotdraft.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.spotdraft.com/api/docs/
- group: operate
  title: ''
  type: Support
  url: https://support.spotdraft.com
- group: operate
  title: ''
  type: Support
  url: https://help.spotdraft.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spotdraft.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.spotdraft.com/book-a-demo
- group: start
  title: ''
  type: Login
  url: https://app.spotdraft.com
- group: company
  title: ''
  type: Blog
  url: https://www.spotdraft.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.spotdraft.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.spotdraft.com/careers
- group: auth
  title: ''
  type: Security
  url: https://www.spotdraft.com/security
- group: auth
  title: ''
  type: Trust
  url: https://www.spotdraft.com/trust-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spotdraft.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spotdraft.com/terms-of-service
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SpotDraft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spotdraft
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/getspotdraft
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@spotdraft
created: '2026-05-25'
description: SpotDraft is an AI-powered Contract Lifecycle Management (CLM) platform headquartered in Bangalore, India, with offices in San Francisco, New York, and London. The platform lets legal, sales, procurement, and operations teams create, negotiate, sign, store, and analyze contracts in one place. Core capabilities include conditional workflows and approval routing, collaborative Word-based negotiation, a searchable contract repository with granular access controls, embedded SpotDraft AI for metadata extraction and risk flagging, ESIGN/EIDAS-compliant e-signatures, Clickwrap agreements, obligation tracking, and analytics dashboards. SpotDraft serves 450+ companies and is recognized as a Leader in the IDC MarketScape for AI-enabled buy-side CLMs and a G2 Leader. The company exposes a documented Public API (OpenAPI 3.0.3) with versions v1, v2, and v2.1 covering contracts, templates, counterparties, approvals, workflows, clickwrap, webhooks, analytics, users, and organizations across
  four regional clusters (India, United States, European Union, Middle East). Webhooks notify external systems of contract lifecycle events in real time. Native integrations exist for Salesforce, HubSpot, Zoho, Slack, Microsoft Teams, Google Drive, Dropbox, Box, OneDrive, SharePoint, DocuSign, Okta, Jira, Coupa, Zapier, and Greenhouse.
examples:
- key_count: 2
  name: Spotdraft Create Contract Example
  slug: spotdraft-create-contract-example
- key_count: 2
  name: Spotdraft List Contracts Example
  slug: spotdraft-list-contracts-example
- key_count: 5
  name: Spotdraft Webhook Event Example
  slug: spotdraft-webhook-event-example
finops:
- name: Spotdraft Finops
  service_category: Business Applications
  slug: spotdraft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spotdraft.png
json_schemas:
- name: SpotDraft Clickwrap
  property_count: 0
  slug: spotdraft-clickwrap
- name: SpotDraft Contract
  property_count: 10
  slug: spotdraft-contract
- name: SpotDraft ContractType
  property_count: 0
  slug: spotdraft-contracttype
- name: SpotDraft Counterparty
  property_count: 7
  slug: spotdraft-counterparty
- name: SpotDraft Organization
  property_count: 11
  slug: spotdraft-organization
- name: SpotDraft User
  property_count: 7
  slug: spotdraft-user
jsonld:
- class_count: 43
  name: Spotdraft Context
  property_count: 0
  slug: spotdraft-context
layout: provider
modified: '2026-05-25'
name: SpotDraft
nav: Providers
network: true
overview: 'SpotDraft publishes 48 APIs on the [APIs.io](https://apis.io/) network, including V1 Contract APIs API, V1 Emails API, V1 Legal Intake API, and 45 more. Tagged areas include Contract Lifecycle Management, CLM, Contracts, Legal Tech, and E-Signature.


  The SpotDraft catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SpotDraft''s developer surface includes authentication, documentation, support, pricing, signup flow, engineering blog, GitHub presence, and 16 more developer resources.'
plans:
- name: Spotdraft Plans Pricing
  plan_count: 4
  slug: spotdraft-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 0
  name: Spotdraft Rate Limits
  slug: spotdraft-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SpotDraft API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spotdraft-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: SpotDraft API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 5
  slug: spotdraft-rules
score:
  band: developing
  composite: 46.3
  delta: -10.9
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 9.8
    contract_quality: 64.4
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 15.8
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 48
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/spotdraft/refs/heads/main/screenshots/spotdraft-2026-06-20T194352.png
security:
- kind: authentication
  name: Spotdraft Authentication
  slug: spotdraft-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Spotdraft Domain Security
  slug: spotdraft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Spotdraft Trust Center
  slug: spotdraft-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR, FIPS 140
slug: spotdraft
tags:
- Contract Lifecycle Management
- CLM
- Contracts
- Legal Tech
- E-Signature
- Clickwrap
- Workflows
- Approvals
- Negotiation
- Templates
- Counterparties
- Obligations
- Analytics
- Webhooks
- AI
- SaaS
- Bangalore
website: https://www.spotdraft.com
---
