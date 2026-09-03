---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 17.6
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prompt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prompthealth.com/
- group: other
  title: ''
  type: Company
  url: https://www.prompthealth.com/company
- group: operate
  title: ''
  type: Support
  url: https://www.prompthealth.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.prompthealth.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.prompthealth.com/resources/topic/product-updates
- group: operate
  title: ''
  type: StatusPage
  url: https://status.promptemr.com/
- group: start
  title: ''
  type: Login
  url: https://go.promptemr.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prompthealth.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prompthealth.com/legal/privacy-policy
- group: operate
  title: ''
  type: FAQ
  url: https://www.prompthealth.com/faq
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prompt-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prompt-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/prompt-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/prompt-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/prompt-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/prompt-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prompt-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/prompt-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prompt-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/prompt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prompt-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/prompt-packages.yml
coverage:
  checked: '2026-08-26'
  detail: 'Prompt ships rehab-therapy EMR software only as an end-user product: a full walk of its 356-URL sitemap returns no developer, API, integration-docs or reference page, api./developers./docs. subdomains on both promptemr.com and prompthealth.com do not resolve in DNS, and the only machine-readable document served on any host it controls is the OpenID Connect discovery metadata for the application login at authenticate.promptemr.com.'
  evidence:
  - status: 200
    url: https://www.prompthealth.com/sitemap.xml
  - status: 404
    url: https://www.prompthealth.com/openapi.json
  - status: 404
    url: https://www.prompthealth.com/.well-known/api-catalog
  - status: 200
    url: https://authenticate.promptemr.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Prompt (formerly Prompt Therapy Solutions / Prompt EMR, rebranded Prompt Health in June 2025) is a cloud-based, AI-assisted electronic medical record and practice-management platform built exclusively for outpatient rehabilitation therapy — physical therapy, occupational therapy, speech-language pathology, pediatric therapy and chiropractic. Founded in 2017 in Hoboken, New Jersey by Mike Dwyer and Adam Baliatico, with its first product launched in 2019, the platform unifies scheduling, clinical documentation, billing and claims, patient engagement, analytics and compliance in a single system, and is extended by the Sidekick (AI scribing), Insight (compliance analytics), Plus (scheduling automation), Engage (patient app), Kiosk (self check-in), Compensation and RCM modules. Prompt reports use by 1,000+ United States outpatient rehab and musculoskeletal practices. As of this profile the company publishes no public developer program: no API reference, OpenAPI/GraphQL contract,
  SDK or webhook catalog is reachable on any host it controls. The only machine-readable surface it serves publicly is the OpenID Connect discovery document for the application identity provider at authenticate.promptemr.com, plus an llms.txt written for AI assistants.'
image: https://cdn.prod.website-files.com/663e8ac23e061e4b80b016d0/67a6825f2013c062c6bd73ae_7c74bf9fc7e6e57d9f6d7e619f90bfb9_prompt-home-og.png
layout: provider
modified: '2026-08-26'
name: Prompt
nav: Providers
network: true
overview: 'Prompt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Electronic Medical Records, Practice Management, and Physical Therapy.


  Prompt''s developer surface includes support, engineering blog, changelog, FAQ, authentication, and 18 more developer resources.'
plans:
- name: Prompt Plans Pricing
  plan_count: 0
  slug: prompt-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Prompt Rate Limits
  slug: prompt-rate-limits
scopes:
- name: Prompt Scopes
  scope_count: 0
  slug: prompt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 27.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 60.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prompt/refs/heads/main/screenshots/prompt-2026-09-02T152148.png
security:
- kind: authentication
  name: Prompt Authentication
  slug: prompt-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Prompt Domain Security
  slug: prompt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prompt
tags:
- Company
- Healthcare
- Electronic Medical Records
- Practice Management
- Physical Therapy
- Rehabilitation Therapy
- Health IT
- Medical Billing
- Patient Engagement
- Artificial Intelligence
website: https://www.prompthealth.com/
---
