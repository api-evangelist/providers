---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DNS‑based blacklist API providing real‑time reputation data for IP addresses, enabling sites to block known spammers, harvesters, and abusive actors.
  name: HTTP:BL API
  slug: httpbl-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/project-honeypot/authentication/project-honeypot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/project-honeypot-authentication.yml
- group: design
  href: https://artifacts.apis.io/project-honeypot/errors/project-honeypot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/project-honeypot-problem-types.yml
- group: other
  href: https://artifacts.apis.io/project-honeypot/hosts/project-honeypot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/project-honeypot-hosts.yml
- group: auth
  href: https://artifacts.apis.io/project-honeypot/security/project-honeypot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/project-honeypot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://projecthoneypot.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.projecthoneypot.org/httpbl_api.php
- group: docs
  title: ''
  type: APIReference
  url: https://www.projecthoneypot.org/httpbl_api.php
- group: start
  title: ''
  type: GettingStarted
  url: https://projecthoneypot.org/create_account.php
- group: operate
  title: ''
  type: Support
  url: https://projecthoneypot.org/faq.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://projecthoneypot.org/terms_of_use.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://projecthoneypot.org/privacy_policy.php
- group: start
  title: ''
  type: SignUp
  url: https://projecthoneypot.org/create_account.php
coverage:
  checked: '2026-10-28'
  detail: Project Honey Pot provides only a DNS-based HTTP:BL API and no public developer program or machine‑readable API specifications.
  evidence:
  - status: 404
    url: https://projecthoneypot.org/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Project Honey Pot operates a collaborative anti‑spam network that tracks online fraud and abuse. By deploying “honeypot” traps on participating websites, it gathers data on malicious IP addresses, email harvesters, and spammers. The collected intelligence is made available via a public HTTP:BL DNS‑based API, allowing website owners and security tools to query the reputation of IPs in real time. The service aims to reduce spam, phishing, and other abusive activities across the web through community‑driven data sharing.
image: https://projecthoneypot.org/images/php_logo.gif
layout: provider
modified: '2026-10-28'
name: Project Honey Pot
nav: Providers
network: true
overview: 'Project Honey Pot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anti-Spam, Security, Community, Fraud Prevention, and Open Data.


  Project Honey Pot''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, and 6 more developer resources.'
plans:
- name: Project Honeypot Plans Pricing
  plan_count: 0
  slug: project-honeypot-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Project Honeypot Rate Limits
  slug: project-honeypot-rate-limits
scopes:
- name: Project Honeypot Scopes
  scope_count: 0
  slug: project-honeypot-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 24.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/project-honeypot/project-honeypot-2026-11-03T141535.png
security:
- kind: authentication
  name: Project Honeypot Authentication
  slug: project-honeypot-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Project Honeypot Domain Security
  slug: project-honeypot-domain-security
  summary_line: TLSv1.3 · HSTS
slug: project-honeypot
tags:
- Anti-Spam
- Security
- Community
- Fraud Prevention
- Open Data
website: https://projecthoneypot.org/
---
