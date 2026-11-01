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
  href: https://artifacts.apis.io/riverside-research/hosts/riverside-research-hosts.yml
  title: ''
  type: Hosts
  url: hosts/riverside-research-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.riversideresearch.org/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.riversideresearch.org/who-we-are/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.riversideresearch.org/insights/category/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/riversideresearch
- group: auth
  href: https://artifacts.apis.io/riverside-research/security/riverside-research-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/riverside-research-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.riversideresearch.org
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: http://api.riversideresearch.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Riverside Research is a nonprofit research organization focused on advanced technologies such as artificial intelligence, plasma physics, radar systems, and secure communications. It provides expertise and services to government and industry partners, offering AI Forge, collection planning tools, and secure platform solutions. The organization emphasizes innovation, community outreach, and a culture of collaboration, aiming to advance scientific research and technology development.
image: https://www.riversideresearch.org/uploads/_1200x630_crop_center-center_none/SEO-Image.jpg
layout: provider
modified: '2026-10-28'
name: Riverside Research
nav: Providers
network: true
overview: 'Riverside Research is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Nonprofit, Research, AI, Plasma Physics, and Radar Systems.


  Riverside Research''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Riverside Research Domain Security
  slug: riverside-research-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: riverside-research
tags:
- Nonprofit
- Research
- AI
- Plasma Physics
- Radar Systems
website: http://www.riversideresearch.org
---
