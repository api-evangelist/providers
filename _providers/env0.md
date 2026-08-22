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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Env0 Agentic Access
  operation_count: 21
  slug: env0-agentic-access
  summary_line: 21 operations · 8 acting
api_count: 12
apis:
- description: env0 is an infrastructure-as-code automation platform providing cost estimation, policy enforcement, and self-service environments. The public REST API is available at https://api.env0.com/ and uses H
  name: Env0
  slug: env0
- description: The Agents API from Env0 — 1 operation(s) for agents.
  name: Env0 Agents API
  slug: env0-agents-api
- description: The ApprovalPolicies API from Env0 — 1 operation(s) for approvalpolicies.
  name: Env0 ApprovalPolicies API
  slug: env0-approvalpolicies-api
- description: The Configuration API from Env0 — 1 operation(s) for configuration.
  name: Env0 Configuration API
  slug: env0-configuration-api
- description: The Deployments API from Env0 — 2 operation(s) for deployments.
  name: Env0 Deployments API
  slug: env0-deployments-api
- description: The Environments API from Env0 — 2 operation(s) for environments.
  name: Env0 Environments API
  slug: env0-environments-api
- description: The Modules API from Env0 — 1 operation(s) for modules.
  name: Env0 Modules API
  slug: env0-modules-api
- description: The Organizations API from Env0 — 1 operation(s) for organizations.
  name: Env0 Organizations API
  slug: env0-organizations-api
- description: The Projects API from Env0 — 2 operation(s) for projects.
  name: Env0 Projects API
  slug: env0-projects-api
- description: The Templates API from Env0 — 1 operation(s) for templates.
  name: Env0 Templates API
  slug: env0-templates-api
- description: The Users API from Env0 — 1 operation(s) for users.
  name: Env0 Users API
  slug: env0-users-api
- description: The Webhooks API from Env0 — 1 operation(s) for webhooks.
  name: Env0 Webhooks API
  slug: env0-webhooks-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: env0 Agents API
  slug: open-env0-agents-api
- collection_type: open
  name: env0 Agents ApprovalPolicies API
  slug: open-env0-approvalpolicies-api
- collection_type: open
  name: env0 Agents Configuration API
  slug: open-env0-configuration-api
- collection_type: open
  name: env0 Agents Deployments API
  slug: open-env0-deployments-api
- collection_type: open
  name: env0 Agents Environments API
  slug: open-env0-environments-api
- collection_type: open
  name: env0 Agents Modules API
  slug: open-env0-modules-api
- collection_type: open
  name: env0 Agents Organizations API
  slug: open-env0-organizations-api
- collection_type: open
  name: env0 Agents Projects API
  slug: open-env0-projects-api
- collection_type: open
  name: env0 Agents Templates API
  slug: open-env0-templates-api
- collection_type: open
  name: env0 Agents Users API
  slug: open-env0-users-api
- collection_type: open
  name: env0 Agents Webhooks API
  slug: open-env0-webhooks-api
- collection_type: open
  name: env0 API
  slug: open-env0
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/env0-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/env0-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/env0-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/env0
- group: company
  title: ''
  type: Website
  url: https://www.env0.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.env0.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.env0.com/reference/api-introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.env0.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.env0.com/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/env0
created: '2026-03-27'
description: env0 is an infrastructure-as-code automation platform providing cost estimation, policy enforcement, and self-service environments for Terraform, OpenTofu, Pulumi, CloudFormation, and Kubernetes workloads.
finops:
- name: Env0 Finops
  service_category: API
  slug: env0-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/env0.png
layout: provider
modified: '2026-04-28'
name: Env0
nav: Providers
network: true
overview: 'Env0 publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Agents API, ApprovalPolicies API, Configuration API, and 8 more. Tagged areas include FinOps, Infrastructure as Code, DevOps, and Cloud.


  Env0''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, GitHub presence, and 4 more developer resources.'
plans:
- name: Env0 Plans Pricing
  plan_count: 3
  slug: env0-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Env0 Rate Limits
  slug: env0-rate-limits
score:
  band: thin
  composite: 31.8
  delta: -1.1
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/env0/refs/heads/main/screenshots/env0-2026-06-20T180838.png
security:
- kind: authentication
  name: Env0 Authentication
  slug: env0-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Env0 Domain Security
  slug: env0-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: env0
tags:
- FinOps
- Infrastructure as Code
- DevOps
- Cloud
website: https://www.env0.com/
---
