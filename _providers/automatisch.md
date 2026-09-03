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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Automatisch exposes a REST API used by its web application for managing flows (automated workflows), connections (service credentials), users, and integrations. The API supports webhook trigger endpoi
  name: Automatisch REST API
  slug: automatisch-rest-api
artifact_total: 21
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/automatisch/automatisch/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/automatisch/automatisch/blob/main/CODE_OF_CONDUCT.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/automatisch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://automatisch.io
- group: docs
  title: ''
  type: Documentation
  url: https://automatisch.io/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/automatisch
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/automatisch/automatisch
- group: start
  title: ''
  type: GettingStarted
  url: https://automatisch.io/docs/installation/docker
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/automatisch/automatisch/releases
created: '2026-03-27'
description: Automatisch is an open source business automation tool and self-hosted alternative to Zapier that connects different services to automate workflows without programming knowledge. Built with JavaScript/Node.js, it supports 100+ integrations including Slack, GitHub, Gmail, PostgreSQL, and AI services. Licensed under AGPL-3.0 for the community edition, with an enterprise edition for commercial deployments.
features:
- description: Automatisch ships with over 100 pre-built connectors for popular services including Slack, Discord, GitHub, GitLab, Gmail, Google Sheets, Airtable, Notion, Trello, OpenAI, Anthropic, PostgreSQL, and many more.
  name: 100+ Built-In Integrations
- description: Deploy Automatisch on your own infrastructure using Docker Compose, keeping all workflow data and credentials under your control with no data sent to third-party cloud services.
  name: Self-Hosted Deployment
- description: Built-in webhook trigger support allows external services to trigger Automatisch flows via HTTP POST, enabling event-driven automation from any service that supports outbound webhooks.
  name: Webhook Triggers
- description: A visual drag-and-drop interface for building multi-step automation workflows connecting triggers from one service to actions in another without writing code.
  name: No-Code Workflow Builder
- description: The community edition is licensed under AGPL-3.0, allowing free use, modification, and distribution. An enterprise edition with additional features is available for commercial deployments.
  name: AGPL-3.0 Open Source
- description: Extend Automatisch by developing custom app integrations using the JavaScript SDK. Custom apps follow the same trigger/action pattern as built-in integrations.
  name: Custom App Development
finops:
- name: Automatisch Finops
  service_category: API
  slug: automatisch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/automatisch.png
integrations:
- description: Send messages, create channels, and respond to Slack events in automated flows.
  name: Slack
- description: Trigger flows from GitHub events and create issues, PRs, and comments programmatically.
  name: GitHub
- description: Send emails and trigger flows from incoming Gmail messages.
  name: Gmail
- description: Read and write rows in Google Sheets as steps in automated workflows.
  name: Google Sheets
- description: Call OpenAI APIs (GPT, DALL-E, Whisper) as steps within Automatisch automation flows.
  name: OpenAI
- description: Query and write to PostgreSQL databases as steps in automation flows.
  name: PostgreSQL
layout: provider
modified: '2026-04-19'
name: Automatisch
nav: Providers
network: true
overview: 'Automatisch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Workflow-Automation, Self-Hosted, Open-Source, Zapier Alternative, and No-Code.


  Automatisch''s developer surface includes documentation, getting-started guide, release notes, and 6 more developer resources.'
plans:
- name: Automatisch Plans Pricing
  plan_count: 3
  slug: automatisch-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Automatisch Rate Limits
  slug: automatisch-rate-limits
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 40.0
  previous_composite: 17.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/automatisch/refs/heads/main/screenshots/automatisch-2026-06-20T172657.png
security:
- kind: domain-security
  name: Automatisch Domain Security
  slug: automatisch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: automatisch
tags:
- Workflow-Automation
- Self-Hosted
- Open-Source
- Zapier Alternative
- No-Code
- JavaScript
- Node.js
- AGPL
use_cases:
- description: Automate repetitive business processes such as lead routing, support ticket triage, and data synchronization between SaaS tools without relying on cloud automation vendors.
  name: Business Process Automation
- description: Self-host workflow automation to keep sensitive business data on-premises or in private cloud infrastructure, meeting GDPR and data residency requirements.
  name: Data Privacy Compliance
- description: Automate developer workflows including GitHub issue-to-Slack notifications, CI/CD status updates, and pull request review reminders.
  name: Developer Workflow Automation
- description: Connect CRM tools with marketing platforms to automate lead nurturing, email sequences, and customer data synchronization across tools.
  name: CRM and Marketing Automation
website: https://automatisch.io
---
