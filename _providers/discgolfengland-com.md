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
    agent_card: near-conformant
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/discgolfengland-com/security/discgolfengland-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/discgolfengland-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/discgolfengland-com/llms/discgolfengland-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/discgolfengland-com-llms.txt
- group: other
  href: https://artifacts.apis.io/discgolfengland-com/a2a/discgolfengland-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/discgolfengland-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/discgolfengland-com/well-known/discgolfengland-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/discgolfengland-com-security.txt
- group: agent
  href: https://artifacts.apis.io/discgolfengland-com/well-known/discgolfengland-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/discgolfengland-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/discgolfengland-com/hosts/discgolfengland-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/discgolfengland-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/discgolfengland-com/vendors/discgolfengland-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/discgolfengland-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://discgolfengland.com/about/governance/policies/register-of-declared-interests/
- group: company
  title: ''
  type: Newsroom
  url: https://discgolfengland.com/news/
- group: company
  title: ''
  type: Blog
  url: https://discgolfengland.com/blog/
- group: auth
  href: https://artifacts.apis.io/discgolfengland-com/security/discgolfengland-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/discgolfengland-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/discgolfengland-com/security/discgolfengland-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/discgolfengland-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://discgolfengland.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://discgolfengland.com/about/
- group: operate
  title: ''
  type: Support
  url: https://discgolfengland.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://discgolfengland.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://discgolfengland.com/terms-of-use/
coverage:
  checked: '2026-11-05'
  detail: The provider is a nonprofit governing body with no public API surface.
  evidence:
  - status: 200
    url: https://discgolfengland.com/
  reason: not-a-software-company
  state: none
created: '2026-11-05'
description: The English Disc Golf Association (EDGA) is the governing body for disc golf in England, supporting the sport’s growth through organizing tournaments, maintaining a network of courses, and providing resources for players of all levels. It offers membership, promotes community events, and works to increase participation across the country, fostering a vibrant disc golf community.
image: https://discgolfengland.com/wp-content/uploads/2025/12/EDGA-colour-W-TEXT.png
layout: provider
modified: '2026-11-05'
name: English Disc Golf Association
nav: Providers
network: true
overview: 'English Disc Golf Association is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Disc Golf, Sports, United Kingdom, Non-Profit, and Community.


  English Disc Golf Association''s developer surface includes signup flow, engineering blog, getting-started guide, support, and 13 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Discgolfengland Com Domain Security
  slug: discgolfengland-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Discgolfengland Com Vulnerability Disclosure
  slug: discgolfengland-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: discgolfengland-com
tags:
- Disc Golf
- Sports
- United Kingdom
- Non-Profit
- Community
website: https://discgolfengland.com/
---
