---
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Emitrr Agentic Access
  operation_count: 26
  slug: emitrr-agentic-access
  summary_line: 26 operations · 19 acting
api_count: 1
apis:
- baseURL: https://dev-workflows-manager.emitrr.com
  baseurl_source: declared
  description: The Actions API from Emitrr — 3 operation(s) for actions.
  name: Emitrr Actions API
  slug: emitrr-actions-api
- baseURL: https://dev-workflows-manager.emitrr.com
  baseurl_source: declared
  description: The Branches API from Emitrr — 4 operation(s) for branches.
  name: Emitrr Branches API
  slug: emitrr-branches-api
- baseURL: https://dev-workflows-manager.emitrr.com
  baseurl_source: declared
  description: The Core API from Emitrr — 1 operation(s) for core.
  name: Emitrr Core API
  slug: emitrr-core-api
- baseURL: https://dev-workflows-manager.emitrr.com
  baseurl_source: declared
  description: The Filters API from Emitrr — 1 operation(s) for filters.
  name: Emitrr Filters API
  slug: emitrr-filters-api
- baseURL: https://dev-workflows-manager.emitrr.com
  baseurl_source: declared
  description: The Health API from Emitrr — 1 operation(s) for health.
  name: Emitrr Health API
  slug: emitrr-health-api
- baseURL: https://dev-workflows-manager.emitrr.com
  baseurl_source: declared
  description: The Triggers API from Emitrr — 2 operation(s) for triggers.
  name: Emitrr Triggers API
  slug: emitrr-triggers-api
- baseURL: https://dev-workflows-manager.emitrr.com
  baseurl_source: declared
  description: The Workflows API from Emitrr — 8 operation(s) for workflows.
  name: Emitrr Workflows API
  slug: emitrr-workflows-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/emitrr/agentic-access/emitrr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/emitrr-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/emitrr/rules/emitrr-rules.yml
  title: ''
  type: Spectral
  url: rules/emitrr-rules.yml
- group: design
  href: https://artifacts.apis.io/emitrr/vocabulary/emitrr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/emitrr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/emitrr/conformance/emitrr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/emitrr-conformance.yml
- group: other
  href: https://artifacts.apis.io/emitrr/hosts/emitrr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/emitrr-hosts.yml
- group: other
  href: https://artifacts.apis.io/emitrr/vendors/emitrr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/emitrr-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emitrr.com/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://emitrr.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emitrr.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://emitrr.com/blog/
- group: auth
  href: https://artifacts.apis.io/emitrr/security/emitrr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emitrr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://emitrr.com/
created: '2026-10-28'
description: Emitrr provides AI-powered communication tools for healthcare and other businesses, offering services such as texting, webchat, reviews, team messaging, VoIP phones, cloud faxing, AI agents, local numbers, online scheduling, digital forms, and more. Their platform aims to streamline patient engagement, improve operational efficiency, and enable 24/7 virtual assistance across various specialties.
image: https://emitrr.com/wp-content/uploads/2021/08/customer_journey-min.png
layout: provider
modified: '2026-10-28'
name: Emitrr
nav: Providers
network: true
overview: 'Emitrr publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actions API, Branches API, Core API, and 4 more. Tagged areas include Healthcare, AI, Communication, Messaging, and SaaS.


  The Emitrr catalog on APIs.io includes 1 Spectral governance ruleset.


  Emitrr''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Emitrr API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: emitrr-rules
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 35.6
    developer_ergonomics: 2.4
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Emitrr Domain Security
  slug: emitrr-domain-security
  summary_line: TLSv1.2 · DMARC
slug: emitrr
tags:
- Healthcare
- AI
- Communication
- Messaging
- SaaS
website: https://emitrr.com/
---
