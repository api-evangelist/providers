---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: REST API for business entity verification. 21 operations across 20 paths covering verification submission and job status, entity lookup and history, jurisdiction discovery, account and credit manageme
  name: BizVerify API
  slug: bizverify-api
- description: Hosted MCP server over Streamable HTTP exposing nine tools — get_config, list_jurisdictions, verify_business, search_entities, check_job_status, get_entity, get_entity_history, get_account and purchas
  name: BizVerify MCP Server
  slug: bizverify-mcp-server
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://bizverify.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bizverify.co
- group: agent
  title: ''
  type: LLMSTxt
  url: llms/bizverify-llms.txt
- group: agent
  title: ''
  type: LLMSTxt
  url: https://bizverify.co/llms.txt
- group: other
  title: ''
  type: APICatalog
  url: well-known/bizverify-api-catalog.json
- group: other
  title: ''
  type: APICatalog
  url: https://bizverify.co/.well-known/api-catalog
- group: agent
  title: ''
  type: AgentSkills
  url: https://api.bizverify.co/tools/openai.json
- group: agent
  title: ''
  type: AgentSkills
  url: https://api.bizverify.co/tools/anthropic.json
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bizverify.co/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bizverify.co/terms
created: '2026-08-02'
description: 'BizVerify is a business entity verification (KYB) API built for AI agents as much as for developers. It confirms business registrations, status, good standing and available public company details across supported US and international jurisdictions, through a REST API and a hosted MCP server that exposes the same capability as nine tools. The agent surface is the unusual part for a provider this size: alongside the OpenAPI it publishes an llms.txt, a proper RFC 9727 API catalog served as application/linkset+json, per-vendor tool manifests at /tools/openai.json and /tools/anthropic.json, and an open-source MCP client repository. Access is credit-based with a free-tier allowance, and the MCP server answers tools/list without credentials.'
layout: provider
modified: '2026-08-02'
name: BizVerify
nav: Providers
network: true
overview: 'BizVerify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business Verification, KYB, Know Your Business, Entity Verification, and Compliance.


  BizVerify''s developer surface includes documentation and 9 more developer resources.'
random_paper: 36
score:
  band: emerging
  composite: 26.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.2
    developer_ergonomics: 8.7
    discoverability: 77.8
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.9
  scored_at: '2026-08-03'
slug: bizverify
tags:
- Business Verification
- KYB
- Know Your Business
- Entity Verification
- Compliance
- MCP
- Agent-native
- Developer Tools
website: https://bizverify.co
---
