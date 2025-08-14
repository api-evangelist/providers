---
aid: api-evangelist-products
url: http://example.com/apis.json
apis:
  - aid: api-evangelist-products:products-api
    name: Products API.
    tags:
      - API
      - Application Programming Interface
      - Products
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: http://apis.example.com
    contact:
      - FN: API Evangelist
        email: info@apievangelist.com
    humanURL: https://example.com/apis.yml
    properties:
      - url: http://example.com/documentation
        type: Documentation
      - url: openapi/products-api-openapi.yml
        type: OpenAPI
      - url: http://example.com/authentication
        type: Authentication
      - url: http://example.com/getting-started
        type: GettingStarted
      - url: http://example.com/change-log
        type: ChangeLog
    description: A demo products API.
name: Products
tags:
  - Application Programming Interface
  - API
  - Products
type: Template
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: http://apievangelist.com
    type: Website
  - url: canvases/Canvas_apiBusinessModelCanvas_en-US.json
    type: APIOpsBusinessModelCanvas
  - url: canvases/Canvas_apiValuePropositionCanvas_en-US.json
    type: APIOpsValuePropositionCanvas
  - url: canvases/Canvas_businessImpactCanvas_en-US.json
    type: APIOpsBusinessImpactCanvas
  - url: canvases/Canvas_capacityCanvas_en-US.json
    type: APIOpsCapacityCanvas
  - url: canvases/Canvas_customerJourneyCanvas_en-US.json
    type: APIOpsCustomerJourneyCanvas
  - url: canvases/Canvas_domainCanvas_en-US.json
    type: APIOpsDomainCanvas
  - url: canvases/Canvas_eventCanvas_en-US.json
    type: APIOpsEventCanvas
  - url: canvases/Canvas_interactionCanvas_en-US.json
    type: APIOpsInteractionCanvas
  - url: canvases/Canvas_locationsCanvas_en-US.json
    type: APIOpsLocationsCanvas
  - url: canvases/Canvas_restCanvas_en-US.json
    type: APIOpsRestCanvas
created: '2024-12-29'
modified: '2024-12-29'
description: >-
  This is a template APIs.json for a products API, to be used in storytelling,
  training, and knowledge bases.
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
specificationVersion: '0.19'

---