---
aid: quorum
name: Quorum Software
description: Quorum Software is a leading provider of energy software for upstream oil and gas operations, providing solutions for land management, royalty accounting, production reporting, and operational data management.
type: Index
image: https://www.quorumsoftware.com/hubfs/quorum-logo.svg
url: https://raw.githubusercontent.com/api-evangelist/quorum/refs/heads/main/apis.yml
tags:
  - Energy
  - Oil & Gas
  - Upstream
  - Land Management
  - Royalty Accounting
  - Production Reporting
created: '2026-03-18'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: quorum:quorum-land-management-api
    name: Quorum Land Management API
    description: Quorum Land Management API provides access to land records, lease management, tract data, and division order information for upstream oil and gas exploration and production companies.
    humanURL: https://www.quorumsoftware.com/
    baseURL: https://api.quorumsoftware.com/v1
    tags:
      - Energy
      - Oil & Gas
      - Upstream
      - Land
      - REST
    properties:
      - type: Documentation
        url: https://www.quorumsoftware.com/
      - type: OpenAPI
        url: openapi/quorum-land-management-openapi.yml
      - type: JSONSchema
        url: json-schema/quorum-lease-schema.json
      - type: JSONLDContext
        url: json-ld/quorum-context.jsonld
  - aid: quorum:quorum-royalty-accounting-api
    name: Quorum Royalty Accounting API
    description: Quorum Royalty Accounting API enables access to royalty payment calculations, owner statements, suspense management, and title data for oil and gas mineral rights owners and operators.
    humanURL: https://www.quorumsoftware.com/
    tags:
      - Energy
      - Oil & Gas
      - Royalty
      - Accounting
      - REST
    properties:
      - type: Documentation
        url: https://www.quorumsoftware.com/
  - aid: quorum:quorum-production-reporting-api
    name: Quorum Production Reporting API
    description: Quorum Production Reporting API provides access to well production volumes, allocations, gas balancing, and regulatory reporting data for upstream oil and gas operations.
    humanURL: https://www.quorumsoftware.com/
    tags:
      - Energy
      - Oil & Gas
      - Production
      - Reporting
      - REST
    properties:
      - type: Documentation
        url: https://www.quorumsoftware.com/
common:
  - type: Portal
    url: https://www.quorumsoftware.com/
  - type: Website
    url: https://www.quorumsoftware.com/
  - type: Support
    url: https://community.quorumsoftware.com/s/login/
  - type: Blog
    url: https://resources.quorumsoftware.com/blog
  - type: PrivacyPolicy
    url: https://www.quorumsoftware.com/privacy-policy/
  - type: TermsOfService
    url: https://www.quorumsoftware.com/terms-and-conditions/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
