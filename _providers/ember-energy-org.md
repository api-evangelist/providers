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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Programmatic access to Ember's open electricity datasets
  name: Ember Data API
  slug: ember-data-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ember-energy-org/refs/heads/main/conformance/ember-energy-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ember-energy-org-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ember-energy-org/refs/heads/main/llms/ember-energy-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ember-energy-org-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ember-energy-org/refs/heads/main/hosts/ember-energy-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ember-energy-org-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ember-energy-org/refs/heads/main/vendors/ember-energy-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ember-energy-org-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ember-energy.org/privacy-policy/
- group: docs
  title: ''
  type: APIReference
  url: https://api.ember-energy.org/v1/docs
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ember-energy-org/refs/heads/main/security/ember-energy-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ember-energy-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ember-energy.org
created: '2026-10-14'
description: Ember is a global climate and energy data analytics organization that provides independent research, policy analysis, and data tools to track the clean energy transition. It offers detailed insights on electricity markets, renewable integration, coal mine methane, and energy security across more than 30 countries, supporting policymakers, investors, and the public with up-to-date, evidence‑based information.
image: https://ember-energy.org/app/uploads/2024/08/AdobeStock_484921441-scaled.jpeg
layout: provider
modified: '2026-10-14'
name: Ember
nav: Providers
network: true
overview: 'Ember is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy Think Tank, Clean Energy Data, Policy Analysis, Electricity Datasets, and Open Data.


  Ember''s developer surface includes API reference and 7 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ember Energy Org Domain Security
  slug: ember-energy-org-domain-security
  summary_line: TLSv1.3
slug: ember-energy-org
tags:
- Energy Think Tank
- Clean Energy Data
- Policy Analysis
- Electricity Datasets
- Open Data
- Research
- Energy Transition
website: https://ember-energy.org
---
