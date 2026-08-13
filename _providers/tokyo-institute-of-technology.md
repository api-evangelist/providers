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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: OAI-PMH 2.0 metadata harvesting interface for T2R2, the Science Tokyo / Tokyo Tech Research Repository operated by GSIC and the university library. Exposes records (papers, theses, manuscripts, patent
  name: T2R2 Research Repository OAI-PMH
  slug: t2r2-oaipmh
- description: SAML 2.0 / Shibboleth identity provider for institutional single sign-on, participating in Japan's GakuNin academic access management federation. This is a federated SAML authentication endpoint for i
  name: GakuNin Shibboleth Identity Provider (SAML)
  slug: gakunin-shibboleth
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tokyo-institute-of-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.isct.ac.jp/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/prg-titech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/sciencetokyo/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sciencetokyo_en
- group: auth
  title: ''
  type: Authentication
  url: https://idp-gakunin.nap.gsic.titech.ac.jp/idp/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/tokyo-institute-of-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tokyo-institute-of-technology-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tokyo-institute-of-technology-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Tokyo Institute of Technology (Tokyo Tech / Titech) was a national research university in Tokyo, Japan, ranked #76 in the QS World University Rankings 2025. In October 2024 it merged with Tokyo Medical and Dental University to form the Institute of Science Tokyo (Science Tokyo), and its public web presence now lives primarily at isct.ac.jp while legacy titech.ac.jp services remain online. Its public, machine-readable developer footprint is limited: the most clearly documented programmatic interface is the T2R2 (Science Tokyo / Tokyo Tech Research Repository) OAI-PMH metadata harvesting endpoint. Identity is federated through GakuNin using Shibboleth/SAML rather than a public OAuth/OpenID Connect API. No official institution-wide REST developer portal or open-data API was found.'
finops:
- name: Tokyo Institute Of Technology Finops
  service_category: Education
  slug: tokyo-institute-of-technology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tokyo-institute-of-technology.png
jsonld:
- class_count: 22
  name: Tokyo Institute Of Technology Context
  property_count: 1
  slug: tokyo-institute-of-technology-context
layout: provider
modified: '2026-06-03'
name: Tokyo Institute of Technology
nav: Providers
network: true
overview: 'Tokyo Institute of Technology publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Japan, and Research.


  The Tokyo Institute of Technology catalog on APIs.io includes 1 JSON-LD context.


  Tokyo Institute of Technology''s developer surface includes GitHub presence, authentication, and 8 more developer resources.'
plans:
- name: Tokyo Institute Of Technology Plans Pricing
  plan_count: 2
  slug: tokyo-institute-of-technology-plans-pricing
random_paper: 119
rate_limits:
- limit_count: 1
  name: Tokyo Institute Of Technology Rate Limits
  slug: tokyo-institute-of-technology-rate-limits
score:
  band: emerging
  composite: 20.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tokyo-institute-of-technology/refs/heads/main/screenshots/tokyo-institute-of-technology-2026-06-20T195440.png
security:
- kind: domain-security
  name: Tokyo Institute Of Technology Domain Security
  slug: tokyo-institute-of-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tokyo-institute-of-technology
tags:
- Education
- Higher Education
- University
- Japan
- Research
- Open Access
- Institutional Repository
- OAI-PMH
website: https://www.isct.ac.jp/en
---
