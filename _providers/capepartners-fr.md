---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-09-25'
api_count: 1
apis:
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: Machine-readable API backing the Cape Partners M&A deal-flow workspace — inbound submission, workspace session and profile management, ranked matching, valuation, pairings and mutual-consent phase cha
  name: Cape Partners Sniffer Agent API
  slug: cape-partners-sniffer-agent-api
- description: 'The A2A 1.0 surface of the Cape Partners agent exchange: SendMessage, GetTask and ListTasks on both the JSON-RPC binding (POST /a2a) and the HTTP+JSON binding (POST /a2a/message:send, GET /a2a/tasks, '
  name: Cape Partners Agent Exchange (A2A)
  slug: cape-partners-agent-exchange-a2a
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.capepartners.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://www.capepartners.fr/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://www.capepartners.fr/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.capepartners.fr/tos
- group: start
  title: ''
  type: SignUp
  url: https://www.capepartners.fr/new-workspace.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/capepartners/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/capepartners-fr/refs/heads/main/llms/capepartners-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capepartners-fr-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/capepartners-fr/refs/heads/main/well-known/capepartners-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capepartners-fr-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/capepartners-fr/refs/heads/main/a2a/capepartners-fr-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/capepartners-fr-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/capepartners-fr/refs/heads/main/security/capepartners-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capepartners-fr-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/capepartners-fr/refs/heads/main/authentication/capepartners-fr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/capepartners-fr-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/capepartners-fr/refs/heads/main/conventions/capepartners-fr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/capepartners-fr-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/capepartners-fr/refs/heads/main/conformance/capepartners-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capepartners-fr-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/capepartners-fr/refs/heads/main/lifecycle/capepartners-fr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/capepartners-fr-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/capepartners-fr/refs/heads/main/plans/capepartners-fr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/capepartners-fr-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/capepartners-fr/refs/heads/main/rate-limits/capepartners-fr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/capepartners-fr-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/capepartners-fr/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-19'
description: 'Cape Partners is an independent M&A advisory firm focused on technology, based in Le Chesnay, France (Cape Partners SAS, SIREN 833 208 960). It operates a deal-flow platform ("Sniffer") that sources and enriches European software companies, matches sellers to strategic and financial buyers with a deterministic-times-semantic fit score, produces preliminary valuations, and lets both sides manage pairings and deal phases in a session-scoped workspace. The platform is agent-first: an OpenAPI 3.1 contract at /openapi.json, a JSON capability index at /api, llms.txt, an AI-plugin discovery manifest, and an A2A 1.0 Agent Card whose SendMessage / GetTask / ListTasks operations are served live at /a2a. External agents take part through an "agent exchange" — publish a six-field manifest with no account or key, then poll for a grounded answer; a workspace UUID is issued only after a human-reviewed handshake, and the Terms of Service are signed by a human principal.'
layout: provider
modified: '2026-09-19'
name: Cape Partners
nav: Providers
network: true
overview: 'Cape Partners publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Sniffer Agent API, and 1 more. Tagged areas include Mergers and Acquisitions, Deal Flow, Valuation, Investment, and Financial Services.


  Cape Partners'' developer surface includes documentation, API reference, signup flow, authentication, and 13 more developer resources.'
plans:
- name: Capepartners Fr Plans Pricing
  plan_count: 0
  slug: capepartners-fr-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Capepartners Fr Rate Limits
  slug: capepartners-fr-rate-limits
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 45.4
    developer_ergonomics: 30.4
    discoverability: 69.6
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 38.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Capepartners Fr Authentication
  slug: capepartners-fr-authentication
  summary_line: apiKey · 6 schemes
- kind: domain-security
  name: Capepartners Fr Domain Security
  slug: capepartners-fr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: capepartners-fr
tags:
- Mergers and Acquisitions
- Deal Flow
- Valuation
- Investment
- Financial Services
- Agents
- A2A
- France
- Technology
- Software-as-a-Service
website: https://www.capepartners.fr/
---
