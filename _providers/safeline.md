---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Safeline Agentic Access
  operation_count: 30
  slug: safeline-agentic-access
  summary_line: 30 operations · 18 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: 'SafeLine provides two MCP (Model Context Protocol) Server implementations for AI-assisted WAF management: a Python MCP Server for tool-based API management and a Go MCP Server for high-performance man'
  name: SafeLine MCP Server
  slug: mcp-server
- description: Access control list rules for blocking and allowing traffic
  name: SafeLine ACL Rules API
  slug: safeline-acl-rules-api
- description: Login and session management
  name: SafeLine Authentication API
  slug: safeline-authentication-api
- description: Security report generation and retrieval
  name: SafeLine Reports API
  slug: safeline-reports-api
- description: Security policy and rule group management
  name: SafeLine Security Policies API
  slug: safeline-security-policies-api
- description: SSL/TLS certificate management
  name: SafeLine SSL Certificates API
  slug: safeline-ssl-certificates-api
- description: System configuration and administration
  name: SafeLine System API
  slug: safeline-system-api
- description: User account and permission management
  name: SafeLine Users API
  slug: safeline-users-api
- description: Protected website (application) management
  name: SafeLine Websites API
  slug: safeline-websites-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SafeLine Management ACL Rules API
  slug: open-safeline-acl-rules-api
- collection_type: open
  name: SafeLine Management ACL Rules Authentication API
  slug: open-safeline-authentication-api
- collection_type: open
  name: SafeLine Management API
  slug: open-safeline-management
- collection_type: open
  name: SafeLine Management ACL Rules Reports API
  slug: open-safeline-reports-api
- collection_type: open
  name: SafeLine Management ACL Rules Security Policies API
  slug: open-safeline-security-policies-api
- collection_type: open
  name: SafeLine Management ACL Rules SSL Certificates API
  slug: open-safeline-ssl-certificates-api
- collection_type: open
  name: SafeLine Management ACL Rules System API
  slug: open-safeline-system-api
- collection_type: open
  name: SafeLine Management ACL Rules Users API
  slug: open-safeline-users-api
- collection_type: open
  name: SafeLine Management ACL Rules Websites API
  slug: open-safeline-websites-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/chaitin/SafeLine/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/safeline-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/safeline-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/safeline-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://waf.chaitin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.waf.chaitin.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chaitin/SafeLine
- group: start
  title: ''
  type: Demo
  url: https://demo.waf.chaitin.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/safeline-management-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/safeline-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/safeline-website-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/safeline-acl-rule-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/safeline-website-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/safeline-acl-rule-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/safeline-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/safeline-vocabulary.yml
created: '2026-03-27'
description: SafeLine is an open-source self-hosted Web Application Firewall (WAF) and reverse proxy developed by Chaitin Technology that protects web applications and APIs from attacks including SQL injection, XSS, code injection, OS command injection, SSRF, path traversal, and RCE. With over 180,000 installations protecting more than 1 million websites, SafeLine handles over 30 billion HTTP requests daily. It provides rate limiting, anti-bot defenses, dynamic code protection, and integrates with API gateways including Apache APISIX and Kong. SafeLine exposes a management API on port 9443 and supports MCP server implementations for AI-assisted management.
examples:
- key_count: 2
  name: Safeline Create Acl Rule Example
  slug: safeline-create-acl-rule-example
- key_count: 2
  name: Safeline Get Acl Execution Logs Example
  slug: safeline-get-acl-execution-logs-example
- key_count: 2
  name: Safeline List Websites Example
  slug: safeline-list-websites-example
finops:
- name: Safeline Finops
  service_category: API
  slug: safeline-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/safeline.png
json_schemas:
- name: SafeLine ACL Rule
  property_count: 6
  slug: safeline-acl-rule
- name: SafeLine Protected Website
  property_count: 9
  slug: safeline-website
json_structures:
- name: Safeline Acl Rule Structure
  property_count: 0
  slug: safeline-acl-rule-structure
- name: Safeline Website Structure
  property_count: 0
  slug: safeline-website-structure
jsonld:
- class_count: 26
  name: Safeline Context
  property_count: 0
  slug: safeline-context
layout: provider
modified: '2026-05-19'
name: SafeLine
nav: Providers
network: true
overview: 'SafeLine publishes 8 APIs on the [APIs.io](https://apis.io/) network, including ACL Rules API, Authentication API, Reports API, and 5 more. Tagged areas include Proxy, WAF, Security, Open-Source, and Reverse Proxy.


  The SafeLine catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SafeLine''s developer surface includes authentication, documentation, and 14 more developer resources.'
plans:
- name: Safeline Plans Pricing
  plan_count: 3
  slug: safeline-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Safeline Rate Limits
  slug: safeline-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SafeLine API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: safeline-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: SafeLine API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 3
  slug: safeline-rules
score:
  band: thin
  composite: 34.4
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 62.6
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/safeline/refs/heads/main/screenshots/safeline-2026-06-20T193323.png
security:
- kind: authentication
  name: Safeline Authentication
  slug: safeline-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Safeline Domain Security
  slug: safeline-domain-security
  summary_line: TLSv1.3 · DMARC
slug: safeline
tags:
- Proxy
- WAF
- Security
- Open-Source
- Reverse Proxy
- API Gateway
website: https://waf.chaitin.com/
---
