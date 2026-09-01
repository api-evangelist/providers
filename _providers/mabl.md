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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Mabl Agentic Access
  operation_count: 36
  slug: mabl-agentic-access
  summary_line: 36 operations · 18 acting
api_count: 1
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
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: mabl Applications API
  slug: open-mabl-applications-api
- collection_type: open
  name: mabl Applications Credentials API
  slug: open-mabl-credentials-api
- collection_type: open
  name: mabl Applications Database Connections API
  slug: open-mabl-database-connections-api
- collection_type: open
  name: mabl Applications Deployment Events API
  slug: open-mabl-deployment-events-api
- collection_type: open
  name: mabl Applications Environments API
  slug: open-mabl-environments-api
- collection_type: open
  name: mabl Applications Flows API
  slug: open-mabl-flows-api
- collection_type: open
  name: mabl Applications Issues API
  slug: open-mabl-issues-api
- collection_type: open
  name: mabl Applications Test Runs API
  slug: open-mabl-test-runs-api
- collection_type: open
  name: mabl Applications Tests API
  slug: open-mabl-tests-api
- collection_type: open
  name: mabl Applications Users API
  slug: open-mabl-users-api
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
random_paper: 13
rate_limits:
- limit_count: 5
  name: Mabl Rate Limits
  slug: mabl-rate-limits
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 27.4
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
