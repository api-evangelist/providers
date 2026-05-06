---
aid: canvas
url: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/apis.yml
name: Canvas
description: Canvas is Instructure's open-source learning management system (LMS) used by K-12, higher education, and corporate training organizations to deliver courses, assessments, and learner communication. Canvas exposes a comprehensive REST API and a GraphQL endpoint for reading and modifying courses, assignments, quizzes, grades, users, enrollments, content, and account administration, and it integrates with external tools through LTI, Caliper, and live event streams.
type: Index
x-type: company
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Education
  - EdTech
  - GraphQL
  - Learning Management System
  - LMS
  - LTI
  - Open Source
  - REST
created: '2025-01-14'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: canvas:canvas-lms-rest-api
    name: Canvas LMS REST API
    description: The Canvas LMS REST API provides programmatic access to courses, assignments, quizzes, grades, users, enrollments, accounts, discussions, files, modules, rubrics, submissions, SIS imports, and account administration. It uses OAuth 2.0 access tokens and returns JSON with ISO 8601 timestamps, supporting pagination, request throttling, masquerading, and compound documents.
    humanURL: https://canvas.instructure.com/doc/api/
    tags:
      - Education
      - LMS
      - REST
    properties:
      - type: Documentation
        url: https://canvas.instructure.com/doc/api/
      - type: Authentication
        url: https://canvas.instructure.com/doc/api/file.oauth.html
      - type: Pagination
        url: https://canvas.instructure.com/doc/api/file.pagination.html
      - type: GitHub Repository
        url: https://github.com/instructure/canvas-lms
    x-features:
      - OAuth 2.0 authentication with access tokens
      - JSON responses with ISO 8601 timestamps
      - 64-bit integer IDs and string ID support
      - Form-encoded and JSON request bodies
      - Pagination for large result sets
      - Request throttling and quota controls
      - Masquerading for acting on behalf of users
      - Compound documents for linked resources
      - File upload workflows
      - SIS imports and roster sync
      - Live event streams via Canvas Data services
      - Caliper event format compatibility
      - xAPI statement support
    x-use-cases:
      - Building custom student dashboards or mobile apps
      - Automating course provisioning and enrollment via SIS imports
      - Syncing grades and assignments to external gradebooks
      - Analytics and learning-event data pipelines
      - Integrating third-party tools through LTI
      - Bulk content migration between courses or institutions
      - Institutional reporting and audit-log extraction
  - aid: canvas:canvas-lms-graphql-api
    name: Canvas LMS GraphQL API
    description: The Canvas LMS GraphQL API is an alternative to the REST API that lets clients request exactly the fields they need across Canvas resources in a single request. It is well suited for dashboards and aggregated views that otherwise require many REST round-trips.
    humanURL: https://canvas.instructure.com/doc/api/file.graphql.html
    tags:
      - Education
      - GraphQL
      - LMS
    properties:
      - type: Documentation
        url: https://canvas.instructure.com/doc/api/file.graphql.html
    x-features:
      - Typed GraphQL schema over Canvas resources
      - Single-request fetches across courses, users, and assignments
      - Reduced over-fetching for dashboards
      - OAuth 2.0 bearer-token authentication
    x-use-cases:
      - Building performant student or instructor dashboards
      - Aggregating course, assignment, and grade data in one request
      - Mobile apps with limited bandwidth
  - aid: canvas:canvas-lti-integrations
    name: Canvas LTI Integrations
    description: Canvas supports Learning Tools Interoperability (LTI 1.1 and LTI 1.3 / Advantage) for embedding external tools, assignments, and content into courses with deep linking, grade passback, and names-and-roles service.
    humanURL: https://canvas.instructure.com/doc/api/file.tools_intro.html
    tags:
      - Education
      - LMS
      - LTI
    properties:
      - type: Documentation
        url: https://canvas.instructure.com/doc/api/file.tools_intro.html
    x-features:
      - LTI 1.1 and LTI 1.3 / Advantage support
      - Deep linking for tool placements
      - Assignment and Grade Services (AGS) for grade passback
      - Names and Roles Provisioning Service (NRPS)
      - Configurable tool placements across Canvas UI
    x-use-cases:
      - Embedding third-party learning tools in Canvas courses
      - Passing grades from external graders back to Canvas
      - Provisioning course rosters into external tools
common:
  - type: Website
    url: https://www.instructure.com/canvas
  - type: Documentation
    url: https://canvas.instructure.com/doc/api/
  - type: GitHub Organization
    url: https://github.com/instructure
  - type: GitHub Repository
    url: https://github.com/instructure/canvas-lms
  - type: Status
    url: https://status.instructure.com/
  - type: Community
    url: https://community.canvaslms.com/
  - type: Privacy Policy
    url: https://www.instructure.com/policies/privacy
  - type: Terms of Service
    url: https://www.instructure.com/policies/product-acceptable-use
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
