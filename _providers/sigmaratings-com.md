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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/sigmaratings-com/hosts/sigmaratings-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sigmaratings-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sigmaratings-com/vendors/sigmaratings-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sigmaratings-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sigma360.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.sigma360.com/knowledge/press/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sigma360.com/
- group: auth
  href: https://artifacts.apis.io/sigmaratings-com/security/sigmaratings-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sigmaratings-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sigmaratings.com/
coverage:
  checked: '2026-10-24'
  detail: Sigma Ratings developer pages return JavaScript-rendered HTML with no machine-readable API spec.
  evidence:
  - status: 200
    url: https://www.sigma360.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Sigma Ratings, operating as Sigma360, provides an AI‑powered financial crime compliance automation platform that streamlines KYC, AML, and risk management processes. The solution offers real‑time risk coverage, reduces false positives by up to 93%, and integrates with existing financial systems to help institutions meet regulatory requirements efficiently.
image: https://www.sigma360.com/wp-content/uploads/2023/01/logo.png
layout: provider
modified: '2026-10-24'
name: Sigma Ratings
nav: Providers
network: true
overview: 'Sigma Ratings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, Compliance, AI, and RiskManagement.


  Sigma Ratings'' developer surface includes documentation and 6 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sigmaratings Com Domain Security
  slug: sigmaratings-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sigmaratings-com
tags:
- Company
- FinTech
- Compliance
- AI
- RiskManagement
website: https://sigmaratings.com/
---
