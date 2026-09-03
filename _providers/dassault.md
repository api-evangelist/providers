---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Dassault Agentic Access
  operation_count: 10
  slug: dassault-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- description: REST API for managing manufacturing item data, manufacturing BOMs, and process plans on the 3DEXPERIENCE platform used in production and factory planning.
  name: 3DEXPERIENCE Manufacturing Web Services
  slug: 3dexperience-manufacturing-web-services
- description: REST API for CAD collaboration and coordination on the 3DEXPERIENCE platform, enabling integration with SolidWorks, CATIA, and other CAD tools for managing design data and versions.
  name: 3DEXPERIENCE CAD Collaboration Web Services
  slug: 3dexperience-cad-collaboration-web-services
- description: REST API for managing manufacturing processes, process plans, and operations on the 3DEXPERIENCE platform, supporting digital manufacturing and process simulation workflows.
  name: 3DEXPERIENCE Manufacturing Process Web Services
  slug: 3dexperience-manufacturing-process-web-services
- description: REST API for project management and task handling on the 3DEXPERIENCE platform, enabling integration with project schedules, milestones, and team assignments within ENOVIA applications.
  name: 3DEXPERIENCE Project Task Web Services
  slug: 3dexperience-project-task-web-services
- description: REST API for change and issue tracking on the 3DEXPERIENCE platform, supporting engineering change orders, problem reports, and corrective actions within the product lifecycle.
  name: 3DEXPERIENCE Issue Web Services
  slug: 3dexperience-issue-web-services
- description: REST API for Dassault Systèmes channel partners to manage orders, price lists, accreditations, leads, and portfolio items through the partner gateway, using API key authentication.
  name: API4Partners
  slug: api4partners
- baseURL: https://apigw-prd.3ds.com
  baseurl_source: declared
  description: This section defines all the operations related to accreditations, including the search of accreditations for a specfic partner.
  name: Dassault Systèmes accreditations API
  slug: dassault-accreditations-api
- baseURL: https://apigw-prd.3ds.com
  baseurl_source: declared
  description: This section defines the operations related to API keys . Current API key management still requires some interaction with Dassault Systèmes Information System (IS) team. This process will likely be up
  name: Dassault Systèmes apikeys API
  slug: dassault-apikeys-api
- baseURL: https://apigw-prd.3ds.com
  baseurl_source: declared
  description: This section defines the operations related to leads and opportunities for sales pipeline management. These ressources are managed with 'MySalesPipeline' application which implements Dassault Systèmes
  name: Dassault Systèmes leads-opportunities API
  slug: dassault-leads-opportunities-api
- baseURL: https://apigw-prd.3ds.com
  baseurl_source: declared
  description: 'This section defines the operations related to orders, including the creation, management, and fulfillment of orders. It provides a comprehensive overview of the order lifecycle, from initial request '
  name: Dassault Systèmes orders API
  slug: dassault-orders-api
- baseURL: https://apigw-prd.3ds.com
  baseurl_source: declared
  description: This section defines the operations related to sales portfolio-items. The portfolio items are used in the definition of leads-opportunities in 'MySalesPipeline' application.
  name: Dassault Systèmes portfolio-items API
  slug: dassault-portfolio-items-api
- baseURL: https://apigw-prd.3ds.com
  baseurl_source: declared
  description: This section defines all the operations related to price lists, including the search of price lists for a specfic partner.
  name: Dassault Systèmes price-lists API
  slug: dassault-price-lists-api
artifact_total: 175
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: APIs for Dassault Systèmes Partners accreditations API
  slug: open-dassault-accreditations-api
- collection_type: open
  name: APIs for Dassault Systèmes Partners accreditations apikeys API
  slug: open-dassault-apikeys-api
- collection_type: open
  name: APIs for Dassault Systèmes Partners accreditations leads-opportunities API
  slug: open-dassault-leads-opportunities-api
- collection_type: open
  name: APIs for Dassault Systèmes Partners accreditations orders API
  slug: open-dassault-orders-api
- collection_type: open
  name: APIs for Dassault Systèmes Partners accreditations portfolio-items API
  slug: open-dassault-portfolio-items-api
- collection_type: open
  name: APIs for Dassault Systèmes Partners accreditations price-lists API
  slug: open-dassault-price-lists-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dassault-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dassault-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dassault-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dassault-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.3ds.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.3ds.com/support/documentation/developer-guides
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/3ds-cpe-emed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dassaultsystemes
- group: company
  title: ''
  type: Blog
  url: https://blog.3ds.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.3ds.com/store
- group: operate
  title: ''
  type: StatusPage
  url: https://www.3ds.com/trust-center/availability
- group: other
  title: ''
  type: X
  url: https://x.com/dassault3ds
- group: commercial
  title: ''
  type: Plans
  url: plans/dassault-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dassault-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dassault-finops.yml
created: '2026-06-13'
description: Dassault Systèmes provides the 3DEXPERIENCE platform with thousands of publicly available REST APIs for product design, simulation, and manufacturing industries. The platform covers SolidWorks, CATIA, ENOVIA, and 3D collaboration tools, exposing web services across engineering items, manufacturing processes, CAD collaboration, project tasks, and partner order management through standardized RESTful endpoints.
examples:
- key_count: 1
  name: Createleadsopportunities Request Createleadbasic
  slug: createLeadsOpportunities-request-createLeadBasic
- key_count: 1
  name: Createleadsopportunities Request Createopportunitybasic
  slug: createLeadsOpportunities-request-createOpportunityBasic
- key_count: 5
  name: Createleadsopportunities Response 201 200_Leadsopportunitiescreateresponse
  slug: createLeadsOpportunities-response-201-200_leadsOpportunitiesCreateResponse
- key_count: 3
  name: Createleadsopportunities Response 400 400_Alreadyexisting
  slug: createLeadsOpportunities-response-400-400_alreadyExisting
- key_count: 3
  name: Createleadsopportunities Response 400 400_Leadsopportunitiescreateresponse
  slug: createLeadsOpportunities-response-400-400_leadsOpportunitiesCreateResponse
- key_count: 1
  name: Createleadsopportunities Response 401 401_Missing Apikey
  slug: createLeadsOpportunities-response-401-401_missing-apikey
- key_count: 1
  name: Createleadsopportunities Response 403 403_Forbidden
  slug: createLeadsOpportunities-response-403-403_forbidden
- key_count: 3
  name: Createleadsopportunities Response 406 406_Incorrectclosedatenextmilestoneformat
  slug: createLeadsOpportunities-response-406-406_IncorrectCloseDateNextMilestoneFormat
- key_count: 1
  name: Createleadsopportunities Response 429 429_Too_Many_Requests
  slug: createLeadsOpportunities-response-429-429_too_many_requests
- key_count: 3
  name: Createleadsopportunities Response 503 503_Serviceunavailable
  slug: createLeadsOpportunities-response-503-503_ServiceUnavailable
- key_count: 1
  name: Generateapikey Response 401 401_Missing Apikey
  slug: generateApiKey-response-401-401_missing-apikey
- key_count: 1
  name: Generateapikey Response 403 403_Forbidden
  slug: generateApiKey-response-403-403_forbidden
- key_count: 1
  name: Generateapikey Response 429 429_Too_Many_Requests
  slug: generateApiKey-response-429-429_too_many_requests
- key_count: 3
  name: Getleadsopportunities Response 200 200_Leadsopportunitiesgetresponse
  slug: getLeadsOpportunities-response-200-200_leadsOpportunitiesGetResponse
- key_count: 1
  name: Getleadsopportunities Response 401 401_Missing Apikey
  slug: getLeadsOpportunities-response-401-401_missing-apikey
- key_count: 1
  name: Getleadsopportunities Response 403 403_Forbidden
  slug: getLeadsOpportunities-response-403-403_forbidden
- key_count: 1
  name: Getleadsopportunities Response 429 429_Too_Many_Requests
  slug: getLeadsOpportunities-response-429-429_too_many_requests
- key_count: 3
  name: Getleadsopportunities Response 500 500_Leadsopportunitiesgetresponse
  slug: getLeadsOpportunities-response-500-500_leadsOpportunitiesGetResponse
- key_count: 3
  name: Getleadsopportunities Response 503 503_Serviceunavailable
  slug: getLeadsOpportunities-response-503-503_ServiceUnavailable
- key_count: 2
  name: Getorderdetails Response 200 Successful_Getorderdetails
  slug: getOrderDetails-response-200-successful_getOrderDetails
- key_count: 3
  name: Getorderdetails Response 400 Failedorderget_Badrequest
  slug: getOrderDetails-response-400-failedOrderGet_BadRequest
- key_count: 1
  name: Getorderdetails Response 401 401_Missing Apikey
  slug: getOrderDetails-response-401-401_missing-apikey
- key_count: 1
  name: Getorderdetails Response 403 403_Forbidden
  slug: getOrderDetails-response-403-403_forbidden
- key_count: 3
  name: Getorderdetails Response 404 Failedorderget_Badrequest
  slug: getOrderDetails-response-404-failedOrderGet_BadRequest
- key_count: 1
  name: Getorderdetails Response 429 429_Too_Many_Requests
  slug: getOrderDetails-response-429-429_too_many_requests
- key_count: 2
  name: Searchaccreditations Response 200 Successful_Accreditations_Search_Noresult
  slug: searchAccreditations-response-200-successful_accreditations_search_noResult
- key_count: 2
  name: Searchaccreditations Response 200 Successful_Accreditations_Search_Threeresult
  slug: searchAccreditations-response-200-successful_accreditations_search_threeResult
- key_count: 3
  name: Searchaccreditations Response 400 Failedaccreditationsearch_Badrequest_Skipnegativenumber
  slug: searchAccreditations-response-400-failedAccreditationSearch_BadRequest_skipNegativeNumber
- key_count: 3
  name: Searchaccreditations Response 400 Failedaccreditationsearch_Badrequest_Topoutsiderange
  slug: searchAccreditations-response-400-failedAccreditationSearch_BadRequest_topOutsideRange
- key_count: 1
  name: Searchaccreditations Response 401 401_Missing Apikey
  slug: searchAccreditations-response-401-401_missing-apikey
- key_count: 1
  name: Searchaccreditations Response 403 403_Forbidden
  slug: searchAccreditations-response-403-403_forbidden
- key_count: 1
  name: Searchaccreditations Response 429 429_Too_Many_Requests
  slug: searchAccreditations-response-429-429_too_many_requests
- key_count: 1
  name: Searchleadsopportunities Request Search_Combined
  slug: searchLeadsOpportunities-request-search_combined
- key_count: 1
  name: Searchleadsopportunities Request Search_Modifieddate
  slug: searchLeadsOpportunities-request-search_modifiedDate
- key_count: 1
  name: Searchleadsopportunities Request Search_Partnerleadopportunityid Unassigned
  slug: searchLeadsOpportunities-request-search_partnerLeadOpportunityId-unassigned
- key_count: 1
  name: Searchleadsopportunities Request Search_Partnerleadopportunityid
  slug: searchLeadsOpportunities-request-search_partnerLeadOpportunityId
- key_count: 3
  name: Searchleadsopportunities Response 200 200_Lead Opportunities_Search
  slug: searchLeadsOpportunities-response-200-200_lead-opportunities_search
- key_count: 3
  name: Searchleadsopportunities Response 400 400_Lead Opportunities_Search_Missingfromtodate
  slug: searchLeadsOpportunities-response-400-400_lead-opportunities_search_missingFromToDate
- key_count: 1
  name: Searchleadsopportunities Response 401 401_Missing Apikey
  slug: searchLeadsOpportunities-response-401-401_missing-apikey
- key_count: 1
  name: Searchleadsopportunities Response 403 403_Forbidden
  slug: searchLeadsOpportunities-response-403-403_forbidden
- key_count: 1
  name: Searchleadsopportunities Response 429 429_Too_Many_Requests
  slug: searchLeadsOpportunities-response-429-429_too_many_requests
- key_count: 3
  name: Searchleadsopportunities Response 503 503_Serviceunavailable
  slug: searchLeadsOpportunities-response-503-503_ServiceUnavailable
- key_count: 4
  name: Searchorders Request Advancedsearchmultiplecriteria
  slug: searchOrders-request-advancedSearchMultipleCriteria
- key_count: 1
  name: Searchorders Request Basicsearchsinglecriteria
  slug: searchOrders-request-basicSearchSingleCriteria
- key_count: 2
  name: Searchorders Response 200 200_Orderssearch_No Result
  slug: searchOrders-response-200-200_ordersSearch_No-Result
- key_count: 2
  name: Searchorders Response 200 Successful_Orderssearch_Oneresult
  slug: searchOrders-response-200-successful_ordersSearch_OneResult
- key_count: 3
  name: Searchorders Response 400 Failedordersearch_Badrequest
  slug: searchOrders-response-400-failedOrderSearch_BadRequest
- key_count: 1
  name: Searchorders Response 401 401_Missing Apikey
  slug: searchOrders-response-401-401_missing-apikey
- key_count: 1
  name: Searchorders Response 403 403_Forbidden
  slug: searchOrders-response-403-403_forbidden
- key_count: 1
  name: Searchorders Response 429 429_Too_Many_Requests
  slug: searchOrders-response-429-429_too_many_requests
- key_count: 2
  name: Searchportfolioitems Response 200 200_Portfolioitemssearchgetresponse
  slug: searchPortfolioItems-response-200-200_portfolioItemsSearchGetResponse
- key_count: 2
  name: Searchportfolioitems Response 400 400_Portfolioitemssearchgetresponse
  slug: searchPortfolioItems-response-400-400_portfolioItemsSearchGetResponse
- key_count: 1
  name: Searchportfolioitems Response 401 401_Missing Apikey
  slug: searchPortfolioItems-response-401-401_missing-apikey
- key_count: 1
  name: Searchportfolioitems Response 403 403_Forbidden
  slug: searchPortfolioItems-response-403-403_forbidden
- key_count: 1
  name: Searchportfolioitems Response 429 429_Too_Many_Requests
  slug: searchPortfolioItems-response-429-429_too_many_requests
- key_count: 2
  name: Searchpricelist Response 200 Successful_Pricelists_Search
  slug: searchPriceList-response-200-successful_priceLists_search
- key_count: 2
  name: Searchpricelist Response 200 Successful_Pricelists_Search_Noresult
  slug: searchPriceList-response-200-successful_priceLists_search_noResult
- key_count: 1
  name: Searchpricelist Response 401 401_Missing Apikey
  slug: searchPriceList-response-401-401_missing-apikey
- key_count: 1
  name: Searchpricelist Response 403 403_Forbidden
  slug: searchPriceList-response-403-403_forbidden
- key_count: 1
  name: Searchpricelist Response 429 429_Too_Many_Requests
  slug: searchPriceList-response-429-429_too_many_requests
- key_count: 1
  name: Updateleadopportunitiesdetails Request Updateleadnextmilestone
  slug: updateLeadOpportunitiesDetails-request-updateLeadNextMilestone
- key_count: 1
  name: Updateleadopportunitiesdetails Request Updateleadstatus
  slug: updateLeadOpportunitiesDetails-request-updateLeadStatus
- key_count: 3
  name: Updateleadopportunitiesdetails Response 200 200_Leadsopportunitiescreateresponse
  slug: updateLeadOpportunitiesDetails-response-200-200_leadsOpportunitiesCreateResponse
- key_count: 3
  name: Updateleadopportunitiesdetails Response 400 400_Leadsopportunitiescreateresponse
  slug: updateLeadOpportunitiesDetails-response-400-400_leadsOpportunitiesCreateResponse
- key_count: 1
  name: Updateleadopportunitiesdetails Response 401 401_Missing Apikey
  slug: updateLeadOpportunitiesDetails-response-401-401_missing-apikey
- key_count: 1
  name: Updateleadopportunitiesdetails Response 403 403_Forbidden
  slug: updateLeadOpportunitiesDetails-response-403-403_forbidden
- key_count: 3
  name: Updateleadopportunitiesdetails Response 406 406_Incorrectclosedatenextmilestoneformat
  slug: updateLeadOpportunitiesDetails-response-406-406_IncorrectCloseDateNextMilestoneFormat
- key_count: 1
  name: Updateleadopportunitiesdetails Response 429 429_Too_Many_Requests
  slug: updateLeadOpportunitiesDetails-response-429-429_too_many_requests
- key_count: 3
  name: Updateleadopportunitiesdetails Response 503 503_Serviceunavailable
  slug: updateLeadOpportunitiesDetails-response-503-503_ServiceUnavailable
finops:
- name: Dassault Finops
  service_category: ''
  slug: dassault-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dassault.png
json_schemas:
- name: 200 Accreditations Search
  property_count: 3
  slug: 200_accreditations_search
- name: 200 Get Leads Opportunities
  property_count: 3
  slug: 200_get_leads-opportunities
- name: 200 Get Orders
  property_count: 3
  slug: 200_get_orders
- name: 200 Get Portfolio Items Search
  property_count: 2
  slug: 200_get_portfolio-items_search
- name: 200 Patch Leads Opportunities
  property_count: 3
  slug: 200_patch_leads-opportunities
- name: 200 Post Apikeys
  property_count: 2
  slug: 200_post_apikeys
- name: 200 Post Leads Opportunities Search
  property_count: 3
  slug: 200_post_leads-opportunities_search
- name: 200 Post Orders Search
  property_count: 3
  slug: 200_post_orders_search
- name: 200 Price Lists Search
  property_count: 3
  slug: 200_price-lists_search
- name: 201 Post Leads Opportunities
  property_count: 5
  slug: 201_post_leads-opportunities
- name: 400 Accreditations Search
  property_count: 3
  slug: 400_accreditations_search
- name: 400 Get Portfolio Items Search
  property_count: 2
  slug: 400_get_portfolio-items_search
- name: 400 Patch Leads Opportunities
  property_count: 3
  slug: 400_patch_leads-opportunities
- name: 400 Post Leads Opportunities
  property_count: 3
  slug: 400_post_leads-opportunities
- name: 400 Post Orders Search
  property_count: 3
  slug: 400_post_orders_search
- name: 401 Basic Unauthorized
  property_count: 1
  slug: 401_basic_unauthorized
- name: 403 Basic Forbidden
  property_count: 1
  slug: 403_basic_forbidden
- name: 406 Leads Opportunities
  property_count: 3
  slug: 406_leads-opportunities
- name: 429 Too Many Requests
  property_count: 1
  slug: 429_too_many_requests
- name: 4Xx Get Orders
  property_count: 3
  slug: 4xx_get_orders
- name: 500 Get Leads Opportunities
  property_count: 4
  slug: 500_get_leads-opportunities
- name: 503 Leads Opportunities
  property_count: 3
  slug: 503_leads-opportunities
- name: Accreditations Search Data
  property_count: 0
  slug: accreditations_search_data
- name: Billto Po Reference
  property_count: 0
  slug: billto_po_reference
- name: Billto Sales Representative
  property_count: 0
  slug: billto_sales_representative
- name: Booking Datetime
  property_count: 0
  slug: booking_datetime
- name: Business Unit
  property_count: 3
  slug: business_unit
- name: Country
  property_count: 0
  slug: country
- name: Country Code
  property_count: 0
  slug: country_code
- name: Country Name
  property_count: 0
  slug: country_name
- name: Creation Datetime
  property_count: 0
  slug: creation_datetime
- name: Currency
  property_count: 0
  slug: currency
- name: Customercontact
  property_count: 6
  slug: customerContact
- name: Customerlegalentity
  property_count: 12
  slug: customerLegalEntity
- name: Date Time From
  property_count: 0
  slug: date_time_from
- name: Date Time To
  property_count: 0
  slug: date_time_to
- name: Dsowneremail
  property_count: 0
  slug: dsOwnerEmail
- name: Ds Offering
  property_count: 0
  slug: ds_offering
- name: Ds Received Po Date
  property_count: 0
  slug: ds_received_po_date
- name: Error
  property_count: 0
  slug: error
- name: Forecastcategory
  property_count: 0
  slug: forecastCategory
- name: Info
  property_count: 3
  slug: info
- name: Info Response Base Attributes
  property_count: 3
  slug: info_response_base_attributes
- name: Info Response Portfolio Items
  property_count: 0
  slug: info_response_portfolio-items
- name: Installed Base Number
  property_count: 0
  slug: installed_base_number
- name: Lead Opportunity Status
  property_count: 0
  slug: lead-opportunity-status
- name: Lead Opportunity Attributes
  property_count: 16
  slug: lead-opportunity_attributes
- name: Lead Opportunity Patch
  property_count: 0
  slug: lead-opportunity_patch
- name: Lead Opportunity Post
  property_count: 0
  slug: lead-opportunity_post
- name: Legal Entity
  property_count: 4
  slug: legal_entity
- name: Local Time Zone
  property_count: 0
  slug: local_time_zone
- name: Offerline
  property_count: 3
  slug: offerLine
- name: Online Consent Status
  property_count: 0
  slug: online_consent_status
- name: Online Instance Seat Id
  property_count: 0
  slug: online_instance_seat_id
- name: Order Get Data
  property_count: 0
  slug: order_get_data
- name: Order Line
  property_count: 8
  slug: order_line
- name: Order Processing Status
  property_count: 0
  slug: order_processing_status
- name: Order Revenue Type
  property_count: 0
  slug: order_revenue_type
- name: Order Sub Line
  property_count: 25
  slug: order_sub_line
- name: Order Type
  property_count: 0
  slug: order_type
- name: Orders Search Data
  property_count: 0
  slug: orders_search_data
- name: Orders Search Req
  property_count: 7
  slug: orders_search_req
- name: Partnercontact
  property_count: 3
  slug: partnerContact
- name: Partnerleadopportunityid
  property_count: 0
  slug: partnerLeadOpportunityId
- name: Patch Leads Opportunities Data
  property_count: 6
  slug: patch_leads-opportunities_data
- name: Portfolio Items Data
  property_count: 7
  slug: portfolio-items_data
- name: Post Leads Opportunities Data
  property_count: 6
  slug: post_leads-opportunities_data
- name: Post Leads Opportunities Search
  property_count: 1
  slug: post_leads-opportunities_search
- name: Price Lists Search Data
  property_count: 0
  slug: price-lists_search_data
- name: Product Type
  property_count: 0
  slug: product_type
- name: Reason Lost
  property_count: 0
  slug: reason_lost
- name: Reason Won
  property_count: 0
  slug: reason_won
- name: Recurring Charge Billing Cycle
  property_count: 0
  slug: recurring_charge_billing_cycle
- name: Revenuetype
  property_count: 0
  slug: revenueType
- name: Sub Order Type
  property_count: 0
  slug: sub_order_type
- name: Transaction
  property_count: 4
  slug: transaction
- name: Transaction Type
  property_count: 0
  slug: transaction_type
jsonld:
- class_count: 0
  name: Dassault Api Context
  property_count: 0
  slug: dassault-api
- class_count: 16
  name: Dassault Context
  property_count: 0
  slug: dassault-context
layout: provider
modified: '2026-06-13'
name: Dassault Systèmes
nav: Providers
network: true
overview: 'Dassault Systèmes publishes 6 APIs on the [APIs.io](https://apis.io/) network, including accreditations API, apikeys API, leads-opportunities API, and 3 more. Tagged areas include 3DEXPERIENCE, PLM, Product Lifecycle Management, CAD, and Manufacturing.


  The Dassault Systèmes catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Dassault Systèmes'' developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Dassault Plans Pricing
  plan_count: 3
  slug: dassault-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Dassault Rate Limits
  slug: dassault-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Dassault Systèmes API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dassault-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 64.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dassault/refs/heads/main/screenshots/dassault-2026-06-20T175506.png
security:
- kind: authentication
  name: Dassault Authentication
  slug: dassault-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dassault Domain Security
  slug: dassault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dassault Trust Center
  slug: dassault-trust-center
  summary_line: ISO 27001, GDPR
slug: dassault
tags:
- 3DEXPERIENCE
- PLM
- Product Lifecycle Management
- CAD
- Manufacturing
- SolidWorks
- CATIA
- ENOVIA
- Engineering
- 3D Collaboration
website: https://www.3ds.com
---
