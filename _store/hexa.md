---
aid: hexa
name: Hex
description: Hex is an AI analytics platform that enables teams to explore, analyze, and share data insights together. It provides agentic notebooks, conversational self-serve analytics, data apps, dashboards, and a Context Studio for semantic modeling and data governance, integrating with major data warehouses such as Snowflake, BigQuery, Databricks, and Redshift.
url: https://raw.githubusercontent.com/api-evangelist/hexa/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Collaboration
  - Data
  - Notebooks
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hexa:hex-api
    name: Hex API
    description: The Hex API provides programmatic access to projects, project runs, data connections, collections, sharing, groups, and users on the Hex collaborative analytics platform.
    humanURL: https://learn.hex.tech/docs/api/api-reference
    baseURL: https://app.hex.tech/api/v1
    tags:
      - Analytics
      - Notebooks
      - Projects
    properties:
      - type: Documentation
        url: https://learn.hex.tech/docs/api/api-reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/hexa/refs/heads/main/openapi/hexa-openapi.yml
common:
  - type: Website
    url: https://hex.tech/
  - type: Documentation
    url: https://learn.hex.tech/
  - type: Pricing
    url: https://hex.tech/pricing/
  - type: Sign Up
    url: https://app.hex.tech/signup
  - type: Login
    url: https://app.hex.tech/login
  - type: Blog
    url: https://hex.tech/blog/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
