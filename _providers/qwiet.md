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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 58.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 59
  human_in_the_loop: 2
  name: Qwiet Agentic Access
  operation_count: 145
  slug: qwiet-agentic-access
  summary_line: 145 operations · 59 acting · 2 human-in-the-loop
api_count: 27
apis:
- description: Notification and alerting related endpoints (such as webhooks)
  name: Qwiet alerting API
  slug: qwiet-alerting-api
- description: The analyze API from Qwiet — 2 operation(s) for analyze.
  name: Qwiet analyze API
  slug: qwiet-analyze-api
- description: The user-created groups of applications. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-3251cbed-4ae3-4b06-8cad-c8748e49c7ec?action=collection%2
  name: Qwiet app_groups API
  slug: qwiet-app-groups-api
- description: The user-created application labels. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/30743751-da3c929b-651f-414c-993c-ee2b2573b2f4?action=collection%2Ffo
  name: Qwiet app_labels API
  slug: qwiet-app-labels-api
- description: The applications submitted for analysis. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-e9d0bf19-30bd-46f4-b40c-9df03d2a463a?action=collection%2
  name: Qwiet apps API
  slug: qwiet-apps-api
- description: The AutoFix suggestions for findings in applications. Harness SAST and SCA AutoFix uses large language models (LLMs) to generate potential code fix suggestions for findings produced by Qwiet AI by Har
  name: Qwiet autofix API
  slug: qwiet-autofix-api
- description: The endpoints to manage the Azure Boards integration.
  name: Qwiet azureboard API
  slug: qwiet-azureboard-api
- description: The branch information for scans of applications.
  name: Qwiet branches API
  slug: qwiet-branches-api
- description: The text threads (with individual comments ordered by time) attached to findings. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-49dbc330-9cb4-4
  name: Qwiet comments API
  slug: qwiet-comments-api
- description: Multi-Language Apps are groups of applications that are scanned together as a single application. This is useful for applications that are a compound of various programming languages and configuration
  name: Qwiet compounds API
  slug: qwiet-compounds-api
- description: The results of a scan (which can include vulnerabilities, secrets, or insights). [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-156075f8-c7cf-4e
  name: Qwiet findings API
  slug: qwiet-findings-api
- description: The endpoints for downloading backups of an organization's data.
  name: Qwiet org_backup API
  slug: qwiet-org-backup-api
- description: The logical grouping (e.g., tenant/account) within Qwiet that defines a set of users, teams, and applications. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-colle
  name: Qwiet orgs API
  slug: qwiet-orgs-api
- description: Roles-based access control (RBAC) allows you to control the permissions users in an organization are granted. The permissions granted to a user are additive. The base level of a user's permission is d
  name: Qwiet rbac API
  slug: qwiet-rbac-api
- description: The summaries of applications and their findings for a specific organization. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-b675d7af-bdd5-49a4-
  name: Qwiet reports API
  slug: qwiet-reports-api
- description: The integration endpoints allowing orgs to configure Qwiet to act as a SAML service provider (SP) that uses the customer's identity provider (IdP) to log users in. [![Run in Postman](https://run.pstmn
  name: Qwiet SAML API
  slug: qwiet-saml-api
- description: The integration endpoints for generating and downloading SARIF reports for applications.
  name: Qwiet sarif API
  slug: qwiet-sarif-api
- description: The saved searches endpoints allow users to save specific search queries for organization and app findings
  name: Qwiet saved_searches API
  slug: qwiet-saved-searches-api
- description: The summaries of software composition analysis (SCA) results for apps in an organization. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/30743751-08a1d6
  name: Qwiet sca API
  slug: qwiet-sca-api
- description: The instances where Qwiet AI by Harness is invoked to identify findings in an application. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-dc6a68
  name: Qwiet scans API
  slug: qwiet-scans-api
- description: Scopes define the type of resource and the operation that you can perform with the access token you bear. For example, `scans:create` means that the bearer of the token with this scope can create scan
  name: Qwiet scopes API
  slug: qwiet-scopes-api
- description: The integration endpoints enabling users to set up a Slack integration.
  name: Qwiet slack API
  slug: qwiet-slack-api
- description: The endpoints to manage team-level configuration.
  name: Qwiet team_config API
  slug: qwiet-team-config-api
- description: Used to authenticate with the API. Can be issued by org admins. Each access token is owned by the org that issued it. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/ru
  name: Qwiet tokens API
  slug: qwiet-tokens-api
- description: Users pertains the users in general as qwiet.ai users and of each org as organization users.
  name: Qwiet users API
  slug: qwiet-users-api
- description: The specific instances of an application scanned using Qwiet AI by Harness. [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9829310-d8e4a6f2-bdce-4807-a8
  name: Qwiet versions API
  slug: qwiet-versions-api
- description: The endpoints to manage the Wiz integration.
  name: Qwiet wiz API
  slug: qwiet-wiz-api
artifact_total: 32
asyncapis:
- description: ''
  name: Qwiet Alerting Webhooks
  slug: qwiet-alerting-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://qwiet.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shiftleft.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shiftleft.io/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ShiftLeftSecurity
- group: company
  title: ''
  type: Blog
  url: https://qwiet.ai/blog/
- group: start
  title: ''
  type: Login
  url: https://app.shiftleft.io/login
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
- group: operate
  title: ''
  type: Support
  url: https://www.harness.io/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shiftleft.io
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/qwiet-api-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/qwiet-api-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qwiet-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qwiet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qwiet-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qwiet-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/qwiet-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qwiet-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qwiet-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/qwiet-alerting-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/qwiet-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/qwiet-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qwiet-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qwiet-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qwiet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qwiet-domain-security.yml
created: '2026-07-17'
description: Qwiet AI (formerly ShiftLeft, now part of Harness) is an application security testing platform delivering SAST, SCA, IaC, container, and secrets scanning in a single scan, with reachability and exploitability filtering to cut false positives and AI-generated code fixes (AutoFix) to speed remediation. The Qwiet API (OpenAPI 3.0.0, v4, Bearer-token auth) lets you programmatically manage applications, run and compare scans, retrieve and triage findings with data flow, request fixes, manage users and RBAC, and configure alerting webhooks. Qwiet also ships an official MCP server and a set of agent skills for the scan-triage-autofix workflow, plus the `sl` CLI.
image: https://docs.shiftleft.io/img/sl-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: qwiet-mcp.yml
  slug: qwiet-mcpyml
modified: '2026-07-20'
name: Qwiet
nav: Providers
network: true
overview: 'Qwiet publishes 27 APIs on the [APIs.io](https://apis.io/) network, including alerting API, analyze API, app_groups API, and 24 more. Tagged areas include Company, Security, Application Security, SAST, and SCA.


  The Qwiet catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qwiet''s developer surface includes documentation, API reference, engineering blog, pricing, support, authentication, CLI, and 21 more developer resources.'
random_paper: 62
score:
  band: developing
  composite: 49.9
  delta: -0.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.2
    developer_ergonomics: 54.3
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 50.6
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Qwiet Authentication
  slug: qwiet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qwiet Domain Security
  slug: qwiet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qwiet
tags:
- Company
- Security
- Application Security
- SAST
- SCA
- Vulnerability Management
- DevSecOps
- Code Analysis
- MCP
website: https://qwiet.ai/
---
