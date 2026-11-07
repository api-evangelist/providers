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
- group: auth
  title: ''
  type: Compliance
  url: https://www.appliedintuition.com/security
- group: other
  href: https://artifacts.apis.io/appliedintuition/hosts/appliedintuition-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appliedintuition-hosts.yml
- group: other
  href: https://artifacts.apis.io/appliedintuition/vendors/appliedintuition-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appliedintuition-vendors.yml
- group: auth
  href: https://artifacts.apis.io/appliedintuition/security/appliedintuition-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/appliedintuition-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://appliedintuition.com
- group: company
  title: ''
  type: About
  url: https://www.appliedintuition.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.appliedintuition.com/blog
- group: agent
  href: https://artifacts.apis.io/appliedintuition/llms/appliedintuition-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appliedintuition-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AppliedIntuition
- group: operate
  title: ''
  type: Support
  url: https://www.appliedintuition.com/contact
- group: auth
  href: https://artifacts.apis.io/appliedintuition/security/appliedintuition-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/appliedintuition-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/appliedintuition/security/appliedintuition-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/appliedintuition-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/appliedintuition/security/appliedintuition-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appliedintuition-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appliedintuition.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appliedintuition.com/privacy-policy
coverage:
  checked: '2026-10-20'
  detail: Applied Intuition sells autonomy and simulation software to enterprise and defense customers through sales contact only; no api/docs/developer host resolves and its GitHub org holds only forks of third-party projects.
  evidence:
  - status: 200
    url: https://www.appliedintuition.com/
  - status: 200
    url: https://www.appliedintuition.com/contact
  - status: 0
    url: https://api.appliedintuition.com/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Applied Intuition builds physical AI software and systems for intelligent machines, helping customers develop, test, validate, deploy, and operate autonomy and vehicle intelligence across automotive, defense, trucking, mining, construction, and agriculture. Its product lines include a Self-Driving System (a unified autonomy stack for land, air, and sea), Vehicle OS (an operating system for intelligent machines), and Tools for Vehicle Intelligence covering simulation, validation, data, training, and evaluation workflows. The company operates as a private enterprise vendor and does not currently publish a public developer API or self-service portal; this profile captures its public identity, security posture, and machine-readable llms.txt.
image: https://cdn.sanity.io/images/a86leg7v/production/7e96db00d9bd9a6aa41194e2b8dbae2d8af500dd-1200x630.png?w=1200&h=630
layout: provider
modified: '2026-10-20'
name: Applied Intuition
nav: Providers
network: true
overview: 'Applied Intuition is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Autonomy, Physical AI, Autonomous Vehicles, and Simulation.


  Applied Intuition''s developer surface includes engineering blog, support, and 13 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.4
    operational_transparency: 13.2
  previous_composite: 17.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/appliedintuition/appliedintuition-2026-07-25T200800.png
security:
- kind: domain-security
  name: Appliedintuition Domain Security
  slug: appliedintuition-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Appliedintuition Vulnerability Disclosure
  slug: appliedintuition-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Appliedintuition Trust Center
  slug: appliedintuition-trust-center
  summary_line: SOC 2, ISO 27001
slug: appliedintuition
tags:
- Company
- Autonomy
- Physical AI
- Autonomous Vehicles
- Simulation
- Defense
- Robotics
website: https://appliedintuition.com
---
