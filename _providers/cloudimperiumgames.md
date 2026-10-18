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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudimperiumgames/refs/heads/main/security/cloudimperiumgames-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cloudimperiumgames-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudimperiumgames/refs/heads/main/hosts/cloudimperiumgames-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudimperiumgames-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudimperiumgames.com/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://cloudimperiumgames.com/pages/press
- group: company
  title: ''
  type: Blog
  url: https://cloudimperiumgames.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudimperiumgames
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudimperiumgames/refs/heads/main/security/cloudimperiumgames-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudimperiumgames-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudimperiumgames/refs/heads/main/security/cloudimperiumgames-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudimperiumgames-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudimperiumgames.com
coverage:
  checked: '2026-10-09'
  detail: Attempted to fetch OpenAPI spec at https://api.cloudimperiumgames.com/openapi.json but host was unreachable (DNS error).
  evidence:
  - status: DNS_ERROR
    url: https://api.cloudimperiumgames.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Cloud Imperium Games (CIG) is a game development studio founded in 2012 by Chris Roberts, creating ambitious space simulation titles such as Star Citizen and Squadron 42. Based in Austin, Texas with additional studios worldwide, CIG engages a large community of backers and fans, operating with a focus on immersive storytelling, cutting‑edge technology, and ongoing development updates. The company also runs a robust online presence, including a blog, privacy policy, legal information, and support channels for its players and partners.
layout: provider
modified: '2026-10-09'
name: Cloudimperiumgames
nav: Providers
network: true
overview: 'Cloudimperiumgames is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Video Games, StarCitizen, and Squadron42.


  Cloudimperiumgames'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudimperiumgames Domain Security
  slug: cloudimperiumgames-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Cloudimperiumgames Vulnerability Disclosure
  slug: cloudimperiumgames-vulnerability-disclosure
  summary_line: no policy recorded
slug: cloudimperiumgames
tags:
- Company
- Gaming
- Video Games
- StarCitizen
- Squadron42
- Community
website: https://cloudimperiumgames.com
---
