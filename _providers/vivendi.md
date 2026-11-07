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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/vivendi/hosts/vivendi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vivendi-hosts.yml
- group: auth
  href: https://artifacts.apis.io/vivendi/security/vivendi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vivendi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vivendi.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vivendi.com/en/footer/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vivendi.com/en/footer/data-and-content-protection-charter/
- group: design
  title: ''
  type: AccessibilityConformance
  url: https://www.vivendi.com/en/accessibility/
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.vivendi.com/en/footer/data-and-content-protection-charter/
coverage:
  checked: '2026-11-04'
  detail: 'vivendi.com is the corporate, investor and press site of a media holding company: no developer, docs or API host resolves (api., developer., developers., docs.vivendi.com all NXDOMAIN) and the site serves 404 for /openapi.json, /swagger.json, /graphql, /wp-json/ and /llms.txt.'
  evidence:
  - status: 200
    url: https://www.vivendi.com/
  - status: 404
    url: https://www.vivendi.com/openapi.json
  - status: 404
    url: https://www.vivendi.com/graphql
  - status: 404
    url: https://www.vivendi.com/llms.txt
  - status: 403
    url: https://www.vivendi.com/.well-known/agent-card.json
  - status: NXDOMAIN
    url: https://api.vivendi.com/
  reason: not-a-software-company
  state: none
created: '2026-11-04'
description: 'Vivendi is a Paris-based content, media and entertainment group (Vivendi SE) that holds a portfolio of listed and unlisted assets: Gameloft (wholly owned video-game publisher), V Collection (luxury media), and minority stakes in Universal Music Group, Banijay, Lagardère, MediaForEurope, Prisma Media and Prisa. Its website is a corporate, investor and press site; the group publishes no public API, SDK or developer program of its own.'
image: https://www.vivendi.com/wp-content/uploads/2024/12/Visuel_def.jpg
layout: provider
modified: '2026-11-04'
name: Vivendi
nav: Providers
network: true
overview: Vivendi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Entertainment, Holding Company, and Investor Relations.
random_paper: 13
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Vivendi Domain Security
  slug: vivendi-domain-security
  summary_line: DNSSEC · DMARC
slug: vivendi
tags:
- Company
- Media
- Entertainment
- Holding Company
- Investor Relations
- Video Games
- Publishing
- France
website: https://www.vivendi.com
---
