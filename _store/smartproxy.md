---
aid: smartproxy
name: Smartproxy
description: Smartproxy (now also known as Decodo) is a proxy network and web scraping infrastructure platform providing residential, datacenter, mobile, and ISP proxies for web data collection at scale. The Smartproxy API enables programmatic management of proxy accounts, sub-users, traffic allocation, IP whitelisting, and endpoint discovery. The platform supports both rotating and sticky session proxy connections across global geographic locations.
url: https://raw.githubusercontent.com/api-evangelist/smartproxy/refs/heads/main/apis.yml
created: '2026-03-29'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Proxies
  - Web Scraping
  - Data Collection
  - Residential Proxies
  - Datacenter Proxies
  - Mobile Proxies
  - Network Infrastructure
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
apis:
  - aid: smartproxy:proxy-management-api
    name: Smartproxy Account Management API
    description: 'The Smartproxy API provides programmatic access to manage proxy sub-users, monitor traffic consumption, configure IP whitelisting, check subscription status, and discover available proxy endpoints. Base URL: https://api.decodo.com/v1. Authentication via API key token in the Authorization header obtained from the /auth endpoint.'
    humanURL: https://smartproxy.com/
    tags:
      - Proxy Management
      - Sub-Users
      - Traffic Management
      - Account Management
    properties:
      - type: Documentation
        url: https://help.smartproxy.com/reference/introduction-1
      - type: GettingStarted
        url: https://help.smartproxy.com/docs/quick-start-1
      - type: OpenAPI
        url: openapi/smartproxy-openapi.yml
      - type: GitHubRepository
        url: https://github.com/Smartproxy/Smartproxy-API
common:
  - type: Website
    url: https://smartproxy.com/
  - type: Documentation
    url: https://help.smartproxy.com/reference/introduction-1
  - type: GitHubOrganization
    url: https://github.com/Smartproxy
  - type: Pricing
    url: https://smartproxy.com/proxies/residential-proxies
  - type: OpenAPI
    url: openapi/smartproxy-openapi.yml
  - type: Spectral
    url: rules/smartproxy-rules.yml
  - type: Capabilities
    url: capabilities/proxy-account-management.yaml
  - type: JSONSchema
    url: json-schema/smartproxy-sub-user-schema.json
  - type: JSONSchema
    url: json-schema/smartproxy-endpoint-schema.json
  - type: JSONStructure
    url: json-structure/smartproxy-structure.json
  - type: JSONLD
    url: json-ld/smartproxy-context.jsonld
  - type: Vocabulary
    url: vocabulary/smartproxy-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
