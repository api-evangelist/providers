---
access_model:
  confidence: medium
  label: Free · no signup
  onboarding: unknown
  pricing: free
  public: true
  source:
  - '{''url'': ''https://wmegrp.com/wp-json/wp/v2/posts?per_page=1'', ''status'': 200, ''note'': "Anonymous GET returned HTTP 200 with content on 2026-09-06 — the only API surface the company serves is its corporate site''s WordPress content API, which needs no key, no account and no plan. There is nothing to buy and nothing to sign up for, so this is free-and-open access to a CMS surface, NOT a commercial API product."}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-12'
api_count: 2
apis:
- baseURL: https://wmegrp.com/wp-json/wp/v2
  baseurl_source: declared
  description: The corporate site of WME Group — the renamed Endeavor Group Holdings — runs WordPress and exposes the WordPress REST API at https://wmegrp.com/wp-json/. The wp/v2 namespace is anonymously readable an
  name: WME Group Content API (WordPress REST wp/v2)
  slug: content-api
- description: A Model Context Protocol server endpoint advertised in the wmegrp.com WordPress REST route index under the "mcp" namespace and served at /wp-json/mcp/mcp-adapter-default-server. The namespace index an
  name: WME Group MCP Server (WordPress MCP Adapter)
  slug: mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Endeavor
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/endeavor/
- group: other
  title: ''
  type: Subsidiary
  url: https://www.wmeagency.com/
- group: other
  title: ''
  type: Subsidiary
  url: https://imglicensing.com/
- group: other
  title: ''
  type: Subsidiary
  url: https://www.pantheonmedia.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/endeavor-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/endeavor-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/endeavor-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/endeavor-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/endeavor-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/endeavor-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/endeavor-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wmegrp.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wmegrp.com/terms-of-use/
- group: company
  title: ''
  type: Careers
  url: https://wmeimg.wd1.myworkdayjobs.com/WMEGRP
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/endeavor-co
- group: company
  title: ''
  type: Website
  url: https://wmegrp.com/
- group: other
  title: ''
  type: Successor
  url: https://wmegrp.com/
- group: other
  title: ''
  type: Spinoff
  url: https://www.tkogrp.com/
created: '2026-03-21'
description: Endeavor was a global sports and entertainment company representing talent and owning and operating events, with subsidiaries including WME, IMG, and UFC. Following the 2024 take-private transaction by Silver Lake and the separation of TKO Group Holdings (UFC and WWE), the remaining talent, media, marketing, and licensing businesses were rebranded as WME Group. This repository tracks Endeavor as a corporate entity. It publishes no developer program, no API documentation and no OpenAPI; the only machine-readable surfaces on its own hosts are the wmegrp.com WordPress content API, which is anonymously readable, and a live but authentication-gated WordPress MCP Adapter endpoint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/endeavor.png
layout: provider
mcp_servers:
- description: ''
  name: Endeavor MCP Server
  slug: endeavor-mcp-server
modified: '2026-09-06'
name: Endeavor
nav: Providers
network: true
overview: 'Endeavor publishes 1 API on the [APIs.io](https://apis.io/) network: WME Group Content API (WordPress REST wp/v2). Tagged areas include Sports, Entertainment, Talent, Media, and Licensing.


  Endeavor''s developer surface includes authentication and 19 more developer resources.'
plans:
- name: Endeavor Plans Pricing
  plan_count: 0
  slug: endeavor-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Endeavor Rate Limits
  slug: endeavor-rate-limits
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 17.7
    developer_ergonomics: 13.7
    discoverability: 68.5
    operational_transparency: 0.0
  previous_composite: 18.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/endeavor/refs/heads/main/screenshots/endeavor-2026-06-20T180654.png
security:
- kind: authentication
  name: Endeavor Authentication
  slug: endeavor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Endeavor Domain Security
  slug: endeavor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: endeavor
tags:
- Sports
- Entertainment
- Talent
- Media
- Licensing
- Marketing
website: https://wmegrp.com/
---
