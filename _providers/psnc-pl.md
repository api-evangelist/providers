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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public API documentation (if any) for the Institute of Bioorganic Chemistry of the Polish Academy of Sciences - Poznan Supercomputing and Networking Center.
  name: PCSS API
  slug: pcss-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/psnc-pl/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/psnc-pl/hosts/psnc-pl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/psnc-pl-hosts.yml
- group: auth
  href: https://artifacts.apis.io/psnc-pl/security/psnc-pl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/psnc-pl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.psnc.pl/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.psnc.pl/
- group: company
  title: ''
  type: Blog
  url: https://www.psnc.pl/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.psnc.pl/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.psnc.pl/sign-up-for-the-echoes-newsletter/
- group: operate
  title: ''
  type: Support
  url: https://www.psnc.pl/contact/contact-details/
coverage:
  checked: '2026-10-29'
  detail: Documentation is public HTML but provides no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.psnc.pl/
  - status: 200
    url: https://docs.psnc.pl/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Poznańskie Centrum Superkomputerowo-Sieciowe (PCSS), affiliated with the Institute of Bioorganic Chemistry of the Polish Academy of Sciences, is one of Poland’s most significant research and development institutions and a key node in the European Research Area. Since 1993, it fulfills the mission of “Integrating and developing IT infrastructure for science,” linking advanced research with modern economy and society.
image: https://www.psnc.pl/files/PCSS-LOGO-2025-EN.svg
layout: provider
modified: '2026-10-29'
name: Institute of Bioorganic Chemistry of the Polish Academy of Sciences - Poznan Supercomputing and Networking Center
nav: Providers
network: true
overview: 'Institute of Bioorganic Chemistry of the Polish Academy of Sciences - Poznan Supercomputing and Networking Center is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Research, Supercomputing, Networking, Poland, and Science.


  Institute of Bioorganic Chemistry of the Polish Academy of Sciences - Poznan Supercomputing and Networking Center''s developer surface includes documentation, engineering blog, signup flow, support, and 5 more developer resources.'
plans:
- name: Psnc Pl Plans Pricing
  plan_count: 0
  slug: psnc-pl-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Psnc Pl Rate Limits
  slug: psnc-pl-rate-limits
scopes:
- name: Psnc Pl Scopes
  scope_count: 0
  slug: psnc-pl-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Psnc Pl Authentication
  slug: psnc-pl-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Psnc Pl Domain Security
  slug: psnc-pl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: psnc-pl
tags:
- Research
- Supercomputing
- Networking
- Poland
- Science
website: https://www.psnc.pl/
---
