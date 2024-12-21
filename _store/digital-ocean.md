---
aid: digital-ocean
url: >-
  https://raw.githubusercontent.com/api-search/cloud/main/_apis/digital-ocean/apis.md
apis:
  - aid: digital-ocean:digital-ocean-api
    name: Digital Ocean API
    tags:
      - Servers
      - Cloud
      - Compute
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://docs.digitalocean.com/
    overlays:
      - url: overlays/digital-ocean-openapi-search.yml
        type: APIs.io Search
    properties:
      - url: https://docs.digitalocean.com/
        type: Documentation
      - url: properties/digital-ocean-openapi-original.yml
        type: OpenAPI
    description: >
      The DigitalOcean API lets you programmatically manage your Droplets and
      other resources using conventional HTTP requests. Any action that you can
      perform through the DigitalOcean Control Panel (except for creating
      personal access tokens) can also be performed with the API.
name: Digital Ocean
tags:
  - Servers
  - Cloud
  - Compute
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://docs.digitalocean.com/support/
    type: Support
  - url: https://docs.digitalocean.com/developer-center/
    type: Developer
  - url: https://blog.digitalocean.com/
    type: Blog
  - url: https://www.digitalocean.com/pricing
    type: Pricing
  - url: https://github.com/digitalocean
    type: Github Organization
  - url: https://www.digitalocean.com/legal/privacy-policy
    type: Privacy Policy
  - url: https://status.digitalocean.com/
    type: Status
  - url: https://www.digitalocean.com/legal/terms-of-service-agreement
    type: Terms of Service
  - url: https://www.digitalocean.com/community
    type: Tutorials
  - url: https://docs.digitalocean.com/reference/opensource/
    type: Open Source
  - url: https://docs.digitalocean.com/reference/libraries/
    type: Libraries
  - url: https://ideas.digitalocean.com/documentation
    type: Ideas
  - url: https://cloud.digitalocean.com/registrations/new
    type: Sign Up
  - url: https://cloud.digitalocean.com/login
    type: Login
created: 2024/03/30
modified: 2024/03/30
overlays:
  - url: overlays/apis-io-search.yml
    type: APIs.io Search
description: >
  DigitalOcean Holdings, Inc. is an American multinational technology company
  and cloud service provider. The company is headquartered in New York City, New
  York, US, with 15 globally distributed data centers. DigitalOcean provides
  developers, startups, and SMBs with cloud infrastructure-as-a-service
  platforms. 
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'
slug: digital-ocean
---