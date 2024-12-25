---
---
aid: api-evangelist-lifecycles
specificationVersion: '0.18'

type: Lifecycle

name: API Evangelist Lifecycles
description: This is the API lifecycle for the API Evangelist lifecycles API, inventorying all of the APIs managed through the platform.

image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png

tags:

  - Lifecycles

created: '2024-10-14'
modified: '2024-10-14'  

url: https://github.com/api-evangelist/lifecycles/blob/main/apis.yml

apis:

  - aid: api-evangelist-lifecycles:lifecycles
    name: API Evangelist Lifecycles API
    description: This is the API lifecycle for the API Evangelist lifecycles API, inventorying all of the APIs managed through the platform.
    image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
    humanURL: https://developer.apievangelist.com/lifecycles/
    baseURL: https://lifecycles-api.api-evangelist.com/
    
    tags:
    
      - Lifecycles
    
    properties:

      # Source of Truth
      - type: GitHubRepository
        url: https://github.com/api-evangelist/lifecycles    
      
      # Pipeline
      - type: GitHubActions
        url: https://github.com/api-evangelist/lifecycles/blob/main/.github/workflows/pipeline.yml        

      # Human Readable Documentation
      - type: Documentation
        url: https://developer.apievangelist.com/documentation/

      # Technical Lifecycle
      - type: OpenAPI
        url: https://github.com/api-evangelist/lifecycles/blob/main/openapi.yml

    contact:

      - FN: APIs.io
        email: info@apievangelist.com 

common:

  # Workspaces
  - type: GitHubOrganization
    url: https://github.com/api-evangelist/ 
                       
# Who Is Responsible for this Lifecycle
maintainers:

  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane---