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
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/proscendia-com/llms/proscendia-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/proscendia-com-llms.txt
- group: other
  href: https://artifacts.apis.io/proscendia-com/hosts/proscendia-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/proscendia-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://proscendia.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://proscendia.com/privacy
- group: auth
  href: https://artifacts.apis.io/proscendia-com/security/proscendia-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/proscendia-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://proscendia.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://proscendia.com/ai-agent-development-cost
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Naresh084
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, or MCP specifications were found on the provider's hosts, and the API subdomain api.proscendia.com does not resolve.
  evidence:
  - status: 0
    url: https://api.proscendia.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Proscendia is an AI agent consultancy that builds autonomous AI agents to automate work inside customers’ own systems. The company emphasizes open‑source tools, publishing projects such as ClaudeGate and Cowork on GitHub, and offers transparent pricing for AI‑agent development. Their site describes a four‑step engagement process, showcases open‑source code, and provides a Calendly link for consultations.
image: https://proscendia.com/og.jpg
layout: provider
modified: '2026-10-30'
name: proscendia-com
nav: Providers
network: true
overview: 'proscendia-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Agent, Consultancy, and OpenSource.


  proscendia-com''s developer surface includes pricing and 7 more developer resources.'
random_paper: 12
scopes:
- name: Proscendia Com Scopes
  scope_count: 0
  slug: proscendia-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Proscendia Com Authentication
  slug: proscendia-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Proscendia Com Domain Security
  slug: proscendia-com-domain-security
  summary_line: TLSv1.3
slug: proscendia-com
tags:
- Company
- AI
- Agent
- Consultancy
- OpenSource
- Automation
website: https://proscendia.com/
---
