---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/repl-it/llms/repl-it-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/repl-it-llms.txt
- group: auth
  title: ''
  type: Compliance
  url: https://replit.com/security
- group: auth
  href: https://artifacts.apis.io/repl-it/security/repl-it-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/repl-it-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/repl-it/a2a/repl-it-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/repl-it-a2a.yml
- group: other
  href: https://artifacts.apis.io/repl-it/hosts/repl-it-hosts.yml
  title: ''
  type: Hosts
  url: hosts/repl-it-hosts.yml
- group: other
  href: https://artifacts.apis.io/repl-it/vendors/repl-it-vendors.yml
  title: ''
  type: Vendors
  url: vendors/repl-it-vendors.yml
- group: build
  href: https://artifacts.apis.io/repl-it/packages/repl-it-packages.yml
  title: ''
  type: SDKs
  url: packages/repl-it-packages.yml
- group: build
  href: https://artifacts.apis.io/repl-it/packages/repl-it-packages.yml
  title: ''
  type: Packages
  url: packages/repl-it-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.replit.com/core-concepts/project-editor/app-setup/development-urls
- group: auth
  href: https://artifacts.apis.io/repl-it/security/repl-it-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/repl-it-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/repl-it/security/repl-it-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/repl-it-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/repl-it/security/repl-it-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/repl-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://repl.it/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.replit.com/
created: '2026-10-21'
description: Replit (formerly Repl.it) is an online IDE and collaborative coding platform that lets users write, run, and host code in many programming languages directly from a browser. It provides instant development environments, multi-user collaboration, deployment tools, and a marketplace for apps and extensions, serving developers, educators, and enterprises worldwide.
image: https://replit.com/public/images/opengraph_rebrand.jpg
layout: provider
modified: '2026-10-21'
name: Repl.it
nav: Providers
network: true
overview: 'Repl.it is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IDE, Cloud, Collaboration, and Education.


  Repl.it''s developer surface includes getting-started guide, documentation, and 12 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 55.4
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 14.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/repl-it/repl-it-2026-11-03T142158.png
security:
- kind: domain-security
  name: Repl It Domain Security
  slug: repl-it-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Repl It Vulnerability Disclosure
  slug: repl-it-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Repl It Trust Center
  slug: repl-it-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: repl-it
tags:
- Company
- IDE
- Cloud
- Collaboration
- Education
- Enterprise
website: https://repl.it/
---
