---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 18.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/earnest-research/well-known/earnest-research-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/earnest-research-well-known.yml
- group: other
  href: https://artifacts.apis.io/earnest-research/hosts/earnest-research-hosts.yml
  title: ''
  type: Hosts
  url: hosts/earnest-research-hosts.yml
- group: other
  href: https://artifacts.apis.io/earnest-research/vendors/earnest-research-vendors.yml
  title: ''
  type: Vendors
  url: vendors/earnest-research-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.earnestanalytics.com/terms-of-use
- group: start
  title: ''
  type: SignUp
  url: https://dash.earnestanalytics.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.earnestanalytics.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.earnestanalytics.com/press
- group: docs
  title: ''
  type: Documentation
  url: https://docs.earnestresearch.com/
- group: auth
  href: https://artifacts.apis.io/earnest-research/security/earnest-research-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/earnest-research-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.earnestanalytics.com
coverage:
  checked: '2026-10-25'
  detail: Docs subdomain redirects to Okta login requiring authentication.
  evidence:
  - status: 302
    url: https://docs.earnestresearch.com
  reason: partner-login
  state: gated
created: '2026-10-25'
description: Earnest Research provides data-driven insights and analytics for financial markets, leveraging advanced statistical models and machine learning to help investors make informed decisions. The company offers a suite of APIs delivering real-time market data, historical datasets, and analytical tools, enabling seamless integration into trading platforms and research workflows. Backed by Bonfire Ventures, Earnest Research focuses on transparency, accuracy, and actionable intelligence for the investment community.
image: https://www.earnestanalytics.com/wp-content/uploads/2022/11/earnest-analytics.png
layout: provider
modified: '2026-10-25'
name: Earnest Research
nav: Providers
network: true
overview: 'Earnest Research is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Data, Analytics, and APIs.


  Earnest Research''s developer surface includes signup flow, documentation, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
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
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Earnest Research Domain Security
  slug: earnest-research-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: earnest-research
tags:
- Company
- Finance
- Data
- Analytics
- APIs
website: https://www.earnestanalytics.com
---
