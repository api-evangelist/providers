---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.1
  scored_at: '2026-09-04'
api_count: 34
apis:
- description: KPN Grip is a KPN identity and access management solution that acts as a central identity hub, letting developers integrate user registration, authentication and authorization (SAML 2.0, OpenID Connec
  name: KPN GRIP API
  slug: kpn-grip
- description: KPN PiM ID generates tamper-proof, company-specific encrypted QR codes from validated customer data (POST /image on https://api-prd.kpn.com/kpn/qrcodegenerator). The codes are embedded in surfaces suc
  name: KPN PIM ID API
  slug: kpn-pim-id
- description: Send and schedule bulk SMS campaigns over the KPN network. Documented on the KPN Developer portal; no public OpenAPI definition was found for this product on KPN's SwaggerHub organisation as of the ha
  name: KPN SMS Campaigns API
  slug: kpn-sms-campaigns
- description: Converts inbound email into SMS messages delivered over the KPN network. Documented on the KPN Developer portal; no public OpenAPI definition was found for this product on KPN's SwaggerHub organisatio
  name: KPN Email-to-SMS API
  slug: kpn-email-to-sms
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: number management from accounts
  name: KPN Account API
  slug: kpn-account-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Activation API from KPN — 1 operation(s) for activation.
  name: KPN Activation API
  slug: kpn-activation-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Alarm operations provide the ability to retrieve and acknowledge ThingPark device and base station alarms.
  name: KPN Alarm API
  slug: kpn-alarm-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The appliance.configure API from KPN — 51 operation(s) for appliance.configure.
  name: KPN Appliance.configure API
  slug: kpn-appliance-configure-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The appliance.monitor API from KPN — 13 operation(s) for appliance.monitor.
  name: KPN Appliance.monitor API
  slug: kpn-appliance-monitor-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Application-scope webhook configuration — webhook URL and field exclusions. Highest precedence — overrides both team and organization config for this specific application.
  name: KPN Application API
  slug: kpn-application-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Signing keys at application scope. Highest precedence — overrides both team and org keys for deliveries belonging to this specific application.
  name: KPN Application Keys API
  slug: kpn-application-keys-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Application related resource management
  name: KPN Applications API
  slug: kpn-applications-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Attachment API from KPN — 1 operation(s) for attachment.
  name: KPN Attachment API
  slug: kpn-attachment-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Authentication endpoints for token management
  name: KPN Authentication API
  slug: kpn-authentication-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Authorization policy enforcement endpoints
  name: KPN Authorization API
  slug: kpn-authorization-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Autologin API from KPN — 1 operation(s) for autologin.
  name: KPN Autologin API
  slug: kpn-autologin-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Callback API from KPN — 1 operation(s) for callback.
  name: KPN Callback API
  slug: kpn-callback-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: All about case handling
  name: KPN Cases API
  slug: kpn-cases-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Logical grouping of content
  name: KPN Catalog API
  slug: kpn-catalog-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The cellularGateway.configure API from KPN — 15 operation(s) for cellulargateway.configure.
  name: KPN Cellular Gateway.configure API
  slug: kpn-cellulargateway-configure-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The cellularGateway.monitor API from KPN — 1 operation(s) for cellulargateway.monitor.
  name: KPN Cellular Gateway.monitor API
  slug: kpn-cellulargateway-monitor-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Config API from KPN — 1 operation(s) for config.
  name: KPN Config API
  slug: kpn-config-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: All about configuring Tracebuzz
  name: KPN Configuration API
  slug: kpn-configuration-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Contract access validation endpoints
  name: KPN Contract Validation API
  slug: kpn-contract-validation-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The DataConsumer API from KPN — 2 operation(s) for dataconsumer.
  name: KPN Data Consumer API
  slug: kpn-dataconsumer-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The DataConsumerDemo API from KPN — 2 operation(s) for dataconsumerdemo.
  name: KPN Data Consumer Demo API
  slug: kpn-dataconsumerdemo-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The default API from KPN — 6 operation(s) for default.
  name: KPN Default API
  slug: kpn-default-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Device operations provide the ability to manage ThingPark devices, device profiles, routing profiles, and connectivity plans.
  name: KPN Device API
  slug: kpn-device-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Devices API from KPN — 1 operation(s) for devices.
  name: KPN Devices API
  slug: kpn-devices-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Device security operations provide the ability to manage AS keys and HSM groups for enhanced message encryption.
  name: KPN Device Security API
  slug: kpn-devicesecurity-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Emailing API from KPN — 1 operation(s) for emailing.
  name: KPN Emailing API
  slug: kpn-emailing-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The endpoint API from KPN — 4 operation(s) for endpoint.
  name: KPN Endpoint API
  slug: kpn-endpoint-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The endpointgroup API from KPN — 1 operation(s) for endpointgroup.
  name: KPN Endpointgroup API
  slug: kpn-endpointgroup-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Events API from KPN — 2 operation(s) for events.
  name: KPN Events API
  slug: kpn-events-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Graphql API from KPN — 1 operation(s) for graphql.
  name: KPN Graphql API
  slug: kpn-graphql-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The identitygroup API from KPN — 1 operation(s) for identitygroup.
  name: KPN Identitygroup API
  slug: kpn-identitygroup-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The insight.configure API from KPN — 3 operation(s) for insight.configure.
  name: KPN Insight.configure API
  slug: kpn-insight-configure-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The insight.monitor API from KPN — 1 operation(s) for insight.monitor.
  name: KPN Insight.monitor API
  slug: kpn-insight-monitor-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Insights API from KPN — 1 operation(s) for insights.
  name: KPN Insights API
  slug: kpn-insights-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The internaluser API from KPN — 1 operation(s) for internaluser.
  name: KPN Internaluser API
  slug: kpn-internaluser-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Detailed descriptions of the content
  name: KPN Item API
  slug: kpn-item-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Call to generate JWT.
  name: KPN JWT API
  slug: kpn-jwt-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Meetings API from KPN — 2 operation(s) for meetings.
  name: KPN Meetings API
  slug: kpn-meetings-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Messages API from KPN — 3 operation(s) for messages.
  name: KPN Messages API
  slug: kpn-messages-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Networks API from KPN — 1 operation(s) for networks.
  name: KPN Networks API
  slug: kpn-networks-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: numbers operations
  name: KPN Number API
  slug: kpn-number-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Organization-scope webhook configuration. Applies to all teams and applications in your organization unless a team or application config overrides it.
  name: KPN Organization API
  slug: kpn-organization-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Signing keys at organization scope. Applied to all webhook deliveries in your organization unless a team or application key overrides them. KPN auto-provisions an organization key on first delivery if
  name: KPN Organization Keys API
  slug: kpn-organization-keys-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Organizations API from KPN — 2 operation(s) for organizations.
  name: KPN Organizations API
  slug: kpn-organizations-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Packages API from KPN — 2 operation(s) for packages.
  name: KPN Packages API
  slug: kpn-packages-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Party and participant management endpoints
  name: KPN Parties API
  slug: kpn-parties-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Personal API from KPN — 3 operation(s) for personal.
  name: KPN Personal API
  slug: kpn-personal-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Polling API from KPN — 1 operation(s) for polling.
  name: KPN Polling API
  slug: kpn-polling-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Register webhook - Demo testing ONLY API from KPN — 1 operation(s) for register webhook - demo testing only.
  name: KPN Register webhook - Demo testing ONLY API
  slug: kpn-register-webhook-demo-testing-only-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Request API from KPN — 2 operation(s) for request.
  name: KPN Request API
  slug: kpn-request-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Address Controller
  name: KPN Rest Address Controller API
  slug: kpn-rest-address-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Block Sim Controller
  name: KPN Rest Block Sim Controller API
  slug: kpn-rest-block-sim-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Business Voice Mail Controller
  name: KPN Rest Business Voice Mail Controller API
  slug: kpn-rest-business-voice-mail-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Contract Controller
  name: KPN Rest Contract Controller API
  slug: kpn-rest-contract-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Contract Terminate Controller
  name: KPN Rest Contract Terminate Controller API
  slug: kpn-rest-contract-terminate-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Contracting Controller
  name: KPN Rest Contracting Controller API
  slug: kpn-rest-contracting-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Hardware Enrollment Controller
  name: KPN Rest Hardware Enrollment Controller API
  slug: kpn-rest-hardware-enrollment-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Hierarchy Controller
  name: KPN Rest Hierarchy Controller API
  slug: kpn-rest-hierarchy-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Invoice Controller
  name: KPN Rest Invoice Controller API
  slug: kpn-rest-invoice-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Order Controller
  name: KPN Rest Order Controller API
  slug: kpn-rest-order-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Separate Fixed Mobile Controller
  name: KPN Rest Separate Fixed Mobile Controller API
  slug: kpn-rest-separate-fixed-mobile-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Subscriber Controller
  name: KPN Rest Subscriber Controller API
  slug: kpn-rest-subscriber-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Template Controller
  name: KPN Rest Template Controller API
  slug: kpn-rest-template-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Threshold Controller
  name: KPN Rest Threshold Controller API
  slug: kpn-rest-threshold-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest Track And Trace Controller
  name: KPN Rest Track And Trace Controller API
  slug: kpn-rest-track-and-trace-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Rest User Controller
  name: KPN Rest User Controller API
  slug: kpn-rest-user-controller-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: All about managing results
  name: KPN Results API
  slug: kpn-results-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Retrieve job result API from KPN — 3 operation(s) for retrieve job result.
  name: KPN Retrieve job result API
  slug: kpn-retrieve-job-result-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Retrieve SIM swap date API from KPN — 1 operation(s) for retrieve sim swap date.
  name: KPN Retrieve SIM swap date API
  slug: kpn-retrieve-sim-swap-date-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: To retrieve transcritions, check the processing status with your unique **job_id**. Please do not use intervals that are shorter than 10 seconds to check status to avoid a throttle penalty.
  name: KPN Retrieve transcription API
  slug: kpn-retrieve-transcription-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Routing API from KPN — 2 operation(s) for routing.
  name: KPN Routing API
  slug: kpn-routing-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Send API from KPN — 1 operation(s) for send.
  name: KPN Send API
  slug: kpn-send-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Send SMS API from KPN — 1 operation(s) for send sms.
  name: KPN Send SMS API
  slug: kpn-send-sms-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Contract access for service consumers (read-only operations)
  name: KPN Service Consumer Contracts API
  slug: kpn-service-consumer-contracts-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Contract management for service providers (full CRUD operations)
  name: KPN Service Provider Contracts API
  slug: kpn-service-provider-contracts-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Service provider view of consumer parties and their contracts
  name: KPN Service Provider Parties API
  slug: kpn-service-provider-parties-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Session API from KPN — 1 operation(s) for session.
  name: KPN Session API
  slug: kpn-session-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Sites API from KPN — 1 operation(s) for sites.
  name: KPN Sites API
  slug: kpn-sites-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Start engineering job API from KPN — 2 operation(s) for start engineering job.
  name: KPN Start engineering job API
  slug: kpn-start-engineering-job-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Statistics API from KPN — 2 operation(s) for statistics.
  name: KPN Statistics API
  slug: kpn-statistics-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Subscription API from KPN — 1 operation(s) for subscription.
  name: KPN Subscription API
  slug: kpn-subscription-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The switch.configure API from KPN — 47 operation(s) for switch.configure.
  name: KPN Switch.configure API
  slug: kpn-switch-configure-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The switch.monitor API from KPN — 9 operation(s) for switch.monitor.
  name: KPN Switch.monitor API
  slug: kpn-switch-monitor-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Task API from KPN — 1 operation(s) for task.
  name: KPN Task API
  slug: kpn-task-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Team-scope webhook configuration — webhook URL and field exclusions. Overrides the organization config for all applications in your team unless an application config is set.
  name: KPN Team API
  slug: kpn-team-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Signing keys at team scope. Override the organization key for all deliveries in your team unless an application key is configured.
  name: KPN Team Keys API
  slug: kpn-team-keys-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Ticket API from KPN — 3 operation(s) for ticket.
  name: KPN Ticket API
  slug: kpn-ticket-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Token API from KPN — 1 operation(s) for token.
  name: KPN Token API
  slug: kpn-token-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Uploads an audio file and start a new analytics job.
  name: KPN Upload audio API
  slug: kpn-upload-audio-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The User Management API from KPN — 1 operation(s) for user management.
  name: KPN User Management API
  slug: kpn-user-management-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Users API from KPN — 4 operation(s) for users.
  name: KPN Users API
  slug: kpn-users-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Verify API from KPN — 4 operation(s) for verify.
  name: KPN Verify API
  slug: kpn-verify-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: Call related resource management
  name: KPN Voice API
  slug: kpn-voice-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The VoIP SIP API API from KPN — 3 operation(s) for voip sip api.
  name: KPN VoIP SIP API
  slug: kpn-voip-sip-api-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Webhook API from KPN — 1 operation(s) for webhook.
  name: KPN Webhook API
  slug: kpn-webhook-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The wireless.configure API from KPN — 37 operation(s) for wireless.configure.
  name: KPN Wireless.configure API
  slug: kpn-wireless-configure-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The wireless.monitor API from KPN — 33 operation(s) for wireless.monitor.
  name: KPN Wireless.monitor API
  slug: kpn-wireless-monitor-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The XML Scripting API API from KPN — 3 operation(s) for xml scripting api.
  name: KPN XML Scripting API
  slug: kpn-xml-scripting-api-api
- baseURL: https://api-prd.kpn.com/communication/kpn/numberverify
  baseurl_source: declared
  description: The Your Active Webhook API from KPN — 1 operation(s) for your active webhook.
  name: KPN Your Active Webhook API
  slug: kpn-your-active-webhook-api
artifact_total: 143
asyncapis:
- description: ''
  name: Kpn Webhooks
  slug: kpn-webhooks
collections:
- collection_type: open
  name: Apidaze Voice - VoIP Innovations
  slug: open-apidaze-voice
- collection_type: open
  name: Disturbance Check - KPN
  slug: open-kpn-disturbance-check
- collection_type: open
  name: FIAM – Eneco Data Products
  slug: open-kpn-fiam-eneco-data-products
- collection_type: open
  name: FIAM-KPN
  slug: open-kpn-fiam
- collection_type: open
  name: High-Level Design FTTx
  slug: open-kpn-high-level-design-ftth
- collection_type: open
  name: Internet Speed Check - KPN
  slug: open-kpn-internet-speed-check
- collection_type: open
  name: ISE - KPN
  slug: open-kpn-ise
- collection_type: open
  name: LoRa Device Management - KPN
  slug: open-kpn-lora-device-management
- collection_type: open
  name: Match - KPN
  slug: open-kpn-match
- collection_type: open
  name: MobileServicesManagement-KPN
  slug: open-kpn-mobile-services-management
- collection_type: open
  name: Number Verify - KPN
  slug: open-kpn-number-verify
- collection_type: open
  name: KPN SD-LAN SD-WAN Network View API
  slug: open-kpn-sd-lan-sd-wan-network-view
- collection_type: open
  name: ServiceNow Customer Connect
  slug: open-kpn-servicenow-connect
- collection_type: open
  name: SIM Swap
  slug: open-kpn-sim-swap
- collection_type: open
  name: Inbound SMS - KPN
  slug: open-kpn-sms-inbound
- collection_type: open
  name: TV Guide - KPN
  slug: open-kpn-tv-guide
- collection_type: open
  name: Webhook Privacy Configuration - KPN
  slug: open-kpn-webhook-privacy-config-manager
- collection_type: open
  name: Webhook Signing Keys - KPN
  slug: open-kpn-webhook-signing-keys
- collection_type: open
  name: Wholesale Broadband Access
  slug: open-kpn-wholesale-broadband-access-fpi-cip
- collection_type: open
  name: WBA APIs
  slug: open-kpn-wholesale-wba
- collection_type: open
  name: Chat and Messaging - Parley
  slug: open-parley-secure-messenger
- collection_type: open
  name: Knowledge Management – Polly.help
  slug: open-pollyhelp-knowledge-management
- collection_type: open
  name: Registered E-mail - Registered E-mail
  slug: open-registered-email
- collection_type: open
  name: SocialMediaWebcare - Tracebuzz
  slug: open-tracebuzz-social-media-webcare
- collection_type: open
  name: Messages - Vonage
  slug: open-vonage-messages
- collection_type: open
  name: Number Insight - Vonage
  slug: open-vonage-number-insight
- collection_type: open
  name: Phone Numbers - Vonage
  slug: open-vonage-phone-numbers
- collection_type: open
  name: SMS-Vonage
  slug: open-vonage-sms
- collection_type: open
  name: Verify-Vonage
  slug: open-vonage-verify
- collection_type: open
  name: Voice-Vonage
  slug: open-vonage-voice
- collection_type: open
  name: WeSeeDo Direct - WeSeeDo
  slug: open-weseedo-direct
- collection_type: open
  name: WeSeeDo Personal - WeSeeDo
  slug: open-weseedo-personal
- collection_type: open
  name: Speech To Text - Xdroid
  slug: open-xdroid-speech-to-text
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kpn-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-number-verify-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-sim-swap-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/kpn-sim-swap-check.md
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-match-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-sms-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/kpn-send-sms.md
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-sms-inbound-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-mobile-services-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-fiam-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-fiam-eneco-data-products-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-disturbance-check-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/kpn-address-service-check.md
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-internet-speed-check-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-high-level-design-ftth-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-lora-device-management-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/kpn-lora-device-onboarding.md
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-sd-lan-sd-wan-network-view-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-servicenow-connect-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/kpn-servicenow-ticket.md
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-ise-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-tv-guide-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-webhook-signing-keys-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/kpn-rotate-webhook-signing-key.md
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-webhook-privacy-config-manager-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/kpn-configure-webhook-privacy.md
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-wholesale-wba-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-wholesale-broadband-access-fpi-cip-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-pollyhelp-knowledge-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-xdroid-speech-to-text-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-parley-secure-messenger-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-tracebuzz-social-media-webcare-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-weseedo-direct-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-weseedo-personal-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-vonage-messages-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-vonage-voice-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-vonage-phone-numbers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-vonage-number-insight-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-vonage-sms-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-vonage-verify-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-apidaze-voice-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kpn-registered-email-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kpn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kpn-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kpn-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kpn-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.kpn.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kpn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kpn.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.kpn.com/page/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://developer.kpn.com/dashboard/register
- group: start
  title: ''
  type: Login
  url: https://developer.kpn.com/dashboard/login
- group: other
  title: ''
  type: Products
  url: https://developer.kpn.com/products
- group: learn
  title: ''
  type: Tutorials
  url: https://developer.kpn.com/tutorials
- group: company
  title: ''
  type: Blog
  url: https://developer.kpn.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.kpn.com/status
- group: operate
  title: ''
  type: Support
  url: https://developer.kpn.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.kpn.com/page/legal
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://developer.kpn.com/page/responsible-disclosure
- group: docs
  title: ''
  type: OpenAPIRepository
  url: https://app.swaggerhub.com/search?owner=kpn
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kpndeveloper
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kpn
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kpn
- group: other
  title: ''
  type: Wholesale
  url: https://www.kpn-wholesale.com/
- group: other
  title: ''
  type: Standard
  url: https://github.com/camaraproject/
- group: other
  title: ''
  type: Standard
  url: https://coin.nl/camara
- group: build
  title: ''
  type: Packages
  url: packages/kpn-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kpn-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kpn-security.txt
- group: auth
  title: ''
  type: Security
  url: https://developer.kpn.com/page/responsible-disclosure
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kpn-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kpn-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/kpn-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kpn-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kpn-sms-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kpn-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.kpn.com/documentation-response-headers
- group: design
  title: ''
  type: Conventions
  url: conventions/kpn-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kpn-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kpn-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kpn-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kpn-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kpn-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://app.swaggerhub.com/search?owner=kpn
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kpn.com/algemeen/missie-en-privacy-statement/privacy-statement.htm
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.kpn.com/algemeen/cookies.htm
created: '2026-07-25'
description: 'Koninklijke KPN N.V. is the incumbent telecommunications and IT provider of the Netherlands, operating the country''s national fixed (copper and fibre) and mobile networks and selling telephony, broadband, television, IoT connectivity and managed IT services to consumers, businesses and — through KPN Wholesale — to other operators. In the telecom API value chain KPN sits on the network-operator side, but it is a conspicuous exception to the carrier norm: rather than routing developers exclusively through aggregators, KPN runs a genuine self-serve developer portal at developer.kpn.com where anyone can register a free account, get a client ID and secret, test in a sandbox at no cost, and see per-transaction pricing, then upgrade to production via a KRN company number or an iDIN identity check. Thirty-four OpenAPI/Swagger definitions are published anonymously downloadable under KPN''s public SwaggerHub organisation, all fronted by an Apigee-style gateway at api-prd.kpn.com with
  OAuth 2.0 client-credentials. KPN is listed in the official CAMARA landscape as an operator and, with Odido and Vodafone under the COIN association and GSMA Open Gateway, launched CAMARA-standard fraud-prevention APIs for the Dutch market in October 2025; its SIM Swap definition points explicitly at github.com/camaraproject as its product documentation. KPN is not an Aduna shareholder and does not reach developers through that JV. Notably, KPN also resells Vonage and Apidaze CPaaS products through its own portal — the aggregator layer appearing inside the carrier''s own catalogue rather than the other way round.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: KPN
nav: Providers
network: true
overview: 'KPN publishes 100 APIs on the [APIs.io](https://apis.io/) network, including Account API, Activation API, Alarm API, and 97 more. Tagged areas include Telecommunications, Netherlands, Mobile Network Operator, Broadband, and Network APIs.


  The KPN catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  KPN''s developer surface includes authentication, documentation, getting-started guide, signup flow, engineering blog, support, changelog, and 80 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 3
  name: Kpn Rate Limits
  slug: kpn-rate-limits
scopes:
- name: Kpn Scopes
  scope_count: 0
  slug: kpn-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 63.8
    developer_ergonomics: 60.1
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 86.8
  previous_composite: 63.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 100
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 78.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kpn/refs/heads/main/screenshots/kpn-2026-08-07T171335.png
security:
- kind: authentication
  name: Kpn Authentication
  slug: kpn-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Kpn Domain Security
  slug: kpn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kpn Vulnerability Disclosure
  slug: kpn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kpn
tags:
- Telecommunications
- Netherlands
- Mobile Network Operator
- Broadband
- Network APIs
- CAMARA
- Open Gateway
- SIM Swap
- Identity Verification
- Messaging
- SMS
- Voice
- IoT
- LoRaWAN
- Fiber
- Wholesale
- 5G
- Europe
website: https://www.kpn.com/
---
