---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The anonymously readable WordPress/Altis REST API that backs the noom.com marketing site and the Noom blog. Discovered by probing https://www.noom.com/wp-json/, which returns a 200 route index adverti
  name: Noom Content API (WordPress REST)
  slug: noom-content-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.noom.com/
- group: company
  title: ''
  type: Blog
  url: https://www.noom.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.noom.com/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.noom.com/support/
- group: start
  title: ''
  type: Login
  url: https://account.noom.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.noom.com/plans/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.noom.com/terms-and-conditions-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.noom.com/noom-privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/noom
- group: auth
  title: ''
  type: Compliance
  url: https://trust.noom.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/noom-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/noom-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noom-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/noom-llms.txt
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/noom_stock/
created: '2026-07-31'
description: Noom, Inc. is a New York-based digital health company founded in 2008 by Saeju Jeong and Artem Petakov, best known for a psychology-based weight-management mobile app that pairs behaviour-change coursework and human coaching with food logging, activity tracking and, through Noom Med, clinician-prescribed GLP-1 medication. Alongside the direct-to-consumer subscription, Noom sells to employers, health plans and health systems through Noom Healthy Weight, Noom Diabetes Prevention, the Noom GLP-1 Companion and a Noom Med Center of Excellence. Noom publishes no public developer portal, no OpenAPI/GraphQL contract and no client SDKs; its application host api.noom.com answers every anonymous request with HTTP 401 UNAUTHENTICATED, and health-system integration is described only as a business capability ("we can integrate into major EHR platforms") with no published specification. The only anonymously callable machine-readable surface found is the WordPress/Altis REST API behind the
  noom.com marketing and blog site.
image: https://www.noom.com/tachyon/2022/11/noom-logo-social-t.png
layout: provider
modified: '2026-07-31'
name: Noom
nav: Providers
network: true
overview: 'Noom publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Weight Management, and Wellness.


  Noom''s developer surface includes engineering blog, support, pricing, and 12 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 24.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/noom/refs/heads/main/screenshots/noom-2026-08-07T185500.png
security:
- kind: domain-security
  name: Noom Domain Security
  slug: noom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Noom Trust Center
  slug: noom-trust-center
  summary_line: trust center published
slug: noom
tags:
- Company
- Health
- Digital Health
- Weight Management
- Wellness
- Behavioral Health
- Telehealth
- Nutrition
- Consumer Health
- Mobile Applications
website: https://www.noom.com/
---
