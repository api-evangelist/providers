---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 83.6
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 553
  human_in_the_loop: 61
  name: Telnyx Agentic Access
  operation_count: 1038
  slug: telnyx-agentic-access
  summary_line: 1038 operations · 553 acting · 61 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Access Tokens creation
  name: Telnyx Access Tokens API
  slug: telnyx-access-tokens-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: 'Operations to work with Address records. Address records are emergency-validated addresses meant to be associated with phone numbers. They are validated for emergency usage purposes at creation time, '
  name: Telnyx Addresses API
  slug: telnyx-addresses-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Advanced Number Orders API from Telnyx — 3 operation(s) for advanced number orders.
  name: Telnyx Advanced Number Orders API
  slug: telnyx-advanced-number-orders-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Configure AI assistant specifications
  name: Telnyx Assistants API
  slug: telnyx-assistants-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Audio API from Telnyx — 1 operation(s) for audio.
  name: Telnyx Audio API
  slug: telnyx-audio-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Audit log operations.
  name: Telnyx Audit Logs API
  slug: telnyx-audit-logs-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Authentication Providers API from Telnyx — 2 operation(s) for authentication providers.
  name: Telnyx Authentication Providers API
  slug: telnyx-authentication-providers-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: V2 Auto Recharge Preferences API
  name: Telnyx AutoRechargePreferences API
  slug: telnyx-autorechargepreferences-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Billing operations
  name: Telnyx Billing API
  slug: telnyx-billing-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Billing groups operations
  name: Telnyx Billing Groups API
  slug: telnyx-billing-groups-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Brand operations
  name: Telnyx Brands API
  slug: telnyx-brands-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: SSL certificate operations
  name: Telnyx Bucket SSL Certificate API
  slug: telnyx-bucket-ssl-certificate-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Bucket Usage operations
  name: Telnyx Bucket Usage API
  slug: telnyx-bucket-usage-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Phone number campaign bulk assignment
  name: Telnyx Bulk Phone Number Campaigns API
  slug: telnyx-bulk-phone-number-campaigns-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Background jobs performed over a batch of phone numbers
  name: Telnyx Bulk Phone Number Operations API
  slug: telnyx-bulk-phone-number-operations-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Bundles API from Telnyx — 2 operation(s) for bundles.
  name: Telnyx Bundles API
  slug: telnyx-bundles-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Call Control command operations
  name: Telnyx Call Commands API
  slug: telnyx-call-commands-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Call Control applications operations
  name: Telnyx Call Control Applications API
  slug: telnyx-call-control-applications-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Call information
  name: Telnyx Call Information API
  slug: telnyx-call-information-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Call Recordings operations.
  name: Telnyx Call Recordings API
  slug: telnyx-call-recordings-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Campaign operations
  name: Telnyx Campaign API
  slug: telnyx-campaign-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Voice batch detail records
  name: Telnyx CDR Reports API
  slug: telnyx-cdr-reports-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Voice usage reports
  name: Telnyx CDR Usage Reports API
  slug: telnyx-cdr-usage-reports-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Charges Breakdown API from Telnyx — 1 operation(s) for charges breakdown.
  name: Telnyx Charges Breakdown API
  slug: telnyx-charges-breakdown-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Charges Summary API from Telnyx — 1 operation(s) for charges summary.
  name: Telnyx Charges Summary API
  slug: telnyx-charges-summary-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Generate text with LLMs
  name: Telnyx Chat API
  slug: telnyx-chat-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Identify common themes and patterns in your embedded documents
  name: Telnyx Clusters API
  slug: telnyx-clusters-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Conference command operations
  name: Telnyx Conference Commands API
  slug: telnyx-conference-commands-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Connections operations
  name: Telnyx Connections API
  slug: telnyx-connections-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage historical AI assistant conversations
  name: Telnyx Conversations API
  slug: telnyx-conversations-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Country Coverage
  name: Telnyx Country Coverage API
  slug: telnyx-country-coverage-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Coverage API from Telnyx — 1 operation(s) for coverage.
  name: Telnyx Coverage API
  slug: telnyx-coverage-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Credential connection operations
  name: Telnyx Credential Connections API
  slug: telnyx-credential-connections-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Credentials operations
  name: Telnyx Credentials API
  slug: telnyx-credentials-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The CSV Downloads API from Telnyx — 2 operation(s) for csv downloads.
  name: Telnyx CSV Downloads API
  slug: telnyx-csv-downloads-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Customer Service Record operations
  name: Telnyx Customer Service Record API
  slug: telnyx-customer-service-record-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Migrate data from an external provider into Telnyx Cloud Storage
  name: Telnyx Data Migration API
  slug: telnyx-data-migration-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Call Control debugging
  name: Telnyx Debugging API
  slug: telnyx-debugging-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Detail Records operations
  name: Telnyx Detail Records API
  slug: telnyx-detail-records-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Dialogflow Connection Operations.
  name: Telnyx Dialogflow Integration API
  slug: telnyx-dialogflow-integration-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Documents
  name: Telnyx Documents API
  slug: telnyx-documents-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Dynamic emergency address operations
  name: Telnyx Dynamic Emergency Addresses API
  slug: telnyx-dynamic-emergency-addresses-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Dynamic Emergency Endpoints
  name: Telnyx Dynamic Emergency Endpoints API
  slug: telnyx-dynamic-emergency-endpoints-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Embed documents and perform text searches
  name: Telnyx Embeddings API
  slug: telnyx-embeddings-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Enterprise management for Branded Calling and Number Reputation services
  name: Telnyx Enterprises API
  slug: telnyx-enterprises-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Enum API from Telnyx — 1 operation(s) for enum.
  name: Telnyx Enum API
  slug: telnyx-enum-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: External Connections operations
  name: Telnyx External Connections API
  slug: telnyx-external-connections-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Customize LLMs for your unique needs
  name: Telnyx Fine Tuning API
  slug: telnyx-fine-tuning-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: FQDN connection operations
  name: Telnyx FQDN Connections API
  slug: telnyx-fqdn-connections-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: FQDN operations
  name: Telnyx FQDNs API
  slug: telnyx-fqdns-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Global IPs
  name: Telnyx Global IPs API
  slug: telnyx-global-ips-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage your messaging hosted numbers
  name: Telnyx Hosted Numbers API
  slug: telnyx-hosted-numbers-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Inexplicit number orders for bulk purchasing without specifying exact numbers
  name: Telnyx Inexplicit Number Orders API
  slug: telnyx-inexplicit-number-orders-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Store and retrieve integration secrets
  name: Telnyx Integration Secrets API
  slug: telnyx-integration-secrets-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Integrations API from Telnyx — 4 operation(s) for integrations.
  name: Telnyx Integrations API
  slug: telnyx-integrations-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Inventory Level
  name: Telnyx Inventory Level API
  slug: telnyx-inventory-level-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Invoices API from Telnyx — 2 operation(s) for invoices.
  name: Telnyx Invoices API
  slug: telnyx-invoices-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: IP Address Operations
  name: Telnyx IP Addresses API
  slug: telnyx-ip-addresses-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: IP connection operations
  name: Telnyx IP Connections API
  slug: telnyx-ip-connections-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: IP Range Operations
  name: Telnyx IP Ranges API
  slug: telnyx-ip-ranges-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Managed Accounts operations
  name: Telnyx Managed Accounts API
  slug: telnyx-managed-accounts-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The MCP Servers API from Telnyx — 2 operation(s) for mcp servers.
  name: Telnyx MCP Servers API
  slug: telnyx-mcp-servers-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The MDR Detail Reports API from Telnyx — 1 operation(s) for mdr detail reports.
  name: Telnyx MDR Detail Reports API
  slug: telnyx-mdr-detail-reports-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Messaging batch detail records
  name: Telnyx MDR Detailed Reports API
  slug: telnyx-mdr-detailed-reports-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Messaging usage reports
  name: Telnyx MDR Usage Reports API
  slug: telnyx-mdr-usage-reports-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Media Storage operations
  name: Telnyx Media Storage API
  slug: telnyx-media-storage-api-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Messages
  name: Telnyx Messages API
  slug: telnyx-messages-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Messaging API from Telnyx — 8 operation(s) for messaging.
  name: Telnyx Messaging API
  slug: telnyx-messaging-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Messaging URL Domains
  name: Telnyx Messaging URL Domains API
  slug: telnyx-messaging-url-domains-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Missions API from Telnyx — 23 operation(s) for missions.
  name: Telnyx Missions API
  slug: telnyx-missions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Mobile network operators operations
  name: Telnyx Mobile Network Operators API
  slug: telnyx-mobile-network-operators-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Mobile Number Settings API from Telnyx — 2 operation(s) for mobile number settings.
  name: Telnyx Mobile Number Settings API
  slug: telnyx-mobile-number-settings-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Mobile phone number operations
  name: Telnyx Mobile Phone Numbers API
  slug: telnyx-mobile-phone-numbers-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Mobile voice connection operations
  name: Telnyx Mobile Voice Connections API
  slug: telnyx-mobile-voice-connections-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Network operations
  name: Telnyx Networks API
  slug: telnyx-networks-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Notification settings operations
  name: Telnyx Notifications API
  slug: telnyx-notifications-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Look up phone number data
  name: Telnyx Number Lookup API
  slug: telnyx-number-lookup-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Number portout operations
  name: Telnyx Number Portout API
  slug: telnyx-number-portout-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage Number Reputation enrollment and check frequency settings for an enterprise
  name: Telnyx Number Reputation Settings API
  slug: telnyx-number-reputation-settings-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Configure your phone numbers
  name: Telnyx Number Settings API
  slug: telnyx-number-settings-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The numbers features API from Telnyx — 1 operation(s) for numbers features.
  name: Telnyx numbers features API
  slug: telnyx-numbers-features-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The OAuth Clients API from Telnyx — 2 operation(s) for oauth clients.
  name: Telnyx OAuth Clients API
  slug: telnyx-oauth-clients-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The OAuth Discovery API from Telnyx — 2 operation(s) for oauth discovery.
  name: Telnyx OAuth Discovery API
  slug: telnyx-oauth-discovery-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The OAuth Grants API from Telnyx — 2 operation(s) for oauth grants.
  name: Telnyx OAuth Grants API
  slug: telnyx-oauth-grants-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The OAuth Protocol API from Telnyx — 7 operation(s) for oauth protocol.
  name: Telnyx OAuth Protocol API
  slug: telnyx-oauth-protocol-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The OpenAI Chat API from Telnyx — 2 operation(s) for openai chat.
  name: Telnyx OpenAI Chat API
  slug: telnyx-openai-chat-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: OpenAI-compatible embeddings endpoints for generating vector representations of text
  name: Telnyx OpenAI Embeddings API
  slug: telnyx-openai-embeddings-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Opt-Out Management
  name: Telnyx Opt-Out Management API
  slug: telnyx-opt-out-management-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Operations related to users in your organization
  name: Telnyx Organization Users API
  slug: telnyx-organization-users-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: OTA updates operations
  name: Telnyx OTA updates API
  slug: telnyx-ota-updates-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Outbound voice profiles operations
  name: Telnyx Outbound Voice Profiles API
  slug: telnyx-outbound-voice-profiles-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Phone Number Block Orders API from Telnyx — 2 operation(s) for phone number block orders.
  name: Telnyx Phone Number Block Orders API
  slug: telnyx-phone-number-block-orders-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Background jobs performed over a phone-numbers block's phone numbers
  name: Telnyx Phone Number Blocks Background Jobs API
  slug: telnyx-phone-number-blocks-background-jobs-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Phone number campaign assignment
  name: Telnyx Phone Number Campaigns API
  slug: telnyx-phone-number-campaigns-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Configure your phone numbers
  name: Telnyx Phone Number Configurations API
  slug: telnyx-phone-number-configurations-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Number orders
  name: Telnyx Phone Number Orders API
  slug: telnyx-phone-number-orders-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Determining portability of phone numbers
  name: Telnyx Phone Number Porting API
  slug: telnyx-phone-number-porting-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Number reservations
  name: Telnyx Phone Number Reservations API
  slug: telnyx-phone-number-reservations-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Number search
  name: Telnyx Phone Number Search API
  slug: telnyx-phone-number-search-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Endpoints related to porting orders management.
  name: Telnyx Porting Orders API
  slug: telnyx-porting-orders-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Presigned object URL operations
  name: Telnyx Presigned Object URLs API
  slug: telnyx-presigned-object-urls-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Private Wireless Gateways operations
  name: Telnyx Private Wireless Gateways API
  slug: telnyx-private-wireless-gateways-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Messaging profiles
  name: Telnyx Profiles API
  slug: telnyx-profiles-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Fax Applications operations
  name: Telnyx Programmable Fax Applications API
  slug: telnyx-programmable-fax-applications-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Programmable fax command operations
  name: Telnyx Programmable Fax Commands API
  slug: telnyx-programmable-fax-commands-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage pronunciation dictionaries for text-to-speech synthesis. Dictionaries contain alias items (text replacement) and phoneme items (IPA pronunciation notation) that control how specific words are s
  name: Telnyx Pronunciation Dictionaries API
  slug: telnyx-pronunciation-dictionaries-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Public Internet Gateway operations
  name: Telnyx Public Internet Gateways API
  slug: telnyx-public-internet-gateways-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Mobile push credential management
  name: Telnyx Push Credentials API
  slug: telnyx-push-credentials-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Queue commands operations
  name: Telnyx Queue Commands API
  slug: telnyx-queue-commands-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Send RCS messages
  name: Telnyx RCS API
  slug: telnyx-rcs-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Regions
  name: Telnyx Regions API
  slug: telnyx-regions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Regulatory Requirements
  name: Telnyx Regulatory Requirements API
  slug: telnyx-regulatory-requirements-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Wireless reporting operations
  name: Telnyx Reporting API
  slug: telnyx-reporting-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Ledger billing reports
  name: Telnyx Reports API
  slug: telnyx-reports-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Associate phone numbers with an enterprise for reputation monitoring and retrieve reputation scores
  name: Telnyx Reputation Phone Numbers API
  slug: telnyx-reputation-phone-numbers-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Requirement Groups
  name: Telnyx Requirement Groups API
  slug: telnyx-requirement-groups-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Types of requirements for international numbers and porting orders
  name: Telnyx Requirement Types API
  slug: telnyx-requirement-types-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Requirements for international numbers and porting orders
  name: Telnyx Requirements API
  slug: telnyx-requirements-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Rooms Compositions operations.
  name: Telnyx Room Compositions API
  slug: telnyx-room-compositions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Rooms Participants operations.
  name: Telnyx Room Participants API
  slug: telnyx-room-participants-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Rooms Recordings operations.
  name: Telnyx Room Recordings API
  slug: telnyx-room-recordings-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Rooms Sessions operations.
  name: Telnyx Room Sessions API
  slug: telnyx-room-sessions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Rooms operations.
  name: Telnyx Rooms API
  slug: telnyx-rooms-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Rooms Client Tokens operations.
  name: Telnyx Rooms Client Tokens API
  slug: telnyx-rooms-client-tokens-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Analyze voice AI sessions, costs, and event hierarchies across Telnyx products.
  name: Telnyx Session Analysis API
  slug: telnyx-session-analysis-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Observability into Telnyx platform stability and performance.
  name: Telnyx SETI Observability API
  slug: telnyx-seti-observability-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Shared Campaigns API from Telnyx — 4 operation(s) for shared campaigns.
  name: Telnyx Shared Campaigns API
  slug: telnyx-shared-campaigns-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Short codes
  name: Telnyx Short Codes API
  slug: telnyx-short-codes-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: View SIM card actions, their progress and timestamps using the SIM Card Actions API
  name: Telnyx SIM Card Actions API
  slug: telnyx-sim-card-actions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: SIM Card Group actions operations
  name: Telnyx SIM Card Group Actions API
  slug: telnyx-sim-card-group-actions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: SIM Card Groups operations
  name: Telnyx SIM Card Groups API
  slug: telnyx-sim-card-groups-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: SIM Card Orders operations
  name: Telnyx SIM Card Orders API
  slug: telnyx-sim-card-orders-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: SIM Cards operations
  name: Telnyx SIM Cards API
  slug: telnyx-sim-cards-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: SIPREC connectors configuration.
  name: Telnyx SIPREC Connectors API
  slug: telnyx-siprec-connectors-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Speech to text batch detail records
  name: Telnyx Speech to Text Batch Reports API
  slug: telnyx-speech-to-text-batch-reports-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Speech to text command operations
  name: Telnyx Speech To Text over WebSockets API
  slug: telnyx-speech-to-text-over-websockets-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Speech to text usage reports
  name: Telnyx Speech to text Usage Reports API
  slug: telnyx-speech-to-text-usage-reports-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Operations for managing stored payment transactions.
  name: Telnyx Stored Payment Transactions API
  slug: telnyx-stored-payment-transactions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Number lookup usage reports
  name: Telnyx Telco Data Usage Reports API
  slug: telnyx-telco-data-usage-reports-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Terms of Service agreement endpoints
  name: Telnyx Terms of Service API
  slug: telnyx-terms-of-service-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: TeXML Applications operations
  name: Telnyx TeXML Applications API
  slug: telnyx-texml-applications-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: TeXML REST Commands
  name: Telnyx TeXML REST Commands API
  slug: telnyx-texml-rest-commands-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Text to speech streaming command operations
  name: Telnyx Text To Speech Commands API
  slug: telnyx-text-to-speech-commands-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Traffic Policy Profiles operations
  name: Telnyx Traffic Policy Profiles API
  slug: telnyx-traffic-policy-profiles-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: UAC connection operations
  name: Telnyx UAC Connections API
  slug: telnyx-uac-connections-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Usage data reporting across Telnyx products
  name: Telnyx Usage Reports (BETA) API
  slug: telnyx-usage-reports-beta-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The User Bundles API from Telnyx — 5 operation(s) for user bundles.
  name: Telnyx User Bundles API
  slug: telnyx-user-bundles-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: User-defined tags for Telnyx resources
  name: Telnyx User Tags API
  slug: telnyx-user-tags-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Operations for working with UserAddress records. UserAddress records are stored addresses that users can use for non-emergency-calling purposes, such as for shipping addresses for orders of wireless S
  name: Telnyx UserAddresses API
  slug: telnyx-useraddresses-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage your tollfree verification requests
  name: Telnyx Verification Requests API
  slug: telnyx-verification-requests-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Verified Numbers operations
  name: Telnyx Verified Numbers API
  slug: telnyx-verified-numbers-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Two factor authentication API
  name: Telnyx Verify API
  slug: telnyx-verify-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Virtual Cross Connect operations
  name: Telnyx Virtual Cross Connects API
  slug: telnyx-virtual-cross-connects-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Voice Channels
  name: Telnyx Voice Channels API
  slug: telnyx-voice-channels-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Capture and manage voice identities as clones for use in text-to-speech synthesis.
  name: Telnyx Voice Clones API
  slug: telnyx-voice-clones-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Create and manage AI-generated voice designs using natural language prompts.
  name: Telnyx Voice Designs API
  slug: telnyx-voice-designs-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Voicemail API
  name: Telnyx Voicemail API
  slug: telnyx-voicemail-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The WDR Detail Reports API from Telnyx — 1 operation(s) for wdr detail reports.
  name: Telnyx WDR Detail Reports API
  slug: telnyx-wdr-detail-reports-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Webhooks operations
  name: Telnyx Webhooks API
  slug: telnyx-webhooks-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage Whatsapp business accounts
  name: Telnyx Whatsapp Business Accounts API
  slug: telnyx-whatsapp-business-accounts-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage Whatsapp message templates
  name: Telnyx Whatsapp Message Templates API
  slug: telnyx-whatsapp-message-templates-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Send Whatsapp messages
  name: Telnyx Whatsapp messaging API
  slug: telnyx-whatsapp-messaging-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage Whatsapp phone numbers
  name: Telnyx Whatsapp Phone Numbers API
  slug: telnyx-whatsapp-phone-numbers-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: WireGuard Interface operations
  name: Telnyx WireGuard Interfaces API
  slug: telnyx-wireguard-interfaces-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Wireless Blocklists operations
  name: Telnyx Wireless Blocklists API
  slug: telnyx-wireless-blocklists-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Regions for wireless services
  name: Telnyx Wireless Regions API
  slug: telnyx-wireless-regions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Operations for x402 cryptocurrency payment transactions. Fund your Telnyx account using USDC stablecoin payments via the x402 protocol.
  name: Telnyx x402 Payment Transactions API
  slug: telnyx-x402-payment-transactions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Callbacks
  name: Telnyx Callbacks API
  slug: telnyx-callbacks-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: IP operations
  name: Telnyx I Ps API
  slug: telnyx-ips-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Create and manage logical collections of your Telnyx data, tune retrieval settings, manage sources, and run collection-scoped semantic search.
  name: Telnyx AI Collections API
  slug: telnyx-ai-collections-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Anthropic Messages API from Telnyx — 1 operation(s) for anthropic messages.
  name: Telnyx Anthropic Messages API
  slug: telnyx-anthropic-messages-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: 'Agentic (bot) signup for Telnyx accounts. An AI agent solves a reverse-CAPTCHA challenge designed to be easy for LLMs and hard for humans, registers an account, and signs in by consuming a magic link '
  name: Telnyx Bot Signup API
  slug: telnyx-bot-signup-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage CloudFS filesystems — JuiceFS-compatible filesystems backed by Telnyx Cloud Storage
  name: Telnyx cloudfs filesystems API
  slug: telnyx-cloudfs-filesystems-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Read messages from the Telnyx vetting team and reply with clarifying information.
  name: Telnyx Comments API
  slug: telnyx-comments-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Page content retrieval for URLs.
  name: Telnyx Contents API
  slug: telnyx-contents-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Semantic vector search over ingested conversation history records with multi-region fan-out.
  name: Telnyx Conversation Histories API
  slug: telnyx-conversation-histories-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Beta API for evaluating shared context with typed questions and structured answers using Flash or Pro.
  name: Telnyx Decision Models API
  slug: telnyx-decision-models-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Submit and manage the two business references and one financial reference that vouch for a DIR. References are contacted to confirm the business identity during vetting.
  name: Telnyx DIR References API
  slug: telnyx-dir-references-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: A Display Identity Record (DIR) is the verified calling identity (display name, logo, call reasons) shown to recipients on outbound calls.
  name: Telnyx Display Identity Records API
  slug: telnyx-display-identity-records-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: DNS verification records for email domains
  name: Telnyx Email Domain DNS Records API
  slug: telnyx-email-domain-dns-records-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Email domain CRUD operations
  name: Telnyx Email Domains API
  slug: telnyx-email-domains-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Create, list, retrieve, update, delete, and send unsent draft messages belonging to an agent inbox.
  name: Telnyx Email Drafts API
  slug: telnyx-email-drafts-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Retrieve account-level email events and event statistics.
  name: Telnyx Email Events API
  slug: telnyx-email-events-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
  name: Telnyx Email Inboxes API
  slug: telnyx-email-inboxes-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Send and manage email messages. Legacy `/v2/emails` routes are aliases for these endpoints.
  name: Telnyx Email Messages API
  slug: telnyx-email-messages-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Async CSV import of competitor suppression lists.
  name: Telnyx Email Suppression Imports API
  slug: telnyx-email-suppression-imports-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Recipient suppression records (`/v2/email_blocks`).
  name: Telnyx Email Suppressions API
  slug: telnyx-email-suppressions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Create, list, retrieve, update, delete, and render Liquid email templates.
  name: Telnyx Email Templates API
  slug: telnyx-email-templates-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Account-wide conversation threads across every inbox, for agents operating many inboxes at once.
  name: Telnyx Email Threads API
  slug: telnyx-email-threads-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Named groups and group-scoped suppressions.
  name: Telnyx Email Unsubscribe Groups API
  slug: telnyx-email-unsubscribe-groups-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Validate email addresses synchronously or in asynchronous batches.
  name: Telnyx Email Validations API
  slug: telnyx-email-validations-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Verify ownership of a DIR's authorizer email. A short code is emailed and confirmed; the email must be verified before references can be submitted.
  name: Telnyx Email Verification API
  slug: telnyx-email-verification-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Per-domain webhook endpoints with event subscriptions
  name: Telnyx Email Webhooks API
  slug: telnyx-email-webhooks-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The functions API from Telnyx — 5 operation(s) for functions.
  name: Telnyx Functions API
  slug: telnyx-functions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Trademark or impersonation claims filed against your DIR. Customers may contest a claim with supporting evidence.
  name: Telnyx Infringement Claims API
  slug: telnyx-infringement-claims-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Read and write keys within a KV namespace
  name: Telnyx kv keys API
  slug: telnyx-kv-keys-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage KV storage namespaces
  name: Telnyx kv namespaces API
  slug: telnyx-kv-namespaces-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Machine payment (MPP) account-credit operations. Fund your Telnyx account programmatically from a machine or agent using the Machine Payment Protocol, an HTTP-402 flow settled via Stripe or Tempo.
  name: Telnyx Machine Payments API
  slug: telnyx-machine-payments-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Send real-time speech and chat actions to an active meeting session.
  name: Telnyx Meeting Session Actions API
  slug: telnyx-meeting-session-actions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Create and retrieve asynchronous summaries and action-item artifacts.
  name: Telnyx Meeting Session Artifacts API
  slug: telnyx-meeting-session-artifacts-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Read lifecycle events, transcript segments, and recordings for a meeting session.
  name: Telnyx Meeting Session Data API
  slug: telnyx-meeting-session-data-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Outbound webhook deliveries for meeting session events.
  name: Telnyx Meeting Session Webhooks API
  slug: telnyx-meeting-session-webhooks-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Create, list, retrieve, update, and stop meeting sessions.
  name: Telnyx Meeting Sessions API
  slug: telnyx-meeting-sessions-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Write memories into a profile and recall them.
  name: Telnyx Memory API
  slug: telnyx-memory-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The Namespaces API from Telnyx — 2 operation(s) for namespaces.
  name: Telnyx Namespaces API
  slug: telnyx-namespaces-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Noise suppression engines that can be selected when configuring noise suppression on voice connections.
  name: Telnyx Noise Suppression Engines API
  slug: telnyx-noise-suppression-engines-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Whether a write has finished.
  name: Telnyx Operations API
  slug: telnyx-operations-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Phone numbers are submitted to Telnyx for vetting in batches. Batches group all numbers added in a single request under the same Letter of Authorization.
  name: Telnyx Phone Number Batches API
  slug: telnyx-phone-number-batches-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Associate phone numbers with a verified DIR so calls from those numbers carry the DIR's display identity.
  name: Telnyx Phone Numbers API
  slug: telnyx-phone-numbers-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Public pricing operations
  name: Telnyx Pricing API
  slug: telnyx-pricing-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage RCS agent registration, testing, verification, and launch.
  name: Telnyx RCS Agents API
  slug: telnyx-rcs-agents-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage the legal business entities that operate RCS agents.
  name: Telnyx RCS Brands API
  slug: telnyx-rcs-brands-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: 'Static reference values the API accepts: call reasons, document types, rejection types.'
  name: Telnyx Reference Data API
  slug: telnyx-reference-data-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Phone-number reputation monitoring (spam-score lookup and tracking).
  name: Telnyx Reputation API
  slug: telnyx-reputation-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Deep research with citations and async task polling.
  name: Telnyx Research API
  slug: telnyx-research-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: How a namespace's summaries are written.
  name: Telnyx Settings API
  slug: telnyx-settings-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: What a profile stored, and what its memories came from.
  name: Telnyx Sources API
  slug: telnyx-sources-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Discover available speech-to-text providers, models, and supported languages.
  name: Telnyx Speech To Text Capabilities API
  slug: telnyx-speech-to-text-capabilities-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Daily and monthly spend limits per product. A limit applies to the organization of the authenticated user, or to the user's own account when they belong to no organization; every user of the organizat
  name: Telnyx Spend Limits API
  slug: telnyx-spend-limits-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Manage SQL databases and run SQL against them
  name: Telnyx sql databases API
  slug: telnyx-sql-databases-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Retrieve raw Voice SDK call report stats payloads for WebRTC call troubleshooting.
  name: Telnyx Voice SDK Stats API
  slug: telnyx-voice-sdk-stats-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: Real-time web search returning structured, LLM-ready JSON results.
  name: Telnyx Web Search API
  slug: telnyx-web-search-api
- baseURL: https://api.telnyx.com/v2
  baseurl_source: declared
  description: The x402 API from Telnyx — 3 operation(s) for x402.
  name: Telnyx X402 API
  slug: telnyx-x402-api
artifact_total: 586
asyncapis:
- description: ''
  name: Telnyx Webhooks
  slug: telnyx-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Telnyx Access Tokens API
  slug: open-telnyx-access-tokens-api
- collection_type: open
  name: Telnyx Access Tokens Addresses API
  slug: open-telnyx-addresses-api
- collection_type: open
  name: Telnyx Access Tokens Advanced Number Orders API
  slug: open-telnyx-advanced-number-orders-api
- collection_type: open
  name: Telnyx Access Tokens Assistants API
  slug: open-telnyx-assistants-api
- collection_type: open
  name: Telnyx Access Tokens Audio API
  slug: open-telnyx-audio-api
- collection_type: open
  name: Telnyx Access Tokens Audit Logs API
  slug: open-telnyx-audit-logs-api
- collection_type: open
  name: Telnyx Access Tokens Authentication Providers API
  slug: open-telnyx-authentication-providers-api
- collection_type: open
  name: Telnyx Access Tokens AutoRechargePreferences API
  slug: open-telnyx-autorechargepreferences-api
- collection_type: open
  name: Telnyx Access Tokens Billing API
  slug: open-telnyx-billing-api
- collection_type: open
  name: Telnyx Access Tokens Billing Groups API
  slug: open-telnyx-billing-groups-api
- collection_type: open
  name: Telnyx Access Tokens Brands API
  slug: open-telnyx-brands-api
- collection_type: open
  name: Telnyx Access Tokens Bucket SSL Certificate API
  slug: open-telnyx-bucket-ssl-certificate-api
- collection_type: open
  name: Telnyx Access Tokens Bucket Usage API
  slug: open-telnyx-bucket-usage-api
- collection_type: open
  name: Telnyx Access Tokens Bulk Phone Number Campaigns API
  slug: open-telnyx-bulk-phone-number-campaigns-api
- collection_type: open
  name: Telnyx Access Tokens Bulk Phone Number Operations API
  slug: open-telnyx-bulk-phone-number-operations-api
- collection_type: open
  name: Telnyx Access Tokens Bundles API
  slug: open-telnyx-bundles-api
- collection_type: open
  name: Telnyx Access Tokens Call Commands API
  slug: open-telnyx-call-commands-api
- collection_type: open
  name: Telnyx Access Tokens Call Control Applications API
  slug: open-telnyx-call-control-applications-api
- collection_type: open
  name: Telnyx Access Tokens Call Information API
  slug: open-telnyx-call-information-api
- collection_type: open
  name: Telnyx Access Tokens Call Recordings API
  slug: open-telnyx-call-recordings-api
- collection_type: open
  name: Telnyx Access Tokens Campaign API
  slug: open-telnyx-campaign-api
- collection_type: open
  name: Telnyx Access Tokens CDR Reports API
  slug: open-telnyx-cdr-reports-api
- collection_type: open
  name: Telnyx Access Tokens CDR Usage Reports API
  slug: open-telnyx-cdr-usage-reports-api
- collection_type: open
  name: Telnyx Access Tokens Charges Breakdown API
  slug: open-telnyx-charges-breakdown-api
- collection_type: open
  name: Telnyx Access Tokens Charges Summary API
  slug: open-telnyx-charges-summary-api
- collection_type: open
  name: Telnyx Access Tokens Chat API
  slug: open-telnyx-chat-api
- collection_type: open
  name: Telnyx Access Tokens Clusters API
  slug: open-telnyx-clusters-api
- collection_type: open
  name: Telnyx Access Tokens Conference Commands API
  slug: open-telnyx-conference-commands-api
- collection_type: open
  name: Telnyx Access Tokens Connections API
  slug: open-telnyx-connections-api
- collection_type: open
  name: Telnyx Access Tokens Conversations API
  slug: open-telnyx-conversations-api
- collection_type: open
  name: Telnyx Access Tokens Country Coverage API
  slug: open-telnyx-country-coverage-api
- collection_type: open
  name: Telnyx Access Tokens Coverage API
  slug: open-telnyx-coverage-api
- collection_type: open
  name: Telnyx Access Tokens Credential Connections API
  slug: open-telnyx-credential-connections-api
- collection_type: open
  name: Telnyx Access Tokens Credentials API
  slug: open-telnyx-credentials-api
- collection_type: open
  name: Telnyx Access Tokens CSV Downloads API
  slug: open-telnyx-csv-downloads-api
- collection_type: open
  name: Telnyx Access Tokens Customer Service Record API
  slug: open-telnyx-customer-service-record-api
- collection_type: open
  name: Telnyx Access Tokens Data Migration API
  slug: open-telnyx-data-migration-api
- collection_type: open
  name: Telnyx Access Tokens Debugging API
  slug: open-telnyx-debugging-api
- collection_type: open
  name: Telnyx Access Tokens Detail Records API
  slug: open-telnyx-detail-records-api
- collection_type: open
  name: Telnyx Access Tokens Dialogflow Integration API
  slug: open-telnyx-dialogflow-integration-api
- collection_type: open
  name: Telnyx Access Tokens Documents API
  slug: open-telnyx-documents-api
- collection_type: open
  name: Telnyx Access Tokens Dynamic Emergency Addresses API
  slug: open-telnyx-dynamic-emergency-addresses-api
- collection_type: open
  name: Telnyx Access Tokens Dynamic Emergency Endpoints API
  slug: open-telnyx-dynamic-emergency-endpoints-api
- collection_type: open
  name: Telnyx Access Tokens Embeddings API
  slug: open-telnyx-embeddings-api
- collection_type: open
  name: Telnyx Access Tokens Enterprises API
  slug: open-telnyx-enterprises-api
- collection_type: open
  name: Telnyx Access Tokens Enum API
  slug: open-telnyx-enum-api
- collection_type: open
  name: Telnyx Access Tokens External Connections API
  slug: open-telnyx-external-connections-api
- collection_type: open
  name: Telnyx Access Tokens Fine Tuning API
  slug: open-telnyx-fine-tuning-api
- collection_type: open
  name: Telnyx Access Tokens FQDN Connections API
  slug: open-telnyx-fqdn-connections-api
- collection_type: open
  name: Telnyx Access Tokens FQDNs API
  slug: open-telnyx-fqdns-api
- collection_type: open
  name: Telnyx Access Tokens Global IPs API
  slug: open-telnyx-global-ips-api
- collection_type: open
  name: Telnyx Access Tokens Hosted Numbers API
  slug: open-telnyx-hosted-numbers-api
- collection_type: open
  name: Telnyx Access Tokens Inexplicit Number Orders API
  slug: open-telnyx-inexplicit-number-orders-api
- collection_type: open
  name: Telnyx Access Tokens Integration Secrets API
  slug: open-telnyx-integration-secrets-api
- collection_type: open
  name: Telnyx Access Tokens Integrations API
  slug: open-telnyx-integrations-api
- collection_type: open
  name: Telnyx Access Tokens Inventory Level API
  slug: open-telnyx-inventory-level-api
- collection_type: open
  name: Telnyx Access Tokens Invoices API
  slug: open-telnyx-invoices-api
- collection_type: open
  name: Telnyx Access Tokens IP Addresses API
  slug: open-telnyx-ip-addresses-api
- collection_type: open
  name: Telnyx Access Tokens IP Connections API
  slug: open-telnyx-ip-connections-api
- collection_type: open
  name: Telnyx Access Tokens IP Ranges API
  slug: open-telnyx-ip-ranges-api
- collection_type: open
  name: Telnyx Access Tokens IPs API
  slug: open-telnyx-ips-api
- collection_type: open
  name: Telnyx Access Tokens Managed Accounts API
  slug: open-telnyx-managed-accounts-api
- collection_type: open
  name: Telnyx Access Tokens MCP Servers API
  slug: open-telnyx-mcp-servers-api
- collection_type: open
  name: Telnyx Access Tokens MDR Detail Reports API
  slug: open-telnyx-mdr-detail-reports-api
- collection_type: open
  name: Telnyx Access Tokens MDR Detailed Reports API
  slug: open-telnyx-mdr-detailed-reports-api
- collection_type: open
  name: Telnyx Access Tokens MDR Usage Reports API
  slug: open-telnyx-mdr-usage-reports-api
- collection_type: open
  name: Telnyx Access Tokens Media Storage API API
  slug: open-telnyx-media-storage-api-api
- collection_type: open
  name: Telnyx Access Tokens Messages API
  slug: open-telnyx-messages-api
- collection_type: open
  name: Telnyx Access Tokens Messaging API
  slug: open-telnyx-messaging-api
- collection_type: open
  name: Telnyx Access Tokens Messaging URL Domains API
  slug: open-telnyx-messaging-url-domains-api
- collection_type: open
  name: Telnyx Access Tokens Missions API
  slug: open-telnyx-missions-api
- collection_type: open
  name: Telnyx Access Tokens Mobile Network Operators API
  slug: open-telnyx-mobile-network-operators-api
- collection_type: open
  name: Telnyx Access Tokens Mobile Number Settings API
  slug: open-telnyx-mobile-number-settings-api
- collection_type: open
  name: Telnyx Access Tokens Mobile Phone Numbers API
  slug: open-telnyx-mobile-phone-numbers-api
- collection_type: open
  name: Telnyx Access Tokens Mobile Voice Connections API
  slug: open-telnyx-mobile-voice-connections-api
- collection_type: open
  name: Telnyx Access Tokens Networks API
  slug: open-telnyx-networks-api
- collection_type: open
  name: Telnyx Access Tokens Notifications API
  slug: open-telnyx-notifications-api
- collection_type: open
  name: Telnyx Access Tokens Number Lookup API
  slug: open-telnyx-number-lookup-api
- collection_type: open
  name: Telnyx Access Tokens Number Portout API
  slug: open-telnyx-number-portout-api
- collection_type: open
  name: Telnyx Access Tokens Number Reputation Settings API
  slug: open-telnyx-number-reputation-settings-api
- collection_type: open
  name: Telnyx Access Tokens Number Settings API
  slug: open-telnyx-number-settings-api
- collection_type: open
  name: Telnyx Access Tokens numbers features API
  slug: open-telnyx-numbers-features-api
- collection_type: open
  name: Telnyx Access Tokens OAuth Clients API
  slug: open-telnyx-oauth-clients-api
- collection_type: open
  name: Telnyx Access Tokens OAuth Discovery API
  slug: open-telnyx-oauth-discovery-api
- collection_type: open
  name: Telnyx Access Tokens OAuth Grants API
  slug: open-telnyx-oauth-grants-api
- collection_type: open
  name: Telnyx Access Tokens OAuth Protocol API
  slug: open-telnyx-oauth-protocol-api
- collection_type: open
  name: Telnyx Access Tokens OpenAI Chat API
  slug: open-telnyx-openai-chat-api
- collection_type: open
  name: Telnyx Access Tokens OpenAI Embeddings API
  slug: open-telnyx-openai-embeddings-api
- collection_type: open
  name: Telnyx Access Tokens Opt-Out Management API
  slug: open-telnyx-opt-out-management-api
- collection_type: open
  name: Telnyx Access Tokens Organization Users API
  slug: open-telnyx-organization-users-api
- collection_type: open
  name: Telnyx Access Tokens OTA updates API
  slug: open-telnyx-ota-updates-api
- collection_type: open
  name: Telnyx Access Tokens Outbound Voice Profiles API
  slug: open-telnyx-outbound-voice-profiles-api
- collection_type: open
  name: Telnyx Access Tokens Phone Number Block Orders API
  slug: open-telnyx-phone-number-block-orders-api
- collection_type: open
  name: Telnyx Access Tokens Phone Number Blocks Background Jobs API
  slug: open-telnyx-phone-number-blocks-background-jobs-api
- collection_type: open
  name: Telnyx Access Tokens Phone Number Campaigns API
  slug: open-telnyx-phone-number-campaigns-api
- collection_type: open
  name: Telnyx Access Tokens Phone Number Configurations API
  slug: open-telnyx-phone-number-configurations-api
- collection_type: open
  name: Telnyx Access Tokens Phone Number Orders API
  slug: open-telnyx-phone-number-orders-api
- collection_type: open
  name: Telnyx Access Tokens Phone Number Porting API
  slug: open-telnyx-phone-number-porting-api
- collection_type: open
  name: Telnyx Access Tokens Phone Number Reservations API
  slug: open-telnyx-phone-number-reservations-api
- collection_type: open
  name: Telnyx Access Tokens Phone Number Search API
  slug: open-telnyx-phone-number-search-api
- collection_type: open
  name: Telnyx Access Tokens Porting Orders API
  slug: open-telnyx-porting-orders-api
- collection_type: open
  name: Telnyx Access Tokens Presigned Object URLs API
  slug: open-telnyx-presigned-object-urls-api
- collection_type: open
  name: Telnyx Access Tokens Private Wireless Gateways API
  slug: open-telnyx-private-wireless-gateways-api
- collection_type: open
  name: Telnyx Access Tokens Profiles API
  slug: open-telnyx-profiles-api
- collection_type: open
  name: Telnyx Access Tokens Programmable Fax Applications API
  slug: open-telnyx-programmable-fax-applications-api
- collection_type: open
  name: Telnyx Access Tokens Programmable Fax Commands API
  slug: open-telnyx-programmable-fax-commands-api
- collection_type: open
  name: Telnyx Access Tokens Pronunciation Dictionaries API
  slug: open-telnyx-pronunciation-dictionaries-api
- collection_type: open
  name: Telnyx Access Tokens Public Internet Gateways API
  slug: open-telnyx-public-internet-gateways-api
- collection_type: open
  name: Telnyx Access Tokens Push Credentials API
  slug: open-telnyx-push-credentials-api
- collection_type: open
  name: Telnyx Access Tokens Queue Commands API
  slug: open-telnyx-queue-commands-api
- collection_type: open
  name: Telnyx Access Tokens RCS API
  slug: open-telnyx-rcs-api
- collection_type: open
  name: Telnyx Access Tokens Regions API
  slug: open-telnyx-regions-api
- collection_type: open
  name: Telnyx Access Tokens Regulatory Requirements API
  slug: open-telnyx-regulatory-requirements-api
- collection_type: open
  name: Telnyx Access Tokens Reporting API
  slug: open-telnyx-reporting-api
- collection_type: open
  name: Telnyx Access Tokens Reports API
  slug: open-telnyx-reports-api
- collection_type: open
  name: Telnyx Access Tokens Reputation Phone Numbers API
  slug: open-telnyx-reputation-phone-numbers-api
- collection_type: open
  name: Telnyx Access Tokens Requirement Groups API
  slug: open-telnyx-requirement-groups-api
- collection_type: open
  name: Telnyx Access Tokens Requirement Types API
  slug: open-telnyx-requirement-types-api
- collection_type: open
  name: Telnyx Access Tokens Requirements API
  slug: open-telnyx-requirements-api
- collection_type: open
  name: Telnyx Access Tokens Room Compositions API
  slug: open-telnyx-room-compositions-api
- collection_type: open
  name: Telnyx Access Tokens Room Participants API
  slug: open-telnyx-room-participants-api
- collection_type: open
  name: Telnyx Access Tokens Room Recordings API
  slug: open-telnyx-room-recordings-api
- collection_type: open
  name: Telnyx Access Tokens Room Sessions API
  slug: open-telnyx-room-sessions-api
- collection_type: open
  name: Telnyx Access Tokens Rooms API
  slug: open-telnyx-rooms-api
- collection_type: open
  name: Telnyx Access Tokens Rooms Client Tokens API
  slug: open-telnyx-rooms-client-tokens-api
- collection_type: open
  name: Telnyx Access Tokens Session Analysis API
  slug: open-telnyx-session-analysis-api
- collection_type: open
  name: Telnyx Access Tokens SETI Observability API
  slug: open-telnyx-seti-observability-api
- collection_type: open
  name: Telnyx Access Tokens Shared Campaigns API
  slug: open-telnyx-shared-campaigns-api
- collection_type: open
  name: Telnyx Access Tokens Short Codes API
  slug: open-telnyx-short-codes-api
- collection_type: open
  name: Telnyx Access Tokens SIM Card Actions API
  slug: open-telnyx-sim-card-actions-api
- collection_type: open
  name: Telnyx Access Tokens SIM Card Group Actions API
  slug: open-telnyx-sim-card-group-actions-api
- collection_type: open
  name: Telnyx Access Tokens SIM Card Groups API
  slug: open-telnyx-sim-card-groups-api
- collection_type: open
  name: Telnyx Access Tokens SIM Card Orders API
  slug: open-telnyx-sim-card-orders-api
- collection_type: open
  name: Telnyx Access Tokens SIM Cards API
  slug: open-telnyx-sim-cards-api
- collection_type: open
  name: Telnyx Access Tokens SIPREC Connectors API
  slug: open-telnyx-siprec-connectors-api
- collection_type: open
  name: Telnyx Access Tokens Speech to Text Batch Reports API
  slug: open-telnyx-speech-to-text-batch-reports-api
- collection_type: open
  name: Telnyx Access Tokens Speech To Text over WebSockets API
  slug: open-telnyx-speech-to-text-over-websockets-api
- collection_type: open
  name: Telnyx Access Tokens Speech to text Usage Reports API
  slug: open-telnyx-speech-to-text-usage-reports-api
- collection_type: open
  name: Telnyx Access Tokens Stored Payment Transactions API
  slug: open-telnyx-stored-payment-transactions-api
- collection_type: open
  name: Telnyx Access Tokens Telco Data Usage Reports API
  slug: open-telnyx-telco-data-usage-reports-api
- collection_type: open
  name: Telnyx Access Tokens Terms of Service API
  slug: open-telnyx-terms-of-service-api
- collection_type: open
  name: Telnyx Access Tokens TeXML Applications API
  slug: open-telnyx-texml-applications-api
- collection_type: open
  name: Telnyx Access Tokens TeXML REST Commands API
  slug: open-telnyx-texml-rest-commands-api
- collection_type: open
  name: Telnyx Access Tokens Text To Speech Commands API
  slug: open-telnyx-text-to-speech-commands-api
- collection_type: open
  name: Telnyx Access Tokens Traffic Policy Profiles API
  slug: open-telnyx-traffic-policy-profiles-api
- collection_type: open
  name: Telnyx Access Tokens UAC Connections API
  slug: open-telnyx-uac-connections-api
- collection_type: open
  name: Telnyx Access Tokens Usage Reports (BETA) API
  slug: open-telnyx-usage-reports-beta-api
- collection_type: open
  name: Telnyx Access Tokens User Bundles API
  slug: open-telnyx-user-bundles-api
- collection_type: open
  name: Telnyx Access Tokens User Tags API
  slug: open-telnyx-user-tags-api
- collection_type: open
  name: Telnyx Access Tokens UserAddresses API
  slug: open-telnyx-useraddresses-api
- collection_type: open
  name: Telnyx Access Tokens Verification Requests API
  slug: open-telnyx-verification-requests-api
- collection_type: open
  name: Telnyx Access Tokens Verified Numbers API
  slug: open-telnyx-verified-numbers-api
- collection_type: open
  name: Telnyx Access Tokens Verify API
  slug: open-telnyx-verify-api
- collection_type: open
  name: Telnyx Access Tokens Virtual Cross Connects API
  slug: open-telnyx-virtual-cross-connects-api
- collection_type: open
  name: Telnyx Access Tokens Voice Channels API
  slug: open-telnyx-voice-channels-api
- collection_type: open
  name: Telnyx Access Tokens Voice Clones API
  slug: open-telnyx-voice-clones-api
- collection_type: open
  name: Telnyx Access Tokens Voice Designs API
  slug: open-telnyx-voice-designs-api
- collection_type: open
  name: Telnyx Access Tokens Voicemail API
  slug: open-telnyx-voicemail-api
- collection_type: open
  name: Telnyx Access Tokens WDR Detail Reports API
  slug: open-telnyx-wdr-detail-reports-api
- collection_type: open
  name: Telnyx Access Tokens Webhooks API
  slug: open-telnyx-webhooks-api
- collection_type: open
  name: Telnyx Access Tokens Whatsapp Business Accounts API
  slug: open-telnyx-whatsapp-business-accounts-api
- collection_type: open
  name: Telnyx Access Tokens Whatsapp Message Templates API
  slug: open-telnyx-whatsapp-message-templates-api
- collection_type: open
  name: Telnyx Access Tokens Whatsapp messaging API
  slug: open-telnyx-whatsapp-messaging-api
- collection_type: open
  name: Telnyx Access Tokens Whatsapp Phone Numbers API
  slug: open-telnyx-whatsapp-phone-numbers-api
- collection_type: open
  name: Telnyx Access Tokens WireGuard Interfaces API
  slug: open-telnyx-wireguard-interfaces-api
- collection_type: open
  name: Telnyx Access Tokens Wireless Blocklists API
  slug: open-telnyx-wireless-blocklists-api
- collection_type: open
  name: Telnyx Access Tokens Wireless Regions API
  slug: open-telnyx-wireless-regions-api
- collection_type: open
  name: Telnyx Access Tokens x402 Payment Transactions API
  slug: open-telnyx-x402-payment-transactions-api
- collection_type: open
  name: Telnyx API
  slug: open-telnyx
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/rules/telnyx-rules.yml
  title: ''
  type: Spectral
  url: rules/telnyx-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/json-ld/telnyx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/telnyx-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/vocabulary/telnyx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/telnyx-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/asyncapi/telnyx-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/telnyx-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/data-model/telnyx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/telnyx-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/conventions/telnyx-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/telnyx-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/conventions/telnyx-conventions.yml
  title: ''
  type: Conventions
  url: conventions/telnyx-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.telnyx.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/errors/telnyx-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/telnyx-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/conformance/telnyx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/telnyx-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/llms/telnyx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/telnyx-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/a2a/telnyx-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/telnyx-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/mcp/telnyx-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/telnyx-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/well-known/telnyx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/telnyx-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/hosts/telnyx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/telnyx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/vendors/telnyx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/telnyx-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/packages/telnyx-packages.yml
  title: ''
  type: SDKs
  url: packages/telnyx-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/packages/telnyx-packages.yml
  title: ''
  type: Packages
  url: packages/telnyx-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://telnyx.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.telnyx.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.telnyx.com/
- group: start
  title: ''
  type: SignUp
  url: https://telnyx.com/sign-up
- group: auth
  title: ''
  type: Security
  url: https://telnyx.com/security
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.telnyx.com/docs/inference/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://telnyx.com/release-notes
- group: docs
  title: ''
  type: Documentation
  url: https://developers.telnyx.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.telnyx.com/api-reference/embeddings/embed-documents
- group: commercial
  title: ''
  type: Pricing
  url: https://telnyx.com/pricing/iot-data-plans
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/capabilities/telnyx-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/telnyx-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/agentic-access/telnyx-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/telnyx-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/security/telnyx-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/telnyx-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/security/telnyx-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/telnyx-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/security/telnyx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/telnyx-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/authentication/telnyx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/telnyx-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/scopes/telnyx-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/telnyx-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/team-telnyx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telnyx
- group: company
  title: ''
  type: Website
  url: https://telnyx.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/plans/telnyx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/telnyx-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/rate-limits/telnyx-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/telnyx-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/finops/telnyx-finops.yml
  title: ''
  type: FinOps
  url: finops/telnyx-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://telnyx.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://telnyx.com/rss.xml
created: '2026-05-08'
description: Telnyx is a private‑IP cloud communications platform that provides a comprehensive suite of real‑time communications APIs. It enables developers to embed voice calling, SMS, MMS, fax, number management, IoT SIM connectivity, AI inference, and authentication capabilities into applications. Telnyx offers programmable SIP trunks, global phone numbers, messaging services, and edge compute resources, supporting use cases from contact centers to AI‑driven agents and IoT deployments.
finops:
- name: Telnyx Finops
  service_category: Communications
  slug: telnyx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telnyx.png
json_schemas:
- name: AcceptSuggestionsRequest
  property_count: 1
  slug: telnyx-accept-suggestions-request
- name: AccessIPAddressListResponseSchema
  property_count: 2
  slug: telnyx-access-ipaddress-list-response-schema
- name: AccessIPAddressPOST
  property_count: 2
  slug: telnyx-access-ipaddress-post
- name: AccessIPAddressResponseSchema
  property_count: 8
  slug: telnyx-access-ipaddress-response-schema
- name: AccessIPRangeListResponseSchema
  property_count: 2
  slug: telnyx-access-iprange-list-response-schema
- name: AccessIPRangePOST
  property_count: 2
  slug: telnyx-access-iprange-post
- name: AccessIPRangeResponseSchema
  property_count: 7
  slug: telnyx-access-iprange-response-schema
- name: AddressCreate
  property_count: 15
  slug: telnyx-address-create
- name: AddressSuggestionResponse
  property_count: 1
  slug: telnyx-address-suggestion-response
- name: AdvancedOrderRequest
  property_count: 8
  slug: telnyx-advanced-order-request
- name: Answer Request
  property_count: 31
  slug: telnyx-answer-request
- name: AssignProfileToCampaignRequest
  property_count: 3
  slug: telnyx-assign-profile-to-campaign-request
- name: AssignProfileToCampaignResponse
  property_count: 4
  slug: telnyx-assign-profile-to-campaign-response
- name: AssignmentTaskStatusResponse
  property_count: 4
  slug: telnyx-assignment-task-status-response
- name: AssistantTestResponse
  property_count: 10
  slug: telnyx-assistant-test-response
- name: AudioTranscriptionRequest
  property_count: 7
  slug: telnyx-audio-transcription-request
- name: AudioTranscriptionResponse
  property_count: 4
  slug: telnyx-audio-transcription-response
- name: AuthenticationProviderCreate
  property_count: 5
  slug: telnyx-authentication-provider-create
- name: AuthenticationProvider
  property_count: 10
  slug: telnyx-authentication-provider
- name: AutoRechargePrefRequest
  property_count: 5
  slug: telnyx-auto-recharge-pref-request
- name: BillingBundleResponse
  property_count: 1
  slug: telnyx-billing-bundle-response
- name: BillingGroup
  property_count: 7
  slug: telnyx-billing-group
- name: BrandSmsOtpStatus
  property_count: 8
  slug: telnyx-brand-sms-otp-status
- name: Bridge Request
  property_count: 20
  slug: telnyx-bridge-request
- name: BucketAPIUsageResponse
  property_count: 3
  slug: telnyx-bucket-apiusage-response
- name: BucketUsage
  property_count: 4
  slug: telnyx-bucket-usage
- name: Dial Request
  property_count: 60
  slug: telnyx-call-request
- name: CampaignCost
  property_count: 4
  slug: telnyx-campaign-cost
- name: CampaignRecordSet_CSP
  property_count: 3
  slug: telnyx-campaign-record-set-csp
- name: CampaignRequest
  property_count: 35
  slug: telnyx-campaign-request
- name: CdrAvailableFieldsResponse
  property_count: 4
  slug: telnyx-cdr-available-fields-response
- name: CdrDeleteDetailReportResponse
  property_count: 1
  slug: telnyx-cdr-delete-detail-report-response
- name: CdrDeleteUsageReportResponse
  property_count: 1
  slug: telnyx-cdr-delete-usage-report-response
- name: CdrDetailedRequest
  property_count: 13
  slug: telnyx-cdr-detailed-request
- name: CdrGetDetailReportByIdResponse
  property_count: 1
  slug: telnyx-cdr-get-detail-report-by-id-response
- name: CdrGetDetailReportResponse
  property_count: 2
  slug: telnyx-cdr-get-detail-report-response
- name: CdrGetSyncUsageReportResponse
  property_count: 1
  slug: telnyx-cdr-get-sync-usage-report-response
- name: CdrGetUsageReportByIdResponse
  property_count: 1
  slug: telnyx-cdr-get-usage-report-by-id-response
- name: CdrGetUsageReportsResponse
  property_count: 2
  slug: telnyx-cdr-get-usage-reports-response
- name: CdrPostUsageReportResponse
  property_count: 1
  slug: telnyx-cdr-post-usage-report-response
- name: ChatCompletionRequest
  property_count: 26
  slug: telnyx-chat-completion-request
- name: ClusteringRequestInfoData
  property_count: 2
  slug: telnyx-clustering-request-info-data
- name: ClusteringStatusResponseData
  property_count: 1
  slug: telnyx-clustering-status-response-data
- name: Conference Gather Using Audio Request
  property_count: 16
  slug: telnyx-conference-gather-using-audio-request
- name: Conference Speak Request
  property_count: 8
  slug: telnyx-conference-speak-request
- name: Conversation
  property_count: 5
  slug: telnyx-conversation
- name: CreateAssistantRequest
  property_count: 27
  slug: telnyx-create-assistant-request
- name: CreateAssistantTestRequest
  property_count: 8
  slug: telnyx-create-assistant-test-request
- name: CreateBrand
  property_count: 24
  slug: telnyx-create-brand
- name: Create Call Control Application Request
  property_count: 14
  slug: telnyx-create-call-control-application-request
- name: Create Conference Request
  property_count: 12
  slug: telnyx-create-conference-request
- name: CreateConversationRequest
  property_count: 2
  slug: telnyx-create-conversation-request
- name: Create Credential Connection Request
  property_count: 25
  slug: telnyx-create-credential-connection-request
- name: CreateDocServiceDocumentRequest
  property_count: 4
  slug: telnyx-create-doc-service-document-request
- name: Create External Connection Request
  property_count: 8
  slug: telnyx-create-external-connection-request
- name: Create Upload Request
  property_count: 5
  slug: telnyx-create-external-connection-upload-request
- name: CreateFineTuningJobRequest
  property_count: 4
  slug: telnyx-create-fine-tuning-job-request
- name: Create FQDN Connection Request
  property_count: 24
  slug: telnyx-create-fqdn-connection-request
- name: Create Fqdn Request
  property_count: 4
  slug: telnyx-create-fqdn-request
- name: CreateIntegrationSecretRequest
  property_count: 5
  slug: telnyx-create-integration-secret-request
- name: Create IP Connection Request
  property_count: 23
  slug: telnyx-create-ip-connection-request
- name: Create Managed Account Request
  property_count: 5
  slug: telnyx-create-managed-account-request
- name: CreateMCPServerRequest
  property_count: 5
  slug: telnyx-create-mcpserver-request
- name: CreateMessagingHostedNumberOrderRequest
  property_count: 2
  slug: telnyx-create-messaging-hosted-number-order-request
- name: CreateMsgReq
  property_count: 8
  slug: telnyx-create-msg-req
- name: CreateMultiPartDocServiceDocumentRequest
  property_count: 2
  slug: telnyx-create-multi-part-doc-service-document-request
- name: CreatedVerificationCodesResponse
  property_count: 1
  slug: telnyx-created-verification-codes-response
- name: DetailRecordsSearchResponse
  property_count: 2
  slug: telnyx-detail-records-search-response
- name: DocServiceDocument
  property_count: 0
  slug: telnyx-doc-service-document
- name: DynamicEmergencyAddress
  property_count: 17
  slug: telnyx-dynamic-emergency-address
- name: DynamicEmergencyEndpoint
  property_count: 9
  slug: telnyx-dynamic-emergency-endpoint
- name: EligibilityNumbersRequest
  property_count: 1
  slug: telnyx-eligibility-numbers-request
- name: EmbeddingBucketRequest
  property_count: 5
  slug: telnyx-embedding-bucket-request
- name: EmbeddingResponse
  property_count: 1
  slug: telnyx-embedding-response
- name: EmbeddingSimilaritySearchRequest
  property_count: 3
  slug: telnyx-embedding-similarity-search-request
- name: EmbeddingSimilaritySearchResponse
  property_count: 1
  slug: telnyx-embedding-similarity-search-response
- name: EmbeddingUrlRequest
  property_count: 2
  slug: telnyx-embedding-url-request
- name: EnterpriseCreate
  property_count: 19
  slug: telnyx-enterprise-create
- name: EnterpriseListPublic
  property_count: 2
  slug: telnyx-enterprise-list-public
- name: EnterprisePublicWrapped
  property_count: 1
  slug: telnyx-enterprise-public-wrapped
- name: EnterpriseUpdate
  property_count: 16
  slug: telnyx-enterprise-update
- name: EnumObjecToObjecttResponse
  property_count: 0
  slug: telnyx-enum-objec-to-objectt-response
- name: EnumObjectListResponse
  property_count: 0
  slug: telnyx-enum-object-list-response
- name: EnumObjectToStringResponse
  property_count: 0
  slug: telnyx-enum-object-to-string-response
- name: EnumPaginatedResponse
  property_count: 3
  slug: telnyx-enum-paginated-response
- name: EnumStringListResponse
  property_count: 0
  slug: telnyx-enum-string-list-response
- name: ExternalVetting
  property_count: 7
  slug: telnyx-external-vetting
- name: FineTuningJob
  property_count: 9
  slug: telnyx-fine-tuning-job
- name: FineTuningJobListData
  property_count: 1
  slug: telnyx-fine-tuning-jobs-list-data
- name: Gather Using Speak Request
  property_count: 16
  slug: telnyx-gather-using-speak-request
- name: GlobalIpAssignment
  property_count: 0
  slug: telnyx-global-ip-assignment
- name: GlobalIpAssignmentUpdate
  property_count: 0
  slug: telnyx-global-ip-assignment-update
- name: GlobalIP
  property_count: 0
  slug: telnyx-global-ip
- name: GlobalIPHealthCheck
  property_count: 0
  slug: telnyx-global-iphealth-check
- name: ImportExternalVetting
  property_count: 3
  slug: telnyx-import-external-vetting
- name: InboundMessagePayload
  property_count: 27
  slug: telnyx-inbound-message-payload
- name: InexplicitNumberOrderRequest
  property_count: 5
  slug: telnyx-inexplicit-number-order-request
- name: inference-embedding_Assistant
  property_count: 33
  slug: telnyx-inference-embedding-assistant
- name: InsightTemplateCreateReq
  property_count: 4
  slug: telnyx-insight-template-create-req
- name: InsightTemplateUpdateReq
  property_count: 4
  slug: telnyx-insight-template-update-req
- name: IntegrationConnectionResponse
  property_count: 1
  slug: telnyx-integration-connection-response
- name: IntegrationConnectionsListResponse
  property_count: 1
  slug: telnyx-integration-connections-list-response
- name: Integration
  property_count: 7
  slug: telnyx-integration
- name: IntegrationSecretCreatedResponse
  property_count: 1
  slug: telnyx-integration-secret-created-response
- name: SecretsListData
  property_count: 2
  slug: telnyx-integration-secrets-list-data
- name: IntegrationsListResponse
  property_count: 1
  slug: telnyx-integrations-list-response
- name: Invoice
  property_count: 6
  slug: telnyx-invoice
- name: Join Conference Request
  property_count: 14
  slug: telnyx-join-conference-request
- name: MCPServer
  property_count: 7
  slug: telnyx-mcpserver
- name: MCPServersListResponse
  property_count: 0
  slug: telnyx-mcpservers-list-response
- name: MdrDeleteDetailReportResponse
  property_count: 1
  slug: telnyx-mdr-delete-detail-report-response
- name: MdrDeleteUsageReportResponse
  property_count: 1
  slug: telnyx-mdr-delete-usage-report-response
- name: MdrDetailedRequest
  property_count: 12
  slug: telnyx-mdr-detailed-request
- name: MdrGetDetailReportByIdResponse
  property_count: 1
  slug: telnyx-mdr-get-detail-report-by-id-response
- name: MdrGetDetailReportResponse
  property_count: 2
  slug: telnyx-mdr-get-detail-report-response
- name: MdrGetDetailResponse
  property_count: 2
  slug: telnyx-mdr-get-detail-response
- name: MdrGetUsageReportByIdResponse
  property_count: 1
  slug: telnyx-mdr-get-usage-report-by-id-response
- name: MdrGetUsageReportsResponse
  property_count: 2
  slug: telnyx-mdr-get-usage-reports-response
- name: MdrPostDetailReportResponse
  property_count: 1
  slug: telnyx-mdr-post-detail-report-response
- name: MdrPostUsageReportRequest
  property_count: 4
  slug: telnyx-mdr-post-usage-report-request
- name: MdrUsageRequestLegacy
  property_count: 6
  slug: telnyx-mdr-usage-request-legacy
- name: MigrationParams
  property_count: 12
  slug: telnyx-migration-params
- name: MigrationSourceCoverageParams
  property_count: 2
  slug: telnyx-migration-source-coverage-params
- name: MigrationSourceParams
  property_count: 5
  slug: telnyx-migration-source-params
- name: ModelsResponse
  property_count: 2
  slug: telnyx-models-response
- name: MonthlyChargesBreakdownResponse
  property_count: 1
  slug: telnyx-monthly-charges-breakdown-response
- name: MonthlyChargesSummaryResponse
  property_count: 1
  slug: telnyx-monthly-charges-summary-response
- name: NewBillingGroup
  property_count: 1
  slug: telnyx-new-billing-group
- name: OutboundMessagePayloadCancelled
  property_count: 28
  slug: telnyx-outbound-message-payload-cancelled
- name: OutboundMessagePayload
  property_count: 29
  slug: telnyx-outbound-message-payload
- name: PaginatedBillingBundlesResponse
  property_count: 2
  slug: telnyx-paginated-billing-bundles-response
- name: PaginationMeta
  property_count: 4
  slug: telnyx-pagination-meta
- name: PaginationMetaSimple
  property_count: 4
  slug: telnyx-pagination-meta-simple
- name: PhoneNumberStatusResponsePaginated
  property_count: 1
  slug: telnyx-phone-number-status-response-paginated
- name: PhoneNumbersJobDeletePhoneNumbersRequest
  property_count: 1
  slug: telnyx-phone-numbers-job-delete-phone-numbers-request
- name: PhoneNumbersJob
  property_count: 11
  slug: telnyx-phone-numbers-job
- name: PhoneNumbersJobUpdateEmergencySettingsRequest
  property_count: 3
  slug: telnyx-phone-numbers-job-update-emergency-settings-request
- name: PhoneNumbersJobUpdatePhoneNumbersRequest
  property_count: 9
  slug: telnyx-phone-numbers-job-update-phone-numbers-request
- name: PublicTextClusteringRequest
  property_count: 5
  slug: telnyx-public-text-clustering-request
- name: Speak Request
  property_count: 11
  slug: telnyx-speak-request
- name: SSLCertificate
  property_count: 6
  slug: telnyx-sslcertificate
- name: standard_MdrGetUsageReportsResponse
  property_count: 2
  slug: telnyx-standard-mdr-get-usage-reports-response
- name: Start Conference Recording Request
  property_count: 7
  slug: telnyx-start-conference-recording-request
- name: SummaryRequest
  property_count: 3
  slug: telnyx-summary-request
- name: SummaryResponseData
  property_count: 1
  slug: telnyx-summary-response-data
- name: TaskStatusResponse
  property_count: 1
  slug: telnyx-task-status-response
- name: TelephonyCredentialCreateRequest
  property_count: 4
  slug: telnyx-telephony-credential-create-request
- name: TelephonyCredentialUpdateRequest
  property_count: 4
  slug: telnyx-telephony-credential-update-request
- name: TelnyxBrand
  property_count: 38
  slug: telnyx-telnyx-brand
- name: TelnyxCampaign_CSP
  property_count: 50
  slug: telnyx-telnyx-campaign-csp
- name: TestRunResponse
  property_count: 12
  slug: telnyx-test-run-response
- name: TextClusteringResponseData
  property_count: 1
  slug: telnyx-text-clustering-response-data
- name: Transfer Call Request
  property_count: 38
  slug: telnyx-transfer-call-request
- name: UpdateAssistantRequest
  property_count: 28
  slug: telnyx-update-assistant-request
- name: Update Authentication Provider Request
  property_count: 5
  slug: telnyx-update-authentication-provider-request
- name: UpdateBillingGroup
  property_count: 1
  slug: telnyx-update-billing-group
- name: UpdateBrand
  property_count: 25
  slug: telnyx-update-brand
- name: Update Call Control Application Request
  property_count: 15
  slug: telnyx-update-call-control-application-request
- name: UpdateCampaignRequest
  property_count: 11
  slug: telnyx-update-campaign-request
- name: Update Conference Request
  property_count: 5
  slug: telnyx-update-conference-request
- name: UpdateConversationRequest
  property_count: 1
  slug: telnyx-update-conversation-request
- name: Update Credential Connection Request
  property_count: 25
  slug: telnyx-update-credential-connection-request
- name: Update External Connection Request
  property_count: 7
  slug: telnyx-update-external-connection-request
- name: Update FQDN Connection Request
  property_count: 23
  slug: telnyx-update-fqdn-connection-request
- name: Update FQDN Request
  property_count: 4
  slug: telnyx-update-fqdn-request
- name: Update Ip Connection Request
  property_count: 23
  slug: telnyx-update-ip-connection-request
- name: Update Managed Account Global Outbound Channels Request
  property_count: 1
  slug: telnyx-update-managed-account-global-channel-limit-request
- name: Update Managed Account Request
  property_count: 1
  slug: telnyx-update-managed-account-request
- name: UpdateMCPServerRequest
  property_count: 7
  slug: telnyx-update-mcpserver-request
- name: Upload media multipart request
  property_count: 2
  slug: telnyx-update-media-multipart-request
- name: Upload media request
  property_count: 2
  slug: telnyx-update-media-request
- name: UploadFileMessagingHostedNumberOrderRequest
  property_count: 2
  slug: telnyx-upload-file-messaging-hosted-number-order-request
- name: Upload media multipart request
  property_count: 3
  slug: telnyx-upload-media-multipart-request
- name: Upload media request
  property_count: 3
  slug: telnyx-upload-media-request
- name: UsageRequestLegacy
  property_count: 7
  slug: telnyx-usage-request-legacy
- name: UsecaseMetadata
  property_count: 7
  slug: telnyx-usecase-metadata
- name: ValidateAddressRequest
  property_count: 6
  slug: telnyx-validate-address-request
- name: ValidationCodesRequest
  property_count: 1
  slug: telnyx-validation-codes-request
- name: VerificationCodesRequest
  property_count: 2
  slug: telnyx-verification-codes-request
jsonld:
- class_count: 120
  name: Telnyx Context
  property_count: 261
  slug: telnyx-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.telnyx.com over HTTP; 6 tools listed.
  name: Telnyx MCP Server
  slug: telnyx
modified: '2026-09-16'
name: Telnyx
nav: Providers
network: true
overview: 'Telnyx publishes 223 APIs on the [APIs.io](https://apis.io/) network, including Access Tokens API, Addresses API, Advanced Number Orders API, and 220 more. Tagged areas include Communications, CPaaS, Voice, SMS, and IoT.


  The Telnyx catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Telnyx''s developer surface includes support, signup flow, getting-started guide, changelog, documentation, API reference, pricing, and 37 more developer resources.'
plans:
- name: Telnyx Plans Pricing
  plan_count: 19
  slug: telnyx-plans-pricing
- name: Telnyx Price Estimates
  plan_count: 0
  slug: telnyx-price-estimates
random_paper: 16
rate_limits:
- limit_count: 7
  name: Telnyx Rate Limits
  slug: telnyx-rate-limits
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Telnyx API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: telnyx-rules
scopes:
- name: Telnyx Scopes
  scope_count: 1
  slug: telnyx-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 79.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 31.4
  facets:
    access_clarity: 89.5
    contract_governance: 22.0
    contract_quality: 76.6
    developer_ergonomics: 56.5
    discoverability: 75.0
    operational_transparency: 84.2
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 223
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 40.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 77.8
screenshot: https://raw.githubusercontent.com/api-evangelist/telnyx/refs/heads/main/screenshots/telnyx-2026-06-20T195051.png
security:
- kind: authentication
  name: Telnyx Authentication
  slug: telnyx-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Telnyx Domain Security
  slug: telnyx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Telnyx Vulnerability Disclosure
  slug: telnyx-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Telnyx Trust Center
  slug: telnyx-trust-center
  summary_line: SOC 2, ISO 27001
slug: telnyx
tags:
- Communications
- CPaaS
- Voice
- SMS
- IoT
- Telecommunications
website: https://telnyx.com/
---
