---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 230
  human_in_the_loop: 3
  name: Signicat Agentic Access
  operation_count: 461
  slug: signicat-agentic-access
  summary_line: 461 operations · 230 acting · 3 human-in-the-loop
api_count: 24
apis:
- description: Legacy SOAP web services for Signicat Enterprise signing (document, archive and packaging services), listed by the CXF service list at api.signicat.com/enterprise/ws/; the archive and packaging servic
  name: Signicat Enterprise SOAP Web Services
  slug: enterprise-ws
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: Provides management endpoints for Accounts.
  name: Signicat Account API
  slug: signicat-account-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'The MobileID account recovery API provides you with operations for our MobileID account recovery feature. ----- <b>Note</b>: The request and response samples are for illustrative purposes only, and di'
  name: Signicat Account recovery API
  slug: signicat-account-recovery-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'The MobileID Admin accounts API provides you with operations related to administering your MobileID account, such as adding an account, and fetching information about an account. ----- **Note**: The r'
  name: Signicat Accounts API
  slug: signicat-accounts-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: This API returns information about a account. Learn more about the different data sources in the [developer documentation](https://developer.signicat.com/docs/data-verification/data-sources/). Also, r
  name: Signicat Accounts And Attributes API
  slug: signicat-accountsandattributes-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'The MobileID Admin **APNs tokens** API provides you with operations related to creating and managing Apple Push Notifications service (APNs) tokens. APNs tokens can be used so that your end-users can '
  name: Signicat APNs tokens API
  slug: signicat-apns-tokens-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The MobileID Admin **Application configuration** API provides you with operations related to administering your <a href="https://developer.signicat.com/docs/mobile-identity/mobileid/features/applicati
  name: Signicat Application configuration API
  slug: signicat-application-configuration-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Archive API from Signicat — 2 operation(s) for archive.
  name: Signicat Archive API
  slug: signicat-archive-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Archive Direct API from Signicat — 1 operation(s) for archive direct.
  name: Signicat Archive Direct API
  slug: signicat-archive-direct-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: Archived documents are stored long-term in Signicat's document archive. Archived documents are referenced by an *archiveID*.
  name: Signicat Archive Document API
  slug: signicat-archive-document-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Assure API from Signicat — 3 operation(s) for assure.
  name: Signicat Assure API
  slug: signicat-assure-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Attachments API from Signicat — 2 operation(s) for attachments.
  name: Signicat Attachments API
  slug: signicat-attachments-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'The MobileID authentication API provides you with operations related to authentication and authorisation for MobileID. ----- <b>Note</b>: The request and response samples are for illustrative purposes'
  name: Signicat Authentication API
  slug: signicat-authentication-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Authentication Session API from Signicat — 3 operation(s) for authentication session.
  name: Signicat Authentication Session API
  slug: signicat-authentication-session-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: This API returns information about a business registry.
  name: Signicat Business Registry API
  slug: signicat-businessregistry-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Capture API from Signicat — 3 operation(s) for capture.
  name: Signicat Capture API
  slug: signicat-capture-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: Endpoint for retrieving person changes for a specific monitor.
  name: Signicat Changes API
  slug: signicat-changes-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Changes Endpoints API from Signicat — 2 operation(s) for changes endpoints.
  name: Signicat Changes Endpoints API
  slug: signicat-changes-endpoints-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Clients API from Signicat — 7 operation(s) for clients.
  name: Signicat Clients API
  slug: signicat-clients-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: Provides management endpoints for contact persons.
  name: Signicat Contact API
  slug: signicat-contact-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Custom claims API from Signicat — 2 operation(s) for custom claims.
  name: Signicat Custom claims API
  slug: signicat-custom-claims-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The DeliveryLogs API from Signicat — 3 operation(s) for deliverylogs.
  name: Signicat Delivery Logs API
  slug: signicat-deliverylogs-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'The MobileID device management API provides you with operations related to device management for MobileID. ----- <b>Note</b>: The request and response samples are for illustrative purposes only, and d'
  name: Signicat Device management API
  slug: signicat-device-management-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: Documents are stored short-term in Signicat's Session Data Storage. Documents are referenced by a *documentID*.
  name: Signicat Document API
  slug: signicat-document-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Document collections API from Signicat — 2 operation(s) for document collections.
  name: Signicat Document collections API
  slug: signicat-document-collections-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Documents API from Signicat — 7 operation(s) for documents.
  name: Signicat Documents API
  slug: signicat-documents-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'Endpoints for managing your domains. See [our documentation](https://developer.signicat.com/docs/dashboard/organisation-management/domains/) in order to become familiar with what domains are used for '
  name: Signicat Domains API
  slug: signicat-domains-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Dossiers API from Signicat — 5 operation(s) for dossiers.
  name: Signicat Dossiers API
  slug: signicat-dossiers-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The MobileID Admin end-to-end (E2E) keys API provides you with operations related to creating and managing your E2E keys. We use E2E keys to create an extra encryption layer in addition to the TLS bet
  name: Signicat End-to-end (E2E) keys API
  slug: signicat-end-to-end-e2e-keys-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Errors API from Signicat — 2 operation(s) for errors.
  name: Signicat Errors API
  slug: signicat-errors-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Events API from Signicat — 2 operation(s) for events.
  name: Signicat Events API
  slug: signicat-events-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The File API from Signicat — 1 operation(s) for file.
  name: Signicat File API
  slug: signicat-file-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: Contains requests related to files
  name: Signicat Files API
  slug: signicat-files-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: This API returns information about geo data.
  name: Signicat Geodata API
  slug: signicat-geodata-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The MobileID identity verification API provides you with operations related to managing the results of identity verification processes, and allows you to link them to the MobileID users that perform t
  name: Signicat Identity verification API
  slug: signicat-identity-verification-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The info API from Signicat — 3 operation(s) for info.
  name: Signicat Info API
  slug: signicat-info-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Invoice API from Signicat — 3 operation(s) for invoice.
  name: Signicat Invoice API
  slug: signicat-invoice-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Journey notes API from Signicat — 2 operation(s) for journey notes.
  name: Signicat Journey notes API
  slug: signicat-journey-notes-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Journeys API from Signicat — 10 operation(s) for journeys.
  name: Signicat Journeys API
  slug: signicat-journeys-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Jwt API from Signicat — 1 operation(s) for jwt.
  name: Signicat JWT API
  slug: signicat-jwt-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Liquid API from Signicat — 1 operation(s) for liquid.
  name: Signicat Liquid API
  slug: signicat-liquid-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Matching API from Signicat — 3 operation(s) for matching.
  name: Signicat Matching API
  slug: signicat-matching-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Merchant signing API from Signicat — 1 operation(s) for merchant signing.
  name: Signicat Merchant signing API
  slug: signicat-merchant-signing-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The MerchantSign API from Signicat — 1 operation(s) for merchantsign.
  name: Signicat Merchant Sign API
  slug: signicat-merchantsign-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Metadata API from Signicat — 3 operation(s) for metadata.
  name: Signicat Metadata API
  slug: signicat-metadata-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'You can use the **MobileID account recovery** resource for operations related to MobileID account recovery for your ReuseID users. ## Useful information - A MobileID account recovery operation is iden'
  name: Signicat MobileID account recovery API
  slug: signicat-mobileid-account-recovery-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'You can use the **MobileID device authentication** resource for operations related to authenticating and authorising with MobileID devices for your ReuseID users. ## Useful information - A MobileID de'
  name: Signicat MobileID device authentication API
  slug: signicat-mobileid-device-authentication-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'You can use the device hashes resource for operations related to: - Reviewing or locking flagged device hashes. - Blocking and unblocking device hashes. --- **Note**: The request and response samples '
  name: Signicat MobileID device hash management API
  slug: signicat-mobileid-device-hash-management-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'You can use the **MobileID device management** resource for operations related to managing MobileID devices for your ReuseID users. ## Useful information All device management operations require both:'
  name: Signicat MobileID device management API
  slug: signicat-mobileid-device-management-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'You can use the **MobileID device registration** resource for operations related to registering MobileID devices for your ReuseID users. ## Useful information - A MobileID device registration operatio'
  name: Signicat MobileID device registration API
  slug: signicat-mobileid-device-registration-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'You can use the **MobileID device signature** resource for operations related to signing with MobileID devices for your ReuseID users. ## Useful information - A MobileID device signature operation is '
  name: Signicat MobileID device signature API
  slug: signicat-mobileid-device-signature-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Monitor Endpoints API from Signicat — 3 operation(s) for monitor endpoints.
  name: Signicat Monitor Endpoints API
  slug: signicat-monitor-endpoints-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: Endpoints for performing CRUD operations on a monitor. A monitor is a collection of persons to monitor for changes.
  name: Signicat Monitors API
  slug: signicat-monitors-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Notifications API from Signicat — 2 operation(s) for notifications.
  name: Signicat Notifications API
  slug: signicat-notifications-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'The ReuseID **Onboarding** API provides you with operations related to the onboarding flow, such as starting and getting information about a ReuseID session. ### About the onboarding flow 1. The onboa'
  name: Signicat Onboarding API
  slug: signicat-onboarding-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Organisation Endpoints API from Signicat — 4 operation(s) for organisation endpoints.
  name: Signicat Organisation Endpoints API
  slug: signicat-organisation-endpoints-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: Provides management endpoints for Organizations.
  name: Signicat Organization API
  slug: signicat-organization-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: This API returns information about an organization. Learn more about the different data sources in the [developer documentation](https://developer.signicat.com/docs/data-verification/data-sources/). A
  name: Signicat Organizations API
  slug: signicat-organizations-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'You can use the **Passkey authentication** resource for operations related to authenticating and authorising with passkeys for your ReuseID users. ## Useful information - A passkey authentication oper'
  name: Signicat Passkey authentication API
  slug: signicat-passkey-authentication-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'You can use the **Passkey management** resource for operations related to managing passkeys for your ReuseID users. ## Useful information All passkey management operations require both: - A ReuseID us'
  name: Signicat Passkey management API
  slug: signicat-passkey-management-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'You can use the **Passkey registration** resource for operations related to registering passkeys for your ReuseID users. ## Useful information - A passkey registration operation is identified by its `'
  name: Signicat Passkey registration API
  slug: signicat-passkey-registration-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Person Endpoints API from Signicat — 2 operation(s) for person endpoints.
  name: Signicat Person Endpoints API
  slug: signicat-person-endpoints-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: This API returns information about a person. Learn more about the different data sources in the [developer documentation](https://developer.signicat.com/docs/data-verification/data-sources/). Also, re
  name: Signicat Persons API
  slug: signicat-persons-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The ping-rest-controller API from Signicat — 1 operation(s) for ping-rest-controller.
  name: Signicat Ping Rest Controller API
  slug: signicat-ping-rest-controller-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Processes API from Signicat — 9 operation(s) for processes.
  name: Signicat Processes API
  slug: signicat-processes-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Public keys API from Signicat — 2 operation(s) for public keys.
  name: Signicat Public keys API
  slug: signicat-public-keys-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Query API from Signicat — 4 operation(s) for query.
  name: Signicat Query API
  slug: signicat-query-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: Contains requests related to recipients
  name: Signicat Recipients API
  slug: signicat-recipients-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The records API from Signicat — 3 operation(s) for records.
  name: Signicat Records API
  slug: signicat-records-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'The MobileID registration API provides you with operations related to registering devices for MobileID. ----- <b>Note</b>: The request and response samples are for illustrative purposes only, and disc'
  name: Signicat Registration API
  slug: signicat-registration-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Report API from Signicat — 1 operation(s) for report.
  name: Signicat Report API
  slug: signicat-report-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The reports API from Signicat — 1 operation(s) for reports.
  name: Signicat Reports API
  slug: signicat-reports-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'You can use the Risk indicators configuration resource for operations related to retrieving and updating risk indicator properties. ----- <b>Note</b>: The request and response samples are for illustra'
  name: Signicat Risk indicators configuration API
  slug: signicat-risk-indicators-configuration-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The SCIM - Custom attribute management API from Signicat — 6 operation(s) for scim - custom attribute management.
  name: Signicat SCIM - Custom attribute management API
  slug: signicat-scim-custom-attribute-management-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The SCIM - External idp management API from Signicat — 2 operation(s) for scim - external idp management.
  name: Signicat SCIM - External idp management API
  slug: signicat-scim-external-idp-management-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The SCIM - Membership management API from Signicat — 2 operation(s) for scim - membership management.
  name: Signicat SCIM - Membership management API
  slug: signicat-scim-membership-management-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The SCIM - Organization management API from Signicat — 2 operation(s) for scim - organization management.
  name: Signicat SCIM - Organization management API
  slug: signicat-scim-organization-management-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The SCIM - Role management API from Signicat — 2 operation(s) for scim - role management.
  name: Signicat SCIM - Role management API
  slug: signicat-scim-role-management-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The SCIM Schemas API from Signicat — 2 operation(s) for scim schemas.
  name: Signicat SCIM Schemas API
  slug: signicat-scim-schemas-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The SCIM - User invitation management API from Signicat — 5 operation(s) for scim - user invitation management.
  name: Signicat SCIM - User invitation management API
  slug: signicat-scim-user-invitation-management-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The SCIM - User management API from Signicat — 5 operation(s) for scim - user management.
  name: Signicat SCIM - User management API
  slug: signicat-scim-user-management-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Secrets API from Signicat — 2 operation(s) for secrets.
  name: Signicat Secrets API
  slug: signicat-secrets-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: Contains requests related to share objects
  name: Signicat Shares API
  slug: signicat-shares-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The MobileID signature API provides you with operations related to signing for MobileID. You can read more about the signature operation in our [Signature](https://developer.signicat.com/docs/mobile-i
  name: Signicat Signature API
  slug: signicat-signature-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The SignatureMethods API from Signicat — 2 operation(s) for signaturemethods.
  name: Signicat Signature Methods API
  slug: signicat-signaturemethods-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Signers API from Signicat — 3 operation(s) for signers.
  name: Signicat Signers API
  slug: signicat-signers-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'The MobileID Admin signing certificates API allows you to get signing certificates, which can be used for certificate verification. ## Useful information JSON Web Tokens (JWTs) are returned as a resul'
  name: Signicat Signing certificates API
  slug: signicat-signing-certificates-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: A signing order represents a single signing process, which can consist of one or more documents and signees
  name: Signicat Signing Order API
  slug: signicat-signing-order-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Signing sessions API from Signicat — 2 operation(s) for signing sessions.
  name: Signicat Signing sessions API
  slug: signicat-signing-sessions-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'Contains information about the different sources used by the API. It is possible to instruct the API to use a preferred source across profiles by including a JWT of the following model in the request '
  name: Signicat Sources API
  slug: signicat-sources-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Statistics API from Signicat — 5 operation(s) for statistics.
  name: Signicat Statistics API
  slug: signicat-statistics-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Step definitions API from Signicat — 2 operation(s) for step definitions.
  name: Signicat Step definitions API
  slug: signicat-step-definitions-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'The ReuseID **Step-up** API provides you with operations related to the step-up flow, such as starting and getting information about a ReuseID step-up session. ### About the step-up flow 1. The step-u'
  name: Signicat Step Up API
  slug: signicat-step-up-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: Subscriptions are used to listen to events generated by Signicat services. Different types of subscriptions are available, allowing your application to listen to events in the way best suited for you.
  name: Signicat Subscriptions API
  slug: signicat-subscriptions-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Themes API from Signicat — 2 operation(s) for themes.
  name: Signicat Themes API
  slug: signicat-themes-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: Api for reading usage Note! Header signicat-organizationid or signicat-accountid must be provided for all calls
  name: Signicat Usage API
  slug: signicat-usage-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: 'The MobileID user API provides you with operations related to creating and managing users (sometimes referred to as <i>identities</i>) for MobileID. ----- <b>Note</b>: The request and response samples'
  name: Signicat User API
  slug: signicat-user-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Utilities API from Signicat — 2 operation(s) for utilities.
  name: Signicat Utilities API
  slug: signicat-utilities-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Validate API from Signicat — 3 operation(s) for validate.
  name: Signicat Validate API
  slug: signicat-validate-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Workflow secrets API from Signicat — 2 operation(s) for workflow secrets.
  name: Signicat Workflow secrets API
  slug: signicat-workflow-secrets-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Workflow templates API from Signicat — 4 operation(s) for workflow templates.
  name: Signicat Workflow templates API
  slug: signicat-workflow-templates-api
- baseURL: https://api.signicat.com/info/lookup
  baseurl_source: declared
  description: The Workflows API from Signicat — 10 operation(s) for workflows.
  name: Signicat Workflows API
  slug: signicat-workflows-api
- baseURL: https://api.signicat.com/enterprise/ws
  baseurl_source: declared
  description: The Audit Log API from Signicat — 1 operation(s) for audit log.
  name: Signicat Audit Log API
  slug: signicat-audit-log-api
artifact_total: 240
common:
- group: other
  href: https://artifacts.apis.io/signicat/capabilities/signicat-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/signicat-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/signicat/agentic-access/signicat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/signicat-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/signicat/rules/signicat-rules.yml
  title: ''
  type: Spectral
  url: rules/signicat-rules.yml
- group: design
  href: https://artifacts.apis.io/signicat/json-ld/signicat-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/signicat-context.jsonld
- group: design
  href: https://artifacts.apis.io/signicat/vocabulary/signicat-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/signicat-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/signicat/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/signicat/data-model/signicat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/signicat-data-model.yml
- group: operate
  href: https://artifacts.apis.io/signicat/changelog/signicat-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/signicat-changelog.yml
- group: design
  href: https://artifacts.apis.io/signicat/conventions/signicat-conventions.yml
  title: ''
  type: Conventions
  url: conventions/signicat-conventions.yml
- group: start
  href: https://artifacts.apis.io/signicat/sandbox/signicat-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/signicat-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://www.signicat.com/security-and-compliance
- group: operate
  href: https://artifacts.apis.io/signicat/lifecycle/signicat-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/signicat-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/signicat/lifecycle/signicat-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/signicat-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/signicat/errors/signicat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/signicat-problem-types.yml
- group: design
  href: https://artifacts.apis.io/signicat/conformance/signicat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/signicat-conformance.yml
- group: other
  href: https://artifacts.apis.io/signicat/overlays/signicat-account-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/signicat-account-management-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/signicat/llms/signicat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/signicat-llms.txt
- group: build
  href: https://artifacts.apis.io/signicat/mcp/signicat-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/signicat-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/signicat/mcp/signicat-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/signicat-mcp.yml
- group: auth
  href: https://artifacts.apis.io/signicat/well-known/signicat-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signicat-security.txt
- group: auth
  href: https://artifacts.apis.io/signicat/well-known/signicat-login-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signicat-login-security.txt
- group: auth
  href: https://artifacts.apis.io/signicat/well-known/signicat-developer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signicat-developer-security.txt
- group: auth
  href: https://artifacts.apis.io/signicat/well-known/signicat-dashboard-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signicat-dashboard-security.txt
- group: auth
  href: https://artifacts.apis.io/signicat/well-known/signicat-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signicat-api-security.txt
- group: agent
  href: https://artifacts.apis.io/signicat/well-known/signicat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/signicat-well-known.yml
- group: other
  href: https://artifacts.apis.io/signicat/hosts/signicat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/signicat-hosts.yml
- group: other
  href: https://artifacts.apis.io/signicat/vendors/signicat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/signicat-vendors.yml
- group: build
  href: https://artifacts.apis.io/signicat/packages/signicat-packages.yml
  title: ''
  type: SDKs
  url: packages/signicat-packages.yml
- group: build
  href: https://artifacts.apis.io/signicat/packages/signicat-packages.yml
  title: ''
  type: Packages
  url: packages/signicat-packages.yml
- group: auth
  href: https://artifacts.apis.io/signicat/authentication/signicat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/signicat-authentication.yml
- group: auth
  href: https://artifacts.apis.io/signicat/scopes/signicat-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/signicat-scopes.yml
- group: auth
  href: https://artifacts.apis.io/signicat/security/signicat-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/signicat-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/signicat/security/signicat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/signicat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://signicat.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.signicat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.signicat.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.signicat.com/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.signicat.com/docs/dashboard/connect-to-signicat-apis/quick-start-guide/
- group: operate
  title: ''
  type: Support
  url: https://www.signicat.com/contact/contact-support
- group: company
  title: ''
  type: Blog
  url: https://www.signicat.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signicat
- group: commercial
  title: ''
  type: Pricing
  url: https://www.signicat.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://login.signicat.com/ownidp/web/registration
- group: start
  title: ''
  type: Login
  url: https://dashboard.signicat.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.signicat.com/about/terms-of-use-signicat-dashboard
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.signicat.com/about/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.signicat.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/signicat/
created: '2026-10-18'
description: Signicat is a European digital identity company offering "one point of integration for all your digital identity needs across borders – in every step of the customer journey." Its products cover identity proofing (eID and Wallet Hub, ID document and biometric verification, ReuseID, data verification, ongoing monitoring), authentication (MobileID, passkeys), electronic signing (Electronic Signature API and the Dokobit signature portal), trust orchestration (Signicat Mint no-code workflows, RiskFlow) and digital evidence management, all exposed to developers through the APIs documented at developer.signicat.com.
image: https://signicat.imgix.net/blog/homepage-featured-signicat.png?auto=format&crop=focalpoint&domain=signicat.imgix.net&fit=crop&fp-x=0.5&fp-y=0.5&h=630&ixlib=php-3.3.1&q=82&usm=20&w=1200&s=8a19581e3ec3eb39eb2d37431ebe788e
json_schemas:
- name: AccountPlatformAllDetailsStatistic
  property_count: 7
  slug: signicat-account-platform-all-details-statistic
- name: AccountRead
  property_count: 13
  slug: signicat-account-read
- name: AccountRecoveryDetails
  property_count: 12
  slug: signicat-account-recovery-details
- name: AccountResponse
  property_count: 13
  slug: signicat-account-response
- name: APNSToken
  property_count: 8
  slug: signicat-apnstoken
- name: ApplicationConfigProperties
  property_count: 49
  slug: signicat-application-config-properties
- name: ApplicationConfigUpdateRequest
  property_count: 47
  slug: signicat-application-config-update-request
- name: Archive.ArchiveObjectsRepresentation.jsonld
  property_count: 7
  slug: signicat-archive-archive-objects-representation-jsonld
- name: Archive-archive.patch
  property_count: 3
  slug: signicat-archive-archive-patch
- name: Archive.Direct.jsonld
  property_count: 3
  slug: signicat-archive-direct-jsonld
- name: Archive.jsonld
  property_count: 12
  slug: signicat-archive-jsonld
- name: Archive
  property_count: 9
  slug: signicat-archive
- name: Artifact
  property_count: 4
  slug: signicat-artifact
- name: AttachmentRequest
  property_count: 7
  slug: signicat-attachment-request
- name: AuditLog.jsonld
  property_count: 10
  slug: signicat-audit-log-jsonld
- name: AuditLog
  property_count: 19
  slug: signicat-audit-log
- name: AuditQueryResult_AuditLog
  property_count: 4
  slug: signicat-audit-query-result-audit-log
- name: Authentication
  property_count: 12
  slug: signicat-authentication
- name: BaseMonitorPerson
  property_count: 8
  slug: signicat-base-monitor-person
- name: BusinessRegistry.RegistrationAuthorityDto
  property_count: 9
  slug: signicat-business-registry-registration-authority-dto
- name: BusinessRegistry.RegistrationAuthorityItemDto
  property_count: 7
  slug: signicat-business-registry-registration-authority-item-dto
- name: CaptureConfigurationResponse
  property_count: 47
  slug: signicat-capture-configuration-response
- name: CaptureConfiguration
  property_count: 44
  slug: signicat-capture-configuration
- name: CheckDnsSetupResponse
  property_count: 2
  slug: signicat-check-dns-setup-response
- name: CheckDomainAvailability
  property_count: 3
  slug: signicat-check-domain-availability
- name: ClientDto
  property_count: 46
  slug: signicat-client-dto
- name: CreateMonitorRequestDto
  property_count: 5
  slug: signicat-create-monitor-request-dto
- name: CreateRecipientDto
  property_count: 8
  slug: signicat-create-recipient-dto
- name: CreateShareDto
  property_count: 9
  slug: signicat-create-share-dto
- name: CreateWorkflowRequest
  property_count: 8
  slug: signicat-create-workflow-request
- name: CustomClaimDto
  property_count: 4
  slug: signicat-custom-claim-dto
- name: DeviceAuthentication
  property_count: 12
  slug: signicat-device-authentication
- name: DeviceRegistration
  property_count: 12
  slug: signicat-device-registration
- name: DeviceSignature
  property_count: 13
  slug: signicat-device-signature
- name: DocumentCollection
  property_count: 5
  slug: signicat-document-collection
- name: Document
  property_count: 7
  slug: signicat-document
- name: DocumentSummary
  property_count: 16
  slug: signicat-document-summary
- name: DomainCreate
  property_count: 5
  slug: signicat-domain-create
- name: DomainPatch
  property_count: 2
  slug: signicat-domain-patch
- name: DomainRead
  property_count: 11
  slug: signicat-domain-read
- name: E2EKey
  property_count: 9
  slug: signicat-e2-ekey
- name: EventLogItem
  property_count: 4
  slug: signicat-event-log-item
- name: Event
  property_count: 3
  slug: signicat-event
- name: ForwardingInfo
  property_count: 8
  slug: signicat-forwarding-info
- name: Geodata.CountryInfoDto
  property_count: 12
  slug: signicat-geodata-country-info-dto
- name: GetMetadataResponse
  property_count: 5
  slug: signicat-get-metadata-response
- name: GroupCustomAttributeDefinitionResource
  property_count: 11
  slug: signicat-group-custom-attribute-definition-resource
- name: IDVerificationAddRequest
  property_count: 5
  slug: signicat-idverification-add-request
- name: InvoiceItem
  property_count: 27
  slug: signicat-invoice-item
- name: InvoiceListItem
  property_count: 26
  slug: signicat-invoice-list-item
- name: Journey
  property_count: 18
  slug: signicat-journey
- name: MatchResponse
  property_count: 5
  slug: signicat-match-response
- name: MembershipCustomAttributeDefinitionResource
  property_count: 13
  slug: signicat-membership-custom-attribute-definition-resource
- name: MembershipResource
  property_count: 10
  slug: signicat-membership-resource
- name: MerchantSignRequest
  property_count: 2
  slug: signicat-merchant-sign-request
- name: MonitorChangesDto
  property_count: 7
  slug: signicat-monitor-changes-dto
- name: MonitorCreate
  property_count: 6
  slug: signicat-monitor-create
- name: MonitorDto
  property_count: 10
  slug: signicat-monitor-dto
- name: MonitorGet
  property_count: 10
  slug: signicat-monitor-get
- name: MonitorPersonGet
  property_count: 12
  slug: signicat-monitor-person-get
- name: OrganisationDataDto
  property_count: 21
  slug: signicat-organisation-data-dto
- name: OrganisationRequestDto
  property_count: 6
  slug: signicat-organisation-request-dto
- name: Organization.BasicInfoDto
  property_count: 14
  slug: signicat-organization-basic-info-dto
- name: OrganizationCreate
  property_count: 9
  slug: signicat-organization-create
- name: OrganizationListResponse
  property_count: 10
  slug: signicat-organization-list-response
- name: Organization.OwnershipDto
  property_count: 5
  slug: signicat-organization-ownership-dto
- name: OrganizationRead
  property_count: 15
  slug: signicat-organization-read
- name: OrganizationWrite
  property_count: 9
  slug: signicat-organization-write
- name: PackagingTaskStatusInfo
  property_count: 4
  slug: signicat-packaging-task-status-info
- name: Page_SubscriptionListItem
  property_count: 2
  slug: signicat-page-subscription-list-item
- name: PagedCollection`1
  property_count: 5
  slug: signicat-paged-collection-1
- name: PaginatedSigningSessionResponse
  property_count: 5
  slug: signicat-paginated-signing-session-response
- name: PasskeyAuthenticationResponse
  property_count: 14
  slug: signicat-passkey-authentication-response
- name: PasskeyRegistrationResponse
  property_count: 14
  slug: signicat-passkey-registration-response
- name: PatchClientDto
  property_count: 41
  slug: signicat-patch-client-dto
- name: Person.BasicInfoDto
  property_count: 10
  slug: signicat-person-basic-info-dto
- name: PersonChanges
  property_count: 6
  slug: signicat-person-changes
- name: PersonResponseDto
  property_count: 19
  slug: signicat-person-response-dto
- name: PostDocumentResponse
  property_count: 4
  slug: signicat-post-document-response
- name: ProcessRequest
  property_count: 9
  slug: signicat-process-request
- name: ProcessResponse
  property_count: 14
  slug: signicat-process-response
- name: Process
  property_count: 12
  slug: signicat-process
- name: PublicKeyDto
  property_count: 8
  slug: signicat-public-key-dto
- name: QueryMetadataResponseEventTypeProperties
  property_count: 1
  slug: signicat-query-metadata-response-event-type-properties
- name: QueryMetadataResponse
  property_count: 2
  slug: signicat-query-metadata-response
- name: QueryRecordResponse
  property_count: 5
  slug: signicat-query-record-response
- name: QueryRequestBody
  property_count: 3
  slug: signicat-query-request-body
- name: Query
  property_count: 3
  slug: signicat-query
- name: RecipientDto
  property_count: 12
  slug: signicat-recipient-dto
- name: RecordResponse
  property_count: 7
  slug: signicat-record-response
- name: Registration
  property_count: 12
  slug: signicat-registration
- name: SecretDto
  property_count: 5
  slug: signicat-secret-dto
- name: SessionDataDto
  property_count: 27
  slug: signicat-session-data-dto
- name: SessionRequestDto
  property_count: 19
  slug: signicat-session-request-dto
- name: ShareResponseDto
  property_count: 15
  slug: signicat-share-response-dto
- name: Signature
  property_count: 13
  slug: signicat-signature
- name: SignerRequest
  property_count: 15
  slug: signicat-signer-request
- name: SignerResponse
  property_count: 19
  slug: signicat-signer-response
- name: SignicatErrorTemplateDto
  property_count: 5
  slug: signicat-signicat-error-template-dto
- name: SigningOrder
  property_count: 8
  slug: signicat-signing-order
- name: SigningSession
  property_count: 25
  slug: signicat-signing-session
- name: Stats
  property_count: 4
  slug: signicat-stats
- name: StepDefinition
  property_count: 10
  slug: signicat-step-definition
- name: SubjectCustomAttributeDefinitionResource
  property_count: 13
  slug: signicat-subject-custom-attribute-definition-resource
- name: SubscriptionCreate
  property_count: 7
  slug: signicat-subscription-create
- name: SubscriptionEventDeliveryAttempt
  property_count: 10
  slug: signicat-subscription-event-delivery-attempt
- name: SubscriptionGet
  property_count: 12
  slug: signicat-subscription-get
- name: SubscriptionUpdate
  property_count: 8
  slug: signicat-subscription-update
- name: TaskStatusInfo
  property_count: 7
  slug: signicat-task-status-info
- name: UpdateRecipientDto
  property_count: 8
  slug: signicat-update-recipient-dto
- name: UpdateShareDto
  property_count: 4
  slug: signicat-update-share-dto
- name: UpdateSignerRequest
  property_count: 13
  slug: signicat-update-signer-request
- name: UpdateSignerResponse
  property_count: 19
  slug: signicat-update-signer-response
- name: UpdateWorkflowRequest
  property_count: 8
  slug: signicat-update-workflow-request
- name: UsageSet
  property_count: 3
  slug: signicat-usage-set
- name: UserResource
  property_count: 16
  slug: signicat-user-resource
- name: User
  property_count: 7
  slug: signicat-user
- name: Workflow
  property_count: 16
  slug: signicat-workflow
- name: WorkflowTemplate
  property_count: 12
  slug: signicat-workflow-template
jsonld:
- class_count: 120
  name: Signicat Context
  property_count: 272
  slug: signicat-context
layout: provider
mcp_servers:
- description: Signicat documentation MCP server (hosted on kapa.ai). Searches and retrieves Signicat developer documentation; it does not invoke Signicat product APIs.
  name: Signicat MCP Server
  slug: signicat-docs
modified: '2026-10-18'
name: Signicat
nav: Providers
network: true
overview: 'Signicat publishes 103 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Account recovery API, Accounts API, and 100 more. Tagged areas include Company, Digital Identity, Authentication, E-Signature, and KYC.


  The Signicat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Signicat''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, support, and 41 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Signicat API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 3
    warn: 3
  slug: signicat-rules
scopes:
- name: Signicat Scopes
  scope_count: 2
  slug: signicat-scopes
  summary_line: 2 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 61.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 62.7
    developer_ergonomics: 73.2
    discoverability: 70.0
    operational_transparency: 55.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 85.3
      derived: 0
      marker_coverage: 0.0
      total: 102
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: eidas
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Signicat Authentication
  slug: signicat-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Signicat Domain Security
  slug: signicat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Signicat Vulnerability Disclosure
  slug: signicat-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
skill_count: 10
skills:
- name: signicat-authenticate-a-user-with-an-eid
  slug: signicat-authenticate-a-user-with-an-eid
- name: signicat-create-and-manage-dossier
  slug: signicat-create-and-manage-dossier
- name: signicat-create-and-manage-signature
  slug: signicat-create-and-manage-signature
- name: signicat-create-and-manage-verification-process
  slug: signicat-create-and-manage-verification-process
- name: signicat-monitor-customers
  slug: signicat-monitor-customers
- name: signicat-sign-a-document
  slug: signicat-sign-a-document
- name: signicat-start-and-track-onboarding
  slug: signicat-start-and-track-onboarding
- name: signicat-upload-and-manage-document
  slug: signicat-upload-and-manage-document
- name: signicat-verify-an-id-document
  slug: signicat-verify-an-id-document
- name: signicat-verify-an-organisation
  slug: signicat-verify-an-organisation
slug: signicat
tags:
- Company
- Digital Identity
- Authentication
- E-Signature
- KYC
- Identity Verification
- eID
- Fraud Prevention
website: https://signicat.com
---
