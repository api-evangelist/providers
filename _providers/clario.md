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
api_count: 1
apis:
- description: Clario provides clinical trial endpoint data solutions and a developer portal with documentation.
  name: Clario API
  slug: clario-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clario/refs/heads/main/llms/clario-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clario-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clario/refs/heads/main/hosts/clario-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clario-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clario/refs/heads/main/vendors/clario-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clario-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.clario.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clario.com/about/legal-and-privacy/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://clario.com/about/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://clario.com/about/leadership/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.clario.com/docs/getting-started-with-ecoa-solutions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forgeglobal
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clario/refs/heads/main/security/clario-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clario-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clario.com
- group: docs
  title: ''
  type: Documentation
  url: https://clario.com/solutions/
- group: company
  title: ''
  type: Blog
  url: https://clario.com/resources/articles/
- group: operate
  title: ''
  type: Contact
  url: https://clario.com/contact/
coverage:
  detail: No OpenAPI or other machine‑readable contract was found on the provider's domain despite probing common spec endpoints.
  evidence:
  - status: 404
    url: https://clario.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Clario provides clinical trial endpoint technology and evidence generation services, offering solutions for cardiac safety, blood pressure monitoring, ECG data collection, and comprehensive data management across all phases of clinical research. Their platform supports hybrid and site‑based trials worldwide, delivering precise, regulatory‑compliant data to accelerate drug development and improve patient outcomes.
image: https://clario.com/wp-content/uploads/2021/11/Clario-Website-Open-Graph-Image.jpg
layout: provider
modified: '2026-10-08'
name: Clario
nav: Providers
network: true
overview: 'Clario is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Clinical Trials, Data Management, Healthcare, Technology, and Services.


  Clario''s developer surface includes support, getting-started guide, documentation, engineering blog, and 10 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 67.9
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clario Domain Security
  slug: clario-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clario
tags:
- Clinical Trials
- Data Management
- Healthcare
- Technology
- Services
website: https://clario.com
---
