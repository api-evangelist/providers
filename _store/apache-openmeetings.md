---
aid: apache-openmeetings
name: Apache OpenMeetings
description: Apache OpenMeetings is a web conferencing and collaboration tool that provides video conferencing, instant messaging, white board, collaborative document editing, and other groupware tools. It offers integration APIs for LMS platforms.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Collaboration
  - Video Conferencing
  - Web Conferencing
  - Whiteboard
  - Apache
  - Open Source
  - Conferencing
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-openmeetings/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-openmeetings:apache-openmeetings-rest-api
    name: Apache OpenMeetings REST API
    description: The OpenMeetings REST API provides endpoints for managing rooms, users, recordings, calendars, and file uploads, with SOAP API support for legacy integrations and plugin APIs for LMS integration (Moodle, Sakai).
    humanURL: https://openmeetings.apache.org/RestAPISample.html
    tags:
      - Conferencing
      - REST
      - SOAP
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://openmeetings.apache.org/RestAPISample.html
      - type: OpenAPI
        url: openapi/apache-openmeetings-rest-api.json
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/openmeetings
  - type: Documentation
    url: https://openmeetings.apache.org/
  - type: GettingStarted
    url: https://openmeetings.apache.org/installation.html
  - type: SpectralRules
    url: rules/apache-openmeetings-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-openmeetings-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/conferencing-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-openmeetings-context.jsonld
  - type: Features
    data:
      - name: Video Conferencing
        description: HTML5-based audio/video conferencing with multi-resolution camera support
      - name: Screen Sharing
        description: Full screen sharing and recording capabilities
      - name: Whiteboard
        description: Multi-instance collaborative whiteboard with document import
      - name: File Management
        description: Advanced file explorer with drag-and-drop for private and public drives
      - name: Calendar Integration
        description: Meeting planning with email invitations and secure hash links
      - name: Recording
        description: Session recording to MP4 with audio and video capture
      - name: REST API
        description: Full REST API for programmatic management of rooms, users, and recordings
      - name: SOAP API
        description: Legacy SOAP API for integrations requiring XML-based communication
  - type: UseCases
    data:
      - name: LMS Integration
        description: Integrate OpenMeetings with Moodle, Sakai, and other LMS platforms
      - name: Corporate Conferencing
        description: Host virtual meetings and webinars for distributed teams
      - name: Remote Education
        description: Deliver interactive online courses with whiteboard and screen sharing
      - name: Custom Conferencing Portal
        description: Build branded conferencing portals using the REST API
  - type: Integrations
    data:
      - name: Moodle
        description: Official Moodle plugin for LMS integration
      - name: Sakai
        description: Sakai CLE integration for academic conferencing
      - name: LDAP/Active Directory
        description: Enterprise authentication via LDAP and ADS
      - name: OAuth2
        description: Social login via OAuth2 providers
      - name: Asterisk/VoIP
        description: VoIP integration via Asterisk for phone conferencing
      - name: CalDAV
        description: Calendar synchronization via CalDAV protocol
      - name: Kurento Media Server
        description: WebRTC media server for streaming and recording
---
