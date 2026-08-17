---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Luma Agentic Access
  operation_count: 62
  slug: luma-agentic-access
  summary_line: 62 operations · 40 acting
api_count: 6
apis:
- description: The Calendars API from Luma — 25 operation(s) for calendars.
  name: Luma Calendars API
  slug: luma-calendars-api
- description: The Events API from Luma — 21 operation(s) for events.
  name: Luma Events API
  slug: luma-events-api
- description: The Memberships API from Luma — 3 operation(s) for memberships.
  name: Luma Memberships API
  slug: luma-memberships-api
- description: The Miscellaneous API from Luma — 3 operation(s) for miscellaneous.
  name: Luma Miscellaneous API
  slug: luma-miscellaneous-api
- description: The Organizations API from Luma — 5 operation(s) for organizations.
  name: Luma Organizations API
  slug: luma-organizations-api
- description: The Webhooks API from Luma — 5 operation(s) for webhooks.
  name: Luma Webhooks API
  slug: luma-webhooks-api
artifact_total: 222
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Luma Calendars API
  slug: open-luma-calendars-api
- collection_type: open
  name: Luma Calendars Events API
  slug: open-luma-events-api
- collection_type: open
  name: Luma Calendars Memberships API
  slug: open-luma-memberships-api
- collection_type: open
  name: Luma Calendars Miscellaneous API
  slug: open-luma-miscellaneous-api
- collection_type: open
  name: Luma Calendars Organizations API
  slug: open-luma-organizations-api
- collection_type: open
  name: Luma Calendars Webhooks API
  slug: open-luma-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/luma-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/luma-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/luma-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/luma-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.luma.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.luma.com/reference
- group: commercial
  title: ''
  type: Pricing
  url: https://luma.com/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.luma.com/
- group: other
  title: ''
  type: APIOverview
  url: https://help.luma.com/p/luma-api
- group: build
  title: ''
  type: SDKEmbedExamples
  url: https://github.com/luma-team/examples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/luma-team
- group: other
  title: ''
  type: X
  url: https://x.com/LumaHQ
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lu.ma
created: '2026-06-13'
description: Modern event hosting platform with REST APIs for creating events, managing ticketing, tracking attendance, and building community around live and virtual events.
examples:
- key_count: 3
  name: V1_Calendar_Add Event_Post_200_Response
  slug: v1_calendar_add-event_post_200_response
- key_count: 12
  name: V1_Calendar_Add Event_Post_Request
  slug: v1_calendar_add-event_post_request
- key_count: 1
  name: V1_Calendar_Admins_List_Get_200_Response
  slug: v1_calendar_admins_list_get_200_response
- key_count: 1
  name: V1_Calendar_Approve Event_Post_Request
  slug: v1_calendar_approve-event_post_request
- key_count: 1
  name: V1_Calendar_Lookup Event_Get_200_Response
  slug: v1_calendar_lookup-event_get_200_response
- key_count: 2
  name: V1_Calendar_Reject Event_Post_Request
  slug: v1_calendar_reject-event_post_request
- key_count: 2
  name: V1_Calendars_Contact Tags_Apply_Post_200_Response
  slug: v1_calendars_contact-tags_apply_post_200_response
- key_count: 3
  name: V1_Calendars_Contact Tags_Apply_Post_Request
  slug: v1_calendars_contact-tags_apply_post_request
- key_count: 1
  name: V1_Calendars_Contact Tags_Create_Post_200_Response
  slug: v1_calendars_contact-tags_create_post_200_response
- key_count: 2
  name: V1_Calendars_Contact Tags_Create_Post_Request
  slug: v1_calendars_contact-tags_create_post_request
- key_count: 1
  name: V1_Calendars_Contact Tags_Delete_Post_Request
  slug: v1_calendars_contact-tags_delete_post_request
- key_count: 2
  name: V1_Calendars_Contact Tags_List_Get_200_Response
  slug: v1_calendars_contact-tags_list_get_200_response
- key_count: 2
  name: V1_Calendars_Contact Tags_Unapply_Post_200_Response
  slug: v1_calendars_contact-tags_unapply_post_200_response
- key_count: 3
  name: V1_Calendars_Contact Tags_Unapply_Post_Request
  slug: v1_calendars_contact-tags_unapply_post_request
- key_count: 3
  name: V1_Calendars_Contact Tags_Update_Post_Request
  slug: v1_calendars_contact-tags_update_post_request
- key_count: 2
  name: V1_Calendars_Contacts_Import_Post_Request
  slug: v1_calendars_contacts_import_post_request
- key_count: 3
  name: V1_Calendars_Contacts_List_Get_200_Response
  slug: v1_calendars_contacts_list_get_200_response
- key_count: 9
  name: V1_Calendars_Coupons_Create_Post_200_Response
  slug: v1_calendars_coupons_create_post_200_response
- key_count: 5
  name: V1_Calendars_Coupons_Create_Post_Request
  slug: v1_calendars_coupons_create_post_request
- key_count: 3
  name: V1_Calendars_Coupons_List_Get_200_Response
  slug: v1_calendars_coupons_list_get_200_response
- key_count: 4
  name: V1_Calendars_Coupons_Update_Post_Request
  slug: v1_calendars_coupons_update_post_request
- key_count: 2
  name: V1_Calendars_Event Tags_Apply_Post_200_Response
  slug: v1_calendars_event-tags_apply_post_200_response
- key_count: 2
  name: V1_Calendars_Event Tags_Apply_Post_Request
  slug: v1_calendars_event-tags_apply_post_request
- key_count: 1
  name: V1_Calendars_Event Tags_Create_Post_200_Response
  slug: v1_calendars_event-tags_create_post_200_response
- key_count: 2
  name: V1_Calendars_Event Tags_Create_Post_Request
  slug: v1_calendars_event-tags_create_post_request
- key_count: 1
  name: V1_Calendars_Event Tags_Delete_Post_Request
  slug: v1_calendars_event-tags_delete_post_request
- key_count: 2
  name: V1_Calendars_Event Tags_List_Get_200_Response
  slug: v1_calendars_event-tags_list_get_200_response
- key_count: 2
  name: V1_Calendars_Event Tags_Unapply_Post_200_Response
  slug: v1_calendars_event-tags_unapply_post_200_response
- key_count: 2
  name: V1_Calendars_Event Tags_Unapply_Post_Request
  slug: v1_calendars_event-tags_unapply_post_request
- key_count: 3
  name: V1_Calendars_Event Tags_Update_Post_Request
  slug: v1_calendars_event-tags_update_post_request
- key_count: 3
  name: V1_Calendars_Events_List_Get_200_Response
  slug: v1_calendars_events_list_get_200_response
- key_count: 15
  name: V1_Calendars_Get_Get_200_Response
  slug: v1_calendars_get_get_200_response
- key_count: 15
  name: V1_Calendars_Update_Post_200_Response
  slug: v1_calendars_update_post_200_response
- key_count: 6
  name: V1_Calendars_Update_Post_Request
  slug: v1_calendars_update_post_request
- key_count: 1
  name: V1_Entity_Lookup_Get_200_Response
  slug: v1_entity_lookup_get_200_response
- key_count: 3
  name: V1_Events_Cancel_Post_Request
  slug: v1_events_cancel_post_request
- key_count: 3
  name: V1_Events_Cancel_Request_Post_200_Response
  slug: v1_events_cancel_request_post_200_response
- key_count: 1
  name: V1_Events_Cancel_Request_Post_Request
  slug: v1_events_cancel_request_post_request
- key_count: 9
  name: V1_Events_Coupons_Create_Post_200_Response
  slug: v1_events_coupons_create_post_200_response
- key_count: 7
  name: V1_Events_Coupons_Create_Post_Request
  slug: v1_events_coupons_create_post_request
- key_count: 3
  name: V1_Events_Coupons_List_Get_200_Response
  slug: v1_events_coupons_list_get_200_response
- key_count: 5
  name: V1_Events_Coupons_Update_Post_Request
  slug: v1_events_coupons_update_post_request
- key_count: 1
  name: V1_Events_Create_Post_200_Response
  slug: v1_events_create_post_200_response
- key_count: 20
  name: V1_Events_Create_Post_Request
  slug: v1_events_create_post_request
- key_count: 24
  name: V1_Events_Get_Get_200_Response
  slug: v1_events_get_get_200_response
- key_count: 6
  name: V1_Events_Guests_Add_Post_Request
  slug: v1_events_guests_add_post_request
- key_count: 18
  name: V1_Events_Guests_Get_Get_200_Response
  slug: v1_events_guests_get_get_200_response
- key_count: 3
  name: V1_Events_Guests_List_Get_200_Response
  slug: v1_events_guests_list_get_200_response
- key_count: 3
  name: V1_Events_Guests_Send Invites_Post_Request
  slug: v1_events_guests_send-invites_post_request
- key_count: 6
  name: V1_Events_Guests_Update Status_Post_Request
  slug: v1_events_guests_update-status_post_request
- key_count: 5
  name: V1_Events_Hosts_Add_Post_Request
  slug: v1_events_hosts_add_post_request
- key_count: 2
  name: V1_Events_Hosts_Remove_Post_Request
  slug: v1_events_hosts_remove_post_request
- key_count: 4
  name: V1_Events_Hosts_Update_Post_Request
  slug: v1_events_hosts_update_post_request
- key_count: 13
  name: V1_Events_Ticket Types_Create_Post_200_Response
  slug: v1_events_ticket-types_create_post_200_response
- key_count: 13
  name: V1_Events_Ticket Types_Create_Post_Request
  slug: v1_events_ticket-types_create_post_request
- key_count: 1
  name: V1_Events_Ticket Types_Delete_Post_Request
  slug: v1_events_ticket-types_delete_post_request
- key_count: 13
  name: V1_Events_Ticket Types_Get_Get_200_Response
  slug: v1_events_ticket-types_get_get_200_response
- key_count: 1
  name: V1_Events_Ticket Types_List_Get_200_Response
  slug: v1_events_ticket-types_list_get_200_response
- key_count: 13
  name: V1_Events_Ticket Types_Update_Post_200_Response
  slug: v1_events_ticket-types_update_post_200_response
- key_count: 13
  name: V1_Events_Ticket Types_Update_Post_Request
  slug: v1_events_ticket-types_update_post_request
- key_count: 22
  name: V1_Events_Update_Post_Request
  slug: v1_events_update_post_request
- key_count: 2
  name: V1_Images_Create Upload Url_Post_200_Response
  slug: v1_images_create-upload-url_post_200_response
- key_count: 1
  name: V1_Images_Create Upload Url_Post_Request
  slug: v1_images_create-upload-url_post_request
- key_count: 2
  name: V1_Memberships_Members_Add_Post_200_Response
  slug: v1_memberships_members_add_post_200_response
- key_count: 4
  name: V1_Memberships_Members_Add_Post_Request
  slug: v1_memberships_members_add_post_request
- key_count: 2
  name: V1_Memberships_Members_Update Status_Post_Request
  slug: v1_memberships_members_update-status_post_request
- key_count: 3
  name: V1_Memberships_Tiers_List_Get_200_Response
  slug: v1_memberships_tiers_list_get_200_response
- key_count: 1
  name: V1_Organizations_Admins_List_Get_200_Response
  slug: v1_organizations_admins_list_get_200_response
- key_count: 3
  name: V1_Organizations_Calendars_List_Get_200_Response
  slug: v1_organizations_calendars_list_get_200_response
- key_count: 3
  name: V1_Organizations_Events_List_Get_200_Response
  slug: v1_organizations_events_list_get_200_response
- key_count: 2
  name: V1_Organizations_Events_Transfer Calendar_Post_Request
  slug: v1_organizations_events_transfer-calendar_post_request
- key_count: 6
  name: V1_Users_Get Self_Get_200_Response
  slug: v1_users_get-self_get_200_response
- key_count: 1
  name: V1_Webhooks_Delete_Post_Request
  slug: v1_webhooks_delete_post_request
- key_count: 3
  name: V1_Webhooks_List_Get_200_Response
  slug: v1_webhooks_list_get_200_response
- key_count: 15
  name: V2_Organizations_Calendars_Create_Post_200_Response
  slug: v2_organizations_calendars_create_post_200_response
- key_count: 5
  name: V2_Organizations_Calendars_Create_Post_Request
  slug: v2_organizations_calendars_create_post_request
- key_count: 6
  name: V2_Webhooks_Create_Post_200_Response
  slug: v2_webhooks_create_post_200_response
- key_count: 2
  name: V2_Webhooks_Create_Post_Request
  slug: v2_webhooks_create_post_request
- key_count: 6
  name: V2_Webhooks_Get_Get_200_Response
  slug: v2_webhooks_get_get_200_response
- key_count: 6
  name: V2_Webhooks_Update_Post_200_Response
  slug: v2_webhooks_update_post_200_response
- key_count: 3
  name: V2_Webhooks_Update_Post_Request
  slug: v2_webhooks_update_post_request
- key_count: 2
  name: Webhook_Calendar_Event_Added_Post_Request
  slug: webhook_calendar_event_added_post_request
- key_count: 2
  name: Webhook_Calendar_Person_Subscribed_Post_Request
  slug: webhook_calendar_person_subscribed_post_request
- key_count: 2
  name: Webhook_Event_Canceled_Post_Request
  slug: webhook_event_canceled_post_request
- key_count: 2
  name: Webhook_Event_Created_Post_Request
  slug: webhook_event_created_post_request
- key_count: 2
  name: Webhook_Event_Updated_Post_Request
  slug: webhook_event_updated_post_request
- key_count: 2
  name: Webhook_Guest_Registered_Post_Request
  slug: webhook_guest_registered_post_request
- key_count: 2
  name: Webhook_Guest_Updated_Post_Request
  slug: webhook_guest_updated_post_request
- key_count: 2
  name: Webhook_Ticket_Registered_Post_Request
  slug: webhook_ticket_registered_post_request
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/luma.png
json_schemas:
- name: V1 Calendar Add Event Post 200 Response
  property_count: 3
  slug: v1_calendar_add_event_post_200_response
- name: V1 Calendar Add Event Post Request
  property_count: 0
  slug: v1_calendar_add_event_post_request
- name: V1 Calendar Admins List Get 200 Response
  property_count: 1
  slug: v1_calendar_admins_list_get_200_response
- name: V1 Calendar Approve Event Post 200 Response
  property_count: 0
  slug: v1_calendar_approve_event_post_200_response
- name: V1 Calendar Approve Event Post Request
  property_count: 1
  slug: v1_calendar_approve_event_post_request
- name: V1 Calendar Lookup Event Get 200 Response
  property_count: 1
  slug: v1_calendar_lookup_event_get_200_response
- name: V1 Calendar Reject Event Post 200 Response
  property_count: 0
  slug: v1_calendar_reject_event_post_200_response
- name: V1 Calendar Reject Event Post Request
  property_count: 2
  slug: v1_calendar_reject_event_post_request
- name: V1 Calendars Contact Tags Apply Post 200 Response
  property_count: 2
  slug: v1_calendars_contact_tags_apply_post_200_response
- name: V1 Calendars Contact Tags Apply Post Request
  property_count: 3
  slug: v1_calendars_contact_tags_apply_post_request
- name: V1 Calendars Contact Tags Create Post 200 Response
  property_count: 1
  slug: v1_calendars_contact_tags_create_post_200_response
- name: V1 Calendars Contact Tags Create Post Request
  property_count: 2
  slug: v1_calendars_contact_tags_create_post_request
- name: V1 Calendars Contact Tags Delete Post 200 Response
  property_count: 0
  slug: v1_calendars_contact_tags_delete_post_200_response
- name: V1 Calendars Contact Tags Delete Post Request
  property_count: 1
  slug: v1_calendars_contact_tags_delete_post_request
- name: V1 Calendars Contact Tags List Get 200 Response
  property_count: 2
  slug: v1_calendars_contact_tags_list_get_200_response
- name: V1 Calendars Contact Tags Unapply Post 200 Response
  property_count: 2
  slug: v1_calendars_contact_tags_unapply_post_200_response
- name: V1 Calendars Contact Tags Unapply Post Request
  property_count: 3
  slug: v1_calendars_contact_tags_unapply_post_request
- name: V1 Calendars Contact Tags Update Post 200 Response
  property_count: 0
  slug: v1_calendars_contact_tags_update_post_200_response
- name: V1 Calendars Contact Tags Update Post Request
  property_count: 3
  slug: v1_calendars_contact_tags_update_post_request
- name: V1 Calendars Contacts Import Post 200 Response
  property_count: 0
  slug: v1_calendars_contacts_import_post_200_response
- name: V1 Calendars Contacts Import Post Request
  property_count: 2
  slug: v1_calendars_contacts_import_post_request
- name: V1 Calendars Contacts List Get 200 Response
  property_count: 3
  slug: v1_calendars_contacts_list_get_200_response
- name: V1 Calendars Coupons Create Post 200 Response
  property_count: 9
  slug: v1_calendars_coupons_create_post_200_response
- name: V1 Calendars Coupons Create Post Request
  property_count: 5
  slug: v1_calendars_coupons_create_post_request
- name: V1 Calendars Coupons List Get 200 Response
  property_count: 3
  slug: v1_calendars_coupons_list_get_200_response
- name: V1 Calendars Coupons Update Post 200 Response
  property_count: 0
  slug: v1_calendars_coupons_update_post_200_response
- name: V1 Calendars Coupons Update Post Request
  property_count: 4
  slug: v1_calendars_coupons_update_post_request
- name: V1 Calendars Event Tags Apply Post 200 Response
  property_count: 2
  slug: v1_calendars_event_tags_apply_post_200_response
- name: V1 Calendars Event Tags Apply Post Request
  property_count: 2
  slug: v1_calendars_event_tags_apply_post_request
- name: V1 Calendars Event Tags Create Post 200 Response
  property_count: 1
  slug: v1_calendars_event_tags_create_post_200_response
- name: V1 Calendars Event Tags Create Post Request
  property_count: 2
  slug: v1_calendars_event_tags_create_post_request
- name: V1 Calendars Event Tags Delete Post 200 Response
  property_count: 0
  slug: v1_calendars_event_tags_delete_post_200_response
- name: V1 Calendars Event Tags Delete Post Request
  property_count: 1
  slug: v1_calendars_event_tags_delete_post_request
- name: V1 Calendars Event Tags List Get 200 Response
  property_count: 2
  slug: v1_calendars_event_tags_list_get_200_response
- name: V1 Calendars Event Tags Unapply Post 200 Response
  property_count: 2
  slug: v1_calendars_event_tags_unapply_post_200_response
- name: V1 Calendars Event Tags Unapply Post Request
  property_count: 2
  slug: v1_calendars_event_tags_unapply_post_request
- name: V1 Calendars Event Tags Update Post 200 Response
  property_count: 0
  slug: v1_calendars_event_tags_update_post_200_response
- name: V1 Calendars Event Tags Update Post Request
  property_count: 3
  slug: v1_calendars_event_tags_update_post_request
- name: V1 Calendars Events List Get 200 Response
  property_count: 3
  slug: v1_calendars_events_list_get_200_response
- name: V1 Calendars Get Get 200 Response
  property_count: 15
  slug: v1_calendars_get_get_200_response
- name: V1 Calendars Update Post 200 Response
  property_count: 15
  slug: v1_calendars_update_post_200_response
- name: V1 Calendars Update Post Request
  property_count: 6
  slug: v1_calendars_update_post_request
- name: V1 Entity Lookup Get 200 Response
  property_count: 1
  slug: v1_entity_lookup_get_200_response
- name: V1 Events Cancel Post 200 Response
  property_count: 0
  slug: v1_events_cancel_post_200_response
- name: V1 Events Cancel Post Request
  property_count: 3
  slug: v1_events_cancel_post_request
- name: V1 Events Cancel Request Post 200 Response
  property_count: 3
  slug: v1_events_cancel_request_post_200_response
- name: V1 Events Cancel Request Post Request
  property_count: 1
  slug: v1_events_cancel_request_post_request
- name: V1 Events Coupons Create Post 200 Response
  property_count: 9
  slug: v1_events_coupons_create_post_200_response
- name: V1 Events Coupons Create Post Request
  property_count: 7
  slug: v1_events_coupons_create_post_request
- name: V1 Events Coupons List Get 200 Response
  property_count: 3
  slug: v1_events_coupons_list_get_200_response
- name: V1 Events Coupons Update Post 200 Response
  property_count: 0
  slug: v1_events_coupons_update_post_200_response
- name: V1 Events Coupons Update Post Request
  property_count: 5
  slug: v1_events_coupons_update_post_request
- name: V1 Events Create Post 200 Response
  property_count: 1
  slug: v1_events_create_post_200_response
- name: V1 Events Create Post Request
  property_count: 20
  slug: v1_events_create_post_request
- name: V1 Events Get Get 200 Response
  property_count: 24
  slug: v1_events_get_get_200_response
- name: V1 Events Guests Add Post 200 Response
  property_count: 0
  slug: v1_events_guests_add_post_200_response
- name: V1 Events Guests Add Post Request
  property_count: 6
  slug: v1_events_guests_add_post_request
- name: V1 Events Guests Get Get 200 Response
  property_count: 18
  slug: v1_events_guests_get_get_200_response
- name: V1 Events Guests List Get 200 Response
  property_count: 3
  slug: v1_events_guests_list_get_200_response
- name: V1 Events Guests Send Invites Post 200 Response
  property_count: 0
  slug: v1_events_guests_send_invites_post_200_response
- name: V1 Events Guests Send Invites Post Request
  property_count: 3
  slug: v1_events_guests_send_invites_post_request
- name: V1 Events Guests Update Status Post 200 Response
  property_count: 0
  slug: v1_events_guests_update_status_post_200_response
- name: V1 Events Guests Update Status Post Request
  property_count: 6
  slug: v1_events_guests_update_status_post_request
- name: V1 Events Hosts Add Post 200 Response
  property_count: 0
  slug: v1_events_hosts_add_post_200_response
- name: V1 Events Hosts Add Post Request
  property_count: 5
  slug: v1_events_hosts_add_post_request
- name: V1 Events Hosts Remove Post 200 Response
  property_count: 0
  slug: v1_events_hosts_remove_post_200_response
- name: V1 Events Hosts Remove Post Request
  property_count: 2
  slug: v1_events_hosts_remove_post_request
- name: V1 Events Hosts Update Post 200 Response
  property_count: 0
  slug: v1_events_hosts_update_post_200_response
- name: V1 Events Hosts Update Post Request
  property_count: 4
  slug: v1_events_hosts_update_post_request
- name: V1 Events Ticket Types Create Post 200 Response
  property_count: 13
  slug: v1_events_ticket_types_create_post_200_response
- name: V1 Events Ticket Types Create Post Request
  property_count: 0
  slug: v1_events_ticket_types_create_post_request
- name: V1 Events Ticket Types Delete Post 200 Response
  property_count: 0
  slug: v1_events_ticket_types_delete_post_200_response
- name: V1 Events Ticket Types Delete Post Request
  property_count: 1
  slug: v1_events_ticket_types_delete_post_request
- name: V1 Events Ticket Types Get Get 200 Response
  property_count: 13
  slug: v1_events_ticket_types_get_get_200_response
- name: V1 Events Ticket Types List Get 200 Response
  property_count: 1
  slug: v1_events_ticket_types_list_get_200_response
- name: V1 Events Ticket Types Update Post 200 Response
  property_count: 13
  slug: v1_events_ticket_types_update_post_200_response
- name: V1 Events Ticket Types Update Post Request
  property_count: 0
  slug: v1_events_ticket_types_update_post_request
- name: V1 Events Update Post 200 Response
  property_count: 0
  slug: v1_events_update_post_200_response
- name: V1 Events Update Post Request
  property_count: 22
  slug: v1_events_update_post_request
- name: V1 Images Create Upload Url Post 200 Response
  property_count: 2
  slug: v1_images_create_upload_url_post_200_response
- name: V1 Images Create Upload Url Post Request
  property_count: 1
  slug: v1_images_create_upload_url_post_request
- name: V1 Memberships Members Add Post 200 Response
  property_count: 2
  slug: v1_memberships_members_add_post_200_response
- name: V1 Memberships Members Add Post Request
  property_count: 4
  slug: v1_memberships_members_add_post_request
- name: V1 Memberships Members Update Status Post 200 Response
  property_count: 0
  slug: v1_memberships_members_update_status_post_200_response
- name: V1 Memberships Members Update Status Post Request
  property_count: 2
  slug: v1_memberships_members_update_status_post_request
- name: V1 Memberships Tiers List Get 200 Response
  property_count: 3
  slug: v1_memberships_tiers_list_get_200_response
- name: V1 Organizations Admins List Get 200 Response
  property_count: 1
  slug: v1_organizations_admins_list_get_200_response
- name: V1 Organizations Calendars List Get 200 Response
  property_count: 3
  slug: v1_organizations_calendars_list_get_200_response
- name: V1 Organizations Events List Get 200 Response
  property_count: 3
  slug: v1_organizations_events_list_get_200_response
- name: V1 Organizations Events Transfer Calendar Post 200 Response
  property_count: 0
  slug: v1_organizations_events_transfer_calendar_post_200_response
- name: V1 Organizations Events Transfer Calendar Post Request
  property_count: 2
  slug: v1_organizations_events_transfer_calendar_post_request
- name: V1 Users Get Self Get 200 Response
  property_count: 6
  slug: v1_users_get_self_get_200_response
- name: V1 Webhooks Delete Post 200 Response
  property_count: 0
  slug: v1_webhooks_delete_post_200_response
- name: V1 Webhooks Delete Post Request
  property_count: 1
  slug: v1_webhooks_delete_post_request
- name: V1 Webhooks List Get 200 Response
  property_count: 3
  slug: v1_webhooks_list_get_200_response
- name: V2 Organizations Calendars Create Post 200 Response
  property_count: 15
  slug: v2_organizations_calendars_create_post_200_response
- name: V2 Organizations Calendars Create Post Request
  property_count: 5
  slug: v2_organizations_calendars_create_post_request
- name: V2 Webhooks Create Post 200 Response
  property_count: 6
  slug: v2_webhooks_create_post_200_response
- name: V2 Webhooks Create Post Request
  property_count: 2
  slug: v2_webhooks_create_post_request
- name: V2 Webhooks Get Get 200 Response
  property_count: 6
  slug: v2_webhooks_get_get_200_response
- name: V2 Webhooks Update Post 200 Response
  property_count: 6
  slug: v2_webhooks_update_post_200_response
- name: V2 Webhooks Update Post Request
  property_count: 3
  slug: v2_webhooks_update_post_request
- name: Webhook Calendar.Event.Added Post Request
  property_count: 2
  slug: webhook_calendar.event.added_post_request
- name: Webhook Calendar.Person.Subscribed Post Request
  property_count: 2
  slug: webhook_calendar.person.subscribed_post_request
- name: Webhook Event.Canceled Post Request
  property_count: 2
  slug: webhook_event.canceled_post_request
- name: Webhook Event.Created Post Request
  property_count: 2
  slug: webhook_event.created_post_request
- name: Webhook Event.Updated Post Request
  property_count: 2
  slug: webhook_event.updated_post_request
- name: Webhook Guest.Registered Post Request
  property_count: 2
  slug: webhook_guest.registered_post_request
- name: Webhook Guest.Updated Post Request
  property_count: 2
  slug: webhook_guest.updated_post_request
- name: Webhook Ticket.Registered Post Request
  property_count: 2
  slug: webhook_ticket.registered_post_request
jsonld:
- class_count: 0
  name: Api Context
  property_count: 0
  slug: api
- class_count: 0
  name: context Context
  property_count: 121
  slug: context
layout: provider
modified: '2026-06-13'
name: Luma
nav: Providers
network: true
overview: 'Luma publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Calendars API, Events API, Memberships API, and 3 more. Tagged areas include Events, Event Management, Ticketing, Community, and Calendars.


  The Luma catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Luma''s developer surface includes authentication, developer portal, documentation, pricing, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 133
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Luma API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: luma-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 62.3
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/luma/refs/heads/main/screenshots/luma-2026-06-20T184751.png
security:
- kind: authentication
  name: Luma Authentication
  slug: luma-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Luma Domain Security
  slug: luma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Luma Vulnerability Disclosure
  slug: luma-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: luma
tags:
- Events
- Event Management
- Ticketing
- Community
- Calendars
- Guests
- Attendance
website: https://docs.luma.com
---
