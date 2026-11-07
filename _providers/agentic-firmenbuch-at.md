---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Das gesamte österreichische Firmenbuch und deutsche Handelsregister in natürlicher Sprache durchsuchen: semantische Suche, Screening nach Finanzkennzahlen, Export als CSV.'
  name: Agentic Firmenbuch API
  slug: agentic-firmenbuch-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/agentic-firmenbuch-at/rate-limits/agentic-firmenbuch-at-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentic-firmenbuch-at-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agentic-firmenbuch-at/plans/agentic-firmenbuch-at-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentic-firmenbuch-at-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/agentic-firmenbuch-at/security/agentic-firmenbuch-at-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentic-firmenbuch-at-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/agentic-firmenbuch-at/llms/agentic-firmenbuch-at-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentic-firmenbuch-at-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentic-firmenbuch-at/mcp/agentic-firmenbuch-at-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentic-firmenbuch-at-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentic-firmenbuch-at/well-known/agentic-firmenbuch-at-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentic-firmenbuch-at-security.txt
- group: auth
  href: https://artifacts.apis.io/agentic-firmenbuch-at/well-known/agentic-firmenbuch-at-agentic-firmenbuch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentic-firmenbuch-at-agentic-firmenbuch-security.txt
- group: agent
  href: https://artifacts.apis.io/agentic-firmenbuch-at/well-known/agentic-firmenbuch-at-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentic-firmenbuch-at-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentic-firmenbuch-at/hosts/agentic-firmenbuch-at-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentic-firmenbuch-at-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.agentic-firmenbuch.at/register
- group: auth
  href: https://artifacts.apis.io/agentic-firmenbuch-at/security/agentic-firmenbuch-at-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentic-firmenbuch-at-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentic-firmenbuch-at/security/agentic-firmenbuch-at-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentic-firmenbuch-at-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentic-firmenbuch.at/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.agentic-firmenbuch.at/
- group: docs
  title: ''
  type: Documentation
  url: https://www.agentic-firmenbuch.at/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agentic-firmenbuch.at/onboarding.html
- group: operate
  title: ''
  type: Support
  url: https://www.agentic-firmenbuch.at/sicherheit
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agentic-firmenbuch.at/preise.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agentic-firmenbuch.at/impressum.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentic-firmenbuch.at/datenschutz.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jkbngb/agentic-firmenbuch
coverage:
  checked: '2026-10-30'
  detail: MCP endpoint https://app.agentic-firmenbuch.at/api/mcp returned 403, indicating the API is gated behind authentication.
  evidence:
  - status: 403
    url: https://app.agentic-firmenbuch.at/api/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Agentic-Firmenbuch.at provides a searchable interface to the entire Austrian Firmenbuch and German Handelsregister in natural language. Users can perform semantic searches, filter by financial metrics, and export results as CSV. The service offers credits starting at €50 plus VAT and a Pro plan at €79 per month plus VAT, targeting investors, M&A professionals, and researchers.
image: https://www.agentic-firmenbuch.at/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.agentic-firmenbuch.at.
  name: agentic-firmenbuch-at MCP Server
  slug: agentic-firmenbuch-at-mcp-yml
modified: '2026-10-29'
name: agentic-firmenbuch-at
nav: Providers
network: true
overview: 'agentic-firmenbuch-at is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finanzen, Firmenbuch, Österreich, Deutschland, and Daten.


  agentic-firmenbuch-at''s developer surface includes signup flow, documentation, getting-started guide, support, pricing, and 16 more developer resources.'
plans:
- name: Agentic Firmenbuch At Plans Pricing
  plan_count: 2
  slug: agentic-firmenbuch-at-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Agentic Firmenbuch At Rate Limits
  slug: agentic-firmenbuch-at-rate-limits
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 48.0
    catalog_earned_first_party: 16.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 66.7
    operational_transparency: 34.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/agentic-firmenbuch-at/agentic-firmenbuch-at-2026-11-03T120357.png
security:
- kind: domain-security
  name: Agentic Firmenbuch At Domain Security
  slug: agentic-firmenbuch-at-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agentic Firmenbuch At Vulnerability Disclosure
  slug: agentic-firmenbuch-at-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentic-firmenbuch-at
tags:
- Finanzen
- Firmenbuch
- Österreich
- Deutschland
- Daten
website: https://agentic-firmenbuch.at/
---
