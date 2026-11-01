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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/compgen/llms/compgen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/compgen-llms.txt
- group: other
  href: https://artifacts.apis.io/compgen/hosts/compgen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compgen-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.compgen.de/status/default
- group: start
  title: ''
  type: SignUp
  url: https://www.compgen.de/2021/08/register-zu-den-grundbuechern-aus-baden-baden/
- group: auth
  href: https://artifacts.apis.io/compgen/security/compgen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compgen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.compgen.de/
- group: docs
  title: ''
  type: Documentation
  url: https://www.compgen.de/downloadbereich/
- group: operate
  title: ''
  type: Support
  url: https://www.compgen.de/kontakt/
- group: company
  title: ''
  type: Blog
  url: https://www.compgen.de/recherchieren/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.compgen.de/datenschutzerklaerung/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.compgen.de/impressum/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec was discovered on any host.
  evidence:
  - status: 404
    url: https://api.compgen.de/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: CompGen DES / domus.genealogy.net historical building map is a German non-profit association (Verein für Computergenealogie e.V.) that provides free access to genealogical data and historical building information. It operates the domus.genealogy.net platform, offering tools for ancestry and family research, as well as a map of historical buildings across Germany, supporting researchers, historians, and the public with extensive data collections.
image: https://www.compgen.de/wp-content/uploads/2022/03/CompGen_Home5-2.jpg
layout: provider
modified: '2026-10-28'
name: CompGen DES / domus.genealogy.net historical building map
nav: Providers
network: true
overview: 'CompGen DES / domus.genealogy.net historical building map is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Genealogy, History, Data, Non-profit, and Germany.


  CompGen DES / domus.genealogy.net historical building map''s developer surface includes signup flow, documentation, support, engineering blog, and 7 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Compgen Domain Security
  slug: compgen-domain-security
  summary_line: TLSv1.3 · HSTS
slug: compgen
tags:
- Genealogy
- History
- Data
- Non-profit
- Germany
website: https://www.compgen.de/
---
