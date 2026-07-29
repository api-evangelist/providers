---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Sastrify platform provides SaaS management capabilities including software discovery, license optimization, vendor negotiations, and benchmark insights. It offers native integrations with accounti
  name: Sastrify Platform
  slug: sastrify-platform
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sastrify-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sastrify
- group: company
  title: ''
  type: Website
  url: https://www.sastrify.com/
- group: other
  title: ''
  type: Platform
  url: https://www.sastrify.com/platform
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sastrify.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.sastrify.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.sastrify.com/support/home
- group: start
  title: ''
  type: GettingStarted
  url: https://support.sastrify.com/support/solutions/folders/101000262118
- group: operate
  title: ''
  type: FAQ
  url: https://support.sastrify.com/support/solutions/folders/101000267482
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Sastrify
- group: start
  title: ''
  type: Login
  url: https://app.sastrify.com/
- group: start
  title: ''
  type: Signup
  url: https://www.sastrify.com/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sastrify-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sastrify-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sastrify-saas-subscription-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sastrify-saas-subscription-structure.json
- group: agent
  title: ''
  type: LlmsText
  url: https://app.sastrify.com/llms.txt
created: '2026-03-16'
description: Sastrify is an AI-powered SaaS management and procurement platform that unites IT, Finance, and Procurement on one intelligent platform. It discovers every tool in an organization's stack, manages licenses and renewals, benchmarks spend automatically against market data, and provides procurement workflow automation to help companies optimize and control their software subscriptions. Sastrify integrates with accounting tools, SSO providers, and SaaS tools for usage analytics, spend visibility, and vendor negotiation support.
finops:
- name: Sastrify Finops
  service_category: API
  slug: sastrify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sastrify.png
json_schemas:
- name: SaaSSubscription
  property_count: 18
  slug: sastrify-saas-subscription
json_structures:
- name: Sastrify Saas Subscription Structure
  property_count: 0
  slug: sastrify-saas-subscription-structure
jsonld:
- class_count: 5
  name: Sastrify Context
  property_count: 21
  slug: sastrify-context
layout: provider
modified: '2026-05-02'
name: Sastrify
nav: Providers
network: true
overview: 'Sastrify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cost Optimization, License Management, Procurement, SaaS Management, and Software Spend.


  The Sastrify catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sastrify''s developer surface includes pricing, engineering blog, support, getting-started guide, FAQ, GitHub presence, signup flow, and 10 more developer resources.'
plans:
- name: Sastrify Plans Pricing
  plan_count: 3
  slug: sastrify-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Sastrify Rate Limits
  slug: sastrify-rate-limits
rules:
- name: Sastrify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sastrify-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.5
  delta: -5.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 17.7
    developer_ergonomics: 17.4
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 44.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sastrify/refs/heads/main/screenshots/sastrify-2026-06-20T193441.png
security:
- kind: domain-security
  name: Sastrify Domain Security
  slug: sastrify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sastrify
tags:
- Cost Optimization
- License Management
- Procurement
- SaaS Management
- Software Spend
- Vendor Management
website: https://www.sastrify.com/
---
