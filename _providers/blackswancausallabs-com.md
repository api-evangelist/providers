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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/blackswancausallabs-com/hosts/blackswancausallabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackswancausallabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blackswancausallabs-com/vendors/blackswancausallabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blackswancausallabs-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blackswancausallabs.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blackswancausallabs.com/privacy.html
- group: auth
  href: https://artifacts.apis.io/blackswancausallabs-com/security/blackswancausallabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackswancausallabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blackswancausallabs.com/
- group: company
  title: ''
  type: Blog
  url: https://blackswancausallabs.com/blog.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/black-swan-causal-labs
- group: docs
  title: ''
  type: Documentation
  url: https://blackswancausallabs.com/methodology.html
- group: operate
  title: ''
  type: Support
  url: https://blackswancausallabs.com/#contact
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is published; the site provides only HTML documentation.
  evidence:
  - status: 200
    url: https://blackswancausallabs.com/
  - status: 0
    url: https://api.blackswancausallabs.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Black Swan Causal Labs provides software and methods for real‑world evidence generation, focusing on causal reasoning, study design, evidence assessment, and regulatory intelligence. Their tools integrate domain expertise with AI to help researchers inspect, review, and apply causal inference in healthcare and related fields, aiming to improve decision‑making and policy development.
layout: provider
modified: '2026-10-29'
name: blackswancausallabs-com
nav: Providers
network: true
overview: 'blackswancausallabs-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Healthcare, CausalInference, and RealWorldEvidence.


  blackswancausallabs-com''s developer surface includes engineering blog, documentation, support, and 7 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blackswancausallabs Com Domain Security
  slug: blackswancausallabs-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: blackswancausallabs-com
tags:
- Company
- AI
- Healthcare
- CausalInference
- RealWorldEvidence
website: https://blackswancausallabs.com/
---
