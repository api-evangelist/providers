---
aid: hubspot
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/hubspot.yml
apis:
  - aid: hubspot:hubspot-domains-api
    name: HubSpot Domains API
    tags:
      - Domains
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/overview
    overlays:
      - url: |-

          overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/domains-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/domains
        type: Documentation
      - url: openapi/hubspot-domains-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/domains-api-domain-collection-response-schema.json
      - type: JSONSchema
        url: json-schema/domains-api-domain-schema.json
      - type: JSONSchema
        url: json-schema/domains-api-forward-paging-schema.json
      - type: JSONSchema
        url: json-schema/domains-api-next-page-schema.json
      - type: JSONSchema
        url: json-structure/domains-api-domain-collection-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/domains-api-domain-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/domains-api-forward-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/domains-api-next-page-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/domains-api-domain-collection-response-example.json
      - type: CodeExamples
        url: examples/domains-api-domain-example.json
      - type: CodeExamples
        url: examples/domains-api-forward-paging-example.json
      - type: CodeExamples
        url: examples/domains-api-next-page-example.json
    description: These endpoints allow you to return information about the domains connected to a particular HubSpot CMS site. You can return data for a list of domains or specify a domain by ID.
  - aid: hubspot:hubspot-source-code-api
    name: HubSpot Source Code API
    tags:
      - Async
      - Code
      - Content
      - Environments
      - Extract
      - Path
      - Sources
      - Status
      - Task
      - Validate
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/cms/source-code
    overlays:
      - url: |-

          overlays/https://api.hubspot.com/public/api/spec/v1/specs/cms/v3/source-code-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/source-code
        type: Documentation
      - url: openapi/hubspot-source-code-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/source-code-api-action-response-schema.json
      - type: JSONSchema
        url: json-schema/source-code-api-asset-file-metadata-schema.json
      - type: JSONSchema
        url: json-schema/source-code-api-file-extract-request-schema.json
      - type: JSONSchema
        url: json-schema/source-code-api-file-upload-request-schema.json
      - type: JSONSchema
        url: json-schema/source-code-api-task-locator-schema.json
      - type: JSONSchema
        url: json-schema/source-code-api-validation-error-schema.json
      - type: JSONSchema
        url: json-schema/source-code-api-validation-result-schema.json
      - type: JSONSchema
        url: json-schema/source-code-api-validation-warning-schema.json
      - type: JSONSchema
        url: json-structure/source-code-api-action-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/source-code-api-asset-file-metadata-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/source-code-api-file-extract-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/source-code-api-file-upload-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/source-code-api-task-locator-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/source-code-api-validation-error-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/source-code-api-validation-result-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/source-code-api-validation-warning-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/source-code-api-action-response-example.json
      - type: CodeExamples
        url: examples/source-code-api-asset-file-metadata-example.json
      - type: CodeExamples
        url: examples/source-code-api-file-extract-request-example.json
      - type: CodeExamples
        url: examples/source-code-api-file-upload-request-example.json
      - type: CodeExamples
        url: examples/source-code-api-task-locator-example.json
      - type: CodeExamples
        url: examples/source-code-api-validation-error-example.json
      - type: CodeExamples
        url: examples/source-code-api-validation-result-example.json
      - type: CodeExamples
        url: examples/source-code-api-validation-warning-example.json
    description: Endpoints for interacting with files in the CMS Developer File System. These files include HTML templates, CSS, JS, modules, and other assets which are used to create CMS content.
  - aid: hubspot:hubspot-posts-api
    name: HubSpot Posts API
    tags:
      - Archive
      - Attach
      - Batch
      - Blog  Posts
      - Blogs
      - Clone
      - Detach
      - Draft
      - Groups
      - Language
      - Live
      - Multi
      - Objects
      - Posts
      - Primary
      - Read
      - Reset
      - Restore
      - Revisions
      - Schedules
      - Set
      - Variations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/cms/blog-post
    overlays:
      - url: |-

          overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/blogs/blog-posts-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/blog-post
        type: Documentation
      - url: openapi/hubspot-blog-posts-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/blog-posts-api-attach-to-language-group-request-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-batch-input-item-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-batch-input-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-batch-response-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-batch-response-with-errors-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-blog-post-collection-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-blog-post-input-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-blog-post-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-clone-request-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-create-language-variation-request-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-detach-from-language-group-request-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-paging-next-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-paging-previous-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-push-live-request-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-reset-draft-request-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-restore-previous-version-request-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-schedule-request-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-set-language-primary-request-schema.json
      - type: JSONSchema
        url: json-schema/blog-posts-api-version-history-schema.json
      - type: JSONSchema
        url: json-structure/blog-posts-api-attach-to-language-group-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-batch-input-item-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-batch-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-batch-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-batch-response-with-errors-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-blog-post-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-blog-post-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-blog-post-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-clone-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-create-language-variation-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-detach-from-language-group-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-paging-next-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-paging-previous-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-push-live-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-reset-draft-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-restore-previous-version-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-schedule-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-set-language-primary-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/blog-posts-api-version-history-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/blog-posts-api-attach-to-language-group-request-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-batch-input-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-batch-input-item-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-batch-response-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-batch-response-with-errors-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-blog-post-collection-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-blog-post-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-blog-post-input-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-clone-request-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-create-language-variation-request-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-detach-from-language-group-request-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-paging-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-paging-next-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-paging-previous-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-push-live-request-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-reset-draft-request-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-restore-previous-version-request-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-schedule-request-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-set-language-primary-request-example.json
      - type: CodeExamples
        url: examples/blog-posts-api-version-history-example.json
    description: Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags.
  - aid: hubspot:hubspot-authors-api
    name: HubSpot Authors API
    tags:
      - Archive
      - Attach
      - Authors
      - Batch
      - Blogs
      - Detach
      - Groups
      - Language
      - Languages
      - Multi
      - Objects
      - Primary
      - Read
      - Set
      - Variations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/cms/blog-authors
    overlays:
      - url: |-

          overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/blogs/authors-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/blog-authors
        type: Documentation
      - url: openapi/hubspot-authors-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/authors-api-attach-to-language-group-request-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-batch-archive-input-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-batch-create-input-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-batch-input-item-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-batch-input-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-batch-read-input-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-batch-response-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-batch-response-with-errors-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-blog-author-collection-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-blog-author-input-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-blog-author-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-create-language-variation-request-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-detach-from-language-group-request-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-paging-next-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/authors-api-set-language-primary-request-schema.json
      - type: JSONSchema
        url: json-structure/authors-api-attach-to-language-group-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-batch-archive-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-batch-create-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-batch-input-item-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-batch-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-batch-read-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-batch-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-batch-response-with-errors-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-blog-author-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-blog-author-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-blog-author-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-create-language-variation-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-detach-from-language-group-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-paging-next-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/authors-api-set-language-primary-request-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/authors-api-attach-to-language-group-request-example.json
      - type: CodeExamples
        url: examples/authors-api-batch-archive-input-example.json
      - type: CodeExamples
        url: examples/authors-api-batch-create-input-example.json
      - type: CodeExamples
        url: examples/authors-api-batch-input-example.json
      - type: CodeExamples
        url: examples/authors-api-batch-input-item-example.json
      - type: CodeExamples
        url: examples/authors-api-batch-read-input-example.json
      - type: CodeExamples
        url: examples/authors-api-batch-response-example.json
      - type: CodeExamples
        url: examples/authors-api-batch-response-with-errors-example.json
      - type: CodeExamples
        url: examples/authors-api-blog-author-collection-example.json
      - type: CodeExamples
        url: examples/authors-api-blog-author-example.json
      - type: CodeExamples
        url: examples/authors-api-blog-author-input-example.json
      - type: CodeExamples
        url: examples/authors-api-create-language-variation-request-example.json
      - type: CodeExamples
        url: examples/authors-api-detach-from-language-group-request-example.json
      - type: CodeExamples
        url: examples/authors-api-paging-example.json
      - type: CodeExamples
        url: examples/authors-api-paging-next-example.json
      - type: CodeExamples
        url: examples/authors-api-set-language-primary-request-example.json
    description: Use the blog authors API to manage author information for your blog posts.
  - aid: hubspot:hubspot-url-redirects-api
    name: HubSpot URL Redirects API
    tags:
      - Redirects
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.hubspot.com/docs/api/cms/url-redirects
    overlays:
      - url: |-

          overlays/https://api.hubspot.com/api-catalog-public/v1/apis/cms/v3/url-redirects-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/url-redirects
        type: Documentation
    description: URL redirects allow you to redirect traffic from a HubSpot-hosted page or blog post to any URL. You can also update URL redirects in bulk and use a flexible pattern redirect to dynamically update the structure of URLs.
  - aid: hubspot:hubspot-cms-hubdb-api
    name: HubSpot CMS HubDB API
    tags:
      - CMS
      - Content
      - Data Tables
      - HubDB
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api-reference/cms-hubdb-v3/guide
    properties:
      - url: https://developers.hubspot.com/docs/api-reference/cms-hubdb-v3/guide
        type: Documentation
      - url: openapi/hubspot-cms-hubdb-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/cms-hubdb-api-collection-response-hub-dbrow-schema.json
      - type: JSONSchema
        url: json-schema/cms-hubdb-api-collection-response-hub-dbtable-schema.json
      - type: JSONSchema
        url: json-schema/cms-hubdb-api-hub-dbcolumn-schema.json
      - type: JSONSchema
        url: json-schema/cms-hubdb-api-hub-dbrow-create-request-schema.json
      - type: JSONSchema
        url: json-schema/cms-hubdb-api-hub-dbrow-schema.json
      - type: JSONSchema
        url: json-schema/cms-hubdb-api-hub-dbtable-create-request-schema.json
      - type: JSONSchema
        url: json-schema/cms-hubdb-api-hub-dbtable-schema.json
      - type: JSONSchema
        url: json-schema/cms-hubdb-api-paging-schema.json
      - type: JSONSchema
        url: json-structure/cms-hubdb-api-collection-response-hub-dbrow-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/cms-hubdb-api-collection-response-hub-dbtable-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/cms-hubdb-api-hub-dbcolumn-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/cms-hubdb-api-hub-dbrow-create-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/cms-hubdb-api-hub-dbrow-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/cms-hubdb-api-hub-dbtable-create-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/cms-hubdb-api-hub-dbtable-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/cms-hubdb-api-paging-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/cms-hubdb-api-collection-response-hub-dbrow-example.json
      - type: CodeExamples
        url: examples/cms-hubdb-api-collection-response-hub-dbtable-example.json
      - type: CodeExamples
        url: examples/cms-hubdb-api-hub-dbcolumn-example.json
      - type: CodeExamples
        url: examples/cms-hubdb-api-hub-dbrow-create-request-example.json
      - type: CodeExamples
        url: examples/cms-hubdb-api-hub-dbrow-example.json
      - type: CodeExamples
        url: examples/cms-hubdb-api-hub-dbtable-create-request-example.json
      - type: CodeExamples
        url: examples/cms-hubdb-api-hub-dbtable-example.json
      - type: CodeExamples
        url: examples/cms-hubdb-api-paging-example.json
    description: The HubDB API allows you to create, update, and delete HubDB data tables and their rows. HubDB tables can be used as data sources for dynamic CMS pages and are available in both draft and published versions.
  - aid: hubspot:hubspot-cms-pages-api
    name: HubSpot CMS Pages API
    tags:
      - CMS
      - Landing Pages
      - Pages
      - Site Pages
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/cms/pages
    properties:
      - url: https://developers.hubspot.com/docs/api/cms/pages
        type: Documentation
      - url: openapi/hubspot-cms-pages-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/cms-pages-api-collection-response-page-schema.json
      - type: JSONSchema
        url: json-schema/cms-pages-api-page-create-request-schema.json
      - type: JSONSchema
        url: json-schema/cms-pages-api-page-schema.json
      - type: JSONSchema
        url: json-schema/cms-pages-api-page-update-request-schema.json
      - type: JSONSchema
        url: json-schema/cms-pages-api-paging-schema.json
      - type: JSONSchema
        url: json-structure/cms-pages-api-collection-response-page-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/cms-pages-api-page-create-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/cms-pages-api-page-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/cms-pages-api-page-update-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/cms-pages-api-paging-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/cms-pages-api-collection-response-page-example.json
      - type: CodeExamples
        url: examples/cms-pages-api-page-create-request-example.json
      - type: CodeExamples
        url: examples/cms-pages-api-page-example.json
      - type: CodeExamples
        url: examples/cms-pages-api-page-update-request-example.json
      - type: CodeExamples
        url: examples/cms-pages-api-paging-example.json
    description: The CMS Pages API provides endpoints for creating and managing site pages and landing pages hosted on HubSpot. You can create, retrieve, update, publish, and delete both site pages and landing pages programmatically.
  - aid: hubspot:hubspot-contacts-api
    name: HubSpot Contacts API
    tags:
      - Contacts
      - CRM
      - Records
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/contacts
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/contacts
        type: Documentation
      - url: openapi/hubspot-crm-contacts-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/crm-contacts-api-association-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-batch-archive-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-batch-create-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-batch-read-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-batch-response-contact-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-batch-update-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-collection-response-association-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-collection-response-contact-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-contact-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-filter-group-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-filter-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-search-request-schema.json
      - type: JSONSchema
        url: json-schema/crm-contacts-api-simple-public-object-input-schema.json
      - type: JSONSchema
        url: json-structure/crm-contacts-api-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-batch-archive-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-batch-create-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-batch-read-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-batch-response-contact-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-batch-update-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-collection-response-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-collection-response-contact-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-contact-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-filter-group-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-filter-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-search-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-contacts-api-simple-public-object-input-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/crm-contacts-api-association-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-batch-archive-input-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-batch-create-input-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-batch-read-input-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-batch-response-contact-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-batch-update-input-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-collection-response-association-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-collection-response-contact-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-contact-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-filter-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-filter-group-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-paging-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-search-request-example.json
      - type: CodeExamples
        url: examples/crm-contacts-api-simple-public-object-input-example.json
    description: Contact records store information about individuals. The contacts endpoints allow you to manage contact data and sync it between HubSpot and other systems. You can create, retrieve, update, and delete contacts, as well as manage associations between contacts and other CRM objects.
  - aid: hubspot:hubspot-companies-api
    name: HubSpot Companies API
    tags:
      - Companies
      - CRM
      - Records
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/companies
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/companies
        type: Documentation
      - url: openapi/hubspot-crm-companies-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/crm-companies-api-association-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-batch-archive-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-batch-create-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-batch-read-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-batch-response-company-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-batch-update-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-collection-response-association-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-collection-response-company-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-company-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-filter-group-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-filter-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-search-request-schema.json
      - type: JSONSchema
        url: json-schema/crm-companies-api-simple-public-object-input-schema.json
      - type: JSONSchema
        url: json-structure/crm-companies-api-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-batch-archive-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-batch-create-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-batch-read-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-batch-response-company-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-batch-update-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-collection-response-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-collection-response-company-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-company-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-filter-group-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-filter-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-search-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-companies-api-simple-public-object-input-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/crm-companies-api-association-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-batch-archive-input-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-batch-create-input-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-batch-read-input-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-batch-response-company-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-batch-update-input-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-collection-response-association-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-collection-response-company-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-company-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-filter-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-filter-group-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-paging-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-search-request-example.json
      - type: CodeExamples
        url: examples/crm-companies-api-simple-public-object-input-example.json
    description: Company records store data about businesses and organizations. The companies endpoints allow you to manage this data and sync it between HubSpot and other systems, including creating, retrieving, updating, and deleting company records and managing their associations.
  - aid: hubspot:hubspot-deals-api
    name: HubSpot Deals API
    tags:
      - CRM
      - Deals
      - Pipeline
      - Sales
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/deals
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/deals
        type: Documentation
      - url: openapi/hubspot-crm-deals-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/crm-deals-api-association-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-batch-archive-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-batch-create-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-batch-read-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-batch-response-deal-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-batch-update-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-collection-response-association-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-collection-response-deal-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-deal-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-filter-group-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-filter-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-search-request-schema.json
      - type: JSONSchema
        url: json-schema/crm-deals-api-simple-public-object-input-schema.json
      - type: JSONSchema
        url: json-structure/crm-deals-api-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-batch-archive-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-batch-create-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-batch-read-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-batch-response-deal-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-batch-update-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-collection-response-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-collection-response-deal-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-deal-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-filter-group-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-filter-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-search-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-deals-api-simple-public-object-input-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/crm-deals-api-association-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-batch-archive-input-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-batch-create-input-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-batch-read-input-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-batch-response-deal-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-batch-update-input-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-collection-response-association-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-collection-response-deal-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-deal-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-filter-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-filter-group-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-paging-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-search-request-example.json
      - type: CodeExamples
        url: examples/crm-deals-api-simple-public-object-input-example.json
    description: A deal stores data about an ongoing transaction or sales opportunity. The deals endpoints allow you to manage deal records and sync data between HubSpot and other systems, supporting the full lifecycle of sales opportunities through pipeline stages.
  - aid: hubspot:hubspot-tickets-api
    name: HubSpot Tickets API
    tags:
      - CRM
      - Customer Service
      - Support
      - Tickets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/tickets
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/tickets
        type: Documentation
      - url: openapi/hubspot-crm-tickets-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/crm-tickets-api-association-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-batch-archive-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-batch-create-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-batch-read-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-batch-response-ticket-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-batch-update-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-collection-response-association-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-collection-response-ticket-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-filter-group-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-filter-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-search-request-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-simple-public-object-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-tickets-api-ticket-schema.json
      - type: JSONSchema
        url: json-structure/crm-tickets-api-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-batch-archive-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-batch-create-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-batch-read-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-batch-response-ticket-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-batch-update-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-collection-response-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-collection-response-ticket-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-filter-group-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-filter-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-search-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-simple-public-object-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-tickets-api-ticket-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/crm-tickets-api-association-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-batch-archive-input-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-batch-create-input-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-batch-read-input-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-batch-response-ticket-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-batch-update-input-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-collection-response-association-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-collection-response-ticket-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-filter-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-filter-group-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-paging-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-search-request-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-simple-public-object-input-example.json
      - type: CodeExamples
        url: examples/crm-tickets-api-ticket-example.json
    description: Tickets represent customer requests for help and are tracked through support pipelines until resolved. The tickets endpoints allow you to create, manage, and retrieve customer support ticket records and associate them with contacts, companies, and other CRM objects.
  - aid: hubspot:hubspot-pipelines-api
    name: HubSpot Pipelines API
    tags:
      - CRM
      - Pipelines
      - Sales
      - Stages
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/pipelines
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/pipelines
        type: Documentation
    description: Pipelines allow you to track records through defined stages in a process, such as sales deals or support tickets. The pipelines endpoints allow you to create, retrieve, update, and delete pipelines and pipeline stages for deals, tickets, and other object types.
  - aid: hubspot:hubspot-products-api
    name: HubSpot Products API
    tags:
      - Catalog
      - Commerce
      - CRM
      - Products
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/products
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/products
        type: Documentation
    description: Products represent the goods or services you sell in HubSpot. The products endpoints allow you to manage a product library which can be used to quickly add products to deals, generate quotes, and report on product performance.
  - aid: hubspot:hubspot-line-items-api
    name: HubSpot Line Items API
    tags:
      - Commerce
      - CRM
      - Line Items
      - Products
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/line-items
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/line-items
        type: Documentation
    description: Line items are individual instances of products that are attached to a deal or quote. The line items endpoints allow you to create, retrieve, update, and delete line item records, enabling detailed product-level tracking on deals and quotes.
  - aid: hubspot:hubspot-quotes-api
    name: HubSpot Quotes API
    tags:
      - Commerce
      - CRM
      - Quotes
      - Sales
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/quotes
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/quotes
        type: Documentation
    description: Quotes allow you to share pricing information with prospects and customers. The quotes endpoints allow you to create and manage quotes with associated line items, deals, and contacts, and support features like e-signatures and payment collection.
  - aid: hubspot:hubspot-crm-properties-api
    name: HubSpot CRM Properties API
    tags:
      - CRM
      - Custom Fields
      - Properties
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/properties
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/properties
        type: Documentation
    description: The CRM properties endpoints allow you to manage custom properties and view default property details for any CRM object type. You can create, retrieve, update, and delete properties for contacts, companies, deals, tickets, and custom objects.
  - aid: hubspot:hubspot-crm-associations-api
    name: HubSpot CRM Associations API
    tags:
      - Associations
      - CRM
      - Relationships
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/associations
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/associations
        type: Documentation
      - url: openapi/hubspot-crm-associations-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/crm-associations-api-association-definition-collection-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-association-definition-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-association-label-collection-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-association-label-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-association-result-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-association-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-association-type-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-association-type-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-batch-association-archive-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-batch-association-archive-item-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-batch-association-create-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-batch-association-create-item-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-batch-association-read-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-batch-association-response-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-create-association-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-create-label-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-object-reference-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-paging-next-schema.json
      - type: JSONSchema
        url: json-schema/crm-associations-api-paging-schema.json
      - type: JSONSchema
        url: json-structure/crm-associations-api-association-definition-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-association-definition-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-association-label-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-association-label-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-association-result-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-association-type-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-association-type-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-batch-association-archive-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-batch-association-archive-item-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-batch-association-create-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-batch-association-create-item-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-batch-association-read-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-batch-association-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-create-association-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-create-label-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-object-reference-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-paging-next-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-associations-api-paging-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/crm-associations-api-association-definition-collection-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-association-definition-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-association-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-association-label-collection-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-association-label-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-association-result-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-association-type-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-association-type-input-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-batch-association-archive-input-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-batch-association-archive-item-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-batch-association-create-input-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-batch-association-create-item-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-batch-association-read-input-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-batch-association-response-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-create-association-input-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-create-label-input-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-object-reference-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-paging-example.json
      - type: CodeExamples
        url: examples/crm-associations-api-paging-next-example.json
    description: The associations endpoints allow you to manage relationships between CRM object records such as contacts, companies, deals, and tickets. You can create, retrieve, and delete associations with or without descriptive labels to represent different types of relationships.
  - aid: hubspot:hubspot-owners-api
    name: HubSpot Owners API
    tags:
      - CRM
      - Owners
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/owners
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/owners
        type: Documentation
    description: The owners endpoints are used to retrieve the list of available owners for a HubSpot account. HubSpot uses owners to assign CRM object records to specific users, and owner IDs are used when setting record ownership through other CRM APIs.
  - aid: hubspot:hubspot-crm-imports-api
    name: HubSpot CRM Imports API
    tags:
      - CRM
      - Data
      - Imports
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/imports
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/imports
        type: Documentation
    description: The imports endpoints allow you to import contact, company, deal, and other CRM object data into a HubSpot account in bulk using CSV or Excel files. You can map file columns to HubSpot properties and track import status through the API.
  - aid: hubspot:hubspot-crm-lists-api
    name: HubSpot CRM Lists API
    tags:
      - CRM
      - Lists
      - Segments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/reference/api/crm/lists
    properties:
      - url: https://developers.hubspot.com/docs/reference/api/crm/lists
        type: Documentation
      - url: openapi/hubspot-crm-lists-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/crm-lists-api-collection-response-list-schema.json
      - type: JSONSchema
        url: json-schema/crm-lists-api-collection-response-membership-schema.json
      - type: JSONSchema
        url: json-schema/crm-lists-api-list-create-request-schema.json
      - type: JSONSchema
        url: json-schema/crm-lists-api-list-schema.json
      - type: JSONSchema
        url: json-schema/crm-lists-api-membership-change-request-schema.json
      - type: JSONSchema
        url: json-schema/crm-lists-api-membership-change-response-schema.json
      - type: JSONSchema
        url: json-schema/crm-lists-api-membership-schema.json
      - type: JSONSchema
        url: json-schema/crm-lists-api-paging-schema.json
      - type: JSONSchema
        url: json-structure/crm-lists-api-collection-response-list-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-lists-api-collection-response-membership-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-lists-api-list-create-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-lists-api-list-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-lists-api-membership-change-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-lists-api-membership-change-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-lists-api-membership-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-lists-api-paging-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/crm-lists-api-collection-response-list-example.json
      - type: CodeExamples
        url: examples/crm-lists-api-collection-response-membership-example.json
      - type: CodeExamples
        url: examples/crm-lists-api-list-create-request-example.json
      - type: CodeExamples
        url: examples/crm-lists-api-list-example.json
      - type: CodeExamples
        url: examples/crm-lists-api-membership-change-request-example.json
      - type: CodeExamples
        url: examples/crm-lists-api-membership-change-response-example.json
      - type: CodeExamples
        url: examples/crm-lists-api-membership-example.json
      - type: CodeExamples
        url: examples/crm-lists-api-paging-example.json
    description: The Lists API allows you to create and manage lists of CRM records based on static membership or dynamic filter criteria. Lists can be used to segment contacts, companies, and other CRM objects for marketing and sales operations.
  - aid: hubspot:hubspot-crm-search-api
    name: HubSpot CRM Search API
    tags:
      - CRM
      - Query
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/search
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/search
        type: Documentation
      - url: openapi/hubspot-crm-search-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/crm-search-api-crmobject-schema.json
      - type: JSONSchema
        url: json-schema/crm-search-api-filter-group-schema.json
      - type: JSONSchema
        url: json-schema/crm-search-api-filter-schema.json
      - type: JSONSchema
        url: json-schema/crm-search-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/crm-search-api-search-request-schema.json
      - type: JSONSchema
        url: json-schema/crm-search-api-search-response-schema.json
      - type: JSONSchema
        url: json-schema/crm-search-api-sort-schema.json
      - type: JSONSchema
        url: json-structure/crm-search-api-crmobject-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-search-api-filter-group-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-search-api-filter-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-search-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-search-api-search-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-search-api-search-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-search-api-sort-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/crm-search-api-crmobject-example.json
      - type: CodeExamples
        url: examples/crm-search-api-filter-example.json
      - type: CodeExamples
        url: examples/crm-search-api-filter-group-example.json
      - type: CodeExamples
        url: examples/crm-search-api-paging-example.json
      - type: CodeExamples
        url: examples/crm-search-api-search-request-example.json
      - type: CodeExamples
        url: examples/crm-search-api-search-response-example.json
      - type: CodeExamples
        url: examples/crm-search-api-sort-example.json
    description: The CRM Search API allows you to query and filter CRM objects using a flexible search interface. You can search across contacts, companies, deals, tickets, and other object types using filter groups, sorts, and pagination.
  - aid: hubspot:hubspot-custom-objects-api
    name: HubSpot Custom Objects API
    tags:
      - CRM
      - Custom Objects
      - Schema
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api-reference/crm-custom-objects-v3/guide
    properties:
      - url: https://developers.hubspot.com/docs/api-reference/crm-custom-objects-v3/guide
        type: Documentation
    description: Custom objects allow you to define and create CRM object types that represent data unique to your business. The custom objects API allows you to define schemas, create records, manage properties, and associate custom objects with standard CRM objects like contacts and deals.
  - aid: hubspot:hubspot-commerce-payments-api
    name: HubSpot Commerce Payments API
    tags:
      - Commerce
      - Payments
      - Transactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/commerce/payments
    properties:
      - url: https://developers.hubspot.com/docs/api/commerce/payments
        type: Documentation
      - url: openapi/hubspot-commerce-payments-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/commerce-payments-api-association-input-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-association-result-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-association-type-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-batch-archive-request-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-batch-create-request-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-batch-create-response-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-batch-error-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-batch-read-input-item-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-batch-read-request-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-batch-read-response-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-batch-update-input-item-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-batch-update-request-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-batch-update-response-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-commerce-payment-collection-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-commerce-payment-input-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-commerce-payment-patch-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-commerce-payment-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-filter-group-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-filter-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-property-history-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-search-request-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-search-response-schema.json
      - type: JSONSchema
        url: json-schema/commerce-payments-api-sort-option-schema.json
      - type: JSONSchema
        url: json-structure/commerce-payments-api-association-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-association-result-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-association-type-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-batch-archive-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-batch-create-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-batch-create-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-batch-error-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-batch-read-input-item-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-batch-read-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-batch-read-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-batch-update-input-item-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-batch-update-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-batch-update-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-commerce-payment-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-commerce-payment-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-commerce-payment-patch-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-commerce-payment-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-filter-group-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-filter-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-property-history-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-search-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-search-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-payments-api-sort-option-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/commerce-payments-api-association-input-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-association-result-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-association-type-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-batch-archive-request-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-batch-create-request-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-batch-create-response-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-batch-error-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-batch-read-input-item-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-batch-read-request-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-batch-read-response-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-batch-update-input-item-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-batch-update-request-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-batch-update-response-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-commerce-payment-collection-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-commerce-payment-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-commerce-payment-input-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-commerce-payment-patch-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-filter-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-filter-group-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-paging-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-property-history-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-search-request-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-search-response-example.json
      - type: CodeExamples
        url: examples/commerce-payments-api-sort-option-example.json
    description: The payments endpoints allow you to retrieve data about payment transactions processed through HubSpot Commerce. You can retrieve payment details, manage subscriptions, and access transaction history for commerce operations.
  - aid: hubspot:hubspot-commerce-subscriptions-api
    name: HubSpot Commerce Subscriptions API
    tags:
      - Commerce
      - Recurring Revenue
      - Subscriptions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/commerce/subscriptions
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/commerce/subscriptions
        type: Documentation
      - url: openapi/hubspot-commerce-subscriptions-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-association-schema.json
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-batch-create-input-schema.json
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-batch-read-input-schema.json
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-batch-response-subscription-schema.json
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-batch-update-input-schema.json
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-collection-response-association-schema.json
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-collection-response-subscription-schema.json
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-filter-group-schema.json
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-filter-schema.json
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-search-request-schema.json
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-simple-public-object-input-schema.json
      - type: JSONSchema
        url: json-schema/commerce-subscriptions-api-subscription-schema.json
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-batch-create-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-batch-read-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-batch-response-subscription-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-batch-update-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-collection-response-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-collection-response-subscription-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-filter-group-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-filter-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-search-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-simple-public-object-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/commerce-subscriptions-api-subscription-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-association-example.json
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-batch-create-input-example.json
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-batch-read-input-example.json
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-batch-response-subscription-example.json
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-batch-update-input-example.json
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-collection-response-association-example.json
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-collection-response-subscription-example.json
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-filter-example.json
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-filter-group-example.json
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-paging-example.json
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-search-request-example.json
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-simple-public-object-input-example.json
      - type: CodeExamples
        url: examples/commerce-subscriptions-api-subscription-example.json
    description: The subscriptions API allows you to retrieve data about recurring subscription records in HubSpot Commerce. Subscriptions are created when a customer purchases a recurring product through HubSpot payments or a connected payment processor.
  - aid: hubspot:hubspot-oauth-api
    name: HubSpot OAuth API
    tags:
      - Access Tokens
      - Authentication
      - OAuth
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/oauth/tokens
    properties:
      - url: https://developers.hubspot.com/docs/api/oauth/tokens
        type: Documentation
      - url: openapi/hubspot-oauth-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/oauth-api-access-token-metadata-schema.json
      - type: JSONSchema
        url: json-schema/oauth-api-refresh-token-metadata-schema.json
      - type: JSONSchema
        url: json-schema/oauth-api-token-request-schema.json
      - type: JSONSchema
        url: json-schema/oauth-api-token-response-schema.json
      - type: JSONSchema
        url: json-structure/oauth-api-access-token-metadata-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/oauth-api-refresh-token-metadata-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/oauth-api-token-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/oauth-api-token-response-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/oauth-api-access-token-metadata-example.json
      - type: CodeExamples
        url: examples/oauth-api-refresh-token-metadata-example.json
      - type: CodeExamples
        url: examples/oauth-api-token-request-example.json
      - type: CodeExamples
        url: examples/oauth-api-token-response-example.json
    description: The OAuth API allows you to manage OAuth access tokens for public applications. You can generate, refresh, retrieve metadata for, and delete OAuth tokens to provide secure, scoped API access for HubSpot integrations.
  - aid: hubspot:hubspot-analytics-events-api
    name: HubSpot Analytics Events API
    tags:
      - Analytics
      - Events
      - Tracking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/analytics/events
    properties:
      - url: https://developers.hubspot.com/docs/api/analytics/events
        type: Documentation
      - url: openapi/hubspot-analytics-events-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/analytics-events-api-event-instance-collection-schema.json
      - type: JSONSchema
        url: json-schema/analytics-events-api-event-instance-schema.json
      - type: JSONSchema
        url: json-schema/analytics-events-api-event-type-collection-schema.json
      - type: JSONSchema
        url: json-schema/analytics-events-api-paging-next-schema.json
      - type: JSONSchema
        url: json-schema/analytics-events-api-paging-previous-schema.json
      - type: JSONSchema
        url: json-schema/analytics-events-api-paging-schema.json
      - type: JSONSchema
        url: json-structure/analytics-events-api-event-instance-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/analytics-events-api-event-instance-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/analytics-events-api-event-type-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/analytics-events-api-paging-next-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/analytics-events-api-paging-previous-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/analytics-events-api-paging-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/analytics-events-api-event-instance-collection-example.json
      - type: CodeExamples
        url: examples/analytics-events-api-event-instance-example.json
      - type: CodeExamples
        url: examples/analytics-events-api-event-type-collection-example.json
      - type: CodeExamples
        url: examples/analytics-events-api-paging-example.json
      - type: CodeExamples
        url: examples/analytics-events-api-paging-next-example.json
      - type: CodeExamples
        url: examples/analytics-events-api-paging-previous-example.json
    description: Custom events allow you to track advanced user activity via a JavaScript or HTTP API. The events API enables you to send custom event occurrences, define event schemas, and retrieve historical event data associated with CRM records.
  - aid: hubspot:hubspot-marketing-email-api
    name: HubSpot Marketing Email API
    tags:
      - Campaigns
      - Email
      - Marketing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api-reference/marketing-marketing-emails-v3/guide
    properties:
      - url: https://developers.hubspot.com/docs/api-reference/marketing-marketing-emails-v3/guide
        type: Documentation
      - url: openapi/hubspot-marketing-emal-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/marketing-emal-api-email-message-schema.json
      - type: JSONSchema
        url: json-schema/marketing-emal-api-next-page-schema.json
      - type: JSONSchema
        url: json-schema/marketing-emal-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/marketing-emal-api-smtp-token-collection-response-schema.json
      - type: JSONSchema
        url: json-schema/marketing-emal-api-smtp-token-create-request-schema.json
      - type: JSONSchema
        url: json-schema/marketing-emal-api-smtp-token-schema.json
      - type: JSONSchema
        url: json-schema/marketing-emal-api-smtp-token-with-password-schema.json
      - type: JSONSchema
        url: json-schema/marketing-emal-api-transactional-email-request-schema.json
      - type: JSONSchema
        url: json-schema/marketing-emal-api-transactional-email-response-schema.json
      - type: JSONSchema
        url: json-structure/marketing-emal-api-email-message-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/marketing-emal-api-next-page-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/marketing-emal-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/marketing-emal-api-smtp-token-collection-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/marketing-emal-api-smtp-token-create-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/marketing-emal-api-smtp-token-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/marketing-emal-api-smtp-token-with-password-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/marketing-emal-api-transactional-email-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/marketing-emal-api-transactional-email-response-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/marketing-emal-api-email-message-example.json
      - type: CodeExamples
        url: examples/marketing-emal-api-next-page-example.json
      - type: CodeExamples
        url: examples/marketing-emal-api-paging-example.json
      - type: CodeExamples
        url: examples/marketing-emal-api-smtp-token-collection-response-example.json
      - type: CodeExamples
        url: examples/marketing-emal-api-smtp-token-create-request-example.json
      - type: CodeExamples
        url: examples/marketing-emal-api-smtp-token-example.json
      - type: CodeExamples
        url: examples/marketing-emal-api-smtp-token-with-password-example.json
      - type: CodeExamples
        url: examples/marketing-emal-api-transactional-email-request-example.json
      - type: CodeExamples
        url: examples/marketing-emal-api-transactional-email-response-example.json
    description: The marketing emails API allows you to programmatically create, update, and retrieve details about marketing emails in HubSpot. You can manage email campaigns, retrieve email performance statistics, and automate email content management workflows.
  - aid: hubspot:hubspot-marketing-events-api
    name: HubSpot Marketing Events API
    tags:
      - Events
      - Marketing
      - Webinars
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/marketing/marketing-events
    properties:
      - url: https://developers.hubspot.com/docs/api/marketing/marketing-events
        type: Documentation
    description: Marketing events are CRM objects that enable you to track marketing activities such as webinars along with the contacts who registered and attended. The marketing events API supports creating and managing events, tracking attendance, and accessing participation analytics.
  - aid: hubspot:hubspot-forms-api
    name: HubSpot Forms API
    tags:
      - Forms
      - Lead Capture
      - Marketing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/marketing/forms
    properties:
      - url: https://developers.hubspot.com/docs/api/marketing/forms
        type: Documentation
    description: The forms endpoints allow you to create and manage HubSpot forms used for capturing lead information. Supported form types include HubSpot native forms, captured external forms, flow forms, and blog comment forms.
  - aid: hubspot:hubspot-conversations-api
    name: HubSpot Conversations API
    tags:
      - Conversations
      - Inbox
      - Messaging
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/conversations/conversations
    properties:
      - url: https://developers.hubspot.com/docs/api/conversations/conversations
        type: Documentation
      - url: openapi/hubspot-conversations-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/conversations-api-actor-collection-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-actor-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-attachment-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-channel-collection-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-channel-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-inbox-collection-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-inbox-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-message-collection-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-message-recipient-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-message-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-message-status-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-paging-next-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-send-message-request-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-thread-collection-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-thread-schema.json
      - type: JSONSchema
        url: json-schema/conversations-api-update-thread-request-schema.json
      - type: JSONSchema
        url: json-structure/conversations-api-actor-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-actor-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-attachment-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-channel-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-channel-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-inbox-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-inbox-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-message-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-message-recipient-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-message-status-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-message-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-paging-next-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-send-message-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-thread-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-thread-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/conversations-api-update-thread-request-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/conversations-api-actor-collection-example.json
      - type: CodeExamples
        url: examples/conversations-api-actor-example.json
      - type: CodeExamples
        url: examples/conversations-api-attachment-example.json
      - type: CodeExamples
        url: examples/conversations-api-channel-collection-example.json
      - type: CodeExamples
        url: examples/conversations-api-channel-example.json
      - type: CodeExamples
        url: examples/conversations-api-inbox-collection-example.json
      - type: CodeExamples
        url: examples/conversations-api-inbox-example.json
      - type: CodeExamples
        url: examples/conversations-api-message-collection-example.json
      - type: CodeExamples
        url: examples/conversations-api-message-example.json
      - type: CodeExamples
        url: examples/conversations-api-message-recipient-example.json
      - type: CodeExamples
        url: examples/conversations-api-message-status-example.json
      - type: CodeExamples
        url: examples/conversations-api-paging-example.json
      - type: CodeExamples
        url: examples/conversations-api-paging-next-example.json
      - type: CodeExamples
        url: examples/conversations-api-send-message-request-example.json
      - type: CodeExamples
        url: examples/conversations-api-thread-collection-example.json
      - type: CodeExamples
        url: examples/conversations-api-thread-example.json
      - type: CodeExamples
        url: examples/conversations-api-update-thread-request-example.json
    description: The conversations API enables management of inboxes, channels, threads, and messages within HubSpot's conversations system. You can retrieve conversation data, update thread statuses, send messages, and access contact-specific conversation history.
  - aid: hubspot:hubspot-engagement-calls-api
    name: HubSpot Engagement Calls API
    tags:
      - Activities
      - Calls
      - Engagements
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/calls
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/calls
        type: Documentation
      - url: openapi/hubspot-engagement-calls-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/engagement-calls-api-association-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-association-type-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-batch-archive-calls-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-batch-calls-response-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-batch-create-calls-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-batch-error-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-batch-read-calls-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-batch-read-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-batch-update-calls-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-batch-update-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-call-collection-response-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-call-create-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-call-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-call-search-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-call-search-response-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-call-update-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-filter-group-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-filter-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-gdpr-delete-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-next-page-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-property-history-schema.json
      - type: JSONSchema
        url: json-schema/engagement-calls-api-sort-option-schema.json
      - type: JSONSchema
        url: json-structure/engagement-calls-api-association-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-association-type-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-batch-archive-calls-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-batch-calls-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-batch-create-calls-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-batch-error-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-batch-read-calls-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-batch-read-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-batch-update-calls-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-batch-update-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-call-collection-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-call-create-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-call-search-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-call-search-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-call-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-call-update-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-filter-group-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-filter-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-gdpr-delete-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-next-page-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-property-history-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-calls-api-sort-option-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/engagement-calls-api-association-input-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-association-type-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-batch-archive-calls-request-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-batch-calls-response-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-batch-create-calls-request-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-batch-error-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-batch-read-calls-request-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-batch-read-input-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-batch-update-calls-request-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-batch-update-input-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-call-collection-response-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-call-create-request-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-call-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-call-search-request-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-call-search-response-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-call-update-request-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-filter-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-filter-group-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-gdpr-delete-request-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-next-page-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-paging-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-property-history-example.json
      - type: CodeExamples
        url: examples/engagement-calls-api-sort-option-example.json
    description: The calls endpoints allow you to log and manage call engagement records within HubSpot CRM. You can create call records, associate them with contacts and deals, retrieve call data, and manage call recordings and transcripts.
  - aid: hubspot:hubspot-engagement-notes-api
    name: HubSpot Engagement Notes API
    tags:
      - Activities
      - Engagements
      - Notes
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/notes
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/notes
        type: Documentation
      - url: openapi/hubspot-engagement-notes-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/engagement-notes-association-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-association-type-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-batch-archive-notes-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-batch-create-notes-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-batch-error-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-batch-notes-response-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-batch-read-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-batch-read-notes-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-batch-update-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-batch-update-notes-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-filter-group-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-filter-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-gdpr-delete-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-next-page-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-note-collection-response-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-note-create-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-note-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-note-search-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-note-search-response-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-note-update-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-paging-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-property-history-schema.json
      - type: JSONSchema
        url: json-schema/engagement-notes-sort-option-schema.json
      - type: JSONSchema
        url: json-structure/engagement-notes-association-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-association-type-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-batch-archive-notes-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-batch-create-notes-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-batch-error-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-batch-notes-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-batch-read-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-batch-read-notes-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-batch-update-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-batch-update-notes-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-filter-group-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-filter-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-gdpr-delete-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-next-page-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-note-collection-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-note-create-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-note-search-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-note-search-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-note-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-note-update-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-property-history-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-notes-sort-option-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/engagement-notes-association-input-example.json
      - type: CodeExamples
        url: examples/engagement-notes-association-type-example.json
      - type: CodeExamples
        url: examples/engagement-notes-batch-archive-notes-request-example.json
      - type: CodeExamples
        url: examples/engagement-notes-batch-create-notes-request-example.json
      - type: CodeExamples
        url: examples/engagement-notes-batch-error-example.json
      - type: CodeExamples
        url: examples/engagement-notes-batch-notes-response-example.json
      - type: CodeExamples
        url: examples/engagement-notes-batch-read-input-example.json
      - type: CodeExamples
        url: examples/engagement-notes-batch-read-notes-request-example.json
      - type: CodeExamples
        url: examples/engagement-notes-batch-update-input-example.json
      - type: CodeExamples
        url: examples/engagement-notes-batch-update-notes-request-example.json
      - type: CodeExamples
        url: examples/engagement-notes-filter-example.json
      - type: CodeExamples
        url: examples/engagement-notes-filter-group-example.json
      - type: CodeExamples
        url: examples/engagement-notes-gdpr-delete-request-example.json
      - type: CodeExamples
        url: examples/engagement-notes-next-page-example.json
      - type: CodeExamples
        url: examples/engagement-notes-note-collection-response-example.json
      - type: CodeExamples
        url: examples/engagement-notes-note-create-request-example.json
      - type: CodeExamples
        url: examples/engagement-notes-note-example.json
      - type: CodeExamples
        url: examples/engagement-notes-note-search-request-example.json
      - type: CodeExamples
        url: examples/engagement-notes-note-search-response-example.json
      - type: CodeExamples
        url: examples/engagement-notes-note-update-request-example.json
      - type: CodeExamples
        url: examples/engagement-notes-paging-example.json
      - type: CodeExamples
        url: examples/engagement-notes-property-history-example.json
      - type: CodeExamples
        url: examples/engagement-notes-sort-option-example.json
    description: The notes endpoints allow you to create and manage note engagement records in HubSpot CRM. Notes can be associated with contacts, companies, deals, and tickets to capture important information and activity history.
  - aid: hubspot:hubspot-engagement-meetings-api
    name: HubSpot Engagement Meetings API
    tags:
      - Activities
      - Engagements
      - Meetings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/meetings
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/meetings
        type: Documentation
      - url: openapi/hubspot-engagement-meetings-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-association-schema.json
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-batch-create-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-batch-read-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-batch-response-meeting-schema.json
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-batch-update-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-collection-response-association-schema.json
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-collection-response-meeting-schema.json
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-filter-group-schema.json
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-filter-schema.json
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-meeting-schema.json
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-search-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-meetings-api-simple-public-object-input-schema.json
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-batch-create-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-batch-read-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-batch-response-meeting-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-batch-update-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-collection-response-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-collection-response-meeting-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-filter-group-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-filter-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-meeting-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-search-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-meetings-api-simple-public-object-input-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/engagement-meetings-api-association-example.json
      - type: CodeExamples
        url: examples/engagement-meetings-api-batch-create-input-example.json
      - type: CodeExamples
        url: examples/engagement-meetings-api-batch-read-input-example.json
      - type: CodeExamples
        url: examples/engagement-meetings-api-batch-response-meeting-example.json
      - type: CodeExamples
        url: examples/engagement-meetings-api-batch-update-input-example.json
      - type: CodeExamples
        url: examples/engagement-meetings-api-collection-response-association-example.json
      - type: CodeExamples
        url: examples/engagement-meetings-api-collection-response-meeting-example.json
      - type: CodeExamples
        url: examples/engagement-meetings-api-filter-example.json
      - type: CodeExamples
        url: examples/engagement-meetings-api-filter-group-example.json
      - type: CodeExamples
        url: examples/engagement-meetings-api-meeting-example.json
      - type: CodeExamples
        url: examples/engagement-meetings-api-paging-example.json
      - type: CodeExamples
        url: examples/engagement-meetings-api-search-request-example.json
      - type: CodeExamples
        url: examples/engagement-meetings-api-simple-public-object-input-example.json
    description: The meetings endpoints allow you to log and manage meeting engagement records in HubSpot CRM. You can create meeting records, associate them with contacts and companies, and retrieve meeting details and outcomes.
  - aid: hubspot:hubspot-engagement-tasks-api
    name: HubSpot Engagement Tasks API
    tags:
      - Activities
      - Engagements
      - Tasks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/crm/tasks
    properties:
      - url: https://developers.hubspot.com/docs/api/crm/tasks
        type: Documentation
      - url: openapi/hubspot-engagement-tasks-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-association-schema.json
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-batch-create-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-batch-read-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-batch-response-task-schema.json
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-batch-update-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-collection-response-association-schema.json
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-collection-response-task-schema.json
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-filter-group-schema.json
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-filter-schema.json
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-search-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-simple-public-object-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-tasks-api-task-schema.json
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-batch-create-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-batch-read-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-batch-response-task-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-batch-update-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-collection-response-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-collection-response-task-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-filter-group-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-filter-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-search-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-simple-public-object-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-tasks-api-task-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/engagement-tasks-api-association-example.json
      - type: CodeExamples
        url: examples/engagement-tasks-api-batch-create-input-example.json
      - type: CodeExamples
        url: examples/engagement-tasks-api-batch-read-input-example.json
      - type: CodeExamples
        url: examples/engagement-tasks-api-batch-response-task-example.json
      - type: CodeExamples
        url: examples/engagement-tasks-api-batch-update-input-example.json
      - type: CodeExamples
        url: examples/engagement-tasks-api-collection-response-association-example.json
      - type: CodeExamples
        url: examples/engagement-tasks-api-collection-response-task-example.json
      - type: CodeExamples
        url: examples/engagement-tasks-api-filter-example.json
      - type: CodeExamples
        url: examples/engagement-tasks-api-filter-group-example.json
      - type: CodeExamples
        url: examples/engagement-tasks-api-paging-example.json
      - type: CodeExamples
        url: examples/engagement-tasks-api-search-request-example.json
      - type: CodeExamples
        url: examples/engagement-tasks-api-simple-public-object-input-example.json
      - type: CodeExamples
        url: examples/engagement-tasks-api-task-example.json
    description: The tasks endpoints allow you to create and manage task engagement records in HubSpot CRM. Tasks represent to-do items that can be assigned to users and associated with contacts, companies, and deals to track follow-up actions.
  - aid: hubspot:hubspot-engagement-emails-api
    name: HubSpot Engagement Emails API
    tags:
      - Activities
      - Emails
      - Engagements
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api-reference/crm-emails-v3/guide
    properties:
      - url: https://developers.hubspot.com/docs/api-reference/crm-emails-v3/guide
        type: Documentation
      - url: openapi/hubspot-engagement-emails-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/engagement-emails-api-association-schema.json
      - type: JSONSchema
        url: json-schema/engagement-emails-api-batch-create-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-emails-api-batch-read-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-emails-api-batch-response-email-engagement-schema.json
      - type: JSONSchema
        url: json-schema/engagement-emails-api-batch-update-input-schema.json
      - type: JSONSchema
        url: json-schema/engagement-emails-api-collection-response-association-schema.json
      - type: JSONSchema
        url: json-schema/engagement-emails-api-collection-response-email-engagement-schema.json
      - type: JSONSchema
        url: json-schema/engagement-emails-api-email-engagement-schema.json
      - type: JSONSchema
        url: json-schema/engagement-emails-api-filter-group-schema.json
      - type: JSONSchema
        url: json-schema/engagement-emails-api-filter-schema.json
      - type: JSONSchema
        url: json-schema/engagement-emails-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/engagement-emails-api-search-request-schema.json
      - type: JSONSchema
        url: json-schema/engagement-emails-api-simple-public-object-input-schema.json
      - type: JSONSchema
        url: json-structure/engagement-emails-api-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-emails-api-batch-create-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-emails-api-batch-read-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-emails-api-batch-response-email-engagement-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-emails-api-batch-update-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-emails-api-collection-response-association-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-emails-api-collection-response-email-engagement-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-emails-api-email-engagement-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-emails-api-filter-group-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-emails-api-filter-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-emails-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-emails-api-search-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/engagement-emails-api-simple-public-object-input-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/engagement-emails-api-association-example.json
      - type: CodeExamples
        url: examples/engagement-emails-api-batch-create-input-example.json
      - type: CodeExamples
        url: examples/engagement-emails-api-batch-read-input-example.json
      - type: CodeExamples
        url: examples/engagement-emails-api-batch-response-email-engagement-example.json
      - type: CodeExamples
        url: examples/engagement-emails-api-batch-update-input-example.json
      - type: CodeExamples
        url: examples/engagement-emails-api-collection-response-association-example.json
      - type: CodeExamples
        url: examples/engagement-emails-api-collection-response-email-engagement-example.json
      - type: CodeExamples
        url: examples/engagement-emails-api-email-engagement-example.json
      - type: CodeExamples
        url: examples/engagement-emails-api-filter-example.json
      - type: CodeExamples
        url: examples/engagement-emails-api-filter-group-example.json
      - type: CodeExamples
        url: examples/engagement-emails-api-paging-example.json
      - type: CodeExamples
        url: examples/engagement-emails-api-search-request-example.json
      - type: CodeExamples
        url: examples/engagement-emails-api-simple-public-object-input-example.json
    description: The emails engagement API allows you to log and manage email activity records on CRM records in HubSpot. You can create email engagement records to track sent emails, associate them with contacts and deals, and retrieve email activity history.
  - aid: hubspot:hubspot-custom-workflow-actions-api
    name: HubSpot Custom Workflow Actions API
    tags:
      - Automation
      - Custom Actions
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/automation/custom-workflow-actions
    properties:
      - url: https://developers.hubspot.com/docs/api/automation/custom-workflow-actions
        type: Documentation
      - url: openapi/hubspot-custom-workflow-actions-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-action-definition-collection-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-action-definition-input-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-action-definition-patch-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-action-definition-revision-collection-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-action-definition-revision-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-action-definition-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-action-function-collection-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-action-function-input-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-action-function-reference-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-action-function-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-action-labels-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-batch-callback-completion-request-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-batch-callback-error-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-batch-callback-input-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-batch-callback-response-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-callback-completion-request-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-field-option-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-field-type-definition-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-input-field-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-object-request-options-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-output-field-schema.json
      - type: JSONSchema
        url: json-schema/custom-workflow-actions-api-paging-schema.json
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-action-definition-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-action-definition-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-action-definition-patch-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-action-definition-revision-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-action-definition-revision-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-action-definition-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-action-function-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-action-function-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-action-function-reference-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-action-function-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-action-labels-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-batch-callback-completion-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-batch-callback-error-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-batch-callback-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-batch-callback-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-callback-completion-request-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-field-option-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-field-type-definition-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-input-field-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-object-request-options-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-output-field-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/custom-workflow-actions-api-paging-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-action-definition-collection-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-action-definition-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-action-definition-input-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-action-definition-patch-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-action-definition-revision-collection-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-action-definition-revision-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-action-function-collection-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-action-function-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-action-function-input-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-action-function-reference-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-action-labels-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-batch-callback-completion-request-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-batch-callback-error-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-batch-callback-input-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-batch-callback-response-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-callback-completion-request-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-field-option-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-field-type-definition-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-input-field-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-object-request-options-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-output-field-example.json
      - type: CodeExamples
        url: examples/custom-workflow-actions-api-paging-example.json
    description: Custom workflow actions allow you to extend HubSpot workflows by creating reusable actions that can be installed by HubSpot users. The custom workflow actions API allows you to define, manage, and retrieve custom action definitions for use in HubSpot automation workflows.
  - aid: hubspot:hubspot-workflows-api
    name: HubSpot Workflows API
    tags:
      - Automation
      - Operations
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/automation/workflows
    properties:
      - url: https://developers.hubspot.com/docs/api/automation/workflows
        type: Documentation
    description: The workflows API allows you to programmatically create, retrieve, update, and delete HubSpot automation workflows. You can manage workflow definitions and automate business processes across CRM objects and marketing activities.
  - aid: hubspot:hubspot-webhooks-api
    name: HubSpot Webhooks API
    tags:
      - Events
      - Integrations
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api/webhooks
    properties:
      - url: https://developers.hubspot.com/docs/api/webhooks
        type: Documentation
      - url: asyncapi/hubspot-webhooks-asyncapi.yml
        type: AsyncAPI
    description: The webhooks API allows you to subscribe to events occurring in a HubSpot account, receiving real-time notifications when CRM objects or conversations are created, updated, or deleted. You can configure subscriptions, manage webhook settings, and validate incoming webhook payloads.
  - aid: hubspot:hubspot-crm-feature-flags-api
    name: HubSpot CRM Feature Flags API
    tags:
      - App Management
      - CRM
      - Feature Flags
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api-reference/crm-public-app-feature-flags-v3-v3/guide
    properties:
      - url: https://developers.hubspot.com/docs/api-reference/crm-public-app-feature-flags-v3-v3/guide
        type: Documentation
      - url: openapi/hubspot-crm-feature-flags-api-openapi.yml
        type: OpenAPI
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-batch-delete-input-item-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-batch-delete-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-batch-error-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-batch-portal-flag-state-input-item-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-batch-portal-flag-state-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-batch-portal-flag-state-response-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-batch-portal-flag-state-response-with-errors-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-feature-flag-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-feature-flag-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-flag-state-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-paging-next-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-paging-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-portal-flag-state-collection-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-portal-flag-state-input-schema.json
      - type: JSONSchema
        url: json-schema/crm-feature-flags-api-portal-flag-state-schema.json
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-batch-delete-input-item-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-batch-delete-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-batch-error-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-batch-portal-flag-state-input-item-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-batch-portal-flag-state-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-batch-portal-flag-state-response-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-batch-portal-flag-state-response-with-errors-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-feature-flag-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-feature-flag-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-flag-state-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-paging-next-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-paging-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-portal-flag-state-collection-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-portal-flag-state-input-structure.json
        title: JSON Structure
      - type: JSONSchema
        url: json-structure/crm-feature-flags-api-portal-flag-state-structure.json
        title: JSON Structure
      - type: CodeExamples
        url: examples/crm-feature-flags-api-batch-delete-input-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-batch-delete-input-item-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-batch-error-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-batch-portal-flag-state-input-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-batch-portal-flag-state-input-item-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-batch-portal-flag-state-response-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-batch-portal-flag-state-response-with-errors-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-feature-flag-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-feature-flag-input-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-flag-state-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-paging-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-paging-next-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-portal-flag-state-collection-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-portal-flag-state-example.json
      - type: CodeExamples
        url: examples/crm-feature-flags-api-portal-flag-state-input-example.json
    description: The feature flags API allows public app developers to manage feature flags for their HubSpot app installations. Feature flags can be used to control the rollout of new functionality to specific accounts or user segments.
  - aid: hubspot:hubspot-settings-user-provisioning-api
    name: HubSpot Settings User Provisioning API
    tags:
      - Settings
      - Teams
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api-reference/settings-user-provisioning-v3/guide
    properties:
      - url: https://developers.hubspot.com/docs/api-reference/settings-user-provisioning-v3/guide
        type: Documentation
    description: The user provisioning API allows you to create and manage users in a HubSpot account along with their roles, permissions, and team assignments. You can add, retrieve, update, and remove users programmatically for account administration.
  - aid: hubspot:hubspot-blog-tags-api
    name: HubSpot Blog Tags API
    tags:
      - Blogs
      - CMS
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/cms/blogs/blog-tags
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/cms/blogs/blog-tags
        type: Documentation
    description: The blog tags API allows you to create, manage, and organize blog post tags in HubSpot CMS. Tags help organize blog content and improve discoverability. You can create, retrieve, update, and delete tags, as well as manage multi-language tag variants.
  - aid: hubspot:hubspot-cms-site-search-api
    name: HubSpot CMS Site Search API
    tags:
      - CMS
      - Content
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/cms/site-search
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/cms/site-search
        type: Documentation
    description: The site search API allows you to search the content of HubSpot-hosted sites, including site pages, blog posts, landing pages, and knowledge articles. You can build custom site search experiences and access indexed data for documents with ranking customization and filtering.
  - aid: hubspot:hubspot-cms-content-audit-api
    name: HubSpot CMS Content Audit API
    tags:
      - Audit
      - CMS
      - Content
      - Logs
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/cms/content-audit
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/cms/content-audit
        type: Documentation
    description: The CMS content audit API allows you to query audit logs of CMS changes that occurred within your HubSpot account. You can filter and sort on content object changes by type, time period, or HubSpot user ID to track content change history.
  - aid: hubspot:hubspot-files-api
    name: HubSpot Files API
    tags:
      - Files
      - Storage
      - Uploads
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/library/files
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/library/files
        type: Documentation
    description: The files API allows you to upload, manage, and organize files in HubSpot's file manager. You can upload files, organize them into folders, control file accessibility and privacy settings, retrieve file details, and attach files to CRM records.
  - aid: hubspot:hubspot-feedback-submissions-api
    name: HubSpot Feedback Submissions API
    tags:
      - CRM
      - Feedback
      - Surveys
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/objects/feedback-submissions
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/objects/feedback-submissions
        type: Documentation
    description: The feedback submissions API allows you to retrieve survey response data from HubSpot surveys including NPS, CSAT, CES, and custom surveys. This is a read-only API that provides access to existing survey responses and their associated properties.
  - aid: hubspot:hubspot-leads-api
    name: HubSpot Leads API
    tags:
      - CRM
      - Leads
      - Sales
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/objects/leads
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/objects/leads
        type: Documentation
    description: The leads API enables you to manage lead records in HubSpot. Leads are contacts or companies that are potential customers who have shown interest in your products or services. You can create, retrieve, update, and delete lead records and manage their associations with contacts and other CRM objects.
  - aid: hubspot:hubspot-goals-api
    name: HubSpot Goals API
    tags:
      - CRM
      - Goals
      - Quotas
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/objects/goals
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/objects/goals
        type: Documentation
    description: The goals API enables you to sync user-specific sales and service team quotas between HubSpot and external systems. Goals are used to create user-specific quotas based on templates provided by HubSpot, and can be retrieved, created, updated, and deleted through the API.
  - aid: hubspot:hubspot-orders-api
    name: HubSpot Orders API
    tags:
      - Commerce
      - Ecommerce
      - Orders
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/commerce/orders
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/commerce/orders
        type: Documentation
    description: The orders API enables you to create and manage ecommerce order data in HubSpot. You can create orders, manage associations to contacts, line items, payments, and invoices, and track fulfillment progress using customizable pipelines and stages.
  - aid: hubspot:hubspot-carts-api
    name: HubSpot Carts API
    tags:
      - Carts
      - Commerce
      - Ecommerce
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/commerce/carts
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/commerce/carts
        type: Documentation
    description: The carts API enables you to create and manage ecommerce cart data in HubSpot. You can sync cart information between HubSpot and external ecommerce platforms, manage cart properties like pricing and currency, and associate carts with contacts, line items, and orders.
  - aid: hubspot:hubspot-invoices-api
    name: HubSpot Invoices API
    tags:
      - Billing
      - Commerce
      - Invoices
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/commerce/invoices
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/commerce/invoices
        type: Documentation
    description: The invoices API allows you to create, manage, retrieve, and delete invoices used for billing customers. Invoices progress through draft, open, paid, and voided statuses, and can be configured with digital payment collection via HubSpot Payments or Stripe.
  - aid: hubspot:hubspot-taxes-api
    name: HubSpot Taxes API
    tags:
      - Commerce
      - Pricing
      - Taxes
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/commerce/taxes
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/commerce/taxes
        type: Documentation
    description: The taxes API enables you to create and associate tax objects as part of the pricing details for quotes and invoices. Taxes are used in conjunction with discounts and fees when determining pricing totals, with taxes applied last in the calculation sequence.
  - aid: hubspot:hubspot-fees-api
    name: HubSpot Fees API
    tags:
      - Commerce
      - Fees
      - Pricing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/commerce/fees
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/commerce/fees
        type: Documentation
    description: The fees API allows you to create and manage fees that can be included in invoices and legacy quotes. Fees support fixed dollar amounts or percentage-based values and are used alongside discounts and taxes when determining pricing totals.
  - aid: hubspot:hubspot-discounts-api
    name: HubSpot Discounts API
    tags:
      - Commerce
      - Discounts
      - Pricing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/commerce/discounts
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/commerce/discounts
        type: Documentation
    description: The discounts API enables you to create and associate discounts as part of the pricing details for quotes. Discounts work alongside fees and taxes in the quote pricing workflow, being applied first in the calculation sequence.
  - aid: hubspot:hubspot-engagement-communications-api
    name: HubSpot Engagement Communications API
    tags:
      - Communications
      - Engagements
      - Messaging
      - SMS
      - WhatsApp
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/engagements/communications
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/engagements/communications
        type: Documentation
    description: The communications API allows you to log WhatsApp, LinkedIn, or SMS messages to CRM record timelines. You can create, retrieve, update, and manage message engagement records and associate them with contacts, companies, and other CRM objects.
  - aid: hubspot:hubspot-engagement-postal-mail-api
    name: HubSpot Engagement Postal Mail API
    tags:
      - Activities
      - Engagements
      - Postal Mail
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/engagements/postal-mail
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/engagements/postal-mail
        type: Documentation
    description: The postal mail engagement API allows you to log postal mail sent to or received from contacts or companies on their CRM records. You can create, retrieve, update, and delete postal mail engagement records and associate them with contacts, companies, deals, and tickets.
  - aid: hubspot:hubspot-transactional-email-api
    name: HubSpot Transactional Email API
    tags:
      - Marketing
      - SMTP
      - Transactional Email
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api-reference/marketing-transactional-single-send-v3/guide
    properties:
      - url: https://developers.hubspot.com/docs/api-reference/marketing-transactional-single-send-v3/guide
        type: Documentation
    description: The transactional email API enables sending template-based transactional emails through HubSpot using the Single Send API and managing SMTP tokens. You can send emails for commerce receipts, account updates, and other essential business transactions over a dedicated IP address.
  - aid: hubspot:hubspot-subscription-preferences-api
    name: HubSpot Subscription Preferences API
    tags:
      - Email Preferences
      - Marketing
      - Subscriptions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/marketing/subscriptions
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/marketing/subscriptions
        type: Documentation
    description: The subscription preferences API allows you to manage email subscription details for contacts in your account. You can retrieve subscription types, check contact preferences, subscribe or unsubscribe contacts, manage global opt-outs, and perform bulk operations on subscription statuses.
  - aid: hubspot:hubspot-timeline-events-api
    name: HubSpot Timeline Events API
    tags:
      - CRM
      - Events
      - Extensions
      - Timeline
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/extensions/timeline
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/extensions/timeline
        type: Documentation
    description: The timeline events API enables technology partners to send custom event data from external systems into HubSpot for display on CRM record activity timelines. You can create event templates, define custom tokens, configure display templates, and associate events with CRM records.
  - aid: hubspot:hubspot-calling-extensions-api
    name: HubSpot Calling Extensions API
    tags:
      - Calling
      - CRM
      - Extensions
      - SDK
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/extensions/calling-sdk
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/extensions/calling-sdk
        type: Documentation
    description: The calling extensions SDK enables apps to provide a custom calling option to HubSpot users directly from CRM records. The SDK facilitates bidirectional communication between calling applications and HubSpot, including call event messaging and automatic engagement record creation.
  - aid: hubspot:hubspot-video-conferencing-api
    name: HubSpot Video Conferencing API
    tags:
      - CRM
      - Extensions
      - Meetings
      - Video Conferencing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/crm/extensions/video-conferencing
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/crm/extensions/video-conferencing
        type: Documentation
    description: The video conferencing API enables you to integrate custom video conferencing solutions into HubSpot's meeting creation workflow. You can configure webhook notifications for meeting creation, updates, and deletion, and provide conference link details directly in meeting invitations.
  - aid: hubspot:hubspot-account-information-api
    name: HubSpot Account Information API
    tags:
      - Account
      - Configuration
      - Settings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/api-reference/account-account-info-v3/guide
    properties:
      - url: https://developers.hubspot.com/docs/api-reference/account-account-info-v3/guide
        type: Documentation
    description: The account information API provides account configuration and usage data for HubSpot accounts. You can retrieve account details including portal ID, time zone, currency settings, and data center location, as well as monitor daily API call consumption.
  - aid: hubspot:hubspot-business-units-api
    name: HubSpot Business Units API
    tags:
      - Brands
      - Business Units
      - Settings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/settings/business-units-api
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/settings/business-units-api
        type: Documentation
    description: The business units (brands) API provides information about brands tied to a HubSpot user. You can retrieve brand data including brand name, ID, and logo metadata for brands associated with a specific user account.
  - aid: hubspot:hubspot-currencies-api
    name: HubSpot Currencies API
    tags:
      - Currencies
      - Exchange Rates
      - Settings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.hubapi.com
    humanURL: https://developers.hubspot.com/docs/guides/api/settings/currencies
    properties:
      - url: https://developers.hubspot.com/docs/guides/api/settings/currencies
        type: Documentation
    description: The currencies API allows you to manage the currencies used in your HubSpot account. You can set your account's company currency, create additional currencies, update exchange rates, and configure automatic exchange rate updates for multi-currency operations.
name: HubSpot
tags:
  - Analytics
  - Commerce
  - Content
  - CRM
  - Customer Service
  - Email Marketing
  - Marketing
  - Marketing Automation
  - Operations
  - Sales
type: Contract
image: https://www.hubspot.com/hubfs/HubSpot_Logos/HubSpot-Inversed-Favicon.png
access: 3rd-Party
common:
  - url: https://api.hubspot.com/api-catalog-public/v1/apis
    type: APIReference
  - url: https://developers.hubspot.com/
    type: Portal
  - url: https://developers.hubspot.com/docs/api/overview
    type: Documentation
  - url: https://developers.hubspot.com/changelog
    type: ChangeLog
  - url: https://community.hubspot.com/t5/HubSpot-Developers/ct-p/developers
    type: Support
  - url: https://developers.hubspot.com/slack
    type: Support
  - url: https://developers.hubspot.com/blog
    type: Blog
  - url: https://offers.hubspot.com/developer-newsletter-signup
    type: Newsletter
  - url: https://www.hubspot.com/developer-community-events
    type: Events
  - url: https://ecosystem.hubspot.com/marketplace/apps
    type: Integrations
  - url: https://legal.hubspot.com/privacy-policy
    type: PrivacyPolicy
  - url: https://legal.hubspot.com/terms-of-service
    type: TermsOfService
  - url: https://developers.hubspot.com/docs/getting-started/overview
    name: Getting started overview | HubSpot
    type: GettingStarted
  - url: https://developers.hubspot.com/docs/guides/api
    name: Guides | HubSpot
    type: Documentation
  - url: https://developers.hubspot.com/docs/reference/api/overview
    name: HubSpot API reference | HubSpot
    type: Documentation
  - url: https://app.hubspot.com/login
    name: HubSpot Login and Sign in
    type: Login
  - url: https://offers.hubspot.com/crm-platform-demo
    name: HubSpot Customer Platform Demo
    type: Contact
  - url: https://www.hubspot.com/our-story
    name: About HubSpot | HubSpots Story
    type: Documentation
  - url: https://blog.hubspot.com/
    name: HubSpot Blog | Marketing, Sales, Agency, and Customer Success Content
    type: Blog
  - url: https://legal.hubspot.com/security
    name: HubSpot Security Program
    type: Security
  - url: https://www.hubspot.com/partners/affiliates
    name: HubSpot Affiliate Program | Overview
    type: Partners
  - url: https://www.hubspot.com/partners
    name: HubSpot Partner Programs
    type: Partners
  - url: https://www.hubspot.com/pricing/marketing/enterprise
    name: Marketing Software Pricing | HubSpot
    type: Pricing
  - url: https://www.hubspot.com/case-studies
    name: Case Studies | HubSpot
    type: Showcase
  - data:
      - Free CRM with unlimited free users
      - Marketing Hub Starter at $9/seat/mo annual
      - Marketing Hub Professional at $890/mo with mandatory $3,000 onboarding
      - Marketing Hub Enterprise at $3,600/mo with $7,000 onboarding
      - Sales, Service, Operations, CMS, and Content Hubs with parallel tiering
      - Marketing Contact-based pricing (1k included Starter, 2k Pro, 10k Enterprise)
      - Additional 5,000 contacts at $250/month on Professional
      - Additional seats at $45/month (Pro) or $75/month (Enterprise)
      - REST API at 250k req/day Free/Starter, 500k Pro/Enterprise
      - 100 req/10s burst (Free/Starter), 150 req/10s (Pro/Enterprise)
      - Search API limited to 4 req/sec
      - Batch endpoints up to 100 objects per request
      - Custom objects on Enterprise
      - Workflows, sequences, and automation
      - OAuth 2.0 and private app tokens
      - Webhooks v3 for object change events
    name: Features
    type: Features
    sources:
      - https://www.hubspot.com/pricing/marketing
    updated: '2026-05-04'
  - data:
      - name: AI-Powered Content Creation
        description: Use AI to generate blog posts, social media content, and marketing copy at scale.
      - name: AI-Powered Sales
        description: Leverage AI for lead scoring, deal forecasting, and automated sales email generation.
      - name: Analytics
        description: Track and analyze marketing, sales, and service performance with unified reporting dashboards.
      - name: Content Creation and Management
        description: Create, manage, and publish website content, blog posts, and landing pages.
      - name: Content Hub
        description: Centralized content management for creating and distributing content across channels.
      - name: Customer Service
        description: Manage customer support tickets, knowledge base, and feedback surveys.
      - name: Customer Support Automation
        description: Automate ticket routing, responses, and escalation with workflow-based support.
      - name: Data Management and Insights
        description: Clean, deduplicate, and enrich CRM data with automated data quality tools.
      - name: Deal Management
        description: Track deals through customizable pipeline stages with forecasting and reporting.
      - name: Email Marketing
        description: Design, send, and analyze marketing email campaigns with segmentation and A/B testing.
      - name: HubSpot Ecosystem
        description: Connect with 1,500+ integrations in the HubSpot App Marketplace.
      - name: Inbound Marketing
        description: Attract visitors with SEO, blogs, and social media, then convert them with forms and CTAs.
      - name: Integration and Automation
        description: Connect apps and automate business processes with programmable workflows.
      - name: Landing Pages & Forms
        description: Build landing pages with embedded forms to capture and qualify leads.
      - name: Lead Generation and Conversion
        description: Capture leads through forms, chatbots, and CTAs, then nurture with automated sequences.
      - name: Live Chat
        description: Engage website visitors in real-time with live chat and route conversations to the right team.
      - name: Operations Hub
        description: Sync, clean, and automate business data across systems with programmable automation.
      - name: Sales Management
        description: Manage sales teams with activity tracking, quotas, forecasting, and coaching tools.
      - name: Service Hub
        description: Deliver customer service with ticketing, knowledge base, feedback, and customer portal.
      - name: Workflows
        description: Automate repetitive tasks across marketing, sales, and service with visual workflow builder.
    name: Use Cases
    type: UseCases
  - url: https://app.hubspot.com/signup/developers
    name: HubSpot Developer Sign Up
    type: SignUp
  - url: https://developers.hubspot.com/docs/api/intro-to-auth
    name: HubSpot Authentication Overview
    type: Authentication
  - url: https://developers.hubspot.com/docs/guides/apps/api-usage/usage-details
    name: HubSpot API Usage Guidelines and Limits
    type: RateLimits
  - url: https://status.hubspot.com
    name: HubSpot Status
    type: StatusPage
  - url: https://community.hubspot.com/t5/APIs-Integrations/bd-p/integrations
    name: HubSpot APIs and Integrations Community
    type: Support
  - url: https://github.com/HubSpot
    name: HubSpot GitHub Organization
    type: GitHubOrganization
  - url: https://github.com/HubSpot/HubSpot-public-api-spec-collection
    name: HubSpot Public API Spec Collection
    type: GitHubRepository
  - url: https://developers.hubspot.com/docs/api/client-libraries
    name: HubSpot Client Libraries
    type: SDK
  - url: https://stackoverflow.com/questions/tagged/hubspot
    name: HubSpot on Stack Overflow
    type: StackOverflow
  - url: https://www.postman.com/hubspot/hubspot-public-api-workspace/overview
    name: HubSpot Public API Postman Workspace
    type: Resources
  - url: https://developers.hubspot.com/developer-tools
    name: HubSpot Developer Tools
    type: Resources
  - url: https://developers.hubspot.com/apisbytier
    name: HubSpot APIs by Product Tier
    type: APIReference
  - url: json-schema/hubspot-crm-object-schema.json
    name: HubSpot CRM Object JSON Schema
    type: JSONSchema
    description: JSON Schema draft 2020-12 for a HubSpot CRM object record including properties, associations, and metadata.
  - url: json-schema/hubspot-crm-search-request-schema.json
    name: HubSpot CRM Search Request JSON Schema
    type: JSONSchema
    description: JSON Schema draft 2020-12 for a CRM search request body with filter groups, sorts, pagination, and property selection.
  - url: json-ld/hubspot-context.jsonld
    name: HubSpot JSON-LD Context
    type: JSONLD
    description: JSON-LD context file mapping HubSpot CRM entities to schema.org, Dublin Core, and other standard vocabularies.
  - type: Integrations
    name: Integrations
    data:
      - name: Salesforce
        description: Bi-directional CRM sync between HubSpot and Salesforce for unified sales and marketing data.
      - name: Slack
        description: Send HubSpot notifications, create tasks, and share CRM data directly in Slack channels.
      - name: Google Workspace
        description: Sync contacts, calendar events, and emails between HubSpot and Google Workspace apps.
      - name: Microsoft 365
        description: Connect Outlook email, calendar, and contacts with HubSpot CRM for seamless productivity.
      - name: Zoom
        description: Automatically log Zoom meeting details and recordings on CRM contact timelines.
      - name: Shopify
        description: Sync ecommerce order data, products, and customers between Shopify and HubSpot.
      - name: WordPress
        description: Embed HubSpot forms, live chat, and analytics on WordPress sites with the official plugin.
      - name: Stripe
        description: Process payments and sync transaction data between Stripe and HubSpot Commerce.
      - name: Zapier
        description: Connect HubSpot with thousands of apps through automated Zapier workflows.
      - name: Jira
        description: Sync support tickets and development issues between HubSpot and Jira.
      - name: QuickBooks
        description: Sync invoices, payments, and customer data between HubSpot and QuickBooks.
      - name: Snowflake
        description: Share HubSpot CRM and marketing data with Snowflake for advanced analytics.
      - name: Google Ads
        description: Track ad performance and sync audiences between HubSpot and Google Ads.
      - name: Facebook Ads
        description: Create and manage Facebook ad campaigns with HubSpot audience targeting.
      - name: LinkedIn
        description: Sync LinkedIn lead gen forms and ads data with HubSpot for B2B marketing.
  - type: SDK
    title: Python SDK
    url: https://pypi.org/project/hubspot-api-client/
  - type: SDK
    title: Node.js SDK
    url: https://www.npmjs.com/package/@hubspot/api-client
  - type: SDK
    title: Ruby SDK
    url: https://rubygems.org/gems/hubspot-api-client
  - type: SDK
    title: PHP SDK
    url: https://packagist.org/packages/hubspot/api-client
  - type: CLI
    title: HubSpot CLI
    url: https://www.npmjs.com/package/@hubspot/cli
  - type: GitHubRepository
    title: HubSpot MCP Server
    url: https://github.com/HubSpot/mcp-server
  - type: SDK
    title: Calling Extensions SDK
    url: https://github.com/HubSpot/calling-extensions-sdk
  - type: JSONLD
    url: json-ld/hubspot-analytics-events-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-authors-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-blog-posts-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-cms-hubdb-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-cms-pages-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-commerce-payments-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-commerce-subscriptions-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-conversations-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-crm-associations-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-crm-companies-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-crm-contacts-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-crm-deals-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-crm-feature-flags-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-crm-lists-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-crm-search-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-crm-tickets-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-custom-workflow-actions-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-domains-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-calls-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-emails-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-meetings-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-notes-association-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-notes-batch-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-notes-filter-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-notes-gdpr-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-notes-next-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-notes-note-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-notes-paging-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-notes-property-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-notes-sort-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-engagement-tasks-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-marketing-emal-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-oauth-api-context.jsonld
  - type: JSONLD
    url: json-ld/hubspot-source-code-api-context.jsonld
  - type: Documentation
    title: Spectral Rules
    url: rules/hubspot-spectral-rules.yml
  - type: Documentation
    title: Vocabulary
    url: vocabulary/hubspot-vocabulary.yaml
  - type: Documentation
    title: Naftiko Capability
    url: capabilities/automation-and-integration.yaml
  - type: Documentation
    title: Naftiko Capability
    url: capabilities/commerce-operations.yaml
  - type: Documentation
    title: Naftiko Capability
    url: capabilities/content-management.yaml
  - type: Documentation
    title: Naftiko Capability
    url: capabilities/crm-management.yaml
  - type: Documentation
    title: Naftiko Capability
    url: capabilities/marketing-automation.yaml
  - type: Documentation
    title: Naftiko Capability
    url: capabilities/sales-engagement.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/analytics-events-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/authors-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/blog-posts-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/cms-hubdb-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/cms-pages-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/commerce-payments-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/commerce-subscriptions-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/conversations-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/crm-associations-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/crm-companies-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/crm-contacts-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/crm-deals-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/crm-feature-flags-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/crm-lists-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/crm-search-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/crm-tickets-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/custom-workflow-actions-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/domains-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/engagement-calls-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/engagement-emails-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/engagement-meetings-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/engagement-notes.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/engagement-tasks-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/marketing-emal-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/oauth-api.yaml
  - type: Documentation
    title: Naftiko Shared Capability
    url: capabilities/shared/source-code-api.yaml
created: 2023/11/14
modified: '2026-05-04'
position: Consuming
description: HubSpot provides a full platform of marketing, sales, customer service, and CRM software plus the methodology, resources, and support to help businesses grow better.
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
specificationVersion: '0.16'
---
