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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/pelago-health/vendors/pelago-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pelago-health-vendors.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.pelagohealth.com/security/
- group: agent
  href: https://artifacts.apis.io/pelago-health/llms/pelago-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pelago-health-llms.txt
- group: auth
  href: https://artifacts.apis.io/pelago-health/well-known/pelago-health-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pelago-health-help-security.txt
- group: agent
  href: https://artifacts.apis.io/pelago-health/well-known/pelago-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pelago-health-well-known.yml
- group: other
  href: https://artifacts.apis.io/pelago-health/hosts/pelago-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pelago-health-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pelagohealth.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.pelagohealth.com/press/
- group: docs
  title: ''
  type: Documentation
  url: https://help.pelagohealth.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PelagoHealth
- group: auth
  href: https://artifacts.apis.io/pelago-health/security/pelago-health-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pelago-health-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/pelago-health/security/pelago-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pelago-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pelagohealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pelagohealth.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pelagohealth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pelagohealth.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.pelagohealth.com/company/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.pelagohealth.com/book-a-demo
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://help.pelagohealth.com/mcp
  - status: 403
    url: https://info.pelagohealth.com/mcp
  - status: 200
    url: https://www.pelagohealth.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Pelago is an AI‑led, clinician‑backed behavioral health platform that unites substance use, mental health, and behavioral addiction care. It offers personalized, private support for individuals and organizations, combining AI‑driven access with human clinical expertise to deliver tailored treatment pathways, wellness resources, and outcomes tracking.
image: https://pelagocms.wpengine.com/wp-content/uploads/2024/10/pelago_pr-1024x494.png
layout: provider
modified: '2026-10-21'
name: Pelago
nav: Providers
network: true
overview: 'Pelago is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, BehavioralHealth, MentalHealth, and SubstanceUse.


  Pelago''s developer surface includes documentation, engineering blog, support, signup flow, and 14 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pelago Health Domain Security
  slug: pelago-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pelago Health Trust Center
  slug: pelago-health-trust-center
  summary_line: HIPAA, GDPR
slug: pelago-health
tags:
- Company
- AI
- BehavioralHealth
- MentalHealth
- SubstanceUse
website: https://www.pelagohealth.com/
---
