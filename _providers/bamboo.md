---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 30
  human_in_the_loop: 22
  name: Bamboo Agentic Access
  operation_count: 102
  slug: bamboo-agentic-access
  summary_line: 102 operations · 30 acting · 22 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: Account creation enables users to invest on Bamboo. Ensure KYC has been completed and each user’s identity verified before creating a brokerage account. **Best Practice:** To avoid maintenance fees on
  name: Bamboo Invest Account Management API
  slug: bamboo-account-management-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: Before you start making requests, you’ll need to generate an access token. Every request to the API must be authenticated using access tokens and user context headers — this ensures secure and authori
  name: Bamboo Invest Authentication API
  slug: bamboo-authentication-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: Deposits fund user brokerage accounts for stock purchases. All deposits require verification through your webhook endpoint before funds are credited. On the <a href="#tag/US-Stock-Portfolio/operation/
  name: Bamboo Invest Deposits API
  slug: bamboo-deposits-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: The exchange rate section provides you with an endpoint that fetches real-time exchange rates effortlessly, enabling accurate currency conversions and financial calculations.
  name: Bamboo Invest Exchange Rate API
  slug: bamboo-exchange-rate-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: 'Stocks are grouped into various categories which help users explore and filter stocks based on common themes, sectors, or other criteria. The endpoints in this section allow you to retrieve a list of '
  name: Bamboo Invest Featured Themes API
  slug: bamboo-featured-themes-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: 'Access various financial documents required for user account management, tax reporting, and regulatory compliance through secure document retrieval endpoints. ##### Document Types and Generation The s'
  name: Bamboo Invest Financial Documents API
  slug: bamboo-financial-documents-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: 'The Https: API from Bamboo Invest — 1 operation(s) for https:.'
  name: 'Bamboo Invest Https: API'
  slug: bamboo-https-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: The Lsx API from Bamboo Invest — 1 operation(s) for lsx.
  name: Bamboo Invest Lsx API
  slug: bamboo-lsx-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: 'The market activity section provides you with endpoints that return the opening and closing times for markets we support, allowing you to check when market is open/closed. This endpoint supports **US '
  name: Bamboo Invest Market Activity API
  slug: bamboo-market-activity-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: The NG Deposits API from Bamboo Invest — 2 operation(s) for ng deposits.
  name: Bamboo Invest NG Deposits API
  slug: bamboo-ng-deposits-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: The section provides us endpoints that allows a client to fetch all the information pertaining to the NG stocks available on Bamboo.
  name: Bamboo Invest NG Securities API
  slug: bamboo-ng-securities-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: This section provides all the information a tenant needs to know about a user's investment portfolio values and general user performance.
  name: Bamboo Invest NG Stock Portfolio API
  slug: bamboo-ng-stock-portfolio-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: The stock trading section details all the endpoints needed to calculate and make trade orders for all NG stock available on Bamboo. Please note that trade charges are applicable and should be agreed u
  name: Bamboo Invest NG Stock Trading API
  slug: bamboo-ng-stock-trading-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: The NG Withdrawals API from Bamboo Invest — 2 operation(s) for ng withdrawals.
  name: Bamboo Invest NG Withdrawals API
  slug: bamboo-ng-withdrawals-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: The One Step Registration API from Bamboo Invest — 1 operation(s) for one step registration.
  name: Bamboo Invest One Step Registration API
  slug: bamboo-one-step-registration-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: The user's portfolio provides comprehensive views of investment performance, cash positions, and account status. Understanding the different cash types and portfolio calculations is essential for pres
  name: Bamboo Invest Portfolio Reporting API
  slug: bamboo-portfolio-reporting-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: The Stock Trading API from Bamboo Invest — 1 operation(s) for stock trading.
  name: Bamboo Invest Stock Trading API
  slug: bamboo-stock-trading-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: The Tenant API from Bamboo Invest — 1 operation(s) for tenant.
  name: Bamboo Invest Tenant API
  slug: bamboo-tenant-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: 'The section provides comprehensive information about available US stocks, including real-time pricing, company details, and market data. Stock themes also help users discover investment opportunities '
  name: Bamboo Invest US Securities API
  slug: bamboo-us-securities-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: 'Users can buy and sell US securities, with support for multiple order types and fractional shares. Understanding order calculations, execution timing, and fees is crucial for integration. ### Trading '
  name: Bamboo Invest US Stock Trading API
  slug: bamboo-us-stock-trading-api
- baseURL: https://api.investbamboo.com
  baseurl_source: declared
  description: 'Withdrawals allow users to extract funds from their brokerage accounts after successful trades. Understanding the settlement timeline is essential. #### Settlement Timeline - Stock sale proceeds settl'
  name: Bamboo Invest Withdrawals API
  slug: bamboo-withdrawals-api
artifact_total: 113
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bamboo Account Management API
  slug: open-bamboo-account-management-api
- collection_type: open
  name: Bamboo Account Management Authentication API
  slug: open-bamboo-authentication-api
- collection_type: open
  name: Bamboo Account Management Deposits API
  slug: open-bamboo-deposits-api
- collection_type: open
  name: Bamboo Account Management Exchange Rate API
  slug: open-bamboo-exchange-rate-api
- collection_type: open
  name: Bamboo Account Management Featured Themes API
  slug: open-bamboo-featured-themes-api
- collection_type: open
  name: Bamboo Account Management Financial Documents API
  slug: open-bamboo-financial-documents-api
- collection_type: open
  name: 'Bamboo Account Management Https: API'
  slug: open-bamboo-https-api
- collection_type: open
  name: Bamboo Account Management Lsx API
  slug: open-bamboo-lsx-api
- collection_type: open
  name: Bamboo Account Management Market Activity API
  slug: open-bamboo-market-activity-api
- collection_type: open
  name: Bamboo Account Management NG Deposits API
  slug: open-bamboo-ng-deposits-api
- collection_type: open
  name: Bamboo Account Management NG Securities API
  slug: open-bamboo-ng-securities-api
- collection_type: open
  name: Bamboo Account Management NG Stock Portfolio API
  slug: open-bamboo-ng-stock-portfolio-api
- collection_type: open
  name: Bamboo Account Management NG Stock Trading API
  slug: open-bamboo-ng-stock-trading-api
- collection_type: open
  name: Bamboo Account Management NG Withdrawals API
  slug: open-bamboo-ng-withdrawals-api
- collection_type: open
  name: Bamboo Account Management One Step Registration API
  slug: open-bamboo-one-step-registration-api
- collection_type: open
  name: Bamboo Account Management Portfolio Reporting API
  slug: open-bamboo-portfolio-reporting-api
- collection_type: open
  name: Bamboo Account Management Stock Trading API
  slug: open-bamboo-stock-trading-api
- collection_type: open
  name: Bamboo Account Management Tenant API
  slug: open-bamboo-tenant-api
- collection_type: open
  name: Bamboo Account Management US Securities API
  slug: open-bamboo-us-securities-api
- collection_type: open
  name: Bamboo Account Management US Stock Trading API
  slug: open-bamboo-us-stock-trading-api
- collection_type: open
  name: Bamboo Account Management Withdrawals API
  slug: open-bamboo-withdrawals-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bamboo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bamboo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://investbamboo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.investbamboo.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/investbamboo
- group: company
  title: ''
  type: LinkedIn
  url: https://ng.linkedin.com/company/investbamboo
- group: company
  title: ''
  type: Blog
  url: https://learn.investbamboo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://faq.investbamboo.com/en/collections/1988034-fees
- group: operate
  title: ''
  type: StatusPage
  url: https://status.investbamboo.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/investbamboo
- group: commercial
  title: ''
  type: Plans
  url: plans/bamboo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bamboo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bamboo-finops.yml
created: '2026-06-13'
description: Bamboo is an African investment platform providing REST APIs for fractional stock investing, dollar investments, portfolio management, and access to US and Nigerian capital markets. The APIs enable fintech partners to integrate brokerage account creation, money movement, stock trading, and portfolio tracking into their own financial services applications.
examples:
- key_count: 1
  name: Get_Api_Lsx_Ng_Dictionary_422_Response
  slug: get_api_lsx_ng_dictionary_422_response
- key_count: 1
  name: Get_Api_Lsx_Ng_Withdraw_Reference_422_Response
  slug: get_api_lsx_ng_withdraw_reference_422_response
- key_count: 1
  name: Get_Https__Cscs Banks.Investbamboo.Com_422_Response
  slug: get_https__cscs-banks.investbamboo.com_422_response
- key_count: 1
  name: Post_Api_Lsx_Ng_Deposit_422_Response
  slug: post_api_lsx_ng_deposit_422_response
- key_count: 1
  name: Post_Api_Lsx_Ng_Withdraw_422_Response
  slug: post_api_lsx_ng_withdraw_422_response
- key_count: 1
  name: Post_Api_Tenant_Brokerage_Withdraw_422_Response
  slug: post_api_tenant_brokerage_withdraw_422_response
- key_count: 1
  name: Post_Bamboo_Webhook_422_Response
  slug: post_bamboo_webhook_422_response
finops:
- name: Bamboo Finops
  service_category: ''
  slug: bamboo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bamboo.png
json_schemas:
- name: Deposit request for Banking Institutions
  property_count: 7
  slug: bamboowebhook
- name: Calculated order response
  property_count: 9
  slug: calculatedorderresponse
- name: Order Cancelled
  property_count: 0
  slug: cancelorderstockidresponse
- name: Supported banks and sortcodes
  property_count: 1
  slug: cscs_banks_and_sortcodes
- name: Deposit request for non-banking institutions
  property_count: 5
  slug: depositrequest
- name: Deposit Details
  property_count: 8
  slug: depositresponse
- name: Status of a Deposit
  property_count: 4
  slug: depositstatus
- name: US Dictionary response
  property_count: 9
  slug: dictionaryresponse
- name: Error changeset response
  property_count: 2
  slug: errorchangesetresponse
- name: Error response
  property_count: 1
  slug: errorresponse
- name: Exchange rates response
  property_count: 1
  slug: exchangeratesresponse
- name: Investment Profile response
  property_count: 13
  slug: investmentprofileresponse
- name: LimitOrderRequest
  property_count: 7
  slug: limitorderrequest
- name: Calculate order request
  property_count: 6
  slug: lsxngcalculate_order
- name: Calculated order response
  property_count: 10
  slug: lsxngcalculate_order_response
- name: Cancel an Order on the NGX
  property_count: 1
  slug: lsxngcancel_orders_response
- name: Deposit request
  property_count: 5
  slug: lsxngdeposit
- name: Deposit request
  property_count: 9
  slug: lsxngdeposit_by_reference_response
- name: Deposit response
  property_count: 9
  slug: lsxngdeposit_response
- name: NGX Dictionary
  property_count: 1
  slug: lsxngdictionary
- name: Array of users NGX stocks
  property_count: 2
  slug: lsxngmy_stocks_response
- name: NGX place order request
  property_count: 10
  slug: lsxngorder
- name: NGX Order details response
  property_count: 16
  slug: lsxngorder_details_response
- name: Order response
  property_count: 1
  slug: lsxngorder_response
- name: NGX Order status response
  property_count: 11
  slug: lsxngorder_status_response
- name: NGX Pending Order Response
  property_count: 2
  slug: lsxngpending_order_response
- name: NGX Portfolio response
  property_count: 8
  slug: lsxngportfolio_breakdown_response
- name: Stock About Info
  property_count: 13
  slug: lsxngstock_about_info
- name: List of all active stocks response
  property_count: 2
  slug: lsxngstocks_response
- name: User's Cash Balance
  property_count: 2
  slug: lsxnguser_cash_balance_response
- name: NGX Withdrawal Request body
  property_count: 3
  slug: lsxngwithdraw
- name: Withdraw status
  property_count: 2
  slug: lsxngwithdraw_by_reference_response
- name: Withdrawal response
  property_count: 2
  slug: lsxngwithdraw_response
- name: MarketOrderRequest
  property_count: 5
  slug: marketorderrequest
- name: Order status response
  property_count: 20
  slug: orderstatusresponse
- name: Order id response
  property_count: 1
  slug: orderstockidresponse
- name: Order Placement Parameters
  property_count: 11
  slug: orderstockrequest
- name: List of pending orders
  property_count: 2
  slug: pendingordersresponse
- name: Portfolio breakdown response
  property_count: 12
  slug: portfoliobreakdownresponse
- name: Portfolio response
  property_count: 30
  slug: portfolioresponse
- name: Profile response
  property_count: 17
  slug: profileresponse
- name: Resource not found
  property_count: 1
  slug: resourcenotfound
- name: Stock Pricing Details
  property_count: 28
  slug: stockdetails
- name: List of all active stocks response
  property_count: 2
  slug: stockslistresponse
- name: List of all Stock Search Results
  property_count: 2
  slug: stockssearchresponse
- name: StopOrderRequest
  property_count: 7
  slug: stoporderrequest
- name: Tenant Brokerage Request body for NGN
  property_count: 4
  slug: tenantbrokeragewithdrawbody
- name: List of all deposits with pagination
  property_count: 2
  slug: tenantdepositspaginationresponse
- name: List of all withdrawals with pagination
  property_count: 2
  slug: tenantwithdrawspaginationresponse
- name: List of all themes
  property_count: 2
  slug: themeslistingresponse
- name: Unauthorized response
  property_count: 1
  slug: unauthorized
- name: List of Documents by Document Type
  property_count: 1
  slug: usdocumentlist
- name: URL to download a Single Document
  property_count: 1
  slug: usdocuments
- name: User Stock Ownership
  property_count: 3
  slug: userstockownership
- name: US Market Activity response
  property_count: 3
  slug: usmarketactivitystatus
- name: User Ownership Details
  property_count: 3
  slug: usownershipresponse
- name: Withdraw status
  property_count: 4
  slug: withdrawstatusresponse
layout: provider
modified: '2026-06-13'
name: Bamboo Invest
nav: Providers
network: true
overview: 'Bamboo Invest publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Account Management API, Authentication API, Deposits API, and 18 more. Tagged areas include Investments, Stocks, Fractional Shares, Africa, and Nigeria.


  The Bamboo Invest catalog on APIs.io includes 1 Spectral governance ruleset.


  Bamboo Invest''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Bamboo Plans Pricing
  plan_count: 3
  slug: bamboo-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Bamboo Rate Limits
  slug: bamboo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Bamboo Invest API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bamboo-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 59.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 50.5
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bamboo/refs/heads/main/screenshots/bamboo-2026-06-20T172931.png
security:
- kind: domain-security
  name: Bamboo Domain Security
  slug: bamboo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bamboo
tags:
- Investments
- Stocks
- Fractional Shares
- Africa
- Nigeria
- Portfolio-Management
- Brokerage
- Fintech
website: https://investbamboo.com/
---
