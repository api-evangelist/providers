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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avantifinancialgroup/refs/heads/main/hosts/avantifinancialgroup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avantifinancialgroup-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avantifinancialgroup.com/privacy-policy.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avantifinancialgroup/refs/heads/main/security/avantifinancialgroup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avantifinancialgroup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avantifinancialgroup.com
- group: company
  title: ''
  type: Blog
  url: https://avantifinancialgroup.com/blog.html
- group: docs
  title: ''
  type: Documentation
  url: https://avantifinancialgroup.com/about-us.html
- group: operate
  title: ''
  type: Support
  url: https://avantifinancialgroup.com/contact.html
coverage:
  checked: 2026-09-26
  detail: Avantifinancialgroup provides insurance services and does not expose a software API.
  evidence:
  - status: 200
    url: https://avantifinancialgroup.com/about-us.html
  reason: not-a-software-company
  state: none
created: '2026-09-26'
description: Avantifinancialgroup, operating as AVANTI FINANCIAL GROUP, provides a broad range of insurance and risk management solutions including commercial property, construction, homeowners, life, and business owners policies. Based in the United States, the company serves individuals and businesses seeking tailored coverage and risk mitigation services across multiple industries. The firm emphasizes personalized service, comprehensive policy options, and expertise in navigating complex insurance needs for both residential and commercial clients, ensuring reliable protection and peace of mind.
layout: provider
modified: '2026-09-26'
name: Avantifinancialgroup
nav: Providers
network: true
overview: 'Avantifinancialgroup is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Risk Management, Financial Services, and US.


  Avantifinancialgroup''s developer surface includes engineering blog, documentation, support, and 4 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 8.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avantifinancialgroup Domain Security
  slug: avantifinancialgroup-domain-security
  summary_line: TLSv1.3
slug: avantifinancialgroup
tags:
- Company
- Insurance
- Risk Management
- Financial Services
- US
website: https://avantifinancialgroup.com
---
