---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-17'
api_count: 9
apis:
- description: 'Person enrichment from an email address, plus the Combined lookup that returns the person and their company in one response. Endpoints: /v2/people/find, /v2/combined/find. Verified live 2026-08-13 (HT'
  name: Clearbit Person Enrichment API
  slug: enrichment
- description: 'Company enrichment from a domain, and the Name to Domain lookup that resolves a company name to its primary domain. Endpoints: /v2/companies/find, /v1/domains/find. Verified live 2026-08-13 (HTTP 401 '
  name: Clearbit Company Enrichment API
  slug: company-enrichment
- description: The same enrichment contract served from a streaming host that holds the connection open for up to 60 seconds so a queued (202) lookup resolves in-band. The provider warns it "leads to slow Enrichment
  name: Clearbit Streaming Enrichment API
  slug: enrichment-streaming
- description: De-anonymizes website visitors by IP address, returning company firmographics for B2B traffic. Endpoint /v1/companies/find?ip=. Verified live 2026-08-13 (HTTP 401 auth_required). Explicitly excluded f
  name: Clearbit Reveal API
  slug: reveal
- description: Search for people matching firmographic and persona filters. Endpoint /v1/people/search. Verified live 2026-08-13 (HTTP 401 auth_required, x-api-version 2018-11-16, x-ratelimit-* headers present). Sup
  name: Clearbit Prospector API
  slug: prospector
- description: Search Clearbit's company database with a structured query to build target-market lists. Endpoint /v1/companies/search. Verified live 2026-08-13 (HTTP 401 auth_required). No published rate limit and n
  name: Clearbit Discovery API
  slug: discovery
- description: Scores an email address for fraud and abuse risk. Endpoint /v1/calculate?email=. Verified live 2026-08-13 (HTTP 401 auth_required, x-api-version 2016-05-03 — the oldest dated version on the estate). D
  name: Clearbit Risk API
  slug: risk
- description: 'Free, unauthenticated company autocomplete: returns candidate companies (name, domain, logo) for a name fragment. Endpoint /v1/companies/suggest?query=. The only Clearbit endpoint that answers an anon'
  name: Clearbit Autocomplete API
  slug: name-to-domain
- description: 'RETIRED 2025-12-08. The free Logo API returned a company logo image for a domain with no authentication. Announced 2025-02-13, moved to 2025-12-01, then final on 2025-12-08 after a deliberate 24-hour '
  name: Clearbit Logo API (retired)
  slug: logo
artifact_total: 18
asyncapis:
- description: ''
  name: Clearbit Webhooks
  slug: clearbit-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://clearbit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.clearbit.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://help.clearbit.com/
- group: docs
  title: ''
  type: APIReference
  url: https://clearbit.com/attributes
- group: operate
  title: ''
  type: Support
  url: https://help.clearbit.com/
- group: company
  title: ''
  type: Blog
  url: https://clearbit-blog.ghost.io/rss/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clearbit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clearbit
- group: commercial
  title: ''
  type: Pricing
  url: https://clearbit.com/pricing
- group: start
  title: ''
  type: Login
  url: https://clearbit.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clearbit.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clearbit.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://clearbit.com/trust#compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/clearbit-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/clearbit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clearbit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clearbit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clearbit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clearbit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clearbit-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clearbit-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clearbit-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clearbit-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clearbit.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://clearbit.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clearbit-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/clearbit-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/clearbit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/clearbit-packages.yml
- group: design
  title: ''
  type: Components
  url: components/clearbit-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clearbit-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/clearbit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clearbit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clearbit-finops.yml
created: '2026-05-08'
description: Clearbit is a B2B marketing and sales intelligence platform whose REST APIs resolve an email address to a person, a domain to a company, and an IP address to the business behind it, returning firmographic, technographic and persona data across a documented 100+ company and 60+ person attributes classified against GICS, SIC and NAICS. HubSpot acquired Clearbit in December 2023 and sells the capability as HubSpot Breeze Intelligence. The legacy Clearbit APIs (Enrichment, Streaming, Reveal, Prospector, Discovery, Risk, Name-to-Domain, Autocomplete) remain live and answer on their production hosts, but the provider is in publicly dated wind-down — new API keys have not been issued since 2023, free accounts were sunset 2025-04-30, and the free Logo API was sunset 2025-12-08 and its host no longer resolves. Only the free Autocomplete API is callable without a credential.
finops:
- name: Clearbit Finops
  service_category: Sales Intelligence
  slug: clearbit-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Clearbit (now HubSpot Breeze Intelligence) B2B data enrichment and intelligence platform. Clearbit provided REST APIs for person and company
  name: Clearbit GraphQL Schema
  slug: clearbit-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clearbit.png
layout: provider
modified: '2026-08-13'
name: Clearbit (HubSpot Breeze Intelligence)
nav: Providers
network: true
overview: 'Clearbit (HubSpot Breeze Intelligence) publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Intelligence, B2B, Enrichment, Reveal, and HubSpot.


  The Clearbit (HubSpot Breeze Intelligence) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Clearbit (HubSpot Breeze Intelligence)''s developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, changelog, and 27 more developer resources.'
plans:
- name: Clearbit Plans Pricing
  plan_count: 1
  slug: clearbit-plans-pricing
random_paper: 93
rate_limits:
- limit_count: 9
  name: Clearbit Rate Limits
  slug: clearbit-rate-limits
score:
  band: strong
  composite: 58.9
  delta: 30.8
  facets:
    commercial_clarity: 73.7
    contract_quality: 63.0
    developer_ergonomics: 47.8
    discoverability: 81.5
    governance: 12.5
    operational_transparency: 71.1
  previous_composite: 28.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/clearbit/refs/heads/main/screenshots/clearbit-2026-06-20T174455.png
security:
- kind: authentication
  name: Clearbit Authentication
  slug: clearbit-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Clearbit Domain Security
  slug: clearbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clearbit Vulnerability Disclosure
  slug: clearbit-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Clearbit Trust Center
  slug: clearbit-trust-center
  summary_line: trust center published
slug: clearbit
tags:
- Sales Intelligence
- B2B
- Enrichment
- Reveal
- HubSpot
- Marketing
- Data
- Firmographics
- Lead Enrichment
- Company Data
website: https://clearbit.com/
---
