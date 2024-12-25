---
---
aid: api-evangelist-rules
specificationVersion: '0.18'

type: Rule

name: API Evangelist Rules
description: This is the API rule for the API Evangelist rules API, inventorying all of the APIs managed through the platform.

image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png

tags:

  - Rules

created: '2024-10-14'
modified: '2024-10-14'  

url: https://github.com/api-evangelist/rules/blob/main/apis.yml

apis:

  - aid: api-evangelist-rules:rules
    name: API Evangelist Rules API
    description: This is the API rule for the API Evangelist rules API, inventorying all of the APIs managed through the platform.
    image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-logos/api-evangelist-butterfly-vertical.png
    humanURL: https://developer.apievangelist.com/rules/
    baseURL: https://rules-api.api-evangelist.com/
    
    tags:
    
      - Rules
    
    properties:

      # Source of Truth
      - type: GitHubRepository
        url: https://github.com/api-evangelist/rules    
      
      # Pipeline
      - type: GitHubActions
        url: https://github.com/api-evangelist/rules/blob/main/.github/workflows/pipeline.yml        

      # Human Readable Documentation
      - type: Documentation
        url: https://developer.apievangelist.com/documentation/

      # Technical Rule
      - type: OpenAPI
        url: https://github.com/api-evangelist/rules/blob/main/openapi.yml

    contact:

      - FN: APIs.io
        email: info@apievangelist.com 

common:

  # Workspaces
  - type: GitHubOrganization
    url: https://github.com/api-evangelist/ 
                       
# Who Is Responsible for this Rule
maintainers:

  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane---