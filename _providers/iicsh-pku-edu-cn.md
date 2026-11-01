---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Developer portal for PKU IICSH (access requires authentication via PKU SSO).
  name: PKU IICSH Developer Portal
  slug: pku-iicsh-developer-portal
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/iicsh-pku-edu-cn/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/iicsh-pku-edu-cn/hosts/iicsh-pku-edu-cn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iicsh-pku-edu-cn-hosts.yml
- group: auth
  href: https://artifacts.apis.io/iicsh-pku-edu-cn/security/iicsh-pku-edu-cn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iicsh-pku-edu-cn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iicsh.pku.edu.cn/
coverage:
  checked: '2026-10-29'
  detail: Portal.pku.edu.cn redirects to PKU SSO login, requiring authentication to access developer documentation.
  evidence:
  - status: 200
    url: https://portal.pku.edu.cn/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: The Peking University International Sci‑Tech Innovation Center (PKU‑IICSH) located in the Lin‑gang Special Area of Shanghai Pilot Free Trade Zone is a research and innovation hub affiliated with Peking University. It focuses on fostering high‑tech entrepreneurship, supporting technology transfer, and promoting collaborative projects between academia, industry, and government. The center provides incubation services, funding assistance, and technical resources to startups and research teams, aiming to accelerate the commercialization of scientific breakthroughs in China and globally.
image: https://www.pku.edu.cn/pku_logo_red.png
layout: provider
modified: '2026-10-29'
name: Peking University International Sci-Tech Innovation Center at Lin-gang Special Area, China (Shanghai) Pilot Free Trade Zone (PKU-IICSH)
nav: Providers
network: true
overview: Peking University International Sci-Tech Innovation Center at Lin-gang Special Area, China (Shanghai) Pilot Free Trade Zone (PKU-IICSH) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Innovation, Research, Technology, Incubator, and China.
plans:
- name: Iicsh Pku Edu Cn Plans Pricing
  plan_count: 0
  slug: iicsh-pku-edu-cn-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Iicsh Pku Edu Cn Rate Limits
  slug: iicsh-pku-edu-cn-rate-limits
scopes:
- name: Iicsh Pku Edu Cn Scopes
  scope_count: 0
  slug: iicsh-pku-edu-cn-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Iicsh Pku Edu Cn Authentication
  slug: iicsh-pku-edu-cn-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Iicsh Pku Edu Cn Domain Security
  slug: iicsh-pku-edu-cn-domain-security
  summary_line: TLSv1.3 · DMARC
slug: iicsh-pku-edu-cn
tags:
- Innovation
- Research
- Technology
- Incubator
- China
- University
website: https://iicsh.pku.edu.cn/
---
