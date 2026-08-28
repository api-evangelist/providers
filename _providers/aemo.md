---
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
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
  score: 37.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 560
  human_in_the_loop: 21
  name: Aemo Agentic Access
  operation_count: 798
  slug: aemo-agentic-access
  summary_line: 798 operations · 560 acting · 21 human-in-the-loop
api_count: 77
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
- description: The Consumer Data Right (CDR) APIs allow Registered Financially Responsible Market Participants (FRMPs) to service API requests for AEMO data from Accredited Data Recipients. AEMO's public API catalog
  name: AEMO CDR
  slug: aemo-cdr
- description: AEMO's public API catalogue lists 2 operation(s) for this API, gateway-routed under the path prefix /NEMRetail/cds-au/v1/discovery. AEMO's own openapi-link export for this API is a shell — it declares
  name: AEMO CDR Common
  slug: aemo-cdr-common
- description: AEMO WEM Attributes Report from AEMO — 2 path(s) described in OpenAPI.
  name: AEMO WEM Attributes Report
  slug: aemo-attributes-report-external-v1-openapi
- description: AEMO B2BMessagingAsync from AEMO — 3 path(s) described in OpenAPI.
  name: AEMO B2BMessagingAsync
  slug: aemo-b2bmessaging-async-v1-openapi
- description: AEMO B2BMessagingPull from AEMO — 3 path(s) described in OpenAPI.
  name: AEMO B2BMessagingPull
  slug: aemo-b2bmessaging-pull-v1-openapi
- description: AEMO B2BMessagingSync from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO B2BMessagingSync
  slug: aemo-b2bmessaging-sync-v1-openapi
- description: AEMO B2MMessagingAsync from AEMO — 3 path(s) described in OpenAPI.
  name: AEMO B2MMessagingAsync
  slug: aemo-b2mmessaging-async-v1-openapi
- description: AEMO B2MMessagingPull from AEMO — 4 path(s) described in OpenAPI.
  name: AEMO B2MMessagingPull
  slug: aemo-b2mmessaging-pull-v1-openapi
- description: AEMO B2MMessagingSync from AEMO — 7 path(s) described in OpenAPI.
  name: AEMO B2MMessagingSync
  slug: aemo-b2mmessaging-sync-v1-openapi
- description: AEMO Balancing Reports v2.1 from AEMO — 5 path(s) described in OpenAPI.
  name: AEMO Balancing Reports v2.1
  slug: aemo-balancing-reports-v2-1-openapi
- description: AEMO Balancing Reports v2.2 from AEMO — 6 path(s) described in OpenAPI.
  name: AEMO Balancing Reports v2.2
  slug: aemo-balancing-reports-v2-2-openapi
- description: AEMO Balancing Reports v2.3 from AEMO — 6 path(s) described in OpenAPI.
  name: AEMO Balancing Reports v2.3
  slug: aemo-balancing-reports-v2-3-openapi
- description: AEMO Balancing Reports v2.4 from AEMO — 6 path(s) described in OpenAPI.
  name: AEMO Balancing Reports v2.4
  slug: aemo-balancing-reports-v2-4-openapi
- description: AEMO Balancing Reports v2.5 from AEMO — 7 path(s) described in OpenAPI.
  name: AEMO Balancing Reports v2.5
  slug: aemo-balancing-reports-v2-5-openapi
- description: AEMO Balancing Reports v2 from AEMO — 5 path(s) described in OpenAPI.
  name: AEMO Balancing Reports v2
  slug: aemo-balancing-reports-v2-openapi
- description: AEMO Balancing Submission v2 from AEMO — 8 path(s) described in OpenAPI.
  name: AEMO Balancing Submission v2
  slug: aemo-balancing-submission-v2-openapi
- description: AEMO NEMDispatchBidding from AEMO — 5 path(s) described in OpenAPI.
  name: AEMO NEMDispatchBidding
  slug: aemo-bidding-v1-openapi
- description: AEMO Bilateral/Stem Submission v1 from AEMO — 2 path(s) described in OpenAPI.
  name: AEMO Bilateral/Stem Submission v1
  slug: aemo-bilateral-stem-submission-v1-openapi
- description: AEMO BlindUpdate from AEMO — 3 path(s) described in OpenAPI.
  name: AEMO BlindUpdate
  slug: aemo-blindupdate-v1-openapi
- description: AEMO Capacity from AEMO — 13 path(s) described in OpenAPI.
  name: AEMO Capacity
  slug: aemo-capacity-v1-openapi
- description: AEMO CapacityAuction from AEMO — 5 path(s) described in OpenAPI.
  name: AEMO CapacityAuction
  slug: aemo-capacityauction-v1-openapi
- description: AEMO DER Registration for NSPs from AEMO — 8 path(s) described in OpenAPI.
  name: AEMO DER Registration for NSPs
  slug: aemo-der-business-registration-v1-openapi
- description: AEMO DER Registration For Account Holders from AEMO — 31 path(s) described in OpenAPI.
  name: AEMO DER Registration For Account Holders
  slug: aemo-der-consumer-registration-v1-openapi
- description: AEMO WEM DER Installation V2 from AEMO — 3 path(s) described in OpenAPI.
  name: AEMO WEM DER Installation V2
  slug: aemo-der-register-installation-v2-openapi
- description: AEMO WEM DER NMI from AEMO — 2 path(s) described in OpenAPI.
  name: AEMO WEM DER NMI
  slug: aemo-der-register-nmi-v1-openapi
- description: AEMO EE Simulation Status Update from AEMO — 2 path(s) described in OpenAPI.
  name: AEMO EE Simulation Status Update
  slug: aemo-ee-simulation-status-update-v1-openapi
- description: AEMO EnablementInstruction from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO EnablementInstruction
  slug: aemo-enablementinstruction-v1-openapi
- description: AEMO GasBB Reporting Public Data from AEMO — 28 path(s) described in OpenAPI.
  name: AEMO GasBB Reporting Public Data
  slug: aemo-gasbb-reporting-public-data-openapi
- description: AEMO GeneratorRecall from AEMO — 3 path(s) described in OpenAPI.
  name: AEMO GeneratorRecall
  slug: aemo-generatorrecall-v1-openapi
- description: AEMO HubMessageManagement from AEMO — 2 path(s) described in OpenAPI.
  name: AEMO HubMessageManagement
  slug: aemo-hubmsgmgt-v1-openapi
- description: AEMO HubMessageManagementV2 from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO HubMessageManagementV2
  slug: aemo-hubmsgmgt-v2-openapi
- description: AEMO IdentityService(v2) from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO IdentityService(v2)
  slug: aemo-identityservice-v2-openapi
- description: AEMO LFAS Reports v2 from AEMO — 4 path(s) described in OpenAPI.
  name: AEMO LFAS Reports v2
  slug: aemo-lfas-reports-v2-openapi
- description: AEMO LFAS Submission v2 from AEMO — 8 path(s) described in OpenAPI.
  name: AEMO LFAS Submission v2
  slug: aemo-lfas-submission-v2-openapi
- description: AEMO Market Reports v2 from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO Market Reports v2
  slug: aemo-market-reports-v2-openapi
- description: AEMO MeterExemption from AEMO — 3 path(s) described in OpenAPI.
  name: AEMO MeterExemption
  slug: aemo-meterexemption-external-v1-openapi
- description: AEMO MT PASA Offers from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO MT PASA Offers
  slug: aemo-mtpasaoffers-v1-openapi
- description: AEMO Oauth-v1 from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO Oauth-v1
  slug: aemo-oauth-v1-openapi
- description: AEMO OIP from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO OIP
  slug: aemo-oip-external-v1-openapi
- description: AEMO Intermittent Generation Availability Submissions from AEMO — 2 path(s) described in OpenAPI.
  name: AEMO Intermittent Generation Availability Submissions
  slug: aemo-opsforecasting-intermittentgen-v1-openapi
- description: AEMO Outage Management from AEMO — 8 path(s) described in OpenAPI.
  name: AEMO Outage Management
  slug: aemo-outage-management-external-v1-openapi
- description: AEMO P2PMessagingSync from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO P2PMessagingSync
  slug: aemo-p2pmessaging-sync-v1-openapi
- description: AEMO Pre-Balancing Reports v6 from AEMO — 70 path(s) described in OpenAPI.
  name: AEMO Pre-Balancing Reports v6
  slug: aemo-pre-balancing-reports-v6-openapi
- description: AEMO Pre-Balancing Reports v7.1 from AEMO — 71 path(s) described in OpenAPI.
  name: AEMO Pre-Balancing Reports v7.1
  slug: aemo-pre-balancing-reports-v7-1-openapi
- description: AEMO Pre-Balancing Reports v7 from AEMO — 71 path(s) described in OpenAPI.
  name: AEMO Pre-Balancing Reports v7
  slug: aemo-pre-balancing-reports-v7-openapi
- description: AEMO Pre-Balancing Reports v8 from AEMO — 73 path(s) described in OpenAPI.
  name: AEMO Pre-Balancing Reports v8
  slug: aemo-pre-balancing-reports-v8-openapi
- description: AEMO Prudentials from AEMO — 10 path(s) described in OpenAPI.
  name: AEMO Prudentials
  slug: aemo-prudentials-v1-openapi
- description: AEMO RCM Operations from AEMO — 47 path(s) described in OpenAPI.
  name: AEMO RCM Operations
  slug: aemo-rcm-ops-external-v1-openapi
- description: AEMO Reallocations from AEMO — 13 path(s) described in OpenAPI.
  name: AEMO Reallocations
  slug: aemo-reallocations-v1-openapi
- description: AEMO Report from AEMO — 22 path(s) described in OpenAPI.
  name: AEMO Report
  slug: aemo-report-v1-openapi
- description: AEMO RTMS from AEMO — 14 path(s) described in OpenAPI.
  name: AEMO RTMS
  slug: aemo-rtms-external-v1-openapi
- description: AEMO SelfForecast from AEMO — 2 path(s) described in OpenAPI.
  name: AEMO SelfForecast
  slug: aemo-selfforecast-v1-openapi
- description: AEMO Settlement Direct from AEMO — 13 path(s) described in OpenAPI.
  name: AEMO Settlement Direct
  slug: aemo-settlementdirect-v1-openapi
- description: AEMO Submission from AEMO — 36 path(s) described in OpenAPI.
  name: AEMO Submission
  slug: aemo-submission-v1-openapi
- description: AEMO System Management Reports v2.1 from AEMO — 9 path(s) described in OpenAPI.
  name: AEMO System Management Reports v2.1
  slug: aemo-system-management-reports-v2-1-openapi
- description: AEMO System Management Reports v2.2 from AEMO — 10 path(s) described in OpenAPI.
  name: AEMO System Management Reports v2.2
  slug: aemo-system-management-reports-v2-2-openapi
- description: AEMO System Management Reports v2.3 from AEMO — 10 path(s) described in OpenAPI.
  name: AEMO System Management Reports v2.3
  slug: aemo-system-management-reports-v2-3-openapi
- description: AEMO System Management Reports v2.4 from AEMO — 10 path(s) described in OpenAPI.
  name: AEMO System Management Reports v2.4
  slug: aemo-system-management-reports-v2-4-openapi
- description: AEMO System Management Reports v2.5 from AEMO — 10 path(s) described in OpenAPI.
  name: AEMO System Management Reports v2.5
  slug: aemo-system-management-reports-v2-5-openapi
- description: AEMO System Management Reports v2.6 from AEMO — 10 path(s) described in OpenAPI.
  name: AEMO System Management Reports v2.6
  slug: aemo-system-management-reports-v2-6-openapi
- description: AEMO System Management Reports v2 from AEMO — 7 path(s) described in OpenAPI.
  name: AEMO System Management Reports v2
  slug: aemo-system-management-reports-v2-openapi
- description: AEMO TLS Certificate Mgmt v1 from AEMO — 8 path(s) described in OpenAPI.
  name: AEMO TLS Certificate Mgmt v1
  slug: aemo-tls-certificate-mgmt-v1-openapi
- description: AEMO VariableParameter from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO VariableParameter
  slug: aemo-variableparameter-v1-openapi
- description: AEMO WEMDE DispatchCase from AEMO — 4 path(s) described in OpenAPI.
  name: AEMO WEMDE DispatchCase
  slug: aemo-wemde-dispatchcase-external-v1-openapi
- description: AEMO WEMDE DispatchCase V2 from AEMO — 3 path(s) described in OpenAPI.
  name: AEMO WEMDE DispatchCase V2
  slug: aemo-wemde-dispatchcase-external-v2-openapi
- description: AEMO WEMDE DispatchInstruction from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO WEMDE DispatchInstruction
  slug: aemo-wemde-dispatchinstruction-external-v1-openapi
- description: AEMO WEMDE DispatchSolution from AEMO — 4 path(s) described in OpenAPI.
  name: AEMO WEMDE DispatchSolution
  slug: aemo-wemde-dispatchsolution-external-v1-openapi
- description: AEMO WEMDE DispatchSolution V2 from AEMO — 3 path(s) described in OpenAPI.
  name: AEMO WEMDE DispatchSolution V2
  slug: aemo-wemde-dispatchsolution-external-v2-openapi
- description: AEMO WEMDE DispatchSummary from AEMO — 4 path(s) described in OpenAPI.
  name: AEMO WEMDE DispatchSummary
  slug: aemo-wemde-dispatchsummary-external-v1-openapi
- description: AEMO WEMDE DSPDispatchInstruction from AEMO — 5 path(s) described in OpenAPI.
  name: AEMO WEMDE DSPDispatchInstruction
  slug: aemo-wemde-dspdispatchinstruction-external-v1-openapi
- description: AEMO WEMDE NCESS from AEMO — 2 path(s) described in OpenAPI.
  name: AEMO WEMDE NCESS
  slug: aemo-wemde-ncess-external-v1-openapi
- description: AEMO WEMDE NotInServiceCapacity from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO WEMDE NotInServiceCapacity
  slug: aemo-wemde-notinservicecapacity-external-v1-openapi
- description: AEMO WEMDE ReferenceTradingPrice from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO WEMDE ReferenceTradingPrice
  slug: aemo-wemde-referencetradingprice-external-v1-openapi
- description: AEMO WEMDE TradingDayReport from AEMO — 1 path(s) described in OpenAPI.
  name: AEMO WEMDE TradingDayReport
  slug: aemo-wemde-tradingdayreport-external-v1-openapi
artifact_total: 160
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
overview: 'AEMO publishes 74 APIs on the [APIs.io](https://apis.io/) network, including CDR, CDR Common, WEM Attributes Report, and 71 more. Tagged areas include Energy, Australia, Electricity, Gas, and Energy Markets.


  The AEMO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AEMO''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 45 more developer resources.'
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
  composite: 60.5
  delta: -2.4
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 56.2
    developer_ergonomics: 70.8
    discoverability: 79.6
    governance: 31.8
    operational_transparency: 52.6
  previous_composite: 62.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 76
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
