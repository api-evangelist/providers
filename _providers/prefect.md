---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 283
  human_in_the_loop: 6
  name: Prefect Agentic Access
  operation_count: 436
  slug: prefect-agentic-access
  summary_line: 436 operations · 283 acting · 6 human-in-the-loop
api_count: 63
apis:
- description: 'The Prefect Server REST API is the self-hosted variant of the Prefect orchestration API for managing workflows, flow runs, task runs, deployments, and work pools. When running Prefect server locally, '
  name: Prefect Server REST API
  slug: prefect-server-rest-api
- description: 'The Prefect Python SDK is used to build, test, and execute workflows against the Prefect API. It provides decorators such as @flow and @task for defining workflows, along with programmatic interfaces '
  name: Prefect Python SDK
  slug: prefect-python-sdk
- description: View and update account billing information.
  name: Prefect Account Billing API
  slug: prefect-account-billing-api
- description: The Account Images API from Prefect — 1 operation(s) for account images.
  name: Prefect Account Images API
  slug: prefect-account-images-api
- description: View and update user memberships to an Account.
  name: Prefect Account Memberships API
  slug: prefect-account-memberships-api
- description: View and define user Roles within an Account.
  name: Prefect Account Roles API
  slug: prefect-account-roles-api
- description: Set up an account.
  name: Prefect Account SSO API
  slug: prefect-account-sso-api
- description: Interact with Prefect Cloud Accounts.
  name: Prefect Accounts API
  slug: prefect-accounts-api
- description: The AI API from Prefect — 1 operation(s) for ai.
  name: Prefect AI API
  slug: prefect-ai-api
- description: The Artifacts API from Prefect — 7 operation(s) for artifacts.
  name: Prefect Artifacts API
  slug: prefect-artifacts-api
- description: The Asset Publications API from Prefect — 1 operation(s) for asset publications.
  name: Prefect Asset Publications API
  slug: prefect-asset-publications-api
- description: The Asset Subscriptions API from Prefect — 1 operation(s) for asset subscriptions.
  name: Prefect Asset Subscriptions API
  slug: prefect-asset-subscriptions-api
- description: The Assets API from Prefect — 11 operation(s) for assets.
  name: Prefect Assets API
  slug: prefect-assets-api
- description: The Automations API from Prefect — 7 operation(s) for automations.
  name: Prefect Automations API
  slug: prefect-automations-api
- description: The Available Assets API from Prefect — 1 operation(s) for available assets.
  name: Prefect Available Assets API
  slug: prefect-available-assets-api
- description: The Block capabilities API from Prefect — 1 operation(s) for block capabilities.
  name: Prefect Block capabilities API
  slug: prefect-block-capabilities-api
- description: Interact with a Workspace's Blocks.
  name: Prefect Block documents API
  slug: prefect-block-documents-api
- description: Interact with a Workspace's Block schemas.
  name: Prefect Block schemas API
  slug: prefect-block-schemas-api
- description: Interact with a Workspace's Block types.
  name: Prefect Block types API
  slug: prefect-block-types-api
- description: Manage bots (service accounts) within an Account
  name: Prefect Bots API
  slug: prefect-bots-api
- description: The Collections API from Prefect — 2 operation(s) for collections.
  name: Prefect Collections API
  slug: prefect-collections-api
- description: Interact with a Workspace's Task Run Concurrency Limits.
  name: Prefect Concurrency Limits API
  slug: prefect-concurrency-limits-api
- description: Interact with a Workspace's Global Concurrency Limits.
  name: Prefect Concurrency Limits V2 API
  slug: prefect-concurrency-limits-v2-api
- description: Interact with a Workspace's Deployments.
  name: Prefect Deployments API
  slug: prefect-deployments-api
- description: The Download API from Prefect — 3 operation(s) for download.
  name: Prefect Download API
  slug: prefect-download-api
- description: The Event Publications API from Prefect — 3 operation(s) for event publications.
  name: Prefect Event Publications API
  slug: prefect-event-publications-api
- description: The Event Subscriptions API from Prefect — 2 operation(s) for event subscriptions.
  name: Prefect Event Subscriptions API
  slug: prefect-event-subscriptions-api
- description: Interact with Prefect Observability
  name: Prefect Events API
  slug: prefect-events-api
- description: Interact with a Workspace's Flow Run States.
  name: Prefect Flow Run States API
  slug: prefect-flow-run-states-api
- description: Interact with a Workspace's Flow Runs.
  name: Prefect Flow Runs API
  slug: prefect-flow-runs-api
- description: Interact with a Workspace's Flows.
  name: Prefect Flows API
  slug: prefect-flows-api
- description: Manage account invitations.
  name: Prefect Invitations API
  slug: prefect-invitations-api
- description: Interact with a Workspace's Logs.
  name: Prefect Logs API
  slug: prefect-logs-api
- description: The Managed Automations API from Prefect — 6 operation(s) for managed automations.
  name: Prefect Managed Automations API
  slug: prefect-managed-automations-api
- description: Inspect the current User.
  name: Prefect Me API
  slug: prefect-me-api
- description: The Metrics API from Prefect — 6 operation(s) for metrics.
  name: Prefect Metrics API
  slug: prefect-metrics-api
- description: The Pins API from Prefect — 3 operation(s) for pins.
  name: Prefect Pins API
  slug: prefect-pins-api
- description: The Rate Limits API from Prefect — 7 operation(s) for rate limits.
  name: Prefect Rate Limits API
  slug: prefect-rate-limits-api
- description: The Resources API from Prefect — 10 operation(s) for resources.
  name: Prefect Resources API
  slug: prefect-resources-api
- description: The Root API from Prefect — 1 operation(s) for root.
  name: Prefect Root API
  slug: prefect-root-api
- description: Interact with a Workspace's Saved Searches.
  name: Prefect SavedSearches API
  slug: prefect-savedsearches-api
- description: The Schemas API from Prefect — 2 operation(s) for schemas.
  name: Prefect Schemas API
  slug: prefect-schemas-api
- description: The SLAs API from Prefect — 9 operation(s) for slas.
  name: Prefect SLAs API
  slug: prefect-slas-api
- description: The Spans API from Prefect — 9 operation(s) for spans.
  name: Prefect Spans API
  slug: prefect-spans-api
- description: Interact with a Workspace's Task Run States.
  name: Prefect Task Run States API
  slug: prefect-task-run-states-api
- description: Interact with a Workspace's Task Runs.
  name: Prefect Task Runs API
  slug: prefect-task-runs-api
- description: The Task Workers API from Prefect — 1 operation(s) for task workers.
  name: Prefect Task Workers API
  slug: prefect-task-workers-api
- description: The Teams API from Prefect — 5 operation(s) for teams.
  name: Prefect Teams API
  slug: prefect-teams-api
- description: The UI API from Prefect — 10 operation(s) for ui.
  name: Prefect UI API
  slug: prefect-ui-api
- description: Interact with User objects, including creating API Keys.
  name: Prefect Users API
  slug: prefect-users-api
- description: The Variables API from Prefect — 5 operation(s) for variables.
  name: Prefect Variables API
  slug: prefect-variables-api
- description: The Webhooks API from Prefect — 4 operation(s) for webhooks.
  name: Prefect Webhooks API
  slug: prefect-webhooks-api
- description: The Work Pools API from Prefect — 20 operation(s) for work pools.
  name: Prefect Work Pools API
  slug: prefect-work-pools-api
- description: Interact with a Workspace's Work Queues.
  name: Prefect Work Queues API
  slug: prefect-work-queues-api
- description: The Workspace Access API from Prefect — 1 operation(s) for workspace access.
  name: Prefect Workspace Access API
  slug: prefect-workspace-access-api
- description: The Workspace Bot Access API from Prefect — 3 operation(s) for workspace bot access.
  name: Prefect Workspace Bot Access API
  slug: prefect-workspace-bot-access-api
- description: Manage workspace invitations.
  name: Prefect Workspace Invitations API
  slug: prefect-workspace-invitations-api
- description: The Workspace Rate Limit Allocations API from Prefect — 1 operation(s) for workspace rate limit allocations.
  name: Prefect Workspace Rate Limit Allocations API
  slug: prefect-workspace-rate-limit-allocations-api
- description: View and define Roles within a Workspace.
  name: Prefect Workspace Roles API
  slug: prefect-workspace-roles-api
- description: View available workspace scopes.
  name: Prefect Workspace Scopes API
  slug: prefect-workspace-scopes-api
- description: The Workspace Team Access API from Prefect — 3 operation(s) for workspace team access.
  name: Prefect Workspace Team Access API
  slug: prefect-workspace-team-access-api
- description: Manage users' access to a Workspace.
  name: Prefect Workspace User Access API
  slug: prefect-workspace-user-access-api
- description: Interact with Prefect Cloud Workspaces.
  name: Prefect Workspaces API
  slug: prefect-workspaces-api
artifact_total: 133
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Prefect Cloud Account Billing API
  slug: open-prefect-account-billing-api
- collection_type: open
  name: Prefect Cloud Account Billing Account Images API
  slug: open-prefect-account-images-api
- collection_type: open
  name: Prefect Cloud Account Billing Account Memberships API
  slug: open-prefect-account-memberships-api
- collection_type: open
  name: Prefect Cloud Account Billing Account Roles API
  slug: open-prefect-account-roles-api
- collection_type: open
  name: Prefect Cloud Account Billing Account SSO API
  slug: open-prefect-account-sso-api
- collection_type: open
  name: Prefect Cloud Account Billing Accounts API
  slug: open-prefect-accounts-api
- collection_type: open
  name: Prefect Cloud Account Billing AI API
  slug: open-prefect-ai-api
- collection_type: open
  name: Prefect Cloud Account Billing Artifacts API
  slug: open-prefect-artifacts-api
- collection_type: open
  name: Prefect Cloud Account Billing Asset Publications API
  slug: open-prefect-asset-publications-api
- collection_type: open
  name: Prefect Cloud Account Billing Asset Subscriptions API
  slug: open-prefect-asset-subscriptions-api
- collection_type: open
  name: Prefect Cloud Account Billing Assets API
  slug: open-prefect-assets-api
- collection_type: open
  name: Prefect Cloud Account Billing Automations API
  slug: open-prefect-automations-api
- collection_type: open
  name: Prefect Cloud Account Billing Available Assets API
  slug: open-prefect-available-assets-api
- collection_type: open
  name: Prefect Cloud Account Billing Block capabilities API
  slug: open-prefect-block-capabilities-api
- collection_type: open
  name: Prefect Cloud Account Billing Block documents API
  slug: open-prefect-block-documents-api
- collection_type: open
  name: Prefect Cloud Account Billing Block schemas API
  slug: open-prefect-block-schemas-api
- collection_type: open
  name: Prefect Cloud Account Billing Block types API
  slug: open-prefect-block-types-api
- collection_type: open
  name: Prefect Cloud Account Billing Bots API
  slug: open-prefect-bots-api
- collection_type: open
  name: Prefect Cloud Account Billing Collections API
  slug: open-prefect-collections-api
- collection_type: open
  name: Prefect Cloud Account Billing Concurrency Limits API
  slug: open-prefect-concurrency-limits-api
- collection_type: open
  name: Prefect Cloud Account Billing Concurrency Limits V2 API
  slug: open-prefect-concurrency-limits-v2-api
- collection_type: open
  name: Prefect Cloud Account Billing Deployments API
  slug: open-prefect-deployments-api
- collection_type: open
  name: Prefect Cloud Account Billing Download API
  slug: open-prefect-download-api
- collection_type: open
  name: Prefect Cloud Account Billing Event Publications API
  slug: open-prefect-event-publications-api
- collection_type: open
  name: Prefect Cloud Account Billing Event Subscriptions API
  slug: open-prefect-event-subscriptions-api
- collection_type: open
  name: Prefect Cloud Account Billing Events API
  slug: open-prefect-events-api
- collection_type: open
  name: Prefect Cloud Account Billing Flow Run States API
  slug: open-prefect-flow-run-states-api
- collection_type: open
  name: Prefect Cloud Account Billing Flow Runs API
  slug: open-prefect-flow-runs-api
- collection_type: open
  name: Prefect Cloud Account Billing Flows API
  slug: open-prefect-flows-api
- collection_type: open
  name: Prefect Cloud Account Billing Invitations API
  slug: open-prefect-invitations-api
- collection_type: open
  name: Prefect Cloud Account Billing Logs API
  slug: open-prefect-logs-api
- collection_type: open
  name: Prefect Cloud Account Billing Managed Automations API
  slug: open-prefect-managed-automations-api
- collection_type: open
  name: Prefect Cloud Account Billing Me API
  slug: open-prefect-me-api
- collection_type: open
  name: Prefect Cloud Account Billing Metrics API
  slug: open-prefect-metrics-api
- collection_type: open
  name: Prefect Cloud Account Billing Pins API
  slug: open-prefect-pins-api
- collection_type: open
  name: Prefect Cloud Account Billing Rate Limits API
  slug: open-prefect-rate-limits-api
- collection_type: open
  name: Prefect Cloud Account Billing Resources API
  slug: open-prefect-resources-api
- collection_type: open
  name: Prefect Cloud Account Billing Root API
  slug: open-prefect-root-api
- collection_type: open
  name: Prefect Cloud Account Billing SavedSearches API
  slug: open-prefect-savedsearches-api
- collection_type: open
  name: Prefect Cloud Account Billing Schemas API
  slug: open-prefect-schemas-api
- collection_type: open
  name: Prefect Cloud Account Billing SLAs API
  slug: open-prefect-slas-api
- collection_type: open
  name: Prefect Cloud Account Billing Spans API
  slug: open-prefect-spans-api
- collection_type: open
  name: Prefect Cloud Account Billing Task Run States API
  slug: open-prefect-task-run-states-api
- collection_type: open
  name: Prefect Cloud Account Billing Task Runs API
  slug: open-prefect-task-runs-api
- collection_type: open
  name: Prefect Cloud Account Billing Task Workers API
  slug: open-prefect-task-workers-api
- collection_type: open
  name: Prefect Cloud Account Billing Teams API
  slug: open-prefect-teams-api
- collection_type: open
  name: Prefect Cloud Account Billing UI API
  slug: open-prefect-ui-api
- collection_type: open
  name: Prefect Cloud Account Billing Users API
  slug: open-prefect-users-api
- collection_type: open
  name: Prefect Cloud Account Billing Variables API
  slug: open-prefect-variables-api
- collection_type: open
  name: Prefect Cloud Account Billing Webhooks API
  slug: open-prefect-webhooks-api
- collection_type: open
  name: Prefect Cloud Account Billing Work Pools API
  slug: open-prefect-work-pools-api
- collection_type: open
  name: Prefect Cloud Account Billing Work Queues API
  slug: open-prefect-work-queues-api
- collection_type: open
  name: Prefect Cloud Account Billing Workspace Access API
  slug: open-prefect-workspace-access-api
- collection_type: open
  name: Prefect Cloud Account Billing Workspace Bot Access API
  slug: open-prefect-workspace-bot-access-api
- collection_type: open
  name: Prefect Cloud Account Billing Workspace Invitations API
  slug: open-prefect-workspace-invitations-api
- collection_type: open
  name: Prefect Cloud Account Billing Workspace Rate Limit Allocations API
  slug: open-prefect-workspace-rate-limit-allocations-api
- collection_type: open
  name: Prefect Cloud Account Billing Workspace Roles API
  slug: open-prefect-workspace-roles-api
- collection_type: open
  name: Prefect Cloud Account Billing Workspace Scopes API
  slug: open-prefect-workspace-scopes-api
- collection_type: open
  name: Prefect Cloud Account Billing Workspace Team Access API
  slug: open-prefect-workspace-team-access-api
- collection_type: open
  name: Prefect Cloud Account Billing Workspace User Access API
  slug: open-prefect-workspace-user-access-api
- collection_type: open
  name: Prefect Cloud Account Billing Workspaces API
  slug: open-prefect-workspaces-api
- collection_type: open
  name: Prefect Cloud API
  slug: open-prefect
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/PrefectHQ/prefect/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prefect-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/prefect-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prefect-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prefect
- group: start
  title: ''
  type: Portal
  url: https://www.prefect.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.prefect.io/v3/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.prefect.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.prefect.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.prefect.cloud/
- group: operate
  title: ''
  type: Support
  url: https://www.prefect.io/support
- group: operate
  title: ''
  type: Community
  url: https://www.prefect.io/community
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.prefect.io/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.prefect.io/
- group: auth
  title: ''
  type: Security
  url: https://www.prefect.io/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prefect.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prefect.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PrefectHQ
- group: start
  title: ''
  type: Login
  url: https://app.prefect.cloud/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/PrefectHQ/prefect-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.prefect.io/llms.txt
created: '2026-03-03'
description: Prefect is a Python-native workflow orchestration tool for building, scheduling, and monitoring data pipelines with fault tolerance. Prefect provides a hybrid execution model where the cloud control plane coordinates workflows while code and data remain in customer infrastructure, offering both a managed cloud platform and a self-hosted open-source server.
finops:
- name: Prefect Finops
  service_category: API
  slug: prefect-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prefect.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: Prefect
nav: Providers
network: true
overview: 'Prefect publishes 61 APIs on the [APIs.io](https://apis.io/) network, including Account Billing API, Account Images API, Account Memberships API, and 58 more. Tagged areas include Automation, Data Pipelines, Orchestration, Python, and Workflows.


  Prefect''s developer surface includes developer portal, getting-started guide, engineering blog, pricing, signup flow, support, changelog, and 14 more developer resources.'
plans:
- name: Prefect Plans Pricing
  plan_count: 3
  slug: prefect-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Prefect Rate Limits
  slug: prefect-rate-limits
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 47.3
    developer_ergonomics: 34.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 61
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prefect/refs/heads/main/screenshots/prefect-2026-06-20T192044.png
security:
- kind: domain-security
  name: Prefect Domain Security
  slug: prefect-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Prefect Trust Center
  slug: prefect-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: prefect
tags:
- Automation
- Data Pipelines
- Orchestration
- Python
- Workflows
website: https://www.prefect.io
---
