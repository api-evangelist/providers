---
aid: crossref
name: Crossref
x-type: company
description: Crossref is a non-profit organization that provides digital infrastructure for scholarly communications. Best known for Digital Object Identifier (DOI) registration, Crossref also operates a public REST API offering searchable, filterable access to metadata for tens of millions of scholarly works, journals, members, funders, prefixes, types, licenses, and DOI registration agency information. The Crossref REST API supports free-form queries, field queries, filters, facets, deep-paging cursors, and selection of specific elements, and is used by reference managers, repositories, discovery layers, and analytics platforms.
url: https://raw.githubusercontent.com/api-evangelist/crossref/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Citations
  - DOI
  - Funders
  - Identifiers
  - Journals
  - Licenses
  - Members
  - Metadata
  - Open Access
  - ORCID
  - Prefixes
  - Publishers
  - Reference Linking
  - ROR
  - Scholarly
created: '2024-07-02'
modified: '2026-04-28'
specificationVersion: '0.20'
type: Index
access: Public
position: Provider
apis:
  - aid: crossref:crossref-rest-api
    name: Crossref REST API
    description: The Crossref REST API is a public, read-only metadata API that provides programmatic access to Crossref's database of scholarly content. Endpoints expose works, journals, members, funders, types, licenses, prefixes, and DOI registration agency lookups, with rich query, filter, facet, sort, select, and cursor-based deep paging capabilities. No sign-up is required, but consumers are encouraged to use the polite pool by including a mailto query parameter or User-Agent contact for higher reliability.
    humanURL: https://www.crossref.org/documentation/retrieve-metadata/rest-api/
    baseURL: https://api.crossref.org
    properties:
      - type: Documentation
        url: https://www.crossref.org/documentation/retrieve-metadata/rest-api/
      - type: SwaggerUI
        url: https://api.crossref.org/swagger-ui/
      - type: PolitePool
        url: https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/#etiquette
      - type: Tips
        url: https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/
      - type: OpenAPI
        url: openapi/crossref-openapi.yml
      - type: Rules
        url: rules/crossref-rules.yml
      - type: Capabilities
        url: capabilities/crossref-capabilities.yml
      - type: JSONSchema
        url: json-schema/crossref-work-schema.json
      - type: JSONLD
        url: json-ld/crossref-context.jsonld
    tags:
      - Agency
      - Funders
      - Journals
      - Licenses
      - Members
      - Metadata
      - Prefixes
      - Types
      - Works
common:
  - type: Vocabulary
    url: vocabulary/crossref-vocabulary.yml
  - type: JSONLD
    url: json-ld/crossref-context.jsonld
  - type: JSONSchema
    url: json-schema/crossref-work-schema.json
  - type: Website
    url: https://www.crossref.org/
  - type: Documentation
    url: https://www.crossref.org/documentation/
  - type: APIDocumentation
    url: https://www.crossref.org/documentation/retrieve-metadata/rest-api/
  - type: Blog
    url: https://www.crossref.org/blog/
  - type: GitHubOrganization
    url: https://github.com/CrossRef
  - type: StatusPage
    url: https://status.crossref.org/
  - type: Community
    url: https://community.crossref.org/
  - type: TermsOfService
    url: https://www.crossref.org/operations-and-sustainability/terms/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
