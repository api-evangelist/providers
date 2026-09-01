---
access_model:
  confidence: high
  label: No public API — aggregator/FDX access only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - developer-portal-probe
  - openbankingtracker
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.comerica.com
- group: other
  title: ''
  type: Personal
  url: https://www.comerica.com/personal-finance.html
- group: other
  title: ''
  type: SmallBusiness
  url: https://www.comerica.com/small-business.html
- group: other
  title: ''
  type: Commercial
  url: https://www.comerica.com/business.html
- group: other
  title: ''
  type: WealthManagement
  url: https://www.comerica.com/wealth-management.html
- group: other
  title: ''
  type: CashManagement
  url: https://www.comerica.com/business/solutions/cash-management.html
- group: other
  title: ''
  type: CommercialInformationManagement
  url: https://www.comerica.com/business/solutions/cash-management/commercial-information-management.html
- group: other
  title: ''
  type: OnlineBanking
  url: https://www.comerica.com/personal-finance/services/online-and-mobile-banking.html
- group: company
  title: ''
  type: Blog
  url: https://www.comerica.com/insights.html
- group: operate
  title: ''
  type: Support
  url: https://www.comerica.com/site-tools/resources/contact-us.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.comerica.com/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.comerica.com/legal
- group: auth
  title: ''
  type: Security
  url: https://www.comerica.com/security-commitment
- group: other
  title: ''
  type: FraudCenter
  url: https://www.comerica.com/fraud-center.html
- group: company
  title: ''
  type: Investors
  url: https://investor.comerica.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/comerica-bank
- group: auth
  title: ''
  type: DomainSecurity
  url: security/comerica-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/comerica-llms.txt
- group: other
  title: ''
  type: AggregatorPlaid
  url: https://plaid.com/institutions/
- group: other
  title: ''
  type: AggregatorAkoya
  url: https://akoya.com/
- group: other
  title: ''
  type: FDXStandard
  url: https://financialdataexchange.org/
- group: other
  title: ''
  type: Acquirer
  url: https://www.53.com/
created: '2026-03-23'
description: 'Comerica Incorporated is a Texas-headquartered super-regional financial services holding company providing retail, small-business, commercial, and wealth-management banking across the United States, with market concentrations in Texas, California, Michigan, Arizona, and Florida. As of July 2026 Comerica publishes NO first-party developer API portal: developer.comerica.com, api.comerica.com, and related developer subdomains do not resolve, and directory trackers (Open Banking Tracker, API Tracker) list no documented API products, OpenAPI/Swagger specs, SDKs, or Postman collections. Consumer and small-business account data is reached indirectly through US open-finance aggregators (Plaid, MX, Finicity, Akoya) and through Financial Data Exchange (FDX) APIs — the CFPB-recognized standard-setting body for the Section 1033 Personal Financial Data Rights rule — rather than a Comerica-published endpoint. Commercial treasury, cash-positioning, ACH/wire initiation, and reporting are delivered
  through Comerica''s Cash Management and Commercial Information Management platforms under direct customer contract (host-to-host files, portal, and BAI/ISO 20022 feeds), not a public REST API. Note: Fifth Third Bancorp completed its all-stock acquisition of Comerica in February 2026, so Comerica''s future digital and API surface is being integrated into Fifth Third''s platform.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/comerica.png
layout: provider
modified: '2026-07-23'
name: Comerica
nav: Providers
network: true
overview: 'Comerica is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Commercial Banking, Financial-Services, Retail Banking, and Wealth Management.


  Comerica''s developer surface includes engineering blog, support, and 20 more developer resources.'
press:
- date: '2026-05-25'
  title: Inaugural Comerica Bank Survey Finds Small Businesses ...
  url: https://www.prnewswire.com/news-releases/inaugural-comerica-bank-survey-finds-small-businesses-optimistic-about-growth-cautious-about-ai-and-focused-on-strategic-investment-302539952.html
- date: '2026-05-25'
  title: 'Automation 101: Technology is Expanding Financial and ...'
  url: https://www.comerica.com/insights/business-finance/automation-101-how-technology-is-expanding-financial-and-banking-services.html
- date: '2026-05-25'
  title: Comerica Bank
  url: https://www.facebook.com/comerica/posts/join-comerica-bank-for-our-next-outlook-on-america-a-virtual-event-with-bill-ada/1292023612955029/
- date: '2026-05-25'
  title: 'Making the Case for AI in Finance: Insights from Strategic ...'
  url: https://www.itemize.com/making-the-case-for-ai-in-finance/
- date: '2026-05-25'
  title: Comerica says its AI bot performs work of six IT help desk ...
  url: https://www.americanbanker.com/news/comerica-says-its-ai-bot-performs-work-of-six-it-helpdesk-agents
random_paper: 16
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 6.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/comerica/refs/heads/main/screenshots/comerica-2026-06-20T174802.png
security:
- kind: domain-security
  name: Comerica Domain Security
  slug: comerica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: comerica
tags:
- Banking
- Commercial Banking
- Financial-Services
- Retail Banking
- Wealth Management
- Treasury Management
- Open Banking
- Super-Regional Bank
- United States
- Fortune 1000
website: https://www.comerica.com
---
