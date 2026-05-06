---
aid: rescuegroups-org
name: RescueGroups.org
description: RescueGroups.org provides the only updatable HTTP/JSON API for adoptable pet data, offering comprehensive search across animals, organizations, breeds, species, colors, and patterns with geodistance filtering. The API supports both public read-only access via API key and authenticated write access via bearer token, enabling rescue organizations to manage and share pet adoption data in real time.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Animals
  - Pet Adoption
  - Rescue
  - Animal Welfare
url: https://raw.githubusercontent.com/api-evangelist/rescuegroups-org/refs/heads/main/apis.yml
created: '2025-01-07'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rescuegroups-org:rescuegroups-org
    name: RescueGroups.org API
    description: The RescueGroups.org REST API v5 provides access to adoptable pet data including animals, organizations, breeds, species, colors, and patterns. It supports advanced search with geodistance filtering, pagination, and relationship inclusion. API key authorization is used for public data access; bearer token authorization is used for private/write operations.
    humanURL: https://rescuegroups.org/services/adoptable-pet-data-api/
    baseURL: https://api.rescuegroups.org/v5
    tags:
      - Animals
      - Pet Adoption
      - Rescue
      - Organizations
      - Animal Welfare
      - Breeds
      - Species
    properties:
      - type: Documentation
        url: https://userguide.rescuegroups.org/spaces/APIDG/pages/24053254/v5
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rescuegroups-org/refs/heads/main/openapi/rescuegroups-org-openapi.yml
      - type: PostmanCollection
        url: https://documenter.getpostman.com/view/60615/SWT5j1e4
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/rescuegroups-org/refs/heads/main/json-schema/rescuegroups-org-animal-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/rescuegroups-org/refs/heads/main/json-schema/rescuegroups-org-organization-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/rescuegroups-org/refs/heads/main/json-structure/rescuegroups-org-animal-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/rescuegroups-org/refs/heads/main/json-ld/rescuegroups-org-context.jsonld
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/rescuegroups-org/refs/heads/main/rules/rescuegroups-org-rules.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/rescuegroups-org/refs/heads/main/capabilities/pet-adoption-search.yaml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/rescuegroups-org/refs/heads/main/vocabulary/rescuegroups-org-vocabulary.yml
    contact:
      - FN: RescueGroups.org Developer Community
        url: https://groups.google.com/a/rescuegroups.org/g/apidev
common:
  - type: Website
    url: https://rescuegroups.org/
  - type: Documentation
    url: https://userguide.rescuegroups.org/spaces/APIDG/pages/8192120/API+Developers+Guide+Home
  - type: PostmanCollection
    url: https://documenter.getpostman.com/view/60615/SWT5j1e4
  - type: CommunityForum
    url: https://groups.google.com/a/rescuegroups.org/g/apidev
  - type: Authentication
    url: https://userguide.rescuegroups.org/spaces/APIDG/pages/24053254/v5
  - type: About
    url: https://rescuegroups.org/about/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
