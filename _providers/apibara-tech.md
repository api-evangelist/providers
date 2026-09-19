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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-09-18'
api_count: 1
apis:
- baseURL: https://apibara.tech/api/v1/vehicle-auction
  baseurl_source: declared
  description: 'REST/JSON API providing normalized Copart & IAAI vehicle auction data: vehicle search, VIN/lot details, vehicle history, related vehicles, filters, auction locations, shipping calculation, URL tools, '
  name: Vehicle Auction Data API
  slug: vehicle-auction-data-api
arazzos:
- description: Retrieve recently updated Copart and IAAI auction records with cursor pagination.
  name: Apibara incremental vehicle-auction synchronization
  slug: apibara-tech-incremental-sync.arazzo
- description: Retrieve a supported vehicle record and then its retained auction history.
  name: Apibara VIN auction research
  slug: apibara-tech-vin-research.arazzo
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://apibara.tech/en
- group: company
  title: ''
  type: About
  url: https://apibara.tech/en/about
- group: docs
  title: ''
  type: Documentation
  url: https://apibara.tech/en/products/vehicle-auction-data-api/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://apibara.tech/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://apibara.tech/en/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apibara.tech/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apibara.tech/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://apibara.tech/en/contact
- group: auth
  title: ''
  type: Security
  url: https://apibara.tech/en/security
- group: operate
  title: ''
  type: StatusPage
  url: https://apibara.tech/en/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://apibara.tech/en/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apibara-tech/refs/heads/main/changelog/apibara-tech-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apibara-tech-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://apibara.tech/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apibara-tech/refs/heads/main/well-known/apibara-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apibara-tech-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apibara-tech/refs/heads/main/conformance/apibara-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apibara-tech-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apibara-tech/refs/heads/main/conventions/apibara-tech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apibara-tech-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apibara-tech/refs/heads/main/lifecycle/apibara-tech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apibara-tech-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apibara-tech/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apibara-tech/refs/heads/main/packages/apibara-tech-packages.yml
  title: ''
  type: Packages
  url: packages/apibara-tech-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apibara-tech/refs/heads/main/security/apibara-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apibara-tech-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apibara-tech/refs/heads/main/authentication/apibara-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apibara-tech-authentication.yml
created: '2026-09-18'
description: Independent developer platform providing structured vehicle auction data (normalized JSON for Copart and IAA/IAAI current and historical auction records), including vehicle search, VIN/lot details, photos, prices, sale history, filter metadata, auction locations, shipping calculation, and an image proxy. Offers both a REST/JSON API and a hosted read-only MCP server. Not affiliated with the similarly named apibara.com blockchain indexer.
image: https://apibara.tech/seo/1783599358_p64LSzUP.png
layout: provider
mcp_servers:
- description: ''
  name: Apibara.tech MCP Server
  slug: apibaratech-mcp-server
modified: '2026-09-18'
name: Apibara.tech
nav: Providers
network: true
overview: 'Apibara.tech publishes 1 API on the [APIs.io](https://apis.io/) network: Vehicle Auction Data API. Tagged areas include Automotive, vehicle-auction-data, Copart, IAAI, and vin-history.


  Apibara.tech''s developer surface includes documentation, pricing, signup flow, support, changelog, authentication, and 15 more developer resources.'
plans:
- name: Apibara Tech Plans Pricing
  plan_count: 8
  slug: apibara-tech-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 9
  name: Apibara Tech Rate Limits
  slug: apibara-tech-rate-limits
score:
  band: strong
  composite: 58.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 61.4
    developer_ergonomics: 51.8
    discoverability: 75.9
    operational_transparency: 73.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Apibara Tech Authentication
  slug: apibara-tech-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apibara Tech Domain Security
  slug: apibara-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apibara-tech
tags:
- Automotive
- vehicle-auction-data
- Copart
- IAAI
- vin-history
- Marketplace
- REST API
- Vehicle Auctions
- Salvage Auctions
- VIN Data
- Used-Car Marketplace Data
- Data Infrastructure
- Data as a Service
- REST
- JSON:API
- MCP
- agent-native
website: https://apibara.tech/en
---
