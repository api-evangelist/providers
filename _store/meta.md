---
aid: meta
url: https://raw.githubusercontent.com/api-search/social/main/_apis/meta/apis.md
apis:
  - aid: meta:facebook-graph-api-user
    name: Facebook Graph API - User
    tags:
      - Social
      - Users
    humanURL: https://developers.facebook.com/docs/graph-api/reference/user/
    description: Managing user on Facebook.
  - aid: meta:instagram-graph-api-user
    name: Instagram Graph API - User
    tags:
      - Social
      - Users
    humanURL: https://developers.facebook.com/docs/instagram-platform
    description: Managing user on Facebook.
name: Meta
tags:
  - Social
  - Advertising
common:
  - url: https://metastatus.com/
    name: Status
    type: Status
  - url: https://developers.facebook.com/?no_redirect=1
    name: Social technologies | Meta for Developers
    type: Portal
    description: 'null'
  - url: https://developers.facebook.com/docs/
    name: Meta Developer Documentation | Meta APIs, SDKs & Guides
    type: Documentation
    description: 'null'
  - url: https://developers.facebook.com/blog/
    name: News for Developers | Facebook Developers
    type: Blog
    description: 'null'
  - url: https://developers.facebook.com/support/
    name: Developer Support - Meta for Developers
    type: Support
    description: 'null'
  - url: https://developers.facebook.com/support/bugs/
    name: Platform Bug Reports - Meta for Developers
    type: Bugs
    description: 'null'
  - url: https://developers.facebook.com/community/
    name: Developer Community Forum - Meta for Developers
    type: Forums
    description: 'null'
  - url: https://developers.facebook.com/support/faq/
    name: Developer FAQ - Meta for Developers
    type: FAQ
    description: 'null'
  - url: https://developers.facebook.com/tools/explorer/
    name: Graph API Explorer - Meta for Developers
    type: Explorer
    description: 'null'
  - url: https://developers.facebook.com/tools/
    name: Developer Tools - Meta for Developers
    type: Tools
    description: 'null'
  - url: https://developers.facebook.com/apps/
    name: All Apps - Meta for Developers
    type: Applications
    description: 'null'
  - url: https://developers.facebook.com/terms/
    name: Platform Terms - Meta for Developers
    type: TermsOfService
    description: 'null'
  - url: https://developers.facebook.com/incident/report/
    name: Report an Incident - Meta for Developers
    type: IncidentReport
    description: 'null'
  - url: https://developers.facebook.com/m/signup/
    name: Meta for Developers Newsletter | Meta for Developers
    type: Newsletter
    description: 'null'
  - url: https://developers.facebook.com/videos/
    name: Videos for Developers
    type: Videos
  - data:
      - id: free
        name: Free
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Free tier.
        description: Facebook only has a single plan.
    name: Plans
    type: Plans
  - url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting/
    data:
      - name: Platform Rate Limits
        type: Platform
        limit: 200
        paths:
          - /v23.0/me
        metric: request
        domains:
          - graph.facebook.com
        timeframe: hours
        operations:
          - getUser
        description: >-
          Graph API requests made with an application access token are counted
          against that apps rate limit. An apps call count is the number of
          calls it can make during a rolling one hour window and is calculated
          as Calls within one hour = 200 * Number of Users. The Number of Users
          is based on the number of unique daily active users an app has. In
          cases where there are slow periods of daily usage, such as if your app
          has high activity on weekends but low activity over weekdays, the
          weekly and monthly active Users are used to calculate the number of
          Users for your app. Apps with high daily engagement will have higher
          rate limits than apps with low daily engagement, regardless of the
          actual number of app installs. Note that this is not a per User limit
          but a limit on calls made by your app. Any individual User can make
          more than 200 calls per hour using your app, as long as the total
          calls from your app does not exceed the app maximum. For example, if
          your app has 100 Users, your app can make 20,000 calls per hour.
          However, your top ten most engaged Users could make 19,000 of those
          calls.
        userMultiplied: true
    name: Rate Limits - Graph API
    type: RateLimits
    description: Working to build as machine-readable schema.
  - url: https://developers.facebook.com/docs/graph-api/guides/versioning
    data:
      type: Semantic
      parameter: path
    name: Versioning - Graph API
    type: Versioning
    description: Working to build as machine-readable schema.
  - url: https://developers.facebook.com/docs/graph-api/results
    name: Paginated Results
    type: Pagination
    mediaType: text/html
  - data:
      $id: https://example.com/offset-pagination.schema.json
      type: object
      title: Offset-based Pagination Response
      $schema: https://json-schema.org/draft/2020-12/schema
      examples:
        - data:
            - id: '123'
              name: Item 26
            - id: '456'
              name: Item 27
            - id: '789'
              name: Item 28
          paging:
            next: https://graph.facebook.com/{your-user-id}/feed?limit=25&offset=50
            previous: https://graph.facebook.com/{your-user-id}/feed?limit=25&offset=0
        - data:
            - id: '111'
              name: First item
            - id: '222'
              name: Second item
          paging:
            next: https://graph.facebook.com/{your-user-id}/feed?limit=25&offset=25
        - data:
            - id: '999'
              name: Last item
          paging:
            previous: https://graph.facebook.com/{your-user-id}/feed?limit=25&offset=75
        - data: []
          paging:
            next: https://graph.facebook.com/{your-user-id}/feed?limit=25&offset=50
      required:
        - data
        - paging
      properties:
        data:
          type: array
          items:
            description: Individual data item (schema depends on specific endpoint)
          description: >-
            Array containing the endpoint data items for the current offset
            range
        paging:
          type: object
          properties:
            next:
              type: string
              format: uri
              description: >-
                Graph API endpoint URL for the next page of data with updated
                'offset' parameter. Absence indicates last page.
            previous:
              type: string
              format: uri
              description: >-
                Graph API endpoint URL for the previous page of data with
                updated 'offset' parameter. Absence indicates first page.
          description: >-
            Pagination metadata and navigation links with offset-based
            parameters
          minProperties: 1
          additionalProperties: false
      description: >-
        JSON schema for offset-based pagination responses using numeric offsets
        in Graph API
      additionalProperties: false
    name: Offset-based Pagination
    type: Pagination
    mediaType: application/schema+json
    description: Still need to figure out how to reference in OpenAPI.
  - data:
      $id: https://example.com/time-pagination.schema.json
      type: object
      title: Facebook Time-based Pagination Response
      $schema: https://json-schema.org/draft/2020-12/schema
      examples:
        - data:
            - id: '123'
              message: Example post
              created_time: 2013-04-02T07:42:34+0000
            - id: '456'
              message: Another post
              created_time: 2013-03-30T15:29:34+0000
          paging:
            next: >-
              https://graph.facebook.com/{your-user-id}/feed?limit=25&until=1364587774
            previous: >-
              https://graph.facebook.com/{your-user-id}/feed?limit=25&since=1364849754
        - data:
            - id: '789'
              message: First page example
          paging:
            next: >-
              https://graph.facebook.com/{your-user-id}/feed?limit=25&until=1364587774
        - data:
            - id: '999'
              message: Last page example
          paging:
            previous: >-
              https://graph.facebook.com/{your-user-id}/feed?limit=25&since=1364849754
      required:
        - data
        - paging
      properties:
        data:
          type: array
          items:
            description: Individual data item (schema depends on specific endpoint)
          description: Array containing the endpoint data items for the current time range
        paging:
          type: object
          properties:
            next:
              type: string
              format: uri
              description: >-
                Graph API endpoint URL for the next page of data with 'until'
                timestamp parameter
            previous:
              type: string
              format: uri
              description: >-
                Graph API endpoint URL for the previous page of data with
                'since' timestamp parameter
          description: Pagination metadata and navigation links with time-based parameters
          minProperties: 1
          additionalProperties: false
      description: >-
        JSON schema for time-based pagination responses using Unix timestamps in
        Graph API
      additionalProperties: false
    name: Time-based Pagination
    type: Pagination
    mediaType: application/schema+json
    description: Still need to figure out how to reference in OpenAPI.
  - data:
      $id: https://example.com/cursor-pagination.schema.json
      type: object
      title: Facebook Cursor-based Pagination Response
      $schema: https://json-schema.org/draft/2020-12/schema
      examples:
        - data:
            - id: '123'
              name: Example Item 1
            - id: '456'
              name: Example Item 2
          paging:
            next: >-
              https://graph.facebook.com/{your-user-id}/albums?limit=25&after=MTAxNTExOTQ1MjAwNzI5NDE=
            cursors:
              after: MTAxNTExOTQ1MjAwNzI5NDE=
              before: NDMyNzQyODI3OTQw
            previous: >-
              https://graph.facebook.com/{your-user-id}/albums?limit=25&before=NDMyNzQyODI3OTQw
      required:
        - data
        - paging
      properties:
        data:
          type: array
          items:
            description: Individual data item (schema depends on specific endpoint)
          description: Array containing the endpoint data items for the current page
        paging:
          type: object
          required:
            - cursors
          properties:
            next:
              type: string
              format: uri
              description: >-
                Graph API endpoint URL for the next page of data. Absence
                indicates last page.
            cursors:
              type: object
              required:
                - after
                - before
              properties:
                after:
                  type: string
                  pattern: ^[A-Za-z0-9+/=]+$
                  description: Cursor pointing to the end of the current page of data
                before:
                  type: string
                  pattern: ^[A-Za-z0-9+/=]+$
                  description: Cursor pointing to the start of the current page of data
              description: Cursor strings marking the boundaries of the current page
              additionalProperties: false
            previous:
              type: string
              format: uri
              description: >-
                Graph API endpoint URL for the previous page of data. Absence
                indicates first page.
          description: Pagination metadata and navigation links
          additionalProperties: false
      description: JSON schema for cursor-based pagination responses used in Graph API
      additionalProperties: false
    name: Cursor-based Pagination
    type: Pagination
    mediaType: application/schema+json
    description: Still need to figure out how to reference in OpenAPI.
  - url: https://developers.facebook.com/tools/explorer/
    name: Graph API Explorer
    type: Explorer
    description: 'null'
  - url: https://developers.facebook.com/apps/
    name: Applications
    type: Applications
    description: 'null'
  - url: https://developers.facebook.com/docs/graph-api/get-started
    name: Get Started
    type: GettingStarted
    description: 'null'
created: '2024-04-14T00:00:00.000Z'
modified: '2025-08-13'
description: >-
  Meta Platforms, Inc., doing business as Meta, and formerly named Facebook,
  Inc., and TheFacebook, Inc., is an American multinational technology
  conglomerate based in Menlo Park, California. The company owns and operates
  Facebook, Instagram, Threads, and WhatsApp, among other products and services.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.19'

---