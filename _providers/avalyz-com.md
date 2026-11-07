---
access_model:
  confidence: low
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/avalyz-com/plans/avalyz-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avalyz-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://avalyz.com/av/securite
- group: agent
  href: https://artifacts.apis.io/avalyz-com/llms/avalyz-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avalyz-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/avalyz-com/well-known/avalyz-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avalyz-com-security.txt
- group: agent
  href: https://artifacts.apis.io/avalyz-com/well-known/avalyz-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avalyz-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/avalyz-com/hosts/avalyz-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avalyz-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/avalyz-com/security/avalyz-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avalyz-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/avalyz-com/security/avalyz-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avalyz-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avalyz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://avalyz.com/methode?lang=en
- group: commercial
  title: ''
  type: Pricing
  url: https://avalyz.com/tarifs?lang=en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avalyz.com/av/cgv
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avalyz.com/av/confidentialite
- group: company
  title: ''
  type: Blog
  url: https://avalyz.com/av/articles?lang=en
- group: start
  title: ''
  type: GettingStarted
  url: https://avalyz.com/banc
- group: start
  title: ''
  type: Login
  url: https://avalyz.com/connexion
coverage:
  checked: '2026-11-02'
  detail: The provider's website offers no public API documentation or machine‑readable specification.
  evidence:
  - status: 404
    url: https://avalyz.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Avalyz provides AI‑powered acceptance testing for any web application, offering a free trial bench where users paste an app URL, run read‑only tests, and receive detailed reports with screenshots, evidence, and actionable findings. The platform aims to give an independent second look, proving functionality rather than promising it, with simple pricing and no commitment.
image: https://avalyz.com/av/og.png
layout: provider
modified: '2026-11-02'
name: Avalyz
nav: Providers
network: true
overview: 'Avalyz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Testing, Web App, Software-as-a-Service, and Automation.


  Avalyz''s developer surface includes documentation, pricing, engineering blog, getting-started guide, and 12 more developer resources.'
plans:
- name: Avalyz Com Plans Pricing
  plan_count: 3
  slug: avalyz-com-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 27.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avalyz Com Domain Security
  slug: avalyz-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avalyz Com Vulnerability Disclosure
  slug: avalyz-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: avalyz-com
tags:
- Artificial Intelligence
- Testing
- Web App
- Software-as-a-Service
- Automation
website: https://avalyz.com/
---
