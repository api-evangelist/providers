---
aid: science-museum-group
name: Science Museum Group
description: 'The Science Museum Group operates five UK science and technology museums: the Science Museum (London), the Science and Industry Museum (Manchester), the National Railway Museum (York), the National Science and Media Museum (Bradford), and Locomotion (Shildon). The group provides an open Collection API giving developers programmatic access to over 7 million objects, people, and documents in the museum collections via a JSONAPI-compliant REST interface. The API is free to use and supports searching, filtering, and retrieval of collection items with rich metadata, images, and curatorial notes.'
url: https://raw.githubusercontent.com/api-evangelist/science-museum-group/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Museums
  - Collections
  - Cultural Heritage
  - Open Data
  - Science
  - Technology
  - United Kingdom
apis:
  - aid: science-museum-group:collection-api
    name: Science Museum Group Collection API
    description: A JSONAPI-compliant REST API providing open access to the Science Museum Group's collection of over 7 million objects, people, and documents across its five UK museums. Search and retrieve data about scientific instruments, industrial artifacts, railway objects, and cultural items with image access, pagination, and rich filtering by date, place, maker, museum, and category.
    humanURL: https://www.sciencemuseumgroup.org.uk/our-work/our-collection/using-our-collection-api
    baseURL: https://collection.sciencemuseumgroup.org.uk
    tags:
      - Collections
      - Museums
      - Open Data
      - Cultural Heritage
      - Science
      - JSONAPI
    properties:
      - type: Documentation
        url: https://www.sciencemuseumgroup.org.uk/our-work/our-collection/using-our-collection-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/science-museum-group/refs/heads/main/openapi/science-museum-group-collection-openapi.yml
      - type: GitHub Repository
        url: https://github.com/TheScienceMuseum/collectionsonline-api
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/science-museum-group/refs/heads/main/rules/science-museum-group-rules.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/science-museum-group/refs/heads/main/capabilities/collection-discovery.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/science-museum-group/refs/heads/main/json-schema/science-museum-group-collection-object-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/science-museum-group/refs/heads/main/json-ld/science-museum-group-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/science-museum-group/refs/heads/main/vocabulary/science-museum-group-vocabulary.yml
common:
  - type: GitHub Organization
    url: https://github.com/TheScienceMuseum
  - type: Website
    url: https://www.sciencemuseumgroup.org.uk/
  - type: Collections Portal
    url: https://collection.sciencemuseumgroup.org.uk
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
