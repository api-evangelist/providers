---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Apache Openmeetings Agentic Access
  operation_count: 56
  slug: apache-openmeetings-agentic-access
  summary_line: 56 operations · 24 acting
api_count: 1
apis:
- baseURL_template: https://{host}:5443/openmeetings/services
  baseurl_source: spec_template
  description: The CalendarService API from Apache OpenMeetings — 8 operation(s) for calendarservice.
  name: Apache OpenMeetings CalendarService API
  slug: apache-openmeetings-calendarservice-api
- baseURL_template: https://{host}:5443/openmeetings/services
  baseurl_source: spec_template
  description: The ErrorService API from Apache OpenMeetings — 2 operation(s) for errorservice.
  name: Apache OpenMeetings ErrorService API
  slug: apache-openmeetings-errorservice-api
- baseURL_template: https://{host}:5443/openmeetings/services
  baseurl_source: spec_template
  description: The FileService API from Apache OpenMeetings — 8 operation(s) for fileservice.
  name: Apache OpenMeetings FileService API
  slug: apache-openmeetings-fileservice-api
- baseURL_template: https://{host}:5443/openmeetings/services
  baseurl_source: spec_template
  description: The GroupService API from Apache OpenMeetings — 5 operation(s) for groupservice.
  name: Apache OpenMeetings GroupService API
  slug: apache-openmeetings-groupservice-api
- baseURL_template: https://{host}:5443/openmeetings/services
  baseurl_source: spec_template
  description: The InfoService API from Apache OpenMeetings — 3 operation(s) for infoservice.
  name: Apache OpenMeetings InfoService API
  slug: apache-openmeetings-infoservice-api
- baseURL_template: https://{host}:5443/openmeetings/services
  baseurl_source: spec_template
  description: The NetTestService API from Apache OpenMeetings — 1 operation(s) for nettestservice.
  name: Apache OpenMeetings NetTestService API
  slug: apache-openmeetings-nettestservice-api
- baseURL_template: https://{host}:5443/openmeetings/services
  baseurl_source: spec_template
  description: The RecordingService API from Apache OpenMeetings — 4 operation(s) for recordingservice.
  name: Apache OpenMeetings RecordingService API
  slug: apache-openmeetings-recordingservice-api
- baseURL_template: https://{host}:5443/openmeetings/services
  baseurl_source: spec_template
  description: The RoomService API from Apache OpenMeetings — 11 operation(s) for roomservice.
  name: Apache OpenMeetings RoomService API
  slug: apache-openmeetings-roomservice-api
- baseURL_template: https://{host}:5443/openmeetings/services
  baseurl_source: spec_template
  description: The UserService API from Apache OpenMeetings — 5 operation(s) for userservice.
  name: Apache OpenMeetings UserService API
  slug: apache-openmeetings-userservice-api
- baseURL_template: https://{host}:5443/openmeetings/services
  baseurl_source: spec_template
  description: The WbService API from Apache OpenMeetings — 4 operation(s) for wbservice.
  name: Apache OpenMeetings WbService API
  slug: apache-openmeetings-wbservice-api
artifact_total: 146
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache OpenMeetings REST CalendarService API
  slug: open-apache-openmeetings-calendarservice-api
- collection_type: open
  name: Apache OpenMeetings REST CalendarService ErrorService API
  slug: open-apache-openmeetings-errorservice-api
- collection_type: open
  name: Apache OpenMeetings REST CalendarService FileService API
  slug: open-apache-openmeetings-fileservice-api
- collection_type: open
  name: Apache OpenMeetings REST CalendarService GroupService API
  slug: open-apache-openmeetings-groupservice-api
- collection_type: open
  name: Apache OpenMeetings REST CalendarService InfoService API
  slug: open-apache-openmeetings-infoservice-api
- collection_type: open
  name: Apache OpenMeetings REST CalendarService NetTestService API
  slug: open-apache-openmeetings-nettestservice-api
- collection_type: open
  name: Apache OpenMeetings REST CalendarService RecordingService API
  slug: open-apache-openmeetings-recordingservice-api
- collection_type: open
  name: Apache OpenMeetings REST API
  slug: open-apache-openmeetings-rest-api
- collection_type: open
  name: Apache OpenMeetings REST CalendarService RoomService API
  slug: open-apache-openmeetings-roomservice-api
- collection_type: open
  name: Apache OpenMeetings REST CalendarService UserService API
  slug: open-apache-openmeetings-userservice-api
- collection_type: open
  name: Apache OpenMeetings REST CalendarService WbService API
  slug: open-apache-openmeetings-wbservice-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-openmeetings-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-openmeetings-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-openmeetings-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/openmeetings
- group: docs
  title: ''
  type: Documentation
  url: https://openmeetings.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://openmeetings.apache.org/installation.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-openmeetings-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-openmeetings-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apache-openmeetings-context.jsonld
created: '2026-03-16'
description: Apache OpenMeetings is a web conferencing and collaboration tool that provides video conferencing, instant messaging, white board, collaborative document editing, and other groupware tools. It offers integration APIs for LMS platforms.
examples:
- key_count: 13
  name: Apache Openmeetings Address Example
  slug: apache-openmeetings-address-example
- key_count: 19
  name: Apache Openmeetings Appointment Dto Example
  slug: apache-openmeetings-appointment-dto-example
- key_count: 1
  name: Apache Openmeetings Appointment Dto List Wrapper Example
  slug: apache-openmeetings-appointment-dto-list-wrapper-example
- key_count: 1
  name: Apache Openmeetings Appointment Dto Wrapper Example
  slug: apache-openmeetings-appointment-dto-wrapper-example
- key_count: 7
  name: Apache Openmeetings External User Dto Example
  slug: apache-openmeetings-external-user-dto-example
- key_count: 4
  name: Apache Openmeetings File Explorer Object Example
  slug: apache-openmeetings-file-explorer-object-example
- key_count: 1
  name: Apache Openmeetings File Explorer Object Wrapper Example
  slug: apache-openmeetings-file-explorer-object-wrapper-example
- key_count: 13
  name: Apache Openmeetings File Item Dto Example
  slug: apache-openmeetings-file-item-dto-example
- key_count: 1
  name: Apache Openmeetings File Item Dto List Wrapper Example
  slug: apache-openmeetings-file-item-dto-list-wrapper-example
- key_count: 1
  name: Apache Openmeetings File Item Dto Wrapper Example
  slug: apache-openmeetings-file-item-dto-wrapper-example
- key_count: 3
  name: Apache Openmeetings Group Dto Example
  slug: apache-openmeetings-group-dto-example
- key_count: 1
  name: Apache Openmeetings Group Dto List Wrapper Example
  slug: apache-openmeetings-group-dto-list-wrapper-example
- key_count: 3
  name: Apache Openmeetings Health Example
  slug: apache-openmeetings-health-example
- key_count: 1
  name: Apache Openmeetings Health Wrapper Example
  slug: apache-openmeetings-health-wrapper-example
- key_count: 3
  name: Apache Openmeetings Info Example
  slug: apache-openmeetings-info-example
- key_count: 1
  name: Apache Openmeetings Info Wrapper Example
  slug: apache-openmeetings-info-wrapper-example
- key_count: 12
  name: Apache Openmeetings Invitation Dto Example
  slug: apache-openmeetings-invitation-dto-example
- key_count: 2
  name: Apache Openmeetings Meeting Member Dto Example
  slug: apache-openmeetings-meeting-member-dto-example
- key_count: 12
  name: Apache Openmeetings Recording Dto Example
  slug: apache-openmeetings-recording-dto-example
- key_count: 1
  name: Apache Openmeetings Recording Dto List Wrapper Example
  slug: apache-openmeetings-recording-dto-list-wrapper-example
- key_count: 23
  name: Apache Openmeetings Room Dto Example
  slug: apache-openmeetings-room-dto-example
- key_count: 1
  name: Apache Openmeetings Room Dto List Wrapper Example
  slug: apache-openmeetings-room-dto-list-wrapper-example
- key_count: 1
  name: Apache Openmeetings Room Dto Wrapper Example
  slug: apache-openmeetings-room-dto-wrapper-example
- key_count: 3
  name: Apache Openmeetings Room File Dto Example
  slug: apache-openmeetings-room-file-dto-example
- key_count: 8
  name: Apache Openmeetings Room Options Dto Example
  slug: apache-openmeetings-room-options-dto-example
- key_count: 2
  name: Apache Openmeetings Service Result Example
  slug: apache-openmeetings-service-result-example
- key_count: 1
  name: Apache Openmeetings Service Result Wrapper Example
  slug: apache-openmeetings-service-result-wrapper-example
- key_count: 13
  name: Apache Openmeetings User Dto Example
  slug: apache-openmeetings-user-dto-example
- key_count: 1
  name: Apache Openmeetings User Dto List Wrapper Example
  slug: apache-openmeetings-user-dto-list-wrapper-example
- key_count: 1
  name: Apache Openmeetings User Dto Wrapper Example
  slug: apache-openmeetings-user-dto-wrapper-example
- key_count: 4
  name: Apache Openmeetings User Search Result Example
  slug: apache-openmeetings-user-search-result-example
- key_count: 1
  name: Apache Openmeetings User Search Result Wrapper Example
  slug: apache-openmeetings-user-search-result-wrapper-example
features:
- description: HTML5-based audio/video conferencing with multi-resolution camera support
  name: Video Conferencing
- description: Full screen sharing and recording capabilities
  name: Screen Sharing
- description: Multi-instance collaborative whiteboard with document import
  name: Whiteboard
- description: Advanced file explorer with drag-and-drop for private and public drives
  name: File Management
- description: Meeting planning with email invitations and secure hash links
  name: Calendar Integration
- description: Session recording to MP4 with audio and video capture
  name: Recording
- description: Full REST API for programmatic management of rooms, users, and recordings
  name: REST API
- description: Legacy SOAP API for integrations requiring XML-based communication
  name: SOAP API
finops:
- name: Apache Openmeetings Finops
  service_category: API
  slug: apache-openmeetings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-openmeetings.png
integrations:
- description: Official Moodle plugin for LMS integration
  name: Moodle
- description: Sakai CLE integration for academic conferencing
  name: Sakai
- description: Enterprise authentication via LDAP and ADS
  name: LDAP/Active Directory
- description: Social login via OAuth2 providers
  name: OAuth2
- description: VoIP integration via Asterisk for phone conferencing
  name: Asterisk/VoIP
- description: Calendar synchronization via CalDAV protocol
  name: CalDAV
- description: WebRTC media server for streaming and recording
  name: Kurento Media Server
json_schemas:
- name: Address
  property_count: 13
  slug: apache-openmeetings-address
- name: AppointmentDTOListWrapper
  property_count: 1
  slug: apache-openmeetings-appointment-dto-list-wrapper
- name: AppointmentDTO
  property_count: 19
  slug: apache-openmeetings-appointment-dto
- name: AppointmentDTOWrapper
  property_count: 1
  slug: apache-openmeetings-appointment-dto-wrapper
- name: ExternalUserDTO
  property_count: 7
  slug: apache-openmeetings-external-user-dto
- name: FileExplorerObject
  property_count: 4
  slug: apache-openmeetings-file-explorer-object
- name: FileExplorerObjectWrapper
  property_count: 1
  slug: apache-openmeetings-file-explorer-object-wrapper
- name: FileItemDTOListWrapper
  property_count: 1
  slug: apache-openmeetings-file-item-dto-list-wrapper
- name: FileItemDTO
  property_count: 13
  slug: apache-openmeetings-file-item-dto
- name: FileItemDTOWrapper
  property_count: 1
  slug: apache-openmeetings-file-item-dto-wrapper
- name: GroupDTOListWrapper
  property_count: 1
  slug: apache-openmeetings-group-dto-list-wrapper
- name: GroupDTO
  property_count: 3
  slug: apache-openmeetings-group-dto
- name: Health
  property_count: 3
  slug: apache-openmeetings-health
- name: HealthWrapper
  property_count: 1
  slug: apache-openmeetings-health-wrapper
- name: Info
  property_count: 3
  slug: apache-openmeetings-info
- name: InfoWrapper
  property_count: 1
  slug: apache-openmeetings-info-wrapper
- name: InvitationDTO
  property_count: 12
  slug: apache-openmeetings-invitation-dto
- name: MeetingMemberDTO
  property_count: 2
  slug: apache-openmeetings-meeting-member-dto
- name: RecordingDTOListWrapper
  property_count: 1
  slug: apache-openmeetings-recording-dto-list-wrapper
- name: RecordingDTO
  property_count: 12
  slug: apache-openmeetings-recording-dto
- name: RoomDTOListWrapper
  property_count: 1
  slug: apache-openmeetings-room-dto-list-wrapper
- name: RoomDTO
  property_count: 23
  slug: apache-openmeetings-room-dto
- name: RoomDTOWrapper
  property_count: 1
  slug: apache-openmeetings-room-dto-wrapper
- name: RoomFileDTO
  property_count: 3
  slug: apache-openmeetings-room-file-dto
- name: RoomOptionsDTO
  property_count: 8
  slug: apache-openmeetings-room-options-dto
- name: ServiceResult
  property_count: 2
  slug: apache-openmeetings-service-result
- name: ServiceResultWrapper
  property_count: 1
  slug: apache-openmeetings-service-result-wrapper
- name: UserDTOListWrapper
  property_count: 1
  slug: apache-openmeetings-user-dto-list-wrapper
- name: UserDTO
  property_count: 13
  slug: apache-openmeetings-user-dto
- name: UserDTOWrapper
  property_count: 1
  slug: apache-openmeetings-user-dto-wrapper
- name: UserSearchResult
  property_count: 4
  slug: apache-openmeetings-user-search-result
- name: UserSearchResultWrapper
  property_count: 1
  slug: apache-openmeetings-user-search-result-wrapper
json_structures:
- name: Apache Openmeetings Address Structure
  property_count: 13
  slug: apache-openmeetings-address-structure
- name: Apache Openmeetings Appointment Dto List Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-appointment-dto-list-wrapper-structure
- name: Apache Openmeetings Appointment Dto Structure
  property_count: 19
  slug: apache-openmeetings-appointment-dto-structure
- name: Apache Openmeetings Appointment Dto Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-appointment-dto-wrapper-structure
- name: Apache Openmeetings External User Dto Structure
  property_count: 7
  slug: apache-openmeetings-external-user-dto-structure
- name: Apache Openmeetings File Explorer Object Structure
  property_count: 4
  slug: apache-openmeetings-file-explorer-object-structure
- name: Apache Openmeetings File Explorer Object Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-file-explorer-object-wrapper-structure
- name: Apache Openmeetings File Item Dto List Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-file-item-dto-list-wrapper-structure
- name: Apache Openmeetings File Item Dto Structure
  property_count: 13
  slug: apache-openmeetings-file-item-dto-structure
- name: Apache Openmeetings File Item Dto Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-file-item-dto-wrapper-structure
- name: Apache Openmeetings Group Dto List Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-group-dto-list-wrapper-structure
- name: Apache Openmeetings Group Dto Structure
  property_count: 3
  slug: apache-openmeetings-group-dto-structure
- name: Apache Openmeetings Health Structure
  property_count: 3
  slug: apache-openmeetings-health-structure
- name: Apache Openmeetings Health Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-health-wrapper-structure
- name: Apache Openmeetings Info Structure
  property_count: 3
  slug: apache-openmeetings-info-structure
- name: Apache Openmeetings Info Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-info-wrapper-structure
- name: Apache Openmeetings Invitation Dto Structure
  property_count: 12
  slug: apache-openmeetings-invitation-dto-structure
- name: Apache Openmeetings Meeting Member Dto Structure
  property_count: 2
  slug: apache-openmeetings-meeting-member-dto-structure
- name: Apache Openmeetings Recording Dto List Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-recording-dto-list-wrapper-structure
- name: Apache Openmeetings Recording Dto Structure
  property_count: 12
  slug: apache-openmeetings-recording-dto-structure
- name: Apache Openmeetings Room Dto List Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-room-dto-list-wrapper-structure
- name: Apache Openmeetings Room Dto Structure
  property_count: 23
  slug: apache-openmeetings-room-dto-structure
- name: Apache Openmeetings Room Dto Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-room-dto-wrapper-structure
- name: Apache Openmeetings Room File Dto Structure
  property_count: 3
  slug: apache-openmeetings-room-file-dto-structure
- name: Apache Openmeetings Room Options Dto Structure
  property_count: 8
  slug: apache-openmeetings-room-options-dto-structure
- name: Apache Openmeetings Service Result Structure
  property_count: 2
  slug: apache-openmeetings-service-result-structure
- name: Apache Openmeetings Service Result Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-service-result-wrapper-structure
- name: Apache Openmeetings User Dto List Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-user-dto-list-wrapper-structure
- name: Apache Openmeetings User Dto Structure
  property_count: 13
  slug: apache-openmeetings-user-dto-structure
- name: Apache Openmeetings User Dto Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-user-dto-wrapper-structure
- name: Apache Openmeetings User Search Result Structure
  property_count: 4
  slug: apache-openmeetings-user-search-result-structure
- name: Apache Openmeetings User Search Result Wrapper Structure
  property_count: 1
  slug: apache-openmeetings-user-search-result-wrapper-structure
jsonld:
- class_count: 32
  name: Apache Openmeetings Context
  property_count: 105
  slug: apache-openmeetings-context
layout: provider
modified: '2026-05-19'
name: Apache OpenMeetings
nav: Providers
network: true
overview: 'Apache OpenMeetings publishes 10 APIs on the [APIs.io](https://apis.io/) network, including CalendarService API, ErrorService API, FileService API, and 7 more. Tagged areas include Collaboration, Video Conferencing, Web Conferencing, Whiteboard, and Apache.


  The Apache OpenMeetings catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache OpenMeetings'' developer surface includes documentation, getting-started guide, and 7 more developer resources.'
plans:
- name: Apache Openmeetings Plans Pricing
  plan_count: 3
  slug: apache-openmeetings-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Apache Openmeetings Rate Limits
  slug: apache-openmeetings-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache OpenMeetings API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-openmeetings-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Apache OpenMeetings API Rules
  rule_count: 17
  severity_counts:
    error: 4
    hint: 0
    info: 4
    warn: 9
  slug: apache-openmeetings-spectral-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 53.3
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-openmeetings/refs/heads/main/screenshots/apache-openmeetings-2026-06-20T172128.png
security:
- kind: domain-security
  name: Apache Openmeetings Domain Security
  slug: apache-openmeetings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Openmeetings Vulnerability Disclosure
  slug: apache-openmeetings-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-openmeetings
tags:
- Collaboration
- Video Conferencing
- Web Conferencing
- Whiteboard
- Apache
- Open-Source
- Conferencing
use_cases:
- description: Integrate OpenMeetings with Moodle, Sakai, and other LMS platforms
  name: LMS Integration
- description: Host virtual meetings and webinars for distributed teams
  name: Corporate Conferencing
- description: Deliver interactive online courses with whiteboard and screen sharing
  name: Remote Education
- description: Build branded conferencing portals using the REST API
  name: Custom Conferencing Portal
---
