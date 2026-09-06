---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 35.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 540
  human_in_the_loop: 26
  name: Wazo Agentic Access
  operation_count: 932
  slug: wazo-agentic-access
  summary_line: 932 operations · 540 acting · 26 human-in-the-loop
api_count: 25
apis:
- baseURL: https://{wazo_stack}/api/provd/0.2
  baseurl_source: declared
  description: Phone auto-provisioning service. Manages device plugins, configuration templates, device registrations, DHCP integration and the plugin repository used to provision desk phones and ATAs from vendors s
  name: Wazo Phone Provisioning API (wazo-provd)
  slug: wazo-phone-provisioning-api-wazo-provd
- baseURL: wss://{wazo_stack}/api/websocketd/
  baseurl_source: declared
  description: WebSocket gateway onto the Wazo internal event bus. An authenticated client subscribes to named platform events (327 event types across confd, calld, agentd, dird, amid, sysconfd and webhookd) and rec
  name: Wazo Websocket Event Stream (wazo-websocketd)
  slug: wazo-websocket-event-stream-wazo-websocketd
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The aastra API from Wazo — 2 operation(s) for aastra.
  name: Wazo Aastra API
  slug: wazo-aastra-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The access_features API from Wazo — 2 operation(s) for access_features.
  name: Wazo Access Features API
  slug: wazo-access-features-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The action API from Wazo — 1 operation(s) for action.
  name: Wazo Action API
  slug: wazo-action-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The adhoc_conferences API from Wazo — 3 operation(s) for adhoc_conferences.
  name: Wazo Adhoc Conferences API
  slug: wazo-adhoc-conferences-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The admin API from Wazo — 1 operation(s) for admin.
  name: Wazo Admin API
  slug: wazo-admin-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The agent_statistics API from Wazo — 2 operation(s) for agent_statistics.
  name: Wazo Agent Statistics API
  slug: wazo-agent-statistics-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The agents API from Wazo — 29 operation(s) for agents.
  name: Wazo Agents API
  slug: wazo-agents-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The applications API from Wazo — 25 operation(s) for applications.
  name: Wazo Applications API
  slug: wazo-applications-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The asterisk API from Wazo — 17 operation(s) for asterisk.
  name: Wazo Asterisk API
  slug: wazo-asterisk-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The backends API from Wazo — 5 operation(s) for backends.
  name: Wazo Backends API
  slug: wazo-backends-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The blocklist API from Wazo — 5 operation(s) for blocklist.
  name: Wazo Blocklist API
  slug: wazo-blocklist-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The callfilters API from Wazo — 5 operation(s) for callfilters.
  name: Wazo Callfilters API
  slug: wazo-callfilters-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The callpermissions API from Wazo — 5 operation(s) for callpermissions.
  name: Wazo Callpermissions API
  slug: wazo-callpermissions-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The callpickups API from Wazo — 6 operation(s) for callpickups.
  name: Wazo Callpickups API
  slug: wazo-callpickups-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The calls API from Wazo — 27 operation(s) for calls.
  name: Wazo Calls API
  slug: wazo-calls-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The cdr API from Wazo — 8 operation(s) for cdr.
  name: Wazo Cdr API
  slug: wazo-cdr-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The cisco API from Wazo — 3 operation(s) for cisco.
  name: Wazo Cisco API
  slug: wazo-cisco-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The command API from Wazo — 1 operation(s) for command.
  name: Wazo Command API
  slug: wazo-command-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The conference API from Wazo — 3 operation(s) for conference.
  name: Wazo Conference API
  slug: wazo-conference-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The conferences API from Wazo — 11 operation(s) for conferences.
  name: Wazo Conferences API
  slug: wazo-conferences-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The config API from Wazo — 1 operation(s) for config.
  name: Wazo Config API
  slug: wazo-config-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The configs API from Wazo — 5 operation(s) for configs.
  name: Wazo Configs API
  slug: wazo-configs-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The configuration API from Wazo — 26 operation(s) for configuration.
  name: Wazo Configuration API
  slug: wazo-configuration-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The connectors API from Wazo — 5 operation(s) for connectors.
  name: Wazo Connectors API
  slug: wazo-connectors-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The contexts API from Wazo — 4 operation(s) for contexts.
  name: Wazo Contexts API
  slug: wazo-contexts-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The custom API from Wazo — 4 operation(s) for custom.
  name: Wazo Custom API
  slug: wazo-custom-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The devices API from Wazo — 16 operation(s) for devices.
  name: Wazo Devices API
  slug: wazo-devices-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The dhcp API from Wazo — 1 operation(s) for dhcp.
  name: Wazo Dhcp API
  slug: wazo-dhcp-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The directories API from Wazo — 8 operation(s) for directories.
  name: Wazo Directories API
  slug: wazo-directories-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The emails API from Wazo — 5 operation(s) for emails.
  name: Wazo Emails API
  slug: wazo-emails-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The endpoint API from Wazo — 3 operation(s) for endpoint.
  name: Wazo Endpoint API
  slug: wazo-endpoint-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The endpoints API from Wazo — 18 operation(s) for endpoints.
  name: Wazo Endpoints API
  slug: wazo-endpoints-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The exports API from Wazo — 3 operation(s) for exports.
  name: Wazo Exports API
  slug: wazo-exports-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The extensions API from Wazo — 12 operation(s) for extensions.
  name: Wazo Extensions API
  slug: wazo-extensions-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The external API from Wazo — 3 operation(s) for external.
  name: Wazo External API
  slug: wazo-external-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The external_apps API from Wazo — 4 operation(s) for external_apps.
  name: Wazo External Apps API
  slug: wazo-external-apps-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The fanvil API from Wazo — 5 operation(s) for fanvil.
  name: Wazo Fanvil API
  slug: wazo-fanvil-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The favorites API from Wazo — 2 operation(s) for favorites.
  name: Wazo Favorites API
  slug: wazo-favorites-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The faxes API from Wazo — 2 operation(s) for faxes.
  name: Wazo Faxes API
  slug: wazo-faxes-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The forwards API from Wazo — 2 operation(s) for forwards.
  name: Wazo Forwards API
  slug: wazo-forwards-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The funckeys API from Wazo — 9 operation(s) for funckeys.
  name: Wazo Funckeys API
  slug: wazo-funckeys-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The gigaset API from Wazo — 1 operation(s) for gigaset.
  name: Wazo Gigaset API
  slug: wazo-gigaset-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The google API from Wazo — 4 operation(s) for google.
  name: Wazo Google API
  slug: wazo-google-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The groups API from Wazo — 15 operation(s) for groups.
  name: Wazo Groups API
  slug: wazo-groups-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The guests API from Wazo — 4 operation(s) for guests.
  name: Wazo Guests API
  slug: wazo-guests-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The ha API from Wazo — 1 operation(s) for ha.
  name: Wazo Ha API
  slug: wazo-ha-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The htek API from Wazo — 1 operation(s) for htek.
  name: Wazo Htek API
  slug: wazo-htek-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The iax API from Wazo — 7 operation(s) for iax.
  name: Wazo Iax API
  slug: wazo-iax-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The identities API from Wazo — 3 operation(s) for identities.
  name: Wazo Identities API
  slug: wazo-identities-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The idp API from Wazo — 3 operation(s) for idp.
  name: Wazo Idp API
  slug: wazo-idp-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The incalls API from Wazo — 4 operation(s) for incalls.
  name: Wazo Incalls API
  slug: wazo-incalls-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The infos API from Wazo — 1 operation(s) for infos.
  name: Wazo Infos API
  slug: wazo-infos-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The ingresses API from Wazo — 2 operation(s) for ingresses.
  name: Wazo Ingresses API
  slug: wazo-ingresses-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The ivr API from Wazo — 2 operation(s) for ivr.
  name: Wazo Ivr API
  slug: wazo-ivr-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The lines API from Wazo — 15 operation(s) for lines.
  name: Wazo Lines API
  slug: wazo-lines-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The localization API from Wazo — 1 operation(s) for localization.
  name: Wazo Localization API
  slug: wazo-localization-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The market API from Wazo — 2 operation(s) for market.
  name: Wazo Market API
  slug: wazo-market-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The meeting_authorizations API from Wazo — 6 operation(s) for meeting_authorizations.
  name: Wazo Meeting Authorizations API
  slug: wazo-meeting-authorizations-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The meetings API from Wazo — 16 operation(s) for meetings.
  name: Wazo Meetings API
  slug: wazo-meetings-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The messages API from Wazo — 2 operation(s) for messages.
  name: Wazo Messages API
  slug: wazo-messages-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The microsoft API from Wazo — 2 operation(s) for microsoft.
  name: Wazo Microsoft API
  slug: wazo-microsoft-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The mobile API from Wazo — 2 operation(s) for mobile.
  name: Wazo Mobile API
  slug: wazo-mobile-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The moh API from Wazo — 3 operation(s) for moh.
  name: Wazo Moh API
  slug: wazo-moh-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The notifications API from Wazo — 1 operation(s) for notifications.
  name: Wazo Notifications API
  slug: wazo-notifications-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The office365 API from Wazo — 1 operation(s) for office365.
  name: Wazo Office365 API
  slug: wazo-office365-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The outcalls API from Wazo — 6 operation(s) for outcalls.
  name: Wazo Outcalls API
  slug: wazo-outcalls-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The pagings API from Wazo — 4 operation(s) for pagings.
  name: Wazo Pagings API
  slug: wazo-pagings-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The parking_lots API from Wazo — 6 operation(s) for parking_lots.
  name: Wazo Parking Lots API
  slug: wazo-parking-lots-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The personal API from Wazo — 4 operation(s) for personal.
  name: Wazo Personal API
  slug: wazo-personal-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The phone-numbers API from Wazo — 4 operation(s) for phone-numbers.
  name: Wazo Phone Numbers API
  slug: wazo-phone-numbers-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The phonebook API from Wazo — 11 operation(s) for phonebook.
  name: Wazo Phonebook API
  slug: wazo-phonebook-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The plugin API from Wazo — 4 operation(s) for plugin.
  name: Wazo Plugin API
  slug: wazo-plugin-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The plugins API from Wazo — 22 operation(s) for plugins.
  name: Wazo Plugins API
  slug: wazo-plugins-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The policies API from Wazo — 6 operation(s) for policies.
  name: Wazo Policies API
  slug: wazo-policies-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The polycom API from Wazo — 2 operation(s) for polycom.
  name: Wazo Polycom API
  slug: wazo-polycom-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The presences API from Wazo — 2 operation(s) for presences.
  name: Wazo Presences API
  slug: wazo-presences-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The provisioning API from Wazo — 1 operation(s) for provisioning.
  name: Wazo Provisioning API
  slug: wazo-provisioning-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The queue_statistics API from Wazo — 3 operation(s) for queue_statistics.
  name: Wazo Queue Statistics API
  slug: wazo-queue-statistics-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The queues API from Wazo — 9 operation(s) for queues.
  name: Wazo Queues API
  slug: wazo-queues-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The recordings-announcements API from Wazo — 1 operation(s) for recordings-announcements.
  name: Wazo Recordings Announcements API
  slug: wazo-recordings-announcements-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The registers API from Wazo — 3 operation(s) for registers.
  name: Wazo Registers API
  slug: wazo-registers-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The registrars API from Wazo — 2 operation(s) for registrars.
  name: Wazo Registrars API
  slug: wazo-registrars-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The relocates API from Wazo — 4 operation(s) for relocates.
  name: Wazo Relocates API
  slug: wazo-relocates-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The retention API from Wazo — 1 operation(s) for retention.
  name: Wazo Retention API
  slug: wazo-retention-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The rooms API from Wazo — 3 operation(s) for rooms.
  name: Wazo Rooms API
  slug: wazo-rooms-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The saml API from Wazo — 4 operation(s) for saml.
  name: Wazo Saml API
  slug: wazo-saml-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The sccp API from Wazo — 4 operation(s) for sccp.
  name: Wazo Sccp API
  slug: wazo-sccp-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The schedules API from Wazo — 7 operation(s) for schedules.
  name: Wazo Schedules API
  slug: wazo-schedules-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The sessions API from Wazo — 4 operation(s) for sessions.
  name: Wazo Sessions API
  slug: wazo-sessions-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The setup API from Wazo — 1 operation(s) for setup.
  name: Wazo Setup API
  slug: wazo-setup-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The sip API from Wazo — 11 operation(s) for sip.
  name: Wazo Sip API
  slug: wazo-sip-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The skills API from Wazo — 5 operation(s) for skills.
  name: Wazo Skills API
  slug: wazo-skills-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The snom API from Wazo — 2 operation(s) for snom.
  name: Wazo Snom API
  slug: wazo-snom-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The sounds API from Wazo — 4 operation(s) for sounds.
  name: Wazo Sounds API
  slug: wazo-sounds-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The status API from Wazo — 1 operation(s) for status.
  name: Wazo Status API
  slug: wazo-status-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The subscriptions API from Wazo — 6 operation(s) for subscriptions.
  name: Wazo Subscriptions API
  slug: wazo-subscriptions-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The switchboards API from Wazo — 9 operation(s) for switchboards.
  name: Wazo Switchboards API
  slug: wazo-switchboards-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The tenants API from Wazo — 4 operation(s) for tenants.
  name: Wazo Tenants API
  slug: wazo-tenants-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The thomson API from Wazo — 1 operation(s) for thomson.
  name: Wazo Thomson API
  slug: wazo-thomson-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The timezones API from Wazo — 1 operation(s) for timezones.
  name: Wazo Timezones API
  slug: wazo-timezones-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The token API from Wazo — 10 operation(s) for token.
  name: Wazo Token API
  slug: wazo-token-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The transcription API from Wazo — 1 operation(s) for transcription.
  name: Wazo Transcription API
  slug: wazo-transcription-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The transfers API from Wazo — 6 operation(s) for transfers.
  name: Wazo Transfers API
  slug: wazo-transfers-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The trunks API from Wazo — 7 operation(s) for trunks.
  name: Wazo Trunks API
  slug: wazo-trunks-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The users API from Wazo — 104 operation(s) for users.
  name: Wazo Users API
  slug: wazo-users-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The voicemail_transcriptions API from Wazo — 1 operation(s) for voicemail_transcriptions.
  name: Wazo Voicemail Transcriptions API
  slug: wazo-voicemail-transcriptions-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The voicemails API from Wazo — 20 operation(s) for voicemails.
  name: Wazo Voicemails API
  slug: wazo-voicemails-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The wazo API from Wazo — 1 operation(s) for wazo.
  name: Wazo Wazo API
  slug: wazo-wazo-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The wizard API from Wazo — 2 operation(s) for wizard.
  name: Wazo Wizard API
  slug: wazo-wizard-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The work_in_progress API from Wazo — 1 operation(s) for work_in_progress.
  name: Wazo Work In Progress API
  slug: wazo-work-in-progress-api
- baseURL: https://{wazo_stack}/api/auth/0.1
  baseurl_source: declared
  description: The yealink API from Wazo — 4 operation(s) for yealink.
  name: Wazo Yealink API
  slug: wazo-yealink-api
artifact_total: 131
asyncapis:
- description: ''
  name: wazo-agentd events
  slug: wazo-agentd-asyncapi
- description: ''
  name: wazo-amid events
  slug: wazo-amid-asyncapi
- description: ''
  name: wazo-auth events
  slug: wazo-auth-asyncapi
- description: ''
  name: wazo-call_logd events
  slug: wazo-call-logd-asyncapi
- description: ''
  name: wazo-calld events
  slug: wazo-calld-asyncapi
- description: ''
  name: wazo-chatd events
  slug: wazo-chatd-asyncapi
- description: ''
  name: wazo-confd events
  slug: wazo-confd-asyncapi
- description: ''
  name: wazo-dird events
  slug: wazo-dird-asyncapi
- description: ''
  name: Wazo Events Webhooks
  slug: wazo-events-webhooks
- description: ''
  name: wazo-plugind events
  slug: wazo-plugind-asyncapi
- description: ''
  name: wazo-sysconfd events
  slug: wazo-sysconfd-asyncapi
- description: ''
  name: undefined events
  slug: wazo-unattributed-asyncapi
- description: ''
  name: wazo-webhookd events
  slug: wazo-webhookd-asyncapi
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/wazo-platform/wazo-provd/blob/master/LICENSE
- group: other
  title: ''
  type: Overlay
  url: overlays/wazo-auth-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/wazo-confd-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/wazo-calld-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/wazo-call-logd-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/wazo-dird-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/wazo-webhookd-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/wazo-plugind-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/wazo-agentd-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/wazo-chatd-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/wazo-phoned-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/wazo-setupd-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/wazo-amid-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wazo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wazo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wazo.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.wazo.io/
- group: start
  title: ''
  type: Portal
  url: https://developers.wazo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://wazo-platform.org/uc-doc/
- group: docs
  title: ''
  type: APIReference
  url: https://api.wazo.io/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://wazo-platform.org/uc-doc/api_sdk/rest_api/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://wazo-platform.org/uc-doc/api_sdk/rest_api/quickstart
- group: operate
  title: ''
  type: Support
  url: https://wazo-platform.discourse.group/
- group: operate
  title: ''
  type: Community
  url: https://mm.wazo.community/wazo-platform/
- group: company
  title: ''
  type: Blog
  url: https://wazo-platform.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wazo-platform
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wazo-communication
- group: operate
  title: ''
  type: IssueTracker
  url: https://wazo-dev.atlassian.net/
- group: start
  title: ''
  type: SignUp
  url: https://wazo.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wazo.io/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wazo.io/privacy
- group: other
  title: ''
  type: Download
  url: https://wazo.io/download
- group: other
  title: ''
  type: Ecosystem
  url: https://wazo-platform.org/ecosystem/
- group: learn
  title: ''
  type: Tutorials
  url: https://wazo-platform.org/tutorials/
- group: build
  title: ''
  type: Packages
  url: packages/wazo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wazo-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wazo-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/wazo-acl-permissions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wazo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wazo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wazo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wazo-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://wazo-platform.org/uc-doc/api_sdk/rest_api/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/wazo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wazo-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/wazo-cli.yml
- group: design
  title: ''
  type: Components
  url: components/wazo-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wazo-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://api.wazo.io/documentation/console/authentication/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wazo-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wazo-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/wazo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wazo-rate-limits.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-unattributed-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-agentd-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-amid-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-auth-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-call-logd-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-calld-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-chatd-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-confd-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-dird-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-plugind-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-sysconfd-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/wazo-webhookd-asyncapi.yml
created: '2026-08-17'
description: 'Wazo Communication Inc. builds the Wazo Platform, an open-source (GPL-3.0) programmable unified-communications and contact-centre platform assembled from Asterisk, Kamailio, RabbitMQ, PostgreSQL and nginx, which MSPs, carriers, telecom integrators and enterprises self-host or resell white-label as UCaaS. The platform is API-first: thirteen HTTP microservices — authentication, stack configuration (confd), runtime call control (calld), call detail records, directories, call-centre agents, presence and chat, phone auto-provisioning, webhooks, plugin management, the Asterisk Manager facade and initial setup — each publish their own Swagger 2.0 contract totalling 932 operations, share a single X-Auth-Token bearer model governed by 788 fine-grained ACL permissions, and emit 327 named events onto a RabbitMQ bus that wazo-webhookd relays as HTTP webhooks and wazo-websocketd streams over WebSocket. There is no public multi-tenant API host: every base URL is the customer''s own stack.'
image: https://wazo-platform.org/images/logo-black.svg
layout: provider
modified: '2026-08-17'
name: Wazo
nav: Providers
network: true
overview: 'Wazo publishes 113 APIs on the [APIs.io](https://apis.io/) network, including Phone Provisioning API (wazo-provd), Websocket Event Stream (wazo-websocketd), Aastra API, and 110 more. Tagged areas include Telephony, VoIP, Unified Communications, UCaaS, and Contact Center.


  The Wazo catalog on APIs.io includes 13 event-driven AsyncAPI specifications.


  Wazo''s developer surface includes developer portal, documentation, API reference, getting-started guide, quickstart, support, engineering blog, and 59 more developer resources.'
plans:
- name: Wazo Plans Pricing
  plan_count: 0
  slug: wazo-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Wazo Rate Limits
  slug: wazo-rate-limits
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 26.5
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 112
      marker_coverage: 100.0
      total: 112
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wazo/refs/heads/main/screenshots/wazo-2026-09-02T170515.png
security:
- kind: authentication
  name: Wazo Authentication
  slug: wazo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wazo Domain Security
  slug: wazo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wazo
tags:
- Telephony
- VoIP
- Unified Communications
- UCaaS
- Contact Center
- SIP
- asterisk
- WebRTC
- Open-Source
- Self-Hosted
- White Label
- PBX
- MSP
- Call Center
- Provisioning
- Webhook
- Event-Driven
- Chat
- Presence
- CDR
website: https://wazo.io/
---
