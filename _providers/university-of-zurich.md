---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: University Of Zurich Agentic Access
  operation_count: 8
  slug: university-of-zurich-agentic-access
  summary_line: 8 operations · 3 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: The Zurich Open Repository and Archive (ZORA) provides open, worldwide access to the peer-reviewed research and scholarly output of the University of Zurich. ZORA supports OAI-PMH 2.0 for metadata har
  name: ZORA Repository OAI-PMH
  slug: zora-oai
- description: Following its 2025 migration to DSpace 7+, ZORA exposes the standard DSpace REST API (HAL+JSON) for programmatic discovery of communities, collections, and items representing UZH research output. This
  name: ZORA DSpace REST API
  slug: zora-rest
- description: OpenID Provider metadata and key material
  name: University of Zurich Discovery API
  slug: university-of-zurich-discovery-api
- description: Authorization and token issuance
  name: University of Zurich OAuth2 API
  slug: university-of-zurich-oauth2-api
- description: Identity, userinfo, and session endpoints
  name: University of Zurich OpenID Connect API
  slug: university-of-zurich-openid-connect-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-zurich-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-zurich-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-zurich-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.uzh.ch/en.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uzh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uzh
- group: company
  title: ''
  type: Twitter
  url: https://x.com/UZH_en
- group: auth
  title: ''
  type: Authentication
  url: https://www.zi.uzh.ch/en/support/identity-access/eduid-faq.html
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-zurich-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-zurich-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-zurich-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Zurich (UZH) is Switzerland''s largest university, founded in 1833, and is ranked #61 in the QS World University Rankings 2025. UZH does not operate a centralized public developer portal; its machine-readable footprint is centered on open scholarship and identity infrastructure. The Zurich Open Repository and Archive (ZORA) exposes the university''s research output, the GitHub organization "uzh" hosts open-source projects, and federated identity is provided through SWITCH edu-ID (SAML/Shibboleth and OpenID Connect). Most student-facing systems (course catalogue, OLAT LMS, student services) are web/SSO-gated rather than openly documented APIs.'
examples:
- key_count: 15
  name: University Of Zurich Discovery Example
  slug: university-of-zurich-discovery-example
- key_count: 2
  name: University Of Zurich Token Example
  slug: university-of-zurich-token-example
- key_count: 2
  name: University Of Zurich Userinfo Example
  slug: university-of-zurich-userinfo-example
finops:
- name: University Of Zurich Finops
  service_category: Education
  slug: university-of-zurich-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-zurich.png
json_schemas:
- name: SWITCH edu-ID Token Response
  property_count: 6
  slug: university-of-zurich-token-response
- name: SWITCH edu-ID UserInfo
  property_count: 22
  slug: university-of-zurich-userinfo
json_structures:
- name: University Of Zurich Token Response Structure
  property_count: 6
  slug: university-of-zurich-token-response-structure
- name: University Of Zurich Userinfo Structure
  property_count: 22
  slug: university-of-zurich-userinfo-structure
jsonld:
- class_count: 19
  name: University Of Zurich Context
  property_count: 4
  slug: university-of-zurich-context
layout: provider
modified: '2026-06-03'
name: University of Zurich
nav: Providers
network: true
overview: 'University of Zurich publishes 3 APIs on the [APIs.io](https://apis.io/) network: Discovery API, OAuth2 API, and OpenID Connect API. Tagged areas include Education, Higher Education, University, Switzerland, and Open Access.


  The University of Zurich catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Zurich''s developer surface includes authentication, GitHub presence, and 10 more developer resources.'
plans:
- name: University Of Zurich Plans Pricing
  plan_count: 2
  slug: university-of-zurich-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 1
  name: University Of Zurich Rate Limits
  slug: university-of-zurich-rate-limits
rules:
- name: University of Zurich API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-zurich-jsonschema-spectral-rules
- name: University of Zurich API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: university-of-zurich-rules
score:
  band: thin
  composite: 39.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-zurich/refs/heads/main/screenshots/university-of-zurich-2026-06-20T200336.png
security:
- kind: authentication
  name: University Of Zurich Authentication
  slug: university-of-zurich-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: University Of Zurich Domain Security
  slug: university-of-zurich-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-zurich
tags:
- Education
- Higher Education
- University
- Switzerland
- Open Access
- Research Repository
- Open Data
- Identity
website: https://www.uzh.ch/en.html
---
