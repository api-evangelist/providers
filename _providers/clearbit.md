---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-06'
api_count: 5
apis:
- description: 'Person and Company enrichment given an email or domain. Returns firmographic, technographic, and persona data. Endpoints: /person, /company, /combined.'
  name: Clearbit Enrichment API
  slug: enrichment
- description: De-anonymizes website visitors by IP address, returning company firmographics for B2B traffic.
  name: Clearbit Reveal API
  slug: reveal
- description: Search for people and companies matching firmographic and persona filters.
  name: Clearbit Prospector API
  slug: prospector
- description: 'Free Logo API: returns a company logo image given a domain. No auth required.'
  name: Clearbit Logo API
  slug: logo
- description: 'Free Autocomplete API: returns company candidates (name, domain, logo) for a name fragment.'
  name: Clearbit Autocomplete (Name-to-Domain) API
  slug: name-to-domain
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/clearbit-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clearbit-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clearbit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clearbit
- group: company
  title: ''
  type: Website
  url: https://clearbit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.clearbit.com/docs
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
- group: company
  title: ''
  type: Blog
  url: https://clearbit-blog.ghost.io/rss/
created: '2026-05-08'
description: Clearbit was a B2B marketing and sales intelligence platform; HubSpot acquired it in late 2023 and has rebranded most capabilities as HubSpot Breeze Intelligence. Legacy Clearbit REST APIs (Enrichment, Reveal, Prospector, Discovery, Risk, Logo, NameToDomain) were widely used; new sign-ups are now redirected into HubSpot's product surface, and standalone Clearbit APIs are being sunset for new customers.
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
modified: '2026-05-08'
name: Clearbit (HubSpot Breeze Intelligence)
nav: Providers
network: true
overview: 'Clearbit (HubSpot Breeze Intelligence) publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Intelligence, B2B, Enrichment, Reveal, and HubSpot.


  Clearbit (HubSpot Breeze Intelligence)''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Clearbit Plans Pricing
  plan_count: 3
  slug: clearbit-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 3
  name: Clearbit Rate Limits
  slug: clearbit-rate-limits
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clearbit/refs/heads/main/screenshots/clearbit-2026-06-20T174455.png
security:
- kind: domain-security
  name: Clearbit Domain Security
  slug: clearbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clearbit Trust Center
  slug: clearbit-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP, GDPR
slug: clearbit
tags:
- Sales Intelligence
- B2B
- Enrichment
- Reveal
- HubSpot
- Marketing
website: https://clearbit.com/
---
