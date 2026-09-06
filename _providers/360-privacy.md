---
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/360-privacy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://360privacy.io/
- group: company
  title: ''
  type: About
  url: https://360privacy.io/company/
- group: company
  title: ''
  type: Blog
  url: https://360privacy.io/articles/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://360privacy.io/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://360privacy.io/terms-conditions/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/360privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/360-privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/360-privacy-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/360-privacy-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/360-privacy-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/360-privacy-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/360-privacy-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/360-privacy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/360-privacy-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: '360 Privacy sells analyst-led data removal as a managed service, not as software an integrator calls: api. and developer. subdomains do not resolve, /openapi.json 404s on the marketing site, the site''s own llms.txt indexes only marketing pages with no developer section, and the single docs host docs.360privacy.io is a GitBook knowledge base for the customer dashboard sealed behind GitBook Visitor Auth into the company Auth0 tenant.'
  evidence:
  - status: 404
    url: https://360privacy.io/openapi.json
  - status: 307
    url: https://docs.360privacy.io/
  - status: 200
    url: https://360privacy.io/llms.txt
  - status: 200
    url: https://auth.360privacy.io/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 360 Privacy is a Nashville, Tennessee based digital executive protection company, founded in 2019, that reduces the online exposure of executives, public figures, athletes and their families. Its analyst-led platform pairs proprietary technology with human intelligence to locate and delete personally identifiable information from data broker and people-search sites (360 Delete), to scan the deep and dark web for compromised credentials and exposed PII (360 Monitor), and to provide continuous monitoring with hands-on threat response for high-risk individuals (360 Defend). The product is delivered as a managed service through an authenticated customer dashboard; as of this profile the company publishes no public developer program, API reference or machine-readable contract.
image: https://360privacy.io/wp-content/uploads/2026/05/WHITE_PRIMARY-scaled.jpg
layout: provider
modified: '2026-09-05'
name: 360 Privacy
nav: Providers
network: true
overview: '360 Privacy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Privacy, Data Removal, Executive Protection, and Cybersecurity.


  360 Privacy''s developer surface includes engineering blog, authentication, and 13 more developer resources.'
plans:
- name: 360 Privacy Plans Pricing
  plan_count: 0
  slug: 360-privacy-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: 360 Privacy Rate Limits
  slug: 360-privacy-rate-limits
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 360 Privacy Authentication
  slug: 360-privacy-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: 360 Privacy Domain Security
  slug: 360-privacy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: 360 Privacy Trust Center
  slug: 360-privacy-trust-center
  summary_line: trust center published
slug: 360-privacy
tags:
- Company
- Privacy
- Data Removal
- Executive Protection
- Cybersecurity
- Threat Intelligence
- Dark Web Monitoring
- Personal Data
- Managed Services
website: https://360privacy.io/
---
