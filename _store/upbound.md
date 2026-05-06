---
aid: upbound
name: Upbound
description: Upbound is a universal cloud platform built on Crossplane, providing managed control planes and a marketplace for cloud infrastructure APIs. The Upbound API enables programmatic management of organizations, spaces, control planes, package repositories, teams, and robot accounts.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Infrastructure
  - Crossplane
  - Developer Experience
  - Internal Developer Platform
  - Platform Engineering
url: https://raw.githubusercontent.com/api-evangelist/upbound/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: upbound:upbound
    name: Upbound API
    description: The Upbound API provides programmatic management of the Upbound universal cloud platform, including organizations, teams, managed Crossplane control planes, package repositories, and robot accounts for CI/CD automation.
    humanURL: https://www.upbound.io
    baseURL: https://api.upbound.io/v1
    tags:
      - Crossplane
      - Developer Experience
      - Internal Developer Platform
      - Control Planes
      - Organizations
    properties:
      - type: Documentation
        url: https://docs.upbound.io
      - type: Getting Started
        url: https://docs.upbound.io/quickstart
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/upbound/refs/heads/main/openapi/upbound-openapi.yml
common:
  - type: Website
    url: https://www.upbound.io
  - type: Documentation
    url: https://docs.upbound.io
  - type: GitHub Organization
    url: https://github.com/upbound
  - type: Marketplace
    url: https://marketplace.upbound.io
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
