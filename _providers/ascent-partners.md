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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/ascent-partners/security/ascent-partners-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ascent-partners-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/ascent-partners/llms/ascent-partners-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ascent-partners-llms.txt
- group: auth
  href: https://artifacts.apis.io/ascent-partners/well-known/ascent-partners-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ascent-partners-security.txt
- group: agent
  href: https://artifacts.apis.io/ascent-partners/well-known/ascent-partners-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ascent-partners-well-known.yml
- group: other
  href: https://artifacts.apis.io/ascent-partners/hosts/ascent-partners-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ascent-partners-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://ascent.partners/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ascent.partners/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://ascent.partners/press
- group: auth
  href: https://artifacts.apis.io/ascent-partners/security/ascent-partners-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ascent-partners-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ascent-partners/security/ascent-partners-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ascent-partners-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ascent.partners/
coverage:
  checked: '2026-11-01'
  detail: Ascent Partners Foundation provides charitable services and does not expose a software API.
  evidence:
  - status: 200
    url: https://ascent.partners/
  reason: not-a-software-company
  state: none
created: '2026-11-01'
description: Ascent Partners Foundation is a Hong Kong‑registered charity focused on connecting funders, researchers, and practitioners to drive sustainable impact across Asia‑Pacific. Established in 2017, it partners with UN agencies, NGOs, and the private sector to mobilise climate, biodiversity and inclusive growth financing. The foundation runs programs, convenes multi‑faith dialogues, and hosts events such as the One Earth Summit, publishing impact reports and fostering community inclusion.
image: https://ascent.partners/assets/og-default.jpg
layout: provider
modified: '2026-11-01'
name: Ascent Partners Foundation
nav: Providers
network: true
overview: 'Ascent Partners Foundation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Charity, Sustainability, Climate, Community, and Asia Pacific.


  Ascent Partners Foundation''s developer surface includes support and 10 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 49.1
    operational_transparency: 10.5
  previous_composite: 9.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ascent Partners Domain Security
  slug: ascent-partners-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ascent Partners Vulnerability Disclosure
  slug: ascent-partners-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ascent-partners
tags:
- Charity
- Sustainability
- Climate
- Community
- Asia Pacific
website: https://ascent.partners/
---
