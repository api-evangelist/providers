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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Office Agentic Access
  operation_count: 15
  slug: microsoft-office-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 9
apis:
- description: API for interacting with Microsoft Word documents, including reading, writing, and formatting content.
  name: Word API
  slug: word-api
- description: API for working with Excel workbooks, worksheets, ranges, charts, and tables.
  name: Excel API
  slug: excel-api
- description: API for creating and manipulating PowerPoint presentations, slides, and content.
  name: PowerPoint API
  slug: powerpoint-api
- description: API for accessing and managing email, calendar, contacts, and tasks in Outlook.
  name: Outlook Mail API
  slug: outlook-mail-api
- description: API for accessing files and folders stored in OneDrive and SharePoint.
  name: OneDrive API
  slug: onedrive-api
- description: API for integrating with Microsoft Teams, including messaging, channels, and collaboration features.
  name: Teams API
  slug: teams-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The Drive API from Microsoft Office — 4 operation(s) for drive.
  name: Microsoft Office Drive API
  slug: microsoft-office-drive-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The Mail API from Microsoft Office — 4 operation(s) for mail.
  name: Microsoft Office Mail API
  slug: microsoft-office-mail-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The Teams API from Microsoft Office — 4 operation(s) for teams.
  name: Microsoft Office Teams API
  slug: microsoft-office-teams-api
arazzos:
- description: Resolve the user's drive, browse the root, inspect an item, and download its content.
  name: Microsoft Office Discover and Download a OneDrive File
  slug: microsoft-office-drive-file-discovery-download-workflow
- description: Find a file in the drive root, confirm its metadata, and post it to a Teams channel.
  name: Microsoft Office Announce a New OneDrive File in a Teams Channel
  slug: microsoft-office-drive-file-to-teams-notification-workflow
- description: Read a file's metadata, back up its current bytes, upload new content, and read the item back.
  name: Microsoft Office Update a OneDrive File and Verify the Write
  slug: microsoft-office-drive-file-update-roundtrip-workflow
- description: Enumerate mail folders, page a filtered message list, and read one message in full.
  name: Microsoft Office Inventory Mail Folders and Export Messages
  slug: microsoft-office-mail-folder-message-export-workflow
- description: Match an inbox message against a filter, read it in full, and raise it as a Teams channel alert.
  name: Microsoft Office Escalate an Inbox Message to a Teams Channel
  slug: microsoft-office-mail-to-teams-alert-workflow
- description: List filtered inbox messages, read the top match in full, and send a reply.
  name: Microsoft Office Triage Inbox Messages and Respond
  slug: microsoft-office-mail-triage-and-respond-workflow
- description: Walk the user's joined teams, enumerate a team's channels, and pull a channel's recent messages.
  name: Microsoft Office Build a Teams Channel Message Digest
  slug: microsoft-office-teams-channel-message-digest-workflow
- description: Resolve a joined team, check for an existing channel, create it when missing, and post a kickoff message.
  name: Microsoft Office Provision a Teams Channel and Announce It
  slug: microsoft-office-teams-channel-provisioning-workflow
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Graph API (Office 365 subset) Drive API
  slug: open-microsoft-office-drive-api
- collection_type: open
  name: Microsoft Graph API (Office 365 subset) Drive Mail API
  slug: open-microsoft-office-mail-api
- collection_type: open
  name: Microsoft Graph API (Office 365 subset) Drive Teams API
  slug: open-microsoft-office-teams-api
- collection_type: open
  name: Microsoft Graph API (Office 365 subset)
  slug: open-microsoft-office
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-office-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/microsoft-office-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microsoft-office-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/microsoft-office-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microsoft-office-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-office-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/microsoft-office-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-office-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-office-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microsoft-office-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/microsoft-office-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/microsoft-office-cli.yml
- group: design
  title: ''
  type: Components
  url: components/microsoft-office-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/microsoft-office-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/microsoft-office-sandbox.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-office-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-office-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-office-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-office-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-office-scopes.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-mail-triage-and-respond-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-mail-folder-message-export-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-mail-to-teams-alert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-drive-file-discovery-download-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-drive-file-update-roundtrip-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-drive-file-to-teams-notification-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-teams-channel-provisioning-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-teams-channel-message-digest-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-365
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/microsoft-365
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/office/dev/add-ins/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
- group: company
  title: ''
  type: Blog
  url: https://developer.microsoft.com/en-us/microsoft-365/blogs/
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/answers/products/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.microsoft.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
created: '2024-01-01'
description: A collection of APIs for Microsoft Office applications and services, providing programmatic access to Word, Excel, PowerPoint, Outlook, OneDrive, and Teams through Microsoft Graph and Office JavaScript APIs.
finops:
- name: Microsoft Office Finops
  service_category: API
  slug: microsoft-office-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-office.png
layout: provider
mcp_servers:
- description: Microsoft ships an official Model Context Protocol server for Microsoft Graph (the API surface behind this Office 365 collection). "Microsoft MCP Server for Enterprise" is a read-only, RAG-assisted se
  name: Microsoft MCP Server for Enterprise
  slug: microsoft-mcp-server-for-enterprise
modified: '2026-06-20'
name: Microsoft Office
nav: Providers
network: true
overview: 'Microsoft Office publishes 3 APIs on the [APIs.io](https://apis.io/) network: Drive API, Mail API, and Teams API. Tagged areas include Collaboration, Documents, Microsoft, Office, and Productivity.


  Microsoft Office''s developer surface includes changelog, CLI, sandbox, authentication, developer portal, documentation, engineering blog, and 32 more developer resources.'
plans:
- name: Microsoft Office Plans Pricing
  plan_count: 3
  slug: microsoft-office-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Microsoft Office Rate Limits
  slug: microsoft-office-rate-limits
scopes:
- name: Microsoft Office Scopes
  scope_count: 16
  slug: microsoft-office-scopes
  summary_line: 16 scopes · authorizationCode
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 4.5
    contract_quality: 50.3
    developer_ergonomics: 78.6
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-office/refs/heads/main/screenshots/microsoft-office-2026-06-20T185511.png
security:
- kind: authentication
  name: Microsoft Office Authentication
  slug: microsoft-office-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Office Domain Security
  slug: microsoft-office-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Office Vulnerability Disclosure
  slug: microsoft-office-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Office Trust Center
  slug: microsoft-office-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, ISO/IEC 22301, FedRAMP High, HIPAA / HITECH, PCI DSS, GDPR, CSA STAR, FIPS 140-2
slug: microsoft-office
tags:
- Collaboration
- Documents
- Microsoft
- Office
- Productivity
website: https://www.microsoft.com/en-us/microsoft-365
---
