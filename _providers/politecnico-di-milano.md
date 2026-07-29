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
    asyncapi_events: false
    auth_clarity: true
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
  score: 12.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Public OAI-PMH 2.0 metadata harvesting endpoint for the IRIS Re.Public@Polimi institutional research repository (CINECA platform). The endpoint resolves and returns a valid Identify response naming th
  name: IRIS Re.Public@Polimi OAI-PMH
  slug: iris-oai-pmh
- description: Institutional open data portal (opendata.polimi.it) publishing the university's public datasets. The portal resolves and serves dataset browsing and download, but exposes no documented programmatic AP
  name: Politecnico di Milano Open Data Portal
  slug: open-data
- description: Shibboleth/SAML2 identity provider for Politecnico di Milano, serving federated single sign-on as part of the Italian IDEM (GARR) academic identity federation. The IdP metadata endpoint resolves publi
  name: Politecnico di Milano Shibboleth Identity Provider
  slug: shibboleth-idp
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/politecnico-di-milano-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.polimi.it/en/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/polimi/
- group: auth
  title: ''
  type: Authentication
  url: https://shibidp.polimi.it/idp/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/politecnico-di-milano-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/politecnico-di-milano-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/politecnico-di-milano-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Politecnico di Milano is Italy''s largest technical university, focused on engineering, architecture, and design, and ranked #111 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is limited and not consolidated into a single developer portal. The most concrete public API surface is the OAI-PMH metadata endpoint of its IRIS Re.Public@Polimi institutional research repository (CINECA platform), an open data portal at opendata.polimi.it (browse/download, with no documented programmatic API), and a Shibboleth/SAML2 identity provider participating in the Italian IDEM (GARR) federation. Most student-facing service APIs (online services / mobile app backends) are gated behind authentication and are not publicly documented.'
finops:
- name: Politecnico Di Milano Finops
  service_category: Education
  slug: politecnico-di-milano-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/politecnico-di-milano.png
jsonld:
- class_count: 19
  name: Politecnico Di Milano Context
  property_count: 5
  slug: politecnico-di-milano-context
layout: provider
modified: '2026-06-03'
name: Politecnico di Milano
nav: Providers
network: true
overview: 'Politecnico di Milano publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Politecnico di Milano catalog on APIs.io includes 1 JSON-LD context.


  Politecnico di Milano''s developer surface includes authentication and 7 more developer resources.'
plans:
- name: Politecnico Di Milano Plans Pricing
  plan_count: 2
  slug: politecnico-di-milano-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Politecnico Di Milano Rate Limits
  slug: politecnico-di-milano-rate-limits
score:
  band: emerging
  composite: 22.1
  delta: -3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/politecnico-di-milano/refs/heads/main/screenshots/politecnico-di-milano-2026-06-20T191910.png
security:
- kind: domain-security
  name: Politecnico Di Milano Domain Security
  slug: politecnico-di-milano-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: politecnico-di-milano
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Repository
- OAI-PMH
- Identity
- Italy
website: https://www.polimi.it/en/
---
