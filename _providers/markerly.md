---
access_model:
  confidence: medium
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://markerly.com/contact-us
  - https://markerly.com/pricing
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: A first-party FFmpeg media-processing microservice Markerly runs on Google Cloud Run. It exposes two documented JSON/HTTP operations — a health check and a thumbnail generator that renders a JPEG fram
  name: Markerly Media Processor
  slug: media-processor
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://markerly.com
- group: company
  title: ''
  type: Blog
  url: https://markerly.com/news
- group: operate
  title: ''
  type: Support
  url: https://markerly.com/contact-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/markerly-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/markerly-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Markerly
- group: commercial
  title: ''
  type: TermsOfService
  url: https://markerly.com/msa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://markerly.com/tos
- group: start
  title: ''
  type: SignUp
  url: https://markerly.creatorsaurus.com/register
- group: start
  title: ''
  type: Login
  url: https://markerly.creatorsaurus.com/login
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/markerly-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/markerly-error-codes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/markerly-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/markerly-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/markerly-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/markerly-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/markerly-plans-pricing.yml
created: '2026-07-17'
description: 'Markerly is a full-service influencer marketing agency, running creator campaigns since 2012 across strategy, vetted-creator sourcing, content, activation, and real-time measurement. Two specialties set the Austin, Texas agency apart: influencer campaigns for government agencies, public health, and nonprofits (advocacy), and bilingual/multicultural creator campaigns. Markerly runs its creator network and client reporting on its own platform — a creator portal at markerly.creatorsaurus.com and a social-account connect app at api.markerly.com that links Instagram, Facebook Pages, and TikTok accounts — and it operates one publicly reachable first-party HTTP service, the Media Processor microservice on Google Cloud Run, whose source, endpoints, rate limits, and error envelope are published openly in the company''s own GitHub organization. Markerly publishes no OpenAPI, no developer portal, and no self-serve API program; per third-party reviews, API access for external integrations
  is bundled into its white-label platform tier rather than sold as a standalone product.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/markerly.png
layout: provider
modified: '2026-08-12'
name: Markerly
nav: Providers
network: true
overview: 'Markerly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Influencer Marketing, Marketing, Creator Economy, and Advertising.


  Markerly''s developer surface includes engineering blog, support, signup flow, authentication, and 13 more developer resources.'
plans:
- name: Markerly Plans Pricing
  plan_count: 0
  slug: markerly-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Markerly Rate Limits
  slug: markerly-rate-limits
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 27.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/markerly/refs/heads/main/screenshots/markerly-2026-07-25T230243.png
security:
- kind: authentication
  name: Markerly Authentication
  slug: markerly-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Markerly Domain Security
  slug: markerly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: markerly
tags:
- Company
- Influencer Marketing
- Marketing
- Creator Economy
- Advertising
- Social-Media
- Advocacy
- Media Processing
- Public Sector
website: https://markerly.com
---
