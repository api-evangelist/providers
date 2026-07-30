---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-07-28'
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
- description: The B2BMessagingAsync API is a B2B SMP APIs used to send and recieve B2B messages between the participants in an asynchronous fashion. AEMO's public API catalogue lists 3 operation(s) for this API, ga
  name: AEMO B2BMessagingAsync
  slug: aemo-b2bmessagingasync
- description: The B2BMessagingPull API is a B2B SMP API used to send and receive B2B messages between the participants in a Pull messaging pattern. The messages will be queued in the e-Hub and the receiving partici
  name: AEMO B2BMessagingPull
  slug: aemo-b2bmessagingpull
- description: The B2BMessagingSync API is a B2B SMP APIs used to send and receive B2B messages between the participants in a synchronous fashion. AEMO's public API catalogue lists 1 operation(s) for this API, gatew
  name: AEMO B2BMessagingSync
  slug: aemo-b2bmessagingsync
- description: The B2MMessagingAsync push-push API supports inbound submitMessages, submitMessageAcknowledgements, and getQueueMetaData endpoints and suits a high volume exchange of messages. Participants push their
  name: AEMO B2MMessagingAsync
  slug: aemo-b2mmessagingasync
- description: The B2MMessagingPull push-pull API supports inbound submitMessages, submitMessageAcknowledgements, getMessages, and getQueueMetaData endpoints and suits low volume exchange of messages. Participants u
  name: AEMO B2MMessagingPull
  slug: aemo-b2mmessagingpull
- description: The B2MMessagingSync API supports generateC1Report, generateC4Report, getMSATSLimits,NMIDiscovery, getNMIDetail, getParticipantSystemStatus, and getMeterData endpoints.The API participant pushes their
  name: AEMO B2MMessagingSync
  slug: aemo-b2mmessagingsync
- description: 'AEMO''s public API catalogue lists 5 operation(s) for this API, gateway-routed under the path prefix /WEM/balancing. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with '
  name: AEMO Balancing Reports v2
  slug: aemo-balancing-reports-v2
- description: 'AEMO''s public API catalogue lists 5 operation(s) for this API, gateway-routed under the path prefix /WEM/balancing. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with '
  name: AEMO Balancing Reports v2.1
  slug: aemo-balancing-reports-v2-1
- description: 'AEMO''s public API catalogue lists 6 operation(s) for this API, gateway-routed under the path prefix /WEM/balancing. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with '
  name: AEMO Balancing Reports v2.2
  slug: aemo-balancing-reports-v2-2
- description: 'AEMO''s public API catalogue lists 6 operation(s) for this API, gateway-routed under the path prefix /WEM/balancing. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with '
  name: AEMO Balancing Reports v2.3
  slug: aemo-balancing-reports-v2-3
- description: 'AEMO''s public API catalogue lists 6 operation(s) for this API, gateway-routed under the path prefix /WEM/balancing. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with '
  name: AEMO Balancing Reports v2.4
  slug: aemo-balancing-reports-v2-4
- description: 'AEMO''s public API catalogue lists 7 operation(s) for this API, gateway-routed under the path prefix /WEM/balancing. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with '
  name: AEMO Balancing Reports v2.5
  slug: aemo-balancing-reports-v2-5
- description: AEMO's public API catalogue lists 8 operation(s) for this API, gateway-routed under the path prefix /WEM/balancing/submissions. AEMO's own openapi-link export for this API is a shell — it declares pat
  name: AEMO Balancing Submission v2
  slug: aemo-balancing-submission-v2
- description: 'AEMO''s public API catalogue lists 2 operation(s) for this API, gateway-routed under the path prefix /WEM/trading. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with ze'
  name: AEMO Bilateral/Stem Submission v1
  slug: aemo-bilateral-stem-submission-v1
- description: The BlindUpdateTool API supports Upload of blind update Data by participants facing API's to backend MSATS systems , Download processed Blind Update file, List of all the Blind Update files uploaded b
  name: AEMO BlindUpdate
  slug: aemo-blindupdate
- description: The Capacity API is used by facility operators and trading participants to submit and receive data relating to capacity trades and day ahead auction for AEMO’s Capacity Transfer Platform (CTP) and Day
  name: AEMO Capacity
  slug: aemo-capacity
- description: The Capacity Auction API is used by facility operators and trading participants to submit and receive data relating to capacity trades and day ahead auction for AEMO’s Capacity Transfer Platform (CTP)
  name: AEMO CapacityAuction
  slug: aemo-capacityauction
- description: The Consumer Data Right (CDR) APIs allow Registered Financially Responsible Market Participants (FRMPs) to service API requests for AEMO data from Accredited Data Recipients. AEMO's public API catalog
  name: AEMO CDR
  slug: aemo-cdr
- description: AEMO's public API catalogue lists 2 operation(s) for this API, gateway-routed under the path prefix /NEMRetail/cds-au/v1/discovery. AEMO's own openapi-link export for this API is a shell — it declares
  name: AEMO CDR Common
  slug: aemo-cdr-common
- description: Using the DER Registration APIs, Account Holders can • Submit DER Connection Agreement data. • Provide AC Connections, and Device details in the same submission AEMO's public API catalogue lists 31 op
  name: AEMO DER Registration For Account Holders
  slug: aemo-der-registration-for-account-holders
- description: Using the DER Registration APIs, NSPs can • Submit DER Connection Agreement data. • Provide AC Connections, and Device details in the same submission AEMO's public API catalogue lists 8 operation(s) f
  name: AEMO DER Registration for NSPs
  slug: aemo-der-registration-for-nsps
- description: EE Simulation Status Update APIs are used by EE to submit the simulation status update AEMO's public API catalogue lists 2 operation(s) for this API, gateway-routed under the path prefix /ee-simulatio
  name: AEMO EE Simulation Status Update
  slug: aemo-ee-simulation-status-update
- description: AEMO's public API catalogue lists 1 operation(s) for this API, gateway-routed under the path prefix /NEM/v1/ISF-External/enablementInstruction. AEMO's own openapi-link export for this API is a shell —
  name: AEMO EnablementInstruction
  slug: aemo-enablementinstruction
- description: This API is intended for AEMO's use only, used by AEMO web pages and is not supported for any other use. It can change at any time. See https://dev.aemo.com.au/ for information on using AEMO APIs. AEM
  name: AEMO GasBB Reporting Public Data
  slug: aemo-gasbb-reporting-public-data
- description: The Generator Recall API is used by generators to send information about recall times into the Generator Recall web-based interface in the EMMS Markets Portal. The system will then transfer the inform
  name: AEMO GeneratorRecall
  slug: aemo-generatorrecall
- description: The HubMessageManagement API is a B2B SMP APIs used retrieve the current list of stop files for all participants or for a specific participant (using alerts) resource. Participants can use this resour
  name: AEMO HubMessageManagement
  slug: aemo-hubmessagemanagement
- description: The HubMessageManagement push API retrieves the current list of B2B and B2M stop files. Business transactions are sent as aseXML documents carried as payloads inside the API message and transmitted ov
  name: AEMO HubMessageManagementV2
  slug: aemo-hubmessagemanagementv2
- description: This API is used by a Participant to update their password for MSATs. AEMO's public API catalogue lists 1 operation(s) for this API, gateway-routed under the path prefix /ws/Common/identityService. AE
  name: AEMO IdentityService(v2)
  slug: aemo-identityservice-v2
- description: This API is used for intermittent generation availability submissions. AEMO's public API catalogue lists 2 operation(s) for this API, gateway-routed under the path prefix /v1/IntermittentGen. AEMO's o
  name: AEMO Intermittent Generation Availability Submissions
  slug: aemo-intermittent-generation-availability-submissions
- description: 'AEMO''s public API catalogue lists 4 operation(s) for this API, gateway-routed under the path prefix /WEM/lfas/v2. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with ze'
  name: AEMO LFAS Reports v2
  slug: aemo-lfas-reports-v2
- description: AEMO's public API catalogue lists 8 operation(s) for this API, gateway-routed under the path prefix /WEM/lfas/submissions/v2. AEMO's own openapi-link export for this API is a shell — it declares paths
  name: AEMO LFAS Submission v2
  slug: aemo-lfas-submission-v2
- description: 'AEMO''s public API catalogue lists 1 operation(s) for this API, gateway-routed under the path prefix /WEM/market. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with zer'
  name: AEMO Market Reports v2
  slug: aemo-market-reports-v2
- description: The Meter Exemptions API enables registered Metering Coordinators (MCs) to create and manage metering exemptions within MSATS. AEMO's public API catalogue lists 3 operation(s) for this API, gateway-ro
  name: AEMO MeterExemption
  slug: aemo-meterexemption
- description: The MT PASA Offers API allows Scheduled Generators, Market Customers, Market Network Service Providers, and Integrated Resource Providers to submit their MT PASA Offers for Bi-directional Units (BDU),
  name: AEMO MT PASA Offers
  slug: aemo-mt-pasa-offers
- description: Bidding Service Open API specification AEMO's public API catalogue lists 5 operation(s) for this API, gateway-routed under the path prefix /NEMWholesale/bidding. AEMO's own openapi-link export for thi
  name: AEMO NEMDispatchBidding
  slug: aemo-nemdispatchbidding
- description: 'AEMO''s public API catalogue lists 1 operation(s) for this API, gateway-routed under the path prefix /oauth/v1. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with zero '
  name: AEMO oauth-v1
  slug: aemo-oauth-v1
- description: AEMO's public API catalogue lists 1 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/outageIntentionPlan. AEMO's own openapi-link export for this API is a shell — it declares pa
  name: AEMO OIP
  slug: aemo-oip
- description: AEMO's public API catalogue lists 8 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/outageManagement. AEMO's own openapi-link export for this API is a shell — it declares paths
  name: AEMO Outage Management
  slug: aemo-outage-management
- description: 'The P2PMessagingSync API is a B2B SMP APIs used to exchange the following Peer-to-Peer information via the e-Hub: - Free-form information - Documents (also called Attachments). The P2PMessagingSync AP'
  name: AEMO P2PMessagingSync
  slug: aemo-p2pmessagingsync
- description: 'AEMO''s public API catalogue lists 70 operation(s) for this API, gateway-routed under the path prefix /WEM/reports. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with z'
  name: AEMO Pre-Balancing Reports v6
  slug: aemo-pre-balancing-reports-v6
- description: 'AEMO''s public API catalogue lists 71 operation(s) for this API, gateway-routed under the path prefix /WEM/reports. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with z'
  name: AEMO Pre-Balancing Reports v7
  slug: aemo-pre-balancing-reports-v7
- description: 'AEMO''s public API catalogue lists 71 operation(s) for this API, gateway-routed under the path prefix /WEM/reports. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with z'
  name: AEMO Pre-Balancing Reports v7.1
  slug: aemo-pre-balancing-reports-v7-1
- description: 'AEMO''s public API catalogue lists 73 operation(s) for this API, gateway-routed under the path prefix /WEM/reports. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with z'
  name: AEMO Pre-Balancing Reports v8
  slug: aemo-pre-balancing-reports-v8
- description: This API supports the various operations performed on Prudentials dashboard AEMO's public API catalogue lists 10 operation(s) for this API, gateway-routed under the path prefix /NEMWholesale/Prudentia
  name: AEMO Prudentials
  slug: aemo-prudentials
- description: 'AEMO''s public API catalogue lists 50 operation(s) for this API, gateway-routed under the path prefix /WEM/RCM. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with zero '
  name: AEMO RCM Operations
  slug: aemo-rcm-operations
- description: The Reallocation API allow you to create, authorise, cancel reallocations. You can also search and retrieve reallocations, calendars, participants, profile types, agreement types, and market price cap
  name: AEMO Reallocations
  slug: aemo-reallocations
- description: The report API allows participants to retrieve data from the Gas Bulletin Board (BB). AEMO's public API catalogue lists 22 operation(s) for this API, gateway-routed under the path prefix /ws/gbb/repor
  name: AEMO Report
  slug: aemo-report
- description: The WEM-Reform API for Real-Time Market submissions available to all Market Participants. AEMO's public API catalogue lists 15 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/r
  name: AEMO RTMS
  slug: aemo-rtms
- description: The Self forecasting API is used by participants who wish to submit their Solar or Wind Forecasts for a DUID to AEMO. AEMO's public API catalogue lists 2 operation(s) for this API, gateway-routed unde
  name: AEMO SelfForecast
  slug: aemo-selfforecast
- description: This API supports the various operations performed in Settlement Direct API AEMO's public API catalogue lists 13 operation(s) for this API, gateway-routed under the path prefix /NEMWholesale/Publishin
  name: AEMO Settlement Direct
  slug: aemo-settlement-direct
- description: The submission API allows participants to submit data to the Gas Bulletin Board (BB). Data submission from BB reporting entities to the BB are divided into two key areas- - Data transfer formats which
  name: AEMO Submission
  slug: aemo-submission
- description: 'AEMO''s public API catalogue lists 7 operation(s) for this API, gateway-routed under the path prefix /WEM/sm. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with zero op'
  name: AEMO System Management Reports v2
  slug: aemo-system-management-reports-v2
- description: 'AEMO''s public API catalogue lists 9 operation(s) for this API, gateway-routed under the path prefix /WEM/sm. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with zero op'
  name: AEMO System Management Reports v2.1
  slug: aemo-system-management-reports-v2-1
- description: 'AEMO''s public API catalogue lists 10 operation(s) for this API, gateway-routed under the path prefix /WEM/sm. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with zero o'
  name: AEMO System Management Reports v2.2
  slug: aemo-system-management-reports-v2-2
- description: 'AEMO''s public API catalogue lists 10 operation(s) for this API, gateway-routed under the path prefix /WEM/sm. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with zero o'
  name: AEMO System Management Reports v2.3
  slug: aemo-system-management-reports-v2-3
- description: 'AEMO''s public API catalogue lists 10 operation(s) for this API, gateway-routed under the path prefix /WEM/sm. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with zero o'
  name: AEMO System Management Reports v2.4
  slug: aemo-system-management-reports-v2-4
- description: 'AEMO''s public API catalogue lists 10 operation(s) for this API, gateway-routed under the path prefix /WEM/sm. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with zero o'
  name: AEMO System Management Reports v2.5
  slug: aemo-system-management-reports-v2-5
- description: 'AEMO''s public API catalogue lists 10 operation(s) for this API, gateway-routed under the path prefix /WEM/sm. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with zero o'
  name: AEMO System Management Reports v2.6
  slug: aemo-system-management-reports-v2-6
- description: The TLS Certificate Management API allows authorised participants to self-manage their AEMO-signed TLS certificates. AEMO's public API catalogue lists 8 operation(s) for this API, gateway-routed under
  name: AEMO TLS Certificate Mgmt v1
  slug: aemo-tls-certificate-mgmt-v1
- description: 'AEMO''s public API catalogue lists 2 operation(s) for this API, gateway-routed under the path prefix /NEM/v1/ISF-External/variableParameter. AEMO''s own openapi-link export for this API is a shell — it '
  name: AEMO VariableParameter
  slug: aemo-variableparameter
- description: 'AEMO''s public API catalogue lists 2 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/attributes. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} w'
  name: AEMO WEM Attributes Report
  slug: aemo-wem-attributes-report
- description: WEM DER Installation API enables the Network Operator to create, update, and retrieve the DER Register information details for the DER installations they have submitted to the DER Register database an
  name: AEMO WEM DER Installation V2
  slug: aemo-wem-der-installation-v2
- description: Using the WEM DER Registration APIs, consumers can Create, update and retrieve NMI details AEMO's public API catalogue lists 3 operation(s) for this API, gateway-routed under the path prefix /wem/v1/d
  name: AEMO WEM DER NMI
  slug: aemo-wem-der-nmi
- description: 'AEMO''s public API catalogue lists 4 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/dispatchCase. AEMO''s own openapi-link export for this API is a shell — it declares paths: {}'
  name: AEMO WEMDE DispatchCase
  slug: aemo-wemde-dispatchcase
- description: 'AEMO''s public API catalogue lists 3 operation(s) for this API, gateway-routed under the path prefix /WEM/v2/dispatchCase. AEMO''s own openapi-link export for this API is a shell — it declares paths: {}'
  name: AEMO WEMDE DispatchCase V2
  slug: aemo-wemde-dispatchcase-v2
- description: AEMO's public API catalogue lists 1 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/dispatchInstruction. AEMO's own openapi-link export for this API is a shell — it declares pa
  name: AEMO WEMDE DispatchInstruction
  slug: aemo-wemde-dispatchinstruction
- description: AEMO's public API catalogue lists 4 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/dispatchSolution. AEMO's own openapi-link export for this API is a shell — it declares paths
  name: AEMO WEMDE DispatchSolution
  slug: aemo-wemde-dispatchsolution
- description: AEMO's public API catalogue lists 3 operation(s) for this API, gateway-routed under the path prefix /WEM/v2/dispatchSolution. AEMO's own openapi-link export for this API is a shell — it declares paths
  name: AEMO WEMDE DispatchSolution V2
  slug: aemo-wemde-dispatchsolution-v2
- description: 'AEMO''s public API catalogue lists 4 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/dispatchSummary. AEMO''s own openapi-link export for this API is a shell — it declares paths:'
  name: AEMO WEMDE DispatchSummary
  slug: aemo-wemde-dispatchsummary
- description: AEMO's public API catalogue lists 5 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/DSPDispatchInstruction. AEMO's own openapi-link export for this API is a shell — it declares
  name: AEMO WEMDE DSPDispatchInstruction
  slug: aemo-wemde-dspdispatchinstruction
- description: 'AEMO''s public API catalogue lists 2 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/Ncess. AEMO''s own openapi-link export for this API is a shell — it declares paths: {} with z'
  name: AEMO WEMDE NCESS
  slug: aemo-wemde-ncess
- description: AEMO's public API catalogue lists 1 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/notInServiceCapacity. AEMO's own openapi-link export for this API is a shell — it declares p
  name: AEMO WEMDE NotInServiceCapacity
  slug: aemo-wemde-notinservicecapacity
- description: 'AEMO''s public API catalogue lists 1 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/referenceTradingPrice. AEMO''s own openapi-link export for this API is a shell — it declares '
  name: AEMO WEMDE ReferenceTradingPrice
  slug: aemo-wemde-referencetradingprice
- description: AEMO's public API catalogue lists 1 operation(s) for this API, gateway-routed under the path prefix /WEM/v1/tradingDayReport. AEMO's own openapi-link export for this API is a shell — it declares paths
  name: AEMO WEMDE TradingDayReport
  slug: aemo-wemde-tradingdayreport
artifact_total: 84
asyncapis:
- description: ''
  name: Aemo Ehub Events
  slug: aemo-ehub-events
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
overview: 'AEMO publishes 74 APIs on the [APIs.io](https://apis.io/) network, including B2BMessagingAsync, B2BMessagingPull, B2BMessagingSync, and 71 more. Tagged areas include Energy, Australia, Electricity, Gas, and Energy Markets.


  The AEMO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AEMO''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 45 more developer resources.'
random_paper: 8
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
  composite: 57.6
  delta: -1.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 66.8
    developer_ergonomics: 64.7
    discoverability: 77.8
    governance: 21.9
    operational_transparency: 57.9
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 97.4
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
    score: 75.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
