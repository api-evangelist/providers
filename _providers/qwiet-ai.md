---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 59
  human_in_the_loop: 2
  name: Qwiet Ai Agentic Access
  operation_count: 145
  slug: qwiet-ai-agentic-access
  summary_line: 145 operations · 59 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: Notification and alerting related endpoints (such as webhooks)
  name: Qwiet Ai alerting API
  slug: qwiet-ai-alerting-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The analyze API from Qwiet Ai — 2 operation(s) for analyze.
  name: Qwiet Ai analyze API
  slug: qwiet-ai-analyze-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The user-created groups of applications. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-3251cbed-4ae3-4b06-8cad-c8748e49c7ec?action=collection%2
  name: Qwiet Ai app_groups API
  slug: qwiet-ai-app-groups-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The user-created application labels. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/30743751-da3c929b-651f-414c-993c-ee2b2573b2f4?action=collection%2Ffo
  name: Qwiet Ai app_labels API
  slug: qwiet-ai-app-labels-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The applications submitted for analysis. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-e9d0bf19-30bd-46f4-b40c-9df03d2a463a?action=collection%2
  name: Qwiet Ai apps API
  slug: qwiet-ai-apps-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The AutoFix suggestions for findings in applications. Harness SAST and SCA AutoFix uses large language models (LLMs) to generate potential code fix suggestions for findings produced by Qwiet AI by Har
  name: Qwiet Ai autofix API
  slug: qwiet-ai-autofix-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The endpoints to manage the Azure Boards integration.
  name: Qwiet Ai azureboard API
  slug: qwiet-ai-azureboard-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The branch information for scans of applications.
  name: Qwiet Ai branches API
  slug: qwiet-ai-branches-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The text threads (with individual comments ordered by time) attached to findings. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-49dbc330-9cb4-4
  name: Qwiet Ai comments API
  slug: qwiet-ai-comments-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: Multi-Language Apps are groups of applications that are scanned together as a single application. This is useful for applications that are a compound of various programming languages and configuration
  name: Qwiet Ai compounds API
  slug: qwiet-ai-compounds-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The results of a scan (which can include vulnerabilities, secrets, or insights). [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-156075f8-c7cf-4e
  name: Qwiet Ai findings API
  slug: qwiet-ai-findings-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The endpoints for downloading backups of an organization's data.
  name: Qwiet Ai org_backup API
  slug: qwiet-ai-org-backup-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The logical grouping (e.g., tenant/account) within Qwiet that defines a set of users, teams, and applications. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-colle
  name: Qwiet Ai orgs API
  slug: qwiet-ai-orgs-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: Roles-based access control (RBAC) allows you to control the permissions users in an organization are granted. The permissions granted to a user are additive. The base level of a user's permission is d
  name: Qwiet Ai rbac API
  slug: qwiet-ai-rbac-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The summaries of applications and their findings for a specific organization. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-b675d7af-bdd5-49a4-
  name: Qwiet Ai reports API
  slug: qwiet-ai-reports-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The integration endpoints allowing orgs to configure Qwiet to act as a SAML service provider (SP) that uses the customer's identity provider (IdP) to log users in. [![Run in Postman](https://run.pstmn
  name: Qwiet Ai SAML API
  slug: qwiet-ai-saml-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The integration endpoints for generating and downloading SARIF reports for applications.
  name: Qwiet Ai sarif API
  slug: qwiet-ai-sarif-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The saved searches endpoints allow users to save specific search queries for organization and app findings
  name: Qwiet Ai saved_searches API
  slug: qwiet-ai-saved-searches-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The summaries of software composition analysis (SCA) results for apps in an organization. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/30743751-08a1d6
  name: Qwiet Ai sca API
  slug: qwiet-ai-sca-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The instances where Qwiet AI by Harness is invoked to identify findings in an application. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-dc6a68
  name: Qwiet Ai scans API
  slug: qwiet-ai-scans-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: Scopes define the type of resource and the operation that you can perform with the access token you bear. For example, `scans:create` means that the bearer of the token with this scope can create scan
  name: Qwiet Ai scopes API
  slug: qwiet-ai-scopes-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The integration endpoints enabling users to set up a Slack integration.
  name: Qwiet Ai slack API
  slug: qwiet-ai-slack-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The endpoints to manage team-level configuration.
  name: Qwiet Ai team_config API
  slug: qwiet-ai-team-config-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: Used to authenticate with the API. Can be issued by org admins. Each access token is owned by the org that issued it. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/ru
  name: Qwiet Ai tokens API
  slug: qwiet-ai-tokens-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: Users pertains the users in general as qwiet.ai users and of each org as organization users.
  name: Qwiet Ai users API
  slug: qwiet-ai-users-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The specific instances of an application scanned using Qwiet AI by Harness. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-d8e4a6f2-bdce-4807-a8
  name: Qwiet Ai versions API
  slug: qwiet-ai-versions-api
- baseURL: https://app.shiftleft.io/api/v4
  baseurl_source: declared
  description: The endpoints to manage the Wiz integration.
  name: Qwiet Ai wiz API
  slug: qwiet-ai-wiz-api
artifact_total: 60
asyncapis:
- description: ''
  name: Qwiet Ai Alerting Webhooks
  slug: qwiet-ai-alerting-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: alerting API
  slug: open-qwiet-ai-alerting-api
- collection_type: open
  name: alerting analyze API
  slug: open-qwiet-ai-analyze-api
- collection_type: open
  name: alerting app_groups API
  slug: open-qwiet-ai-app-groups-api
- collection_type: open
  name: alerting app_labels API
  slug: open-qwiet-ai-app-labels-api
- collection_type: open
  name: alerting apps API
  slug: open-qwiet-ai-apps-api
- collection_type: open
  name: alerting autofix API
  slug: open-qwiet-ai-autofix-api
- collection_type: open
  name: alerting azureboard API
  slug: open-qwiet-ai-azureboard-api
- collection_type: open
  name: alerting branches API
  slug: open-qwiet-ai-branches-api
- collection_type: open
  name: alerting comments API
  slug: open-qwiet-ai-comments-api
- collection_type: open
  name: alerting compounds API
  slug: open-qwiet-ai-compounds-api
- collection_type: open
  name: alerting findings API
  slug: open-qwiet-ai-findings-api
- collection_type: open
  name: alerting org_backup API
  slug: open-qwiet-ai-org-backup-api
- collection_type: open
  name: alerting orgs API
  slug: open-qwiet-ai-orgs-api
- collection_type: open
  name: alerting rbac API
  slug: open-qwiet-ai-rbac-api
- collection_type: open
  name: alerting reports API
  slug: open-qwiet-ai-reports-api
- collection_type: open
  name: alerting SAML API
  slug: open-qwiet-ai-saml-api
- collection_type: open
  name: alerting sarif API
  slug: open-qwiet-ai-sarif-api
- collection_type: open
  name: alerting saved_searches API
  slug: open-qwiet-ai-saved-searches-api
- collection_type: open
  name: alerting sca API
  slug: open-qwiet-ai-sca-api
- collection_type: open
  name: alerting scans API
  slug: open-qwiet-ai-scans-api
- collection_type: open
  name: alerting scopes API
  slug: open-qwiet-ai-scopes-api
- collection_type: open
  name: alerting slack API
  slug: open-qwiet-ai-slack-api
- collection_type: open
  name: alerting team_config API
  slug: open-qwiet-ai-team-config-api
- collection_type: open
  name: alerting tokens API
  slug: open-qwiet-ai-tokens-api
- collection_type: open
  name: alerting users API
  slug: open-qwiet-ai-users-api
- collection_type: open
  name: alerting versions API
  slug: open-qwiet-ai-versions-api
- collection_type: open
  name: alerting wiz API
  slug: open-qwiet-ai-wiz-api
common:
- group: company
  title: ''
  type: Website
  url: https://qwiet.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.harness.io/docs/sast-and-sca/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shiftleft.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shiftleft.io/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shiftleft.io/inspect/getting-started/quickstart
- group: start
  title: ''
  type: Login
  url: https://app.shiftleft.io/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ShiftLeftSecurity
- group: operate
  title: ''
  type: Support
  url: https://www.harness.io/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.harness.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.harness.io/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.harness.io/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/qwiet-ai-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qwiet-ai-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qwiet-ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qwiet-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qwiet-ai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qwiet-ai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qwiet-ai-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/qwiet-ai-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/qwiet-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qwiet-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/qwiet-ai-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qwiet-ai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/qwiet-ai-alerting-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qwiet-ai-llms.txt
- group: build
  title: ''
  type: Postman
  url: https://god.gw.postman.com/run-collection/9829310-3251cbed-4ae3-4b06-8cad-c8748e49c7ec
- group: company
  title: ''
  type: Blog
  url: https://qwiet.ai/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shiftleft.io
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/qwiet-ai-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qwiet-ai-agentic-access.yml
created: '2026-07-17'
description: Qwiet AI (by Harness, formerly ShiftLeft) is an application security testing platform that unifies SAST, SCA, secrets, IaC, and container scanning with AI-assisted AutoFix remediation. The Qwiet AI API v4 (https://app.shiftleft.io/api/v4) lets teams programmatically manage applications, run and read code scans, work with findings and source-to-sink data flows, request and apply AutoFix recommendations, look up package CVEs (Intelligent SCA), manage RBAC/teams/tokens, and configure alerting webhooks and Slack notifications. Qwiet also ships a first-party CLI (`sl`), a published MCP server (harness-code-security-mcp), and packaged agent skills, making its code-security workflows agent-ready. Surfaced as a portfolio company of Mayfield and enriched from the provider's public developer surface.
image: https://docs.shiftleft.io/img/sl-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Qwiet Ai MCP Server
  slug: qwiet-ai-mcp-server
modified: '2026-08-08'
name: Qwiet Ai
nav: Providers
network: true
overview: 'Qwiet Ai publishes 27 APIs on the [APIs.io](https://apis.io/) network, including alerting API, analyze API, app_groups API, and 24 more. Tagged areas include Company, Security, Application Security, SAST, and SCA.


  The Qwiet Ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qwiet Ai''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, CLI, and 24 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 58.6
    developer_ergonomics: 83.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qwiet-ai/refs/heads/main/screenshots/qwiet-ai-2026-08-17T081438.png
security:
- kind: authentication
  name: Qwiet Ai Authentication
  slug: qwiet-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qwiet Ai Domain Security
  slug: qwiet-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qwiet-ai
tags:
- Company
- Security
- Application Security
- SAST
- SCA
- Code Security
- Vulnerability Management
- DevSecOps
- AutoFix
website: https://qwiet.ai
---
