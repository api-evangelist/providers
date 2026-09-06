---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Hosted MCP server over Streamable HTTP exposing nine tools — get_config, list_jurisdictions, verify_business, search_entities, check_job_status, get_entity, get_entity_history, get_account and purchas
  name: BizVerify MCP Server
  slug: bizverify-mcp-server
- baseURL: https://api.bizverify.co
  baseurl_source: declared
  description: The Account API from BizVerify — 5 operation(s) for account.
  name: BizVerify Account API
  slug: bizverify-account-api
- baseURL: https://api.bizverify.co
  baseurl_source: declared
  description: The Auth API from BizVerify — 2 operation(s) for auth.
  name: BizVerify Auth API
  slug: bizverify-auth-api
- baseURL: https://api.bizverify.co
  baseurl_source: declared
  description: The Billing API from BizVerify — 2 operation(s) for billing.
  name: BizVerify Billing API
  slug: bizverify-billing-api
- baseURL: https://api.bizverify.co
  baseurl_source: declared
  description: The Entities API from BizVerify — 2 operation(s) for entities.
  name: BizVerify Entities API
  slug: bizverify-entities-api
- baseURL: https://api.bizverify.co
  baseurl_source: declared
  description: The Meta API from BizVerify — 2 operation(s) for meta.
  name: BizVerify Meta API
  slug: bizverify-meta-api
- baseURL: https://api.bizverify.co
  baseurl_source: declared
  description: The Public API from BizVerify — 2 operation(s) for public.
  name: BizVerify Public API
  slug: bizverify-public-api
- baseURL: https://api.bizverify.co
  baseurl_source: declared
  description: The Search API from BizVerify — 1 operation(s) for search.
  name: BizVerify Search API
  slug: bizverify-search-api
- baseURL: https://api.bizverify.co
  baseurl_source: declared
  description: The Tools API from BizVerify — 2 operation(s) for tools.
  name: BizVerify Tools API
  slug: bizverify-tools-api
- baseURL: https://api.bizverify.co
  baseurl_source: declared
  description: The Verification API from BizVerify — 2 operation(s) for verification.
  name: BizVerify Verification API
  slug: bizverify-verification-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BizVerify Account API
  slug: open-bizverify-account-api
- collection_type: open
  name: BizVerify Auth API
  slug: open-bizverify-auth-api
- collection_type: open
  name: BizVerify Billing API
  slug: open-bizverify-billing-api
- collection_type: open
  name: BizVerify Entities API
  slug: open-bizverify-entities-api
- collection_type: open
  name: BizVerify Meta API
  slug: open-bizverify-meta-api
- collection_type: open
  name: BizVerify Public API
  slug: open-bizverify-public-api
- collection_type: open
  name: BizVerify Search API
  slug: open-bizverify-search-api
- collection_type: open
  name: BizVerify Tools API
  slug: open-bizverify-tools-api
- collection_type: open
  name: BizVerify Verification API
  slug: open-bizverify-verification-api
- collection_type: open
  name: BizVerify API
  slug: open-bizverify
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/BizVerify/bizverify-mcp/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/BizVerify/bizverify-mcp/blob/main/LICENSE
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
mcp_servers:
- description: ''
  name: BizVerify MCP Server
  slug: bizverify-mcp-server
modified: '2026-08-02'
name: BizVerify
nav: Providers
network: true
overview: 'BizVerify publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Auth API, Billing API, and 6 more. Tagged areas include Business Verification, KYB, Know Your Business, Entity Verification, and Compliance.


  BizVerify''s developer surface includes documentation and 11 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 47.8
    developer_ergonomics: 16.7
    discoverability: 77.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bizverify/refs/heads/main/screenshots/bizverify-2026-08-07T162603.png
slug: bizverify
tags:
- Business Verification
- KYB
- Know Your Business
- Entity Verification
- Compliance
- MCP
- agent-native
- Developer Tools
website: https://bizverify.co
---
