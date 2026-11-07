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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/dataart-com/well-known/dataart-com-dataart-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dataart-com-dataart-security.txt
- group: agent
  href: https://artifacts.apis.io/dataart-com/llms/dataart-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataart-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/dataart-com/well-known/dataart-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dataart-com-www-security.txt
- group: auth
  href: https://artifacts.apis.io/dataart-com/well-known/dataart-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dataart-com-security.txt
- group: agent
  href: https://artifacts.apis.io/dataart-com/well-known/dataart-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dataart-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dataart-com/hosts/dataart-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataart-com-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://www.dataart.com/services/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dataart.com/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.dataart.com/company/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.dataart.com/company/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DataArt
- group: company
  title: ''
  type: Blog
  url: https://www.dataart.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.dataart.com/
- group: auth
  href: https://artifacts.apis.io/dataart-com/security/dataart-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dataart-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dataart-com/security/dataart-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataart-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataart.com/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's API host.
  evidence:
  - status: 0
    url: https://api.dataart.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: DataArt is a global AI software development and data consulting partner founded in 1997. With over 6,000 employees across 20+ countries, DataArt delivers AI‑first solutions, custom software engineering, cloud and DevOps services to Fortune 500 enterprises in finance, healthcare, retail, media, travel, automotive, and more. The company emphasizes enterprise‑scale AI pipelines, data strategy, and industry‑specific digital transformation.
image: https://www.dataart.com/media/vcod0xx1/default-meta-image-com.png
layout: provider
modified: '2026-11-04'
name: DataArt
nav: Providers
network: true
overview: 'DataArt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Consulting, Software Development, Data Engineering, and Enterprise.


  DataArt''s developer surface includes engineering blog, documentation, and 14 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 51.8
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dataart Com Domain Security
  slug: dataart-com-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dataart Com Vulnerability Disclosure
  slug: dataart-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dataart-com
tags:
- Artificial Intelligence
- Consulting
- Software Development
- Data Engineering
- Enterprise
website: https://dataart.com/
---
