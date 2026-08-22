---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
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
  score: 20.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Mockoon Agentic Access
  operation_count: 3
  slug: mockoon-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 2
apis:
- description: Mockoon ships as a desktop application, a CLI, and a serverless package for designing and running mock REST APIs. Mocks are configured in Mockoon and exposed locally as HTTP endpoints; the tool itself
  name: Mockoon
  slug: mockoon
- description: Inspect and reset data buckets defined in the mock environment.
  name: Mockoon Data Buckets API
  slug: mockoon-data-buckets-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mockoon Admin Data Buckets API
  slug: open-mockoon-data-buckets-api
- collection_type: open
  name: Mockoon Admin API
  slug: open-mockoon
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/mockoon/mockoon/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/mockoon/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/mockoon/mockoon/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/mockoon/mockoon/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mockoon-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mockoon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mockoon-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mockoon
- group: company
  title: ''
  type: Website
  url: https://mockoon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mockoon.com/docs/latest/about/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mockoon
- group: learn
  title: ''
  type: Tutorials
  url: https://mockoon.com/tutorials/
- group: company
  title: ''
  type: Blog
  url: https://mockoon.com/blog/
- group: operate
  title: ''
  type: Issues
  url: https://github.com/mockoon/mockoon/issues
- group: agent
  title: ''
  type: LlmsText
  url: https://mockoon.com/llms.txt
created: '2025-01-08'
description: Mockoon is the easiest and quickest way to design and run mock REST APIs. Available as a free, open-source desktop application and CLI, it lets developers build, share, and serve realistic mock endpoints locally, in CI, or in containers. No remote deployment, no account required.
finops:
- name: Mockoon Finops
  service_category: API
  slug: mockoon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mockoon.png
layout: provider
modified: '2026-04-28'
name: Mockoon
nav: Providers
network: true
overview: 'Mockoon publishes 1 API on the [APIs.io](https://apis.io/) network: Data Buckets API. Tagged areas include Mock Servers, Mocking, Testing, REST API, and Desktop.


  Mockoon''s developer surface includes documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Mockoon Plans Pricing
  plan_count: 3
  slug: mockoon-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Mockoon Rate Limits
  slug: mockoon-rate-limits
score:
  band: thin
  composite: 28.4
  delta: -1.6
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 30.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mockoon/refs/heads/main/screenshots/mockoon-2026-06-20T185637.png
security:
- kind: domain-security
  name: Mockoon Domain Security
  slug: mockoon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Mockoon Trust Center
  slug: mockoon-trust-center
  summary_line: PCI DSS, GDPR
slug: mockoon
tags:
- Mock Servers
- Mocking
- Testing
- REST API
- Desktop
- CLI
- Platform
- Open Source
website: https://mockoon.com/
---
