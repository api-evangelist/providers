---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API reference not publicly available; no machine‑readable contract discovered.
  name: Antevo API
  slug: antevo-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/antevo-ch/llms/antevo-ch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/antevo-ch-llms.txt
- group: agent
  href: https://artifacts.apis.io/antevo-ch/well-known/antevo-ch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/antevo-ch-well-known.yml
- group: other
  href: https://artifacts.apis.io/antevo-ch/hosts/antevo-ch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/antevo-ch-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://wealth.antevo.ch/sign-up
- group: auth
  href: https://artifacts.apis.io/antevo-ch/security/antevo-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/antevo-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://antevo.ch/
- group: docs
  title: ''
  type: Documentation
  url: https://antevo.ch/mcp
- group: operate
  title: ''
  type: Support
  url: https://antevo.ch/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ANTEVO-CH
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://antevo.ch/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://antevo.ch/policies/terms-of-use
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on any discovered host.
  evidence:
  - status: 404
    url: https://api.antevo.ch/openapi.json
  - status: 404
    url: https://antevo.ch/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Antevo provides intelligence and data integration for wealth management, helping advisors and family offices monitor brand, market, and regulatory developments. The platform offers a suite of tools, including MCP servers for AI assistants, a CLI, and a web portal that aggregates public intelligence with client‑specific context. It emphasizes Swiss‑hosted security and privacy, serving clients from Zurich.
image: https://antevo.ch/assets/antevo-og.jpg
layout: provider
modified: '2026-10-29'
name: antevo-ch
nav: Providers
network: true
overview: 'antevo-ch is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wealth, Data-Integration, AI-Assistants, and Swiss.


  antevo-ch''s developer surface includes signup flow, documentation, support, and 8 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Antevo Ch Domain Security
  slug: antevo-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: antevo-ch
tags:
- Company
- Wealth
- Data-Integration
- AI-Assistants
- Swiss
website: https://antevo.ch/
---
