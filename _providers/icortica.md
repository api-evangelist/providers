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
- group: agent
  href: https://artifacts.apis.io/icortica/llms/icortica-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/icortica-llms.txt
- group: other
  href: https://artifacts.apis.io/icortica/hosts/icortica-hosts.yml
  title: ''
  type: Hosts
  url: hosts/icortica-hosts.yml
- group: other
  href: https://artifacts.apis.io/icortica/vendors/icortica-vendors.yml
  title: ''
  type: Vendors
  url: vendors/icortica-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.icortica.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.icortica.com/blog
- group: auth
  href: https://artifacts.apis.io/icortica/security/icortica-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/icortica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.icortica.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.icortica.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: icortica provides a B2B SaaS platform that gives dental laboratories and distributors a 360‑degree view of customer relationships. The solution transforms scattered customer data into predictive insights, risk and opportunity alerts, and automated workflows to help sales, marketing, and customer‑success teams increase retention and revenue. It offers dashboards, AI‑driven action recommendations, and playbooks to guide users in cross‑selling and account management.
image: https://www.icortica.com/_astro/icortica-share.X88Qgg_6_Z1PL7UX.webp?dpl=6ad7ca275e8fef6c069d4aea
layout: provider
modified: '2026-10-24'
name: icortica
nav: Providers
network: true
overview: 'icortica is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Intelligence, Dental Laboratories, Retention, and Predictive Analytics.


  icortica''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Icortica Domain Security
  slug: icortica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: icortica
tags:
- Customer Intelligence
- Dental Laboratories
- Retention
- Predictive Analytics
website: https://www.icortica.com/
---
