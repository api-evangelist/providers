---
aid: zoom
url: https://raw.githubusercontent.com/api-search/videos/main/_apis/zoom/apis.md
apis:
  - aid: zoom:zoom-graphql-api
    name: Zoom GraphQL API
    tags: []
    description: >-
      Zoom GraphQL is in a public beta. See the GraphQL beta FAQ for details.
      GraphQL is a query language for APIs as well as a runtime environment for
      filling those queries with data.
  - aid: zoom:zoom-chat-api
    name: Zoom Chat API
    tags:
      - Chat
    humanURL: https://developers.zoom.us/docs/api/rest/chat-api/
    properties:
      - url: openapi/zoom-chat--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/chat-api/
        type: Documentation
    description: >-
      Developers can use the Zoom Chat API to access chat and chat channel data
      to build private services or public applications on the Zoom App
      Marketplace.
  - aid: zoom:zoom-group-api
    name: Zoom Group API
    tags:
      - Groups
      - Edit
      - Members
    humanURL: https://developers.zoom.us/docs/api/
    properties:
      - url: openapi/zoom-group--openapi-original.yml
        type: OpenAPI
    description: For managing Zoom groups.
  - aid: zoom:zoom-device-api
    name: Zoom Device API
    tags:
      - Device
      - H323
    humanURL: https://developers.zoom.us/docs/api/rest/zoom-phone-api/
    properties:
      - url: openapi/zoom-device--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/zoom-phone-api/
        type: Documentation
    description: >-
      You can access information from Zoom with Zoom Phone APIs to build private
      services or public applications on the Zoom App Marketplace.
  - aid: zoom:zoom-instant-message-api
    name: Zoom Instant Message API
    tags:
      - Groups
      - Edit
      - Members
    humanURL: https://developers.zoom.us/docs/api/
    properties:
      - url: openapi/zoom-im--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/
        type: Documentation
    description: Provides the ability to instant message.
  - aid: zoom:zoom-account-api
    name: Zoom Account API
    tags:
      - Accounts
      - Billing
      - Plan
      - Subscribe
    humanURL: https://developers.zoom.us/docs/api/rest/account/
    properties:
      - url: openapi/zoom-account--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/account/
        type: Documentation
    description: >-
      The Zoom Account API lets developers access data related to Accounts,
      Dashboards, Information Barriers, and Roles. Use this API to build private
      services or public applications on the Zoom App Marketplace. Learn how to
      get your credentials and create private/public applications in our
      Authorization Guide.
  - aid: zoom:zoom-recording-api
    name: Zoom Recording API
    tags:
      - Mc
      - Recording
    humanURL: https://developers.zoom.us/docs/video-sdk/web/recording/
    properties:
      - url: openapi/zoom-recording--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/video-sdk/web/recording/
        type: Documentation
    description: Manage the recordings made of Zoom calls.
  - aid: zoom:zoom-meeting-api
    name: Zoom Meeting API
    tags:
      - Meetings
      - Live
      - Register
    humanURL: https://developers.zoom.us/docs/api/rest/meeting/
    properties:
      - url: openapi/zoom-meeting--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/meeting/
        type: Documentation
    description: >-
      The Zoom Meeting API lets developers access meeting and webinar data from
      Zoom Meeting. Use this API to build private services or public
      applications on the Zoom App Marketplace.
  - aid: zoom:zoom-metrics-api
    name: Zoom Metrics API
    tags:
      - Crc
      - Metrics
      - Meetingdetail
      - Meetings
      - Qos
      - Webinardetail
      - Webinars
      - Zoomroomdetail
      - Zoomrooms
    humanURL: https://developers.zoom.us/docs/api/
    properties:
      - url: openapi/zoom-metrics--openapi-original.yml
        type: OpenAPI
    description: Access and manage all of the metrics associate with operating on Zoom.
  - aid: zoom:zoom-recording-api
    name: Zoom Recording API
    tags: []
    properties:
      - url: openapi/zoom-recording--openapi-original.yml
        type: OpenAPI
    description: DELETE
  - aid: zoom:zoom-report-api
    name: Zoom Report API
    tags: []
    humanURL: >-
      https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#tag/Reports
    properties:
      - url: openapi/zoom-report--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/
        type: Documentation
    description: Access and manage reports associated with using Zoom.
  - aid: zoom:zoom-user-api
    name: Zoom User API
    tags:
      - Assistants
      - Users
      - Sets
      - Autocreate
      - Checkemail
      - Checkzpk
      - Custcreate
      - Activate
      - Deactivate
      - Getbyemail
      - Pending
      - Permanentdelete
      - Revoketoken
      - Scheduleforhost
      - Ssocreate
      - Updatepassword
    humanURL: https://developers.zoom.us/docs/api/rest/user/
    properties:
      - url: openapi/zoom-user--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/user/
        type: Documentation
    description: >-
      The Zoom User API lets developers access data related to Contact Groups,
      Groups, and Users. Use this API to build private services or public
      applications on the Zoom App Marketplace. Learn how to get your
      credentials and create private/public applications in our Authorization
      Guide.
  - aid: zoom:zoom-webinar-api
    name: Zoom Webinar API
    tags:
      - Attendees
      - Webinar
      - Registrations
      - Panelists
      - Polls
      - Questions
      - Register
      - Approve
      - Registrants
      - Cancel
      - Uu
    humanURL: >-
      https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#tag/Webinars
    properties:
      - url: openapi/zoom-webinar--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/
        type: Documentation
    description: Provides the ability to manage details of webinars operated via Zoom.
name: Zoom
tags:
  - Videos
  - Video Conferences
  - Webinars
created: 2024/04/14
modified: '2024-12-24'
description: >-
  This is a starter APIs.json that you can use to learn the specification and
  make your own.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'

---