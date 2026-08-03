---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 15
  human_in_the_loop: 2
  name: Openhands Agentic Access
  operation_count: 43
  slug: openhands-agentic-access
  summary_line: 43 operations · 15 acting · 2 human-in-the-loop
api_count: 14
apis:
- description: Composable Python SDK for defining, running, and orchestrating agents locally or scaled to thousands in the cloud. Source at github.com/All-Hands-AI/agent-sdk.
  name: OpenHands Agent SDK
  slug: agent-sdk
- description: Command-line interface for running OpenHands agents with Claude, GPT, or any other LLM. Source at github.com/OpenHands/OpenHands-CLI.
  name: OpenHands CLI
  slug: cli
- description: Local React application with a REST API behind it for driving agents from the desktop. Shipped via Docker and the main OpenHands repo.
  name: OpenHands Local GUI REST API
  slug: local-gui-rest
- description: Hosted OpenHands platform at app.all-hands.dev with a free tier (Minimax model), GitHub/GitLab/Bitbucket integrations, and Slack/Jira/Linear connectors.
  name: OpenHands Cloud
  slug: cloud
- description: The Add Git Providers API from OpenHands — 1 operation(s) for add git providers.
  name: OpenHands Add Git Providers API
  slug: openhands-add-git-providers-api
- description: The Alive API from OpenHands — 1 operation(s) for alive.
  name: OpenHands Alive API
  slug: openhands-alive-api
- description: The Conversations API from OpenHands — 16 operation(s) for conversations.
  name: OpenHands Conversations API
  slug: openhands-conversations-api
- description: The Health API from OpenHands — 1 operation(s) for health.
  name: OpenHands Health API
  slug: openhands-health-api
- description: The Options API from OpenHands — 4 operation(s) for options.
  name: OpenHands Options API
  slug: openhands-options-api
- description: The Reset Settings API from OpenHands — 1 operation(s) for reset settings.
  name: OpenHands Reset Settings API
  slug: openhands-reset-settings-api
- description: The Secrets API from OpenHands — 2 operation(s) for secrets.
  name: OpenHands Secrets API
  slug: openhands-secrets-api
- description: The Settings API from OpenHands — 1 operation(s) for settings.
  name: OpenHands Settings API
  slug: openhands-settings-api
- description: The Unset Provider Tokens API from OpenHands — 1 operation(s) for unset provider tokens.
  name: OpenHands Unset Provider Tokens API
  slug: openhands-unset-provider-tokens-api
- description: The User API from OpenHands — 8 operation(s) for user.
  name: OpenHands User API
  slug: openhands-user-api
artifact_total: 37
collections:
- collection_type: open
  name: OpenHands
  slug: open-openhands
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openhands-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openhands-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openhands-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openhands-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.openhands.dev/
- group: start
  title: ''
  type: Portal
  url: https://app.all-hands.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openhands.dev/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.openhands.dev/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.openhands.dev/usage/getting-started
- group: build
  title: ''
  type: SDKs
  url: https://docs.openhands.dev/sdk
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/OpenHands/OpenHands
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/All-Hands-AI/OpenHands
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/All-Hands-AI/agent-sdk
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/OpenHands/OpenHands-CLI
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/orgs/openhands/projects/1
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenHands
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/All-Hands-AI
- group: operate
  title: ''
  type: Slack
  url: https://dub.sh/openhands
- group: operate
  title: ''
  type: Contact
  url: https://www.openhands.dev/contact
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/OpenHands
- group: company
  title: ''
  type: Blog
  url: https://www.openhands.dev/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openhands.dev/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openhands.dev/terms
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/OpenHandsDev
- group: commercial
  title: ''
  type: License
  url: https://github.com/OpenHands/OpenHands/blob/main/LICENSE
created: '2026-05-23'
description: OpenHands (by All Hands AI, formerly OpenDevin) is an open-source autonomous coding agent platform. Ships as a Python Agent SDK, CLI, local GUI with a REST API, Docker images, and a hosted cloud at app.all-hands.dev plus a self-hosted Kubernetes Enterprise tier. Core code is MIT licensed at github.com/OpenHands/OpenHands with 75K+ stars.
features:
- Open-source autonomous coding agent under MIT license
- Python Agent SDK for embedding agents into custom apps
- CLI for terminal-based agent pair programming
- Local desktop GUI with REST API
- Docker images for one-command local deploy
- Hosted cloud with free tier (Minimax model)
- Self-hosted Enterprise on Kubernetes in private VPC
- Works with Claude, GPT, and any LLM provider
- GitHub, GitLab, Bitbucket integrations
- Slack, Jira, Linear connectors (Cloud/Enterprise)
- Multi-user RBAC for Enterprise
- Conversation sharing and collaboration
- Sandboxed, auditable execution environments
- 75K+ GitHub stars, 9.5K+ forks, 100+ releases
- Use cases include vuln scanning, PR review, legacy migration, incident triage, test expansion, docs automation
finops:
- name: Openhands Finops
  service_category: API
  slug: openhands-finops
image: https://www.openhands.dev/og-image.png
layout: provider
modified: '2026-05-23'
name: OpenHands
nav: Providers
network: true
overview: 'OpenHands publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Add Git Providers API, Alive API, Conversations API, and 7 more. Tagged areas include AI, Agents, Autonomous, Open Source, and Developer Tools.


  OpenHands'' developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 20 more developer resources.'
plans:
- name: Openhands Plans Pricing
  plan_count: 1
  slug: openhands-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Openhands Rate Limits
  slug: openhands-rate-limits
score:
  band: developing
  composite: 42.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 54.3
    developer_ergonomics: 47.8
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openhands/refs/heads/main/screenshots/openhands-2026-06-20T191005.png
security:
- kind: authentication
  name: Openhands Authentication
  slug: openhands-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openhands Domain Security
  slug: openhands-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Openhands Vulnerability Disclosure
  slug: openhands-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: openhands
tags:
- AI
- Agents
- Autonomous
- Open Source
- Developer Tools
- Software Engineering
- Code Generation
website: https://www.openhands.dev/
---
