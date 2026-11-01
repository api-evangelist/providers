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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.phenom.com/vdp
- group: agent
  href: https://artifacts.apis.io/phenompeople-com/llms/phenompeople-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/phenompeople-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/phenompeople-com/well-known/phenompeople-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/phenompeople-com-www-security.txt
- group: agent
  href: https://artifacts.apis.io/phenompeople-com/well-known/phenompeople-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/phenompeople-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/phenompeople-com/hosts/phenompeople-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/phenompeople-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.phenom.com:443/terms--conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.phenom.com:443/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.phenom.com:443/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.phenom.com:443/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phenompeople
- group: auth
  href: https://artifacts.apis.io/phenompeople-com/security/phenompeople-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/phenompeople-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/phenompeople-com/security/phenompeople-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phenompeople-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://phenompeople.com/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on any discovered host.
  evidence:
  - status: 403
    url: https://api.phenom.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Phenom Applied AI provides a Talent Intelligence Platform that leverages AI to help companies attract, engage, and retain talent. Their solutions include a talent CRM, intelligent career site, automated interview scheduling, workforce planning, and AI agents for screening and coaching. Serving industries such as healthcare, finance, technology, and retail, Phenom aims to improve hiring speed, candidate experience, and overall workforce intelligence.
image: https://images.ctfassets.net/0d3i1kfsuaq3/62p83cDOitH0AQ0Hx0Zkna/417d7f1500c30149103bc7410e6cb00f/Pheom_Applied_AI.jpg?q=70
layout: provider
modified: '2026-10-29'
name: Phenom
nav: Providers
network: true
overview: 'Phenom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Talent, AI, Recruiting, and Platform.


  Phenom''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Phenompeople Com Domain Security
  slug: phenompeople-com-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Phenompeople Com Vulnerability Disclosure
  slug: phenompeople-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: phenompeople-com
tags:
- Company
- Talent
- AI
- Recruiting
- Platform
website: https://phenompeople.com/
---
