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
  scored_at: '2026-08-30'
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
random_paper: 2
rate_limits:
- limit_count: 1
  name: Upm Rate Limits
  slug: upm-rate-limits
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 25.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
