---
aid: netbox
name: NetBox
description: NetBox is the leading solution for modeling and documenting modern networks. By combining the traditional disciplines of IP address management (IPAM) and datacenter infrastructure management (DCIM) with powerful APIs and extensions, NetBox provides the ideal "source of truth" to power network automation.
image: https://netbox.dev/static/img/netbox-logo.svg
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/netbox/refs/heads/main/apis.yml
apis:
  - aid: netbox:netbox-rest
    name: NetBox REST API
    description: A comprehensive REST API for programmatic access to all NetBox data and functionality. Supports full CRUD operations for all objects including devices, IP addresses, circuits, and more.
    image: https://netbox.dev/static/img/netbox-logo.svg
    humanURL: https://docs.netbox.dev/en/stable/
    baseURL: https://demo.netbox.dev/api
    tags:
      - Automation
      - DCIM
      - Documentation
      - Infrastructure
      - IPAM
      - Network Management
    properties:
      - type: Documentation
        url: https://docs.netbox.dev/en/stable/integrations/rest-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/netbox/refs/heads/main/openapi/netbox-openapi.yml
      - type: Authentication
        url: https://docs.netbox.dev/en/stable/integrations/rest-api/#authentication
    contact:
      - type: Email
        url: mailto:info@netbox.dev
      - type: GitHub
        url: https://github.com/netbox-community/netbox
  - name: NetBox GraphQL API
    description: A GraphQL API providing flexible querying capabilities for NetBox data with support for nested queries and custom field selection.
    image: https://netbox.dev/static/img/netbox-logo.svg
    humanURL: https://docs.netbox.dev/en/stable/integrations/graphql-api/
    baseURL: https://demo.netbox.dev/graphql
    tags:
      - DCIM
      - GraphQL
      - IPAM
      - Query Language
    properties:
      - type: Documentation
        url: https://docs.netbox.dev/en/stable/integrations/graphql-api/
      - type: GraphiQL Interface
        url: https://demo.netbox.dev/graphql
common:
  - type: GitHub Organization
    url: https://github.com/netbox-community
  - type: Slack Community
    url: https://netdev.chat/
  - type: Blog
    url: https://netbox.dev/blog/
  - type: Getting Started
    url: https://docs.netbox.dev/en/stable/getting-started/
  - type: Plugins
    url: https://netbox.dev/plugins/
  - type: Demo Instance
    url: https://demo.netbox.dev/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Data Center
  - DCIM
  - Infrastructure as Code
  - IPAM
  - Network Automation
  - Network Management
  - Open Source
  - Source of Truth
---
