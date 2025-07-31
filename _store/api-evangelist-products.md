---
---
aid: api-evangelist-products
name: Products
type: Template
description: |-
  This is a template APIs.json for a products API, to be used in storytelling, training, and knowledge bases.

image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
- Application Programming Interface
- API
- Products

created: '2024-12-29'
modified: '2024-12-29'

url: http://example.com/apis.json
specificationVersion: '0.19'
apis:

  - aid: api-evangelist-products:products-api
    name: Products API.
    description: A demo products API.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://example.com/apis.yml
    baseURL: http://apis.example.com
    tags:
      - API
      - Application Programming Interface
      - Products
    properties:
      - type: Documentation
        url: http://example.com/documentation
      - type: OpenAPI
        url: openapi/products-api-openapi.yml
      - type: Authentication
        url: http://example.com/authentication
      - type: GettingStarted
        url: http://example.com/getting-started
      - type: ChangeLog
        url: http://example.com/change-log 
    contact:
      - FN: API Evangelist
        email: info@apievangelist.com

common:

  - type: Website
    url: http://apievangelist.com

  # APIOps Canvases - https://canvascreator.apiopscycles.com/

  # APIOps Business Model Canvas - https://www.apiopscycles.com/resources/api-business-model-canvas
  - type: APIOpsBusinessModelCanvas
    url:  canvases/Canvas_apiBusinessModelCanvas_en-US.json

  # APIOps Value Proposition Canvas - https://www.apiopscycles.com/resources/api-value-proposition-canvas
  - type: APIOpsValuePropositionCanvas
    url:  canvases/Canvas_apiValuePropositionCanvas_en-US.json
  
  # APIOps Business Impact Canvas - https://www.apiopscycles.com/resources/business-impact-canvas
  - type: APIOpsBusinessImpactCanvas
    url:  canvases/Canvas_businessImpactCanvas_en-US.json

  # APIOps Capacity Canvas - https://www.apiopscycles.com/resources/capacity-canvas     
  - type: APIOpsCapacityCanvas
    url:  canvases/Canvas_capacityCanvas_en-US.json

  # APIOps Customer Journey Canvas - https://www.apiopscycles.com/resources/customer-journey-canvas
  - type: APIOpsCustomerJourneyCanvas
    url:  canvases/Canvas_customerJourneyCanvas_en-US.json

  # APIOps Domain Canvas - https://www.apiopscycles.com/resources/domain-canvas
  - type: APIOpsDomainCanvas
    url:  canvases/Canvas_domainCanvas_en-US.json

  # APIOps Event Canvas - No Page to Link To
  - type: APIOpsEventCanvas
    url:  canvases/Canvas_eventCanvas_en-US.json

  # APIOps Interaction Canvas - https://www.apiopscycles.com/resources/interaction-canvas 
  - type: APIOpsInteractionCanvas
    url:  canvases/Canvas_interactionCanvas_en-US.json

  # APIOps Locations Canvas - https://www.apiopscycles.com/resources/locations-canvas
  - type: APIOpsLocationsCanvas
    url:  canvases/Canvas_locationsCanvas_en-US.json

  # APIOps Rest Canvas - https://www.apiopscycles.com/resources/rest-api-design-guide
  - type: APIOpsRestCanvas
    url:  canvases/Canvas_restCanvas_en-US.json

maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com---