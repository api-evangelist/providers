---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.7
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Skinory Agentic Access
  operation_count: 2
  slug: skinory-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://skinory.io
  baseurl_source: spec
  description: The Inventories API from Skinory (submitted as g2push) — 1 operation(s) for inventories.
  name: Skinory (submitted as g2push) Inventories API
  slug: skinory-inventories-api
- baseURL: https://skinory.io
  baseurl_source: spec
  description: The Inventory API from Skinory (submitted as g2push) — 1 operation(s) for inventory.
  name: Skinory (submitted as g2push) Inventory API
  slug: skinory-inventory-api
artifact_total: 7
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/agentic-access/skinory-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/skinory-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/rules/skinory-rules.yml
  title: ''
  type: Spectral
  url: rules/skinory-rules.yml
- group: auth
  title: ''
  type: Security
  url: https://skinory.io/en/about
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/errors/skinory-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/skinory-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/conformance/skinory-conformance.yml
  title: ''
  type: Conformance
  url: conformance/skinory-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/overlays/skinory-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/skinory-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/llms/skinory-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skinory-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/well-known/skinory-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/skinory-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/well-known/skinory-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/skinory-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/hosts/skinory-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skinory-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/vendors/skinory-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skinory-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://skinory.io/en/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/authentication/skinory-authentication.yml
  title: ''
  type: Authentication
  url: authentication/skinory-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/security/skinory-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/skinory-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/skinory/refs/heads/main/security/skinory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skinory-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skinory.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skinory.io/en/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://skinory.io/en/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://skinory.io/en/developers
created: '2026-09-28'
description: Skinory offers a free, public read‑only JSON API delivering real‑time CS2 and CS:GO skin price data, historical price trends, Steam inventory valuation, and detailed statistics for professional teams and players. The service operates without authentication for basic limits, supports optional API keys for higher quotas, and enforces open CORS for client‑side use. Comprehensive documentation, including endpoint details, rate limits, and licensing information, is available at https://skinory.io/en/developers, with the full OpenAPI 3.1 specification provided at /api/openapi.json.
image: https://skinory.io/og/en.png?brand=skinory-wordmark-12
layout: provider
modified: '2026-09-28'
name: Skinory (submitted as g2push)
nav: Providers
network: true
overview: 'Skinory (submitted as g2push) publishes 2 APIs on the [APIs.io](https://apis.io/) network: Inventories API and Inventory API. Tagged areas include Company, Gaming, Skins, CS2, and CS:GO.


  The Skinory (submitted as g2push) catalog on APIs.io includes 1 Spectral governance ruleset.


  Skinory (submitted as g2push)''s developer surface includes authentication, documentation, getting-started guide, and 16 more developer resources.'
random_paper: 13
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Skinory (submitted as g2push) API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: skinory-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Skinory Authentication
  slug: skinory-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Skinory Domain Security
  slug: skinory-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Skinory Vulnerability Disclosure
  slug: skinory-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: skinory
tags:
- Company
- Gaming
- Skins
- CS2
- CS:GO
website: https://skinory.io/
---
