---
aid: digital-ocean
name: Digital Ocean
description: DigitalOcean Holdings, Inc. is an American multinational technology company and cloud service provider. The company is headquartered in New York City, New York, US, with 15 globally distributed data centers. DigitalOcean provides developers, startups, and SMBs with cloud infrastructure-as-a-service platforms.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/digital-ocean/refs/heads/main/apis.yml
created: '2024-03-30'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
position: Consumer
access: 3rd-Party
tags:
  - Cloud
  - Compute
  - Servers
  - Infrastructure
apis:
  - aid: digital-ocean:digital-ocean-api
    name: Digital Ocean API
    tags:
      - Cloud
      - Compute
      - Servers
      - Infrastructure
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.digitalocean.com/v2
    humanURL: https://docs.digitalocean.com/reference/api/api-reference/
    properties:
      - url: https://docs.digitalocean.com/reference/api/api-reference/
        type: Documentation
      - url: openapi/digital-ocean-openapi-original.yml
        type: OpenAPI
      - url: https://github.com/digitalocean/openapi
        type: SourceCode
    description: The DigitalOcean API lets you programmatically manage your Droplets and other resources using conventional HTTP requests. Any action that you can perform through the DigitalOcean Control Panel (except for creating personal access tokens) can also be performed with the API. Resources include Droplets, Kubernetes, Apps, Databases, Spaces, Volumes, Load Balancers, Networking, Functions, Container Registry, Monitoring, and Billing.
common:
  - type: Documentation
    url: https://docs.digitalocean.com/
  - type: Support
    url: https://docs.digitalocean.com/support/
  - type: Developer
    url: https://docs.digitalocean.com/developer-center/
  - type: Blog
    url: https://blog.digitalocean.com/
  - type: Pricing
    url: https://www.digitalocean.com/pricing
  - type: GitHub
    url: https://github.com/digitalocean
  - type: PrivacyPolicy
    url: https://www.digitalocean.com/legal/privacy-policy
  - type: Status
    url: https://status.digitalocean.com/
  - type: TermsOfService
    url: https://www.digitalocean.com/legal/terms-of-service-agreement
  - type: Tutorials
    url: https://www.digitalocean.com/community
  - type: OpenSource
    url: https://docs.digitalocean.com/reference/opensource/
  - type: Libraries
    url: https://docs.digitalocean.com/reference/libraries/
  - type: Ideas
    url: https://ideas.digitalocean.com/documentation
  - type: SignUp
    url: https://cloud.digitalocean.com/registrations/new
  - type: Login
    url: https://cloud.digitalocean.com/login
maintainers:
  - FN: Kin Lane
    url: https://apievangelist.com
    email: kin@apievangelist.com
---
