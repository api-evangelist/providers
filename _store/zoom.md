---
aid: zoom
url: https://raw.githubusercontent.com/api-search/videos/main/_apis/zoom/apis.md
apis:
  - aid: zoom:zoom-rest-api
    name: Zoom Rest API
    tags: []
    properties:
      - url: https://developers.zoom.us/docs/api/#rest-apis
        type: Documentation
      - url: properties/zoom-openapi-original.yml
        type: OpenAPI
    description: >-
      Our REST APIs are organized based on Zoom product, but the base URL for
      all Zoom REST API requests is https://api.zoom.us/v2/ across products.
  - aid: zoom:zoom-graphql-api
    name: Zoom GraphQL API
    tags: []
    overlays: []
    description: >-
      Zoom GraphQL is in a public beta. See the GraphQL beta FAQ for details.
      GraphQL is a query language for APIs as well as a runtime environment for
      filling those queries with data.
  - name: Zoom Chat API
    tags:
      - Chat
    humanURL: https://developers.zoom.us/docs/api/rest/chat-api/
    overlays:
      - url: overlays/zoom-chat--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/zoom-chat--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/chat-api/
        type: Documentation
    description: >-
      Developers can use the Zoom Chat API to access chat and chat channel data
      to build private services or public applications on the Zoom App
      Marketplace.
    aid: undefined:zoom-chat-api
  - name: Zoom Group API
    tags:
      - Groups
      - Edit
      - Members
    humanURL: https://developers.zoom.us/docs/api/
    overlays:
      - url: overlays/zoom-group--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/zoom-group--openapi-original.yml
        type: OpenAPI
    description: For managing Zoom groups.
    aid: undefined:zoom-group-api
  - name: Zoom Device API
    tags:
      - Device
      - H323
    humanURL: https://developers.zoom.us/docs/api/rest/zoom-phone-api/
    overlays:
      - url: overlays/zoom-device--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/zoom-device--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/zoom-phone-api/
        type: Documentation
    description: >-
      You can access information from Zoom with Zoom Phone APIs to build private
      services or public applications on the Zoom App Marketplace.
    aid: undefined:zoom-device-api
  - name: Zoom Instant Message API
    tags:
      - Groups
      - Edit
      - Members
    humanURL: https://developers.zoom.us/docs/api/
    overlays:
      - url: overlays/zoom-im--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/zoom-im--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/
        type: Documentation
    description: Provides the ability to instant message.
    aid: undefined:zoom-instant-message-api
  - name: Zoom Account API
    tags:
      - Accounts
      - Billing
      - Plan
      - Subscribe
    humanURL: https://developers.zoom.us/docs/api/rest/account/
    overlays:
      - url: overlays/zoom-account--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/zoom-account--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/account/
        type: Documentation
    description: >-
      The Zoom Account API lets developers access data related to Accounts,
      Dashboards, Information Barriers, and Roles. Use this API to build private
      services or public applications on the Zoom App Marketplace. Learn how to
      get your credentials and create private/public applications in our
      Authorization Guide.
    aid: undefined:zoom-account-api
  - name: Zoom Recording API
    tags:
      - Mc
      - Recording
    humanURL: https://developers.zoom.us/docs/video-sdk/web/recording/
    overlays:
      - url: overlays/zoom-recording--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/zoom-recording--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/video-sdk/web/recording/
        type: Documentation
    description: Manage the recordings made of Zoom calls.
    aid: undefined:zoom-recording-api
  - name: Zoom Meeting API
    tags:
      - Meetings
      - Live
      - Register
    humanURL: https://developers.zoom.us/docs/api/rest/meeting/
    overlays:
      - url: overlays/zoom-meeting--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/zoom-meeting--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/meeting/
        type: Documentation
    description: >-
      The Zoom Meeting API lets developers access meeting and webinar data from
      Zoom Meeting. Use this API to build private services or public
      applications on the Zoom App Marketplace.
    aid: undefined:zoom-meeting-api
  - name: Zoom Metrics API
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
    overlays:
      - url: overlays/zoom-metrics--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/zoom-metrics--openapi-original.yml
        type: OpenAPI
    description: Access and manage all of the metrics associate with operating on Zoom.
    aid: undefined:zoom-metrics-api
  - name: Zoom Recording API
    tags: []
    overlays:
      - url: overlays/zoom-recording--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/zoom-recording--openapi-original.yml
        type: OpenAPI
    description: DELETE
    aid: undefined:zoom-recording-api
  - name: Zoom Report API
    tags: []
    humanURL: >-
      https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#tag/Reports
    overlays:
      - url: overlays/zoom-report--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/zoom-report--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/
        type: Documentation
    description: Access and manage reports associated with using Zoom.
    aid: undefined:zoom-report-api
  - name: Zoom User API
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
    overlays:
      - url: overlays/zoom-user--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/zoom-user--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/user/
        type: Documentation
    description: >-
      The Zoom User API lets developers access data related to Contact Groups,
      Groups, and Users. Use this API to build private services or public
      applications on the Zoom App Marketplace. Learn how to get your
      credentials and create private/public applications in our Authorization
      Guide.
    aid: undefined:zoom-user-api
  - name: Zoom Webinar API
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
    overlays:
      - url: overlays/zoom-webinar--openapi-search.yml
        type: OpenAPI
    properties:
      - url: properties/zoom-webinar--openapi-original.yml
        type: OpenAPI
      - url: https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/
        type: Documentation
    description: Provides the ability to manage details of webinars operated via Zoom.
    aid: undefined:zoom-webinar-api
name: Zoom
tags: []
created: 2024/04/14
modified: '2024-07-03'
description: >-
  This is a starter APIs.json that you can use to learn the specification and
  make your own.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'
---