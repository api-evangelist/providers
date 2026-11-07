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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.criteriacorp.com/terms-use
- group: auth
  title: ''
  type: Compliance
  url: https://www.criteriacorp.com/security-and-compliance
- group: auth
  href: https://artifacts.apis.io/criteria-corp/security/criteria-corp-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/criteria-corp-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/criteria-corp/hosts/criteria-corp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/criteria-corp-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.criteriacorp.com/press
- group: other
  title: ''
  type: Leadership
  url: https://www.criteriacorp.com/team
- group: auth
  href: https://artifacts.apis.io/criteria-corp/security/criteria-corp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/criteria-corp-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/criteria-corp/security/criteria-corp-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/criteria-corp-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/criteria-corp/security/criteria-corp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/criteria-corp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://criteriacorp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.criteriacorp.com/develop
- group: docs
  title: ''
  type: Documentation
  url: https://www.criteriacorp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.criteriacorp.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.criteriacorp.com/plans-and-pricing
- group: company
  title: ''
  type: Blog
  url: https://www.criteriacorp.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.criteriacorp.com/plans-and-pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.criteriacorp.com/privacy-policy
coverage:
  checked: '2026-10-27'
  detail: Developer portal pages provide HTML docs but no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.criteriacorp.com/develop
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Criteria Corp provides pre‑employment testing and employee assessment solutions, offering a suite of scientifically validated assessments such as cognitive aptitude, personality, emotional intelligence, risk, skills, and game‑based tests. Their platform includes AI‑proctored video interviewing, real‑time interview scoring, and ongoing employee development tools like weekly manager check‑ins and coaching. Serving enterprises, mid‑market, and small businesses, Criteria Corp helps organizations make data‑driven hiring and development decisions through a cloud‑based SaaS platform.
image: https://www.criteriacorp.com/files/docs/files/cc-share.png
layout: provider
modified: '2026-10-27'
name: Criteria Corp
nav: Providers
network: true
overview: 'Criteria Corp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pre-Employment Testing, Assessment, Video Interviewing, Talent Development, and AI Proctoring.


  Criteria Corp''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, and 12 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 50.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/criteria-corp/criteria-corp-2026-11-03T125622.png
security:
- kind: domain-security
  name: Criteria Corp Domain Security
  slug: criteria-corp-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Criteria Corp Vulnerability Disclosure
  slug: criteria-corp-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Criteria Corp Trust Center
  slug: criteria-corp-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: criteria-corp
tags:
- Pre-Employment Testing
- Assessment
- Video Interviewing
- Talent Development
- AI Proctoring
- Enterprise Hiring
website: https://criteriacorp.com/
---
