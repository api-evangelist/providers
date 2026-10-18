---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 5
apis:
- description: Magma is a next-generation packet core that delivers cellular network innovation at lower cost of ownership, with REST and gRPC APIs for orchestration, subscriber management, and policy enforcement.
  name: Magma
  slug: magma
- description: Terragraph is a wireless technology that enables internet service providers to deliver gigabit-speed last-mile access to homes, enterprises, and multi-dwelling buildings cost-effectively.
  name: Terragraph
  slug: terragraph
- description: Open M-Plane is a software component of Meta's Evenstar hardware design for configuration and management of the Radio Access Network (RAN).
  name: Open M-Plane
  slug: open-mplane
- description: Maveric is a platform that uses AI/ML to provide realistic cellular network simulations and reference examples demonstrating their use.
  name: Maveric
  slug: maveric
- description: ISP Toolbox empowers ISP operators with products, tools, and resources to better plan, analyze, and run their broadband businesses.
  name: ISP Toolbox
  slug: isp-toolbox
artifact_total: 9
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lf-connectivity/refs/heads/main/plans/lf-connectivity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lf-connectivity-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lf-connectivity/refs/heads/main/rate-limits/lf-connectivity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lf-connectivity-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lf-connectivity/refs/heads/main/finops/lf-connectivity-finops.yml
  title: ''
  type: FinOps
  url: finops/lf-connectivity-finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/magma/magma/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/magma/magma/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/magma/magma/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/magma/magma/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/magma/magma/blob/master/CONTRIBUTING.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lf-connectivity/refs/heads/main/security/lf-connectivity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lf-connectivity-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://lfconnectivity.dev/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/lf-connectivity
- group: company
  title: ''
  type: Website
  url: https://lfconnectivity.dev/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/magma
- group: company
  title: ''
  type: Blog
  url: https://magmacore.org/feed/
created: '2026-03-16'
description: LF Connectivity is a Linux Foundation umbrella initiative, launched with Meta, that improves access to networks through open source projects. Sub-projects include Magma (a next-generation packet core), Terragraph (gigabit wireless last-mile access), Open M-Plane (RAN configuration and management), Maveric (AI/ML cellular network simulations), and the ISP Toolbox (planning and analytics for ISP operators).
finops:
- has_sources: false
  method: generated
  name: Lf Connectivity Finops
  primary_unit: ''
  service_category: API
  slug: lf-connectivity-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lf-connectivity.png
layout: provider
modified: '2026-04-28'
name: LF Connectivity
nav: Providers
network: true
overview: 'LF Connectivity is listed with 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Connectivity, Linux Foundation, Networking, Telecommunications, and Wireless.


  LF Connectivity''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Lf Connectivity Plans Pricing
  plan_count: 3
  slug: lf-connectivity-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Lf Connectivity Rate Limits
  slug: lf-connectivity-rate-limits
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 62.5
    operational_transparency: 39.5
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 5.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/lf-connectivity/refs/heads/main/screenshots/lf-connectivity-2026-06-20T184450.png
security:
- kind: domain-security
  name: Lf Connectivity Domain Security
  slug: lf-connectivity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lf-connectivity
tags:
- Connectivity
- Linux Foundation
- Networking
- Telecommunications
- Wireless
- 5G
- Open Source
website: https://lfconnectivity.dev/
---
