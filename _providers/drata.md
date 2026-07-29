---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 7
  human_in_the_loop: 0
  name: Drata Agentic Access
  operation_count: 21
  slug: drata-agentic-access
  summary_line: 21 operations · 7 acting
api_count: 15
apis:
- description: Public REST API for managing controls, frameworks, evidence, personnel, assets, policies, and tests. v2 expands endpoints and improves data structures over v1.
  name: Drata Public API v2
  slug: public-api-v2
- description: Build custom integrations to automate evidence collection from any internal or third-party system.
  name: Drata Custom Connections API
  slug: custom-connections
- description: Manage SafeBase trust centers and security questionnaires programmatically; acquired by Drata and now part of the Drata platform.
  name: SafeBase Trust API
  slug: safebase-trust-api
- description: Model Context Protocol server enabling AI agents to interact with Drata for compliance workflows.
  name: Drata MCP Server
  slug: mcp
- description: The Assets API from Drata — 2 operation(s) for assets.
  name: Drata Assets API
  slug: drata-assets-api
- description: The Audits API from Drata — 1 operation(s) for audits.
  name: Drata Audits API
  slug: drata-audits-api
- description: The Controls API from Drata — 2 operation(s) for controls.
  name: Drata Controls API
  slug: drata-controls-api
- description: The Evidence Library API from Drata — 1 operation(s) for evidence library.
  name: Drata Evidence Library API
  slug: drata-evidence-library-api
- description: The Frameworks API from Drata — 1 operation(s) for frameworks.
  name: Drata Frameworks API
  slug: drata-frameworks-api
- description: The Monitoring Tests API from Drata — 1 operation(s) for monitoring tests.
  name: Drata Monitoring Tests API
  slug: drata-monitoring-tests-api
- description: The Personnel API from Drata — 2 operation(s) for personnel.
  name: Drata Personnel API
  slug: drata-personnel-api
- description: The Policies API from Drata — 1 operation(s) for policies.
  name: Drata Policies API
  slug: drata-policies-api
- description: The Risks API from Drata — 1 operation(s) for risks.
  name: Drata Risks API
  slug: drata-risks-api
- description: The Tasks API from Drata — 1 operation(s) for tasks.
  name: Drata Tasks API
  slug: drata-tasks-api
- description: The Vendors API from Drata — 1 operation(s) for vendors.
  name: Drata Vendors API
  slug: drata-vendors-api
artifact_total: 24
collections:
- collection_type: open
  name: Drata Public API v2
  slug: open-drata
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/drata-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/drata-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/drata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/drata-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/drata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drata
- group: company
  title: ''
  type: Website
  url: https://drata.com/
- group: other
  title: ''
  type: Developer
  url: https://developers.drata.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/drata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/drata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/drata-finops.yml
created: '2026-05-08'
description: Drata is a continuous security and compliance automation platform supporting SOC 2, ISO 27001, HIPAA, PCI DSS, GDPR, and more, with policies, evidence, and trust center. Drata exposes a public REST API plus the SafeBase Trust API (acquired) and a Custom Connections framework for evidence collection.
finops:
- name: Drata Finops
  service_category: GRC
  slug: drata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drata.png
layout: provider
modified: '2026-05-08'
name: Drata
nav: Providers
network: true
overview: 'Drata publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Audits API, Controls API, and 8 more. Tagged areas include GRC, Compliance, SOC 2, ISO 27001, and Security.


  Drata''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Drata Plans Pricing
  plan_count: 1
  slug: drata-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 1
  name: Drata Rate Limits
  slug: drata-rate-limits
score:
  band: thin
  composite: 32.8
  delta: -1.7
  facets:
    commercial_clarity: 36.8
    contract_quality: 53.4
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drata/refs/heads/main/screenshots/drata-2026-06-20T180244.png
security:
- kind: authentication
  name: Drata Authentication
  slug: drata-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Drata Domain Security
  slug: drata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Drata Vulnerability Disclosure
  slug: drata-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Drata Trust Center
  slug: drata-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR
slug: drata
tags:
- GRC
- Compliance
- SOC 2
- ISO 27001
- Security
website: https://drata.com/
---
