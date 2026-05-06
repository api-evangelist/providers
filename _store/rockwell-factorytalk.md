---
aid: rockwell-factorytalk
url: https://raw.githubusercontent.com/api-evangelist/rockwell-factorytalk/refs/heads/main/apis.yml
apis:
  - aid: rockwell-factorytalk:factorytalk-optix-rest-api
    name: Rockwell FactoryTalk Optix REST API
    tags:
      - Automation
      - HMI
      - Manufacturing
      - REST
    image: https://raw.githubusercontent.com/api-evangelist/rockwell-factorytalk/refs/heads/main/image.png
    humanURL: https://docs.rockwellautomation.com/en/products/software/factorytalk/factorytalk-optix.html
    baseURL: https://api.factorytalk.example.com
    properties:
      - url: https://docs.rockwellautomation.com/en/products/software/factorytalk/factorytalk-optix.html
        type: Documentation
      - url: openapi/rockwell-factorytalk-optix-openapi.yml
        type: OpenAPI
    description: Rockwell Automation FactoryTalk Optix REST API provides programmatic access to HMI and SCADA visualization applications, enabling external system integration, tag read/write, alarm management, and runtime control of FactoryTalk Optix applications.
  - aid: rockwell-factorytalk:factorytalk-hub-api
    name: Rockwell FactoryTalk Hub API
    tags:
      - Automation
      - Cloud
      - Manufacturing
      - REST
    image: https://raw.githubusercontent.com/api-evangelist/rockwell-factorytalk/refs/heads/main/image.png
    humanURL: https://www.rockwellautomation.com/en-us/products/software/factorytalk.html
    baseURL: https://api.factorytalk.example.com
    properties:
      - url: https://www.rockwellautomation.com/en-us/products/software/factorytalk.html
        type: Documentation
      - url: asyncapi/rockwell-factorytalk-realtime-asyncapi.yml
        type: AsyncAPI
    description: Rockwell FactoryTalk Hub provides cloud-based industrial API services for connecting FactoryTalk software applications, enabling centralized identity management, software licensing, and connected factory services.
  - aid: rockwell-factorytalk:logix-designer-api
    name: Rockwell FactoryTalk Logix Designer API
    tags:
      - Automation
      - Manufacturing
      - PLC
      - Programming
      - REST
    image: https://raw.githubusercontent.com/api-evangelist/rockwell-factorytalk/refs/heads/main/image.png
    humanURL: https://github.com/rockwellautomation/ra-logix-designer-vcs-custom-tools
    baseURL: https://api.factorytalk.example.com
    properties:
      - url: https://github.com/rockwellautomation/ra-logix-designer-vcs-custom-tools
        type: Documentation
      - url: https://github.com/rockwellautomation/ra-logix-cicd
        type: SDKs
    description: Rockwell Automation FactoryTalk Logix Designer provides programmatic access to Logix controller programming, allowing version control integration, CI/CD pipeline automation, and export of L5X controller files for PLC program management.
common:
  - url: https://www.rockwellautomation.com/en-us/products/software/factorytalk.html
    type: Portal
  - url: https://docs.rockwellautomation.com/en/products/software/factorytalk/
    type: Documentation
  - url: https://www.rockwellautomation.com/en-us/
    type: Website
  - url: https://www.rockwellautomation.com/en-us/support/
    type: Support
  - url: https://www.rockwellautomation.com/en-us/company/news/blogs/
    type: Blog
  - url: https://www.rockwellautomation.com/en-us/company/about-us/legal-notices/privacy-and-cookies-policy.html
    type: PrivacyPolicy
  - url: https://github.com/rockwellautomation
    type: GitHubOrganization
  - url: openapi/rockwell-factorytalk-optix-openapi.yml
    type: OpenAPI
  - url: asyncapi/rockwell-factorytalk-realtime-asyncapi.yml
    type: AsyncAPI
  - url: json-schema/rockwell-factorytalk-tag-schema.json
    type: JSONSchema
  - url: json-ld/rockwell-factorytalk-context.jsonld
    type: JSONLDContext
  - url: json-structure/rockwell-factorytalk-structure.json
    type: JSONStructure
  - url: vocabulary/rockwell-factorytalk-vocabulary.yml
    type: Vocabulary
  - url: rules/rockwell-factorytalk-rules.yml
    type: SpectralRuleset
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
modified: '2026-05-02'
description: Rockwell FactoryTalk is a portfolio of software products by Rockwell Automation that supports the design, operation, and maintenance of industrial control systems and connected manufacturing operations.
---
