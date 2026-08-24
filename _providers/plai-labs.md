---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'Deploy a Salt AI workflow as a production HTTP API. A POST to the deployment execution endpoint accepts a workflow_input map (per input node: value + value_type such as RAW) and an optional callback U'
  name: Salt AI Workflow Deployment API
  slug: salt-ai-workflow-deployment-api
artifact_total: 3
asyncapis:
- description: ''
  name: Plai Labs Execution Webhook
  slug: plai-labs-execution-webhook
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plai-labs-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.salt.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.salt.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.salt.ai/deployments/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.salt.ai/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://www.salt.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.salt.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.salt.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.salt.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salt.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salt.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plailabs
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/plai-labs-execution-webhook.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/plai-labs-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plai-labs-llms.txt
created: '2026-07-17'
description: Plai Labs is the a16z-backed venture founded by ex-MySpace leaders Aber Whitcomb and Jim Benedetto (with Chris DeWolfe); its plailabs.com domain now redirects to Salt AI (salt.ai), the team's enterprise AI platform. Salt AI is a visual plus full-code AI workflow platform positioned as "Contextual AI for Regulated Enterprise" that deploys governed, auditable, model-agnostic AI workflows inside a customer's own infrastructure (behind the firewall, zero public data egress to external model providers, immutable audit trails) for life sciences, financial services, energy, and public-sector customers. Workflows built in the Salt visual builder can be deployed as production HTTP APIs that execute asynchronously and return their results via a webhook callback to a caller-supplied URL.
image: https://framerusercontent.com/images/hzTNjbzAvRgyFTtaOqS9rM94NI.png
layout: provider
modified: '2026-07-20'
name: Plai Labs
nav: Providers
network: true
overview: 'Plai Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Workflows, Agents, and LLM.


  The Plai Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Plai Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, and 9 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 30.8
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 45.1
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Plai Labs Domain Security
  slug: plai-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: plai-labs
tags:
- Company
- Artificial Intelligence
- AI Workflows
- Agents
- LLM
- Enterprise
- Regulated Industries
- Life Sciences
- Workflow-Automation
- No-Code
website: https://docs.salt.ai/
---
