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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: International Trade Administration Agentic Access
  operation_count: 7
  slug: international-trade-administration-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://data.trade.gov
  baseurl_source: declared
  description: Search the consolidated list of parties for which the U.S. Government maintains restrictions on certain exports, reexports, or transfers of items. Combines screening lists from the Departments of Comm
  name: International Trade Administration Consolidated Screening List API
  slug: international-trade-administration-consolidated-screening-list-api
- baseURL: https://data.trade.gov
  baseurl_source: declared
  description: Country-specific reports prepared by U.S. embassies covering the market conditions, opportunities, regulations, and business customs for U.S. exporters.
  name: International Trade Administration Country Commercial Guides API
  slug: international-trade-administration-country-commercial-guides-api
- baseURL: https://data.trade.gov
  baseurl_source: declared
  description: Tariff rates and import requirements for U.S. exports across global markets via the Customs Info Database.
  name: International Trade Administration Customs Tariff API
  slug: international-trade-administration-customs-tariff-api
- baseURL: https://data.trade.gov
  baseurl_source: declared
  description: Country-level customs de minimis values - the threshold below which duty and tax do not apply to imported goods.
  name: International Trade Administration De Minimis API
  slug: international-trade-administration-de-minimis-api
- baseURL: https://data.trade.gov
  baseurl_source: declared
  description: Curated market intelligence articles authored by ITA's network of international trade specialists.
  name: International Trade Administration Market Intelligence API
  slug: international-trade-administration-market-intelligence-api
- baseURL: https://data.trade.gov
  baseurl_source: declared
  description: Aggregated international trade events including trade missions, conferences, webinars, and trade shows from federal partners.
  name: International Trade Administration Trade Events API
  slug: international-trade-administration-trade-events-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: International Trade Administration Data Services Consolidated Screening List API
  slug: open-international-trade-administration-consolidated-screening-list-api
- collection_type: open
  name: International Trade Administration Data Services Consolidated Screening List Country Commercial Guides API
  slug: open-international-trade-administration-country-commercial-guides-api
- collection_type: open
  name: International Trade Administration Data Services Consolidated Screening List Customs Tariff API
  slug: open-international-trade-administration-customs-tariff-api
- collection_type: open
  name: International Trade Administration Data Services Consolidated Screening List De Minimis API
  slug: open-international-trade-administration-de-minimis-api
- collection_type: open
  name: International Trade Administration Data Services Consolidated Screening List Market Intelligence API
  slug: open-international-trade-administration-market-intelligence-api
- collection_type: open
  name: International Trade Administration Data Services Consolidated Screening List Trade Events API
  slug: open-international-trade-administration-trade-events-api
- collection_type: open
  name: International Trade Administration Data Services API
  slug: open-international-trade-administration
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/international-trade-administration-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/international-trade-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/international-trade-administration-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/international-trade-administration-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InternationalTradeAdministration
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/international-trade-administration
- group: start
  title: ''
  type: Portal
  url: https://developer.trade.gov
- group: company
  title: ''
  type: Website
  url: https://www.trade.gov
- group: docs
  title: ''
  type: Documentation
  url: https://developer.trade.gov
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.trade.gov/getting-started
- group: start
  title: ''
  type: Signup
  url: https://developer.trade.gov/user/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.trade.gov/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://developer.trade.gov/contact
created: '2024-12-03'
description: The International Trade Administration (ITA) creates prosperity by strengthening the international competitiveness of U.S. industry, promoting trade and investment, and ensuring fair trade and compliance with trade laws and agreements. ITA's Data Services Platform provides authoritative APIs for U.S. exporting and international trade including the Consolidated Screening List, Country Commercial Guides, Market Intelligence, Trade Events, Customs Tariff lookups, and De Minimis thresholds.
finops:
- name: International Trade Administration Finops
  service_category: API
  slug: international-trade-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/international-trade-administration.png
layout: provider
modified: '2026-05-19'
name: International Trade Administration
nav: Providers
network: true
overview: 'International Trade Administration publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Consolidated Screening List API, Country Commercial Guides API, Customs Tariff API, and 3 more. Tagged areas include Compliance, Customs, Export, Federal-Government, and International Business.


  The International Trade Administration catalog on APIs.io includes 1 Spectral governance ruleset.


  International Trade Administration''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, support, and 7 more developer resources.'
plans:
- name: International Trade Administration Plans Pricing
  plan_count: 3
  slug: international-trade-administration-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: International Trade Administration Rate Limits
  slug: international-trade-administration-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: International Trade Administration API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: international-trade-administration-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 12
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/international-trade-administration/refs/heads/main/screenshots/international-trade-administration-2026-06-20T183459.png
security:
- kind: authentication
  name: International Trade Administration Authentication
  slug: international-trade-administration-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: International Trade Administration Domain Security
  slug: international-trade-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: international-trade-administration
tags:
- Compliance
- Customs
- Export
- Federal-Government
- International Business
- Screening List
- Tariffs
- Trade
- Trade Data
- Trade Events
website: https://www.trade.gov
---
