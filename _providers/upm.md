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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: Standards-based OAI-PMH 2.0 metadata harvesting interface for the Universiti Putra Malaysia Institutional Repository (PSAS IR), running on EPrints. Supports the Identify, ListMetadataFormats, ListReco
  name: PSAS Institutional Repository OAI-PMH
  slug: oai-pmh
- description: Federated single sign-on identity provider for Universiti Putra Malaysia, built on Shibboleth and publishing SAML 2.0 / SAML 1.1 metadata at its entityID. Used for research and education community fed
  name: UPM Shibboleth SAML 2.0 Identity Provider
  slug: saml-idp
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/upm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upm.edu.my/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universiti-putra-malaysia/
- group: build
  title: ''
  type: Library
  url: https://lib.upm.edu.my/
- group: other
  title: ''
  type: Repository
  url: http://psasir.upm.edu.my/
- group: auth
  title: ''
  type: Authentication
  url: https://idf.upm.edu.my/idp/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/upm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/upm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/upm-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universiti Putra Malaysia (UPM) is a Malaysian public research university in Serdang, Selangor, formerly the Universiti Pertanian Malaysia, and ranked #148 in the QS World University Rankings 2025. UPM has no central, publicly documented developer portal, but it does operate machine-readable scholarly and identity infrastructure: an EPrints-based institutional repository (PSAS IR) that exposes a standards-based OAI-PMH 2.0 metadata harvesting interface, and a Shibboleth SAML 2.0 identity provider used for federated single sign-on. Application access for students and staff (study portal, Putra portal, SIMS) is gated behind UPM-ID SSO and is not openly documented.'
finops:
- name: Upm Finops
  service_category: Education
  slug: upm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upm.png
jsonld:
- class_count: 15
  name: Upm Context
  property_count: 1
  slug: upm-context
layout: provider
modified: '2026-06-03'
name: Universiti Putra Malaysia
nav: Providers
network: true
overview: 'Universiti Putra Malaysia publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Universiti Putra Malaysia catalog on APIs.io includes 1 JSON-LD context.


  Universiti Putra Malaysia''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Upm Plans Pricing
  plan_count: 2
  slug: upm-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 1
  name: Upm Rate Limits
  slug: upm-rate-limits
score:
  band: emerging
  composite: 23.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/upm/refs/heads/main/screenshots/upm-2026-06-20T200449.png
security:
- kind: domain-security
  name: Upm Domain Security
  slug: upm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Upm Vulnerability Disclosure
  slug: upm-vulnerability-disclosure
  summary_line: disclosure policy published
slug: upm
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Institutional Repository
- Identity
- Malaysia
website: https://upm.edu.my/
---
