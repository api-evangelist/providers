---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/upworthy/hosts/upworthy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/upworthy-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.upworthy.com/registered-nurse-shares-her-radical-but-distinctly-american-plan-to-stop-gun-violence/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upworthy.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upworthy
- group: auth
  href: https://artifacts.apis.io/upworthy/security/upworthy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/upworthy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upworthy.com/
coverage:
  checked: '2026-10-23'
  detail: Upworthy website provides no discoverable OpenAPI, GraphQL, or other machine-readable API specifications.
  evidence:
  - status: 404
    url: https://www.upworthy.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Upworthy is a digital media company that creates and curates uplifting, inspirational, and socially relevant content. It focuses on storytelling that resonates with a broad audience, aiming to inspire positive change and share compelling narratives across its website and social platforms. The company leverages data-driven approaches to amplify stories that matter, engaging readers with high-quality articles, videos, and interactive media.
image: https://www.upworthy.com/wp-content/uploads/sites/2/2025/12/cropped-upworthy-site-icon_2ff506.png?w=192
layout: provider
modified: '2026-10-22'
name: Upworthy
nav: Providers
network: true
overview: 'Upworthy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Content, Storytelling, Social Impact, and Digital.


  Upworthy''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Upworthy Domain Security
  slug: upworthy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upworthy
tags:
- Media
- Content
- Storytelling
- Social Impact
- Digital
website: https://www.upworthy.com/
---
