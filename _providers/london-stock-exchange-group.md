---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 48
  human_in_the_loop: 2
  name: London Stock Exchange Group Agentic Access
  operation_count: 78
  slug: london-stock-exchange-group-agentic-access
  summary_line: 78 operations · 48 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Create, screen, update, archive, assign, link, and search screening cases; review and resolve screening results; enable ongoing screening and retrieve ongoing screening updates for KYC and third-party
  name: LSEG World-Check One Case API
  slug: lseg-world-check-one-case-api
- description: Retrieve MediaCheck adverse-media screening results, article metadata and content, attach or detach articles to cases, and mark articles as reviewed.
  name: LSEG World-Check One Media-Check API
  slug: lseg-world-check-one-media-check-api
- description: Enable, disable, and retrieve the MediaCheck smart filter on screening cases.
  name: LSEG World-Check One Smart Filter API
  slug: lseg-world-check-one-smart-filter-api
- description: Retrieve filtered audit events for screening cases to evidence compliance workflows.
  name: LSEG World-Check One Audit API
  slug: lseg-world-check-one-audit-api
- description: Retrieve and update the risk rating on a screening case.
  name: LSEG World-Check One Case Rating API
  slug: lseg-world-check-one-case-rating-api
- description: Create, retrieve, and delete relationships between screening cases.
  name: LSEG World-Check One Linked Cases API
  slug: lseg-world-check-one-linked-cases-api
- description: Retrieve groups, case templates, and resolution toolkits that govern how cases are created and results resolved.
  name: LSEG World-Check One Group API
  slug: lseg-world-check-one-group-api
- description: List active users in the client account for case assignment.
  name: LSEG World-Check One User API
  slug: lseg-world-check-one-user-api
- description: Reference data for screening - countries, nationalities, providers, search filters, World-Check profiles and records, and PEP details.
  name: LSEG World-Check One Reference API
  slug: lseg-world-check-one-reference-api
- description: Maintain custom client watchlist sources and records for screening.
  name: LSEG World-Check One Client Watchlist API
  slug: lseg-world-check-one-client-watchlist-api
- description: Submit asynchronous case report requests, poll report status, and download completed reports.
  name: LSEG World-Check One Reporting API
  slug: lseg-world-check-one-reporting-api
- description: Report status listing, report error details, and report cancellation operations.
  name: LSEG World-Check One Upcoming API
  slug: lseg-world-check-one-upcoming-api
- description: Generate machine-readable zone (MRZ) data for passport verification.
  name: LSEG World-Check One Passport Check API
  slug: lseg-world-check-one-passport-check-api
- description: Zero Footprint Screening surface - synchronous screening, groups, case templates, reference data, and client watchlist maintenance without persisting case data.
  name: LSEG World-Check One Zero Footprint Screening API
  slug: lseg-world-check-one-zfs-api
- description: Retrieve information about the public API, including the current API version.
  name: LSEG World-Check One API Info API
  slug: lseg-world-check-one-api-info-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info API
  slug: open-london-stock-exchange-group-api-info-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info Audit API
  slug: open-london-stock-exchange-group-audit-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info Case API
  slug: open-london-stock-exchange-group-case-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info Case-Rating API
  slug: open-london-stock-exchange-group-case-rating-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info Client-Watchlist API
  slug: open-london-stock-exchange-group-client-watchlist-api
- collection_type: open
  name: London Stock Exchange LSEG World-Check One Api-Info Group API
  slug: open-london-stock-exchange-group-group-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info Linked-Cases API
  slug: open-london-stock-exchange-group-linked-cases-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info Media-Check API
  slug: open-london-stock-exchange-group-media-check-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info Passport-Check API
  slug: open-london-stock-exchange-group-passport-check-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info Reference API
  slug: open-london-stock-exchange-group-reference-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info Reporting API
  slug: open-london-stock-exchange-group-reporting-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info Smart-Filter API
  slug: open-london-stock-exchange-group-smart-filter-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info Upcoming API
  slug: open-london-stock-exchange-group-upcoming-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info User API
  slug: open-london-stock-exchange-group-user-api
- collection_type: open
  name: London Stock Exchange Group LSEG World-Check One Api-Info Zfs API
  slug: open-london-stock-exchange-group-zfs-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.lseg.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.lseg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lseg.com/en/api-catalog
- group: docs
  title: ''
  type: APIReference
  url: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-one-api/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-one-api/quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.lseg.com/
- group: operate
  title: ''
  type: Community
  url: https://community.developers.lseg.com/
- group: company
  title: ''
  type: Blog
  url: https://developers.lseg.com/en/article-catalog
- group: start
  title: ''
  type: SignUp
  url: https://developers.lseg.com/en/register
- group: operate
  title: ''
  type: StatusPage
  url: https://liveservice.lseg.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lseg.com/en/policies/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lseg.com/en/policies/privacy-statement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LSEG
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/london-stock-exchange-group
- group: auth
  title: ''
  type: Authentication
  url: authentication/london-stock-exchange-group-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/london-stock-exchange-group-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/london-stock-exchange-group-packages.yml
- group: design
  title: ''
  type: Components
  url: components/london-stock-exchange-group-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/london-stock-exchange-group-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/london-stock-exchange-group-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/london-stock-exchange-group-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/london-stock-exchange-group-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/london-stock-exchange-group-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/london-stock-exchange-group-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/london-stock-exchange-group-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/london-stock-exchange-group-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/london-stock-exchange-group-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/london-stock-exchange-group-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/london-stock-exchange-group-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/london-stock-exchange-group-finops.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/london-stock-exchange-group-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/london-stock-exchange-group-domain-security.yml
created: '2024-04-14'
description: London Stock Exchange Group plc is a United Kingdom-based stock exchange and financial information company headquartered in the City of London, England. LSEG provides capital markets, data and analytics, risk management, and post-trade services including the World-Check screening platform for KYC and anti-money-laundering due diligence.
finops:
- name: London Stock Exchange Group Finops
  service_category: API
  slug: london-stock-exchange-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/london-stock-exchange-group.png
layout: provider
mcp_servers:
- description: ''
  name: London Stock Exchange Group MCP Server
  slug: london-stock-exchange-group-mcp-server
modified: '2026-07-22'
name: London Stock Exchange Group
nav: Providers
network: true
overview: 'London Stock Exchange Group publishes 15 APIs on the [APIs.io](https://apis.io/) network, including LSEG World-Check One Case API, LSEG World-Check One Media-Check API, LSEG World-Check One Smart Filter API, and 12 more. Tagged areas include Financial, Stock Exchange, Market Data, KYC, and Compliance.


  London Stock Exchange Group''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 26 more developer resources.'
plans:
- name: London Stock Exchange Group Plans Pricing
  plan_count: 3
  slug: london-stock-exchange-group-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: London Stock Exchange Group Rate Limits
  slug: london-stock-exchange-group-rate-limits
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 23
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 50.8
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/london-stock-exchange-group/refs/heads/main/screenshots/london-stock-exchange-group-2026-06-20T184706.png
security:
- kind: authentication
  name: London Stock Exchange Group Authentication
  slug: london-stock-exchange-group-authentication
  summary_line: oauth2/hmac-signature · 2 schemes
- kind: domain-security
  name: London Stock Exchange Group Domain Security
  slug: london-stock-exchange-group-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: london-stock-exchange-group
tags:
- Financial
- Stock Exchange
- Market Data
- KYC
- Compliance
website: https://www.lseg.com/
---
