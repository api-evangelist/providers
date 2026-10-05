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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Avataar platform providing AI-native transformation services.
  name: Avataar API
  slug: avataar-api
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avataar/refs/heads/main/changelog/avataar-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/avataar-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avataar/refs/heads/main/llms/avataar-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avataar-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avataar/refs/heads/main/well-known/avataar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avataar-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avataar/refs/heads/main/hosts/avataar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avataar-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avataar.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avataar.ai/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.avataar.ai/knowledge-center/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.avataar.ai/knowledge-center/before-getting-started/3d-user
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avataar/refs/heads/main/security/avataar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avataar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avataar.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.avataar.ai/platform-and-technology
- group: company
  title: ''
  type: About
  url: https://www.avataar.ai/about
- group: operate
  title: ''
  type: Contact
  url: https://www.avataar.ai/contact
coverage:
  checked: 2026-09-26
  detail: Documentation pages are rendered HTML; markdown twins exist but contain no machine-readable specs.
  evidence:
  - status: 200
    url: https://docs.avataar.ai/knowledge-center
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Avataar is an AI-native transformation platform based in Bengaluru, India, founded in 2014. It provides a suite of agentic AI tools that automate enterprise workflows, improve operational efficiency, and enable intelligent execution across industries such as finance, manufacturing, healthcare, and retail. The company raised $55.5M in Series B funding and serves large enterprises seeking to modernize their processes with autonomous AI agents.
image: https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=1440,h=756,fit=crop,f=jpeg/Awv4LQyN0yfNwwV0/screenshot-2025-06-25-at-6.52.36a-pm-YD0wjbGPQxFVorNW.png
layout: provider
modified: '2026-09-26'
name: Avataar
nav: Providers
network: true
overview: 'Avataar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Enterprise, Automation, and AI Agents.


  Avataar''s developer surface includes changelog, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 64.3
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avataar Domain Security
  slug: avataar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avataar
tags:
- Company
- Artificial Intelligence
- Enterprise
- Automation
- AI Agents
- Bengaluru
website: https://www.avataar.ai/
---
