---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - https://apps.shopify.com/mai-marketing-ai-agents
  trial: true
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The one public, callable API MAI publishes. A single unauthenticated write-only endpoint, POST /api/collect, that ingests first-party commerce events from a merchant's storefront — product views, cart
  name: MAI Pixel Event Collection API
  slug: mai-pixel-event-collection-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.mai.co/
- group: company
  title: ''
  type: About
  url: https://www.mai.co/about
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mai.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.mai.co/
- group: operate
  title: ''
  type: FAQ
  url: https://www.mai.co/faq
- group: other
  title: ''
  type: CaseStudies
  url: https://www.mai.co/case-studies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mai.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mai.co/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://mai-unbound.secureframetrust.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mai-agents/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Mai_Agents
- group: auth
  title: ''
  type: TrustCenter
  url: security/mai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mai-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mai-co
- group: operate
  title: ''
  type: Support
  url: https://apps.shopify.com/mai-marketing-ai-agents
- group: build
  title: ''
  type: Packages
  url: packages/mai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mai-packages.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mai-pixel-event.schema.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/mai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mai-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mai-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mai-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mai-llms.txt
created: '2026-07-17'
description: 'MAI is an AI performance-marketing platform that runs autonomous AI agents to create, monitor, and optimize digital advertising campaigns 24/7 on behalf of brands. Founded in December 2024 by former Google Ads and Instacart engineering leaders, MAI natively connects to a company''s advertising accounts and first-party data to deliver real-time performance analysis, attribution modeling, cross-channel budget allocation, automated campaign creation, and bid optimization. Its agents currently manage millions of dollars of Google Ads spend each month for e-commerce and consumer brands. MAI raised a $25M seed round led by Kleiner Perkins with participation from Gaorong Ventures and UpHonest Capital. MAI is delivered mainly as a managed SaaS product and as a Shopify app, and it has no general-purpose developer platform — no developer portal, API reference, OpenAPI, GraphQL or MCP server. It does publish one public, callable API: the MAI Pixel Event Collection endpoint at https://pixel.mai.co/api/collect,
  which ingests first-party commerce events from a merchant storefront so MAI''s agents can attribute ad spend to revenue. Its contract is published not as a specification but as first-party TypeScript declarations inside MAI''s MIT-licensed @mai-co/pixel SDK on npm.'
image: https://xqxhyvqndlcdmf5c.public.blob.vercel-storage.com/assets/images/website-preview.png
json_schemas:
- name: MAI Pixel Event Payload
  property_count: 15
  slug: mai-pixel-event.schema
layout: provider
modified: '2026-08-12'
name: MAI
nav: Providers
network: true
overview: 'MAI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Marketing, Advertising, and Performance Marketing.


  MAI''s developer surface includes pricing, signup flow, FAQ, support, authentication, and 21 more developer resources.'
plans:
- name: Mai Plans Pricing
  plan_count: 2
  slug: mai-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Mai Rate Limits
  slug: mai-rate-limits
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 8.0
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.6
  provenance:
    conformance: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mai/refs/heads/main/screenshots/mai-2026-07-25T225907.png
security:
- kind: authentication
  name: Mai Authentication
  slug: mai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mai Domain Security
  slug: mai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Mai Trust Center
  slug: mai-trust-center
  summary_line: trust center published
slug: mai
tags:
- Company
- Artificial Intelligence
- Marketing
- Advertising
- Performance Marketing
- AI Agents
- Digital Advertising
- MarTech
- Google Ads
- Shopify
- E-Commerce
- Attribution
- Analytics
- Event Tracking
website: https://www.mai.co/
---
