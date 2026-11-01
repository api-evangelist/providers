---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/conduitly/plans/conduitly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/conduitly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/conduitly/conformance/conduitly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/conduitly-conformance.yml
- group: other
  href: https://artifacts.apis.io/conduitly/hosts/conduitly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conduitly-hosts.yml
- group: other
  href: https://artifacts.apis.io/conduitly/vendors/conduitly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/conduitly-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.conduitly.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://help.conduitly.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.conduitly.com/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.conduitly.com/category/4-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.conduitly.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/conduitly
- group: auth
  href: https://artifacts.apis.io/conduitly/security/conduitly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conduitly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conduitly.com/
created: '2026-10-20'
description: Conduitly provides a platform that connects and automates data flow between business applications. It enables companies to integrate various SaaS tools, automate repetitive tasks, and streamline workflows without manual data entry. By offering a wide range of integrations across HR, payroll, sales, marketing, and more, Conduitly helps businesses reduce busywork, improve efficiency, and focus on core activities. The service includes customizable automation, a marketplace of pre-built connectors, and tools for building custom integrations, aiming to accelerate work and eliminate duplicate data entry.
layout: provider
modified: '2026-10-20'
name: Conduitly
nav: Providers
network: true
overview: 'Conduitly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Integrations, Automation, Workflow, and Business Software.


  Conduitly''s developer surface includes support, getting-started guide, documentation, and 9 more developer resources.'
plans:
- name: Conduitly Plans Pricing
  plan_count: 8
  slug: conduitly-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 12.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 35.7
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Conduitly Domain Security
  slug: conduitly-domain-security
  summary_line: TLSv1.3 · DMARC
slug: conduitly
tags:
- Integrations
- Automation
- Workflow
- Business Software
website: https://conduitly.com/
---
