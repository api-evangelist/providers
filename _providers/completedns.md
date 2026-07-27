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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Completedns Agentic Access
  operation_count: 2
  slug: completedns-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Nameserver and drop history for a domain
  name: CompleteDNS DNS History API
  slug: completedns-dns-history-api
- description: Nameserver history (legacy) for a domain
  name: CompleteDNS NS History API
  slug: completedns-ns-history-api
artifact_total: 14
collections:
- collection_type: open
  name: CompleteDNS API v1
  slug: open-completedns-v1
- collection_type: open
  name: CompleteDNS API v2
  slug: open-completedns-v2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/completedns-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/completedns-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/completedns-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://completedns.com/
- group: docs
  title: ''
  type: Documentation
  url: https://completedns.com/api/documentation/v2
- group: start
  title: ''
  type: Signup
  url: https://completedns.com/register
- group: start
  title: ''
  type: Login
  url: https://completedns.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://completedns.com/pricing
- group: operate
  title: ''
  type: Contact
  url: https://completedns.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://completedns.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://completedns.com/privacy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/completedns-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/completedns-dns-history-schema.json
created: '2025-02-09'
description: CompleteDNS is a DNS research platform that tracks nameserver modifications and domain drops, with over twenty years of history and billions of recorded changes. The CompleteDNS API exposes domain-scoped lookups that return the chronological history of nameserver changes, drop events, and parking status for a given domain. Both a current v2 API and a legacy v1 API are available, authenticated by API key.
finops:
- name: Completedns Finops
  service_category: API
  slug: completedns-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/completedns.png
json_schemas:
- name: CompleteDNS DNS History
  property_count: 6
  slug: completedns-dns-history
jsonld:
- class_count: 0
  name: Completedns Context
  property_count: 3
  slug: completedns-context
layout: provider
modified: '2026-05-19'
name: CompleteDNS
nav: Providers
network: true
overview: 'CompleteDNS publishes 2 APIs on the [APIs.io](https://apis.io/) network: DNS History API and NS History API. Tagged areas include DNS, DNS History, Domain Intelligence, Domains, and Nameservers.


  The CompleteDNS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CompleteDNS''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, and 8 more developer resources.'
plans:
- name: Completedns Plans Pricing
  plan_count: 3
  slug: completedns-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 5
  name: Completedns Rate Limits
  slug: completedns-rate-limits
rules:
- name: CompleteDNS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: completedns-jsonschema-spectral-rules
- name: CompleteDNS API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: completedns-rules
score:
  band: strong
  composite: 61.7
  delta: 3.2
  facets:
    commercial_clarity: 84.2
    contract_quality: 68.1
    developer_ergonomics: 28.3
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 58.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/completedns/refs/heads/main/screenshots/completedns-2026-06-20T174832.png
security:
- kind: authentication
  name: Completedns Authentication
  slug: completedns-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Completedns Domain Security
  slug: completedns-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: completedns
tags:
- DNS
- DNS History
- Domain Intelligence
- Domains
- Nameservers
- Threat Intelligence
website: https://completedns.com/
---
