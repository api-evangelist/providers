---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dxc Technology Agentic Access
  operation_count: 2
  slug: dxc-technology-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://developer.dxc.com
  baseurl_source: declared
  description: Integration and connectivity services
  name: DXC Technology Integration API
  slug: dxc-technology-integration-api
- baseURL: https://developer.dxc.com
  baseurl_source: declared
  description: Platform service operations
  name: DXC Technology Platform API
  slug: dxc-technology-platform-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DXC Developer Central API
  slug: open-dxc-developer-central-api
- collection_type: open
  name: DXC Developer Central Integration API
  slug: open-dxc-technology-integration-api
- collection_type: open
  name: DXC Developer Central Integration Platform API
  slug: open-dxc-technology-platform-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dxc-technology/refs/heads/main/plans/dxc-technology-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dxc-technology-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dxc-technology/refs/heads/main/rate-limits/dxc-technology-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dxc-technology-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dxc-technology/refs/heads/main/finops/dxc-technology-finops.yml
  title: ''
  type: FinOps
  url: finops/dxc-technology-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://dxc.com/solutions/engineering
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dxc-technology/refs/heads/main/agentic-access/dxc-technology-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dxc-technology-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dxc-technology/refs/heads/main/security/dxc-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dxc-technology-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dxc-technology/refs/heads/main/authentication/dxc-technology-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dxc-technology-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://dxc.com
- group: start
  title: ''
  type: Portal
  url: https://developer.dxc.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dxc-technology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dxctechnology/
created: '2026-03-21'
description: DXC Technology is a global IT services company that helps clients harness the power of innovation to thrive on change, providing application services, business process services, cloud, and security solutions.
finops:
- has_sources: true
  method: generated
  name: Dxc Technology Finops
  primary_unit: ''
  service_category: IT Services
  slug: dxc-technology-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dxc-technology.png
layout: provider
modified: '2026-10-06'
name: DXC Technology
nav: Providers
network: true
overview: 'DXC Technology publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Integration API and Platform API. Tagged areas include IT Services, Enterprise, Platform, and Integration.


  DXC Technology''s developer surface includes engineering blog, authentication, developer portal, and 8 more developer resources.'
plans:
- name: Dxc Technology Plans Pricing
  plan_count: 1
  slug: dxc-technology-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Dxc Technology Rate Limits
  slug: dxc-technology-rate-limits
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 48.4
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 26.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/dxc-technology/refs/heads/main/screenshots/dxc-technology-2026-06-20T180335.png
security:
- kind: authentication
  name: Dxc Technology Authentication
  slug: dxc-technology-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dxc Technology Domain Security
  slug: dxc-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dxc-technology
tags:
- IT Services
- Enterprise
- Platform
- Integration
website: https://dxc.com
---
