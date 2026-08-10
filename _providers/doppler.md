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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Doppler Agentic Access
  operation_count: 19
  slug: doppler-agentic-access
  summary_line: 19 operations · 7 acting
api_count: 9
apis:
- description: Versioned REST API (v3) for managing Doppler workplaces, projects, environments, configs, secrets, dynamic secrets, service tokens, service accounts, integrations, audit logs, and webhooks. Authentica
  name: Doppler REST API
  slug: rest-api
- description: The ActivityLogs API from Doppler — 1 operation(s) for activitylogs.
  name: Doppler ActivityLogs API
  slug: doppler-activitylogs-api
- description: The Auth API from Doppler — 1 operation(s) for auth.
  name: Doppler Auth API
  slug: doppler-auth-api
- description: The Configs API from Doppler — 2 operation(s) for configs.
  name: Doppler Configs API
  slug: doppler-configs-api
- description: The Environments API from Doppler — 1 operation(s) for environments.
  name: Doppler Environments API
  slug: doppler-environments-api
- description: The Projects API from Doppler — 2 operation(s) for projects.
  name: Doppler Projects API
  slug: doppler-projects-api
- description: The Secrets API from Doppler — 3 operation(s) for secrets.
  name: Doppler Secrets API
  slug: doppler-secrets-api
- description: The ServiceTokens API from Doppler — 1 operation(s) for servicetokens.
  name: Doppler ServiceTokens API
  slug: doppler-servicetokens-api
- description: The Webhooks API from Doppler — 1 operation(s) for webhooks.
  name: Doppler Webhooks API
  slug: doppler-webhooks-api
artifact_total: 15
collections:
- collection_type: open
  name: Doppler REST API
  slug: open-doppler
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doppler-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/doppler-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/doppler-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doppler-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doppler-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dopplerhq
- group: company
  title: ''
  type: Website
  url: https://www.doppler.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.doppler.com
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.doppler.com/reference/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.doppler.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://dashboard.doppler.com/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DopplerHQ
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.doppler.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.doppler.com/blog/rss.xml
created: '2026-05-11'
description: Doppler is a centralized, cloud-based SecretOps platform that manages application configuration and secrets for humans, CI/CD pipelines, and AI agents across environments. It provides Git-style activity logs, rollbacks, webhooks, SDKs, and deep integrations with AWS, Azure, GCP, Kubernetes, and the major CI providers, with SOC 2 and ISO compliance. The Doppler REST API offers full programmatic control over projects, configs, secrets, tokens, service accounts, and audit logs using Bearer token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doppler.png
layout: provider
modified: '2026-05-11'
name: Doppler
nav: Providers
network: true
overview: 'Doppler publishes 8 APIs on the [APIs.io](https://apis.io/) network, including ActivityLogs API, Auth API, Configs API, and 5 more. Tagged areas include Secrets Management, SecretOps, DevOps, Configuration Management, and Security.


  Doppler''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 9 more developer resources.'
random_paper: 62
score:
  band: thin
  composite: 31.8
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 57.4
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doppler/refs/heads/main/screenshots/doppler-2026-06-20T180156.png
security:
- kind: authentication
  name: Doppler Authentication
  slug: doppler-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Doppler Domain Security
  slug: doppler-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Doppler Vulnerability Disclosure
  slug: doppler-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Doppler Trust Center
  slug: doppler-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: doppler
tags:
- Secrets Management
- SecretOps
- DevOps
- Configuration Management
- Security
- CI/CD
website: https://www.doppler.com
---
