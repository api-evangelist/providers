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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/joon/well-known/joon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/joon-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.joon.co/
- group: other
  href: https://artifacts.apis.io/joon/hosts/joon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joon-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joon.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joon.co/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://dev.joon.co/
- group: auth
  href: https://artifacts.apis.io/joon/security/joon-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/joon-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/joon/security/joon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joon.co
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://joon.co
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Joon provides AI-managed cybersecurity solutions, offering autonomous virtual experts that integrate with existing security stacks to deliver rapid SOC modernization, continuous threat detection, and automated response, backed by service level agreements and enterprise-grade compliance.
image: https://joon.co/images/og-thumbnail.png
layout: provider
modified: '2026-10-24'
name: Joon
nav: Providers
network: true
overview: 'Joon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Cybersecurity, SOC, and Automation.


  Joon''s developer surface includes documentation and 8 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/joon/joon-2026-11-03T134228.png
security:
- kind: domain-security
  name: Joon Domain Security
  slug: joon-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Joon Trust Center
  slug: joon-trust-center
  summary_line: SOC 2, ISO 27001
slug: joon
tags:
- Company
- Artificial Intelligence
- Cybersecurity
- SOC
- Automation
website: https://joon.co
---
