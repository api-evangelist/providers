---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Rynse provides fleet washing APIs documented at the developer portal.
  name: Rynse API
  slug: rynse-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/rynse/llms/rynse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rynse-llms.txt
- group: other
  href: https://artifacts.apis.io/rynse/a2a/rynse-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/rynse-a2a.yml
- group: agent
  href: https://artifacts.apis.io/rynse/well-known/rynse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rynse-well-known.yml
- group: other
  href: https://artifacts.apis.io/rynse/hosts/rynse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rynse-hosts.yml
- group: other
  href: https://artifacts.apis.io/rynse/vendors/rynse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rynse-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.gorynse.com/security
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gorynse.com/rynse-web/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.gorynse.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gorynse
- group: auth
  href: https://artifacts.apis.io/rynse/security/rynse-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rynse-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/rynse/security/rynse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rynse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gorynse.com/
- group: company
  title: ''
  type: Blog
  url: https://www.gorynse.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.v2.gorynse.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gorynse.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gorynse.com/terms-of-service
coverage:
  checked: '2026-10-29'
  detail: Documentation is provided as markdown pages without a published OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://docs.gorynse.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Rynse provides a comprehensive fleet washing and vehicle care platform that connects fleet managers with a nationwide network of mobile and brick‑and‑mortar wash providers. The solution offers centralized billing, spend controls, fraud monitoring, and real‑time vehicle activity tracking, plus additional services such as fuel, EV charging, and maintenance, serving public and private sector fleets across the United States.
layout: provider
modified: '2026-10-29'
name: Rynse
nav: Providers
network: true
overview: 'Rynse is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fleet, Washing, VehicleCare, and SaaS.


  Rynse''s developer surface includes getting-started guide, documentation, engineering blog, and 13 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Rynse Domain Security
  slug: rynse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rynse Vulnerability Disclosure
  slug: rynse-vulnerability-disclosure
  summary_line: no policy recorded
slug: rynse
tags:
- Company
- Fleet
- Washing
- VehicleCare
- SaaS
website: https://www.gorynse.com/
---
