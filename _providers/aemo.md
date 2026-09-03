---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 560
  human_in_the_loop: 21
  name: Aemo Agentic Access
  operation_count: 798
  slug: aemo-agentic-access
  summary_line: 798 operations · 560 acting · 21 human-in-the-loop
api_count: 76
apis:
- description: 'The JSON API behind AEMO''s public National Electricity Market data dashboard, and the closest thing AEMO operates to an open real-time market API. Confirmed live and fully anonymous on 2026-07-27: GET'
  name: AEMO NEM Data Dashboard API
  slug: aemo-nem-data-dashboard-api
- description: NEMWeb is AEMO's open bulk-data channel for the National Electricity Market and the single largest genuinely open energy dataset in Australia. It is not a REST API — it is an anonymously browsable HTT
  name: AEMO NEMWeb Public Data Feed
  slug: aemo-nemweb-public-data-feed
- description: 'The Western Australian equivalent of NEMWeb, covering the Wholesale Electricity Market that AEMO operates separately from the NEM. Confirmed anonymous and live on 2026-07-27: GET https://data.wa.aemo.'
  name: AEMO WA Market Data Public Feed
  slug: aemo-wa-market-data-public-feed
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO B2 B Messaging Async API
  slug: aemo-b2bmessagingasync-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: The B2BMessagingPull API is a B2B SMP API used to send and receive B2B messages between the participants in a Pull messaging pattern. The messages will be queued in the e-Hub and the receiving partici
  name: AEMO B2 B Messaging Pull API
  slug: aemo-b2bmessagingpull-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO B2 B Messaging Sync API
  slug: aemo-b2bmessagingsync-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO B2 M Messaging Async API
  slug: aemo-b2mmessagingasync-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO B2 M Messaging Pull API
  slug: aemo-b2mmessagingpull-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO B2 M Messaging Sync API
  slug: aemo-b2mmessagingsync-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Balancing Reports v2.1
  name: AEMO Balancing Reports v2.1 API
  slug: aemo-balancing-reports-v2-1-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Balancing Reports v2.2
  name: AEMO Balancing Reports v2.2 API
  slug: aemo-balancing-reports-v2-2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Balancing Reports v2.3
  name: AEMO Balancing Reports v2.3 API
  slug: aemo-balancing-reports-v2-3-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Balancing Reports v2.4
  name: AEMO Balancing Reports v2.4 API
  slug: aemo-balancing-reports-v2-4-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Balancing Reports v2.5
  name: AEMO Balancing Reports v2.5 API
  slug: aemo-balancing-reports-v2-5-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Balancing Reports v2
  name: AEMO Balancing Reports v2 API
  slug: aemo-balancing-reports-v2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Balancing Submission v2
  name: AEMO Balancing Submission v2 API
  slug: aemo-balancing-submission-v2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Bilateral/Stem Submission v1
  name: AEMO Bilateral/Stem Submission v1 API
  slug: aemo-bilateral-stem-submission-v1-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO Blind Update API
  slug: aemo-blindupdate-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Capacity
  name: AEMO Capacity API
  slug: aemo-capacity-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: CapacityAuction
  name: AEMO Capacity Auction API
  slug: aemo-capacityauction-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO CDR API
  slug: aemo-cdr-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: CDR Common
  name: AEMO CDR Common API
  slug: aemo-cdr-common-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Data Holder Customer endpoints
  name: AEMO Data Holder Customers API
  slug: aemo-data-holder-customers-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Data Holder Operations endpoints
  name: AEMO Data Holder Operations API
  slug: aemo-data-holder-operations-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO DER Registration For Account Holders API
  slug: aemo-der-registration-for-account-holders-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO DER Registration for NSPs API
  slug: aemo-der-registration-for-nsps-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Distributed Energy Resource endpoints
  name: AEMO Distributed Energy Resources API
  slug: aemo-distributed-energy-resources-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO EE Simulation Status Update API
  slug: aemo-ee-simulation-status-update-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Electricity Service Point endpoints
  name: AEMO Electricity Service Points API
  slug: aemo-electricity-service-points-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Electricity Usage endpoints
  name: AEMO Electricity Usage API
  slug: aemo-electricity-usage-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: EnablementInstruction
  name: AEMO Enablement Instruction API
  slug: aemo-enablementinstruction-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Energy Account Balance endpoints
  name: AEMO Energy Account Balances API
  slug: aemo-energy-account-balances-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Energy Account Billing endpoints
  name: AEMO Energy Account Billing API
  slug: aemo-energy-account-billing-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Energy Account endpoints
  name: AEMO Energy Accounts API
  slug: aemo-energy-accounts-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Energy Plan endpoints
  name: AEMO Energy Plans API
  slug: aemo-energy-plans-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: This API is intended for AEMO's use only, used by AEMO web pages and is not supported for any other use. It can change at any time. See https://dev.aemo.com.au/ for information on using AEMO APIs.
  name: AEMO GasBB Reporting Public Data API
  slug: aemo-gasbb-reporting-public-data-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: The Generator Recall API is used by generators to send information about recall times into the Generator Recall web-based interface in the EMMS Markets Portal. The system will then transfer the inform
  name: AEMO Generator Recall API
  slug: aemo-generatorrecall-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO Hub Message Management API
  slug: aemo-hubmessagemanagement-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO Hub Message Management V2 API
  slug: aemo-hubmessagemanagementv2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO Identity Service(v2) API
  slug: aemo-identityservice-v2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO Intermittent Generation Availability Submissions API
  slug: aemo-intermittent-generation-availability-submissions-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: LFAS Reports v2
  name: AEMO LFAS Reports v2 API
  slug: aemo-lfas-reports-v2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: LFAS Submission v2
  name: AEMO LFAS Submission v2 API
  slug: aemo-lfas-submission-v2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Market Reports v2
  name: AEMO Market Reports v2 API
  slug: aemo-market-reports-v2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: The Meter Exemptions API enables registered Metering Coordinators (MCs) to create and manage metering exemptions within MSATS.
  name: AEMO Meter Exemption API
  slug: aemo-meterexemption-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO MT PASA Offers API
  slug: aemo-mt-pasa-offers-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Bidding Service Open API specification
  name: AEMO NEM Dispatch Bidding API
  slug: aemo-nemdispatchbidding-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: oauth-v1
  name: AEMO OAUTH V1 API
  slug: aemo-oauth-v1-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: OIP
  name: AEMO OIP API
  slug: aemo-oip-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Outage Management
  name: AEMO Outage Management API
  slug: aemo-outage-management-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO P2 P Messaging Sync API
  slug: aemo-p2pmessagingsync-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Pre-Balancing Reports v6
  name: AEMO Pre-Balancing Reports v6 API
  slug: aemo-pre-balancing-reports-v6-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Pre-Balancing Reports v7.1
  name: AEMO Pre-Balancing Reports v7.1 API
  slug: aemo-pre-balancing-reports-v7-1-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Pre-Balancing Reports v7
  name: AEMO Pre-Balancing Reports v7 API
  slug: aemo-pre-balancing-reports-v7-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Pre-Balancing Reports v8
  name: AEMO Pre-Balancing Reports v8 API
  slug: aemo-pre-balancing-reports-v8-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: This API supports the various operations performed on Prudentials dashboard
  name: AEMO Prudentials API
  slug: aemo-prudentials-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: RCM Operations
  name: AEMO RCM Operations API
  slug: aemo-rcm-operations-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO Reallocations API
  slug: aemo-reallocations-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Report
  name: AEMO Report API
  slug: aemo-report-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: The WEM-Reform API for Real-Time Market submissions available to all Market Participants.
  name: AEMO RTMS API
  slug: aemo-rtms-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO Self Forecast API
  slug: aemo-selfforecast-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: This API supports the various operations performed in Settlement Direct API
  name: AEMO Settlement Direct API
  slug: aemo-settlement-direct-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Submission
  name: AEMO Submission API
  slug: aemo-submission-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: System Management Reports v2.1
  name: AEMO System Management Reports v2.1 API
  slug: aemo-system-management-reports-v2-1-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: System Management Reports v2.2
  name: AEMO System Management Reports v2.2 API
  slug: aemo-system-management-reports-v2-2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: System Management Reports v2.3
  name: AEMO System Management Reports v2.3 API
  slug: aemo-system-management-reports-v2-3-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: System Management Reports v2.4
  name: AEMO System Management Reports v2.4 API
  slug: aemo-system-management-reports-v2-4-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: System Management Reports v2.5
  name: AEMO System Management Reports v2.5 API
  slug: aemo-system-management-reports-v2-5-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: System Management Reports v2.6
  name: AEMO System Management Reports v2.6 API
  slug: aemo-system-management-reports-v2-6-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: System Management Reports v2
  name: AEMO System Management Reports v2 API
  slug: aemo-system-management-reports-v2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: 'The TLS Certificate Management API allows authorised participants to self-manage their AEMO-signed TLS certificates. This API provides the following features:'
  name: AEMO TLS Certificate Mgmt v1 API
  slug: aemo-tls-certificate-mgmt-v1-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: VariableParameter
  name: AEMO Variable Parameter API
  slug: aemo-variableparameter-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: WEM Attributes Report
  name: AEMO WEM Attributes Report API
  slug: aemo-wem-attributes-report-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO WEM DER Installation V2 API
  slug: aemo-wem-der-installation-v2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: Introduction
  name: AEMO WEM DER NMI API
  slug: aemo-wem-der-nmi-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: WEMDE DispatchCase
  name: AEMO WEMDE DispatchCase API
  slug: aemo-wemde-dispatchcase-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: WEMDE DispatchCase V2
  name: AEMO WEMDE DispatchCase V2 API
  slug: aemo-wemde-dispatchcase-v2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: WEMDE DispatchInstruction
  name: AEMO WEMDE DispatchInstruction API
  slug: aemo-wemde-dispatchinstruction-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: WEMDE DispatchSolution
  name: AEMO WEMDE DispatchSolution API
  slug: aemo-wemde-dispatchsolution-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: WEMDE DispatchSolution V2
  name: AEMO WEMDE DispatchSolution V2 API
  slug: aemo-wemde-dispatchsolution-v2-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: WEMDE DispatchSummary
  name: AEMO WEMDE DispatchSummary API
  slug: aemo-wemde-dispatchsummary-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: WEMDE DSPDispatchInstruction
  name: AEMO WEMDE DSPDispatchInstruction API
  slug: aemo-wemde-dspdispatchinstruction-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: WEMDE NCESS
  name: AEMO WEMDE NCESS API
  slug: aemo-wemde-ncess-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: WEMDE NotInServiceCapacity
  name: AEMO WEMDE NotInServiceCapacity API
  slug: aemo-wemde-notinservicecapacity-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: WEMDE ReferenceTradingPrice
  name: AEMO WEMDE ReferenceTradingPrice API
  slug: aemo-wemde-referencetradingprice-api
- baseURL: https://visualisations.aemo.com.au/aemo/apps/api/report
  baseurl_source: declared
  description: WEMDE TradingDayReport
  name: AEMO WEMDE TradingDayReport API
  slug: aemo-wemde-tradingdayreport-api
artifact_total: 169
asyncapis:
- description: ''
  name: Aemo Ehub Events
  slug: aemo-ehub-events
collections:
- collection_type: open
  name: WEM Attributes Report
  slug: open-aemo-attributes-report-external-v1
- collection_type: open
  name: B2BMessagingAsync
  slug: open-aemo-b2bmessaging-async-v1
- collection_type: open
  name: B2BMessagingPull
  slug: open-aemo-b2bmessaging-pull-v1
- collection_type: open
  name: B2BMessagingSync
  slug: open-aemo-b2bmessaging-sync-v1
- collection_type: open
  name: B2MMessagingAsync
  slug: open-aemo-b2mmessaging-async-v1
- collection_type: open
  name: B2MMessagingPull
  slug: open-aemo-b2mmessaging-pull-v1
- collection_type: open
  name: B2MMessagingSync
  slug: open-aemo-b2mmessaging-sync-v1
- collection_type: open
  name: Balancing Reports v2.1
  slug: open-aemo-balancing-reports-v2-1
- collection_type: open
  name: Balancing Reports v2.2
  slug: open-aemo-balancing-reports-v2-2
- collection_type: open
  name: Balancing Reports v2.3
  slug: open-aemo-balancing-reports-v2-3
- collection_type: open
  name: Balancing Reports v2.4
  slug: open-aemo-balancing-reports-v2-4
- collection_type: open
  name: Balancing Reports v2.5
  slug: open-aemo-balancing-reports-v2-5
- collection_type: open
  name: Balancing Reports v2
  slug: open-aemo-balancing-reports-v2
- collection_type: open
  name: Balancing Submission v2
  slug: open-aemo-balancing-submission-v2
- collection_type: open
  name: NEMDispatchBidding
  slug: open-aemo-bidding-v1
- collection_type: open
  name: Bilateral/Stem Submission v1
  slug: open-aemo-bilateral-stem-submission-v1
- collection_type: open
  name: BlindUpdate
  slug: open-aemo-blindupdate-v1
- collection_type: open
  name: Capacity
  slug: open-aemo-capacity-v1
- collection_type: open
  name: CapacityAuction
  slug: open-aemo-capacityAuction-v1
- collection_type: open
  name: CDR Common
  slug: open-aemo-cdr-common
- collection_type: open
  name: CDR
  slug: open-aemo-cdr
- collection_type: open
  name: CDR Common API
  slug: open-aemo-cds-common-api
- collection_type: open
  name: CDR Energy API
  slug: open-aemo-cds-energy-api
- collection_type: open
  name: DER Registration for NSPs
  slug: open-aemo-der-business-registration-v1
- collection_type: open
  name: DER Registration For Account Holders
  slug: open-aemo-der-consumer-registration-v1
- collection_type: open
  name: WEM DER Installation V2
  slug: open-aemo-der-register-installation-v2
- collection_type: open
  name: WEM DER NMI
  slug: open-aemo-der-register-nmi-v1
- collection_type: open
  name: EE Simulation Status Update
  slug: open-aemo-ee-simulation-status-update-v1
- collection_type: open
  name: EnablementInstruction
  slug: open-aemo-enablementinstruction-v1
- collection_type: open
  name: GasBB Reporting Public Data
  slug: open-aemo-gasbb-reporting-public-data
- collection_type: open
  name: GeneratorRecall
  slug: open-aemo-generatorRecall-v1
- collection_type: open
  name: HubMessageManagement
  slug: open-aemo-hubmsgmgt-v1
- collection_type: open
  name: HubMessageManagementV2
  slug: open-aemo-hubmsgmgt-v2
- collection_type: open
  name: IdentityService(v2)
  slug: open-aemo-identityService-v2
- collection_type: open
  name: LFAS Reports v2
  slug: open-aemo-lfas-reports-v2
- collection_type: open
  name: LFAS Submission v2
  slug: open-aemo-lfas-submission-v2
- collection_type: open
  name: Market Reports v2
  slug: open-aemo-market-reports-v2
- collection_type: open
  name: MeterExemption
  slug: open-aemo-meterexemption-external-v1
- collection_type: open
  name: MT PASA Offers
  slug: open-aemo-mtpasaoffers-v1
- collection_type: open
  name: oauth-v1
  slug: open-aemo-oauth-v1
- collection_type: open
  name: OIP
  slug: open-aemo-oip-external-v1
- collection_type: open
  name: Intermittent Generation Availability Submissions
  slug: open-aemo-opsforecasting-intermittentgen-v1
- collection_type: open
  name: Outage Management
  slug: open-aemo-outage-management-external-v1
- collection_type: open
  name: P2PMessagingSync
  slug: open-aemo-p2pmessaging-sync-v1
- collection_type: open
  name: Pre-Balancing Reports v6
  slug: open-aemo-pre-balancing-reports-v6
- collection_type: open
  name: Pre-Balancing Reports v7.1
  slug: open-aemo-pre-balancing-reports-v7-1
- collection_type: open
  name: Pre-Balancing Reports v7
  slug: open-aemo-pre-balancing-reports-v7
- collection_type: open
  name: Pre-Balancing Reports v8
  slug: open-aemo-pre-balancing-reports-v8
- collection_type: open
  name: Prudentials
  slug: open-aemo-prudentials-v1
- collection_type: open
  name: RCM Operations
  slug: open-aemo-rcm-ops-external-v1
- collection_type: open
  name: Reallocations
  slug: open-aemo-reallocations-v1
- collection_type: open
  name: Report
  slug: open-aemo-report-v1
- collection_type: open
  name: RTMS
  slug: open-aemo-rtms-external-v1
- collection_type: open
  name: SelfForecast
  slug: open-aemo-selfForecast-v1
- collection_type: open
  name: Settlement Direct
  slug: open-aemo-settlementDirect-v1
- collection_type: open
  name: Submission
  slug: open-aemo-submission-v1
- collection_type: open
  name: System Management Reports v2.1
  slug: open-aemo-system-management-reports-v2-1
- collection_type: open
  name: System Management Reports v2.2
  slug: open-aemo-system-management-reports-v2-2
- collection_type: open
  name: System Management Reports v2.3
  slug: open-aemo-system-management-reports-v2-3
- collection_type: open
  name: System Management Reports v2.4
  slug: open-aemo-system-management-reports-v2-4
- collection_type: open
  name: System Management Reports v2.5
  slug: open-aemo-system-management-reports-v2-5
- collection_type: open
  name: System Management Reports v2.6
  slug: open-aemo-system-management-reports-v2-6
- collection_type: open
  name: System Management Reports v2
  slug: open-aemo-system-management-reports-v2
- collection_type: open
  name: TLS Certificate Mgmt v1
  slug: open-aemo-tls-certificate-mgmt-v1
- collection_type: open
  name: VariableParameter
  slug: open-aemo-variableparameter-v1
- collection_type: open
  name: WEMDE DispatchCase
  slug: open-aemo-wemde-dispatchcase-external-v1
- collection_type: open
  name: WEMDE DispatchCase V2
  slug: open-aemo-wemde-dispatchcase-external-v2
- collection_type: open
  name: WEMDE DispatchInstruction
  slug: open-aemo-wemde-dispatchinstruction-external-v1
- collection_type: open
  name: WEMDE DispatchSolution
  slug: open-aemo-wemde-dispatchsolution-external-v1
- collection_type: open
  name: WEMDE DispatchSolution V2
  slug: open-aemo-wemde-dispatchsolution-external-v2
- collection_type: open
  name: WEMDE DispatchSummary
  slug: open-aemo-wemde-dispatchsummary-external-v1
- collection_type: open
  name: WEMDE DSPDispatchInstruction
  slug: open-aemo-wemde-dspdispatchinstruction-external-v1
- collection_type: open
  name: WEMDE NCESS
  slug: open-aemo-wemde-ncess-external-v1
- collection_type: open
  name: WEMDE NotInServiceCapacity
  slug: open-aemo-wemde-notinservicecapacity-external-v1
- collection_type: open
  name: WEMDE ReferenceTradingPrice
  slug: open-aemo-wemde-referencetradingprice-external-v1
- collection_type: open
  name: WEMDE TradingDayReport
  slug: open-aemo-wemde-tradingdayreport-external-v1
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/aemo-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aemo-cds-energy-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aemo-cds-common-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aemo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aemo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aemo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aemo.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.aemo.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.aemo.com.au/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.aemo.com.au/developer/apis?api-version=2022-04-01-preview
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.aemo.com.au/working-with-aemo-apis
- group: start
  title: ''
  type: SignUp
  url: https://dev.aemo.com.au/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dev.aemo.com.au/terms
- group: auth
  title: ''
  type: Authentication
  url: https://dev.aemo.com.au/urm-username-password
- group: auth
  title: ''
  type: OAuth
  url: https://dev.aemo.com.au/oauth
- group: build
  title: ''
  type: PostmanCollection
  url: https://documenter.getpostman.com/view/10032049/2s93CNNDaK
- group: other
  title: ''
  type: ConsumerDataRight
  url: https://aemo.com.au/initiatives/major-programs/cdr-at-aemo
- group: other
  title: ''
  type: APIStandards
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: other
  title: ''
  type: Regulator
  url: https://www.cdr.gov.au/
- group: other
  title: ''
  type: DataFeed
  url: https://nemweb.com.au/Reports/Current/
- group: other
  title: ''
  type: DataFeed
  url: https://data.wa.aemo.com.au/public/
- group: other
  title: ''
  type: Dashboard
  url: https://visualisations.aemo.com.au/aemo/apps/visualisations/index.html
- group: other
  title: ''
  type: GasBulletinBoard
  url: https://gbbwa.aemo.com.au/
- group: start
  title: ''
  type: MarketsPortalHelp
  url: https://markets-portal-help.docs.public.aemo.com.au/Content/API_Reference/API_introduction.htm
- group: other
  title: ''
  type: Registration
  url: https://www.aemo.com.au/energy-systems/registration
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/aemo
- group: operate
  title: ''
  type: Support
  url: https://dev.aemo.com.au/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://dev.aemo.com.au/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.aemo.com.au/newsroom/news-updates
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aemo.com.au/en/privacy-and-legal-notices/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.aemo.com.au/energy-systems/market-it-systems/it-change-and-release-management
- group: operate
  title: ''
  type: Deprecation
  url: https://www.aemo.com.au/energy-systems/market-it-systems/it-change-and-release-management
- group: auth
  title: ''
  type: Security
  url: https://www.aemo.com.au/.well-known/security.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://aemo.com.au/market-notices?marketNoticeFacets=MARKET+SYSTEMS
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/10032049/2s93CNNDaK
- group: other
  title: ''
  type: OpenIDConnect
  url: https://login.aemo.com.au/login.aemo.com.au/v2.0/.well-known/openid-configuration?p=B2C_1A_DERR_SIGNUPSIGNIN
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aemo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aemo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aemo-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aemo-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aemo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aemo-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aemo-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aemo-glossary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aemo-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aemo-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/aemo-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aemo-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/aemo-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aemo-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aemo-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aemo-ehub-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPCandidate
  url: mcp/aemo-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aemo-tool-crosswalk.yml
created: '2026-07-27'
description: 'AEMO, the Australian Energy Market Operator, is the independent system and market operator for Australia''s electricity and gas systems — it dispatches and prices the National Electricity Market across Queensland, New South Wales, Victoria, South Australia and Tasmania every five minutes, runs the Wholesale Electricity Market and the Gas Bulletin Board in Western Australia, operates the Victorian gas declared wholesale market and the Gas Supply Hubs, maintains the MSATS metering registry and the national Distributed Energy Resources register, and publishes the Integrated System Plan. It sits at the centre of the value chain: it does not generate, network or retail energy, it clears the market and holds the settlement-grade metering data that every other participant depends on. Under the Consumer Data Right extended to energy, AEMO is the designated SECONDARY data holder and gateway — retailers are the primary data holders, and AEMO serves NMI standing data, distributed energy
  resource records and up to twenty-four months of interval meter data through mandated Consumer Data Standards endpoints. Its API posture splits cleanly in two, and the split is the whole story: the market-data half is genuinely, radically open — 103 live NEMWeb report directories plus 68 archive directories of dispatch, price, demand, bidding, constraint and settlement data downloadable by anyone with no key, no account and no licence, alongside anonymous JSON endpoints behind the public NEM dashboard; the participant and consumer half is completely closed — a public developer portal at dev.aemo.com.au catalogues 74 APIs and 771 operations that anyone may read, but every one of them requires registration as an AEMO market participant, a Participant ID, MSATS user rights and an AEMO-signed mutual-TLS client certificate, and the OpenAPI documents the portal exports publicly are empty shells that declare zero paths and point at internal hostnames.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aemo.png
layout: provider
modified: '2026-07-27'
name: AEMO
nav: Providers
network: true
overview: 'AEMO publishes 83 APIs on the [APIs.io](https://apis.io/) network, including B2 B Messaging Async API, B2 B Messaging Pull API, B2 B Messaging Sync API, and 80 more. Tagged areas include Energy, Australia, Electricity, Gas, and Energy Markets.


  The AEMO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AEMO''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 48 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 0
  name: Aemo Rate Limits
  slug: aemo-rate-limits
scopes:
- name: Aemo Scopes
  scope_count: 2
  slug: aemo-scopes
  summary_line: 2 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 25
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.9
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 19.7
    contract_quality: 55.7
    developer_ergonomics: 70.8
    discoverability: 68.5
    governance: 19.7
    operational_transparency: 52.6
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 83
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aemo/refs/heads/main/screenshots/aemo-2026-08-07T160947.png
security:
- kind: authentication
  name: Aemo Authentication
  slug: aemo-authentication
  summary_line: apiKey · 8 schemes
- kind: domain-security
  name: Aemo Domain Security
  slug: aemo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aemo Vulnerability Disclosure
  slug: aemo-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: aemo
tags:
- Energy
- Australia
- Electricity
- Gas
- Energy Markets
- Grid
- Market Operator
- System Operator
- Open Energy Data
- Consumer Data Right
- CDR
- Smart Metering
- Distributed Energy Resources
- Renewables
- Utilities
website: https://aemo.com.au/
---
