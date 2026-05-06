---
aid: safeline
name: SafeLine
description: SafeLine is an open-source self-hosted Web Application Firewall (WAF) and reverse proxy developed by Chaitin Technology that protects web applications and APIs from attacks including SQL injection, XSS, code injection, OS command injection, SSRF, path traversal, and RCE. With over 180,000 installations protecting more than 1 million websites, SafeLine handles over 30 billion HTTP requests daily. It provides rate limiting, anti-bot defenses, dynamic code protection, and integrates with API gateways including Apache APISIX and Kong. SafeLine exposes a management API on port 9443 and supports MCP server implementations for AI-assisted management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Proxy
  - WAF
  - Security
  - Open Source
  - Reverse Proxy
  - API Gateway
url: https://raw.githubusercontent.com/api-evangelist/safeline/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: safeline:safeline
    name: SafeLine Management API
    description: SafeLine Management API provides programmatic control of the SafeLine WAF including application management, security rule configuration, attack event analysis, IP allowlist/blocklist management, and traffic monitoring. The management API is exposed on port 9443 and supports authentication via API tokens.
    humanURL: https://waf.chaitin.com/
    tags:
      - Proxy
      - WAF
      - Security
      - REST
      - Open Source
    properties:
      - type: Documentation
        url: https://docs.waf.chaitin.com/
      - type: Getting Started
        url: https://docs.waf.chaitin.com/en/getting-started
      - type: GitHubRepository
        url: https://github.com/chaitin/SafeLine
      - type: OpenAPI
        url: openapi/safeline-management-openapi.yml
  - aid: safeline:mcp-server
    name: SafeLine MCP Server
    description: 'SafeLine provides two MCP (Model Context Protocol) Server implementations for AI-assisted WAF management: a Python MCP Server for tool-based API management and a Go MCP Server for high-performance management. These servers expose tools for application management, security rule configuration, and attack event analysis.'
    humanURL: https://github.com/chaitin/SafeLine
    tags:
      - WAF
      - MCP
      - AI
      - Security
    properties:
      - type: GitHubRepository
        url: https://github.com/chaitin/SafeLine
common:
  - type: Website
    url: https://waf.chaitin.com/
  - type: Documentation
    url: https://docs.waf.chaitin.com/
  - type: GitHubOrganization
    url: https://github.com/chaitin/SafeLine
  - type: Demo
    url: https://demo.waf.chaitin.com/
  - type: OpenAPI
    url: openapi/safeline-management-openapi.yml
  - type: SpectralRules
    url: rules/safeline-rules.yml
  - type: JSONSchema
    url: json-schema/safeline-website-schema.json
  - type: JSONSchema
    url: json-schema/safeline-acl-rule-schema.json
  - type: JSONStructure
    url: json-structure/safeline-website-structure.json
  - type: JSONStructure
    url: json-structure/safeline-acl-rule-structure.json
  - type: JSONLDContext
    url: json-ld/safeline-context.jsonld
  - type: Vocabulary
    url: vocabulary/safeline-vocabulary.yml
  - type: Capabilities
    url: capabilities/waf-protection-management.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
