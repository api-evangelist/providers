---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Customer signup
  name: FilingSift Accounts API
  slug: filingsift-accounts-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Internal platform administration; platform-admin key required
  name: FilingSift Administration API
  slug: filingsift-administration-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Source-linked Excel exports
  name: FilingSift Analyst API
  slug: filingsift-analyst-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Runtime plan catalog and provider-controlled checkout availability
  name: FilingSift Billing API
  slug: filingsift-billing-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: API lifecycle and schema metadata
  name: FilingSift Contract API
  slug: filingsift-contract-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Deployed public ownership and event queries. Supplied credentials require search:read and billing access; the current router does not apply watchlist or plan-history filters.
  name: FilingSift Corporate Events API
  slug: filingsift-corporate-events-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Filing streams
  name: FilingSift Developer API
  slug: filingsift-developer-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Issuers and structured SEC filings
  name: FilingSift Filings API
  slug: filingsift-filings-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: First-party website intake
  name: FilingSift Intake API
  slug: filingsift-intake-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Private feeds
  name: FilingSift Integrations API
  slug: filingsift-integrations-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Source-cited facts and comparisons
  name: FilingSift Intelligence API
  slug: filingsift-intelligence-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Private consented pilot enrollment
  name: FilingSift Pilots API
  slug: filingsift-pilots-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Free public
  name: FilingSift Reference API
  slug: filingsift-reference-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Bounded filing search
  name: FilingSift Search API
  slug: filingsift-search-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: MFA factors
  name: FilingSift Security API
  slug: filingsift-security-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Invitations
  name: FilingSift Team API
  slug: filingsift-team-api
- baseURL: https://api.filingsift.com/api/v1
  baseurl_source: declared
  description: Deployed public raw-fact and network resources. The current router does not apply issuer or plan-history filters; composite responses are bounded.
  name: FilingSift XBRL API
  slug: filingsift-xbrl-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/filingsift/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/filingsift/data-model/filingsift-data-model.yml
  title: ''
  type: DataModel
  url: data-model/filingsift-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://filingsift.com/security.html
- group: design
  href: https://artifacts.apis.io/filingsift/errors/filingsift-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/filingsift-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/filingsift/llms/filingsift-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/filingsift-llms.txt
- group: auth
  href: https://artifacts.apis.io/filingsift/well-known/filingsift-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/filingsift-security.txt
- group: agent
  href: https://artifacts.apis.io/filingsift/well-known/filingsift-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/filingsift-well-known.yml
- group: other
  href: https://artifacts.apis.io/filingsift/hosts/filingsift-hosts.yml
  title: ''
  type: Hosts
  url: hosts/filingsift-hosts.yml
- group: other
  href: https://artifacts.apis.io/filingsift/vendors/filingsift-vendors.yml
  title: ''
  type: Vendors
  url: vendors/filingsift-vendors.yml
- group: build
  href: https://artifacts.apis.io/filingsift/packages/filingsift-packages.yml
  title: ''
  type: Packages
  url: packages/filingsift-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://filingsift.com/sdks/
- group: auth
  href: https://artifacts.apis.io/filingsift/security/filingsift-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/filingsift-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/filingsift/security/filingsift-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/filingsift-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://filingsift.com/
- group: docs
  title: ''
  type: Documentation
  url: https://filingsift.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://filingsift.com/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://filingsift.com/guides/filing-comparisons/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://filingsift.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://filingsift.com/privacy.html
created: '2026-10-21'
description: FilingSift provides source‑cited SEC filing data through a REST API and client libraries. It enables analysts and software teams to search indexed SEC filings, compare financing disclosures, and retrieve primary‑source rates, bank and credit information. The platform returns evidence‑backed facts with accession numbers, filing URLs, and verification states, supporting free, Builder, Professional, and Team plans.
layout: provider
modified: '2026-10-21'
name: FilingSift
nav: Providers
network: true
overview: 'FilingSift publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Administration API, Analyst API, and 14 more. Tagged areas include SEC, Filings, Data, and Finance.


  FilingSift''s developer surface includes documentation, API reference, getting-started guide, and 16 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 49.2
    developer_ergonomics: 23.2
    discoverability: 60.7
    operational_transparency: 5.3
  previous_composite: 31.5
  provenance:
    contracts:
      callable: 94.4
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 14.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/filingsift/filingsift-2026-11-03T132017.png
security:
- kind: domain-security
  name: Filingsift Domain Security
  slug: filingsift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Filingsift Vulnerability Disclosure
  slug: filingsift-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: getbis-credit-context
  slug: filingsift-getbis-credit-context
slug: filingsift
tags:
- SEC
- Filings
- Data
- Finance
website: https://filingsift.com/
---
