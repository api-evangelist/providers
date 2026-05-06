---
aid: figma
name: Figma
description: Figma is a collaborative interface design tool with a comprehensive REST API for accessing and manipulating design files, projects, and teams.
url: https://raw.githubusercontent.com/api-evangelist/figma/refs/heads/main/apis.yml
image: https://www.figma.com/favicon.ico
tags:
  - Collaboration
  - Design
  - Graphics
  - Interfaces
  - Prototypes
  - Prototyping
  - UI/UX
created: '2023-11-22'
modified: '2026-05-04'
specificationVersion: '0.19'
type: Index
apis:
  - aid: figma:figma-api
    name: Figma API
    description: Figma allows designers to create and prototype their digital experiences - together in real-time and in one place - helping them turn their ideas and visions into products, faster. Figma's mission is to make design accessible to everyone. The Figma API is one of the ways we aim to do that.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://www.figma.com/developers
    tags:
      - Design
      - Users
    properties:
      - type: OpenAPI
        url: openapi/figma-api-openapi.yml
      - type: OpenAPI
        url: openapi/figma-rest-api-openapi.yml
        title: Figma REST API
      - type: AsyncAPI
        url: asyncapi/figma-webhooks-asyncapi.yml
      - type: JSONSchema
        url: json-schema/figma-file-schema.json
      - type: JSONSchema
        url: json-schema/figma-component-schema.json
      - type: JSONSchema
        url: json-schema/figma-user-schema.json
      - type: JSONSchema
        url: json-schema/figma-error-response-payload-schema.json
      - type: JSONSchema
        url: json-schema/figma-get-me-response-body-schema.json
      - type: JSONStructure
        url: json-structure/figma-get-me-response-body-structure.json
      - type: JSONStructure
        url: json-structure/figma-error-response-payload-structure.json
      - type: JSONStructure
        url: json-structure/figma-user-structure.json
      - type: JSONLD
        url: json-ld/figma-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/
  - aid: figma:figma-rest-api
    name: Figma REST API
    description: The Figma REST API provides programmatic access to Figma files, comments, components, and related resources. It enables developers to read and interact with design data, export assets, manage comments and reactions, and query published components and styles from team libraries.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/
    tags:
      - Comments
      - Components
      - Files
      - Projects
      - Users
    properties:
      - type: OpenAPI
        url: openapi/figma-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-rest-get-file-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-file-nodes-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-images-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-image-fills-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-file-versions-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-comments-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-post-comment-request-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-reactions-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-team-components-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-file-components-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-component-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-team-component-sets-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-team-styles-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-team-projects-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-get-project-files-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-error-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-branch-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-canvas-node-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-client-meta-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-color-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-comment-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-component-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-component-set-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-document-node-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-documentation-link-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-frame-info-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-pagination-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-project-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-project-file-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-published-component-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-published-component-set-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-published-style-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-reaction-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-style-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-success-response-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-user-schema.json
      - type: JSONSchema
        url: json-schema/figma-rest-version-schema.json
      - type: JSONLD
        url: json-ld/figma-rest-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/
  - aid: figma:figma-files-api
    name: Figma Files API
    description: Figma Files API provides access to design file data including document trees, nodes, images, version history, and file metadata. Read and export design data from Figma files programmatically.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/file-endpoints/
    tags:
      - Dev Resources
      - Files
    properties:
      - type: OpenAPI
        url: openapi/figma-files-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-files-get-file-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-branch-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-canvas-node-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-color-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-comment-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-component-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-component-set-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-delete-dev-resource-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-dev-resource-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-document-node-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-documentation-link-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-error-response-payload-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-frame-info-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-get-dev-resources-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-published-component-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-published-component-set-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-reaction-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-style-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-style-type-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-user-schema.json
      - type: JSONSchema
        url: json-schema/figma-files-version-schema.json
      - type: JSONLD
        url: json-ld/figma-files-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/file-endpoints/
  - aid: figma:figma-images-api
    name: Figma Images API
    description: Figma Images API provides endpoints for rendering and exporting images from Figma files in various formats including PNG, JPG, SVG, and PDF.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/file-endpoints/
    tags:
      - Export
      - Images
      - Rendering
    properties:
      - type: OpenAPI
        url: openapi/figma-images-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-images-get-images-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-images-bad-request-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-images-error-response-payload-schema.json
      - type: JSONSchema
        url: json-schema/figma-images-forbidden-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-images-internal-server-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-images-not-found-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-images-too-many-requests-error-schema.json
      - type: JSONLD
        url: json-ld/figma-images-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/file-endpoints/
  - aid: figma:figma-teams-api
    name: Figma Teams API
    description: Figma Teams API provides endpoints for managing team-level resources including webhooks, projects, and team configuration.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/file-endpoints/
    tags:
      - Teams
      - Webhooks
    properties:
      - type: OpenAPI
        url: openapi/figma-teams-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-teams-get-team-webhooks-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-teams-webhook-v2-schema.json
      - type: JSONSchema
        url: json-schema/figma-teams-webhook-v2-event-schema.json
      - type: JSONSchema
        url: json-schema/figma-teams-webhook-v2-status-schema.json
      - type: JSONSchema
        url: json-schema/figma-teams-error-response-payload-schema.json
      - type: JSONSchema
        url: json-schema/figma-teams-forbidden-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-teams-internal-server-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-teams-not-found-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-teams-too-many-requests-error-schema.json
      - type: JSONLD
        url: json-ld/figma-teams-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/file-endpoints/
  - aid: figma:figma-projects-api
    name: Figma Projects API
    description: Figma Projects API provides endpoints for listing team projects and retrieving project files.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/projects-types/
    tags:
      - Files
      - Projects
    properties:
      - type: OpenAPI
        url: openapi/figma-projects-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-projects-get-project-files-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-projects-project-file-schema.json
      - type: JSONSchema
        url: json-schema/figma-projects-bad-request-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-projects-error-response-payload-with-err-schema.json
      - type: JSONSchema
        url: json-schema/figma-projects-error-response-payload-with-message-schema.json
      - type: JSONSchema
        url: json-schema/figma-projects-forbidden-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-projects-internal-server-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-projects-too-many-requests-error-schema.json
      - type: JSONLD
        url: json-ld/figma-projects-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/projects-types/
  - aid: figma:figma-me-api
    name: Figma Me API
    description: Figma Me API provides the endpoint for retrieving information about the currently authenticated user.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/users-endpoints/
    tags:
      - Authentication
      - Users
    properties:
      - type: OpenAPI
        url: openapi/figma-me-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-me-user-schema.json
      - type: JSONSchema
        url: json-schema/figma-me-user-with-email-schema.json
      - type: JSONSchema
        url: json-schema/figma-me-error-response-payload-schema.json
      - type: JSONSchema
        url: json-schema/figma-me-forbidden-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-me-internal-server-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-me-too-many-requests-error-schema.json
      - type: JSONLD
        url: json-ld/figma-me-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/users-endpoints/
  - aid: figma:figma-components-api
    name: Figma Components API
    description: Figma Components API provides access to published components, component sets, and styles from team libraries. Query component metadata, retrieve thumbnails, and access documentation links for reusable design elements.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/component-types/
    tags:
      - Components
      - Design Systems
      - Libraries
    properties:
      - type: OpenAPI
        url: openapi/figma-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-component-schema.json
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/component-types/
  - aid: figma:figma-component-sets-api
    name: Figma Component Sets API
    description: Figma Component Sets API provides endpoints for retrieving published component set metadata from team libraries.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/component-types/
    tags:
      - Component Sets
      - Design Systems
    properties:
      - type: OpenAPI
        url: openapi/figma-component-sets-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-component-sets-get-component-set-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-component-sets-published-component-set-schema.json
      - type: JSONSchema
        url: json-schema/figma-component-sets-frame-info-schema.json
      - type: JSONSchema
        url: json-schema/figma-component-sets-user-schema.json
      - type: JSONSchema
        url: json-schema/figma-component-sets-error-response-payload-with-err-schema.json
      - type: JSONSchema
        url: json-schema/figma-component-sets-error-response-payload-with-error-schema.json
      - type: JSONLD
        url: json-ld/figma-component-sets-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/component-types/
  - aid: figma:figma-styles-api
    name: Figma Styles API
    description: Figma Styles API provides endpoints for retrieving published style metadata including colors, text styles, and effects from team libraries.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/component-types/
    tags:
      - Design Systems
      - Styles
    properties:
      - type: OpenAPI
        url: openapi/figma-styles-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-styles-get-style-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-styles-published-style-schema.json
      - type: JSONSchema
        url: json-schema/figma-styles-style-type-schema.json
      - type: JSONSchema
        url: json-schema/figma-styles-user-schema.json
      - type: JSONSchema
        url: json-schema/figma-styles-bad-request-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-styles-error-response-payload-with-err-schema.json
      - type: JSONSchema
        url: json-schema/figma-styles-error-response-payload-with-message-schema.json
      - type: JSONSchema
        url: json-schema/figma-styles-forbidden-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-styles-internal-server-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-styles-not-found-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-styles-too-many-requests-error-schema.json
      - type: JSONLD
        url: json-ld/figma-styles-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/component-types/
  - aid: figma:figma-activity-logs-api
    name: Figma Activity Logs API
    description: Figma Activity Logs API provides endpoints for retrieving activity log events for an organization, enabling audit trail and compliance monitoring.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/activity-logs/
    tags:
      - Activity Logs
      - Audit
      - Compliance
    properties:
      - type: OpenAPI
        url: openapi/figma-activity-logs-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-activity-logs-get-activity-logs-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-activity-logs-activity-log-schema.json
      - type: JSONSchema
        url: json-schema/figma-activity-logs-activity-log-action-schema.json
      - type: JSONSchema
        url: json-schema/figma-activity-logs-activity-log-actor-schema.json
      - type: JSONSchema
        url: json-schema/figma-activity-logs-activity-log-context-schema.json
      - type: JSONSchema
        url: json-schema/figma-activity-logs-activity-log-entity-schema.json
      - type: JSONSchema
        url: json-schema/figma-activity-logs-activity-log-file-entity-schema.json
      - type: JSONSchema
        url: json-schema/figma-activity-logs-activity-log-org-entity-schema.json
      - type: JSONSchema
        url: json-schema/figma-activity-logs-activity-log-project-entity-schema.json
      - type: JSONSchema
        url: json-schema/figma-activity-logs-activity-log-team-entity-schema.json
      - type: JSONSchema
        url: json-schema/figma-activity-logs-activity-log-user-entity-schema.json
      - type: JSONSchema
        url: json-schema/figma-activity-logs-activity-logs-meta-schema.json
      - type: JSONSchema
        url: json-schema/figma-activity-logs-error-response-payload-schema.json
      - type: JSONLD
        url: json-ld/figma-activity-logs-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/activity-logs/
  - aid: figma:figma-payments-api
    name: Figma Payments API
    description: Figma Payments API provides endpoints for querying user payment information on plugins, widgets, and Community files.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/plugins/api/figma-payments/
    tags:
      - Monetization
      - Payments
      - Plugins
    properties:
      - type: OpenAPI
        url: openapi/figma-payments-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-payments-get-payments-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-payments-payment-information-schema.json
      - type: JSONSchema
        url: json-schema/figma-payments-payment-status-schema.json
      - type: JSONSchema
        url: json-schema/figma-payments-error-response-payload-schema.json
      - type: JSONSchema
        url: json-schema/figma-payments-internal-server-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-payments-too-many-requests-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-payments-unauthorized-error-schema.json
      - type: JSONLD
        url: json-ld/figma-payments-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/plugins/api/figma-payments/
  - aid: figma:figma-dev-resources-api
    name: Figma Dev Resources API
    description: Figma Dev Resources API provides endpoints for creating, updating, and deleting dev resources attached to design nodes, enabling design-to-code workflows.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/dev-resources/
    tags:
      - Design to Code
      - Dev Resources
      - Development
    properties:
      - type: OpenAPI
        url: openapi/figma-dev-resources-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-dev-resources-create-dev-resource-item-schema.json
      - type: JSONSchema
        url: json-schema/figma-dev-resources-create-dev-resources-request-schema.json
      - type: JSONSchema
        url: json-schema/figma-dev-resources-dev-resource-schema.json
      - type: JSONSchema
        url: json-schema/figma-dev-resources-dev-resource-create-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-dev-resources-dev-resource-update-error-schema.json
      - type: JSONSchema
        url: json-schema/figma-dev-resources-error-response-payload-schema.json
      - type: JSONSchema
        url: json-schema/figma-dev-resources-post-dev-resources-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-dev-resources-put-dev-resources-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-dev-resources-update-dev-resource-item-schema.json
      - type: JSONSchema
        url: json-schema/figma-dev-resources-update-dev-resources-request-schema.json
      - type: JSONLD
        url: json-ld/figma-dev-resources-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/dev-resources/
  - aid: figma:figma-analytics-api
    name: Figma Analytics API
    description: Figma Analytics API provides endpoints for tracking component, style, and variable usage across team libraries, enabling design system adoption measurement.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/library-analytics-intro/
    tags:
      - Analytics
      - Design Systems
      - Libraries
    properties:
      - type: OpenAPI
        url: openapi/figma-analytics-api-openapi.yml
      - type: JSONSchema
        url: json-schema/figma-analytics-get-library-analytics-usages-response-body-schema.json
      - type: JSONSchema
        url: json-schema/figma-analytics-library-analytics-usages-by-component-schema.json
      - type: JSONSchema
        url: json-schema/figma-analytics-library-analytics-usages-by-file-schema.json
      - type: JSONSchema
        url: json-schema/figma-analytics-library-analytics-actions-by-component-schema.json
      - type: JSONSchema
        url: json-schema/figma-analytics-library-analytics-actions-by-team-schema.json
      - type: JSONSchema
        url: json-schema/figma-analytics-library-analytics-style-usages-by-asset-schema.json
      - type: JSONSchema
        url: json-schema/figma-analytics-library-analytics-style-usages-by-file-schema.json
      - type: JSONSchema
        url: json-schema/figma-analytics-library-analytics-variable-usages-by-asset-schema.json
      - type: JSONSchema
        url: json-schema/figma-analytics-library-analytics-variable-usages-by-file-schema.json
      - type: JSONSchema
        url: json-schema/figma-analytics-error-response-payload-schema.json
      - type: JSONLD
        url: json-ld/figma-analytics-context.jsonld
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/library-analytics-intro/
  - aid: figma:figma-comments-api
    name: Figma Comments API
    description: Figma Commenting mode allows users to leave comments directly on layers or objects on the canvas. You can use the Figma API to post comments and reactions to a Figma file, view existing comments and reactions, and access information about a comment including when it was made, by whom, and its exact location on the canvas.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/comments-endpoints/
    tags:
      - Annotations
      - Collaboration
      - Comments
      - Reactions
    properties:
      - type: OpenAPI
        url: openapi/figma-rest-api-openapi.yml
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/comments-endpoints/
  - aid: figma:figma-version-history-api
    name: Figma Version History API
    description: Figma allows you to distinguish different stages or versions of a file as it evolves over time. The Version History API provides endpoints to view, track, and restore previous versions of a file, recorded in the version history.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/version-history-endpoints/
    tags:
      - Files
      - History
      - Versions
    properties:
      - type: OpenAPI
        url: openapi/figma-rest-api-openapi.yml
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/version-history-endpoints/
  - aid: figma:figma-variables-api
    name: Figma Variables API
    description: The Variables REST API includes endpoints for querying, creating, updating, and deleting variables. Variables store reusable values that can be applied to design properties and prototyping actions. To use this API, you must have a Full seat in an Enterprise org.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/variables-endpoints/
    tags:
      - Collections
      - Design Tokens
      - Variables
    properties:
      - type: OpenAPI
        url: openapi/figma-rest-api-openapi.yml
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/variables-endpoints/
  - aid: figma:figma-library-analytics-api
    name: Figma Library Analytics API
    description: The Library Analytics REST API provides six methods for tracking component, style, and variable usage. Each resource type has an actions endpoint and a usages endpoint, allowing you to get time series data about user actions and usage data for your library assets.
    image: https://www.figma.com/favicon.ico
    baseURL: https://api.figma.com
    humanURL: https://developers.figma.com/docs/rest-api/library-analytics-endpoints/
    tags:
      - Analytics
      - Components
      - Libraries
      - Styles
      - Usages
      - Variables
    properties:
      - type: OpenAPI
        url: openapi/figma-rest-api-openapi.yml
      - type: Documentation
        url: https://developers.figma.com/docs/rest-api/library-analytics-endpoints/
common:
  - type: Portal
    url: https://www.figma.com/developers
  - type: Authentication
    url: https://developers.figma.com/docs/rest-api/authentication/
  - type: ChangeLog
    url: https://developers.figma.com/docs/rest-api/changelog/
  - type: RateLimits
    url: https://developers.figma.com/docs/rest-api/rate-limits/
  - type: OpenAPI
    url: https://github.com/figma/rest-api-spec
    title: Figma REST API OpenAPI Specification
  - type: GettingStarted
    url: https://developers.figma.com/docs/code-connect/quickstart-guide/
  - type: SignUp
    url: https://www.figma.com/signup?cont=/developers/embed
  - type: Login
    url: https://www.figma.com/login?cont=/developers/embed
  - type: Pricing
    url: https://www.figma.com/pricing/
  - type: Blog
    url: https://www.figma.com/blog/
  - type: Security
    url: https://www.figma.com/security/
  - type: StatusPage
    url: https://status.figma.com/
  - type: TermsOfService
    url: https://www.figma.com/legal/tos/
  - type: PrivacyPolicy
    url: https://www.figma.com/legal/privacy/
  - type: Partners
    url: https://www.figma.com/partners/
  - type: Events
    url: https://www.figma.com/events/
  - type: Support
    url: https://help.figma.com/hc/en-us/
  - type: Contact
    url: https://www.figma.com/contact/
  - type: Support
    url: https://forum.figma.com/
    title: Forum
  - type: GitHubOrganization
    url: https://github.com/figma
  - type: GitHubRepository
    url: https://github.com/figma/rest-api-spec
    title: REST API OpenAPI Specification
  - type: GitHubRepository
    url: https://github.com/figma/code-connect
    title: Code Connect
  - type: GitHubRepository
    url: https://github.com/figma/plugin-typings
    title: Plugin API Typings
  - type: GitHubRepository
    url: https://github.com/figma/community-resources
    title: Community Resources
  - type: GitHubRepository
    url: https://github.com/figma/mcp-server-guide
    title: MCP Server Guide
  - type: SpectralRules
    url: rules/figma-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/figma-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/rest-api.yaml
    title: REST API Shared Definition
  - type: NaftikoCapability
    url: capabilities/design-system-management.yaml
    title: Design System Management Workflow
  - type: Features
    data:
      - Starter free with unlimited drafts and 150-500 AI credits/mo
      - Professional at $16/full-seat/mo with team libraries and MCP Server
      - Organization at $55/full-seat/mo with shared libraries and centralized admin
      - Enterprise at $90/full-seat/mo with design system APIs and SCIM
      - REST API for files, projects, components, comments
      - Plugin API for in-editor extensions
      - Widget API for FigJam interactive widgets
      - Variables API for design token management
      - Webhooks v2 for file and library updates
      - OAuth 2.0 with granular scopes
      - Personal access tokens for scripts/automation
      - Dev Mode for handoff and code generation
      - Dev Mode MCP Server for AI design integration
      - FigJam whiteboarding included
      - Variables and modes for design system theming (Enterprise)
      - Branching and merging on Organization+
    sources:
      - https://www.figma.com/pricing/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Design System Management
        description: Build, publish, and track adoption of shared component libraries across product teams.
      - name: Automated Asset Export
        description: Programmatically export design assets for build pipelines and content delivery workflows.
      - name: Design-to-Code Handoff
        description: Attach code references to design nodes using dev resources for seamless developer handoff.
      - name: Plugin and Widget Development
        description: Extend Figma with custom plugins and widgets using the Plugin API and Widget API.
      - name: Compliance and Audit
        description: Monitor organization activity logs for security compliance and access auditing.
      - name: Design File Backup
        description: Programmatically back up file data and version history for disaster recovery.
  - type: Integrations
    data:
      - name: Slack
        description: Receive Figma file update notifications and preview designs directly in Slack channels.
      - name: Jira
        description: Embed Figma designs in Jira issues and link design tasks to development tickets.
      - name: GitHub
        description: Link Figma designs to pull requests and track design-to-code implementation.
      - name: Storybook
        description: Connect Figma components to Storybook stories using Code Connect for design-code parity.
      - name: Zeplin
        description: Export designs from Figma to Zeplin for detailed developer handoff and style guides.
      - name: Abstract
        description: Version control and branching for Figma design files with Abstract integration.
      - name: Microsoft Teams
        description: Share and preview Figma designs within Microsoft Teams conversations and channels.
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
  - name: Figma
    email: support@figma.com
    url: https://www.figma.com
---
