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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/london-stock-exchange-group/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acadiasoft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lseg.com/en/post-trade/solutions/acadia
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AcadiaSoft
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/AcadiaSoft/simm-lib
- group: build
  title: ''
  type: Packages
  url: packages/acadiasoft-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acadiasoft-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acadiasoft-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/acadiasoft-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acadiasoft-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/acadiasoft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acadiasoft-rate-limits.yml
coverage:
  checked: '2026-09-06'
  detail: Acadia's entire product documentation set lives on an Atlassian Confluence instance at portal.acadiasoft.com whose every anonymous request 302s to an OAuth2 authorization endpoint with realm=docportal, and whose own OpenID/RFC 8414 discovery documents return 401 — so the direct API its factsheets advertise has no publicly readable contract, reference or limits.
  evidence:
  - status: 302
    url: https://portal.acadiasoft.com/
  - status: 401
    url: https://portal.acadiasoft.com/identity/.well-known/openid-configuration
  - status: 301
    url: https://acadia.inc/openapi.json
  - status: 200
    url: https://www.lseg.com/en/post-trade/solutions/streamline/margin-manager
  reason: customer-only-docs
  state: gated
created: '2026-09-06'
description: 'Acadia, founded in 2009 as AcadiaSoft, provides risk, margin and collateral management services to the global uncleared OTC derivatives market and now operates as part of LSEG Post Trade following LSEG''s December 2022 acquisition. Its AcadiaPlus platform — Agreement Manager, Margin Manager, Collateral Manager, IM Exposure Manager, Payments Manager, Settlement Manager and Relay, alongside the Risk Suite analytics services — connects more than 2,000 market participants for initial-margin calculation, margin-call messaging, reconciliation, dispute resolution and settlement. Acadia''s own factsheets state its applications are reachable by web user interface, direct API and SFTP, but that interface is delivered under customer contract: the product documentation portal is authenticated and no public specification is published. The company''s one public machine-readable artifact is simm-lib, an MIT-licensed Java implementation of the ISDA SIMM initial-margin model.'
image: https://avatars.githubusercontent.com/u/30508839?v=4
layout: provider
modified: '2026-09-06'
name: Acadia
nav: Providers
network: true
overview: 'Acadia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Capital Markets, Derivatives, and Risk Management.


  Acadia''s developer surface includes changelog and 11 more developer resources.'
plans:
- name: Acadiasoft Plans Pricing
  plan_count: 0
  slug: acadiasoft-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Acadiasoft Rate Limits
  slug: acadiasoft-rate-limits
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    operational_transparency: 18.4
  previous_composite: 9.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acadiasoft Domain Security
  slug: acadiasoft-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: acadiasoft
tags:
- Company
- Financial Services
- Capital Markets
- Derivatives
- Risk Management
- Collateral Management
- Margin
- Post Trade
- Regulatory Compliance
website: https://www.lseg.com/en/post-trade/solutions/acadia
---
