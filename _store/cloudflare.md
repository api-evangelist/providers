---
aid: cloudflare
url: >-
  https://raw.githubusercontent.com/api-search/infrastructure/main/_apis/cloudflare/apis.md
apis:
  - aid: cloudflare:cloudflare-api
    name: Cloudflare API
    tags: []
    baseURL: https://api.cloudflare.com
    contact:
      - FN: Support
        url: https://support.cloudflare.com/
        email: ''
    humanURL: https://developers.cloudflare.com/api/
    description: >-
      Easily integrate with Cloudflare's products and services using the
      Cloudflare API. Authentication is essential when utilizing the API to
      ensure proper authorization and access control. Generate an API token to
      enable performing various actions with the API.
  - aid: cloudflare:cloudflare-accounts-api
    name: Cloudflare Accounts API
    tags:
      - DNS
    humanURL: https://developers.cloudflare.com/api/operations/accounts-list-accounts
    properties:
      - url: openapi/cloudflare-accounts--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developers.cloudflare.com/api/operations/accounts-list-accounts
        type: Documentation
    description: Managing all the details of your Cloudflare Account using the API.
  - aid: cloudflare:cloudflare-certificates-api
    name: Cloudflare Certificates API
    tags:
      - Certificates
    humanURL: https://developers.cloudflare.com/api/
    properties:
      - url: openapi/cloudflare-certificates--openapi-original.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/api/
        type: Documentation
    description: Managing certificates used across Cloudflare.
  - aid: cloudflare:cloudflare-ip-addresses-api
    name: Cloudflare IP Addresses API
    tags:
      - IP Addresses
    humanURL: >-
      https://developers.cloudflare.com/api/operations/ip-access-rules-for-a-user-list-ip-access-rules
    properties:
      - url: openapi/cloudflare-ips--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developers.cloudflare.com/api/operations/ip-access-rules-for-a-user-list-ip-access-rules
        type: Documentation
    description: >-
      Provides the ability to manage IP addresses used across a Cloudflare
      account.
  - aid: cloudflare:cloudflare-memberships-api
    name: Cloudflare Memberships API
    tags:
      - Memberships
      - Details
    humanURL: >-
      https://developers.cloudflare.com/api/operations/user'-s-account-memberships-list-memberships
    properties:
      - url: openapi/cloudflare-memberships--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developers.cloudflare.com/api/operations/user'-s-account-memberships-list-memberships
        type: Documentation
    description: Provides the ability to manage memberships across accounts.
  - aid: cloudflare:cloudflare-radar-api
    name: Cloudflare Radar API
    tags:
      - Radar
    humanURL: https://developers.cloudflare.com/api/operations/radar-get-search-global
    properties:
      - url: openapi/cloudflare-radar--openapi-original.yml
        type: OpenAPI
      - url: >-
          https://developers.cloudflare.com/api/operations/radar-get-search-global
        type: Documentation
    description: Provides the ability to access all of Cloudflare's radar capabilities.
  - aid: cloudflare:cloudflare-user-api
    name: Cloudflare User API
    tags:
      - Users
    humanURL: https://developers.cloudflare.com/api/operations/user-user-details
    properties:
      - url: openapi/cloudflare-user--openapi-original.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/api/operations/user-user-details
        type: Documentation
    description: >-
      Provides the ability to manage all of the users across a Cloudflare
      account.
  - aid: cloudflare:cloudflare-zones-api
    name: Cloudflare Zones API
    tags:
      - DNS
      - Zones
    humanURL: https://developers.cloudflare.com/api/operations/zones-get
    properties:
      - url: openapi/cloudflare-zones--openapi-original.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/api/operations/zones-get
        type: Documentation
    description: Provides the ability to manage DNS Zones across the Cloudflare platform.
name: Cloudflare
tags:
  - DNS
  - Cloud
  - Edge
  - Platform
  - API Gateway
  - AI Gateway
type: Contract
access: 3rd-Party
created: 2024/04/14
modified: '2025-08-19'
position: Consuming
description: >-
  Cloudflare is a U.S.-based company that provides a suite of services aimed at
  enhancing the security, performance, and reliability of internet properties.
  Its offerings include content delivery network (CDN) services, DDoS
  mitigation, internet security, and distributed domain name server (DNS)
  services. 
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'

---