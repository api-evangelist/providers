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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Mabl Agentic Access
  operation_count: 36
  slug: mabl-agentic-access
  summary_line: 36 operations · 18 acting
api_count: 11
apis:
- description: Manage resources in your workspace programmatically with the mabl API. By integrating mabl API endpoints into your workflow, you can manage tests, runs, environments, applications, plans, deployments,
  name: Mabl API
  slug: mabl-api
- description: The Applications API from Mabl — 2 operation(s) for applications.
  name: Mabl Applications API
  slug: mabl-applications-api
- description: The Credentials API from Mabl — 2 operation(s) for credentials.
  name: Mabl Credentials API
  slug: mabl-credentials-api
- description: The Database Connections API from Mabl — 2 operation(s) for database connections.
  name: Mabl Database Connections API
  slug: mabl-database-connections-api
- description: The Deployment Events API from Mabl — 2 operation(s) for deployment events.
  name: Mabl Deployment Events API
  slug: mabl-deployment-events-api
- description: The Environments API from Mabl — 2 operation(s) for environments.
  name: Mabl Environments API
  slug: mabl-environments-api
- description: The Flows API from Mabl — 1 operation(s) for flows.
  name: Mabl Flows API
  slug: mabl-flows-api
- description: The Issues API from Mabl — 2 operation(s) for issues.
  name: Mabl Issues API
  slug: mabl-issues-api
- description: The Test Runs API from Mabl — 3 operation(s) for test runs.
  name: Mabl Test Runs API
  slug: mabl-test-runs-api
- description: The Tests API from Mabl — 1 operation(s) for tests.
  name: Mabl Tests API
  slug: mabl-tests-api
- description: The Users API from Mabl — 1 operation(s) for users.
  name: Mabl Users API
  slug: mabl-users-api
artifact_total: 19
collections:
- collection_type: open
  name: mabl API
  slug: open-mabl
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mabl-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mabl-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mabl-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mabl-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mablhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mabl
- group: company
  title: ''
  type: Website
  url: https://www.mabl.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.mabl.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.help.mabl.com/reference/intro-to-the-mabl-api
- group: agent
  title: ''
  type: LlmsText
  url: https://api.help.mabl.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.mabl.com/blog/rss.xml
created: '2025-01-08'
description: mabl, the leading AI-native test automation platform, empowers software teams to accelerate innovation while ensuring exceptional quality. Their unified platform streamlines testing across web, mobile, API, accessibility, and performance, enabling teams to release faster with confidence. Trusted by industry leaders like Microsoft, Charles Schwab, and JetBlue, mabl transforms how teams approach software quality.
finops:
- name: Mabl Finops
  service_category: API
  slug: mabl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mabl.png
layout: provider
modified: '2026-04-28'
name: Mabl
nav: Providers
network: true
overview: 'Mabl publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Credentials API, Database Connections API, and 7 more. Tagged areas include Test Automation, QA, DevOps, AI Testing, and Platform.


  Mabl''s developer surface includes authentication, documentation, API reference, engineering blog, and 7 more developer resources.'
plans:
- name: Mabl Plans Pricing
  plan_count: 3
  slug: mabl-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Mabl Rate Limits
  slug: mabl-rate-limits
score:
  band: thin
  composite: 39.8
  delta: -1.7
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.4
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mabl/refs/heads/main/screenshots/mabl-2026-06-20T184832.png
security:
- kind: authentication
  name: Mabl Authentication
  slug: mabl-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mabl Domain Security
  slug: mabl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mabl Trust Center
  slug: mabl-trust-center
  summary_line: SOC 2
slug: mabl
tags:
- Test Automation
- QA
- DevOps
- AI Testing
- Platform
website: https://www.mabl.com
---
