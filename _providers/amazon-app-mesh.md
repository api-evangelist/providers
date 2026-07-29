---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Amazon App Mesh Agentic Access
  operation_count: 76
  slug: amazon-app-mesh-agentic-access
  summary_line: 76 operations · 46 acting
api_count: 4
apis:
- description: The Meshes API from Amazon App Mesh — 14 operation(s) for meshes.
  name: Amazon App Mesh Meshes API
  slug: amazon-app-mesh-meshes-api
- description: The Tag#resourceArn API from Amazon App Mesh — 1 operation(s) for tag#resourcearn.
  name: Amazon App Mesh Tag#resourceArn API
  slug: amazon-app-mesh-tag-resourcearn-api
- description: The Tags#resourceArn API from Amazon App Mesh — 1 operation(s) for tags#resourcearn.
  name: Amazon App Mesh Tags#resourceArn API
  slug: amazon-app-mesh-tags-resourcearn-api
- description: The Untag#resourceArn API from Amazon App Mesh — 1 operation(s) for untag#resourcearn.
  name: Amazon App Mesh Untag#resourceArn API
  slug: amazon-app-mesh-untag-resourcearn-api
artifact_total: 993
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-app-mesh-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-app-mesh-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-app-mesh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-app-mesh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-app-mesh-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/app-mesh/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/app-mesh/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/appmesh/
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: Status
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-app-mesh-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-app-mesh-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-app-mesh-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-app-mesh-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-app-mesh-security.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-app-mesh-lifecycle.yml
created: '2024-01-15'
description: AWS App Mesh is a service mesh that provides application-level networking to make it easy for your services to communicate with each other across multiple types of compute infrastructure.
examples:
- key_count: 1
  name: Amazon App Mesh Accesslog Example
  slug: amazon-app-mesh-accesslog-example
- key_count: 0
  name: Amazon App Mesh Accountid Example
  slug: amazon-app-mesh-accountid-example
- key_count: 0
  name: Amazon App Mesh Arn Example
  slug: amazon-app-mesh-arn-example
- key_count: 2
  name: Amazon App Mesh Awscloudmapinstanceattribute Example
  slug: amazon-app-mesh-awscloudmapinstanceattribute-example
- key_count: 0
  name: Amazon App Mesh Awscloudmapinstanceattributekey Example
  slug: amazon-app-mesh-awscloudmapinstanceattributekey-example
- key_count: 0
  name: Amazon App Mesh Awscloudmapinstanceattributes Example
  slug: amazon-app-mesh-awscloudmapinstanceattributes-example
- key_count: 0
  name: Amazon App Mesh Awscloudmapinstanceattributevalue Example
  slug: amazon-app-mesh-awscloudmapinstanceattributevalue-example
- key_count: 0
  name: Amazon App Mesh Awscloudmapname Example
  slug: amazon-app-mesh-awscloudmapname-example
- key_count: 4
  name: Amazon App Mesh Awscloudmapservicediscovery Example
  slug: amazon-app-mesh-awscloudmapservicediscovery-example
- key_count: 1
  name: Amazon App Mesh Backend Example
  slug: amazon-app-mesh-backend-example
- key_count: 1
  name: Amazon App Mesh Backenddefaults Example
  slug: amazon-app-mesh-backenddefaults-example
- key_count: 0
  name: Amazon App Mesh Backends Example
  slug: amazon-app-mesh-backends-example
- key_count: 0
  name: Amazon App Mesh Boolean Example
  slug: amazon-app-mesh-boolean-example
- key_count: 0
  name: Amazon App Mesh Certificateauthorityarns Example
  slug: amazon-app-mesh-certificateauthorityarns-example
- key_count: 1
  name: Amazon App Mesh Clientpolicy Example
  slug: amazon-app-mesh-clientpolicy-example
- key_count: 4
  name: Amazon App Mesh Clientpolicytls Example
  slug: amazon-app-mesh-clientpolicytls-example
- key_count: 2
  name: Amazon App Mesh Clienttlscertificate Example
  slug: amazon-app-mesh-clienttlscertificate-example
- key_count: 4
  name: Amazon App Mesh Creategatewayrouteinput Example
  slug: amazon-app-mesh-creategatewayrouteinput-example
- key_count: 1
  name: Amazon App Mesh Creategatewayrouteoutput Example
  slug: amazon-app-mesh-creategatewayrouteoutput-example
- key_count: 4
  name: Amazon App Mesh Createmeshinput Example
  slug: amazon-app-mesh-createmeshinput-example
- key_count: 1
  name: Amazon App Mesh Createmeshoutput Example
  slug: amazon-app-mesh-createmeshoutput-example
- key_count: 4
  name: Amazon App Mesh Createrouteinput Example
  slug: amazon-app-mesh-createrouteinput-example
- key_count: 1
  name: Amazon App Mesh Createrouteoutput Example
  slug: amazon-app-mesh-createrouteoutput-example
- key_count: 4
  name: Amazon App Mesh Createvirtualgatewayinput Example
  slug: amazon-app-mesh-createvirtualgatewayinput-example
- key_count: 1
  name: Amazon App Mesh Createvirtualgatewayoutput Example
  slug: amazon-app-mesh-createvirtualgatewayoutput-example
- key_count: 4
  name: Amazon App Mesh Createvirtualnodeinput Example
  slug: amazon-app-mesh-createvirtualnodeinput-example
- key_count: 1
  name: Amazon App Mesh Createvirtualnodeoutput Example
  slug: amazon-app-mesh-createvirtualnodeoutput-example
- key_count: 4
  name: Amazon App Mesh Createvirtualrouterinput Example
  slug: amazon-app-mesh-createvirtualrouterinput-example
- key_count: 1
  name: Amazon App Mesh Createvirtualrouteroutput Example
  slug: amazon-app-mesh-createvirtualrouteroutput-example
- key_count: 4
  name: Amazon App Mesh Createvirtualserviceinput Example
  slug: amazon-app-mesh-createvirtualserviceinput-example
- key_count: 1
  name: Amazon App Mesh Createvirtualserviceoutput Example
  slug: amazon-app-mesh-createvirtualserviceoutput-example
- key_count: 0
  name: Amazon App Mesh Defaultgatewayrouterewrite Example
  slug: amazon-app-mesh-defaultgatewayrouterewrite-example
- key_count: 0
  name: Amazon App Mesh Deletegatewayrouteinput Example
  slug: amazon-app-mesh-deletegatewayrouteinput-example
- key_count: 1
  name: Amazon App Mesh Deletegatewayrouteoutput Example
  slug: amazon-app-mesh-deletegatewayrouteoutput-example
- key_count: 0
  name: Amazon App Mesh Deletemeshinput Example
  slug: amazon-app-mesh-deletemeshinput-example
- key_count: 1
  name: Amazon App Mesh Deletemeshoutput Example
  slug: amazon-app-mesh-deletemeshoutput-example
- key_count: 0
  name: Amazon App Mesh Deleterouteinput Example
  slug: amazon-app-mesh-deleterouteinput-example
- key_count: 1
  name: Amazon App Mesh Deleterouteoutput Example
  slug: amazon-app-mesh-deleterouteoutput-example
- key_count: 0
  name: Amazon App Mesh Deletevirtualgatewayinput Example
  slug: amazon-app-mesh-deletevirtualgatewayinput-example
- key_count: 1
  name: Amazon App Mesh Deletevirtualgatewayoutput Example
  slug: amazon-app-mesh-deletevirtualgatewayoutput-example
- key_count: 0
  name: Amazon App Mesh Deletevirtualnodeinput Example
  slug: amazon-app-mesh-deletevirtualnodeinput-example
- key_count: 1
  name: Amazon App Mesh Deletevirtualnodeoutput Example
  slug: amazon-app-mesh-deletevirtualnodeoutput-example
- key_count: 0
  name: Amazon App Mesh Deletevirtualrouterinput Example
  slug: amazon-app-mesh-deletevirtualrouterinput-example
- key_count: 1
  name: Amazon App Mesh Deletevirtualrouteroutput Example
  slug: amazon-app-mesh-deletevirtualrouteroutput-example
- key_count: 0
  name: Amazon App Mesh Deletevirtualserviceinput Example
  slug: amazon-app-mesh-deletevirtualserviceinput-example
- key_count: 1
  name: Amazon App Mesh Deletevirtualserviceoutput Example
  slug: amazon-app-mesh-deletevirtualserviceoutput-example
- key_count: 0
  name: Amazon App Mesh Describegatewayrouteinput Example
  slug: amazon-app-mesh-describegatewayrouteinput-example
- key_count: 1
  name: Amazon App Mesh Describegatewayrouteoutput Example
  slug: amazon-app-mesh-describegatewayrouteoutput-example
- key_count: 0
  name: Amazon App Mesh Describemeshinput Example
  slug: amazon-app-mesh-describemeshinput-example
- key_count: 1
  name: Amazon App Mesh Describemeshoutput Example
  slug: amazon-app-mesh-describemeshoutput-example
- key_count: 0
  name: Amazon App Mesh Describerouteinput Example
  slug: amazon-app-mesh-describerouteinput-example
- key_count: 1
  name: Amazon App Mesh Describerouteoutput Example
  slug: amazon-app-mesh-describerouteoutput-example
- key_count: 0
  name: Amazon App Mesh Describevirtualgatewayinput Example
  slug: amazon-app-mesh-describevirtualgatewayinput-example
- key_count: 1
  name: Amazon App Mesh Describevirtualgatewayoutput Example
  slug: amazon-app-mesh-describevirtualgatewayoutput-example
- key_count: 0
  name: Amazon App Mesh Describevirtualnodeinput Example
  slug: amazon-app-mesh-describevirtualnodeinput-example
- key_count: 1
  name: Amazon App Mesh Describevirtualnodeoutput Example
  slug: amazon-app-mesh-describevirtualnodeoutput-example
- key_count: 0
  name: Amazon App Mesh Describevirtualrouterinput Example
  slug: amazon-app-mesh-describevirtualrouterinput-example
- key_count: 1
  name: Amazon App Mesh Describevirtualrouteroutput Example
  slug: amazon-app-mesh-describevirtualrouteroutput-example
- key_count: 0
  name: Amazon App Mesh Describevirtualserviceinput Example
  slug: amazon-app-mesh-describevirtualserviceinput-example
- key_count: 1
  name: Amazon App Mesh Describevirtualserviceoutput Example
  slug: amazon-app-mesh-describevirtualserviceoutput-example
- key_count: 0
  name: Amazon App Mesh Dnsresponsetype Example
  slug: amazon-app-mesh-dnsresponsetype-example
- key_count: 3
  name: Amazon App Mesh Dnsservicediscovery Example
  slug: amazon-app-mesh-dnsservicediscovery-example
- key_count: 2
  name: Amazon App Mesh Duration Example
  slug: amazon-app-mesh-duration-example
- key_count: 0
  name: Amazon App Mesh Durationunit Example
  slug: amazon-app-mesh-durationunit-example
- key_count: 0
  name: Amazon App Mesh Durationvalue Example
  slug: amazon-app-mesh-durationvalue-example
- key_count: 1
  name: Amazon App Mesh Egressfilter Example
  slug: amazon-app-mesh-egressfilter-example
- key_count: 0
  name: Amazon App Mesh Egressfiltertype Example
  slug: amazon-app-mesh-egressfiltertype-example
- key_count: 0
  name: Amazon App Mesh Exacthostname Example
  slug: amazon-app-mesh-exacthostname-example
- key_count: 2
  name: Amazon App Mesh Fileaccesslog Example
  slug: amazon-app-mesh-fileaccesslog-example
- key_count: 0
  name: Amazon App Mesh Filepath Example
  slug: amazon-app-mesh-filepath-example
- key_count: 6
  name: Amazon App Mesh Gatewayroutedata Example
  slug: amazon-app-mesh-gatewayroutedata-example
- key_count: 2
  name: Amazon App Mesh Gatewayroutehostnamematch Example
  slug: amazon-app-mesh-gatewayroutehostnamematch-example
- key_count: 1
  name: Amazon App Mesh Gatewayroutehostnamerewrite Example
  slug: amazon-app-mesh-gatewayroutehostnamerewrite-example
- key_count: 0
  name: Amazon App Mesh Gatewayroutelist Example
  slug: amazon-app-mesh-gatewayroutelist-example
- key_count: 0
  name: Amazon App Mesh Gatewayroutepriority Example
  slug: amazon-app-mesh-gatewayroutepriority-example
- key_count: 9
  name: Amazon App Mesh Gatewayrouteref Example
  slug: amazon-app-mesh-gatewayrouteref-example
- key_count: 4
  name: Amazon App Mesh Gatewayroutespec Example
  slug: amazon-app-mesh-gatewayroutespec-example
- key_count: 1
  name: Amazon App Mesh Gatewayroutestatus Example
  slug: amazon-app-mesh-gatewayroutestatus-example
- key_count: 0
  name: Amazon App Mesh Gatewayroutestatuscode Example
  slug: amazon-app-mesh-gatewayroutestatuscode-example
- key_count: 2
  name: Amazon App Mesh Gatewayroutetarget Example
  slug: amazon-app-mesh-gatewayroutetarget-example
- key_count: 1
  name: Amazon App Mesh Gatewayroutevirtualservice Example
  slug: amazon-app-mesh-gatewayroutevirtualservice-example
- key_count: 2
  name: Amazon App Mesh Grpcgatewayroute Example
  slug: amazon-app-mesh-grpcgatewayroute-example
- key_count: 2
  name: Amazon App Mesh Grpcgatewayrouteaction Example
  slug: amazon-app-mesh-grpcgatewayrouteaction-example
- key_count: 4
  name: Amazon App Mesh Grpcgatewayroutematch Example
  slug: amazon-app-mesh-grpcgatewayroutematch-example
- key_count: 3
  name: Amazon App Mesh Grpcgatewayroutemetadata Example
  slug: amazon-app-mesh-grpcgatewayroutemetadata-example
- key_count: 0
  name: Amazon App Mesh Grpcgatewayroutemetadatalist Example
  slug: amazon-app-mesh-grpcgatewayroutemetadatalist-example
- key_count: 1
  name: Amazon App Mesh Grpcgatewayrouterewrite Example
  slug: amazon-app-mesh-grpcgatewayrouterewrite-example
- key_count: 5
  name: Amazon App Mesh Grpcmetadatamatchmethod Example
  slug: amazon-app-mesh-grpcmetadatamatchmethod-example
- key_count: 5
  name: Amazon App Mesh Grpcretrypolicy Example
  slug: amazon-app-mesh-grpcretrypolicy-example
- key_count: 0
  name: Amazon App Mesh Grpcretrypolicyevent Example
  slug: amazon-app-mesh-grpcretrypolicyevent-example
- key_count: 0
  name: Amazon App Mesh Grpcretrypolicyevents Example
  slug: amazon-app-mesh-grpcretrypolicyevents-example
- key_count: 4
  name: Amazon App Mesh Grpcroute Example
  slug: amazon-app-mesh-grpcroute-example
- key_count: 1
  name: Amazon App Mesh Grpcrouteaction Example
  slug: amazon-app-mesh-grpcrouteaction-example
- key_count: 4
  name: Amazon App Mesh Grpcroutematch Example
  slug: amazon-app-mesh-grpcroutematch-example
- key_count: 3
  name: Amazon App Mesh Grpcroutemetadata Example
  slug: amazon-app-mesh-grpcroutemetadata-example
- key_count: 0
  name: Amazon App Mesh Grpcroutemetadatalist Example
  slug: amazon-app-mesh-grpcroutemetadatalist-example
- key_count: 5
  name: Amazon App Mesh Grpcroutemetadatamatchmethod Example
  slug: amazon-app-mesh-grpcroutemetadatamatchmethod-example
- key_count: 2
  name: Amazon App Mesh Grpctimeout Example
  slug: amazon-app-mesh-grpctimeout-example
- key_count: 0
  name: Amazon App Mesh Headermatch Example
  slug: amazon-app-mesh-headermatch-example
- key_count: 5
  name: Amazon App Mesh Headermatchmethod Example
  slug: amazon-app-mesh-headermatchmethod-example
- key_count: 0
  name: Amazon App Mesh Headername Example
  slug: amazon-app-mesh-headername-example
- key_count: 0
  name: Amazon App Mesh Healthcheckintervalmillis Example
  slug: amazon-app-mesh-healthcheckintervalmillis-example
- key_count: 7
  name: Amazon App Mesh Healthcheckpolicy Example
  slug: amazon-app-mesh-healthcheckpolicy-example
- key_count: 0
  name: Amazon App Mesh Healthcheckthreshold Example
  slug: amazon-app-mesh-healthcheckthreshold-example
- key_count: 0
  name: Amazon App Mesh Healthchecktimeoutmillis Example
  slug: amazon-app-mesh-healthchecktimeoutmillis-example
- key_count: 0
  name: Amazon App Mesh Hostname Example
  slug: amazon-app-mesh-hostname-example
- key_count: 2
  name: Amazon App Mesh Httpgatewayroute Example
  slug: amazon-app-mesh-httpgatewayroute-example
- key_count: 2
  name: Amazon App Mesh Httpgatewayrouteaction Example
  slug: amazon-app-mesh-httpgatewayrouteaction-example
- key_count: 3
  name: Amazon App Mesh Httpgatewayrouteheader Example
  slug: amazon-app-mesh-httpgatewayrouteheader-example
- key_count: 0
  name: Amazon App Mesh Httpgatewayrouteheaders Example
  slug: amazon-app-mesh-httpgatewayrouteheaders-example
- key_count: 7
  name: Amazon App Mesh Httpgatewayroutematch Example
  slug: amazon-app-mesh-httpgatewayroutematch-example
- key_count: 1
  name: Amazon App Mesh Httpgatewayroutepathrewrite Example
  slug: amazon-app-mesh-httpgatewayroutepathrewrite-example
- key_count: 0
  name: Amazon App Mesh Httpgatewayrouteprefix Example
  slug: amazon-app-mesh-httpgatewayrouteprefix-example
- key_count: 2
  name: Amazon App Mesh Httpgatewayrouteprefixrewrite Example
  slug: amazon-app-mesh-httpgatewayrouteprefixrewrite-example
- key_count: 3
  name: Amazon App Mesh Httpgatewayrouterewrite Example
  slug: amazon-app-mesh-httpgatewayrouterewrite-example
- key_count: 0
  name: Amazon App Mesh Httpmethod Example
  slug: amazon-app-mesh-httpmethod-example
- key_count: 0
  name: Amazon App Mesh Httppathexact Example
  slug: amazon-app-mesh-httppathexact-example
- key_count: 2
  name: Amazon App Mesh Httppathmatch Example
  slug: amazon-app-mesh-httppathmatch-example
- key_count: 0
  name: Amazon App Mesh Httppathregex Example
  slug: amazon-app-mesh-httppathregex-example
- key_count: 2
  name: Amazon App Mesh Httpqueryparameter Example
  slug: amazon-app-mesh-httpqueryparameter-example
- key_count: 0
  name: Amazon App Mesh Httpqueryparameters Example
  slug: amazon-app-mesh-httpqueryparameters-example
- key_count: 4
  name: Amazon App Mesh Httpretrypolicy Example
  slug: amazon-app-mesh-httpretrypolicy-example
- key_count: 0
  name: Amazon App Mesh Httpretrypolicyevent Example
  slug: amazon-app-mesh-httpretrypolicyevent-example
- key_count: 0
  name: Amazon App Mesh Httpretrypolicyevents Example
  slug: amazon-app-mesh-httpretrypolicyevents-example
- key_count: 4
  name: Amazon App Mesh Httproute Example
  slug: amazon-app-mesh-httproute-example
- key_count: 1
  name: Amazon App Mesh Httprouteaction Example
  slug: amazon-app-mesh-httprouteaction-example
- key_count: 3
  name: Amazon App Mesh Httprouteheader Example
  slug: amazon-app-mesh-httprouteheader-example
- key_count: 0
  name: Amazon App Mesh Httprouteheaders Example
  slug: amazon-app-mesh-httprouteheaders-example
- key_count: 7
  name: Amazon App Mesh Httproutematch Example
  slug: amazon-app-mesh-httproutematch-example
- key_count: 0
  name: Amazon App Mesh Httpscheme Example
  slug: amazon-app-mesh-httpscheme-example
- key_count: 2
  name: Amazon App Mesh Httptimeout Example
  slug: amazon-app-mesh-httptimeout-example
- key_count: 0
  name: Amazon App Mesh Ippreference Example
  slug: amazon-app-mesh-ippreference-example
- key_count: 0
  name: Amazon App Mesh Jsonformat Example
  slug: amazon-app-mesh-jsonformat-example
- key_count: 2
  name: Amazon App Mesh Jsonformatref Example
  slug: amazon-app-mesh-jsonformatref-example
- key_count: 0
  name: Amazon App Mesh Jsonkey Example
  slug: amazon-app-mesh-jsonkey-example
- key_count: 0
  name: Amazon App Mesh Jsonvalue Example
  slug: amazon-app-mesh-jsonvalue-example
- key_count: 6
  name: Amazon App Mesh Listener Example
  slug: amazon-app-mesh-listener-example
- key_count: 0
  name: Amazon App Mesh Listenerport Example
  slug: amazon-app-mesh-listenerport-example
- key_count: 0
  name: Amazon App Mesh Listeners Example
  slug: amazon-app-mesh-listeners-example
- key_count: 4
  name: Amazon App Mesh Listenertimeout Example
  slug: amazon-app-mesh-listenertimeout-example
- key_count: 3
  name: Amazon App Mesh Listenertls Example
  slug: amazon-app-mesh-listenertls-example
- key_count: 1
  name: Amazon App Mesh Listenertlsacmcertificate Example
  slug: amazon-app-mesh-listenertlsacmcertificate-example
- key_count: 3
  name: Amazon App Mesh Listenertlscertificate Example
  slug: amazon-app-mesh-listenertlscertificate-example
- key_count: 2
  name: Amazon App Mesh Listenertlsfilecertificate Example
  slug: amazon-app-mesh-listenertlsfilecertificate-example
- key_count: 0
  name: Amazon App Mesh Listenertlsmode Example
  slug: amazon-app-mesh-listenertlsmode-example
- key_count: 1
  name: Amazon App Mesh Listenertlssdscertificate Example
  slug: amazon-app-mesh-listenertlssdscertificate-example
- key_count: 2
  name: Amazon App Mesh Listenertlsvalidationcontext Example
  slug: amazon-app-mesh-listenertlsvalidationcontext-example
- key_count: 2
  name: Amazon App Mesh Listenertlsvalidationcontexttrust Example
  slug: amazon-app-mesh-listenertlsvalidationcontexttrust-example
- key_count: 0
  name: Amazon App Mesh Listgatewayroutesinput Example
  slug: amazon-app-mesh-listgatewayroutesinput-example
- key_count: 0
  name: Amazon App Mesh Listgatewayrouteslimit Example
  slug: amazon-app-mesh-listgatewayrouteslimit-example
- key_count: 2
  name: Amazon App Mesh Listgatewayroutesoutput Example
  slug: amazon-app-mesh-listgatewayroutesoutput-example
- key_count: 0
  name: Amazon App Mesh Listmeshesinput Example
  slug: amazon-app-mesh-listmeshesinput-example
- key_count: 0
  name: Amazon App Mesh Listmesheslimit Example
  slug: amazon-app-mesh-listmesheslimit-example
- key_count: 2
  name: Amazon App Mesh Listmeshesoutput Example
  slug: amazon-app-mesh-listmeshesoutput-example
- key_count: 0
  name: Amazon App Mesh Listroutesinput Example
  slug: amazon-app-mesh-listroutesinput-example
- key_count: 0
  name: Amazon App Mesh Listrouteslimit Example
  slug: amazon-app-mesh-listrouteslimit-example
- key_count: 2
  name: Amazon App Mesh Listroutesoutput Example
  slug: amazon-app-mesh-listroutesoutput-example
- key_count: 0
  name: Amazon App Mesh Listtagsforresourceinput Example
  slug: amazon-app-mesh-listtagsforresourceinput-example
- key_count: 2
  name: Amazon App Mesh Listtagsforresourceoutput Example
  slug: amazon-app-mesh-listtagsforresourceoutput-example
- key_count: 0
  name: Amazon App Mesh Listvirtualgatewaysinput Example
  slug: amazon-app-mesh-listvirtualgatewaysinput-example
- key_count: 0
  name: Amazon App Mesh Listvirtualgatewayslimit Example
  slug: amazon-app-mesh-listvirtualgatewayslimit-example
- key_count: 2
  name: Amazon App Mesh Listvirtualgatewaysoutput Example
  slug: amazon-app-mesh-listvirtualgatewaysoutput-example
- key_count: 0
  name: Amazon App Mesh Listvirtualnodesinput Example
  slug: amazon-app-mesh-listvirtualnodesinput-example
- key_count: 0
  name: Amazon App Mesh Listvirtualnodeslimit Example
  slug: amazon-app-mesh-listvirtualnodeslimit-example
- key_count: 2
  name: Amazon App Mesh Listvirtualnodesoutput Example
  slug: amazon-app-mesh-listvirtualnodesoutput-example
- key_count: 0
  name: Amazon App Mesh Listvirtualroutersinput Example
  slug: amazon-app-mesh-listvirtualroutersinput-example
- key_count: 0
  name: Amazon App Mesh Listvirtualrouterslimit Example
  slug: amazon-app-mesh-listvirtualrouterslimit-example
- key_count: 2
  name: Amazon App Mesh Listvirtualroutersoutput Example
  slug: amazon-app-mesh-listvirtualroutersoutput-example
- key_count: 0
  name: Amazon App Mesh Listvirtualservicesinput Example
  slug: amazon-app-mesh-listvirtualservicesinput-example
- key_count: 0
  name: Amazon App Mesh Listvirtualserviceslimit Example
  slug: amazon-app-mesh-listvirtualserviceslimit-example
- key_count: 2
  name: Amazon App Mesh Listvirtualservicesoutput Example
  slug: amazon-app-mesh-listvirtualservicesoutput-example
- key_count: 1
  name: Amazon App Mesh Logging Example
  slug: amazon-app-mesh-logging-example
- key_count: 2
  name: Amazon App Mesh Loggingformat Example
  slug: amazon-app-mesh-loggingformat-example
- key_count: 0
  name: Amazon App Mesh Long Example
  slug: amazon-app-mesh-long-example
- key_count: 2
  name: Amazon App Mesh Matchrange Example
  slug: amazon-app-mesh-matchrange-example
- key_count: 0
  name: Amazon App Mesh Maxconnections Example
  slug: amazon-app-mesh-maxconnections-example
- key_count: 0
  name: Amazon App Mesh Maxpendingrequests Example
  slug: amazon-app-mesh-maxpendingrequests-example
- key_count: 0
  name: Amazon App Mesh Maxrequests Example
  slug: amazon-app-mesh-maxrequests-example
- key_count: 0
  name: Amazon App Mesh Maxretries Example
  slug: amazon-app-mesh-maxretries-example
- key_count: 4
  name: Amazon App Mesh Meshdata Example
  slug: amazon-app-mesh-meshdata-example
- key_count: 0
  name: Amazon App Mesh Meshlist Example
  slug: amazon-app-mesh-meshlist-example
- key_count: 7
  name: Amazon App Mesh Meshref Example
  slug: amazon-app-mesh-meshref-example
- key_count: 1
  name: Amazon App Mesh Meshservicediscovery Example
  slug: amazon-app-mesh-meshservicediscovery-example
- key_count: 2
  name: Amazon App Mesh Meshspec Example
  slug: amazon-app-mesh-meshspec-example
- key_count: 1
  name: Amazon App Mesh Meshstatus Example
  slug: amazon-app-mesh-meshstatus-example
- key_count: 0
  name: Amazon App Mesh Meshstatuscode Example
  slug: amazon-app-mesh-meshstatuscode-example
- key_count: 0
  name: Amazon App Mesh Methodname Example
  slug: amazon-app-mesh-methodname-example
- key_count: 4
  name: Amazon App Mesh Outlierdetection Example
  slug: amazon-app-mesh-outlierdetection-example
- key_count: 0
  name: Amazon App Mesh Outlierdetectionmaxejectionpercent Example
  slug: amazon-app-mesh-outlierdetectionmaxejectionpercent-example
- key_count: 0
  name: Amazon App Mesh Outlierdetectionmaxservererrors Example
  slug: amazon-app-mesh-outlierdetectionmaxservererrors-example
- key_count: 0
  name: Amazon App Mesh Percentint Example
  slug: amazon-app-mesh-percentint-example
- key_count: 2
  name: Amazon App Mesh Portmapping Example
  slug: amazon-app-mesh-portmapping-example
- key_count: 0
  name: Amazon App Mesh Portnumber Example
  slug: amazon-app-mesh-portnumber-example
- key_count: 0
  name: Amazon App Mesh Portprotocol Example
  slug: amazon-app-mesh-portprotocol-example
- key_count: 0
  name: Amazon App Mesh Portset Example
  slug: amazon-app-mesh-portset-example
- key_count: 1
  name: Amazon App Mesh Queryparametermatch Example
  slug: amazon-app-mesh-queryparametermatch-example
- key_count: 0
  name: Amazon App Mesh Queryparametername Example
  slug: amazon-app-mesh-queryparametername-example
- key_count: 7
  name: Amazon App Mesh Resourcemetadata Example
  slug: amazon-app-mesh-resourcemetadata-example
- key_count: 0
  name: Amazon App Mesh Resourcename Example
  slug: amazon-app-mesh-resourcename-example
- key_count: 6
  name: Amazon App Mesh Routedata Example
  slug: amazon-app-mesh-routedata-example
- key_count: 0
  name: Amazon App Mesh Routelist Example
  slug: amazon-app-mesh-routelist-example
- key_count: 0
  name: Amazon App Mesh Routepriority Example
  slug: amazon-app-mesh-routepriority-example
- key_count: 9
  name: Amazon App Mesh Routeref Example
  slug: amazon-app-mesh-routeref-example
- key_count: 5
  name: Amazon App Mesh Routespec Example
  slug: amazon-app-mesh-routespec-example
- key_count: 1
  name: Amazon App Mesh Routestatus Example
  slug: amazon-app-mesh-routestatus-example
- key_count: 0
  name: Amazon App Mesh Routestatuscode Example
  slug: amazon-app-mesh-routestatuscode-example
- key_count: 0
  name: Amazon App Mesh Sdssecretname Example
  slug: amazon-app-mesh-sdssecretname-example
- key_count: 2
  name: Amazon App Mesh Servicediscovery Example
  slug: amazon-app-mesh-servicediscovery-example
- key_count: 0
  name: Amazon App Mesh Servicename Example
  slug: amazon-app-mesh-servicename-example
- key_count: 0
  name: Amazon App Mesh String Example
  slug: amazon-app-mesh-string-example
- key_count: 0
  name: Amazon App Mesh Subjectalternativename Example
  slug: amazon-app-mesh-subjectalternativename-example
- key_count: 0
  name: Amazon App Mesh Subjectalternativenamelist Example
  slug: amazon-app-mesh-subjectalternativenamelist-example
- key_count: 1
  name: Amazon App Mesh Subjectalternativenamematchers Example
  slug: amazon-app-mesh-subjectalternativenamematchers-example
- key_count: 1
  name: Amazon App Mesh Subjectalternativenames Example
  slug: amazon-app-mesh-subjectalternativenames-example
- key_count: 0
  name: Amazon App Mesh Suffixhostname Example
  slug: amazon-app-mesh-suffixhostname-example
- key_count: 0
  name: Amazon App Mesh Tagkey Example
  slug: amazon-app-mesh-tagkey-example
- key_count: 0
  name: Amazon App Mesh Tagkeylist Example
  slug: amazon-app-mesh-tagkeylist-example
- key_count: 0
  name: Amazon App Mesh Taglist Example
  slug: amazon-app-mesh-taglist-example
- key_count: 2
  name: Amazon App Mesh Tagref Example
  slug: amazon-app-mesh-tagref-example
- key_count: 1
  name: Amazon App Mesh Tagresourceinput Example
  slug: amazon-app-mesh-tagresourceinput-example
- key_count: 0
  name: Amazon App Mesh Tagresourceoutput Example
  slug: amazon-app-mesh-tagresourceoutput-example
- key_count: 0
  name: Amazon App Mesh Tagslimit Example
  slug: amazon-app-mesh-tagslimit-example
- key_count: 0
  name: Amazon App Mesh Tagvalue Example
  slug: amazon-app-mesh-tagvalue-example
- key_count: 0
  name: Amazon App Mesh Tcpretrypolicyevent Example
  slug: amazon-app-mesh-tcpretrypolicyevent-example
- key_count: 0
  name: Amazon App Mesh Tcpretrypolicyevents Example
  slug: amazon-app-mesh-tcpretrypolicyevents-example
- key_count: 3
  name: Amazon App Mesh Tcproute Example
  slug: amazon-app-mesh-tcproute-example
- key_count: 1
  name: Amazon App Mesh Tcprouteaction Example
  slug: amazon-app-mesh-tcprouteaction-example
- key_count: 1
  name: Amazon App Mesh Tcproutematch Example
  slug: amazon-app-mesh-tcproutematch-example
- key_count: 1
  name: Amazon App Mesh Tcptimeout Example
  slug: amazon-app-mesh-tcptimeout-example
- key_count: 0
  name: Amazon App Mesh Textformat Example
  slug: amazon-app-mesh-textformat-example
- key_count: 0
  name: Amazon App Mesh Timestamp Example
  slug: amazon-app-mesh-timestamp-example
- key_count: 2
  name: Amazon App Mesh Tlsvalidationcontext Example
  slug: amazon-app-mesh-tlsvalidationcontext-example
- key_count: 1
  name: Amazon App Mesh Tlsvalidationcontextacmtrust Example
  slug: amazon-app-mesh-tlsvalidationcontextacmtrust-example
- key_count: 1
  name: Amazon App Mesh Tlsvalidationcontextfiletrust Example
  slug: amazon-app-mesh-tlsvalidationcontextfiletrust-example
- key_count: 1
  name: Amazon App Mesh Tlsvalidationcontextsdstrust Example
  slug: amazon-app-mesh-tlsvalidationcontextsdstrust-example
- key_count: 3
  name: Amazon App Mesh Tlsvalidationcontexttrust Example
  slug: amazon-app-mesh-tlsvalidationcontexttrust-example
- key_count: 1
  name: Amazon App Mesh Untagresourceinput Example
  slug: amazon-app-mesh-untagresourceinput-example
- key_count: 0
  name: Amazon App Mesh Untagresourceoutput Example
  slug: amazon-app-mesh-untagresourceoutput-example
- key_count: 2
  name: Amazon App Mesh Updategatewayrouteinput Example
  slug: amazon-app-mesh-updategatewayrouteinput-example
- key_count: 1
  name: Amazon App Mesh Updategatewayrouteoutput Example
  slug: amazon-app-mesh-updategatewayrouteoutput-example
- key_count: 2
  name: Amazon App Mesh Updatemeshinput Example
  slug: amazon-app-mesh-updatemeshinput-example
- key_count: 1
  name: Amazon App Mesh Updatemeshoutput Example
  slug: amazon-app-mesh-updatemeshoutput-example
- key_count: 2
  name: Amazon App Mesh Updaterouteinput Example
  slug: amazon-app-mesh-updaterouteinput-example
- key_count: 1
  name: Amazon App Mesh Updaterouteoutput Example
  slug: amazon-app-mesh-updaterouteoutput-example
- key_count: 2
  name: Amazon App Mesh Updatevirtualgatewayinput Example
  slug: amazon-app-mesh-updatevirtualgatewayinput-example
- key_count: 1
  name: Amazon App Mesh Updatevirtualgatewayoutput Example
  slug: amazon-app-mesh-updatevirtualgatewayoutput-example
- key_count: 2
  name: Amazon App Mesh Updatevirtualnodeinput Example
  slug: amazon-app-mesh-updatevirtualnodeinput-example
- key_count: 1
  name: Amazon App Mesh Updatevirtualnodeoutput Example
  slug: amazon-app-mesh-updatevirtualnodeoutput-example
- key_count: 2
  name: Amazon App Mesh Updatevirtualrouterinput Example
  slug: amazon-app-mesh-updatevirtualrouterinput-example
- key_count: 1
  name: Amazon App Mesh Updatevirtualrouteroutput Example
  slug: amazon-app-mesh-updatevirtualrouteroutput-example
- key_count: 2
  name: Amazon App Mesh Updatevirtualserviceinput Example
  slug: amazon-app-mesh-updatevirtualserviceinput-example
- key_count: 1
  name: Amazon App Mesh Updatevirtualserviceoutput Example
  slug: amazon-app-mesh-updatevirtualserviceoutput-example
- key_count: 1
  name: Amazon App Mesh Virtualgatewayaccesslog Example
  slug: amazon-app-mesh-virtualgatewayaccesslog-example
- key_count: 1
  name: Amazon App Mesh Virtualgatewaybackenddefaults Example
  slug: amazon-app-mesh-virtualgatewaybackenddefaults-example
- key_count: 0
  name: Amazon App Mesh Virtualgatewaycertificateauthorityarns Example
  slug: amazon-app-mesh-virtualgatewaycertificateauthorityarns-example
- key_count: 1
  name: Amazon App Mesh Virtualgatewayclientpolicy Example
  slug: amazon-app-mesh-virtualgatewayclientpolicy-example
- key_count: 4
  name: Amazon App Mesh Virtualgatewayclientpolicytls Example
  slug: amazon-app-mesh-virtualgatewayclientpolicytls-example
- key_count: 2
  name: Amazon App Mesh Virtualgatewayclienttlscertificate Example
  slug: amazon-app-mesh-virtualgatewayclienttlscertificate-example
- key_count: 3
  name: Amazon App Mesh Virtualgatewayconnectionpool Example
  slug: amazon-app-mesh-virtualgatewayconnectionpool-example
- key_count: 5
  name: Amazon App Mesh Virtualgatewaydata Example
  slug: amazon-app-mesh-virtualgatewaydata-example
- key_count: 2
  name: Amazon App Mesh Virtualgatewayfileaccesslog Example
  slug: amazon-app-mesh-virtualgatewayfileaccesslog-example
- key_count: 1
  name: Amazon App Mesh Virtualgatewaygrpcconnectionpool Example
  slug: amazon-app-mesh-virtualgatewaygrpcconnectionpool-example
- key_count: 0
  name: Amazon App Mesh Virtualgatewayhealthcheckintervalmillis Example
  slug: amazon-app-mesh-virtualgatewayhealthcheckintervalmillis-example
- key_count: 7
  name: Amazon App Mesh Virtualgatewayhealthcheckpolicy Example
  slug: amazon-app-mesh-virtualgatewayhealthcheckpolicy-example
- key_count: 0
  name: Amazon App Mesh Virtualgatewayhealthcheckthreshold Example
  slug: amazon-app-mesh-virtualgatewayhealthcheckthreshold-example
- key_count: 0
  name: Amazon App Mesh Virtualgatewayhealthchecktimeoutmillis Example
  slug: amazon-app-mesh-virtualgatewayhealthchecktimeoutmillis-example
- key_count: 1
  name: Amazon App Mesh Virtualgatewayhttp2Connectionpool Example
  slug: amazon-app-mesh-virtualgatewayhttp2connectionpool-example
- key_count: 2
  name: Amazon App Mesh Virtualgatewayhttpconnectionpool Example
  slug: amazon-app-mesh-virtualgatewayhttpconnectionpool-example
- key_count: 0
  name: Amazon App Mesh Virtualgatewaylist Example
  slug: amazon-app-mesh-virtualgatewaylist-example
- key_count: 4
  name: Amazon App Mesh Virtualgatewaylistener Example
  slug: amazon-app-mesh-virtualgatewaylistener-example
- key_count: 0
  name: Amazon App Mesh Virtualgatewaylisteners Example
  slug: amazon-app-mesh-virtualgatewaylisteners-example
- key_count: 3
  name: Amazon App Mesh Virtualgatewaylistenertls Example
  slug: amazon-app-mesh-virtualgatewaylistenertls-example
- key_count: 1
  name: Amazon App Mesh Virtualgatewaylistenertlsacmcertificate Example
  slug: amazon-app-mesh-virtualgatewaylistenertlsacmcertificate-example
- key_count: 3
  name: Amazon App Mesh Virtualgatewaylistenertlscertificate Example
  slug: amazon-app-mesh-virtualgatewaylistenertlscertificate-example
- key_count: 2
  name: Amazon App Mesh Virtualgatewaylistenertlsfilecertificate Example
  slug: amazon-app-mesh-virtualgatewaylistenertlsfilecertificate-example
- key_count: 0
  name: Amazon App Mesh Virtualgatewaylistenertlsmode Example
  slug: amazon-app-mesh-virtualgatewaylistenertlsmode-example
- key_count: 1
  name: Amazon App Mesh Virtualgatewaylistenertlssdscertificate Example
  slug: amazon-app-mesh-virtualgatewaylistenertlssdscertificate-example
- key_count: 2
  name: Amazon App Mesh Virtualgatewaylistenertlsvalidationcontext Example
  slug: amazon-app-mesh-virtualgatewaylistenertlsvalidationcontext-example
- key_count: 2
  name: Amazon App Mesh Virtualgatewaylistenertlsvalidationcontexttrust Example
  slug: amazon-app-mesh-virtualgatewaylistenertlsvalidationcontexttrust-example
- key_count: 1
  name: Amazon App Mesh Virtualgatewaylogging Example
  slug: amazon-app-mesh-virtualgatewaylogging-example
- key_count: 2
  name: Amazon App Mesh Virtualgatewayportmapping Example
  slug: amazon-app-mesh-virtualgatewayportmapping-example
- key_count: 0
  name: Amazon App Mesh Virtualgatewayportprotocol Example
  slug: amazon-app-mesh-virtualgatewayportprotocol-example
- key_count: 8
  name: Amazon App Mesh Virtualgatewayref Example
  slug: amazon-app-mesh-virtualgatewayref-example
- key_count: 0
  name: Amazon App Mesh Virtualgatewaysdssecretname Example
  slug: amazon-app-mesh-virtualgatewaysdssecretname-example
- key_count: 3
  name: Amazon App Mesh Virtualgatewayspec Example
  slug: amazon-app-mesh-virtualgatewayspec-example
- key_count: 1
  name: Amazon App Mesh Virtualgatewaystatus Example
  slug: amazon-app-mesh-virtualgatewaystatus-example
- key_count: 0
  name: Amazon App Mesh Virtualgatewaystatuscode Example
  slug: amazon-app-mesh-virtualgatewaystatuscode-example
- key_count: 2
  name: Amazon App Mesh Virtualgatewaytlsvalidationcontext Example
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontext-example
- key_count: 1
  name: Amazon App Mesh Virtualgatewaytlsvalidationcontextacmtrust Example
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontextacmtrust-example
- key_count: 1
  name: Amazon App Mesh Virtualgatewaytlsvalidationcontextfiletrust Example
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontextfiletrust-example
- key_count: 1
  name: Amazon App Mesh Virtualgatewaytlsvalidationcontextsdstrust Example
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontextsdstrust-example
- key_count: 3
  name: Amazon App Mesh Virtualgatewaytlsvalidationcontexttrust Example
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontexttrust-example
- key_count: 4
  name: Amazon App Mesh Virtualnodeconnectionpool Example
  slug: amazon-app-mesh-virtualnodeconnectionpool-example
- key_count: 5
  name: Amazon App Mesh Virtualnodedata Example
  slug: amazon-app-mesh-virtualnodedata-example
- key_count: 1
  name: Amazon App Mesh Virtualnodegrpcconnectionpool Example
  slug: amazon-app-mesh-virtualnodegrpcconnectionpool-example
- key_count: 1
  name: Amazon App Mesh Virtualnodehttp2Connectionpool Example
  slug: amazon-app-mesh-virtualnodehttp2connectionpool-example
- key_count: 2
  name: Amazon App Mesh Virtualnodehttpconnectionpool Example
  slug: amazon-app-mesh-virtualnodehttpconnectionpool-example
- key_count: 0
  name: Amazon App Mesh Virtualnodelist Example
  slug: amazon-app-mesh-virtualnodelist-example
- key_count: 8
  name: Amazon App Mesh Virtualnoderef Example
  slug: amazon-app-mesh-virtualnoderef-example
- key_count: 1
  name: Amazon App Mesh Virtualnodeserviceprovider Example
  slug: amazon-app-mesh-virtualnodeserviceprovider-example
- key_count: 5
  name: Amazon App Mesh Virtualnodespec Example
  slug: amazon-app-mesh-virtualnodespec-example
- key_count: 1
  name: Amazon App Mesh Virtualnodestatus Example
  slug: amazon-app-mesh-virtualnodestatus-example
- key_count: 0
  name: Amazon App Mesh Virtualnodestatuscode Example
  slug: amazon-app-mesh-virtualnodestatuscode-example
- key_count: 1
  name: Amazon App Mesh Virtualnodetcpconnectionpool Example
  slug: amazon-app-mesh-virtualnodetcpconnectionpool-example
- key_count: 5
  name: Amazon App Mesh Virtualrouterdata Example
  slug: amazon-app-mesh-virtualrouterdata-example
- key_count: 0
  name: Amazon App Mesh Virtualrouterlist Example
  slug: amazon-app-mesh-virtualrouterlist-example
- key_count: 1
  name: Amazon App Mesh Virtualrouterlistener Example
  slug: amazon-app-mesh-virtualrouterlistener-example
- key_count: 0
  name: Amazon App Mesh Virtualrouterlisteners Example
  slug: amazon-app-mesh-virtualrouterlisteners-example
- key_count: 8
  name: Amazon App Mesh Virtualrouterref Example
  slug: amazon-app-mesh-virtualrouterref-example
- key_count: 1
  name: Amazon App Mesh Virtualrouterserviceprovider Example
  slug: amazon-app-mesh-virtualrouterserviceprovider-example
- key_count: 1
  name: Amazon App Mesh Virtualrouterspec Example
  slug: amazon-app-mesh-virtualrouterspec-example
- key_count: 1
  name: Amazon App Mesh Virtualrouterstatus Example
  slug: amazon-app-mesh-virtualrouterstatus-example
- key_count: 0
  name: Amazon App Mesh Virtualrouterstatuscode Example
  slug: amazon-app-mesh-virtualrouterstatuscode-example
- key_count: 2
  name: Amazon App Mesh Virtualservicebackend Example
  slug: amazon-app-mesh-virtualservicebackend-example
- key_count: 5
  name: Amazon App Mesh Virtualservicedata Example
  slug: amazon-app-mesh-virtualservicedata-example
- key_count: 0
  name: Amazon App Mesh Virtualservicelist Example
  slug: amazon-app-mesh-virtualservicelist-example
- key_count: 2
  name: Amazon App Mesh Virtualserviceprovider Example
  slug: amazon-app-mesh-virtualserviceprovider-example
- key_count: 8
  name: Amazon App Mesh Virtualserviceref Example
  slug: amazon-app-mesh-virtualserviceref-example
- key_count: 1
  name: Amazon App Mesh Virtualservicespec Example
  slug: amazon-app-mesh-virtualservicespec-example
- key_count: 1
  name: Amazon App Mesh Virtualservicestatus Example
  slug: amazon-app-mesh-virtualservicestatus-example
- key_count: 0
  name: Amazon App Mesh Virtualservicestatuscode Example
  slug: amazon-app-mesh-virtualservicestatuscode-example
- key_count: 3
  name: Amazon App Mesh Weightedtarget Example
  slug: amazon-app-mesh-weightedtarget-example
- key_count: 0
  name: Amazon App Mesh Weightedtargets Example
  slug: amazon-app-mesh-weightedtargets-example
features:
- description: Create and manage service meshes that define the logical boundary for network traffic between microservices.
  name: Service Mesh Management
- description: Define virtual services that act as logical routers for microservice traffic, abstracting the underlying routing logic.
  name: Virtual Service Configuration
- description: Configure virtual routers and routes to implement traffic management policies including weighted routing and retry policies.
  name: Traffic Routing Control
- description: Manage virtual nodes representing microservice task groups with service discovery and health check configurations.
  name: Virtual Node Management
- description: Configure access logs and tracing for end-to-end visibility of traffic flowing through the service mesh.
  name: Observability Integration
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-app-mesh.png
integrations:
- description: Deploy App Mesh sidecar proxies alongside ECS tasks for automatic traffic interception and routing.
  name: AWS ECS
- description: Run App Mesh with Kubernetes via the App Mesh Controller for Kubernetes for native K8s integration.
  name: AWS EKS
- description: Use X-Ray for distributed tracing of requests flowing through the App Mesh service mesh.
  name: AWS X-Ray
- description: Integrate App Mesh with Cloud Map for service discovery across ECS, EKS, and EC2 compute.
  name: AWS Cloud Map
json_schemas:
- name: AccessLog
  property_count: 1
  slug: amazon-app-mesh-accesslog
- name: AccountId
  property_count: 0
  slug: amazon-app-mesh-accountid
- name: Arn
  property_count: 0
  slug: amazon-app-mesh-arn
- name: AwsCloudMapInstanceAttribute
  property_count: 2
  slug: amazon-app-mesh-awscloudmapinstanceattribute
- name: AwsCloudMapInstanceAttributeKey
  property_count: 0
  slug: amazon-app-mesh-awscloudmapinstanceattributekey
- name: AwsCloudMapInstanceAttributes
  property_count: 0
  slug: amazon-app-mesh-awscloudmapinstanceattributes
- name: AwsCloudMapInstanceAttributeValue
  property_count: 0
  slug: amazon-app-mesh-awscloudmapinstanceattributevalue
- name: AwsCloudMapName
  property_count: 0
  slug: amazon-app-mesh-awscloudmapname
- name: AwsCloudMapServiceDiscovery
  property_count: 4
  slug: amazon-app-mesh-awscloudmapservicediscovery
- name: Backend
  property_count: 1
  slug: amazon-app-mesh-backend
- name: BackendDefaults
  property_count: 1
  slug: amazon-app-mesh-backenddefaults
- name: Backends
  property_count: 0
  slug: amazon-app-mesh-backends
- name: Boolean
  property_count: 0
  slug: amazon-app-mesh-boolean
- name: CertificateAuthorityArns
  property_count: 0
  slug: amazon-app-mesh-certificateauthorityarns
- name: ClientPolicy
  property_count: 1
  slug: amazon-app-mesh-clientpolicy
- name: ClientPolicyTls
  property_count: 4
  slug: amazon-app-mesh-clientpolicytls
- name: ClientTlsCertificate
  property_count: 2
  slug: amazon-app-mesh-clienttlscertificate
- name: CreateGatewayRouteInput
  property_count: 4
  slug: amazon-app-mesh-creategatewayrouteinput
- name: CreateGatewayRouteOutput
  property_count: 1
  slug: amazon-app-mesh-creategatewayrouteoutput
- name: CreateMeshInput
  property_count: 4
  slug: amazon-app-mesh-createmeshinput
- name: CreateMeshOutput
  property_count: 1
  slug: amazon-app-mesh-createmeshoutput
- name: CreateRouteInput
  property_count: 4
  slug: amazon-app-mesh-createrouteinput
- name: CreateRouteOutput
  property_count: 1
  slug: amazon-app-mesh-createrouteoutput
- name: CreateVirtualGatewayInput
  property_count: 4
  slug: amazon-app-mesh-createvirtualgatewayinput
- name: CreateVirtualGatewayOutput
  property_count: 1
  slug: amazon-app-mesh-createvirtualgatewayoutput
- name: CreateVirtualNodeInput
  property_count: 4
  slug: amazon-app-mesh-createvirtualnodeinput
- name: CreateVirtualNodeOutput
  property_count: 1
  slug: amazon-app-mesh-createvirtualnodeoutput
- name: CreateVirtualRouterInput
  property_count: 4
  slug: amazon-app-mesh-createvirtualrouterinput
- name: CreateVirtualRouterOutput
  property_count: 1
  slug: amazon-app-mesh-createvirtualrouteroutput
- name: CreateVirtualServiceInput
  property_count: 4
  slug: amazon-app-mesh-createvirtualserviceinput
- name: CreateVirtualServiceOutput
  property_count: 1
  slug: amazon-app-mesh-createvirtualserviceoutput
- name: DefaultGatewayRouteRewrite
  property_count: 0
  slug: amazon-app-mesh-defaultgatewayrouterewrite
- name: DeleteGatewayRouteInput
  property_count: 0
  slug: amazon-app-mesh-deletegatewayrouteinput
- name: DeleteGatewayRouteOutput
  property_count: 1
  slug: amazon-app-mesh-deletegatewayrouteoutput
- name: DeleteMeshInput
  property_count: 0
  slug: amazon-app-mesh-deletemeshinput
- name: DeleteMeshOutput
  property_count: 1
  slug: amazon-app-mesh-deletemeshoutput
- name: DeleteRouteInput
  property_count: 0
  slug: amazon-app-mesh-deleterouteinput
- name: DeleteRouteOutput
  property_count: 1
  slug: amazon-app-mesh-deleterouteoutput
- name: DeleteVirtualGatewayInput
  property_count: 0
  slug: amazon-app-mesh-deletevirtualgatewayinput
- name: DeleteVirtualGatewayOutput
  property_count: 1
  slug: amazon-app-mesh-deletevirtualgatewayoutput
- name: DeleteVirtualNodeInput
  property_count: 0
  slug: amazon-app-mesh-deletevirtualnodeinput
- name: DeleteVirtualNodeOutput
  property_count: 1
  slug: amazon-app-mesh-deletevirtualnodeoutput
- name: DeleteVirtualRouterInput
  property_count: 0
  slug: amazon-app-mesh-deletevirtualrouterinput
- name: DeleteVirtualRouterOutput
  property_count: 1
  slug: amazon-app-mesh-deletevirtualrouteroutput
- name: DeleteVirtualServiceInput
  property_count: 0
  slug: amazon-app-mesh-deletevirtualserviceinput
- name: DeleteVirtualServiceOutput
  property_count: 1
  slug: amazon-app-mesh-deletevirtualserviceoutput
- name: DescribeGatewayRouteInput
  property_count: 0
  slug: amazon-app-mesh-describegatewayrouteinput
- name: DescribeGatewayRouteOutput
  property_count: 1
  slug: amazon-app-mesh-describegatewayrouteoutput
- name: DescribeMeshInput
  property_count: 0
  slug: amazon-app-mesh-describemeshinput
- name: DescribeMeshOutput
  property_count: 1
  slug: amazon-app-mesh-describemeshoutput
- name: DescribeRouteInput
  property_count: 0
  slug: amazon-app-mesh-describerouteinput
- name: DescribeRouteOutput
  property_count: 1
  slug: amazon-app-mesh-describerouteoutput
- name: DescribeVirtualGatewayInput
  property_count: 0
  slug: amazon-app-mesh-describevirtualgatewayinput
- name: DescribeVirtualGatewayOutput
  property_count: 1
  slug: amazon-app-mesh-describevirtualgatewayoutput
- name: DescribeVirtualNodeInput
  property_count: 0
  slug: amazon-app-mesh-describevirtualnodeinput
- name: DescribeVirtualNodeOutput
  property_count: 1
  slug: amazon-app-mesh-describevirtualnodeoutput
- name: DescribeVirtualRouterInput
  property_count: 0
  slug: amazon-app-mesh-describevirtualrouterinput
- name: DescribeVirtualRouterOutput
  property_count: 1
  slug: amazon-app-mesh-describevirtualrouteroutput
- name: DescribeVirtualServiceInput
  property_count: 0
  slug: amazon-app-mesh-describevirtualserviceinput
- name: DescribeVirtualServiceOutput
  property_count: 1
  slug: amazon-app-mesh-describevirtualserviceoutput
- name: DnsResponseType
  property_count: 0
  slug: amazon-app-mesh-dnsresponsetype
- name: DnsServiceDiscovery
  property_count: 3
  slug: amazon-app-mesh-dnsservicediscovery
- name: Duration
  property_count: 2
  slug: amazon-app-mesh-duration
- name: DurationUnit
  property_count: 0
  slug: amazon-app-mesh-durationunit
- name: DurationValue
  property_count: 0
  slug: amazon-app-mesh-durationvalue
- name: EgressFilter
  property_count: 1
  slug: amazon-app-mesh-egressfilter
- name: EgressFilterType
  property_count: 0
  slug: amazon-app-mesh-egressfiltertype
- name: ExactHostName
  property_count: 0
  slug: amazon-app-mesh-exacthostname
- name: FileAccessLog
  property_count: 2
  slug: amazon-app-mesh-fileaccesslog
- name: FilePath
  property_count: 0
  slug: amazon-app-mesh-filepath
- name: GatewayRouteData
  property_count: 6
  slug: amazon-app-mesh-gatewayroutedata
- name: GatewayRouteHostnameMatch
  property_count: 2
  slug: amazon-app-mesh-gatewayroutehostnamematch
- name: GatewayRouteHostnameRewrite
  property_count: 1
  slug: amazon-app-mesh-gatewayroutehostnamerewrite
- name: GatewayRouteList
  property_count: 0
  slug: amazon-app-mesh-gatewayroutelist
- name: GatewayRoutePriority
  property_count: 0
  slug: amazon-app-mesh-gatewayroutepriority
- name: GatewayRouteRef
  property_count: 9
  slug: amazon-app-mesh-gatewayrouteref
- name: GatewayRouteSpec
  property_count: 4
  slug: amazon-app-mesh-gatewayroutespec
- name: GatewayRouteStatus
  property_count: 1
  slug: amazon-app-mesh-gatewayroutestatus
- name: GatewayRouteStatusCode
  property_count: 0
  slug: amazon-app-mesh-gatewayroutestatuscode
- name: GatewayRouteTarget
  property_count: 2
  slug: amazon-app-mesh-gatewayroutetarget
- name: GatewayRouteVirtualService
  property_count: 1
  slug: amazon-app-mesh-gatewayroutevirtualservice
- name: GrpcGatewayRoute
  property_count: 2
  slug: amazon-app-mesh-grpcgatewayroute
- name: GrpcGatewayRouteAction
  property_count: 2
  slug: amazon-app-mesh-grpcgatewayrouteaction
- name: GrpcGatewayRouteMatch
  property_count: 4
  slug: amazon-app-mesh-grpcgatewayroutematch
- name: GrpcGatewayRouteMetadata
  property_count: 3
  slug: amazon-app-mesh-grpcgatewayroutemetadata
- name: GrpcGatewayRouteMetadataList
  property_count: 0
  slug: amazon-app-mesh-grpcgatewayroutemetadatalist
- name: GrpcGatewayRouteRewrite
  property_count: 1
  slug: amazon-app-mesh-grpcgatewayrouterewrite
- name: GrpcMetadataMatchMethod
  property_count: 5
  slug: amazon-app-mesh-grpcmetadatamatchmethod
- name: GrpcRetryPolicy
  property_count: 5
  slug: amazon-app-mesh-grpcretrypolicy
- name: GrpcRetryPolicyEvent
  property_count: 0
  slug: amazon-app-mesh-grpcretrypolicyevent
- name: GrpcRetryPolicyEvents
  property_count: 0
  slug: amazon-app-mesh-grpcretrypolicyevents
- name: GrpcRoute
  property_count: 4
  slug: amazon-app-mesh-grpcroute
- name: GrpcRouteAction
  property_count: 1
  slug: amazon-app-mesh-grpcrouteaction
- name: GrpcRouteMatch
  property_count: 4
  slug: amazon-app-mesh-grpcroutematch
- name: GrpcRouteMetadata
  property_count: 3
  slug: amazon-app-mesh-grpcroutemetadata
- name: GrpcRouteMetadataList
  property_count: 0
  slug: amazon-app-mesh-grpcroutemetadatalist
- name: GrpcRouteMetadataMatchMethod
  property_count: 5
  slug: amazon-app-mesh-grpcroutemetadatamatchmethod
- name: GrpcTimeout
  property_count: 2
  slug: amazon-app-mesh-grpctimeout
- name: HeaderMatch
  property_count: 0
  slug: amazon-app-mesh-headermatch
- name: HeaderMatchMethod
  property_count: 5
  slug: amazon-app-mesh-headermatchmethod
- name: HeaderName
  property_count: 0
  slug: amazon-app-mesh-headername
- name: HealthCheckIntervalMillis
  property_count: 0
  slug: amazon-app-mesh-healthcheckintervalmillis
- name: HealthCheckPolicy
  property_count: 7
  slug: amazon-app-mesh-healthcheckpolicy
- name: HealthCheckThreshold
  property_count: 0
  slug: amazon-app-mesh-healthcheckthreshold
- name: HealthCheckTimeoutMillis
  property_count: 0
  slug: amazon-app-mesh-healthchecktimeoutmillis
- name: Hostname
  property_count: 0
  slug: amazon-app-mesh-hostname
- name: HttpGatewayRoute
  property_count: 2
  slug: amazon-app-mesh-httpgatewayroute
- name: HttpGatewayRouteAction
  property_count: 2
  slug: amazon-app-mesh-httpgatewayrouteaction
- name: HttpGatewayRouteHeader
  property_count: 3
  slug: amazon-app-mesh-httpgatewayrouteheader
- name: HttpGatewayRouteHeaders
  property_count: 0
  slug: amazon-app-mesh-httpgatewayrouteheaders
- name: HttpGatewayRouteMatch
  property_count: 7
  slug: amazon-app-mesh-httpgatewayroutematch
- name: HttpGatewayRoutePathRewrite
  property_count: 1
  slug: amazon-app-mesh-httpgatewayroutepathrewrite
- name: HttpGatewayRoutePrefix
  property_count: 0
  slug: amazon-app-mesh-httpgatewayrouteprefix
- name: HttpGatewayRoutePrefixRewrite
  property_count: 2
  slug: amazon-app-mesh-httpgatewayrouteprefixrewrite
- name: HttpGatewayRouteRewrite
  property_count: 3
  slug: amazon-app-mesh-httpgatewayrouterewrite
- name: HttpMethod
  property_count: 0
  slug: amazon-app-mesh-httpmethod
- name: HttpPathExact
  property_count: 0
  slug: amazon-app-mesh-httppathexact
- name: HttpPathMatch
  property_count: 2
  slug: amazon-app-mesh-httppathmatch
- name: HttpPathRegex
  property_count: 0
  slug: amazon-app-mesh-httppathregex
- name: HttpQueryParameter
  property_count: 2
  slug: amazon-app-mesh-httpqueryparameter
- name: HttpQueryParameters
  property_count: 0
  slug: amazon-app-mesh-httpqueryparameters
- name: HttpRetryPolicy
  property_count: 4
  slug: amazon-app-mesh-httpretrypolicy
- name: HttpRetryPolicyEvent
  property_count: 0
  slug: amazon-app-mesh-httpretrypolicyevent
- name: HttpRetryPolicyEvents
  property_count: 0
  slug: amazon-app-mesh-httpretrypolicyevents
- name: HttpRoute
  property_count: 4
  slug: amazon-app-mesh-httproute
- name: HttpRouteAction
  property_count: 1
  slug: amazon-app-mesh-httprouteaction
- name: HttpRouteHeader
  property_count: 3
  slug: amazon-app-mesh-httprouteheader
- name: HttpRouteHeaders
  property_count: 0
  slug: amazon-app-mesh-httprouteheaders
- name: HttpRouteMatch
  property_count: 7
  slug: amazon-app-mesh-httproutematch
- name: HttpScheme
  property_count: 0
  slug: amazon-app-mesh-httpscheme
- name: HttpTimeout
  property_count: 2
  slug: amazon-app-mesh-httptimeout
- name: IpPreference
  property_count: 0
  slug: amazon-app-mesh-ippreference
- name: JsonFormat
  property_count: 0
  slug: amazon-app-mesh-jsonformat
- name: JsonFormatRef
  property_count: 2
  slug: amazon-app-mesh-jsonformatref
- name: JsonKey
  property_count: 0
  slug: amazon-app-mesh-jsonkey
- name: JsonValue
  property_count: 0
  slug: amazon-app-mesh-jsonvalue
- name: Listener
  property_count: 6
  slug: amazon-app-mesh-listener
- name: ListenerPort
  property_count: 0
  slug: amazon-app-mesh-listenerport
- name: Listeners
  property_count: 0
  slug: amazon-app-mesh-listeners
- name: ListenerTimeout
  property_count: 4
  slug: amazon-app-mesh-listenertimeout
- name: ListenerTls
  property_count: 3
  slug: amazon-app-mesh-listenertls
- name: ListenerTlsAcmCertificate
  property_count: 1
  slug: amazon-app-mesh-listenertlsacmcertificate
- name: ListenerTlsCertificate
  property_count: 3
  slug: amazon-app-mesh-listenertlscertificate
- name: ListenerTlsFileCertificate
  property_count: 2
  slug: amazon-app-mesh-listenertlsfilecertificate
- name: ListenerTlsMode
  property_count: 0
  slug: amazon-app-mesh-listenertlsmode
- name: ListenerTlsSdsCertificate
  property_count: 1
  slug: amazon-app-mesh-listenertlssdscertificate
- name: ListenerTlsValidationContext
  property_count: 2
  slug: amazon-app-mesh-listenertlsvalidationcontext
- name: ListenerTlsValidationContextTrust
  property_count: 2
  slug: amazon-app-mesh-listenertlsvalidationcontexttrust
- name: ListGatewayRoutesInput
  property_count: 0
  slug: amazon-app-mesh-listgatewayroutesinput
- name: ListGatewayRoutesLimit
  property_count: 0
  slug: amazon-app-mesh-listgatewayrouteslimit
- name: ListGatewayRoutesOutput
  property_count: 2
  slug: amazon-app-mesh-listgatewayroutesoutput
- name: ListMeshesInput
  property_count: 0
  slug: amazon-app-mesh-listmeshesinput
- name: ListMeshesLimit
  property_count: 0
  slug: amazon-app-mesh-listmesheslimit
- name: ListMeshesOutput
  property_count: 2
  slug: amazon-app-mesh-listmeshesoutput
- name: ListRoutesInput
  property_count: 0
  slug: amazon-app-mesh-listroutesinput
- name: ListRoutesLimit
  property_count: 0
  slug: amazon-app-mesh-listrouteslimit
- name: ListRoutesOutput
  property_count: 2
  slug: amazon-app-mesh-listroutesoutput
- name: ListTagsForResourceInput
  property_count: 0
  slug: amazon-app-mesh-listtagsforresourceinput
- name: ListTagsForResourceOutput
  property_count: 2
  slug: amazon-app-mesh-listtagsforresourceoutput
- name: ListVirtualGatewaysInput
  property_count: 0
  slug: amazon-app-mesh-listvirtualgatewaysinput
- name: ListVirtualGatewaysLimit
  property_count: 0
  slug: amazon-app-mesh-listvirtualgatewayslimit
- name: ListVirtualGatewaysOutput
  property_count: 2
  slug: amazon-app-mesh-listvirtualgatewaysoutput
- name: ListVirtualNodesInput
  property_count: 0
  slug: amazon-app-mesh-listvirtualnodesinput
- name: ListVirtualNodesLimit
  property_count: 0
  slug: amazon-app-mesh-listvirtualnodeslimit
- name: ListVirtualNodesOutput
  property_count: 2
  slug: amazon-app-mesh-listvirtualnodesoutput
- name: ListVirtualRoutersInput
  property_count: 0
  slug: amazon-app-mesh-listvirtualroutersinput
- name: ListVirtualRoutersLimit
  property_count: 0
  slug: amazon-app-mesh-listvirtualrouterslimit
- name: ListVirtualRoutersOutput
  property_count: 2
  slug: amazon-app-mesh-listvirtualroutersoutput
- name: ListVirtualServicesInput
  property_count: 0
  slug: amazon-app-mesh-listvirtualservicesinput
- name: ListVirtualServicesLimit
  property_count: 0
  slug: amazon-app-mesh-listvirtualserviceslimit
- name: ListVirtualServicesOutput
  property_count: 2
  slug: amazon-app-mesh-listvirtualservicesoutput
- name: Logging
  property_count: 1
  slug: amazon-app-mesh-logging
- name: LoggingFormat
  property_count: 2
  slug: amazon-app-mesh-loggingformat
- name: Long
  property_count: 0
  slug: amazon-app-mesh-long
- name: MatchRange
  property_count: 2
  slug: amazon-app-mesh-matchrange
- name: MaxConnections
  property_count: 0
  slug: amazon-app-mesh-maxconnections
- name: MaxPendingRequests
  property_count: 0
  slug: amazon-app-mesh-maxpendingrequests
- name: MaxRequests
  property_count: 0
  slug: amazon-app-mesh-maxrequests
- name: MaxRetries
  property_count: 0
  slug: amazon-app-mesh-maxretries
- name: MeshData
  property_count: 4
  slug: amazon-app-mesh-meshdata
- name: MeshList
  property_count: 0
  slug: amazon-app-mesh-meshlist
- name: MeshRef
  property_count: 7
  slug: amazon-app-mesh-meshref
- name: MeshServiceDiscovery
  property_count: 1
  slug: amazon-app-mesh-meshservicediscovery
- name: MeshSpec
  property_count: 2
  slug: amazon-app-mesh-meshspec
- name: MeshStatus
  property_count: 1
  slug: amazon-app-mesh-meshstatus
- name: MeshStatusCode
  property_count: 0
  slug: amazon-app-mesh-meshstatuscode
- name: MethodName
  property_count: 0
  slug: amazon-app-mesh-methodname
- name: OutlierDetection
  property_count: 4
  slug: amazon-app-mesh-outlierdetection
- name: OutlierDetectionMaxEjectionPercent
  property_count: 0
  slug: amazon-app-mesh-outlierdetectionmaxejectionpercent
- name: OutlierDetectionMaxServerErrors
  property_count: 0
  slug: amazon-app-mesh-outlierdetectionmaxservererrors
- name: PercentInt
  property_count: 0
  slug: amazon-app-mesh-percentint
- name: PortMapping
  property_count: 2
  slug: amazon-app-mesh-portmapping
- name: PortNumber
  property_count: 0
  slug: amazon-app-mesh-portnumber
- name: PortProtocol
  property_count: 0
  slug: amazon-app-mesh-portprotocol
- name: PortSet
  property_count: 0
  slug: amazon-app-mesh-portset
- name: QueryParameterMatch
  property_count: 1
  slug: amazon-app-mesh-queryparametermatch
- name: QueryParameterName
  property_count: 0
  slug: amazon-app-mesh-queryparametername
- name: ResourceMetadata
  property_count: 7
  slug: amazon-app-mesh-resourcemetadata
- name: ResourceName
  property_count: 0
  slug: amazon-app-mesh-resourcename
- name: RouteData
  property_count: 6
  slug: amazon-app-mesh-routedata
- name: RouteList
  property_count: 0
  slug: amazon-app-mesh-routelist
- name: RoutePriority
  property_count: 0
  slug: amazon-app-mesh-routepriority
- name: RouteRef
  property_count: 9
  slug: amazon-app-mesh-routeref
- name: RouteSpec
  property_count: 5
  slug: amazon-app-mesh-routespec
- name: RouteStatus
  property_count: 1
  slug: amazon-app-mesh-routestatus
- name: RouteStatusCode
  property_count: 0
  slug: amazon-app-mesh-routestatuscode
- name: SdsSecretName
  property_count: 0
  slug: amazon-app-mesh-sdssecretname
- name: ServiceDiscovery
  property_count: 2
  slug: amazon-app-mesh-servicediscovery
- name: ServiceName
  property_count: 0
  slug: amazon-app-mesh-servicename
- name: String
  property_count: 0
  slug: amazon-app-mesh-string
- name: SubjectAlternativeName
  property_count: 0
  slug: amazon-app-mesh-subjectalternativename
- name: SubjectAlternativeNameList
  property_count: 0
  slug: amazon-app-mesh-subjectalternativenamelist
- name: SubjectAlternativeNameMatchers
  property_count: 1
  slug: amazon-app-mesh-subjectalternativenamematchers
- name: SubjectAlternativeNames
  property_count: 1
  slug: amazon-app-mesh-subjectalternativenames
- name: SuffixHostname
  property_count: 0
  slug: amazon-app-mesh-suffixhostname
- name: TagKey
  property_count: 0
  slug: amazon-app-mesh-tagkey
- name: TagKeyList
  property_count: 0
  slug: amazon-app-mesh-tagkeylist
- name: TagList
  property_count: 0
  slug: amazon-app-mesh-taglist
- name: TagRef
  property_count: 2
  slug: amazon-app-mesh-tagref
- name: TagResourceInput
  property_count: 1
  slug: amazon-app-mesh-tagresourceinput
- name: TagResourceOutput
  property_count: 0
  slug: amazon-app-mesh-tagresourceoutput
- name: TagsLimit
  property_count: 0
  slug: amazon-app-mesh-tagslimit
- name: TagValue
  property_count: 0
  slug: amazon-app-mesh-tagvalue
- name: TcpRetryPolicyEvent
  property_count: 0
  slug: amazon-app-mesh-tcpretrypolicyevent
- name: TcpRetryPolicyEvents
  property_count: 0
  slug: amazon-app-mesh-tcpretrypolicyevents
- name: TcpRoute
  property_count: 3
  slug: amazon-app-mesh-tcproute
- name: TcpRouteAction
  property_count: 1
  slug: amazon-app-mesh-tcprouteaction
- name: TcpRouteMatch
  property_count: 1
  slug: amazon-app-mesh-tcproutematch
- name: TcpTimeout
  property_count: 1
  slug: amazon-app-mesh-tcptimeout
- name: TextFormat
  property_count: 0
  slug: amazon-app-mesh-textformat
- name: Timestamp
  property_count: 0
  slug: amazon-app-mesh-timestamp
- name: TlsValidationContext
  property_count: 2
  slug: amazon-app-mesh-tlsvalidationcontext
- name: TlsValidationContextAcmTrust
  property_count: 1
  slug: amazon-app-mesh-tlsvalidationcontextacmtrust
- name: TlsValidationContextFileTrust
  property_count: 1
  slug: amazon-app-mesh-tlsvalidationcontextfiletrust
- name: TlsValidationContextSdsTrust
  property_count: 1
  slug: amazon-app-mesh-tlsvalidationcontextsdstrust
- name: TlsValidationContextTrust
  property_count: 3
  slug: amazon-app-mesh-tlsvalidationcontexttrust
- name: UntagResourceInput
  property_count: 1
  slug: amazon-app-mesh-untagresourceinput
- name: UntagResourceOutput
  property_count: 0
  slug: amazon-app-mesh-untagresourceoutput
- name: UpdateGatewayRouteInput
  property_count: 2
  slug: amazon-app-mesh-updategatewayrouteinput
- name: UpdateGatewayRouteOutput
  property_count: 1
  slug: amazon-app-mesh-updategatewayrouteoutput
- name: UpdateMeshInput
  property_count: 2
  slug: amazon-app-mesh-updatemeshinput
- name: UpdateMeshOutput
  property_count: 1
  slug: amazon-app-mesh-updatemeshoutput
- name: UpdateRouteInput
  property_count: 2
  slug: amazon-app-mesh-updaterouteinput
- name: UpdateRouteOutput
  property_count: 1
  slug: amazon-app-mesh-updaterouteoutput
- name: UpdateVirtualGatewayInput
  property_count: 2
  slug: amazon-app-mesh-updatevirtualgatewayinput
- name: UpdateVirtualGatewayOutput
  property_count: 1
  slug: amazon-app-mesh-updatevirtualgatewayoutput
- name: UpdateVirtualNodeInput
  property_count: 2
  slug: amazon-app-mesh-updatevirtualnodeinput
- name: UpdateVirtualNodeOutput
  property_count: 1
  slug: amazon-app-mesh-updatevirtualnodeoutput
- name: UpdateVirtualRouterInput
  property_count: 2
  slug: amazon-app-mesh-updatevirtualrouterinput
- name: UpdateVirtualRouterOutput
  property_count: 1
  slug: amazon-app-mesh-updatevirtualrouteroutput
- name: UpdateVirtualServiceInput
  property_count: 2
  slug: amazon-app-mesh-updatevirtualserviceinput
- name: UpdateVirtualServiceOutput
  property_count: 1
  slug: amazon-app-mesh-updatevirtualserviceoutput
- name: VirtualGatewayAccessLog
  property_count: 1
  slug: amazon-app-mesh-virtualgatewayaccesslog
- name: VirtualGatewayBackendDefaults
  property_count: 1
  slug: amazon-app-mesh-virtualgatewaybackenddefaults
- name: VirtualGatewayCertificateAuthorityArns
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaycertificateauthorityarns
- name: VirtualGatewayClientPolicy
  property_count: 1
  slug: amazon-app-mesh-virtualgatewayclientpolicy
- name: VirtualGatewayClientPolicyTls
  property_count: 4
  slug: amazon-app-mesh-virtualgatewayclientpolicytls
- name: VirtualGatewayClientTlsCertificate
  property_count: 2
  slug: amazon-app-mesh-virtualgatewayclienttlscertificate
- name: VirtualGatewayConnectionPool
  property_count: 3
  slug: amazon-app-mesh-virtualgatewayconnectionpool
- name: VirtualGatewayData
  property_count: 5
  slug: amazon-app-mesh-virtualgatewaydata
- name: VirtualGatewayFileAccessLog
  property_count: 2
  slug: amazon-app-mesh-virtualgatewayfileaccesslog
- name: VirtualGatewayGrpcConnectionPool
  property_count: 1
  slug: amazon-app-mesh-virtualgatewaygrpcconnectionpool
- name: VirtualGatewayHealthCheckIntervalMillis
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayhealthcheckintervalmillis
- name: VirtualGatewayHealthCheckPolicy
  property_count: 7
  slug: amazon-app-mesh-virtualgatewayhealthcheckpolicy
- name: VirtualGatewayHealthCheckThreshold
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayhealthcheckthreshold
- name: VirtualGatewayHealthCheckTimeoutMillis
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayhealthchecktimeoutmillis
- name: VirtualGatewayHttp2ConnectionPool
  property_count: 1
  slug: amazon-app-mesh-virtualgatewayhttp2connectionpool
- name: VirtualGatewayHttpConnectionPool
  property_count: 2
  slug: amazon-app-mesh-virtualgatewayhttpconnectionpool
- name: VirtualGatewayList
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylist
- name: VirtualGatewayListener
  property_count: 4
  slug: amazon-app-mesh-virtualgatewaylistener
- name: VirtualGatewayListeners
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylisteners
- name: VirtualGatewayListenerTls
  property_count: 3
  slug: amazon-app-mesh-virtualgatewaylistenertls
- name: VirtualGatewayListenerTlsAcmCertificate
  property_count: 1
  slug: amazon-app-mesh-virtualgatewaylistenertlsacmcertificate
- name: VirtualGatewayListenerTlsCertificate
  property_count: 3
  slug: amazon-app-mesh-virtualgatewaylistenertlscertificate
- name: VirtualGatewayListenerTlsFileCertificate
  property_count: 2
  slug: amazon-app-mesh-virtualgatewaylistenertlsfilecertificate
- name: VirtualGatewayListenerTlsMode
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylistenertlsmode
- name: VirtualGatewayListenerTlsSdsCertificate
  property_count: 1
  slug: amazon-app-mesh-virtualgatewaylistenertlssdscertificate
- name: VirtualGatewayListenerTlsValidationContext
  property_count: 2
  slug: amazon-app-mesh-virtualgatewaylistenertlsvalidationcontext
- name: VirtualGatewayListenerTlsValidationContextTrust
  property_count: 2
  slug: amazon-app-mesh-virtualgatewaylistenertlsvalidationcontexttrust
- name: VirtualGatewayLogging
  property_count: 1
  slug: amazon-app-mesh-virtualgatewaylogging
- name: VirtualGatewayPortMapping
  property_count: 2
  slug: amazon-app-mesh-virtualgatewayportmapping
- name: VirtualGatewayPortProtocol
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayportprotocol
- name: VirtualGatewayRef
  property_count: 8
  slug: amazon-app-mesh-virtualgatewayref
- name: VirtualGatewaySdsSecretName
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaysdssecretname
- name: VirtualGatewaySpec
  property_count: 3
  slug: amazon-app-mesh-virtualgatewayspec
- name: VirtualGatewayStatus
  property_count: 1
  slug: amazon-app-mesh-virtualgatewaystatus
- name: VirtualGatewayStatusCode
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaystatuscode
- name: VirtualGatewayTlsValidationContext
  property_count: 2
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontext
- name: VirtualGatewayTlsValidationContextAcmTrust
  property_count: 1
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontextacmtrust
- name: VirtualGatewayTlsValidationContextFileTrust
  property_count: 1
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontextfiletrust
- name: VirtualGatewayTlsValidationContextSdsTrust
  property_count: 1
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontextsdstrust
- name: VirtualGatewayTlsValidationContextTrust
  property_count: 3
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontexttrust
- name: VirtualNodeConnectionPool
  property_count: 4
  slug: amazon-app-mesh-virtualnodeconnectionpool
- name: VirtualNodeData
  property_count: 5
  slug: amazon-app-mesh-virtualnodedata
- name: VirtualNodeGrpcConnectionPool
  property_count: 1
  slug: amazon-app-mesh-virtualnodegrpcconnectionpool
- name: VirtualNodeHttp2ConnectionPool
  property_count: 1
  slug: amazon-app-mesh-virtualnodehttp2connectionpool
- name: VirtualNodeHttpConnectionPool
  property_count: 2
  slug: amazon-app-mesh-virtualnodehttpconnectionpool
- name: VirtualNodeList
  property_count: 0
  slug: amazon-app-mesh-virtualnodelist
- name: VirtualNodeRef
  property_count: 8
  slug: amazon-app-mesh-virtualnoderef
- name: VirtualNodeServiceProvider
  property_count: 1
  slug: amazon-app-mesh-virtualnodeserviceprovider
- name: VirtualNodeSpec
  property_count: 5
  slug: amazon-app-mesh-virtualnodespec
- name: VirtualNodeStatus
  property_count: 1
  slug: amazon-app-mesh-virtualnodestatus
- name: VirtualNodeStatusCode
  property_count: 0
  slug: amazon-app-mesh-virtualnodestatuscode
- name: VirtualNodeTcpConnectionPool
  property_count: 1
  slug: amazon-app-mesh-virtualnodetcpconnectionpool
- name: VirtualRouterData
  property_count: 5
  slug: amazon-app-mesh-virtualrouterdata
- name: VirtualRouterList
  property_count: 0
  slug: amazon-app-mesh-virtualrouterlist
- name: VirtualRouterListener
  property_count: 1
  slug: amazon-app-mesh-virtualrouterlistener
- name: VirtualRouterListeners
  property_count: 0
  slug: amazon-app-mesh-virtualrouterlisteners
- name: VirtualRouterRef
  property_count: 8
  slug: amazon-app-mesh-virtualrouterref
- name: VirtualRouterServiceProvider
  property_count: 1
  slug: amazon-app-mesh-virtualrouterserviceprovider
- name: VirtualRouterSpec
  property_count: 1
  slug: amazon-app-mesh-virtualrouterspec
- name: VirtualRouterStatus
  property_count: 1
  slug: amazon-app-mesh-virtualrouterstatus
- name: VirtualRouterStatusCode
  property_count: 0
  slug: amazon-app-mesh-virtualrouterstatuscode
- name: VirtualServiceBackend
  property_count: 2
  slug: amazon-app-mesh-virtualservicebackend
- name: VirtualServiceData
  property_count: 5
  slug: amazon-app-mesh-virtualservicedata
- name: VirtualServiceList
  property_count: 0
  slug: amazon-app-mesh-virtualservicelist
- name: VirtualServiceProvider
  property_count: 2
  slug: amazon-app-mesh-virtualserviceprovider
- name: VirtualServiceRef
  property_count: 8
  slug: amazon-app-mesh-virtualserviceref
- name: VirtualServiceSpec
  property_count: 1
  slug: amazon-app-mesh-virtualservicespec
- name: VirtualServiceStatus
  property_count: 1
  slug: amazon-app-mesh-virtualservicestatus
- name: VirtualServiceStatusCode
  property_count: 0
  slug: amazon-app-mesh-virtualservicestatuscode
- name: WeightedTarget
  property_count: 3
  slug: amazon-app-mesh-weightedtarget
- name: WeightedTargets
  property_count: 0
  slug: amazon-app-mesh-weightedtargets
json_structures:
- name: Amazon App Mesh Accesslog Structure
  property_count: 0
  slug: amazon-app-mesh-accesslog-structure
- name: Amazon App Mesh Accountid Structure
  property_count: 0
  slug: amazon-app-mesh-accountid-structure
- name: Amazon App Mesh Arn Structure
  property_count: 0
  slug: amazon-app-mesh-arn-structure
- name: Amazon App Mesh Awscloudmapinstanceattribute Structure
  property_count: 0
  slug: amazon-app-mesh-awscloudmapinstanceattribute-structure
- name: Amazon App Mesh Awscloudmapinstanceattributekey Structure
  property_count: 0
  slug: amazon-app-mesh-awscloudmapinstanceattributekey-structure
- name: Amazon App Mesh Awscloudmapinstanceattributes Structure
  property_count: 0
  slug: amazon-app-mesh-awscloudmapinstanceattributes-structure
- name: Amazon App Mesh Awscloudmapinstanceattributevalue Structure
  property_count: 0
  slug: amazon-app-mesh-awscloudmapinstanceattributevalue-structure
- name: Amazon App Mesh Awscloudmapname Structure
  property_count: 0
  slug: amazon-app-mesh-awscloudmapname-structure
- name: Amazon App Mesh Awscloudmapservicediscovery Structure
  property_count: 0
  slug: amazon-app-mesh-awscloudmapservicediscovery-structure
- name: Amazon App Mesh Backend Structure
  property_count: 0
  slug: amazon-app-mesh-backend-structure
- name: Amazon App Mesh Backenddefaults Structure
  property_count: 0
  slug: amazon-app-mesh-backenddefaults-structure
- name: Amazon App Mesh Backends Structure
  property_count: 0
  slug: amazon-app-mesh-backends-structure
- name: Amazon App Mesh Boolean Structure
  property_count: 0
  slug: amazon-app-mesh-boolean-structure
- name: Amazon App Mesh Certificateauthorityarns Structure
  property_count: 0
  slug: amazon-app-mesh-certificateauthorityarns-structure
- name: Amazon App Mesh Clientpolicy Structure
  property_count: 0
  slug: amazon-app-mesh-clientpolicy-structure
- name: Amazon App Mesh Clientpolicytls Structure
  property_count: 0
  slug: amazon-app-mesh-clientpolicytls-structure
- name: Amazon App Mesh Clienttlscertificate Structure
  property_count: 0
  slug: amazon-app-mesh-clienttlscertificate-structure
- name: Amazon App Mesh Creategatewayrouteinput Structure
  property_count: 0
  slug: amazon-app-mesh-creategatewayrouteinput-structure
- name: Amazon App Mesh Creategatewayrouteoutput Structure
  property_count: 0
  slug: amazon-app-mesh-creategatewayrouteoutput-structure
- name: Amazon App Mesh Createmeshinput Structure
  property_count: 0
  slug: amazon-app-mesh-createmeshinput-structure
- name: Amazon App Mesh Createmeshoutput Structure
  property_count: 0
  slug: amazon-app-mesh-createmeshoutput-structure
- name: Amazon App Mesh Createrouteinput Structure
  property_count: 0
  slug: amazon-app-mesh-createrouteinput-structure
- name: Amazon App Mesh Createrouteoutput Structure
  property_count: 0
  slug: amazon-app-mesh-createrouteoutput-structure
- name: Amazon App Mesh Createvirtualgatewayinput Structure
  property_count: 0
  slug: amazon-app-mesh-createvirtualgatewayinput-structure
- name: Amazon App Mesh Createvirtualgatewayoutput Structure
  property_count: 0
  slug: amazon-app-mesh-createvirtualgatewayoutput-structure
- name: Amazon App Mesh Createvirtualnodeinput Structure
  property_count: 0
  slug: amazon-app-mesh-createvirtualnodeinput-structure
- name: Amazon App Mesh Createvirtualnodeoutput Structure
  property_count: 0
  slug: amazon-app-mesh-createvirtualnodeoutput-structure
- name: Amazon App Mesh Createvirtualrouterinput Structure
  property_count: 0
  slug: amazon-app-mesh-createvirtualrouterinput-structure
- name: Amazon App Mesh Createvirtualrouteroutput Structure
  property_count: 0
  slug: amazon-app-mesh-createvirtualrouteroutput-structure
- name: Amazon App Mesh Createvirtualserviceinput Structure
  property_count: 0
  slug: amazon-app-mesh-createvirtualserviceinput-structure
- name: Amazon App Mesh Createvirtualserviceoutput Structure
  property_count: 0
  slug: amazon-app-mesh-createvirtualserviceoutput-structure
- name: Amazon App Mesh Defaultgatewayrouterewrite Structure
  property_count: 0
  slug: amazon-app-mesh-defaultgatewayrouterewrite-structure
- name: Amazon App Mesh Deletegatewayrouteinput Structure
  property_count: 0
  slug: amazon-app-mesh-deletegatewayrouteinput-structure
- name: Amazon App Mesh Deletegatewayrouteoutput Structure
  property_count: 0
  slug: amazon-app-mesh-deletegatewayrouteoutput-structure
- name: Amazon App Mesh Deletemeshinput Structure
  property_count: 0
  slug: amazon-app-mesh-deletemeshinput-structure
- name: Amazon App Mesh Deletemeshoutput Structure
  property_count: 0
  slug: amazon-app-mesh-deletemeshoutput-structure
- name: Amazon App Mesh Deleterouteinput Structure
  property_count: 0
  slug: amazon-app-mesh-deleterouteinput-structure
- name: Amazon App Mesh Deleterouteoutput Structure
  property_count: 0
  slug: amazon-app-mesh-deleterouteoutput-structure
- name: Amazon App Mesh Deletevirtualgatewayinput Structure
  property_count: 0
  slug: amazon-app-mesh-deletevirtualgatewayinput-structure
- name: Amazon App Mesh Deletevirtualgatewayoutput Structure
  property_count: 0
  slug: amazon-app-mesh-deletevirtualgatewayoutput-structure
- name: Amazon App Mesh Deletevirtualnodeinput Structure
  property_count: 0
  slug: amazon-app-mesh-deletevirtualnodeinput-structure
- name: Amazon App Mesh Deletevirtualnodeoutput Structure
  property_count: 0
  slug: amazon-app-mesh-deletevirtualnodeoutput-structure
- name: Amazon App Mesh Deletevirtualrouterinput Structure
  property_count: 0
  slug: amazon-app-mesh-deletevirtualrouterinput-structure
- name: Amazon App Mesh Deletevirtualrouteroutput Structure
  property_count: 0
  slug: amazon-app-mesh-deletevirtualrouteroutput-structure
- name: Amazon App Mesh Deletevirtualserviceinput Structure
  property_count: 0
  slug: amazon-app-mesh-deletevirtualserviceinput-structure
- name: Amazon App Mesh Deletevirtualserviceoutput Structure
  property_count: 0
  slug: amazon-app-mesh-deletevirtualserviceoutput-structure
- name: Amazon App Mesh Describegatewayrouteinput Structure
  property_count: 0
  slug: amazon-app-mesh-describegatewayrouteinput-structure
- name: Amazon App Mesh Describegatewayrouteoutput Structure
  property_count: 0
  slug: amazon-app-mesh-describegatewayrouteoutput-structure
- name: Amazon App Mesh Describemeshinput Structure
  property_count: 0
  slug: amazon-app-mesh-describemeshinput-structure
- name: Amazon App Mesh Describemeshoutput Structure
  property_count: 0
  slug: amazon-app-mesh-describemeshoutput-structure
- name: Amazon App Mesh Describerouteinput Structure
  property_count: 0
  slug: amazon-app-mesh-describerouteinput-structure
- name: Amazon App Mesh Describerouteoutput Structure
  property_count: 0
  slug: amazon-app-mesh-describerouteoutput-structure
- name: Amazon App Mesh Describevirtualgatewayinput Structure
  property_count: 0
  slug: amazon-app-mesh-describevirtualgatewayinput-structure
- name: Amazon App Mesh Describevirtualgatewayoutput Structure
  property_count: 0
  slug: amazon-app-mesh-describevirtualgatewayoutput-structure
- name: Amazon App Mesh Describevirtualnodeinput Structure
  property_count: 0
  slug: amazon-app-mesh-describevirtualnodeinput-structure
- name: Amazon App Mesh Describevirtualnodeoutput Structure
  property_count: 0
  slug: amazon-app-mesh-describevirtualnodeoutput-structure
- name: Amazon App Mesh Describevirtualrouterinput Structure
  property_count: 0
  slug: amazon-app-mesh-describevirtualrouterinput-structure
- name: Amazon App Mesh Describevirtualrouteroutput Structure
  property_count: 0
  slug: amazon-app-mesh-describevirtualrouteroutput-structure
- name: Amazon App Mesh Describevirtualserviceinput Structure
  property_count: 0
  slug: amazon-app-mesh-describevirtualserviceinput-structure
- name: Amazon App Mesh Describevirtualserviceoutput Structure
  property_count: 0
  slug: amazon-app-mesh-describevirtualserviceoutput-structure
- name: Amazon App Mesh Dnsresponsetype Structure
  property_count: 0
  slug: amazon-app-mesh-dnsresponsetype-structure
- name: Amazon App Mesh Dnsservicediscovery Structure
  property_count: 0
  slug: amazon-app-mesh-dnsservicediscovery-structure
- name: Amazon App Mesh Duration Structure
  property_count: 0
  slug: amazon-app-mesh-duration-structure
- name: Amazon App Mesh Durationunit Structure
  property_count: 0
  slug: amazon-app-mesh-durationunit-structure
- name: Amazon App Mesh Durationvalue Structure
  property_count: 0
  slug: amazon-app-mesh-durationvalue-structure
- name: Amazon App Mesh Egressfilter Structure
  property_count: 0
  slug: amazon-app-mesh-egressfilter-structure
- name: Amazon App Mesh Egressfiltertype Structure
  property_count: 0
  slug: amazon-app-mesh-egressfiltertype-structure
- name: Amazon App Mesh Exacthostname Structure
  property_count: 0
  slug: amazon-app-mesh-exacthostname-structure
- name: Amazon App Mesh Fileaccesslog Structure
  property_count: 0
  slug: amazon-app-mesh-fileaccesslog-structure
- name: Amazon App Mesh Filepath Structure
  property_count: 0
  slug: amazon-app-mesh-filepath-structure
- name: Amazon App Mesh Gatewayroutedata Structure
  property_count: 0
  slug: amazon-app-mesh-gatewayroutedata-structure
- name: Amazon App Mesh Gatewayroutehostnamematch Structure
  property_count: 0
  slug: amazon-app-mesh-gatewayroutehostnamematch-structure
- name: Amazon App Mesh Gatewayroutehostnamerewrite Structure
  property_count: 0
  slug: amazon-app-mesh-gatewayroutehostnamerewrite-structure
- name: Amazon App Mesh Gatewayroutelist Structure
  property_count: 0
  slug: amazon-app-mesh-gatewayroutelist-structure
- name: Amazon App Mesh Gatewayroutepriority Structure
  property_count: 0
  slug: amazon-app-mesh-gatewayroutepriority-structure
- name: Amazon App Mesh Gatewayrouteref Structure
  property_count: 0
  slug: amazon-app-mesh-gatewayrouteref-structure
- name: Amazon App Mesh Gatewayroutespec Structure
  property_count: 0
  slug: amazon-app-mesh-gatewayroutespec-structure
- name: Amazon App Mesh Gatewayroutestatus Structure
  property_count: 0
  slug: amazon-app-mesh-gatewayroutestatus-structure
- name: Amazon App Mesh Gatewayroutestatuscode Structure
  property_count: 0
  slug: amazon-app-mesh-gatewayroutestatuscode-structure
- name: Amazon App Mesh Gatewayroutetarget Structure
  property_count: 0
  slug: amazon-app-mesh-gatewayroutetarget-structure
- name: Amazon App Mesh Gatewayroutevirtualservice Structure
  property_count: 0
  slug: amazon-app-mesh-gatewayroutevirtualservice-structure
- name: Amazon App Mesh Grpcgatewayroute Structure
  property_count: 0
  slug: amazon-app-mesh-grpcgatewayroute-structure
- name: Amazon App Mesh Grpcgatewayrouteaction Structure
  property_count: 0
  slug: amazon-app-mesh-grpcgatewayrouteaction-structure
- name: Amazon App Mesh Grpcgatewayroutematch Structure
  property_count: 0
  slug: amazon-app-mesh-grpcgatewayroutematch-structure
- name: Amazon App Mesh Grpcgatewayroutemetadata Structure
  property_count: 0
  slug: amazon-app-mesh-grpcgatewayroutemetadata-structure
- name: Amazon App Mesh Grpcgatewayroutemetadatalist Structure
  property_count: 0
  slug: amazon-app-mesh-grpcgatewayroutemetadatalist-structure
- name: Amazon App Mesh Grpcgatewayrouterewrite Structure
  property_count: 0
  slug: amazon-app-mesh-grpcgatewayrouterewrite-structure
- name: Amazon App Mesh Grpcmetadatamatchmethod Structure
  property_count: 0
  slug: amazon-app-mesh-grpcmetadatamatchmethod-structure
- name: Amazon App Mesh Grpcretrypolicy Structure
  property_count: 0
  slug: amazon-app-mesh-grpcretrypolicy-structure
- name: Amazon App Mesh Grpcretrypolicyevent Structure
  property_count: 0
  slug: amazon-app-mesh-grpcretrypolicyevent-structure
- name: Amazon App Mesh Grpcretrypolicyevents Structure
  property_count: 0
  slug: amazon-app-mesh-grpcretrypolicyevents-structure
- name: Amazon App Mesh Grpcroute Structure
  property_count: 0
  slug: amazon-app-mesh-grpcroute-structure
- name: Amazon App Mesh Grpcrouteaction Structure
  property_count: 0
  slug: amazon-app-mesh-grpcrouteaction-structure
- name: Amazon App Mesh Grpcroutematch Structure
  property_count: 0
  slug: amazon-app-mesh-grpcroutematch-structure
- name: Amazon App Mesh Grpcroutemetadata Structure
  property_count: 0
  slug: amazon-app-mesh-grpcroutemetadata-structure
- name: Amazon App Mesh Grpcroutemetadatalist Structure
  property_count: 0
  slug: amazon-app-mesh-grpcroutemetadatalist-structure
- name: Amazon App Mesh Grpcroutemetadatamatchmethod Structure
  property_count: 0
  slug: amazon-app-mesh-grpcroutemetadatamatchmethod-structure
- name: Amazon App Mesh Grpctimeout Structure
  property_count: 0
  slug: amazon-app-mesh-grpctimeout-structure
- name: Amazon App Mesh Headermatch Structure
  property_count: 0
  slug: amazon-app-mesh-headermatch-structure
- name: Amazon App Mesh Headermatchmethod Structure
  property_count: 0
  slug: amazon-app-mesh-headermatchmethod-structure
- name: Amazon App Mesh Headername Structure
  property_count: 0
  slug: amazon-app-mesh-headername-structure
- name: Amazon App Mesh Healthcheckintervalmillis Structure
  property_count: 0
  slug: amazon-app-mesh-healthcheckintervalmillis-structure
- name: Amazon App Mesh Healthcheckpolicy Structure
  property_count: 0
  slug: amazon-app-mesh-healthcheckpolicy-structure
- name: Amazon App Mesh Healthcheckthreshold Structure
  property_count: 0
  slug: amazon-app-mesh-healthcheckthreshold-structure
- name: Amazon App Mesh Healthchecktimeoutmillis Structure
  property_count: 0
  slug: amazon-app-mesh-healthchecktimeoutmillis-structure
- name: Amazon App Mesh Hostname Structure
  property_count: 0
  slug: amazon-app-mesh-hostname-structure
- name: Amazon App Mesh Httpgatewayroute Structure
  property_count: 0
  slug: amazon-app-mesh-httpgatewayroute-structure
- name: Amazon App Mesh Httpgatewayrouteaction Structure
  property_count: 0
  slug: amazon-app-mesh-httpgatewayrouteaction-structure
- name: Amazon App Mesh Httpgatewayrouteheader Structure
  property_count: 0
  slug: amazon-app-mesh-httpgatewayrouteheader-structure
- name: Amazon App Mesh Httpgatewayrouteheaders Structure
  property_count: 0
  slug: amazon-app-mesh-httpgatewayrouteheaders-structure
- name: Amazon App Mesh Httpgatewayroutematch Structure
  property_count: 0
  slug: amazon-app-mesh-httpgatewayroutematch-structure
- name: Amazon App Mesh Httpgatewayroutepathrewrite Structure
  property_count: 0
  slug: amazon-app-mesh-httpgatewayroutepathrewrite-structure
- name: Amazon App Mesh Httpgatewayrouteprefix Structure
  property_count: 0
  slug: amazon-app-mesh-httpgatewayrouteprefix-structure
- name: Amazon App Mesh Httpgatewayrouteprefixrewrite Structure
  property_count: 0
  slug: amazon-app-mesh-httpgatewayrouteprefixrewrite-structure
- name: Amazon App Mesh Httpgatewayrouterewrite Structure
  property_count: 0
  slug: amazon-app-mesh-httpgatewayrouterewrite-structure
- name: Amazon App Mesh Httpmethod Structure
  property_count: 0
  slug: amazon-app-mesh-httpmethod-structure
- name: Amazon App Mesh Httppathexact Structure
  property_count: 0
  slug: amazon-app-mesh-httppathexact-structure
- name: Amazon App Mesh Httppathmatch Structure
  property_count: 0
  slug: amazon-app-mesh-httppathmatch-structure
- name: Amazon App Mesh Httppathregex Structure
  property_count: 0
  slug: amazon-app-mesh-httppathregex-structure
- name: Amazon App Mesh Httpqueryparameter Structure
  property_count: 0
  slug: amazon-app-mesh-httpqueryparameter-structure
- name: Amazon App Mesh Httpqueryparameters Structure
  property_count: 0
  slug: amazon-app-mesh-httpqueryparameters-structure
- name: Amazon App Mesh Httpretrypolicy Structure
  property_count: 0
  slug: amazon-app-mesh-httpretrypolicy-structure
- name: Amazon App Mesh Httpretrypolicyevent Structure
  property_count: 0
  slug: amazon-app-mesh-httpretrypolicyevent-structure
- name: Amazon App Mesh Httpretrypolicyevents Structure
  property_count: 0
  slug: amazon-app-mesh-httpretrypolicyevents-structure
- name: Amazon App Mesh Httproute Structure
  property_count: 0
  slug: amazon-app-mesh-httproute-structure
- name: Amazon App Mesh Httprouteaction Structure
  property_count: 0
  slug: amazon-app-mesh-httprouteaction-structure
- name: Amazon App Mesh Httprouteheader Structure
  property_count: 0
  slug: amazon-app-mesh-httprouteheader-structure
- name: Amazon App Mesh Httprouteheaders Structure
  property_count: 0
  slug: amazon-app-mesh-httprouteheaders-structure
- name: Amazon App Mesh Httproutematch Structure
  property_count: 0
  slug: amazon-app-mesh-httproutematch-structure
- name: Amazon App Mesh Httpscheme Structure
  property_count: 0
  slug: amazon-app-mesh-httpscheme-structure
- name: Amazon App Mesh Httptimeout Structure
  property_count: 0
  slug: amazon-app-mesh-httptimeout-structure
- name: Amazon App Mesh Ippreference Structure
  property_count: 0
  slug: amazon-app-mesh-ippreference-structure
- name: Amazon App Mesh Jsonformat Structure
  property_count: 0
  slug: amazon-app-mesh-jsonformat-structure
- name: Amazon App Mesh Jsonformatref Structure
  property_count: 0
  slug: amazon-app-mesh-jsonformatref-structure
- name: Amazon App Mesh Jsonkey Structure
  property_count: 0
  slug: amazon-app-mesh-jsonkey-structure
- name: Amazon App Mesh Jsonvalue Structure
  property_count: 0
  slug: amazon-app-mesh-jsonvalue-structure
- name: Amazon App Mesh Listener Structure
  property_count: 0
  slug: amazon-app-mesh-listener-structure
- name: Amazon App Mesh Listenerport Structure
  property_count: 0
  slug: amazon-app-mesh-listenerport-structure
- name: Amazon App Mesh Listeners Structure
  property_count: 0
  slug: amazon-app-mesh-listeners-structure
- name: Amazon App Mesh Listenertimeout Structure
  property_count: 0
  slug: amazon-app-mesh-listenertimeout-structure
- name: Amazon App Mesh Listenertls Structure
  property_count: 0
  slug: amazon-app-mesh-listenertls-structure
- name: Amazon App Mesh Listenertlsacmcertificate Structure
  property_count: 0
  slug: amazon-app-mesh-listenertlsacmcertificate-structure
- name: Amazon App Mesh Listenertlscertificate Structure
  property_count: 0
  slug: amazon-app-mesh-listenertlscertificate-structure
- name: Amazon App Mesh Listenertlsfilecertificate Structure
  property_count: 0
  slug: amazon-app-mesh-listenertlsfilecertificate-structure
- name: Amazon App Mesh Listenertlsmode Structure
  property_count: 0
  slug: amazon-app-mesh-listenertlsmode-structure
- name: Amazon App Mesh Listenertlssdscertificate Structure
  property_count: 0
  slug: amazon-app-mesh-listenertlssdscertificate-structure
- name: Amazon App Mesh Listenertlsvalidationcontext Structure
  property_count: 0
  slug: amazon-app-mesh-listenertlsvalidationcontext-structure
- name: Amazon App Mesh Listenertlsvalidationcontexttrust Structure
  property_count: 0
  slug: amazon-app-mesh-listenertlsvalidationcontexttrust-structure
- name: Amazon App Mesh Listgatewayroutesinput Structure
  property_count: 0
  slug: amazon-app-mesh-listgatewayroutesinput-structure
- name: Amazon App Mesh Listgatewayrouteslimit Structure
  property_count: 0
  slug: amazon-app-mesh-listgatewayrouteslimit-structure
- name: Amazon App Mesh Listgatewayroutesoutput Structure
  property_count: 0
  slug: amazon-app-mesh-listgatewayroutesoutput-structure
- name: Amazon App Mesh Listmeshesinput Structure
  property_count: 0
  slug: amazon-app-mesh-listmeshesinput-structure
- name: Amazon App Mesh Listmesheslimit Structure
  property_count: 0
  slug: amazon-app-mesh-listmesheslimit-structure
- name: Amazon App Mesh Listmeshesoutput Structure
  property_count: 0
  slug: amazon-app-mesh-listmeshesoutput-structure
- name: Amazon App Mesh Listroutesinput Structure
  property_count: 0
  slug: amazon-app-mesh-listroutesinput-structure
- name: Amazon App Mesh Listrouteslimit Structure
  property_count: 0
  slug: amazon-app-mesh-listrouteslimit-structure
- name: Amazon App Mesh Listroutesoutput Structure
  property_count: 0
  slug: amazon-app-mesh-listroutesoutput-structure
- name: Amazon App Mesh Listtagsforresourceinput Structure
  property_count: 0
  slug: amazon-app-mesh-listtagsforresourceinput-structure
- name: Amazon App Mesh Listtagsforresourceoutput Structure
  property_count: 0
  slug: amazon-app-mesh-listtagsforresourceoutput-structure
- name: Amazon App Mesh Listvirtualgatewaysinput Structure
  property_count: 0
  slug: amazon-app-mesh-listvirtualgatewaysinput-structure
- name: Amazon App Mesh Listvirtualgatewayslimit Structure
  property_count: 0
  slug: amazon-app-mesh-listvirtualgatewayslimit-structure
- name: Amazon App Mesh Listvirtualgatewaysoutput Structure
  property_count: 0
  slug: amazon-app-mesh-listvirtualgatewaysoutput-structure
- name: Amazon App Mesh Listvirtualnodesinput Structure
  property_count: 0
  slug: amazon-app-mesh-listvirtualnodesinput-structure
- name: Amazon App Mesh Listvirtualnodeslimit Structure
  property_count: 0
  slug: amazon-app-mesh-listvirtualnodeslimit-structure
- name: Amazon App Mesh Listvirtualnodesoutput Structure
  property_count: 0
  slug: amazon-app-mesh-listvirtualnodesoutput-structure
- name: Amazon App Mesh Listvirtualroutersinput Structure
  property_count: 0
  slug: amazon-app-mesh-listvirtualroutersinput-structure
- name: Amazon App Mesh Listvirtualrouterslimit Structure
  property_count: 0
  slug: amazon-app-mesh-listvirtualrouterslimit-structure
- name: Amazon App Mesh Listvirtualroutersoutput Structure
  property_count: 0
  slug: amazon-app-mesh-listvirtualroutersoutput-structure
- name: Amazon App Mesh Listvirtualservicesinput Structure
  property_count: 0
  slug: amazon-app-mesh-listvirtualservicesinput-structure
- name: Amazon App Mesh Listvirtualserviceslimit Structure
  property_count: 0
  slug: amazon-app-mesh-listvirtualserviceslimit-structure
- name: Amazon App Mesh Listvirtualservicesoutput Structure
  property_count: 0
  slug: amazon-app-mesh-listvirtualservicesoutput-structure
- name: Amazon App Mesh Logging Structure
  property_count: 0
  slug: amazon-app-mesh-logging-structure
- name: Amazon App Mesh Loggingformat Structure
  property_count: 0
  slug: amazon-app-mesh-loggingformat-structure
- name: Amazon App Mesh Long Structure
  property_count: 0
  slug: amazon-app-mesh-long-structure
- name: Amazon App Mesh Matchrange Structure
  property_count: 0
  slug: amazon-app-mesh-matchrange-structure
- name: Amazon App Mesh Maxconnections Structure
  property_count: 0
  slug: amazon-app-mesh-maxconnections-structure
- name: Amazon App Mesh Maxpendingrequests Structure
  property_count: 0
  slug: amazon-app-mesh-maxpendingrequests-structure
- name: Amazon App Mesh Maxrequests Structure
  property_count: 0
  slug: amazon-app-mesh-maxrequests-structure
- name: Amazon App Mesh Maxretries Structure
  property_count: 0
  slug: amazon-app-mesh-maxretries-structure
- name: Amazon App Mesh Meshdata Structure
  property_count: 0
  slug: amazon-app-mesh-meshdata-structure
- name: Amazon App Mesh Meshlist Structure
  property_count: 0
  slug: amazon-app-mesh-meshlist-structure
- name: Amazon App Mesh Meshref Structure
  property_count: 0
  slug: amazon-app-mesh-meshref-structure
- name: Amazon App Mesh Meshservicediscovery Structure
  property_count: 0
  slug: amazon-app-mesh-meshservicediscovery-structure
- name: Amazon App Mesh Meshspec Structure
  property_count: 0
  slug: amazon-app-mesh-meshspec-structure
- name: Amazon App Mesh Meshstatus Structure
  property_count: 0
  slug: amazon-app-mesh-meshstatus-structure
- name: Amazon App Mesh Meshstatuscode Structure
  property_count: 0
  slug: amazon-app-mesh-meshstatuscode-structure
- name: Amazon App Mesh Methodname Structure
  property_count: 0
  slug: amazon-app-mesh-methodname-structure
- name: Amazon App Mesh Outlierdetection Structure
  property_count: 0
  slug: amazon-app-mesh-outlierdetection-structure
- name: Amazon App Mesh Outlierdetectionmaxejectionpercent Structure
  property_count: 0
  slug: amazon-app-mesh-outlierdetectionmaxejectionpercent-structure
- name: Amazon App Mesh Outlierdetectionmaxservererrors Structure
  property_count: 0
  slug: amazon-app-mesh-outlierdetectionmaxservererrors-structure
- name: Amazon App Mesh Percentint Structure
  property_count: 0
  slug: amazon-app-mesh-percentint-structure
- name: Amazon App Mesh Portmapping Structure
  property_count: 0
  slug: amazon-app-mesh-portmapping-structure
- name: Amazon App Mesh Portnumber Structure
  property_count: 0
  slug: amazon-app-mesh-portnumber-structure
- name: Amazon App Mesh Portprotocol Structure
  property_count: 0
  slug: amazon-app-mesh-portprotocol-structure
- name: Amazon App Mesh Portset Structure
  property_count: 0
  slug: amazon-app-mesh-portset-structure
- name: Amazon App Mesh Queryparametermatch Structure
  property_count: 0
  slug: amazon-app-mesh-queryparametermatch-structure
- name: Amazon App Mesh Queryparametername Structure
  property_count: 0
  slug: amazon-app-mesh-queryparametername-structure
- name: Amazon App Mesh Resourcemetadata Structure
  property_count: 0
  slug: amazon-app-mesh-resourcemetadata-structure
- name: Amazon App Mesh Resourcename Structure
  property_count: 0
  slug: amazon-app-mesh-resourcename-structure
- name: Amazon App Mesh Routedata Structure
  property_count: 0
  slug: amazon-app-mesh-routedata-structure
- name: Amazon App Mesh Routelist Structure
  property_count: 0
  slug: amazon-app-mesh-routelist-structure
- name: Amazon App Mesh Routepriority Structure
  property_count: 0
  slug: amazon-app-mesh-routepriority-structure
- name: Amazon App Mesh Routeref Structure
  property_count: 0
  slug: amazon-app-mesh-routeref-structure
- name: Amazon App Mesh Routespec Structure
  property_count: 0
  slug: amazon-app-mesh-routespec-structure
- name: Amazon App Mesh Routestatus Structure
  property_count: 0
  slug: amazon-app-mesh-routestatus-structure
- name: Amazon App Mesh Routestatuscode Structure
  property_count: 0
  slug: amazon-app-mesh-routestatuscode-structure
- name: Amazon App Mesh Sdssecretname Structure
  property_count: 0
  slug: amazon-app-mesh-sdssecretname-structure
- name: Amazon App Mesh Servicediscovery Structure
  property_count: 0
  slug: amazon-app-mesh-servicediscovery-structure
- name: Amazon App Mesh Servicename Structure
  property_count: 0
  slug: amazon-app-mesh-servicename-structure
- name: Amazon App Mesh String Structure
  property_count: 0
  slug: amazon-app-mesh-string-structure
- name: Amazon App Mesh Subjectalternativename Structure
  property_count: 0
  slug: amazon-app-mesh-subjectalternativename-structure
- name: Amazon App Mesh Subjectalternativenamelist Structure
  property_count: 0
  slug: amazon-app-mesh-subjectalternativenamelist-structure
- name: Amazon App Mesh Subjectalternativenamematchers Structure
  property_count: 0
  slug: amazon-app-mesh-subjectalternativenamematchers-structure
- name: Amazon App Mesh Subjectalternativenames Structure
  property_count: 0
  slug: amazon-app-mesh-subjectalternativenames-structure
- name: Amazon App Mesh Suffixhostname Structure
  property_count: 0
  slug: amazon-app-mesh-suffixhostname-structure
- name: Amazon App Mesh Tagkey Structure
  property_count: 0
  slug: amazon-app-mesh-tagkey-structure
- name: Amazon App Mesh Tagkeylist Structure
  property_count: 0
  slug: amazon-app-mesh-tagkeylist-structure
- name: Amazon App Mesh Taglist Structure
  property_count: 0
  slug: amazon-app-mesh-taglist-structure
- name: Amazon App Mesh Tagref Structure
  property_count: 0
  slug: amazon-app-mesh-tagref-structure
- name: Amazon App Mesh Tagresourceinput Structure
  property_count: 0
  slug: amazon-app-mesh-tagresourceinput-structure
- name: Amazon App Mesh Tagresourceoutput Structure
  property_count: 0
  slug: amazon-app-mesh-tagresourceoutput-structure
- name: Amazon App Mesh Tagslimit Structure
  property_count: 0
  slug: amazon-app-mesh-tagslimit-structure
- name: Amazon App Mesh Tagvalue Structure
  property_count: 0
  slug: amazon-app-mesh-tagvalue-structure
- name: Amazon App Mesh Tcpretrypolicyevent Structure
  property_count: 0
  slug: amazon-app-mesh-tcpretrypolicyevent-structure
- name: Amazon App Mesh Tcpretrypolicyevents Structure
  property_count: 0
  slug: amazon-app-mesh-tcpretrypolicyevents-structure
- name: Amazon App Mesh Tcproute Structure
  property_count: 0
  slug: amazon-app-mesh-tcproute-structure
- name: Amazon App Mesh Tcprouteaction Structure
  property_count: 0
  slug: amazon-app-mesh-tcprouteaction-structure
- name: Amazon App Mesh Tcproutematch Structure
  property_count: 0
  slug: amazon-app-mesh-tcproutematch-structure
- name: Amazon App Mesh Tcptimeout Structure
  property_count: 0
  slug: amazon-app-mesh-tcptimeout-structure
- name: Amazon App Mesh Textformat Structure
  property_count: 0
  slug: amazon-app-mesh-textformat-structure
- name: Amazon App Mesh Timestamp Structure
  property_count: 0
  slug: amazon-app-mesh-timestamp-structure
- name: Amazon App Mesh Tlsvalidationcontext Structure
  property_count: 0
  slug: amazon-app-mesh-tlsvalidationcontext-structure
- name: Amazon App Mesh Tlsvalidationcontextacmtrust Structure
  property_count: 0
  slug: amazon-app-mesh-tlsvalidationcontextacmtrust-structure
- name: Amazon App Mesh Tlsvalidationcontextfiletrust Structure
  property_count: 0
  slug: amazon-app-mesh-tlsvalidationcontextfiletrust-structure
- name: Amazon App Mesh Tlsvalidationcontextsdstrust Structure
  property_count: 0
  slug: amazon-app-mesh-tlsvalidationcontextsdstrust-structure
- name: Amazon App Mesh Tlsvalidationcontexttrust Structure
  property_count: 0
  slug: amazon-app-mesh-tlsvalidationcontexttrust-structure
- name: Amazon App Mesh Untagresourceinput Structure
  property_count: 0
  slug: amazon-app-mesh-untagresourceinput-structure
- name: Amazon App Mesh Untagresourceoutput Structure
  property_count: 0
  slug: amazon-app-mesh-untagresourceoutput-structure
- name: Amazon App Mesh Updategatewayrouteinput Structure
  property_count: 0
  slug: amazon-app-mesh-updategatewayrouteinput-structure
- name: Amazon App Mesh Updategatewayrouteoutput Structure
  property_count: 0
  slug: amazon-app-mesh-updategatewayrouteoutput-structure
- name: Amazon App Mesh Updatemeshinput Structure
  property_count: 0
  slug: amazon-app-mesh-updatemeshinput-structure
- name: Amazon App Mesh Updatemeshoutput Structure
  property_count: 0
  slug: amazon-app-mesh-updatemeshoutput-structure
- name: Amazon App Mesh Updaterouteinput Structure
  property_count: 0
  slug: amazon-app-mesh-updaterouteinput-structure
- name: Amazon App Mesh Updaterouteoutput Structure
  property_count: 0
  slug: amazon-app-mesh-updaterouteoutput-structure
- name: Amazon App Mesh Updatevirtualgatewayinput Structure
  property_count: 0
  slug: amazon-app-mesh-updatevirtualgatewayinput-structure
- name: Amazon App Mesh Updatevirtualgatewayoutput Structure
  property_count: 0
  slug: amazon-app-mesh-updatevirtualgatewayoutput-structure
- name: Amazon App Mesh Updatevirtualnodeinput Structure
  property_count: 0
  slug: amazon-app-mesh-updatevirtualnodeinput-structure
- name: Amazon App Mesh Updatevirtualnodeoutput Structure
  property_count: 0
  slug: amazon-app-mesh-updatevirtualnodeoutput-structure
- name: Amazon App Mesh Updatevirtualrouterinput Structure
  property_count: 0
  slug: amazon-app-mesh-updatevirtualrouterinput-structure
- name: Amazon App Mesh Updatevirtualrouteroutput Structure
  property_count: 0
  slug: amazon-app-mesh-updatevirtualrouteroutput-structure
- name: Amazon App Mesh Updatevirtualserviceinput Structure
  property_count: 0
  slug: amazon-app-mesh-updatevirtualserviceinput-structure
- name: Amazon App Mesh Updatevirtualserviceoutput Structure
  property_count: 0
  slug: amazon-app-mesh-updatevirtualserviceoutput-structure
- name: Amazon App Mesh Virtualgatewayaccesslog Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayaccesslog-structure
- name: Amazon App Mesh Virtualgatewaybackenddefaults Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaybackenddefaults-structure
- name: Amazon App Mesh Virtualgatewaycertificateauthorityarns Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaycertificateauthorityarns-structure
- name: Amazon App Mesh Virtualgatewayclientpolicy Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayclientpolicy-structure
- name: Amazon App Mesh Virtualgatewayclientpolicytls Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayclientpolicytls-structure
- name: Amazon App Mesh Virtualgatewayclienttlscertificate Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayclienttlscertificate-structure
- name: Amazon App Mesh Virtualgatewayconnectionpool Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayconnectionpool-structure
- name: Amazon App Mesh Virtualgatewaydata Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaydata-structure
- name: Amazon App Mesh Virtualgatewayfileaccesslog Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayfileaccesslog-structure
- name: Amazon App Mesh Virtualgatewaygrpcconnectionpool Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaygrpcconnectionpool-structure
- name: Amazon App Mesh Virtualgatewayhealthcheckintervalmillis Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayhealthcheckintervalmillis-structure
- name: Amazon App Mesh Virtualgatewayhealthcheckpolicy Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayhealthcheckpolicy-structure
- name: Amazon App Mesh Virtualgatewayhealthcheckthreshold Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayhealthcheckthreshold-structure
- name: Amazon App Mesh Virtualgatewayhealthchecktimeoutmillis Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayhealthchecktimeoutmillis-structure
- name: Amazon App Mesh Virtualgatewayhttp2Connectionpool Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayhttp2connectionpool-structure
- name: Amazon App Mesh Virtualgatewayhttpconnectionpool Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayhttpconnectionpool-structure
- name: Amazon App Mesh Virtualgatewaylist Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylist-structure
- name: Amazon App Mesh Virtualgatewaylistener Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylistener-structure
- name: Amazon App Mesh Virtualgatewaylisteners Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylisteners-structure
- name: Amazon App Mesh Virtualgatewaylistenertls Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylistenertls-structure
- name: Amazon App Mesh Virtualgatewaylistenertlsacmcertificate Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylistenertlsacmcertificate-structure
- name: Amazon App Mesh Virtualgatewaylistenertlscertificate Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylistenertlscertificate-structure
- name: Amazon App Mesh Virtualgatewaylistenertlsfilecertificate Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylistenertlsfilecertificate-structure
- name: Amazon App Mesh Virtualgatewaylistenertlsmode Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylistenertlsmode-structure
- name: Amazon App Mesh Virtualgatewaylistenertlssdscertificate Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylistenertlssdscertificate-structure
- name: Amazon App Mesh Virtualgatewaylistenertlsvalidationcontext Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylistenertlsvalidationcontext-structure
- name: Amazon App Mesh Virtualgatewaylistenertlsvalidationcontexttrust Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylistenertlsvalidationcontexttrust-structure
- name: Amazon App Mesh Virtualgatewaylogging Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaylogging-structure
- name: Amazon App Mesh Virtualgatewayportmapping Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayportmapping-structure
- name: Amazon App Mesh Virtualgatewayportprotocol Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayportprotocol-structure
- name: Amazon App Mesh Virtualgatewayref Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayref-structure
- name: Amazon App Mesh Virtualgatewaysdssecretname Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaysdssecretname-structure
- name: Amazon App Mesh Virtualgatewayspec Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewayspec-structure
- name: Amazon App Mesh Virtualgatewaystatus Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaystatus-structure
- name: Amazon App Mesh Virtualgatewaystatuscode Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaystatuscode-structure
- name: Amazon App Mesh Virtualgatewaytlsvalidationcontext Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontext-structure
- name: Amazon App Mesh Virtualgatewaytlsvalidationcontextacmtrust Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontextacmtrust-structure
- name: Amazon App Mesh Virtualgatewaytlsvalidationcontextfiletrust Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontextfiletrust-structure
- name: Amazon App Mesh Virtualgatewaytlsvalidationcontextsdstrust Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontextsdstrust-structure
- name: Amazon App Mesh Virtualgatewaytlsvalidationcontexttrust Structure
  property_count: 0
  slug: amazon-app-mesh-virtualgatewaytlsvalidationcontexttrust-structure
- name: Amazon App Mesh Virtualnodeconnectionpool Structure
  property_count: 0
  slug: amazon-app-mesh-virtualnodeconnectionpool-structure
- name: Amazon App Mesh Virtualnodedata Structure
  property_count: 0
  slug: amazon-app-mesh-virtualnodedata-structure
- name: Amazon App Mesh Virtualnodegrpcconnectionpool Structure
  property_count: 0
  slug: amazon-app-mesh-virtualnodegrpcconnectionpool-structure
- name: Amazon App Mesh Virtualnodehttp2Connectionpool Structure
  property_count: 0
  slug: amazon-app-mesh-virtualnodehttp2connectionpool-structure
- name: Amazon App Mesh Virtualnodehttpconnectionpool Structure
  property_count: 0
  slug: amazon-app-mesh-virtualnodehttpconnectionpool-structure
- name: Amazon App Mesh Virtualnodelist Structure
  property_count: 0
  slug: amazon-app-mesh-virtualnodelist-structure
- name: Amazon App Mesh Virtualnoderef Structure
  property_count: 0
  slug: amazon-app-mesh-virtualnoderef-structure
- name: Amazon App Mesh Virtualnodeserviceprovider Structure
  property_count: 0
  slug: amazon-app-mesh-virtualnodeserviceprovider-structure
- name: Amazon App Mesh Virtualnodespec Structure
  property_count: 0
  slug: amazon-app-mesh-virtualnodespec-structure
- name: Amazon App Mesh Virtualnodestatus Structure
  property_count: 0
  slug: amazon-app-mesh-virtualnodestatus-structure
- name: Amazon App Mesh Virtualnodestatuscode Structure
  property_count: 0
  slug: amazon-app-mesh-virtualnodestatuscode-structure
- name: Amazon App Mesh Virtualnodetcpconnectionpool Structure
  property_count: 0
  slug: amazon-app-mesh-virtualnodetcpconnectionpool-structure
- name: Amazon App Mesh Virtualrouterdata Structure
  property_count: 0
  slug: amazon-app-mesh-virtualrouterdata-structure
- name: Amazon App Mesh Virtualrouterlist Structure
  property_count: 0
  slug: amazon-app-mesh-virtualrouterlist-structure
- name: Amazon App Mesh Virtualrouterlistener Structure
  property_count: 0
  slug: amazon-app-mesh-virtualrouterlistener-structure
- name: Amazon App Mesh Virtualrouterlisteners Structure
  property_count: 0
  slug: amazon-app-mesh-virtualrouterlisteners-structure
- name: Amazon App Mesh Virtualrouterref Structure
  property_count: 0
  slug: amazon-app-mesh-virtualrouterref-structure
- name: Amazon App Mesh Virtualrouterserviceprovider Structure
  property_count: 0
  slug: amazon-app-mesh-virtualrouterserviceprovider-structure
- name: Amazon App Mesh Virtualrouterspec Structure
  property_count: 0
  slug: amazon-app-mesh-virtualrouterspec-structure
- name: Amazon App Mesh Virtualrouterstatus Structure
  property_count: 0
  slug: amazon-app-mesh-virtualrouterstatus-structure
- name: Amazon App Mesh Virtualrouterstatuscode Structure
  property_count: 0
  slug: amazon-app-mesh-virtualrouterstatuscode-structure
- name: Amazon App Mesh Virtualservicebackend Structure
  property_count: 0
  slug: amazon-app-mesh-virtualservicebackend-structure
- name: Amazon App Mesh Virtualservicedata Structure
  property_count: 0
  slug: amazon-app-mesh-virtualservicedata-structure
- name: Amazon App Mesh Virtualservicelist Structure
  property_count: 0
  slug: amazon-app-mesh-virtualservicelist-structure
- name: Amazon App Mesh Virtualserviceprovider Structure
  property_count: 0
  slug: amazon-app-mesh-virtualserviceprovider-structure
- name: Amazon App Mesh Virtualserviceref Structure
  property_count: 0
  slug: amazon-app-mesh-virtualserviceref-structure
- name: Amazon App Mesh Virtualservicespec Structure
  property_count: 0
  slug: amazon-app-mesh-virtualservicespec-structure
- name: Amazon App Mesh Virtualservicestatus Structure
  property_count: 0
  slug: amazon-app-mesh-virtualservicestatus-structure
- name: Amazon App Mesh Virtualservicestatuscode Structure
  property_count: 0
  slug: amazon-app-mesh-virtualservicestatuscode-structure
- name: Amazon App Mesh Weightedtarget Structure
  property_count: 0
  slug: amazon-app-mesh-weightedtarget-structure
- name: Amazon App Mesh Weightedtargets Structure
  property_count: 0
  slug: amazon-app-mesh-weightedtargets-structure
jsonld:
- class_count: 0
  name: Amazon App Mesh Context
  property_count: 1
  slug: amazon-app-mesh-context
layout: provider
modified: '2026-06-20'
name: Amazon App Mesh
nav: Providers
network: true
overview: 'Amazon App Mesh publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Meshes API, Tag#resourceArn API, Tags#resourceArn API, and 1 more. Tagged areas include Microservices, Networking, and Service Mesh.


  The Amazon App Mesh catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon App Mesh''s developer surface includes authentication, developer portal, documentation, support, developer console, signup flow, status page, and 16 more developer resources.'
random_paper: 28
rules:
- name: Amazon App Mesh API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-app-mesh-jsonschema-spectral-rules
- name: Amazon App Mesh API Rules
  rule_count: 12
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 8
  slug: amazon-app-mesh-spectral-rules
score:
  band: developing
  composite: 50.9
  delta: -0.5
  facets:
    commercial_clarity: 42.1
    contract_quality: 67.8
    developer_ergonomics: 39.1
    discoverability: 74.1
    governance: 80.2
    operational_transparency: 5.3
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-app-mesh/refs/heads/main/screenshots/amazon-app-mesh-2026-07-25T195916.png
security:
- kind: authentication
  name: Amazon App Mesh Authentication
  slug: amazon-app-mesh-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon App Mesh Domain Security
  slug: amazon-app-mesh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon App Mesh Vulnerability Disclosure
  slug: amazon-app-mesh-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon App Mesh Trust Center
  slug: amazon-app-mesh-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-app-mesh
tags:
- Microservices
- Networking
- Service Mesh
use_cases:
- description: Control traffic routing between microservices with weighted routing, canary deployments, and circuit breaking.
  name: Microservices Traffic Management
- description: Integrate App Mesh with AWS Cloud Map for automatic service discovery across compute types.
  name: Service Discovery Integration
- description: Connect services running on ECS, EKS, and EC2 instances within a unified service mesh for consistent networking policies.
  name: Multi-Cluster Networking
website: https://aws.amazon.com/app-mesh/
---
