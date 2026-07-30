---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 313
  human_in_the_loop: 1
  name: 3Gpp Agentic Access
  operation_count: 465
  slug: 3gpp-agentic-access
  summary_line: 465 operations · 313 acting · 1 human-in-the-loop
api_count: 117
apis:
- description: OAS 3.0.1 specification of the MDA NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management servi
  name: 3GPP TS 28.104 Mda Nrm API
  slug: 3gpp-ts28104-mdanrm
- description: OAS 3.0.1 specification of the MDA Report. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management se
  name: 3GPP TS 28.104 Mda Report API
  slug: 3gpp-ts28104-mdareport
- description: OAS 3.0.1 specification of the AI/ML NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management ser
  name: 3GPP TS 28.105 Ai Ml Nrm API
  slug: 3gpp-ts28105-aimlnrm
- description: OAS 3.0.1 definition of the Fault Supervision MnS. An OpenAPI 3.0.1 document with 1 path(s), API version 19.3.0, published verbatim by 3GPP in 3GPP TS 28.111 as part of the Management Services (SA5 OA
  name: 3GPP TS 28.111 Fault Notifications API
  slug: 3gpp-ts28111-faultnotifications
- description: OAS 3.0.1 definition of the Fault Supervision MnS. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance manag
  name: 3GPP TS 28.111 Fault Nrm API
  slug: 3gpp-ts28111-faultnrm
- description: OAS 3.0.1 specification of the Energy Information NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance m
  name: 3GPP TS 28.310 Energy Information Nrm API
  slug: 3gpp-ts28310-energyinformationnrm
- description: OAS 3.0.1 definition of scenario specific Intent Expectations. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Perfo
  name: 3GPP TS 28.312 Intent Expectations API
  slug: 3gpp-ts28312-intentexpectations
- description: OAS 3.0.1 definition of the Intent NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management servi
  name: 3GPP TS 28.312 Intent Nrm API
  slug: 3gpp-ts28312-intentnrm
- description: OAS 3.0.1 definition of the RANSC NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management servic
  name: 3GPP TS 28.317 Ran Sc Nrm API
  slug: 3gpp-ts28317-ranscnrm
- description: OAS 3.0.1 specification of the OutageAndRecoveryInfo NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performanc
  name: 3GPP TS 28.318 Dso Nrm API
  slug: 3gpp-ts28318-dsonrm
- description: OAS 3.0.1 definition of the MSAC NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management service
  name: 3GPP TS 28.319 Msac Nrm API
  slug: 3gpp-ts28319-msacnrm
- description: OAS 3.0.1 definition of the Network Slice Provisioning MnS. An OpenAPI 3.0.1 document with 2 path(s), API version 18.6.0, published verbatim by 3GPP in 3GPP TS 28.531 as part of the Management Service
  name: 3GPP TS 28.531 NS Prov Mn S API
  slug: 3gpp-ts28531-nsprovmns
- description: OAS 3.0.1 definition of the Network Slice Suubnet Provisioning MnS. An OpenAPI 3.0.1 document with 2 path(s), API version 18.6.0, published verbatim by 3GPP in 3GPP TS 28.531 as part of the Management
  name: 3GPP TS 28.531 NSS Prov Mn S API
  slug: 3gpp-ts28531-nssprovmns
- description: 'OAS 3.0.1 definition of the File Data Reporting MnS. An OpenAPI 3.0.1 document with 3 path(s), API version 19.1.0, published verbatim by 3GPP in 3GPP TS 28.532 as part of the Management Services (SA5 '
  name: 3GPP TS 28.532 File Data Reporting Mn S API
  slug: 3gpp-ts28532-filedatareportingmns
- description: OAS 3.0.1 definition of the heartbeat notification. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance mana
  name: 3GPP TS 28.532 Heartbeat Ntf API
  slug: 3gpp-ts28532-heartbeatntf
- description: OAS 3.0.1 definition of the Performance Threshold Monitoring MnS. An OpenAPI 3.0.1 document with 1 path(s), API version 18.1.0, published verbatim by 3GPP in 3GPP TS 28.532 as part of the Management S
  name: 3GPP TS 28.532 Perf Mn S API
  slug: 3gpp-ts28532-perfmns
- description: OAS 3.0.1 definition of the Provisioning MnS. An OpenAPI 3.0.1 document with 2 path(s), API version 19.2.0, published verbatim by 3GPP in 3GPP TS 28.532 as part of the Management Services (SA5 OAM) su
  name: 3GPP TS 28.532 Prov Mn S API
  slug: 3gpp-ts28532-provmns
- description: 'OAS 3.0.1 specification for the Streaming data reporting service (Streaming MnS). An OpenAPI 3.0.1 document with 4 path(s), API version 19.0.0, published verbatim by 3GPP in 3GPP TS 28.532 as part of '
  name: 3GPP TS 28.532 Streaming Data Mn S API
  slug: 3gpp-ts28532-streamingdatamns
- description: OAS 3.0.1 specification of the Cosla NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management ser
  name: 3GPP TS 28.536 Cosla Nrm API
  slug: 3gpp-ts28536-coslanrm
- description: OAS 3.0.1 specification of the Edge NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management serv
  name: 3GPP TS 28.538 Edge Nrm API
  slug: 3gpp-ts28538-edgenrm
- description: OAS 3.0.1 specification of the 5GC NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management servi
  name: 3GPP TS 28.541 5 Gc Nrm API
  slug: 3gpp-ts28541-5gcnrm
- description: OAS 3.0.1 specification of the NR NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management servic
  name: 3GPP TS 28.541 Nr Nrm API
  slug: 3gpp-ts28541-nrnrm
- description: OAS 3.0.1 specification of the Slice NRM @ 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved. An OpenAPI 3.0.1 data-model-only document (no paths; it de
  name: 3GPP TS 28.541 Slice Nrm API
  slug: 3gpp-ts28541-slicenrm
- description: OAS 3.0.1 specification of the Performance Measurement Job Control Service @ 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved. An OpenAPI 3.0.1 documen
  name: 3GPP TS 28.550 Perf Meas Job Ctrl Mn S API
  slug: 3gpp-ts28550-perfmeasjobctrlmns
- description: OAS 3.0.1 definition of the NDT NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management services
  name: 3GPP TS 28.561 Ndt Nrm API
  slug: 3gpp-ts28561-ndtnrm
- description: OAS 3.0.1 definition of the CCL NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management services
  name: 3GPP TS 28.567 Ccl Nrm API
  slug: 3gpp-ts28567-cclnrm
- description: OAS 3.0.1 specification of API for managing network configuration plans and related jobs. An OpenAPI 3.0.1 document with 16 path(s), API version 19.2.0, published verbatim by 3GPP in 3GPP TS 28.572 as
  name: 3GPP TS 28.572 Plan Management API
  slug: 3gpp-ts28572-planmanagement
- description: OAS 3.0.1 specification of common type definitions in the Generic NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning a
  name: 3GPP TS 28.623 Com Defs API
  slug: 3gpp-ts28623-comdefs
- description: OAS 3.0.1 definition of the External data type NRM fragment. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Perform
  name: 3GPP TS 28.623 External Data Mgmt Nrm API
  slug: 3gpp-ts28623-externaldatamgmtnrm
- description: 'OAS 3.0.1 definition of the Features of NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management '
  name: 3GPP TS 28.623 Feature Nrm API
  slug: 3gpp-ts28623-featurenrm
- description: OAS 3.0.1 definition of the File Management NRM fragment. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performanc
  name: 3GPP TS 28.623 File Management Nrm API
  slug: 3gpp-ts28623-filemanagementnrm
- description: OAS 3.0.1 definition of the Generic NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management serv
  name: 3GPP TS 28.623 Generic Nrm API
  slug: 3gpp-ts28623-genericnrm
- description: OAS 3.0.1 definition of the Management Data Collection NRM fragment. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and
  name: 3GPP TS 28.623 Management Data Collection Nrm API
  slug: 3gpp-ts28623-managementdatacollectionnrm
- description: OAS 3.0.1 definition of the MnS Registry NRM fragment. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance m
  name: 3GPP TS 28.623 Mn S Registry Nrm API
  slug: 3gpp-ts28623-mnsregistrynrm
- description: OAS 3.0.1 definition of the PM control NRM fragment. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance man
  name: 3GPP TS 28.623 Pm Control Nrm API
  slug: 3gpp-ts28623-pmcontrolnrm
- description: OAS 3.0.1 definition of the QoE Measurement Collection NRM. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performa
  name: 3GPP TS 28.623 Qo E Measurement Collection Nrm API
  slug: 3gpp-ts28623-qoemeasurementcollectionnrm
- description: OAS 3.0.1 definition of the Subscription Control NRM fragment. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Perfo
  name: 3GPP TS 28.623 Subscription Control Nrm API
  slug: 3gpp-ts28623-subscriptioncontrolnrm
- description: OAS 3.0.1 definition of the Threshold Monitor NRM fragment. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performa
  name: 3GPP TS 28.623 Threshold Monitor Nrm API
  slug: 3gpp-ts28623-thresholdmonitornrm
- description: 'OAS 3.0.1 definition of the Trace Control NRM fragment. An OpenAPI 3.0.1 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance '
  name: 3GPP TS 28.623 Trace Control Nrm API
  slug: 3gpp-ts28623-tracecontrolnrm
- description: API for setting us an AS session with required QoS. An OpenAPI 3.0.0 document with 2 path(s), API version 1.4.1, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exp
  name: 3GPP TS 29.122 As Session With Qo S API
  slug: 3gpp-ts29122-assessionwithqos
- description: API for Chargeable Party management. An OpenAPI 3.0.0 document with 2 path(s), API version 1.4.1, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exposure) suite an
  name: 3GPP TS 29.122 Chargeable Party API
  slug: 3gpp-ts29122-chargeableparty
- description: Data types applicable to several APIs. An OpenAPI 3.0.0 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance management servic
  name: 3GPP TS 29.122 Common Data API
  slug: 3gpp-ts29122-commondata
- description: 'API for provisioning communication pattern parameters. An OpenAPI 3.0.0 document with 3 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF '
  name: 3GPP TS 29.122 Cp Provisioning API
  slug: 3gpp-ts29122-cpprovisioning
- description: 'Device Triggering API. An OpenAPI 3.0.0 document with 2 path(s), API version 1.3.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exposure) suite and mirrored in '
  name: 3GPP TS 29.122 Device Triggering API
  slug: 3gpp-ts29122-devicetriggering
- description: API for enhanced converage restriction control. An OpenAPI 3.0.0 document with 2 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exposur
  name: 3GPP TS 29.122 ECR Control API
  slug: 3gpp-ts29122-ecrcontrol
- description: API for Group Message Delivery via MBMS by MB2. An OpenAPI 3.0.0 document with 4 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exposur
  name: 3GPP TS 29.122 GM Dvia MBM Sby MB2 API
  slug: 3gpp-ts29122-gmdviambmsbymb2
- description: API for Group Message Delivery via MBMS by xMB. An OpenAPI 3.0.0 document with 4 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exposur
  name: 3GPP TS 29.122 GM Dvia MBM Sbyx MB API
  slug: 3gpp-ts29122-gmdviambmsbyxmb
- description: Monitoring Event API. An OpenAPI 3.0.0 document with 2 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exposure) suite and mirrored in t
  name: 3GPP TS 29.122 Monitoring Event API
  slug: 3gpp-ts29122-monitoringevent
- description: API for MSISDN-less Mobile Originated SMS. An OpenAPI 3.0.0 document with 1 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exposure) su
  name: 3GPP TS 29.122 Msisdn Less Mo Sms API
  slug: 3gpp-ts29122-msisdnlessmosms
- description: API for non IP data delivery. An OpenAPI 3.0.0 document with 6 path(s), API version 1.3.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exposure) suite and mirro
  name: 3GPP TS 29.122 NIDD API
  slug: 3gpp-ts29122-nidd
- description: API for network parameter configuration. An OpenAPI 3.0.0 document with 2 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exposure) suit
  name: 3GPP TS 29.122 Np Configuration API
  slug: 3gpp-ts29122-npconfiguration
- description: Pfd Management API. An OpenAPI 3.0.0 document with 3 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exposure) suite and mirrored in the
  name: 3GPP TS 29.122 Pfd Management API
  slug: 3gpp-ts29122-pfdmanagement
- description: API for provisioning UE radio capability parameters. An OpenAPI 3.0.0 document with 2 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Ex
  name: 3GPP TS 29.122 Racs Parameter Provisioning API
  slug: 3gpp-ts29122-racsparameterprovisioning
- description: API for reporting network status. An OpenAPI 3.0.0 document with 2 path(s), API version 1.3.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exposure) suite and m
  name: 3GPP TS 29.122 Reporting Network Status API
  slug: 3gpp-ts29122-reportingnetworkstatus
- description: API for BDT resouce management. An OpenAPI 3.0.0 document with 2 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.122 as part of the T8 Northbound (SCEF/NEF Exposure) suite and mir
  name: 3GPP TS 29.122 Resource Management Of Bdt API
  slug: 3gpp-ts29122-resourcemanagementofbdt
- description: API for AEF security management. An OpenAPI 3.0.0 document with 2 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.222 as part of the CAPIF (Common API Framework) suite and mirrore
  name: 3GPP TS 29.222 AEF Security API
  slug: 3gpp-ts29222-aef-security-api
- description: 'API for access control policy. An OpenAPI 3.0.0 document with 1 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.222 as part of the CAPIF (Common API Framework) suite and mirrored '
  name: 3GPP TS 29.222 CAPIF Access Control Policy API
  slug: 3gpp-ts29222-capif-access-control-policy-api
- description: API for API invoker management. An OpenAPI 3.0.0 document with 2 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.222 as part of the CAPIF (Common API Framework) suite and mirrored
  name: 3GPP TS 29.222 CAPIF API Invoker Management API
  slug: 3gpp-ts29222-capif-api-invoker-management-api
- description: 'API for API provider domain functions management. An OpenAPI 3.0.0 document with 2 path(s), API version 1.3.0, published verbatim by 3GPP in 3GPP TS 29.222 as part of the CAPIF (Common API Framework) '
  name: 3GPP TS 29.222 CAPIF API Provider Management API
  slug: 3gpp-ts29222-capif-api-provider-management-api
- description: CAPIF Auditing API. An OpenAPI 3.0.0 document with 1 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.222 as part of the CAPIF (Common API Framework) suite and mirrored in the publ
  name: 3GPP TS 29.222 CAPIF Auditing API
  slug: 3gpp-ts29222-capif-auditing-api
- description: API for discovering service APIs. An OpenAPI 3.0.0 document with 1 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.222 as part of the CAPIF (Common API Framework) suite and mirror
  name: 3GPP TS 29.222 CAPIF Discover Service API
  slug: 3gpp-ts29222-capif-discover-service-api
- description: API for event subscription management. An OpenAPI 3.0.0 document with 2 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.222 as part of the CAPIF (Common API Framework) suite and m
  name: 3GPP TS 29.222 CAPIF Events API
  slug: 3gpp-ts29222-capif-events-api
- description: CAPIF Logging API Invocation API. An OpenAPI 3.0.0 document with 2 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.222 as part of the CAPIF (Common API Framework) suite and mirror
  name: 3GPP TS 29.222 CAPIF Logging API Invocation API
  slug: 3gpp-ts29222-capif-logging-api-invocation-api
- description: 'API for open discovery of service APIs. An OpenAPI 3.0.0 document with 1 path(s), API version 1.0.0, published verbatim by 3GPP in 3GPP TS 29.222 as part of the CAPIF (Common API Framework) suite and '
  name: 3GPP TS 29.222 CAPIF Open Discover Service API
  slug: 3gpp-ts29222-capif-open-discover-service-api
- description: API for publishing service APIs. An OpenAPI 3.0.0 document with 2 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.222 as part of the CAPIF (Common API Framework) suite and mirrore
  name: 3GPP TS 29.222 CAPIF Publish Service API
  slug: 3gpp-ts29222-capif-publish-service-api
- description: API for Routing information. An OpenAPI 3.0.0 document with 1 path(s), API version 1.3.0, published verbatim by 3GPP in 3GPP TS 29.222 as part of the CAPIF (Common API Framework) suite and mirrored in
  name: 3GPP TS 29.222 CAPIF Routing Info API
  slug: 3gpp-ts29222-capif-routing-info-api
- description: API for CAPIF security management. An OpenAPI 3.0.0 document with 4 path(s), API version 1.4.0, published verbatim by 3GPP in 3GPP TS 29.222 as part of the CAPIF (Common API Framework) suite and mirro
  name: 3GPP TS 29.222 CAPIF Security API
  slug: 3gpp-ts29222-capif-security-api
- description: Session Management Policy Control Service. An OpenAPI 3.0.0 document with 4 path(s), API version 1.1.7, published verbatim by 3GPP in 3GPP TS 29.512 as part of the Policy Control (PCF) suite and mirro
  name: 3GPP TS 29.512 Npcf SM Policy Control API
  slug: 3gpp-ts29512-npcf-smpolicycontrol
- description: PCF Policy Authorization Service. An OpenAPI 3.0.0 document with 5 path(s), API version 1.1.5, published verbatim by 3GPP in 3GPP TS 29.514 as part of the Policy Authorization (PCF) suite and mirrored
  name: 3GPP TS 29.514 Npcf Policy Authorization API
  slug: 3gpp-ts29514-npcf-policyauthorization
- description: Nnwdaf_AnalyticsInfo Service API. An OpenAPI 3.0.0 document with 2 path(s), API version 1.2.1, published verbatim by 3GPP in 3GPP TS 29.520 as part of the Network Data Analytics (NWDAF) suite and mirr
  name: 3GPP TS 29.520 Nnwdaf Analytics Info API
  slug: 3gpp-ts29520-nnwdaf-analyticsinfo
- description: Nnwdaf_EventsSubscription Service API. An OpenAPI 3.0.0 document with 4 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.520 as part of the Network Data Analytics (NWDAF) suite and
  name: 3GPP TS 29.520 Nnwdaf Events Subscription API
  slug: 3gpp-ts29520-nnwdaf-eventssubscription
- description: 'API for 5G LAN Parameter Provision. An OpenAPI 3.0.0 document with 2 path(s), API version 1.3.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite '
  name: 3GPP TS 29.522 5 GLAN Parameter Provision API
  slug: 3gpp-ts29522-5glanparameterprovision
- description: 'API for 5G ACS Parameter Provision. An OpenAPI 3.0.0 document with 2 path(s), API version 1.1.2, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite '
  name: 3GPP TS 29.522 ACS Parameter Provision API
  slug: 3gpp-ts29522-acsparameterprovision
- description: API for Addressing Parameters Provisioning. An OpenAPI 3.0.0 document with 2 path(s), API version 1.0.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure
  name: 3GPP TS 29.522 Addressing Param Provision API
  slug: 3gpp-ts29522-addressingparamprovision
- description: API for UE Address service. An OpenAPI 3.0.0 document with 2 path(s), API version 1.0.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirr
  name: 3GPP TS 29.522 A Io T API
  slug: 3gpp-ts29522-aiot
- description: AKMA API. An OpenAPI 3.0.0 document with 1 path(s), API version 1.1.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirrored in the public
  name: 3GPP TS 29.522 AKMA API
  slug: 3gpp-ts29522-akma
- description: AM Influence API. An OpenAPI 3.0.0 document with 2 path(s), API version 1.2.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirrored in th
  name: 3GPP TS 29.522 AM Influence API
  slug: 3gpp-ts29522-aminfluence
- description: API for AM policy authorization. An OpenAPI 3.0.0 document with 3 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and
  name: 3GPP TS 29.522 AM Policy Authorization API
  slug: 3gpp-ts29522-ampolicyauthorization
- description: API for Analytics Exposure. An OpenAPI 3.0.0 document with 3 path(s), API version 1.3.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirr
  name: 3GPP TS 29.522 Analytics Exposure API
  slug: 3gpp-ts29522-analyticsexposure
- description: API for applying BDT policy. An OpenAPI 3.0.0 document with 2 path(s), API version 1.1.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mir
  name: 3GPP TS 29.522 Applying Bdt Policy API
  slug: 3gpp-ts29522-applyingbdtpolicy
- description: ASTI API. An OpenAPI 3.0.0 document with 3 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirrored in the public
  name: 3GPP TS 29.522 ASTI API
  slug: 3gpp-ts29522-asti
- description: API for CAG Information Parameters Provisioning. An OpenAPI 3.0.0 document with 2 path(s), API version 1.0.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exp
  name: 3GPP TS 29.522 Cag Info Param Provision API
  slug: 3gpp-ts29522-caginfoparamprovision
- description: API for 3GPP Data Reporting. An OpenAPI 3.0.0 document with 3 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mir
  name: 3GPP TS 29.522 Data Reporting API
  slug: 3gpp-ts29522-datareporting
- description: API for 3GPP Data Reporting and Provisioning. An OpenAPI 3.0.0 document with 4 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposu
  name: 3GPP TS 29.522 Data Reporting Provisioning API
  slug: 3gpp-ts29522-datareportingprovisioning
- description: DNAI Mapping API. An OpenAPI 3.0.0 document with 2 path(s), API version 1.0.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirrored in th
  name: 3GPP TS 29.522 DNAI Mapping API
  slug: 3gpp-ts29522-dnaimapping
- description: API for AF provisioned EAS Deployment. An OpenAPI 3.0.0 document with 3 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) sui
  name: 3GPP TS 29.522 EAS Deployment API
  slug: 3gpp-ts29522-easdeployment
- description: API for AF provisioned ECS Address Configuration Information. An OpenAPI 3.0.0 document with 3 path(s), API version 1.1.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound
  name: 3GPP TS 29.522 ECS Address API
  slug: 3gpp-ts29522-ecsaddress
- description: API for ECS Address Provisioning. An OpenAPI 3.0.0 document with 2 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite an
  name: 3GPP TS 29.522 Ecs Address Provision API
  slug: 3gpp-ts29522-ecsaddressprovision
- description: API for Group Parameters Provisioning. An OpenAPI 3.0.0 document with 2 path(s), API version 1.1.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) sui
  name: 3GPP TS 29.522 Group Parameters Provisioning API
  slug: 3gpp-ts29522-groupparametersprovisioning
- description: API for the IMS Event Exposure Service. An OpenAPI 3.0.0 document with 2 path(s), API version 1.0.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) su
  name: 3GPP TS 29.522 Ims Event Exposure API
  slug: 3gpp-ts29522-imseventexposure
- description: API for the IMS Parameters Provisioning Service. An OpenAPI 3.0.0 document with 2 path(s), API version 1.0.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exp
  name: 3GPP TS 29.522 Ims Param Provision API
  slug: 3gpp-ts29522-imsparamprovision
- description: API for the IMS Session Management Service. An OpenAPI 3.0.0 document with 2 path(s), API version 1.0.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure
  name: 3GPP TS 29.522 Ims Session Management API
  slug: 3gpp-ts29522-imssessionmanagement
- description: API for IPTV configuration. An OpenAPI 3.0.0 document with 2 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirr
  name: 3GPP TS 29.522 IPTV Configuration API
  slug: 3gpp-ts29522-iptvconfiguration
- description: 'API for Location Privacy Indication Parameters Provisioning. An OpenAPI 3.0.0 document with 2 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound '
  name: 3GPP TS 29.522 Lpi Parameter Provision API
  slug: 3gpp-ts29522-lpiparameterprovision
- description: 'API for MBS Group Message Delivery. An OpenAPI 3.0.0 document with 2 path(s), API version 1.1.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite '
  name: 3GPP TS 29.522 MBS Group Msg Delivery API
  slug: 3gpp-ts29522-mbsgroupmsgdelivery
- description: 'API for MBS Session Management. An OpenAPI 3.0.0 document with 6 path(s), API version 1.3.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and '
  name: 3GPP TS 29.522 MBS Session API
  slug: 3gpp-ts29522-mbssession
- description: 'API for the allocation, deallocation and management of TMGI(s) for MBS. An OpenAPI 3.0.0 document with 2 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF '
  name: 3GPP TS 29.522 MBSTMGI API
  slug: 3gpp-ts29522-mbstmgi
- description: API for MBS User Data Ingest Session. An OpenAPI 3.0.0 document with 4 path(s), API version 1.2.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suit
  name: 3GPP TS 29.522 MBS User Data Ingest Session API
  slug: 3gpp-ts29522-mbsuserdataingestsession
- description: MBS User Service API. An OpenAPI 3.0.0 document with 2 path(s), API version 1.1.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirrored i
  name: 3GPP TS 29.522 MBS User Service API
  slug: 3gpp-ts29522-mbsuserservice
- description: API for Member UE Selection Assistance. An OpenAPI 3.0.0 document with 2 path(s), API version 1.1.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) su
  name: 3GPP TS 29.522 Member UE Selection Assistance API
  slug: 3gpp-ts29522-memberueselectionassistance
- description: API for UE updated location information notification. An OpenAPI 3.0.0 document with 1 path(s), API version 1.3.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Networ
  name: 3GPP TS 29.522 Mo Lcs Notify API
  slug: 3gpp-ts29522-molcsnotify
- description: API for Media Streaming Event Exposure. An OpenAPI 3.0.0 document with 2 path(s), API version 1.2.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) su
  name: 3GPP TS 29.522 MS Event Exposure API
  slug: 3gpp-ts29522-mseventexposure
- description: 'API for NIDD Configuration Trigger. An OpenAPI 3.0.0 document with 1 path(s), API version 1.1.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite '
  name: 3GPP TS 29.522 NIDD Configuration Trigger API
  slug: 3gpp-ts29522-niddconfigurationtrigger
- description: API for PDTQ Policy Negotiation. An OpenAPI 3.0.0 document with 2 path(s), API version 1.1.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and
  name: 3GPP TS 29.522 PDTQ Policy Negotiation API
  slug: 3gpp-ts29522-pdtqpolicynegotiation
- description: API for RSLPPI Parameters Provisioning. An OpenAPI 3.0.0 document with 2 path(s), API version 1.0.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) su
  name: 3GPP TS 29.522 RSLPPI Parameters Provisioning API
  slug: 3gpp-ts29522-rslppiparametersprovisioning
- description: API for AF service paramter. An OpenAPI 3.0.0 document with 2 path(s), API version 1.3.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mir
  name: 3GPP TS 29.522 Service Parameter API
  slug: 3gpp-ts29522-serviceparameter
- description: API for Network Slice Parameters Provisioning. An OpenAPI 3.0.0 document with 2 path(s), API version 1.0.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Expos
  name: 3GPP TS 29.522 Slice Param Provision API
  slug: 3gpp-ts29522-sliceparamprovision
- description: API for time synchronization exposure. An OpenAPI 3.0.0 document with 4 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) sui
  name: 3GPP TS 29.522 Time Sync Exposure API
  slug: 3gpp-ts29522-timesyncexposure
- description: API for AF traffic influence. An OpenAPI 3.0.0 document with 2 path(s), API version 1.4.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mi
  name: 3GPP TS 29.522 Traffic Influence API
  slug: 3gpp-ts29522-trafficinfluence
- description: API for UAV Flight Assistance. An OpenAPI 3.0.0 document with 3 path(s), API version 1.0.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and m
  name: 3GPP TS 29.522 UAV Flight Assistance API
  slug: 3gpp-ts29522-uavflightassistance
- description: API for UE Address service. An OpenAPI 3.0.0 document with 3 path(s), API version 1.1.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirr
  name: 3GPP TS 29.522 UE Address API
  slug: 3gpp-ts29522-ueaddress
- description: UE Id API. An OpenAPI 3.0.0 document with 5 path(s), API version 1.2.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirrored in the publi
  name: 3GPP TS 29.522 UE Id API
  slug: 3gpp-ts29522-ueid
- description: VFL Inference API. An OpenAPI 3.0.0 document with 2 path(s), API version 1.0.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirrored in t
  name: 3GPP TS 29.522 VFL Inference API
  slug: 3gpp-ts29522-vflinference
- description: VFLNF Discovery API. An OpenAPI 3.0.0 document with 2 path(s), API version 1.0.0, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirrored in
  name: 3GPP TS 29.522 VFLNF Discovery API
  slug: 3gpp-ts29522-vflnfdiscovery
- description: VFL Training API. An OpenAPI 3.0.0 document with 2 path(s), API version 1.0.1, published verbatim by 3GPP in 3GPP TS 29.522 as part of the 5G NEF Northbound (Network Exposure) suite and mirrored in th
  name: 3GPP TS 29.522 VFL Training API
  slug: 3gpp-ts29522-vfltraining
- description: Common Data Types for Service Based Interfaces. An OpenAPI 3.0.0 data-model-only document (no paths; it defines the schemas/Network Resource Model consumed by the Provisioning and Performance manageme
  name: 3GPP TS 29.571 Common Data API
  slug: 3gpp-ts29571-commondata
- description: 'The 3GPP Forge (forge.3gpp.org) is a self-managed GitLab instance where 3GPP publishes the machine-readable OpenAPI for the 5G Service Based Architecture, the NEF/SCEF northbound exposure APIs, CAPIF '
  name: 3GPP Forge API
  slug: forge-gitlab-api
artifact_total: 124
asyncapis:
- description: ''
  name: 3Gpp Notifications Webhooks
  slug: 3gpp-notifications-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/3gpp-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/3gpp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3gpp-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/3gpp-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/3gpp-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.3gpp.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.3gpp.org/specifications-technologies
- group: docs
  title: ''
  type: SpecificationsArchive
  url: https://www.3gpp.org/ftp/Specs/archive/
- group: start
  title: ''
  type: Portal
  url: https://portal.3gpp.org/
- group: build
  title: ''
  type: SourceCode
  url: https://forge.3gpp.org/rep/all/5G_APIs
- group: build
  title: ''
  type: SourceCode
  url: https://forge.3gpp.org/rep/sa5/MnS
- group: build
  title: ''
  type: Tools
  url: https://forge.3gpp.org/swagger/tools/parser.html
- group: company
  title: ''
  type: Blog
  url: https://www.3gpp.org/news-events
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/3gpp
- group: build
  title: ''
  type: Packages
  url: packages/3gpp-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/3gpp-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/3gpp-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3gpp-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/3gpp-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/3gpp-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/3gpp-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.3gpp.org/specifications-technologies/specifications-by-series/ts-or-tr-proposed-for-withdrawal
- group: auth
  title: ''
  type: Security
  url: https://www.3gpp.org/delegates-corner/coordinated-vulnerability-disclosure
- group: design
  title: ''
  type: Conventions
  url: conventions/3gpp-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/3gpp-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/3gpp-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/3gpp-notifications-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://www.3gpp.org/specifications-technologies/3gpp-work-plan
- group: operate
  title: ''
  type: Support
  url: https://www.3gpp.org/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.3gpp.org/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.3gpp.org/about-us/legal-matters/3gpp-privacy-policy
- group: docs
  title: ''
  type: APIReference
  url: https://www.3gpp.org/specifications-technologies/specifications-by-series
- group: start
  title: ''
  type: GettingStarted
  url: https://forge.3gpp.org/rep/all/5G_APIs/-/blob/REL-20/README.md
created: '2026-07-25'
description: '3GPP (the 3rd Generation Partnership Project) is the global standards partnership that writes the technical specifications for mobile networks — GSM, UMTS, LTE, 5G and the ongoing 6G work — through seven regional Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA and TTC) and a membership of operators, vendors and chipset makers. It is not a service provider and sells nothing to developers; it sits at the very top of the telecom value chain, defining the network functions that every mobile operator on earth deploys and that every CPaaS aggregator ultimately resells. Its API posture is unusually open for a standards body: all 3GPP specifications are published free of charge with no membership or login, and since Release 15 the RESTful Service-Based Architecture, the SCEF/NEF northbound exposure APIs and the SA5 management services have been published as machine-readable OpenAPI 3.0 YAML in a public GitLab instance at forge.3gpp.org. What 3GPP does not run is a developer
  programme — there is no portal, no key, no sandbox and no callable endpoint; the specifications describe interfaces that operators instantiate, and the developer-facing abstraction over them is CAMARA and GSMA Open Gateway, not 3GPP itself.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: 3gpp-mcp.yml
  slug: 3gpp-mcpyml
modified: '2026-07-25'
name: 3GPP
nav: Providers
network: true
overview: '3GPP publishes 116 APIs on the [APIs.io](https://apis.io/) network, including TS 28.104 Mda Nrm API, TS 28.104 Mda Report API, TS 28.105 Ai Ml Nrm API, and 113 more. Tagged areas include Telecommunications, Global, Standards, Standards Body, and Network APIs.


  The 3GPP catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  3GPP''s developer surface includes authentication, documentation, developer portal, tooling, engineering blog, changelog, support, and 28 more developer resources.'
random_paper: 50
scopes:
- name: 3Gpp Scopes
  scope_count: 6
  slug: 3gpp-scopes
  summary_line: 6 scopes · clientCredentials
score:
  band: developing
  composite: 47.8
  delta: 3.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 48.9
    developer_ergonomics: 56.0
    discoverability: 77.8
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 116
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 75.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: 3Gpp Authentication
  slug: 3gpp-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: 3Gpp Domain Security
  slug: 3gpp-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: 3Gpp Vulnerability Disclosure
  slug: 3gpp-vulnerability-disclosure
  summary_line: disclosure policy published
slug: 3gpp
tags:
- Telecommunications
- Global
- Standards
- Standards Body
- Network APIs
- 5G
- Network Exposure
- NEF
- SCEF
- CAPIF
- Service Based Architecture
- OpenAPI
- OSS
- Network Functions
- 6G
website: https://www.3gpp.org/
---
