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
- description: Ørsted provides digital services for offshore wind data and analytics.
  name: Orsted API
  slug: orsted-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/orsted/refs/heads/main/hosts/orsted-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orsted-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://orsted.com/en/offshore-wind/offshore-wind-data/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://orsted.com/en/media/news/sign-up-for-news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orsted.com/en/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://orsted.com/en/investors/news
- group: other
  title: ''
  type: Leadership
  url: https://orsted.com/en/about-us/our-organisation/management
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Orsted
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/orsted/refs/heads/main/security/orsted-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orsted-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orsted.com
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discovered on orsted.com or api.orsted.com.
  evidence:
  - status: 200
    url: https://orsted.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Ørsted is a global leader in offshore renewable energy, developing, constructing and operating offshore wind farms, as well as providing onshore wind, solar, bioenergy and energy trading solutions. The company focuses on sustainable energy transition, delivering clean power to customers worldwide while driving innovation in digital trading and analytics. Ørsted’s portfolio includes large-scale offshore wind projects across Europe, the United States and Asia, and it actively invests in new technologies to reduce carbon emissions and support a greener future.
image: https://cdn.orsted.com/-/media/www/images/corp/some-images/gtf-office-flags.jpg?rev=247991a4dada461caaeae8ffad71bc9e&extension=webp&hash=8991FFDF71C6C00805927A92D77D817C
layout: provider
modified: '2026-10-13'
name: Orsted
nav: Providers
network: true
overview: 'Orsted is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Renewables, OffshoreWind, Sustainability, and Denmark.


  Orsted''s developer surface includes signup flow and 8 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 60.7
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Orsted Domain Security
  slug: orsted-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: orsted
tags:
- Energy
- Renewables
- OffshoreWind
- Sustainability
- Denmark
- Company
website: https://orsted.com
---
