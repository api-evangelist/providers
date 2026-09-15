---
agent_readiness:
  band: agent-ready
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-09-14'
api_count: 2
apis:
- description: Pearson's named API program. Historically served the LearningStudio RESTful Course APIs, the SOAP SIS APIs, an eventing surface and a Financial Times Education API via api.pearson.com. The platform wa
  name: Pearson Developers Network
  slug: pearson-developers-network
- description: The integration surface Pearson VUE offers test owners for candidate registration, scheduling and results delivery. ws.pearsonvue.com resolves and is a live Azure API Management gateway, answering unk
  name: Pearson VUE Web Services
  slug: pearson-vue-web-services
artifact_total: 8
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pearson/refs/heads/main/security/pearson-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pearson-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pearson/refs/heads/main/well-known/pearson-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pearson-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pearson/refs/heads/main/authentication/pearson-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pearson-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pearson/refs/heads/main/scopes/pearson-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/pearson-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pearson/refs/heads/main/conformance/pearson-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pearson-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pearson/refs/heads/main/lifecycle/pearson-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pearson-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pearson.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pearson/refs/heads/main/security/pearson-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pearson-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.pearson.com/en-us/legal-information/our-policies/responsible-security-disclosure-policy.html
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pearson/refs/heads/main/packages/pearson-packages.yml
  title: ''
  type: Packages
  url: packages/pearson-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pearson/refs/heads/main/llms/pearson-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pearson-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pearson/refs/heads/main/plans/pearson-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pearson-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pearson/refs/heads/main/rate-limits/pearson-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pearson-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.pearson.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pearson.com/en-us/higher-education/educators/digital-learning-platforms/lms-integration-services.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PearsonDevelopersNetwork
- group: operate
  title: ''
  type: Support
  url: https://support.pearson.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pearson.com/en-us/higher-education/insights-and-events/teaching-and-learning-blog.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pearson.com/en-us/legal-information/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pearson.com/en-us/legal-information/privacy-policy.html
- group: start
  title: ''
  type: Login
  url: https://developer.pearson.com/login
- group: company
  title: ''
  type: Website
  url: https://www.pearson.com/
coverage:
  checked: '2026-09-13'
  detail: Every path on developer.pearson.com — the Pearson Developers Network, including the LearningStudio API reference, the available-APIs index and the authentication guide — answers HTTP 401 and SAML-redirects into Pearson's corporate Entra ID tenant and a Salesforce Experience Cloud community, while the program's gateway api.pearson.com returns 403 "We apologize, you have reached a service that has been moved."
  evidence:
  - status: 401
    url: https://developer.pearson.com/learningstudio/available-apis
  - status: 401
    url: https://developer.pearson.com/openapi.json
  - status: 403
    url: https://api.pearson.com/openapi.json
  - status: 500
    url: https://ws.pearsonvue.com/
  - status: 200
    url: https://developer.pearson.com/.well-known/openid-configuration
  reason: partner-login
  state: gated
created: '2026-09-13'
description: 'Pearson plc is the world''s largest learning company, operating courseware and assessment platforms (MyLab, Mastering, Revel, Pearson+, Learning Catalytics), UK and international qualifications (Edexcel, BTEC), clinical and school assessment businesses, Pearson Virtual Schools, English language learning, and Pearson VUE, the computer-based certification and licensure testing network. Pearson once ran a substantial public API program — the Pearson Developers Network, with RESTful LearningStudio Course APIs, SOAP SIS APIs, an eventing surface and first-party client libraries in five languages. That program is retired and closed: LearningStudio ended in 2018, eCollege shut down in 2023, api.pearson.com answers "service that has been moved", and developer.pearson.com returns 401 behind a Salesforce community. What remains public is an OIDC discovery document, a live status page, a security disclosure policy, LTI 1.3 guidance, and three retired SIS WSDLs.'
image: https://www.pearson.com/media_11f626a45563a855db4c129c4851356069ff52ec8.png?width=1200&format=pjpg&optimize=medium
layout: provider
modified: '2026-09-13'
name: Pearson
nav: Providers
network: true
overview: 'Pearson publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Learning, Assessment, Certification, and Publishing.


  Pearson''s developer surface includes authentication, documentation, support, engineering blog, and 18 more developer resources.'
plans:
- name: Pearson Plans Pricing
  plan_count: 0
  slug: pearson-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Pearson Rate Limits
  slug: pearson-rate-limits
scopes:
- name: Pearson Scopes
  scope_count: 0
  slug: pearson-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 25.0
    discoverability: 68.5
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 68.5
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pearson Authentication
  slug: pearson-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pearson Domain Security
  slug: pearson-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pearson Vulnerability Disclosure
  slug: pearson-vulnerability-disclosure
  summary_line: Hackerone
slug: pearson
tags:
- Education
- Learning
- Assessment
- Certification
- Publishing
- EdTech
- Qualifications
- Testing
- Learning Management
- Workforce Skills
website: https://www.pearson.com/
---
