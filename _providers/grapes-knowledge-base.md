---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Grapes Knowledge Base Agentic Access
  operation_count: 8
  slug: grapes-knowledge-base-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.data-grapes.com
  baseurl_source: spec
  description: Configure Grapes agents
  name: Grapes Knowledge Base Agents API
  slug: grapes-knowledge-base-agents-api
- baseURL: https://api.data-grapes.com
  baseurl_source: spec
  description: Import and export datasets
  name: Grapes Knowledge Base Datasets API
  slug: grapes-knowledge-base-datasets-api
- baseURL: https://api.data-grapes.com
  baseurl_source: spec
  description: Create and customize Grapes projects
  name: Grapes Knowledge Base Projects API
  slug: grapes-knowledge-base-projects-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Grapes Knowledge Base Agents API
  slug: open-grapes-knowledge-base-agents-api
- collection_type: open
  name: Grapes Knowledge Base Agents Datasets API
  slug: open-grapes-knowledge-base-datasets-api
- collection_type: open
  name: Grapes Knowledge Base Agents Projects API
  slug: open-grapes-knowledge-base-projects-api
- collection_type: open
  name: Grapes Knowledge Base API
  slug: open-grapes-knowledge-base
common:
- group: company
  title: ''
  type: Website
  url: https://data-grapes.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/grapes-knowledge-base-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grapes-knowledge-base-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/grapes-knowledge-base-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.data-grapes.com/en/
- group: docs
  title: ''
  type: DeveloperDocs
  url: https://docs.data-grapes.com/en/docs/developer-docs/
- group: docs
  title: ''
  type: UserGuide
  url: https://docs.data-grapes.com/en/docs/user-guide/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/grapes-knowledge-base-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/grapes-knowledge-base-project-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/grapes-knowledge-base-context.jsonld
- group: design
  title: ''
  type: Rules
  url: grapes-knowledge-base-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://data-grapes.com/articles/
created: '2025-02-24'
description: Grapes is a knowledge management platform with administrative, configuration, and project management capabilities. The Grapes API allows automation of recurring operations including project administration, agent configuration, and dataset import/export. Documentation is available in English and French.
finops:
- name: Grapes Knowledge Base Finops
  service_category: API
  slug: grapes-knowledge-base-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grapes-knowledge-base.png
json_schemas:
- name: Grapes Project
  property_count: 6
  slug: grapes-knowledge-base-project
jsonld:
- class_count: 9
  name: Grapes Knowledge Base Context
  property_count: 2
  slug: grapes-knowledge-base-context
layout: provider
modified: '2026-05-19'
name: Grapes Knowledge Base
nav: Providers
network: true
overview: 'Grapes Knowledge Base publishes 3 APIs on the [APIs.io](https://apis.io/) network: Agents API, Datasets API, and Projects API. Tagged areas include Knowledge-Management, Knowledge Base, Data Management, Automation, and HATEOAS.


  The Grapes Knowledge Base catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Grapes Knowledge Base''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Grapes Knowledge Base Plans Pricing
  plan_count: 3
  slug: grapes-knowledge-base-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Grapes Knowledge Base Rate Limits
  slug: grapes-knowledge-base-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Grapes Knowledge Base API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: grapes-knowledge-base-jsonschema-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/grapes-knowledge-base/refs/heads/main/screenshots/grapes-knowledge-base-2026-06-20T182323.png
security:
- kind: authentication
  name: Grapes Knowledge Base Authentication
  slug: grapes-knowledge-base-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Grapes Knowledge Base Domain Security
  slug: grapes-knowledge-base-domain-security
  summary_line: TLSv1.3 · HSTS
slug: grapes-knowledge-base
tags:
- Knowledge-Management
- Knowledge Base
- Data Management
- Automation
- HATEOAS
website: https://data-grapes.com/
---
