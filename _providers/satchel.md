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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/satchel/llms/satchel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/satchel-llms.txt
- group: auth
  href: https://artifacts.apis.io/satchel/well-known/satchel-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/satchel-help-security.txt
- group: agent
  href: https://artifacts.apis.io/satchel/well-known/satchel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/satchel-well-known.yml
- group: other
  href: https://artifacts.apis.io/satchel/hosts/satchel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/satchel-hosts.yml
- group: other
  href: https://artifacts.apis.io/satchel/vendors/satchel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/satchel-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teamsatchel.com/legals/terms.html
- group: operate
  title: ''
  type: Support
  url: https://help.teamsatchel.com/en/articles/2904595-satchel-and-gdpr-compliance
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teamsatchel.com/legals/privacy_notice.html
- group: company
  title: ''
  type: Blog
  url: https://blog.teamsatchel.com
- group: start
  title: ''
  type: GettingStarted
  url: https://help.satchelone.com/en/articles/11065949-assessment-setup
- group: docs
  title: ''
  type: Documentation
  url: https://help.teamsatchel.com/
- group: auth
  href: https://artifacts.apis.io/satchel/security/satchel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/satchel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.teamsatchel.com/
coverage:
  checked: '2026-10-29'
  detail: No public developer program or API documentation was found on Satchel's website or API subdomains.
  evidence:
  - status: 200
    url: https://www.teamsatchel.com/
  - status: null
    url: https://api.teamsatchel.com/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Satchel provides the award‑winning Show My Homework platform and the Satchel One learning suite, helping schools and teachers streamline homework tracking, attendance, timetables and classroom management. Based in London, the company focuses on reducing teacher workload through a SaaS solution that integrates behavior monitoring, content delivery and wellbeing tools for educators.
image: https://www.teamsatchel.com/assets/images/sticky-logo.png
layout: provider
modified: '2026-10-29'
name: Satchel
nav: Providers
network: true
overview: 'Satchel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, SaaS, and LearningPlatform.


  Satchel''s developer surface includes support, engineering blog, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 0
  name: Satchel Rate Limits
  slug: satchel-rate-limits
scopes:
- name: Satchel Scopes
  scope_count: 0
  slug: satchel-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Satchel Authentication
  slug: satchel-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Satchel Domain Security
  slug: satchel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: satchel
tags:
- Company
- Education
- EdTech
- SaaS
- LearningPlatform
- HomeworkManagement
- UK
website: https://www.teamsatchel.com/
---
