---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Mockoon Agentic Access
  operation_count: 3
  slug: mockoon-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: Mockoon ships as a desktop application, a CLI, and a serverless package for designing and running mock REST APIs. Mocks are configured in Mockoon and exposed locally as HTTP endpoints; the tool itself
  name: Mockoon
  slug: mockoon
- baseURL_template: http://localhost:{port}
  baseurl_source: spec_template
  description: Inspect and reset data buckets defined in the mock environment.
  name: Mockoon Data Buckets API
  slug: mockoon-data-buckets-api
artifact_total: 11
collections:
- collection_type: open
  name: Mockoon Admin Data Buckets API
  slug: open-mockoon-data-buckets-api
- collection_type: open
  name: Mockoon Admin API
  slug: open-mockoon
common:
- group: commercial
  href: https://artifacts.apis.io/mockoon/plans/mockoon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mockoon-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mockoon/rate-limits/mockoon-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mockoon-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mockoon/finops/mockoon-finops.yml
  title: ''
  type: FinOps
  url: finops/mockoon-finops.yml
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
  href: https://artifacts.apis.io/mockoon/agentic-access/mockoon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mockoon-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mockoon/security/mockoon-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mockoon-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mockoon/security/mockoon-domain-security.yml
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
- has_sources: false
  method: generated
  name: Mockoon Finops
  primary_unit: request
  service_category: API
  slug: mockoon-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mockoon.png
layout: provider
modified: '2026-04-28'
name: Mockoon
nav: Providers
network: true
overview: 'Mockoon publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data Buckets API, and 1 more. Tagged areas include Mock Servers, Mocking, Testing, REST API, and Desktop.


  The Mockoon catalog on APIs.io includes 1 Spectral governance ruleset.


  Mockoon''s developer surface includes documentation, engineering blog, and 16 more developer resources.'
plans:
- name: Mockoon Plans Pricing
  plan_count: 3
  slug: mockoon-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Mockoon Rate Limits
  slug: mockoon-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Mockoon API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: mockoon-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 41.6
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/mockoon/mockoon-2026-06-20T185637.png
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
