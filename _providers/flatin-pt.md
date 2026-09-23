---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-09-23'
api_count: 1
apis:
- baseURL: https://flatin.pt/api/v1
  baseurl_source: declared
  description: Keyless REST API for Portuguese IMI rates and IMT/stamp duty calculations, with a remote MCP server exposing four agent tools and an llms.txt for agent discovery.
  name: flatin.pt API
  slug: flatinpt-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://flatin.pt/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://flatin.pt/en/tools/api-and-data/
- group: docs
  title: ''
  type: Documentation
  url: https://flatin.pt/en/tools/api-and-data/
- group: start
  title: ''
  type: GettingStarted
  url: https://flatin.pt/en/tools/api-and-data/#rest
- group: docs
  title: ''
  type: APIReference
  url: https://flatin.pt/api/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://flatin.pt/api/plans.json
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/rate-limits/flatin-pt-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/flatin-pt-rate-limits.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://flatin.pt/status/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/changelog/flatin-pt-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flatin-pt-changelog.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flatin.pt/en/legal/termos-utilizacao/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flatin.pt/en/legal/privacidade/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/security/flatin-pt-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/flatin-pt-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/well-known/flatin-pt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/flatin-pt-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/security/flatin-pt-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/flatin-pt-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/security/flatin-pt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flatin-pt-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/well-known/flatin-pt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flatin-pt-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/well-known/flatin-pt-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/flatin-pt-api-catalog.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/rules/flatin-pt-spectral.yaml
  title: ''
  type: SpectralRules
  url: rules/flatin-pt-spectral.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/llms/flatin-pt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flatin-pt-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/mcp/flatin-pt-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/flatin-pt-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/packages/flatin-pt-packages.yml
  title: ''
  type: SDKs
  url: packages/flatin-pt-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flatin-pt/refs/heads/main/packages/flatin-pt-packages.yml
  title: ''
  type: Packages
  url: packages/flatin-pt-packages.yml
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/licenses/by/4.0/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flatinpt
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/flatinpt/mcp
- group: operate
  title: ''
  type: Support
  url: mailto:info@flatin.pt
created: '2026-09-16'
description: Portuguese property-tax APIs providing keyless access to IMI rates for all 308 municipalities and IMT/stamp duty purchase-cost calculations, sourced from official Autoridade Tributária tables. flatin.pt serves the same numbers as a REST API with an OpenAPI schema, a remote MCP server exposing four agent tools, an llms.txt for agent discovery, and a CC BY 4.0 open CSV dataset — no key and no sign-up.
image: https://flatin.pt/assets/brand/raster/icon-256.png
layout: provider
mcp_servers:
- description: Remote Model Context Protocol server for Portuguese property taxes — IMT/stamp duty on a purchase and IMI rates for all 308 municipalities. Keyless, stateless Streamable HTTP.
  name: flatin.pt Property Taxes MCP
  slug: flatinpt-property-taxes-mcp
modified: '2026-09-16'
name: flatin.pt
nav: Providers
network: true
overview: 'flatin.pt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, Property Tax, Tax, IMI, and IMT.


  The flatin.pt catalog on APIs.io includes 1 Spectral governance ruleset.


  flatin.pt''s developer surface includes documentation, getting-started guide, API reference, pricing, changelog, support, and 20 more developer resources.'
plans:
- name: Flatin Pt Plans Pricing
  plan_count: 1
  slug: flatin-pt-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Flatin Pt Rate Limits
  slug: flatin-pt-rate-limits
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: flatin.pt API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 4
  slug: flatin-pt-spectral
score:
  band: strong
  composite: 63.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 71.0
    catalog_earned_first_party: 16.0
    catalog_gap: 44.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 59.1
    contract_quality: 49.0
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 65.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - portugal
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 63.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Flatin Pt Authentication
  slug: flatin-pt-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Flatin Pt Domain Security
  slug: flatin-pt-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Flatin Pt Vulnerability Disclosure
  slug: flatin-pt-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: flatin-pt
tags:
- Real-Estate
- Property Tax
- Tax
- IMI
- IMT
- Stamp Duty
- Portugal
- Open Data
- Government Data
- Fiscal Data
- MCP
- AI Agents
website: https://flatin.pt/en/
---
