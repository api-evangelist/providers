---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Leave management API
  name: TiLT API
  slug: tilt-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/hellotilt-com/plans/hellotilt-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hellotilt-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://hellotilt.com/security/
- group: other
  href: https://artifacts.apis.io/hellotilt-com/hosts/hellotilt-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hellotilt-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/hellotilt-com/vendors/hellotilt-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hellotilt-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://hellotilt.com/security/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hellotilt.com/
- group: auth
  href: https://artifacts.apis.io/hellotilt-com/security/hellotilt-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hellotilt-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hellotilt-com/security/hellotilt-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hellotilt-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hellotilt-com/security/hellotilt-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hellotilt-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hellotilt.com/
- group: company
  title: ''
  type: Blog
  url: https://hellotilt.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://hellotilt.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hellotilt.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hellotilt.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://hellotilt.com/platform/premium-support/
coverage:
  checked: '2026-10-29'
  detail: Developer portal requires login to access API documentation and specifications.
  evidence:
  - status: 200
    url: https://developer.hellotilt.com/login/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Tilt is a leave management platform that helps companies manage employee leave in-house. The service offers a suite of tools including a leave planner, HR reporting dashboard, and integration capabilities. Tilt emphasizes a human-centered approach to leave, providing resources such as research guides, case studies, and a blog. It offers pricing plans, broker partnerships, and a demo request option. The platform aims to simplify leave administration while ensuring compliance and employee satisfaction.
image: https://hellotilt.com/wp-content/uploads/2026/08/HR-Reporting-Dashboard-Hero.png
layout: provider
modified: '2026-10-29'
name: TiLT
nav: Providers
network: true
overview: 'TiLT is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HR, LeaveManagement, SaaS, and Platform.


  TiLT''s developer surface includes documentation, engineering blog, pricing, support, and 11 more developer resources.'
plans:
- name: Hellotilt Com Plans Pricing
  plan_count: 2
  slug: hellotilt-com-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hellotilt Com Domain Security
  slug: hellotilt-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hellotilt Com Vulnerability Disclosure
  slug: hellotilt-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Hellotilt Com Trust Center
  slug: hellotilt-com-trust-center
  summary_line: SOC 2
slug: hellotilt-com
tags:
- Company
- HR
- LeaveManagement
- SaaS
- Platform
website: https://hellotilt.com/
---
