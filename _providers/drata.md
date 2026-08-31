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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 114
  human_in_the_loop: 93
  name: Drata Agentic Access
  operation_count: 238
  slug: drata-agentic-access
  summary_line: 238 operations · 114 acting · 93 human-in-the-loop
api_count: 3
apis:
- description: Drata's hosted remote Model Context Protocol server (Beta). MCP-compatible clients (Claude, ChatGPT, Cursor, Microsoft Copilot) connect over OAuth 2.1 with PKCE to regional endpoints for the US, EU an
  name: Drata MCP Server
  slug: mcp
- description: The Account Members API from Drata — 3 operation(s) for account members.
  name: Drata Account Members API
  slug: drata-account-members-api
- description: The Accounts API from Drata — 3 operation(s) for accounts.
  name: Drata Accounts API
  slug: drata-accounts-api
- description: Assets let you build an inventory of policies, personnel and computer infrastructure. The [help docs](https://help.drata.com/en/collections/10485424) have more information.
  name: Drata Assets API
  slug: drata-assets-api
- description: The Audit Requests API from Drata — 2 operation(s) for audit requests.
  name: Drata Audit Requests API
  slug: drata-audit-requests-api
- description: Audits represent compliance assessments for a specific framework and time period. Audit Requests are evidence requests associated with an audit.
  name: Drata Audits API
  slug: drata-audits-api
- description: Background checks verify a person’s identity, history, and qualifications to ensure they meet legal, regulatory, or policy standards. The [help docs](https://help.drata.com/en/articles/5833999-backgro
  name: Drata Background Checks API
  slug: drata-background-checks-api
- description: The Company tracks essential information about your organization. The [help docs](https://help.drata.com/en/articles/8283910) have more information on the purpose of each field.
  name: Drata Company API
  slug: drata-company-api
- description: The Control Library is a catalog of pre-built Control Templates that can be provisioned into a Workspace. Each item carries default mappings to Tests, Policies, Evidence, and Framework Requirements.
  name: Drata Control Library API
  slug: drata-control-library-api
- description: Control Notes allow you to provide additional information about Controls.
  name: Drata Control Notes API
  slug: drata-control-notes-api
- description: Control Owners are the Users responsible for Controls. They ensure the right evidence is associated, that any automated tests are passing, and help prepare for an audit.
  name: Drata Control Owners API
  slug: drata-control-owners-api
- description: Controls are a strategic measure or safeguard that an organization puts in place to protect its assets and meet the requirements of specific compliance frameworks.
  name: Drata Controls API
  slug: drata-controls-api
- description: Custom Connections allow users to integrate external systems with Drata. CUSTOM connections push arbitrary JSON evidence records using a user-defined schema. MDM and HRIS connections use a fixed commo
  name: Drata Custom Connections API
  slug: drata-custom-connections-api
- description: Custom Data Records are JSON evidence records pushed to a Custom Connection resource. Use the session management endpoints to batch upload records and track the status of bulk operations. You can crea
  name: Drata Custom Data Records API
  slug: drata-custom-data-records-api
- description: 'Custom Field Definitions describe the schema - name, required, type, options, entity placements, and framework scope - of the Custom Fields configured on your account. Use them to discover the option '
  name: Drata Custom Field Definitions API
  slug: drata-custom-field-definitions-api
- description: Device Documents allow you to provide manual evidence of Devices compliance. Using the Drata Agent or an MDM connection automatically provides this information.
  name: Drata Device Documents API
  slug: drata-device-documents-api
- description: Devices are computers used by personnel. The data is provided by the Drata Agent or an MDM connection.
  name: Drata Devices API
  slug: drata-devices-api
- description: The Documents API from Drata — 4 operation(s) for documents.
  name: Drata Documents API
  slug: drata-documents-api
- description: Events record the activity of User and automated processes in the Drata platform.
  name: Drata Events API
  slug: drata-events-api
- description: 'Evidence items hold one or more artifacts, the files, URLs, or ticket references that demonstrate a control is operating. <br/>Use the evidence-files endpoint to pre-upload a file, then reference the '
  name: Drata Evidence API
  slug: drata-evidence-api
- description: Drata's Evidence Library serves as a repository for all the evidence you need to collect across your controls. The [help docs](https://help.drata.com/en/articles/8288579-evidence-library-overview) hav
  name: Drata Evidence Library API
  slug: drata-evidence-library-api
- description: Frameworks are collections of controls that are used to assess compliance with specific standards or regulations. The [help docs](https://help.drata.com/en/articles/5329593-frameworks) have more infor
  name: Drata Frameworks API
  slug: drata-frameworks-api
- description: Groups are collections of Users that can be used to manage permissions and access to resources.
  name: Drata Groups API
  slug: drata-groups-api
- description: HR user identity records for a Custom HRIS connection. Use the batch upsert endpoint to submit employee records keyed by your own `identityId`, then use the update endpoint to reflect employment chang
  name: Drata HRIS User Identities API
  slug: drata-hris-user-identities-api
- description: The Knowledge Base API from Drata — 3 operation(s) for knowledge base.
  name: Drata Knowledge Base API
  slug: drata-knowledge-base-api
- description: Monitoring Tests are compliance tests used to determine whether a person, system, process, or organization is adhering to standards set by compliance controls within a framework. The [help docs](https
  name: Drata Monitoring Tests API
  slug: drata-monitoring-tests-api
- description: The Organization API from Drata — 4 operation(s) for organization.
  name: Drata Organization API
  slug: drata-organization-api
- description: Personnel are people who work for your organization. The [help docs](https://help.drata.com/en/collections/2653981) have more information.
  name: Drata Personnel API
  slug: drata-personnel-api
- description: 'A policy is a document that outlines an organization’s commitment to following standards relevant to its operations. The [help docs](https://help.drata.com/en/articles/9202419-policy-center-overview) '
  name: Drata Policies API
  slug: drata-policies-api
- description: Policy Languages let an organization publish the same Policy Version in several languages. Settings endpoints expose the languages an organization has configured and which one is the default; Policy L
  name: Drata Policy Languages API
  slug: drata-policy-languages-api
- description: The Portals API from Drata — 1 operation(s) for portals.
  name: Drata Portals API
  slug: drata-portals-api
- description: The Procurement Connection Mappings API from Drata — 1 operation(s) for procurement connection mappings.
  name: Drata Procurement Connection Mappings API
  slug: drata-procurement-connection-mappings-api
- description: The Products API from Drata — 1 operation(s) for products.
  name: Drata Products API
  slug: drata-products-api
- description: The Questionnaires API from Drata — 2 operation(s) for questionnaires.
  name: Drata Questionnaires API
  slug: drata-questionnaires-api
- description: The Requests API from Drata — 3 operation(s) for requests.
  name: Drata Requests API
  slug: drata-requests-api
- description: Risk Documents are supporting documents, evidence, or other materials that are associated with a risk.
  name: Drata Risk Documents API
  slug: drata-risk-documents-api
- description: The Risk Library is a collection of Risks that can be copied into a Risk Register. The [help docs](https://help.drata.com/en/articles/13371089-drata-s-risk-library-new-experience) have more informatio
  name: Drata Risk Library API
  slug: drata-risk-library-api
- description: Risk Notes allow you to provide additional information about Risks.
  name: Drata Risk Notes API
  slug: drata-risk-notes-api
- description: Risk Registers are a collection of Risks. They are used to organize and manage Risks.
  name: Drata Risk Registers API
  slug: drata-risk-registers-api
- description: Risks are potential events that could impact the security, reputation, and financial health of a company.
  name: Drata Risks API
  slug: drata-risks-api
- description: The Tags API from Drata — 1 operation(s) for tags.
  name: Drata Tags API
  slug: drata-tags-api
- description: Tasks are individual units of work that can be assigned to users.
  name: Drata Tasks API
  slug: drata-tasks-api
- description: The Trust Center Updates API from Drata — 4 operation(s) for trust center updates.
  name: Drata Trust Center Updates API
  slug: drata-trust-center-updates-api
- description: Uploads let you request a pre-signed S3 URL to upload a file for a given purpose (e.g. Evidence), then reference the resulting object key when creating the associated resource.
  name: Drata Uploads API
  slug: drata-uploads-api
- description: User Documents allow you to provide manual evidence of User and Personnel compliance.
  name: Drata User Documents API
  slug: drata-user-documents-api
- description: User's Assigned Policies track the acknowledgement of Policy Versions by Users.
  name: Drata User's Assigned Policies API
  slug: drata-user-s-assigned-policies-api
- description: '**Users** are are people with access to the Drata platform. **Roles** grant permissions to Users. The [help docs](https://help.drata.com/en/collections/5993507) have more information on the default Ro'
  name: Drata Users and Roles API
  slug: drata-users-and-roles-api
- description: Vendor Documents provide compliance-related documentation, such as bridge letters, questionnaires, and SOC reports.
  name: Drata Vendor Documents API
  slug: drata-vendor-documents-api
- description: Vendor Security Reviews track the status of security reviews for Vendors. You can create a security review, upload questionnaires, and track the progress of the review. The [help docs](https://help.dr
  name: Drata Vendor Security Reviews API
  slug: drata-vendor-security-reviews-api
- description: Vendor Types are user-defined classifications used to categorize and organize vendors.
  name: Drata Vendor Types API
  slug: drata-vendor-types-api
- description: Vendors are third-parties that your organization is working with. Drata allows you to track and review risks associated with these third-parties. The [help docs](https://help.drata.com/en/articles/967
  name: Drata Vendors API
  slug: drata-vendors-api
- description: Workspaces allow you to represent different products or business lines that have different compliance requirements. Each Workspace can have its own Frameworks and Controls. The [help docs](https://hel
  name: Drata Workspaces API
  slug: drata-workspaces-api
artifact_total: 62
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/drata-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/drata-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/drata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/drata-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/drata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drata
- group: company
  title: ''
  type: Website
  url: https://drata.com/
- group: other
  title: ''
  type: Developer
  url: https://developers.drata.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/drata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/drata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/drata-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/drata-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/drata-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/drata-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/drata-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/drata-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/drata-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/drata-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/drata-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/drata-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/drata-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/drata-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/drata-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/drata-api-v2-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/drata-examples.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.drata.com/
- group: auth
  title: ''
  type: Security
  url: security/drata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.drata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.drata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.drata.com/openapi/reference/v2/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.drata.com/openapi/reference/v2/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.drata.com/developer-portal/v2/recipes/create-an-api-key/
- group: operate
  title: ''
  type: Support
  url: https://help.drata.com/
- group: company
  title: ''
  type: Blog
  url: https://drata.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://drata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://drata.com/demo
- group: start
  title: ''
  type: Login
  url: https://app.drata.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drata.com/privacy
created: '2026-05-08'
description: Drata is a continuous security and compliance automation platform supporting SOC 2, ISO 27001, HIPAA, PCI DSS, GDPR, and more, with policies, evidence, and trust center. Drata exposes a public REST API plus the SafeBase Trust API (acquired) and a Custom Connections framework for evidence collection.
finops:
- name: Drata Finops
  service_category: GRC
  slug: drata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drata.png
layout: provider
mcp_servers:
- description: Drata's official hosted, remote Model Context Protocol server. It exposes Drata's live compliance, control, policy, monitoring-test, risk and workspace data to MCP-compatible clients (Claude, ChatGPT,
  name: Drata MCP Server
  slug: drata-mcp-server
modified: '2026-08-27'
name: Drata
nav: Providers
network: true
overview: 'Drata publishes 51 APIs on the [APIs.io](https://apis.io/) network, including Account Members API, Accounts API, Assets API, and 48 more. Tagged areas include GRC, Compliance, SOC 2, ISO 27001, and Security.


  Drata''s developer surface includes authentication, changelog, code examples, documentation, API reference, getting-started guide, support, and 34 more developer resources.'
plans:
- name: Drata Plans Pricing
  plan_count: 1
  slug: drata-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Drata Rate Limits
  slug: drata-rate-limits
scopes:
- name: Drata Scopes
  scope_count: 0
  slug: drata-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 23
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 65.0
    developer_ergonomics: 64.3
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/screenshots/drata-2026-06-20T180244.png
security:
- kind: authentication
  name: Drata Authentication
  slug: drata-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Drata Domain Security
  slug: drata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Drata Vulnerability Disclosure
  slug: drata-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Drata Trust Center
  slug: drata-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
slug: drata
tags:
- GRC
- Compliance
- SOC 2
- ISO 27001
- Security
- Risk Management
- Trust Center
- Audit
- Vendor Risk Management
- Compliance Automation
website: https://drata.com/
---
