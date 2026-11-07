---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Drive Agentic Access
  operation_count: 8
  slug: google-drive-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 2
apis:
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The Google Drive REST API v3 — 64 operations across files, permissions, comments, replies, revisions, shared drives, changes, approvals, access proposals and apps, converted from Google's own Discover
  name: Google Drive Files API
  slug: google-drive-files-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The about API from Google Drive — 1 operation(s) for about.
  name: Google Drive About API
  slug: google-drive-about-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The accessproposals API from Google Drive — 3 operation(s) for accessproposals.
  name: Google Drive Accessproposals API
  slug: google-drive-accessproposals-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The approvals API from Google Drive — 8 operation(s) for approvals.
  name: Google Drive Approvals API
  slug: google-drive-approvals-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The apps API from Google Drive — 2 operation(s) for apps.
  name: Google Drive Apps API
  slug: google-drive-apps-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The changes API from Google Drive — 3 operation(s) for changes.
  name: Google Drive Changes API
  slug: google-drive-changes-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The channels API from Google Drive — 1 operation(s) for channels.
  name: Google Drive Channels API
  slug: google-drive-channels-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The comments API from Google Drive — 2 operation(s) for comments.
  name: Google Drive Comments API
  slug: google-drive-comments-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The drives API from Google Drive — 4 operation(s) for drives.
  name: Google Drive Drives API
  slug: google-drive-drives-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The operations API from Google Drive — 1 operation(s) for operations.
  name: Google Drive Operations API
  slug: google-drive-operations-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The permissions API from Google Drive — 1 operation(s) for permissions.
  name: Google Drive Permissions API
  slug: google-drive-permissions-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The replies API from Google Drive — 2 operation(s) for replies.
  name: Google Drive Replies API
  slug: google-drive-replies-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The revisions API from Google Drive — 2 operation(s) for revisions.
  name: Google Drive Revisions API
  slug: google-drive-revisions-api
- baseURL: https://www.googleapis.com/drive/v3
  baseurl_source: declared
  description: The teamdrives API from Google Drive — 2 operation(s) for teamdrives.
  name: Google Drive Teamdrives API
  slug: google-drive-teamdrives-api
arazzos:
- description: Resolve a file, copy it into an archive folder, verify the backup exists, and only then permanently delete the original.
  name: Google Drive Back Up a File Before Permanently Deleting It
  slug: google-drive-backup-and-delete-workflow
- description: Resolve a template file, copy it into a destination folder under a new name, and read the copy back.
  name: Google Drive Copy a Template File into a Folder
  slug: google-drive-copy-template-workflow
- description: Create a folder, create a file inside it, and read the file back to confirm placement.
  name: Google Drive Provision a Folder and Seed a File
  slug: google-drive-provision-folder-workflow
- description: Verify a file, audit who already has access, grant a new permission, and confirm the resulting access list.
  name: Google Drive Share a File and Audit Its Access
  slug: google-drive-share-file-workflow
- description: Find a file by name within a folder and update it if it exists, otherwise create it.
  name: Google Drive Upsert a File by Name
  slug: google-drive-upsert-file-by-name-workflow
artifact_total: 81
collections:
- collection_type: open
  name: Google Drive Files API
  slug: open-google-drive-files-api
- collection_type: open
  name: Google Drive API
  slug: open-google-drive
common:
- group: agent
  href: https://artifacts.apis.io/google-drive/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/google-drive/rate-limits/google-drive-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-drive-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/google-drive/rules/google-drive-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/google-drive-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/google-drive/rules/google-drive-rules.yml
  title: ''
  type: Spectral
  url: rules/google-drive-rules.yml
- group: design
  href: https://artifacts.apis.io/google-drive/rules/google-drive-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/google-drive-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/google-drive/vocabulary/google-drive-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/google-drive-vocabulary.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cloud.google.com/security/compliance/offerings
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.google.com/workspace/drive/api/v3/reference
- group: build
  href: https://artifacts.apis.io/google-drive/mcp/google-drive-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/google-drive-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/google-drive/hosts/google-drive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/google-drive-hosts.yml
- group: build
  href: https://artifacts.apis.io/google-drive/integrations/google-drive-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/google-drive-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/google-drive/packages/google-drive-packages.yml
  title: ''
  type: SDKs
  url: packages/google-drive-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/?utm_source=about&utm_medium=referral&utm_campaign=footer-link
- group: auth
  title: ''
  type: Security
  url: https://accounts.google.com/ServiceLogin?hl=en-US&continue=https://myaccount.google.com/intro/security
- group: start
  title: ''
  type: Sandbox
  url: https://play.google.com/console/about/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy?hl=en&fg=1
- group: start
  title: ''
  type: Login
  url: https://accounts.google.com/v3/signin/identifier?continue=https://docs.google.com/&emr=1&followup=https://docs.google.com/&osid=1&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1322403262:1793808245464019
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-drive/overview
- group: commercial
  href: https://artifacts.apis.io/google-drive/plans/google-drive-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-drive-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/google-drive/finops/google-drive-finops.yml
  title: ''
  type: FinOps
  url: finops/google-drive-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: other
  href: https://artifacts.apis.io/google-drive/overlays/google-drive-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/google-drive-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/google-drive/agentic-access/google-drive-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-drive-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-drive/security/google-drive-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-drive-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-drive/security/google-drive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-drive-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-drive/security/google-drive-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/google-drive-trust-center.yml
- group: build
  href: https://artifacts.apis.io/google-drive/packages/google-drive-packages.yml
  title: ''
  type: Packages
  url: packages/google-drive-packages.yml
- group: agent
  href: https://artifacts.apis.io/google-drive/well-known/google-drive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-drive-well-known.yml
- group: agent
  href: https://artifacts.apis.io/google-drive/mcp/google-drive-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/google-drive-mcp.yml
- group: agent
  href: https://artifacts.apis.io/google-drive/llms/google-drive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-drive-llms.txt
- group: design
  href: https://artifacts.apis.io/google-drive/conformance/google-drive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-drive-conformance.yml
- group: design
  href: https://artifacts.apis.io/google-drive/errors/google-drive-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-drive-problem-types.yml
- group: design
  href: https://artifacts.apis.io/google-drive/lifecycle/google-drive-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-drive-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/google-drive/scopes/google-drive-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-drive-scopes.yml
- group: auth
  href: https://artifacts.apis.io/google-drive/authentication/google-drive-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-drive-authentication.yml
- group: design
  href: https://artifacts.apis.io/google-drive/conventions/google-drive-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-drive-conventions.yml
- group: operate
  href: https://artifacts.apis.io/google-drive/changelog/google-drive-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-drive-changelog.yml
- group: design
  href: https://artifacts.apis.io/google-drive/components/google-drive-components.yml
  title: ''
  type: Components
  url: components/google-drive-components.yml
- group: design
  href: https://artifacts.apis.io/google-drive/data-model/google-drive-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-drive-data-model.yml
- group: design
  href: https://artifacts.apis.io/google-drive/arazzo/google-drive-upsert-file-by-name-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-drive-upsert-file-by-name-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-drive/arazzo/google-drive-provision-folder-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-drive-provision-folder-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-drive/arazzo/google-drive-share-file-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-drive-share-file-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-drive/arazzo/google-drive-copy-template-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-drive-copy-template-workflow.yml
- group: design
  href: https://artifacts.apis.io/google-drive/arazzo/google-drive-backup-and-delete-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/google-drive-backup-and-delete-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: start
  title: ''
  type: Portal
  url: https://console.cloud.google.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/drive/api/v3/enable-drive-api
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.google.com/drive/api/v3/handle-errors#rate-limit-exceeded
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus
- group: design
  href: https://artifacts.apis.io/google-drive/json-ld/google-drive-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-drive-context.jsonld
created: '2024-01-15'
description: The Google Drive API allows developers to integrate with Google Drive to create, read, update, and delete files and folders stored in Google Drive. The v3 REST API supports file metadata operations, content upload and download, folder hierarchies, sharing and permissions, and search across a user's Drive.
features:
- 'Google Drive (and Workspace): hundreds of services across File Storage and Productivity'
- 'Detailed pricing: see https://workspace.google.com/pricing.html'
- 'Service: Drive API v3'
- 'Service: Drive Activity API'
- 'Service: Docs API'
- 'Service: Sheets API'
- 'Service: Slides API'
- 'Service: Forms API'
- 'Service: Apps Script'
- 'Service: Workspace Marketplace API'
- 'Service: Drive Labels API'
finops:
- has_sources: true
  method: derived
  name: Google Drive Finops
  primary_unit: user
  service_category: ''
  slug: google-drive-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-drive.png
json_schemas:
- name: About
  property_count: 13
  slug: google-drive-about
- name: AccessProposal
  property_count: 7
  slug: google-drive-access-proposal
- name: AppList
  property_count: 4
  slug: google-drive-app-list
- name: App
  property_count: 24
  slug: google-drive-app
- name: ApprovalList
  property_count: 3
  slug: google-drive-approval-list
- name: Approval
  property_count: 11
  slug: google-drive-approval
- name: ApproveApprovalRequest
  property_count: 1
  slug: google-drive-approve-approval-request
- name: ChangeList
  property_count: 4
  slug: google-drive-change-list
- name: Channel
  property_count: 10
  slug: google-drive-channel
- name: CommentList
  property_count: 3
  slug: google-drive-comment-list
- name: Comment
  property_count: 14
  slug: google-drive-comment
- name: DeclineApprovalRequest
  property_count: 1
  slug: google-drive-decline-approval-request
- name: DriveList
  property_count: 3
  slug: google-drive-drive-list
- name: Drive
  property_count: 12
  slug: google-drive-drive
- name: Google Drive File
  property_count: 14
  slug: google-drive-file
- name: FileList
  property_count: 2
  slug: google-drive-filelist
- name: ListAccessProposalsResponse
  property_count: 2
  slug: google-drive-list-access-proposals-response
- name: Operation
  property_count: 5
  slug: google-drive-operation
- name: Permission
  property_count: 5
  slug: google-drive-permission
- name: PermissionList
  property_count: 2
  slug: google-drive-permissionlist
- name: ReassignApprovalRequest
  property_count: 3
  slug: google-drive-reassign-approval-request
- name: ReplyList
  property_count: 3
  slug: google-drive-reply-list
- name: Reply
  property_count: 11
  slug: google-drive-reply
- name: ResolveAccessProposalRequest
  property_count: 4
  slug: google-drive-resolve-access-proposal-request
- name: RevisionList
  property_count: 3
  slug: google-drive-revision-list
- name: Revision
  property_count: 14
  slug: google-drive-revision
- name: StartApprovalRequest
  property_count: 5
  slug: google-drive-start-approval-request
- name: StartPageToken
  property_count: 2
  slug: google-drive-start-page-token
- name: TeamDriveList
  property_count: 3
  slug: google-drive-team-drive-list
- name: TeamDrive
  property_count: 11
  slug: google-drive-team-drive
json_structures:
- name: Google Drive Structure
  property_count: 0
  slug: google-drive-structure
jsonld:
- class_count: 18
  name: Google Drive Context
  property_count: 0
  slug: google-drive-context
layout: provider
mcp_servers:
- description: Google operates an official remote Model Context Protocol server for Google Drive (Developer Preview). It acts as a proxy that lets AI applications (e.g. Google Antigravity, Claude) read and act on Dr
  name: Google Drive MCP Server
  slug: google-drive
modified: '2026-11-04'
name: Google Drive
nav: Providers
network: true
overview: 'Google Drive publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Files API, About API, Accessproposals API, and 11 more. Tagged areas include Cloud Storage, Collaboration, Document Management, Drives, and File.


  The Google Drive catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Google Drive''s developer surface includes support, sandbox, documentation, authentication, changelog, developer portal, getting-started guide, and 46 more developer resources.'
plans:
- name: Google Drive Plans Pricing
  plan_count: 4
  slug: google-drive-plans-pricing
- name: Google Drive Price Estimates
  plan_count: 0
  slug: google-drive-price-estimates
random_paper: 20
rate_limits:
- limit_count: 4
  name: Google Drive Rate Limits
  slug: google-drive-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Drive — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-drive-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: Google Drive API Rules
  rule_count: 71
  severity_counts:
    error: 54
    hint: 0
    info: 4
    warn: 13
  slug: google-drive-rules
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Google Drive API Rules
  rule_count: 17
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 5
  slug: google-drive-spectral-rules
scopes:
- name: Google Drive Scopes
  scope_count: 13
  slug: google-drive-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: exemplar
  composite: 67.1
  coverage:
    artifact_dirs: 38
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.7
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 64.4
    developer_ergonomics: 58.9
    discoverability: 68.3
    operational_transparency: 75.0
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-drive/google-drive-2026-08-17T083537.png
security:
- kind: authentication
  name: Google Drive Authentication
  slug: google-drive-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Google Drive Domain Security
  slug: google-drive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Drive Vulnerability Disclosure
  slug: google-drive-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Google Drive Trust Center
  slug: google-drive-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, PCI DSS, HIPAA, FedRAMP, GDPR
skill_count: 3
skills:
- name: google-drive-search-and-read-files
  slug: google-drive-search-and-read-files
- name: google-drive-share-file-and-audit-access
  slug: google-drive-share-file-and-audit-access
- name: google-drive-track-drive-changes
  slug: google-drive-track-drive-changes
slug: google-drive
tags:
- Cloud Storage
- Collaboration
- Document Management
- Drives
- File
- Google
- Storage
website: https://www.google.com/
---
