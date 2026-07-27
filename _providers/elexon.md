---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Elexon Agentic Access
  operation_count: 312
  slug: elexon-agentic-access
  summary_line: 312 operations
api_count: 32
apis:
- description: Dynamic data.
  name: Elexon Balancing Mechanism Dynamic API
  slug: elexon-balancing-mechanism-dynamic-api
- description: Physical data consists of PN, QPN, MILS, &amp; MELS.
  name: Elexon Balancing Mechanism Physical API
  slug: elexon-balancing-mechanism-physical-api
- description: Adjustment actions (DISBSAD) for a given settlement period, or summarised by settlement period over a time range.
  name: Elexon Balancing Services Adjustment - Disaggregated API
  slug: elexon-balancing-services-adjustment-disaggregated-api
- description: Net balancing services adjustment data (NETBSAD), provided as a time series or filtered to events.
  name: Elexon Balancing Services Adjustment - Net API
  slug: elexon-balancing-services-adjustment-net-api
- description: Bid-offer acceptance data (BOALF).
  name: Elexon Bid-Offer Acceptances API
  slug: elexon-bid-offer-acceptances-api
- description: Bid-offer data.
  name: Elexon Bid-Offer API
  slug: elexon-bid-offer-api
- description: Raw datasets as received from the National Grid, with associated metadata. The output in JSON format matches IRIS, and can be used interchangeably with IRIS output.
  name: Elexon BMRS Datasets API
  slug: elexon-bmrs-datasets-api
- description: Credit Default Notice data.
  name: Elexon Credit Default Notice API
  slug: elexon-credit-default-notice-api
- description: The number of datapoints ingested for a dataset in a given period of time, grouped by settlement period.
  name: Elexon Data Status API
  slug: elexon-data-status-api
- description: GB electricity demand, including historic.
  name: Elexon Demand API
  slug: elexon-demand-api
- description: Current or historic demand forecasts.
  name: Elexon Demand Forecast API
  slug: elexon-demand-forecast-api
- description: GB electricity generation output, including historic.
  name: Elexon Generation API
  slug: elexon-generation-api
- description: Current or historic generation forecasts.
  name: Elexon Generation Forecast API
  slug: elexon-generation-forecast-api
- description: Provides an endpoint to check the health of the Insights API service.
  name: Elexon Health Check API
  slug: elexon-health-check-api
- description: Day-and-day-ahead indicated forecast, categorized as Indicated Generation (INDGEN), Indicated Demand (INDDEM), Imbalance (IMBALNGC) and Margin (MELNGC).
  name: Elexon Indicated Forecast API
  slug: elexon-indicated-forecast-api
- description: Data related to the settlement process.
  name: Elexon Indicative Imbalance Settlement API
  slug: elexon-indicative-imbalance-settlement-api
- description: The Legacy API from Elexon — 2 operation(s) for legacy.
  name: Elexon Legacy API
  slug: elexon-legacy-api
- description: Load shape period data and load shape totals data as calculated by the Load Shaping Service
  name: Elexon Load Shape API
  slug: elexon-load-shape-api
- description: Loss of load probability and de-rated margin forecast data.
  name: Elexon Loss of Load Probability and De-rated Margin API
  slug: elexon-loss-of-load-probability-and-de-rated-margin-api
- description: Generating Plant Operating Margin forecast data, including historical views of data by publish time or forecast date.
  name: Elexon Margin Forecast API
  slug: elexon-margin-forecast-api
- description: Market Index prices filtered by time.
  name: Elexon Market Index API
  slug: elexon-market-index-api
- description: Short Term Operating Reserves (STOR) data, provided as a time series or filtered to events.
  name: Elexon Non-BM STOR API
  slug: elexon-non-bm-stor-api
- description: Balancing services volume data, filtered by BM Unit and time range.
  name: Elexon Non-BM Volumes API
  slug: elexon-non-bm-volumes-api
- description: Reference data which can be used to filter other API requests.
  name: Elexon Reference API
  slug: elexon-reference-api
- description: REMIT messages, including previous revisions.
  name: Elexon REMIT API
  slug: elexon-remit-api
- description: The Rolling System Demand API from Elexon — 1 operation(s) for rolling system demand.
  name: Elexon Rolling System Demand API
  slug: elexon-rolling-system-demand-api
- description: Datasets received from the Settlement Administration Agent (SAA)
  name: Elexon SAA Datasets API
  slug: elexon-saa-datasets-api
- description: SO-SO Prices (SOSO) data, filtered by start time.
  name: Elexon SO-SO Prices API
  slug: elexon-so-so-prices-api
- description: Generating Plant Operating Surplus forecast data, including historical views of data by publish time or forecast date.
  name: Elexon Surplus Forecast API
  slug: elexon-surplus-forecast-api
- description: Transmission System data.
  name: Elexon System API
  slug: elexon-system-api
- description: Transmission System forecasts
  name: Elexon System forecast API
  slug: elexon-system-forecast-api
- description: Daily average & reference temperatures.
  name: Elexon Temperature API
  slug: elexon-temperature-api
artifact_total: 355
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elexon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elexon-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.data.elexon.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://bmrs.elexon.co.uk/api-documentation/guidance
- group: docs
  title: ''
  type: OpenAPI
  url: https://data.elexon.co.uk/swagger/v1/swagger.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elexon.co.uk/bsc/data/balancing-mechanism-reporting-agent/copyright-licence-bmrs-data/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elexon.co.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/elexon-data
- group: build
  title: ''
  type: GitHub
  url: https://github.com/elexon-data/insights-docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/elexon-data/insights-issues
- group: build
  title: ''
  type: GitHub
  url: https://github.com/elexon-data/iris-clients
- group: company
  title: ''
  type: Blog
  url: https://www.elexon.co.uk/news-insights/
- group: operate
  title: ''
  type: Support
  url: mailto:insightssupport@elexon.co.uk
- group: commercial
  title: ''
  type: Plans
  url: plans/elexon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elexon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/elexon-finops.yml
created: '2026-06-13'
description: Elexon is the UK's Balancing and Settlement Code (BSC) Company, responsible for administering the electricity balancing and settlement arrangements in Great Britain. As the operator of the Balancing Mechanism Reporting Service (BMRS), Elexon publishes a publicly accessible REST API — the Insights Solution API — that provides free, no-key access to real-time and historical data from the UK electricity market. The API covers balancing mechanism dynamic and physical data per Balancing Mechanism Unit (BMU), bid-offer acceptances, balancing services adjustments, physical notifications, generation availability forecasts, settlement reports, meter readings, and UK market transparency data mandated under European legislation. All data is returned in JSON, XML, or CSV format. A companion near-real-time push service (IRIS — Insights Real-time Information Service) streams the same datasets over WebSocket/STOMP for latency-sensitive consumers. The API is freely accessible to industry participants
  and the public with no registration or API key required, and data may be reused with attribution ("Contains BMRS data © Elexon Limited copyright and database right").
examples:
- key_count: 5
  name: Get_Balancing_Acceptances_200
  slug: get_balancing_acceptances_200
- key_count: 5
  name: Get_Balancing_Acceptances_Acceptancenumber_200
  slug: get_balancing_acceptances_acceptanceNumber_200
- key_count: 5
  name: Get_Balancing_Acceptances_All_200
  slug: get_balancing_acceptances_all_200
- key_count: 5
  name: Get_Balancing_Acceptances_All_Latest_200
  slug: get_balancing_acceptances_all_latest_200
- key_count: 5
  name: Get_Balancing_Bid Offer_200
  slug: get_balancing_bid-offer_200
- key_count: 5
  name: Get_Balancing_Bid Offer_All_200
  slug: get_balancing_bid-offer_all_200
- key_count: 5
  name: Get_Balancing_Dynamic_200
  slug: get_balancing_dynamic_200
- key_count: 5
  name: Get_Balancing_Dynamic_All_200
  slug: get_balancing_dynamic_all_200
- key_count: 5
  name: Get_Balancing_Dynamic_Rates_200
  slug: get_balancing_dynamic_rates_200
- key_count: 5
  name: Get_Balancing_Dynamic_Rates_All_200
  slug: get_balancing_dynamic_rates_all_200
- key_count: 5
  name: Get_Balancing_Nonbm_Disbsad_Details_200
  slug: get_balancing_nonbm_disbsad_details_200
- key_count: 5
  name: Get_Balancing_Nonbm_Disbsad_Summary_200
  slug: get_balancing_nonbm_disbsad_summary_200
- key_count: 5
  name: Get_Balancing_Nonbm_Netbsad_200
  slug: get_balancing_nonbm_netbsad_200
- key_count: 5
  name: Get_Balancing_Nonbm_Netbsad_Events_200
  slug: get_balancing_nonbm_netbsad_events_200
- key_count: 5
  name: Get_Balancing_Physical_200
  slug: get_balancing_physical_200
- key_count: 5
  name: Get_Balancing_Physical_All_200
  slug: get_balancing_physical_all_200
- key_count: 5
  name: Get_Datasets_Nonbm_200
  slug: get_datasets_NONBM_200
- key_count: 5
  name: Get_Datasets_Nonbm_Stream_200
  slug: get_datasets_NONBM_stream_200
- key_count: 5
  name: Get_Datasets_Pn_200
  slug: get_datasets_PN_200
- key_count: 5
  name: Get_Datasets_Pn_Stream_200
  slug: get_datasets_PN_stream_200
finops:
- name: Elexon Finops
  service_category: Analytics and Data
  slug: elexon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elexon.png
json_schemas:
- name: Insights.Api.LegacyInteroperability.LegacyRemitDetailBody
  property_count: 2
  slug: Insights.Api.LegacyInteroperability.LegacyRemitDetailBody
- name: Insights.Api.LegacyInteroperability.LegacyRemitDetailItem
  property_count: 27
  slug: Insights.Api.LegacyInteroperability.LegacyRemitDetailItem
- name: Insights.Api.LegacyInteroperability.LegacyRemitDetailList
  property_count: 1
  slug: Insights.Api.LegacyInteroperability.LegacyRemitDetailList
- name: Insights.Api.LegacyInteroperability.LegacyRemitDetailMetadata
  property_count: 4
  slug: Insights.Api.LegacyInteroperability.LegacyRemitDetailMetadata
- name: Insights.Api.LegacyInteroperability.LegacyRemitDetailResponse
  property_count: 2
  slug: Insights.Api.LegacyInteroperability.LegacyRemitDetailResponse
- name: Insights.Api.LegacyInteroperability.LegacyRemitListItem
  property_count: 28
  slug: Insights.Api.LegacyInteroperability.LegacyRemitListItem
- name: Insights.Api.LegacyInteroperability.LegacyRemitListMetadata
  property_count: 6
  slug: Insights.Api.LegacyInteroperability.LegacyRemitListMetadata
- name: Insights.Api.LegacyInteroperability.LegacyRemitListResponse
  property_count: 2
  slug: Insights.Api.LegacyInteroperability.LegacyRemitListResponse
- name: Insights.Api.LegacyInteroperability.LegacyRemitListResponseBody
  property_count: 2
  slug: Insights.Api.LegacyInteroperability.LegacyRemitListResponseBody
- name: Insights.Api.LegacyInteroperability.LegacyRemitOutageProfile
  property_count: 1
  slug: Insights.Api.LegacyInteroperability.LegacyRemitOutageProfile
- name: Insights.Api.LegacyInteroperability.LegacyRemitOutageProfileSegment
  property_count: 3
  slug: Insights.Api.LegacyInteroperability.LegacyRemitOutageProfileSegment
- name: Insights.Api.LegacyInteroperability.LegacyRemitResponseList
  property_count: 1
  slug: Insights.Api.LegacyInteroperability.LegacyRemitResponseList
- name: Insights.Api.Models.Data.Entities.LoadShapePeriodData
  property_count: 16
  slug: Insights.Api.Models.Data.Entities.LoadShapePeriodData
- name: Insights.Api.Models.Data.Entities.LoadShapeTotalsData
  property_count: 18
  slug: Insights.Api.Models.Data.Entities.LoadShapeTotalsData
- name: Insights.Api.Models.Metadata.ApiResponseSourceMetadata
  property_count: 1
  slug: Insights.Api.Models.Metadata.ApiResponseSourceMetadata
- name: Insights.Api.Models.Metadata.RemitApiResponseSourceMetadata
  property_count: 2
  slug: Insights.Api.Models.Metadata.RemitApiResponseSourceMetadata
- name: Insights.Api.Models.Requests.DataStatus.RemitDataSource
  property_count: 0
  slug: Insights.Api.Models.Requests.DataStatus.RemitDataSource
- name: Insights.Api.Models.Responses.Balancing.BalancingServicesVolume
  property_count: 6
  slug: Insights.Api.Models.Responses.Balancing.BalancingServicesVolume
- name: Insights.Api.Models.Responses.Balancing.BidOfferAcceptancesResponse
  property_count: 15
  slug: Insights.Api.Models.Responses.Balancing.BidOfferAcceptancesResponse
- name: Insights.Api.Models.Responses.Balancing.BidOfferResponse
  property_count: 11
  slug: Insights.Api.Models.Responses.Balancing.BidOfferResponse
- name: Insights.Api.Models.Responses.Balancing.CreditDefaultNoticeResponse
  property_count: 8
  slug: Insights.Api.Models.Responses.Balancing.CreditDefaultNoticeResponse
- name: Insights.Api.Models.Responses.Balancing.DatasetRows.BalancingServicesVolumeData
  property_count: 6
  slug: Insights.Api.Models.Responses.Balancing.DatasetRows.BalancingServicesVolumeData
- name: Insights.Api.Models.Responses.Balancing.DatasetRows.BidOfferAcceptanceLevelDatasetResponse
  property_count: 17
  slug: Insights.Api.Models.Responses.Balancing.DatasetRows.BidOfferAcceptanceLevelDatasetResponse
- name: Insights.Api.Models.Responses.Balancing.DatasetRows.BidOfferDatasetResponse
  property_count: 12
  slug: Insights.Api.Models.Responses.Balancing.DatasetRows.BidOfferDatasetResponse
- name: Insights.Api.Models.Responses.Balancing.DatasetRows.CreditDefaultNoticeDatasetResponse
  property_count: 9
  slug: Insights.Api.Models.Responses.Balancing.DatasetRows.CreditDefaultNoticeDatasetResponse
- name: Insights.Api.Models.Responses.Balancing.DatasetRows.DisaggregatedBalancingServicesAdjustmentData
  property_count: 12
  slug: Insights.Api.Models.Responses.Balancing.DatasetRows.DisaggregatedBalancingServicesAdjustmentData
- name: Insights.Api.Models.Responses.Balancing.DatasetRows.MarketIndexDatasetResponse
  property_count: 7
  slug: Insights.Api.Models.Responses.Balancing.DatasetRows.MarketIndexDatasetResponse
- name: Insights.Api.Models.Responses.Balancing.DatasetRows.NetBalancingServicesAdjustmentData
  property_count: 11
  slug: Insights.Api.Models.Responses.Balancing.DatasetRows.NetBalancingServicesAdjustmentData
- name: Insights.Api.Models.Responses.Balancing.DisaggregatedBalancingServicesAdjustmentDetailsResponse
  property_count: 13
  slug: Insights.Api.Models.Responses.Balancing.DisaggregatedBalancingServicesAdjustmentDetailsResponse
- name: Insights.Api.Models.Responses.Balancing.DisaggregatedBalancingServicesAdjustmentSummaryResponse
  property_count: 14
  slug: Insights.Api.Models.Responses.Balancing.DisaggregatedBalancingServicesAdjustmentSummaryResponse
- name: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryPeriodMaxData
  property_count: 7
  slug: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryPeriodMaxData
- name: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryPeriodMinData
  property_count: 7
  slug: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryPeriodMinData
- name: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryVolumeMaxData
  property_count: 7
  slug: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryVolumeMaxData
- name: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.MaximumDeliveryBidData
  property_count: 11
  slug: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.MaximumDeliveryBidData
- name: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.MaximumDeliveryOfferData
  property_count: 11
  slug: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.MaximumDeliveryOfferData
- name: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.NoticeData
  property_count: 7
  slug: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.NoticeData
- name: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.StablePortageLimitData
  property_count: 7
  slug: Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.StablePortageLimitData
- name: Insights.Api.Models.Responses.Balancing.Dynamic.DynamicData
  property_count: 7
  slug: Insights.Api.Models.Responses.Balancing.Dynamic.DynamicData
- name: Insights.Api.Models.Responses.Balancing.Dynamic.DynamicParametersData
  property_count: 11
  slug: Insights.Api.Models.Responses.Balancing.Dynamic.DynamicParametersData
- name: Insights.Api.Models.Responses.Balancing.Dynamic.RateData
  property_count: 11
  slug: Insights.Api.Models.Responses.Balancing.Dynamic.RateData
- name: Insights.Api.Models.Responses.Balancing.MarketIndexResponse
  property_count: 6
  slug: Insights.Api.Models.Responses.Balancing.MarketIndexResponse
- name: Insights.Api.Models.Responses.Balancing.NetBalancingServicesAdjustmentResponse
  property_count: 11
  slug: Insights.Api.Models.Responses.Balancing.NetBalancingServicesAdjustmentResponse
- name: Insights.Api.Models.Responses.Balancing.NonBmStorResponse
  property_count: 5
  slug: Insights.Api.Models.Responses.Balancing.NonBmStorResponse
- name: Insights.Api.Models.Responses.Balancing.Physical.DatasetRows.DeliveryLimitMaxData
  property_count: 11
  slug: Insights.Api.Models.Responses.Balancing.Physical.DatasetRows.DeliveryLimitMaxData
- name: Insights.Api.Models.Responses.Balancing.Physical.DatasetRows.PhysicalNotificationData
  property_count: 9
  slug: Insights.Api.Models.Responses.Balancing.Physical.DatasetRows.PhysicalNotificationData
- name: Insights.Api.Models.Responses.Balancing.Physical.PhysicalData
  property_count: 9
  slug: Insights.Api.Models.Responses.Balancing.Physical.PhysicalData
- name: Insights.Api.Models.Responses.Balancing.Settlement.AcceptanceVolumeResponse
  property_count: 12
  slug: Insights.Api.Models.Responses.Balancing.Settlement.AcceptanceVolumeResponse
- name: Insights.Api.Models.Responses.Balancing.Settlement.DerivedDataBidOfferPairs
  property_count: 12
  slug: Insights.Api.Models.Responses.Balancing.Settlement.DerivedDataBidOfferPairs
- name: Insights.Api.Models.Responses.Balancing.Settlement.HistoricAcceptanceResponse
  property_count: 9
  slug: Insights.Api.Models.Responses.Balancing.Settlement.HistoricAcceptanceResponse
- name: Insights.Api.Models.Responses.Balancing.Settlement.IndicativeCashflowResponse
  property_count: 10
  slug: Insights.Api.Models.Responses.Balancing.Settlement.IndicativeCashflowResponse
- name: Insights.Api.Models.Responses.Balancing.Settlement.IndicativeVolumeResponse
  property_count: 11
  slug: Insights.Api.Models.Responses.Balancing.Settlement.IndicativeVolumeResponse
- name: Insights.Api.Models.Responses.Balancing.Settlement.MarketDepthResponse
  property_count: 9
  slug: Insights.Api.Models.Responses.Balancing.Settlement.MarketDepthResponse
- name: Insights.Api.Models.Responses.Balancing.Settlement.SettlementMessageResponse
  property_count: 8
  slug: Insights.Api.Models.Responses.Balancing.Settlement.SettlementMessageResponse
- name: Insights.Api.Models.Responses.Balancing.Settlement.SettlementStackResponse
  property_count: 23
  slug: Insights.Api.Models.Responses.Balancing.Settlement.SettlementStackResponse
- name: Insights.Api.Models.Responses.Balancing.Settlement.SettlementSummaryPrice
  property_count: 3
  slug: Insights.Api.Models.Responses.Balancing.Settlement.SettlementSummaryPrice
- name: Insights.Api.Models.Responses.Balancing.Settlement.SettlementSummaryResponse
  property_count: 10
  slug: Insights.Api.Models.Responses.Balancing.Settlement.SettlementSummaryResponse
- name: Insights.Api.Models.Responses.Balancing.Settlement.SystemPriceResponse
  property_count: 22
  slug: Insights.Api.Models.Responses.Balancing.Settlement.SystemPriceResponse
- name: Insights.Api.Models.Responses.DataStatus.DataStatusResponse
  property_count: 3
  slug: Insights.Api.Models.Responses.DataStatus.DataStatusResponse
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.CreditDefaultNoticeResponse
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.CreditDefaultNoticeResponse
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.BalancingServicesVolumeData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.BalancingServicesVolumeData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.BidOfferAcceptanceLevelDatasetResponse
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.BidOfferAcceptanceLevelDatasetResponse
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.BidOfferDatasetResponse
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.BidOfferDatasetResponse
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.CreditDefaultNoticeDatasetResponse
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.CreditDefaultNoticeDatasetResponse
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.DisaggregatedBalancingServicesAdjustmentData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.DisaggregatedBalancingServicesAdjustmentData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.MarketIndexDatasetResponse
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.MarketIndexDatasetResponse
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.NetBalancingServicesAdjustmentData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.DatasetRows.NetBalancingServicesAdjustmentData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryPeriodMaxData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryPeriodMaxData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryPeriodMinData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryPeriodMinData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryVolumeMaxData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.DeliveryVolumeMaxData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.MaximumDeliveryBidData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.MaximumDeliveryBidData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.MaximumDeliveryOfferData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.MaximumDeliveryOfferData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.NoticeData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.NoticeData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.StablePortageLimitData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.DatasetRows.StablePortageLimitData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.RateData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Dynamic.RateData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Physical.DatasetRows.DeliveryLimitMaxData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Physical.DatasetRows.DeliveryLimitMaxData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Physical.DatasetRows.PhysicalNotificationData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Balancing.Physical.DatasetRows.PhysicalNotificationData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalDaily
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalDaily
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalDayAhead
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalDayAhead
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalWeekly
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalWeekly
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastTransmissionDaily
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastTransmissionDaily
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastTransmissionDayAhead
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastTransmissionDayAhead
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastTransmissionWeekly
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastTransmissionWeekly
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandOutturn.DatasetRows.DemandOutturnNational
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandOutturn.DatasetRows.DemandOutturnNational
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandOutturn.DatasetRows.DemandOutturnTransmission
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandOutturn.DatasetRows.DemandOutturnTransmission
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandOutturn.DatasetRows.IndodDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.DemandOutturn.DatasetRows.IndodDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.ForecastMargin.DatasetRows.ForecastMarginDaily
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.ForecastMargin.DatasetRows.ForecastMarginDaily
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.ForecastMargin.DatasetRows.ForecastMarginWeekly
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.ForecastMargin.DatasetRows.ForecastMarginWeekly
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.ForecastSurplus.DatasetRows.ForecastSurplusDaily
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.ForecastSurplus.DatasetRows.ForecastSurplusDaily
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.ForecastSurplus.DatasetRows.ForecastSurplusWeekly
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.ForecastSurplus.DatasetRows.ForecastSurplusWeekly
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AugmentedOutturnData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AugmentedOutturnData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByBmUnitDaily
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByBmUnitDaily
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByBmUnitWeekly
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByBmUnitWeekly
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByFuelTypeDaily
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByFuelTypeDaily
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByFuelTypeWeekly
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByFuelTypeWeekly
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityDaily
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityDaily
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityWeekly
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityWeekly
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.NonBmStorData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.NonBmStorData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.WindGenerationForecast
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Generation.DatasetRows.WindGenerationForecast
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedDemand
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedDemand
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedGeneration
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedGeneration
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedImbalance
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedImbalance
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedMargin
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedMargin
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.DemandControlInstructionDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.DemandControlInstructionDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.LossOfLoadProbabilityDeratedMarginData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.LossOfLoadProbabilityDeratedMarginData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.SoSoPricesDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.SoSoPricesDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.SystemFrequency
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.SystemFrequency
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.SystemWarningsData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.SystemWarningsData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.TemperatureData
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.TemperatureData
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.TudmDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Misc.DatasetRows.TudmDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Reference.DatasetMetadataLatestRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Reference.DatasetMetadataLatestRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.RestorationZone.RestorationZoneDemandForecastDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.RestorationZone.RestorationZoneDemandForecastDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.RestorationZone.RestorationZoneDemandRestoredDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.RestorationZone.RestorationZoneDemandRestoredDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.AbucDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.AbucDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.ActualAggregatedGenerationPerTypeDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.ActualAggregatedGenerationPerTypeDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.ActualGenerationOutputPerGenerationUnitDatasetResponse
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.ActualGenerationOutputPerGenerationUnitDatasetResponse
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.ActualGenerationWindSolarDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.ActualGenerationWindSolarDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.ActualTotalLoadPerBiddingZoneDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.ActualTotalLoadPerBiddingZoneDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.AobeDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.AobeDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.BebDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.BebDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.CbsDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.CbsDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.CostsOfCongestionManagementDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.CostsOfCongestionManagementDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.DayAheadAggregatedGenerationDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.DayAheadAggregatedGenerationDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.DayAheadGenerationForWindAndSolarDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.DayAheadGenerationForWindAndSolarDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.DayAheadTotalLoadPerBiddingZoneDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.DayAheadTotalLoadPerBiddingZoneDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.FeibDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.FeibDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.IgcaDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.IgcaDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.IgcpuDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.IgcpuDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.MonthAheadTotalLoadPerBiddingZoneDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.MonthAheadTotalLoadPerBiddingZoneDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.PbcDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.PbcDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.PpbrDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.PpbrDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.WeekAheadTotalLoadPerBiddingZoneDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.WeekAheadTotalLoadPerBiddingZoneDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.YearAheadForecastMarginDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.YearAheadForecastMarginDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.YearAheadTotalLoadPerBiddingZoneDatasetRow
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.DatasetRows.YearAheadTotalLoadPerBiddingZoneDatasetRow
- name: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.Remit.DatasetRows.RemitMessage
  property_count: 1
  slug: Insights.Api.Models.Responses.DatasetResponse-1_Insights.Api.Models.Responses.Transparency.Remit.DatasetRows.RemitMessage
- name: Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalDaily
  property_count: 4
  slug: Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalDaily
- name: Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalDayAhead
  property_count: 7
  slug: Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalDayAhead
- name: Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalWeekly
  property_count: 5
  slug: Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastNationalWeekly
- name: Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastTransmissionDaily
  property_count: 4
  slug: Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastTransmissionDaily
- name: Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastTransmissionDayAhead
  property_count: 7
  slug: Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastTransmissionDayAhead
- name: Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastTransmissionWeekly
  property_count: 5
  slug: Insights.Api.Models.Responses.DemandForecast.DatasetRows.DemandForecastTransmissionWeekly
- name: Insights.Api.Models.Responses.DemandForecast.DemandForecastDaily
  property_count: 4
  slug: Insights.Api.Models.Responses.DemandForecast.DemandForecastDaily
- name: Insights.Api.Models.Responses.DemandForecast.DemandForecastDayAhead
  property_count: 7
  slug: Insights.Api.Models.Responses.DemandForecast.DemandForecastDayAhead
- name: Insights.Api.Models.Responses.DemandForecast.DemandForecastPeak
  property_count: 6
  slug: Insights.Api.Models.Responses.DemandForecast.DemandForecastPeak
- name: Insights.Api.Models.Responses.DemandForecast.DemandForecastWeekly
  property_count: 6
  slug: Insights.Api.Models.Responses.DemandForecast.DemandForecastWeekly
- name: Insights.Api.Models.Responses.DemandOutturn.DatasetRows.DemandOutturnNational
  property_count: 6
  slug: Insights.Api.Models.Responses.DemandOutturn.DatasetRows.DemandOutturnNational
- name: Insights.Api.Models.Responses.DemandOutturn.DatasetRows.DemandOutturnTransmission
  property_count: 6
  slug: Insights.Api.Models.Responses.DemandOutturn.DatasetRows.DemandOutturnTransmission
- name: Insights.Api.Models.Responses.DemandOutturn.DatasetRows.IndodDatasetRow
  property_count: 4
  slug: Insights.Api.Models.Responses.DemandOutturn.DatasetRows.IndodDatasetRow
- name: Insights.Api.Models.Responses.DemandOutturn.DemandOutturn
  property_count: 6
  slug: Insights.Api.Models.Responses.DemandOutturn.DemandOutturn
- name: Insights.Api.Models.Responses.DemandOutturn.DemandOutturnPeak
  property_count: 5
  slug: Insights.Api.Models.Responses.DemandOutturn.DemandOutturnPeak
- name: Insights.Api.Models.Responses.DemandOutturn.IndicativeDemandPeak
  property_count: 5
  slug: Insights.Api.Models.Responses.DemandOutturn.IndicativeDemandPeak
- name: Insights.Api.Models.Responses.DemandOutturn.IndodRow
  property_count: 3
  slug: Insights.Api.Models.Responses.DemandOutturn.IndodRow
- name: Insights.Api.Models.Responses.DemandOutturn.RollingSystemDemand
  property_count: 3
  slug: Insights.Api.Models.Responses.DemandOutturn.RollingSystemDemand
- name: Insights.Api.Models.Responses.ForecastMargin.DatasetRows.ForecastMarginDaily
  property_count: 4
  slug: Insights.Api.Models.Responses.ForecastMargin.DatasetRows.ForecastMarginDaily
- name: Insights.Api.Models.Responses.ForecastMargin.DatasetRows.ForecastMarginWeekly
  property_count: 5
  slug: Insights.Api.Models.Responses.ForecastMargin.DatasetRows.ForecastMarginWeekly
- name: Insights.Api.Models.Responses.ForecastMargin.ForecastMarginDaily
  property_count: 3
  slug: Insights.Api.Models.Responses.ForecastMargin.ForecastMarginDaily
- name: Insights.Api.Models.Responses.ForecastMargin.ForecastMarginWeekly
  property_count: 5
  slug: Insights.Api.Models.Responses.ForecastMargin.ForecastMarginWeekly
- name: Insights.Api.Models.Responses.ForecastSurplus.DatasetRows.ForecastSurplusDaily
  property_count: 4
  slug: Insights.Api.Models.Responses.ForecastSurplus.DatasetRows.ForecastSurplusDaily
- name: Insights.Api.Models.Responses.ForecastSurplus.DatasetRows.ForecastSurplusWeekly
  property_count: 5
  slug: Insights.Api.Models.Responses.ForecastSurplus.DatasetRows.ForecastSurplusWeekly
- name: Insights.Api.Models.Responses.ForecastSurplus.ForecastSurplusDaily
  property_count: 3
  slug: Insights.Api.Models.Responses.ForecastSurplus.ForecastSurplusDaily
- name: Insights.Api.Models.Responses.ForecastSurplus.ForecastSurplusWeekly
  property_count: 5
  slug: Insights.Api.Models.Responses.ForecastSurplus.ForecastSurplusWeekly
- name: Insights.Api.Models.Responses.Generation.AvailabilityDaily
  property_count: 7
  slug: Insights.Api.Models.Responses.Generation.AvailabilityDaily
- name: Insights.Api.Models.Responses.Generation.AvailabilityWeekly
  property_count: 8
  slug: Insights.Api.Models.Responses.Generation.AvailabilityWeekly
- name: Insights.Api.Models.Responses.Generation.DatasetRows.AugmentedOutturnData
  property_count: 7
  slug: Insights.Api.Models.Responses.Generation.DatasetRows.AugmentedOutturnData
- name: Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByBmUnitDaily
  property_count: 7
  slug: Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByBmUnitDaily
- name: Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByBmUnitWeekly
  property_count: 8
  slug: Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByBmUnitWeekly
- name: Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByFuelTypeDaily
  property_count: 10
  slug: Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByFuelTypeDaily
- name: Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByFuelTypeWeekly
  property_count: 10
  slug: Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityByFuelTypeWeekly
- name: Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityDaily
  property_count: 6
  slug: Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityDaily
- name: Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityWeekly
  property_count: 6
  slug: Insights.Api.Models.Responses.Generation.DatasetRows.AvailabilityWeekly
- name: Insights.Api.Models.Responses.Generation.DatasetRows.NonBmStorData
  property_count: 6
  slug: Insights.Api.Models.Responses.Generation.DatasetRows.NonBmStorData
- name: Insights.Api.Models.Responses.Generation.DatasetRows.WindGenerationForecast
  property_count: 4
  slug: Insights.Api.Models.Responses.Generation.DatasetRows.WindGenerationForecast
- name: Insights.Api.Models.Responses.Generation.GenerationByFuelType
  property_count: 8
  slug: Insights.Api.Models.Responses.Generation.GenerationByFuelType
- name: Insights.Api.Models.Responses.Generation.HalfHourlyInterconnectorOutturn
  property_count: 8
  slug: Insights.Api.Models.Responses.Generation.HalfHourlyInterconnectorOutturn
- name: Insights.Api.Models.Responses.Generation.OutturnGenerationBySettlementPeriod
  property_count: 3
  slug: Insights.Api.Models.Responses.Generation.OutturnGenerationBySettlementPeriod
- name: Insights.Api.Models.Responses.Generation.OutturnGenerationValue
  property_count: 2
  slug: Insights.Api.Models.Responses.Generation.OutturnGenerationValue
- name: Insights.Api.Models.Responses.Generation.WindGenerationForecast
  property_count: 5
  slug: Insights.Api.Models.Responses.Generation.WindGenerationForecast
- name: Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedDemand
  property_count: 7
  slug: Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedDemand
- name: Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedGeneration
  property_count: 7
  slug: Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedGeneration
- name: Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedImbalance
  property_count: 7
  slug: Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedImbalance
- name: Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedMargin
  property_count: 7
  slug: Insights.Api.Models.Responses.IndicatedForecast.DatasetRows.IndicatedMargin
- name: Insights.Api.Models.Responses.IndicatedForecast.IndicatedForecast
  property_count: 9
  slug: Insights.Api.Models.Responses.IndicatedForecast.IndicatedForecast
- name: Insights.Api.Models.Responses.Misc.DatasetRows.DemandControlInstructionDatasetRow
  property_count: 14
  slug: Insights.Api.Models.Responses.Misc.DatasetRows.DemandControlInstructionDatasetRow
- name: Insights.Api.Models.Responses.Misc.DatasetRows.LossOfLoadProbabilityDeratedMarginData
  property_count: 8
  slug: Insights.Api.Models.Responses.Misc.DatasetRows.LossOfLoadProbabilityDeratedMarginData
- name: Insights.Api.Models.Responses.Misc.DatasetRows.SoSoPricesDatasetRow
  property_count: 13
  slug: Insights.Api.Models.Responses.Misc.DatasetRows.SoSoPricesDatasetRow
- name: Insights.Api.Models.Responses.Misc.DatasetRows.SystemFrequency
  property_count: 3
  slug: Insights.Api.Models.Responses.Misc.DatasetRows.SystemFrequency
- name: Insights.Api.Models.Responses.Misc.DatasetRows.SystemWarningsData
  property_count: 4
  slug: Insights.Api.Models.Responses.Misc.DatasetRows.SystemWarningsData
- name: Insights.Api.Models.Responses.Misc.DatasetRows.TemperatureData
  property_count: 4
  slug: Insights.Api.Models.Responses.Misc.DatasetRows.TemperatureData
- name: Insights.Api.Models.Responses.Misc.DatasetRows.TudmDatasetRow
  property_count: 13
  slug: Insights.Api.Models.Responses.Misc.DatasetRows.TudmDatasetRow
- name: Insights.Api.Models.Responses.Misc.DemandControlInstructionData
  property_count: 13
  slug: Insights.Api.Models.Responses.Misc.DemandControlInstructionData
- name: Insights.Api.Models.Responses.Misc.LossOfLoadProbabilityDeratedMarginResponse
  property_count: 8
  slug: Insights.Api.Models.Responses.Misc.LossOfLoadProbabilityDeratedMarginResponse
- name: Insights.Api.Models.Responses.Misc.SoSoPrices
  property_count: 7
  slug: Insights.Api.Models.Responses.Misc.SoSoPrices
- name: Insights.Api.Models.Responses.Misc.SystemFrequency
  property_count: 2
  slug: Insights.Api.Models.Responses.Misc.SystemFrequency
- name: Insights.Api.Models.Responses.Misc.SystemWarningsData
  property_count: 3
  slug: Insights.Api.Models.Responses.Misc.SystemWarningsData
- name: Insights.Api.Models.Responses.Misc.TemperatureData
  property_count: 6
  slug: Insights.Api.Models.Responses.Misc.TemperatureData
- name: Insights.Api.Models.Responses.Reference.BmUnitData
  property_count: 22
  slug: Insights.Api.Models.Responses.Reference.BmUnitData
- name: Insights.Api.Models.Responses.Reference.DatasetMetadataLatestRow
  property_count: 2
  slug: Insights.Api.Models.Responses.Reference.DatasetMetadataLatestRow
- name: Insights.Api.Models.Responses.Reference.InterconnectorData
  property_count: 3
  slug: Insights.Api.Models.Responses.Reference.InterconnectorData
- name: Insights.Api.Models.Responses.RemitResponseWithMetadata-1_Insights.Api.Models.Responses.DataStatus.DataStatusResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.RemitResponseWithMetadata-1_Insights.Api.Models.Responses.DataStatus.DataStatusResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Data.Entities.LoadShapePeriodData
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Data.Entities.LoadShapePeriodData
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Data.Entities.LoadShapeTotalsData
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Data.Entities.LoadShapeTotalsData
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.BalancingServicesVolume
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.BalancingServicesVolume
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.BidOfferAcceptancesResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.BidOfferAcceptancesResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.BidOfferResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.BidOfferResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.DisaggregatedBalancingServicesAdjustmentDetailsResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.DisaggregatedBalancingServicesAdjustmentDetailsResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.DisaggregatedBalancingServicesAdjustmentSummaryResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.DisaggregatedBalancingServicesAdjustmentSummaryResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Dynamic.DynamicData
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Dynamic.DynamicData
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Dynamic.DynamicParametersData
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Dynamic.DynamicParametersData
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Dynamic.RateData
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Dynamic.RateData
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.MarketIndexResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.MarketIndexResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.NetBalancingServicesAdjustmentResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.NetBalancingServicesAdjustmentResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.NonBmStorResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.NonBmStorResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Physical.PhysicalData
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Physical.PhysicalData
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.AcceptanceVolumeResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.AcceptanceVolumeResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.HistoricAcceptanceResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.HistoricAcceptanceResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.IndicativeCashflowResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.IndicativeCashflowResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.IndicativeVolumeResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.IndicativeVolumeResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.MarketDepthResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.MarketDepthResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.SettlementMessageResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.SettlementMessageResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.SettlementStackResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.SettlementStackResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.SystemPriceResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Balancing.Settlement.SystemPriceResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DataStatus.DataStatusResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DataStatus.DataStatusResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandForecast.DemandForecastDaily
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandForecast.DemandForecastDaily
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandForecast.DemandForecastDayAhead
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandForecast.DemandForecastDayAhead
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandForecast.DemandForecastPeak
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandForecast.DemandForecastPeak
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandForecast.DemandForecastWeekly
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandForecast.DemandForecastWeekly
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandOutturn.DemandOutturn
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandOutturn.DemandOutturn
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandOutturn.DemandOutturnPeak
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandOutturn.DemandOutturnPeak
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandOutturn.IndicativeDemandPeak
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandOutturn.IndicativeDemandPeak
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandOutturn.IndodRow
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandOutturn.IndodRow
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandOutturn.RollingSystemDemand
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.DemandOutturn.RollingSystemDemand
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.ForecastMargin.ForecastMarginDaily
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.ForecastMargin.ForecastMarginDaily
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.ForecastMargin.ForecastMarginWeekly
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.ForecastMargin.ForecastMarginWeekly
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.ForecastSurplus.ForecastSurplusDaily
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.ForecastSurplus.ForecastSurplusDaily
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.ForecastSurplus.ForecastSurplusWeekly
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.ForecastSurplus.ForecastSurplusWeekly
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Generation.AvailabilityDaily
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Generation.AvailabilityDaily
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Generation.AvailabilityWeekly
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Generation.AvailabilityWeekly
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Generation.HalfHourlyInterconnectorOutturn
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Generation.HalfHourlyInterconnectorOutturn
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Generation.WindGenerationForecast
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Generation.WindGenerationForecast
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.IndicatedForecast.IndicatedForecast
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.IndicatedForecast.IndicatedForecast
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Misc.DemandControlInstructionData
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Misc.DemandControlInstructionData
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Misc.LossOfLoadProbabilityDeratedMarginResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Misc.LossOfLoadProbabilityDeratedMarginResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Misc.SoSoPrices
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Misc.SoSoPrices
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Misc.SystemFrequency
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Misc.SystemFrequency
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Misc.SystemWarningsData
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Misc.SystemWarningsData
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Misc.TemperatureData
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Misc.TemperatureData
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.RestorationZone.RestorationZoneDemandRestoredDatasetRow
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.RestorationZone.RestorationZoneDemandRestoredDatasetRow
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.TotalExemptSupplyVolume.TotalExemptSupplyVolumeResponse
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.TotalExemptSupplyVolume.TotalExemptSupplyVolumeResponse
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.ActualGenerationBySettlementPeriod
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.ActualGenerationBySettlementPeriod
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.ActualGenerationWindSolar
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.ActualGenerationWindSolar
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.ActualTotalLoadPerBiddingZone
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.ActualTotalLoadPerBiddingZone
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.DayAheadAggregatedGeneration
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.DayAheadAggregatedGeneration
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.DayAheadGenerationForWindAndSolar
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.DayAheadGenerationForWindAndSolar
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.DayAheadTotalLoadPerBiddingZone
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.DayAheadTotalLoadPerBiddingZone
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.Remit.RemitMessageIdentifierWithUrl
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.Remit.RemitMessageIdentifierWithUrl
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.Remit.RemitMessageWithId
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.Remit.RemitMessageWithId
- name: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.WeekAheadTotalLoadPerBiddingZone
  property_count: 2
  slug: Insights.Api.Models.Responses.ResponseWithMetadata-1_Insights.Api.Models.Responses.Transparency.WeekAheadTotalLoadPerBiddingZone
- name: Insights.Api.Models.Responses.RestorationZone.RestorationZoneDemandForecastDatasetRow
  property_count: 8
  slug: Insights.Api.Models.Responses.RestorationZone.RestorationZoneDemandForecastDatasetRow
- name: Insights.Api.Models.Responses.RestorationZone.RestorationZoneDemandRestoredDatasetRow
  property_count: 6
  slug: Insights.Api.Models.Responses.RestorationZone.RestorationZoneDemandRestoredDatasetRow
- name: Insights.Api.Models.Responses.TotalExemptSupplyVolume.TotalExemptSupplyVolumeResponse
  property_count: 5
  slug: Insights.Api.Models.Responses.TotalExemptSupplyVolume.TotalExemptSupplyVolumeResponse
- name: Insights.Api.Models.Responses.Transparency.ActualGenerationBySettlementPeriod
  property_count: 3
  slug: Insights.Api.Models.Responses.Transparency.ActualGenerationBySettlementPeriod
- name: Insights.Api.Models.Responses.Transparency.ActualGenerationValue
  property_count: 3
  slug: Insights.Api.Models.Responses.Transparency.ActualGenerationValue
- name: Insights.Api.Models.Responses.Transparency.ActualGenerationWindSolar
  property_count: 7
  slug: Insights.Api.Models.Responses.Transparency.ActualGenerationWindSolar
- name: Insights.Api.Models.Responses.Transparency.ActualTotalLoadPerBiddingZone
  property_count: 5
  slug: Insights.Api.Models.Responses.Transparency.ActualTotalLoadPerBiddingZone
- name: Insights.Api.Models.Responses.Transparency.AgptSummaryData
  property_count: 5
  slug: Insights.Api.Models.Responses.Transparency.AgptSummaryData
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.AbucDatasetRow
  property_count: 10
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.AbucDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.ActualAggregatedGenerationPerTypeDatasetRow
  property_count: 10
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.ActualAggregatedGenerationPerTypeDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.ActualGenerationOutputPerGenerationUnitDatasetResponse
  property_count: 8
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.ActualGenerationOutputPerGenerationUnitDatasetResponse
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.ActualGenerationWindSolarDatasetRow
  property_count: 10
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.ActualGenerationWindSolarDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.ActualTotalLoadPerBiddingZoneDatasetRow
  property_count: 8
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.ActualTotalLoadPerBiddingZoneDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.AobeDatasetRow
  property_count: 11
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.AobeDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.BebDatasetRow
  property_count: 11
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.BebDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.CbsDatasetRow
  property_count: 10
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.CbsDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.CostsOfCongestionManagementDatasetRow
  property_count: 8
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.CostsOfCongestionManagementDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.DayAheadAggregatedGenerationDatasetRow
  property_count: 8
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.DayAheadAggregatedGenerationDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.DayAheadGenerationForWindAndSolarDatasetRow
  property_count: 11
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.DayAheadGenerationForWindAndSolarDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.DayAheadTotalLoadPerBiddingZoneDatasetRow
  property_count: 8
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.DayAheadTotalLoadPerBiddingZoneDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.FeibDatasetRow
  property_count: 9
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.FeibDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.IgcaDatasetRow
  property_count: 8
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.IgcaDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.IgcpuDatasetRow
  property_count: 10
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.IgcpuDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.MonthAheadTotalLoadPerBiddingZoneDatasetRow
  property_count: 9
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.MonthAheadTotalLoadPerBiddingZoneDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.PbcDatasetRow
  property_count: 12
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.PbcDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.PpbrDatasetRow
  property_count: 9
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.PpbrDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.WeekAheadTotalLoadPerBiddingZoneDatasetRow
  property_count: 8
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.WeekAheadTotalLoadPerBiddingZoneDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.YearAheadForecastMarginDatasetRow
  property_count: 7
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.YearAheadForecastMarginDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DatasetRows.YearAheadTotalLoadPerBiddingZoneDatasetRow
  property_count: 8
  slug: Insights.Api.Models.Responses.Transparency.DatasetRows.YearAheadTotalLoadPerBiddingZoneDatasetRow
- name: Insights.Api.Models.Responses.Transparency.DayAheadAggregatedGeneration
  property_count: 5
  slug: Insights.Api.Models.Responses.Transparency.DayAheadAggregatedGeneration
- name: Insights.Api.Models.Responses.Transparency.DayAheadGenerationForWindAndSolar
  property_count: 8
  slug: Insights.Api.Models.Responses.Transparency.DayAheadGenerationForWindAndSolar
- name: Insights.Api.Models.Responses.Transparency.DayAheadTotalLoadPerBiddingZone
  property_count: 5
  slug: Insights.Api.Models.Responses.Transparency.DayAheadTotalLoadPerBiddingZone
- name: Insights.Api.Models.Responses.Transparency.Remit.DatasetRows.OutageProfileData
  property_count: 3
  slug: Insights.Api.Models.Responses.Transparency.Remit.DatasetRows.OutageProfileData
- name: Insights.Api.Models.Responses.Transparency.Remit.DatasetRows.RemitMessage
  property_count: 28
  slug: Insights.Api.Models.Responses.Transparency.Remit.DatasetRows.RemitMessage
- name: Insights.Api.Models.Responses.Transparency.Remit.RemitMessageIdentifierWithUrl
  property_count: 6
  slug: Insights.Api.Models.Responses.Transparency.Remit.RemitMessageIdentifierWithUrl
- name: Insights.Api.Models.Responses.Transparency.Remit.RemitMessageWithId
  property_count: 29
  slug: Insights.Api.Models.Responses.Transparency.Remit.RemitMessageWithId
- name: Insights.Api.Models.Responses.Transparency.WeekAheadTotalLoadPerBiddingZone
  property_count: 5
  slug: Insights.Api.Models.Responses.Transparency.WeekAheadTotalLoadPerBiddingZone
- name: Insights.Api.Models.Service.DayAheadDemandForecastRow
  property_count: 7
  slug: Insights.Api.Models.Service.DayAheadDemandForecastRow
- name: Insights.Api.Models.Service.WindGenerationForecastRow
  property_count: 5
  slug: Insights.Api.Models.Service.WindGenerationForecastRow
jsonld:
- class_count: 6
  name: Api Context
  property_count: 2
  slug: api
- class_count: 6
  name: context Context
  property_count: 2
  slug: context
layout: provider
modified: '2026-06-13'
name: Elexon
nav: Providers
network: true
overview: 'Elexon publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Balancing Mechanism Dynamic API, Balancing Mechanism Physical API, Balancing Services Adjustment - Disaggregated API, and 29 more. Tagged areas include Electricity, Energy, UK Energy Market, Balancing Mechanism, and Settlement.


  The Elexon catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Elexon''s developer surface includes developer portal, documentation, GitHub presence, engineering blog, support, and 11 more developer resources.'
plans:
- name: Elexon Plans Pricing
  plan_count: 1
  slug: elexon-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 3
  name: Elexon Rate Limits
  slug: elexon-rate-limits
rules:
- name: Elexon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: elexon-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.4
    developer_ergonomics: 23.9
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 51.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elexon/refs/heads/main/screenshots/elexon-2026-06-20T180600.png
security:
- kind: domain-security
  name: Elexon Domain Security
  slug: elexon-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: elexon
tags:
- Electricity
- Energy
- UK Energy Market
- Balancing Mechanism
- Settlement
- Meter Readings
- Market Transparency
- BMRS
- Electricity Grid
- Power Generation
- United Kingdom
website: https://developer.data.elexon.co.uk/
---
