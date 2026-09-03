---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 38
  human_in_the_loop: 3
  name: Speakeasy Api Agentic Access
  operation_count: 77
  slug: speakeasy-api-agentic-access
  summary_line: 77 operations · 38 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for working with Registry artifacts
  name: Speakeasy Artifacts API
  slug: speakeasy-api-artifacts-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing Authentication
  name: Speakeasy Auth API
  slug: speakeasy-api-auth-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for retrieving Code Samples
  name: Speakeasy CodeSamples API
  slug: speakeasy-api-codesamples-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing events captured by a speakeasy binary (CLI, GitHub Action etc)
  name: Speakeasy Events API
  slug: speakeasy-api-events-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing the github integration
  name: Speakeasy Github API
  slug: speakeasy-api-github-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing Organizations (speakeasy L1 Tenancy construct)
  name: Speakeasy Organizations API
  slug: speakeasy-api-organizations-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: The PublishingTokens API from Speakeasy — 4 operation(s) for publishingtokens.
  name: Speakeasy PublishingTokens API
  slug: speakeasy-api-publishingtokens-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing reports (lint reports, change reports, etc)
  name: Speakeasy Reports API
  slug: speakeasy-api-reports-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: The SchemaStore API from Speakeasy — 1 operation(s) for schemastore.
  name: Speakeasy SchemaStore API
  slug: speakeasy-api-schemastore-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing short URLs
  name: Speakeasy ShortURLs API
  slug: speakeasy-api-shorturls-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing subscriptions
  name: Speakeasy Subscriptions API
  slug: speakeasy-api-subscriptions-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing LLM OAS suggestions
  name: Speakeasy Suggest API
  slug: speakeasy-api-suggest-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing Workspaces (speakeasy tenancy)
  name: Speakeasy Workspaces API
  slug: speakeasy-api-workspaces-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Speakeasy Artifacts API
  slug: open-speakeasy-api-artifacts-api
- collection_type: open
  name: Speakeasy Artifacts Auth API
  slug: open-speakeasy-api-auth-api
- collection_type: open
  name: Speakeasy Artifacts CodeSamples API
  slug: open-speakeasy-api-codesamples-api
- collection_type: open
  name: Speakeasy Artifacts Events API
  slug: open-speakeasy-api-events-api
- collection_type: open
  name: Speakeasy Artifacts Github API
  slug: open-speakeasy-api-github-api
- collection_type: open
  name: Speakeasy Artifacts Organizations API
  slug: open-speakeasy-api-organizations-api
- collection_type: open
  name: Speakeasy Artifacts PublishingTokens API
  slug: open-speakeasy-api-publishingtokens-api
- collection_type: open
  name: Speakeasy Artifacts Reports API
  slug: open-speakeasy-api-reports-api
- collection_type: open
  name: Speakeasy Artifacts SchemaStore API
  slug: open-speakeasy-api-schemastore-api
- collection_type: open
  name: Speakeasy Artifacts ShortURLs API
  slug: open-speakeasy-api-shorturls-api
- collection_type: open
  name: Speakeasy Artifacts Subscriptions API
  slug: open-speakeasy-api-subscriptions-api
- collection_type: open
  name: Speakeasy Artifacts Suggest API
  slug: open-speakeasy-api-suggest-api
- collection_type: open
  name: Speakeasy Artifacts Workspaces API
  slug: open-speakeasy-api-workspaces-api
- collection_type: open
  name: Speakeasy API
  slug: open-speakeasy-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/speakeasy-api-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/speakeasy-api-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/speakeasy-api-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/speakeasy-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/speakeasyapi
- group: company
  title: ''
  type: Website
  url: https://www.speakeasy.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.speakeasy.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/speakeasy-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/speakeasy-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/speakeasy-api-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.speakeasy.com/blog
created: '2026-07-11'
description: Speakeasy is an API developer-experience platform that generates production-ready, type-safe SDKs (client libraries), Terraform providers, MCP servers, CLIs, code samples, and docs from an OpenAPI specification. The primary interface is the Speakeasy CLI plus GitHub Actions and the hosted platform, but Speakeasy also exposes a documented public REST API at https://api.prod.speakeasy.com that backs the CLI and platform - covering the OpenAPI/artifact registry, workspaces and organizations, schema store, code samples, generation events, lint/change reports, GitHub automation, LLM-powered OpenAPI suggestions, and SDK publishing tokens. It is OpenAPI-native with no proprietary DSL, targeting API design, API lifecycle, and SDK/client-library generation use cases.
finops:
- name: Speakeasy Api Finops
  service_category: Developer Tools and API Management
  slug: speakeasy-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/speakeasy-api.png
layout: provider
modified: '2026-07-11'
name: Speakeasy
nav: Providers
network: true
overview: 'Speakeasy publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Artifacts API, Auth API, CodeSamples API, and 10 more. Tagged areas include API Lifecycle, SDK Generation, Client Library, API Design, and Developer Tools.


  Speakeasy''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Speakeasy Api Plans Pricing
  plan_count: 3
  slug: speakeasy-api-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Speakeasy Api Rate Limits
  slug: speakeasy-api-rate-limits
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Speakeasy Api Authentication
  slug: speakeasy-api-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Speakeasy Api Domain Security
  slug: speakeasy-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: speakeasy-api
tags:
- API Lifecycle
- SDK Generation
- Client Library
- API Design
- Developer Tools
- OpenAPI
- Code Generation
- Terraform
- MCP
- Developer Experience
website: https://www.speakeasy.com
---
