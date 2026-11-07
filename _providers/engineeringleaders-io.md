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
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 10.0
  scored_at: '2026-11-06'
api_count: 1
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/engineeringleaders-io/llms/engineeringleaders-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/engineeringleaders-io-llms.txt
- group: other
  href: https://artifacts.apis.io/engineeringleaders-io/a2a/engineeringleaders-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/engineeringleaders-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/engineeringleaders-io/well-known/engineeringleaders-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/engineeringleaders-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/engineeringleaders-io/hosts/engineeringleaders-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/engineeringleaders-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/engineeringleaders-io/vendors/engineeringleaders-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/engineeringleaders-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.engineeringleaders.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.engineeringleaders.io/privacy
- group: other
  title: ''
  type: Leadership
  url: https://www.engineeringleaders.io/team/
- group: company
  title: ''
  type: Blog
  url: https://www.engineeringleaders.io/blog
- group: auth
  href: https://artifacts.apis.io/engineeringleaders-io/security/engineeringleaders-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/engineeringleaders-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://engineeringleaders.io/
coverage:
  checked: '2026-10-30'
  detail: The provider's website offers community features but no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.engineeringleaders.io/
  reason: no-developer-program
  state: none
created: '2026-10-30'
description: Engineeringleaders.io is a community platform for engineering leaders in Central and Eastern Europe, offering meetups, conferences, mentorship, peer circles, and AI toolkits. It provides membership options for individuals and companies, organizes events across Prague, Brno, Bratislava, and Kraków, and supports leadership development through workshops, an academy, and networking opportunities. The platform aims to foster knowledge sharing and professional growth among senior engineering professionals.
image: https://www.engineeringleaders.io/gallery/home/og-home.webp
layout: provider
modified: '2026-10-30'
name: engineeringleaders-io
nav: Providers
network: true
overview: 'engineeringleaders-io publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Community, Leadership, Event, and Membership.


  engineeringleaders-io''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 28.6
    contract_governance: 0.0
    contract_quality: 6.0
    developer_ergonomics: 1.2
    discoverability: 56.3
    operational_transparency: 0.0
  previous_composite: 18.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/engineeringleaders-io/engineeringleaders-io-2026-11-03T131527.png
security:
- kind: domain-security
  name: Engineeringleaders Io Domain Security
  slug: engineeringleaders-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: engineeringleaders-io
tags:
- Company
- Community
- Leadership
- Event
- Membership
website: https://engineeringleaders.io/
---
